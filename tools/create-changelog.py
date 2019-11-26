import json
import shutil
from pathlib import Path
from distutils.version import StrictVersion


def parse_new_types(release, item_type):
    new_items = []
    if release.get(item_type):
        for key,value in release[item_type].items():
            if value["Type"] == 'New':
                new_items.append(f"- [{key}]({value['Documentation']})\n")
                if value["AllRegions"]:
                    new_items.append(f"  - Available in **ALL** regions.\n")
                else:
                    for region in value["Regions"]:
                        new_items.append(f"  - `{region}`\n")
                new_items[-1] += "\n"            
    
    return new_items


def parse_deleted_types(release, item_type):
    deleted_items = []
    if release.get(item_type):
        for key,value in release[item_type].items():
            if value["Type"] == 'Deleted':
                deleted_items.append(f"- [{key}]({value['Documentation']})\n")
                for region in value["Regions"]:
                    deleted_items.append(f"  - `{region}`\n")
                deleted_items[-1] += "\n"
    
    return deleted_items


def parse_expanded_types(release, item_type):
    expanded_items = []
    if release.get(item_type):
        for key,value in release[item_type].items():
            if value["Type"] == "Existing" and value["Expanded"]:
                expanded_items.append(f"- [{key}]({value['Documentation']})\n")
                if value["AllRegions"]:
                    expanded_items.append(f"  - Now available to **ALL** regions.\n")
                else:
                    for region in value["Expanded"]:
                        expanded_items.append(f"  - `{region}`\n")
                expanded_items[-1] += "\n"
    
    return expanded_items


def parse_reduced_types(release, item_type):
    reduced_items = []
    if release.get(item_type):
        for key,value in release[item_type].items():
            if value.get("Reduced"):
                if value["Type"] == "Existing" and value["Reduced"]:
                    reduced_items.append(f"- [{key}]({value['Documentation']})\n")
                    for region in value["Reduced"]:
                        reduced_items.append(f"  - `{region}`\n")
                    reduced_items[-1] += "\n"
    
    return reduced_items


def parse_useast1_missing_types(release, version, item_type):
    useast1_missing_items = {
        'still_missing': [],
        'newly_missing': [],
        'newly_fixed': []
    }
    results = []
    if release.get(item_type):
        for key,value in release[item_type].items():
            if value["Fixed"] == False:
                if value["Since"] == version:
                    if not useast1_missing_items["newly_missing"]:
                        useast1_missing_items["newly_missing"].append(f"- New {item_type.rstrip('s') + '(s)'} Missing\n")
                    useast1_missing_items["newly_missing"].append(f"  - [{key}]({value['Documentation']})\n")
                    for region in value["Regions"]:
                        useast1_missing_items["newly_missing"].append(f"    - `{region}`\n")
                    useast1_missing_items["newly_missing"][-1] += "\n"
                else:
                    if not useast1_missing_items["still_missing"]:
                        useast1_missing_items["still_missing"].append(f"- {item_type.rstrip('s' + '(s)')} Still Missing\n")
                    useast1_missing_items["still_missing"].append(f"  - Since v{value['Since']}: [{key}]({value['Documentation']})\n")
                    for region in value["Regions"]:
                        useast1_missing_items["still_missing"].append(f"    - `{region}`\n")
                    useast1_missing_items["still_missing"][-1] += "\n"
            else:
                if not useast1_missing_items["newly_fixed"]:
                    useast1_missing_items["newly_fixed"].append(f"- {item_type.rstrip('s') + '(s)'} No Longer Missing\n")
                useast1_missing_items["newly_fixed"].append(f"  - [{key}]({value['Documentation']})\n")
                useast1_missing_items["newly_fixed"].append(f"    - Was missing since v{value['Since']}\n\n")
    for key, value in useast1_missing_items.items():
        if value:
            results.extend(value)
    
    return results


changelog_dir = Path.cwd().joinpath('changelogs')
versions = []
for item in changelog_dir.iterdir():
    if item.suffix == '.json':
        versions.append(item.name.split('-')[0].replace('v',''))

latest_major = max(versions)
changelog_source_file = changelog_dir.joinpath(f"v{latest_major}-changelog.json")
changelog_md_file = changelog_dir.joinpath(f"v{latest_major}-CHANGELOG.md")

totals = [
    "TotalPropertyTypes",
    "TotalPropertyTypesSupportedGlobally",
    "TotalResourceTypes",
    "TotalResourceTypesSupportedGlobally"
]

# Setup changelog header
changelog_markdown = []
changelog_markdown.append("# Changelog\n\n")
changelog_markdown.append(f"This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v{latest_major}-changelog.json`](changelogs/v8-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)\n\n")
changelog_markdown.append("Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.\n\n")
changelog_markdown.append("> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_\n\n")

# Open the source changelog; start with latest version
with open(changelog_source_file, 'r') as source_json:
    changelog_source = json.loads(source_json.read())

release_versions = list(changelog_source.keys())
release_versions.sort(key=StrictVersion, reverse=True)

release_markdown = []
for release in release_versions:
    with open("all-cfn-versions.json", 'r') as source_json:
        version_date = json.loads(source_json.read())['us-east-1'][release]
    
    # Release header
    release_markdown.append(f"## [{release}](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v{release}) ({version_date})\n\n")
    #release_header.append(f"- [Full Git Diff](https://github.com/ScriptAutomate/aws-cfn-resource-specs/commit/{commit_id})\n")
    release_markdown.append(f"- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v{release.split('.')[0]}-changelog.json)\n")
    release_markdown.append(f"  - Change source is a diff between [v{release}](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v{release}) and [v{changelog_source[release]['ResourceSpecificationVersionOld']}](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v{changelog_source[release]['ResourceSpecificationVersionOld']})\n\n")

    # Release totals
    release_markdown.append(f"### Totals\n\n")
    for total in totals:
        release_markdown.append(f"- {total}: {changelog_source[release]['Totals'][total]['Value']} **(+{changelog_source[release]['Totals'][total]['Change'][0]})**\n")
    release_markdown[-1] += "\n"

    main_section = {
        'new_types': ['### Introduction of New ResourceTypes and/or PropertyTypes\n\n'],
        'deleted_types': ['### Complete Removal of ResourceTypes and/or PropertyTypes\n\n'],
        'expanded_types': ['### Existing ResourceTypes and PropertyTypes: Added Regions\n\n'],
        'reduced_types': ['### Existing ResourceTypes and PropertyTypes: Removed Regions\n\n'],
        'useast1_missing': ['### Existing ResourceTypes and PropertyTypes Not in `us-east-1`\n\n'],
    }

    # Generate main release changelog
    item_types = ["ResourceTypes","PropertyTypes"]
    for item_type in item_types:
        main_section['new_types'].extend(parse_new_types(changelog_source[release], item_type))
        main_section['deleted_types'].extend(parse_deleted_types(changelog_source[release], item_type))
        main_section['expanded_types'].extend(parse_expanded_types(changelog_source[release], item_type))
        main_section['reduced_types'].extend(parse_reduced_types(changelog_source[release], item_type))
        main_section['useast1_missing'].extend(parse_useast1_missing_types(changelog_source[release]["TypesNotInUSEAST1"], release, item_type))


    for key, value in main_section.items():
        if len(value) > 1:
            release_markdown.extend(value)


changelog_markdown.extend(release_markdown)
with open(changelog_md_file, 'w') as markdown_writer:
    markdown_writer.writelines(changelog_markdown)

# Copy latest major changelog to repo root
shutil.copy(changelog_md_file,Path.cwd().joinpath('CHANGELOG.md'))