import json
from gzip import GzipFile
import os
from datetime import date
from pathlib import Path
from distutils.version import StrictVersion

# Third-Party modules
import requests
import git
from github import Github
from packaging import version
from boto3 import client, resource


def resource_spec_versions(cfn_resource_spec_bucket):
    '''Return all available versions of a CFN Resource Specification file'''
    versions = set()
    # Create a client
    conn = client('s3', region_name='us-east-1')
    # Create a reusable Paginator
    paginator = conn.get_paginator('list_objects')
    # Create a PageIterator from the Paginator
    page_iterator = paginator.paginate(Bucket=cfn_resource_spec_bucket)
    for page in page_iterator:
        for key in page['Contents']:
            prefix,file = key['Key'].split('/',1)
            versions.add(prefix)
    return versions


def resource_spec_date(version, cfn_resource_spec_bucket, cfn_json):
    '''Find the release date (last modified timestamp) of a CFN Resource Specification file'''
    key = version + '/gzip/' + cfn_json
    s3 = resource('s3',region_name='us-east-1')
    obj = s3.Object(cfn_resource_spec_bucket, key)
    return str(obj.last_modified.date())


def resource_download(resource_spec_dir, version, region_name, cfn_resource_spec_bucket, cfn_json, standard=True):
    '''Download a CFN Resource Specification file'''
    key = version + '/gzip/' + cfn_json
    if standard:
        resource('s3',region_name='us-east-1').Bucket(cfn_resource_spec_bucket).download_file(key, f"{resource_spec_dir}/{region_name}/{cfn_json}")
    else:
        extension = 'com'
        if region_name.startswith('cn'):
            extension += '.cn'
        url = f"https://{cfn_resource_spec_bucket}.s3.{region_name}.amazonaws.{extension}/{version}/gzip/{cfn_json}"
        print(f"[INFO][{region_name}][DOWNLOADING]Latest resource spec")
        cfn_request = requests.get(url)
        print(f"[INFO][{region_name}][DOWNLOADED]Latest resource spec")
        with open(f"{resource_spec_dir}/{region_name}/{cfn_json}", 'wb') as cfn_download:
            cfn_download.write(cfn_request.content)
        
    return Path.cwd().joinpath(f"{resource_spec_dir}/{region_name}/{cfn_json}")


def resource_json_sort_keys(resource_json_file_path, gzipped = True):
    # Open JSON
    if gzipped:
        with GzipFile(resource_json_file_path, 'r') as file_to_read:
            json_contents = json.loads(file_to_read.read().decode('utf-8'))
    else:
        with open(resource_json_file_path, 'r') as file_to_read:
            json_contents = json.loads(file_to_read.read())
    # Rewrite downloaded JSON with sorted keys for proper git diff generation
    with open(resource_json_file_path, 'w') as file_to_dump:
        json.dump(json_contents, file_to_dump, indent=2, sort_keys=True)


resource_spec_dir = 'specs'
cfn_json = 'CloudFormationResourceSpecification.json'
debugging = False

if Path.cwd().joinpath("regions.json").exists():
    with open(Path.cwd().joinpath("regions.json"), 'r') as file_to_read:
        regions_data = json.loads(file_to_read.read())
        supported_regions = []
        oddballs = []
        for key, value in regions_data.items():
            supported_regions.append(key)
            if value["normal_s3_download"] == False:
                oddballs.append(key)
        regions_data = None

if Path.cwd().joinpath("all-cfn-versions.json").exists():
    with open(Path.cwd().joinpath("all-cfn-versions.json"), 'r') as file_to_read:
        region_details_old = json.loads(file_to_read.read())
else:
    region_details_old = {}

region_details={}
version_master=[]
updated_regions=[]
for region_name in supported_regions:
    print(f"[INFO][{region_name}][SEARCHING]Querying for new versions")
    Path.mkdir(Path.cwd().joinpath(f"{resource_spec_dir}/{region_name}"),exist_ok=True)
    cfn_resource_spec_bucket=f"cfn-resource-specifications-{region_name}-prod"
    if region_name not in oddballs:
        cfn_resources = resource_spec_versions(
            cfn_resource_spec_bucket
        )
        sorted_resources = list(cfn_resources)
        sorted_resources.sort()
        current_version = Path.cwd().joinpath(f"{resource_spec_dir}/{region_name}/{cfn_json}")
        new_version_available = False
        if current_version.exists():
            with current_version.open('r') as cfn_content:
                json_contents = json.loads(cfn_content.read())
                old_version = json_contents['ResourceSpecificationVersion']
            if sorted_resources[-2] != old_version:
                new_version_available = True
        else:
            new_version_available = True
        if new_version_available:
            for version in sorted_resources[:-1]:
                if (not region_details_old.get(region_name) or not region_details_old[region_name].get(version)) and version != 'latest':
                    spec_date = resource_spec_date(
                        version, cfn_resource_spec_bucket, cfn_json
                    )
                    if region_details_old.get(region_name) and region_details_old[region_name].get(version) and region_details_old[region_name][version] == spec_date:
                        break
                    print(f"[INFO][{region_name}][DISCOVERED]New Resource Spec: {version} - {spec_date}")
                    if region_details.get(region_name): 
                        region_details[region_name][version] = spec_date
                    else:
                        region_details[region_name] = {version : spec_date}
                    if version not in version_master and version != 'latest':
                        version_master.append(version)
                    if region_name not in updated_regions:
                        updated_regions.append(region_name)
    else:
        current_version = Path.cwd().joinpath(f"{resource_spec_dir}/{region_name}/{cfn_json}")
        if current_version.exists():
            with current_version.open('r') as cfn_content:
                json_contents = json.loads(cfn_content.read())
                old_version = json_contents['ResourceSpecificationVersion']
        else:
            old_version = None
        downloaded_cfn = resource_download(
            resource_spec_dir, 'latest', region_name, cfn_resource_spec_bucket, cfn_json, False
        )
        # Sort keys in downloaded JSON
        resource_json_sort_keys(downloaded_cfn, False)
        with downloaded_cfn.open('r') as cfn_content:
            json_contents = json.loads(cfn_content.read())
            new_version = json_contents['ResourceSpecificationVersion']
        if new_version != old_version and new_version != 'latest':
            if new_version not in version_master:
                version_master.append(new_version)
            spec_date = None
            if region_details_old.get(supported_regions[0]):
                spec_date = region_details_old[supported_regions[0]].get(new_version)
            #if not spec_date:
            #    spec_date = region_details['us-east-1'].get(new_version)
            if not spec_date:
                spec_date = f"{date.today():%Y-%m-%d}"
            print(f"[INFO][{region_name}][DISCOVERED]New resource spec: {new_version} - {spec_date}")
            region_details[region_name] = {new_version : spec_date}
            updated_regions.append(region_name)
        else:
            print(f"[INFO][{region_name}][NO_CHANGE]Latest oddball resource spec: {new_version} is unchanged")

# Sort versions based on semantic versioning
version_master.sort(key=StrictVersion)

if updated_regions:
    repo = git.Repo(f"{Path.cwd()}") # git repo base info
    if not debugging:
        git_email = os.environ['GITHUB_ACTOR'] + '@users.noreply.github.com'
        git_name = os.environ['GITHUB_ACTOR']
        github_repo = os.environ['GITHUB_REPOSITORY']
        github_token = os.environ['GITHUB_TOKEN']
        repo.git.config('--global', 'user.email', f"{git_email}")
        repo.git.config('--global', 'user.name', f"{git_name}")
    for version in version_master:
        index = repo.index # current git head
        changes_to_commit = []
        for region_name in updated_regions:
            included_regions = []
            for version_key,date_value in region_details[region_name].items():
                if version_key == version:
                    if region_name not in oddballs:
                        cfn_resource_spec_bucket=f"cfn-resource-specifications-{region_name}-prod"
                        downloaded_cfn = resource_download(
                            resource_spec_dir, version_key, region_name, cfn_resource_spec_bucket, cfn_json
                        )
                        # Sort keys in downloaded JSON
                        resource_json_sort_keys(downloaded_cfn)
                        print(f"[INFO][UPDATED]New Resource Spec for {region_name}: {version_key}")
                    else:
                        print(f"[INFO][UPDATED]New Resource Spec for {region_name}: {version_key}")
                    changes_to_commit.append(f"{resource_spec_dir}/{region_name}/{cfn_json}")
                    if not region_details_old.get(region_name):
                        region_details_old[region_name] = {version: date_value, 'latest': version}
                    else:
                        region_details_old[region_name][version] = date_value
                        region_details_old[region_name]['latest'] = version
                    commit_date_note = date_value
                    break
        # Push all updated files of a particular version to Git repository
        #  with commit message and git tag of ResourceSpecificationVersion
        index.add(changes_to_commit) # git add
        if f"v{version}" not in [str(old_tag) for old_tag in repo.tags]:
            index.commit(f"Version {version} {commit_date_note}") # git commit
            new_tag = repo.create_tag(f"v{version}", message="New CFN Resource Spec release")
        else:
            index.commit(f"Version {version} {commit_date_note}") # git commit
            new_tag = repo.create_tag(f"v{version}", force=True, message="New CFN Resource Spec release")
        if debugging:
            origin = repo.remotes[0]
            origin.push()
        else:
            repo.git.config('--global', 'user.email', f"{git_email}")
            repo.git.config('--global', 'user.name', f"{git_name}")
            repo.git.remote('set-url', 'origin', "https://x-access-token:%s@github.com/%s" % (github_token, github_repo))
            #repo.git.push('-f', 'origin', 'master')
            #repo.git.tag('-a',f"v{version}", '-m', "New CFN Resource Spec release")
            #repo.git.push('-f', 'origin', f"v{version}")
            origin = repo.remotes[0]
            origin.push()
            origin.push(new_tag)
        
    # Lastly, update the all-cfn-version.json with latest info
    with open("all-cfn-versions.json", 'w') as file_to_dump:
        json.dump(region_details_old, file_to_dump, indent=2, sort_keys=True)

    # Update all-cfn-versions.json
    index.add(["all-cfn-versions.json"]) # git add
    index.commit(f"Latest Version {version_master[-1]}-{date.today():%Y%m%d} {commit_date_note}") # git commit
    origin.push() # git push
