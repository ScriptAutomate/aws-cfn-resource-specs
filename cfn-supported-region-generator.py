import json
from pathlib import Path

# Third-Party modules
import requests
from git import Repo

def valid_doc_link_check(doc_type, key, url, source_dict):
    # Broken doc links default redirect to UserGuide main page
    if requests.get(url).url == "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/":
        source_dict[doc_type]["BrokenDocLinks"][key] = url


def valid_md_file_check(doc_type, key, url, source_dict):
    source_repo_local = "aws-cloudformation-user-guide/doc_source"
    source_repo_online = "https://github.com/awsdocs/aws-cloudformation-user-guide/tree/master/doc_source"
    url_prefix = "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/"
    md_file = url.replace(url_prefix,"").replace(".html",".md")
    if not Path.cwd().joinpath(f"{source_repo_local}/{md_file}").exists():
        source_dict[doc_type]["MissingFromAWSGitHubSourceRepo"][key] = f"{source_repo_online}/{md_file}"


cfn_json = 'CloudFormationResourceSpecification.json'
resource_spec_dir = 'specs'

# Dependent on latest documentation
Repo.clone_from("https://github.com/awsdocs/aws-cloudformation-user-guide.git","aws-cloudformation-user-guide")
if Path.cwd().joinpath(f"{resource_spec_dir}/regions.json").exists():
    with open(f"{resource_spec_dir}/regions.json", 'r') as file_to_read:
        regions_data = json.loads(file_to_read.read())
        regions = []
        for key in regions_data.keys():
            regions.append(key)
        regions_data = None

# Find resource spec with most supported resources
resource_count = {}
for region in regions:
    target_cfn = Path.cwd().joinpath(f"{resource_spec_dir}/{region}/{cfn_json}")
    with target_cfn.open('r') as cfn_content:
        json_contents = json.loads(cfn_content.read())
        resource_count[region] = len(json_contents["ResourceTypes"].keys()) + len(json_contents["PropertyTypes"].keys())
master_resource_spec = max(resource_count, key=lambda key: resource_count[key])

# Create base master resource dictionary
supported_resources = {
    "ResourceTypes" : {},
    "PropertyTypes" : {}
}

# Create base master documentation lookup dictionary
documentation_lookup = {
    "ResourceTypes" : {
        "MissingDocLinks" : [],
        "BrokenDocLinks" : {},
        "MissingFromAWSGitHubSourceRepo" : {}
    },
    "PropertyTypes" : {
        "MissingDocLinks" : [],
        "BrokenDocLinks" : {},
        "MissingFromAWSGitHubSourceRepo" : {}
    }
}

total_lookups = resource_count[master_resource_spec]
current_lookup = 0
with Path.cwd().joinpath(f"{resource_spec_dir}/{master_resource_spec}/{cfn_json}").open('r') as master_file:
    json_contents = json.loads(master_file.read())
    resource_spec_version = json_contents["ResourceSpecificationVersion"]
    for key, value in json_contents["ResourceTypes"].items():
        current_lookup += 1
        percentage_done = int(current_lookup / total_lookups * 100)
        supported_resources["ResourceTypes"][key] = {
            "Regions" : [
                master_resource_spec
            ]
        }
        if value.get("Documentation"):
            supported_resources["ResourceTypes"][key]["Documentation"] = value["Documentation"]
            print(f"{percentage_done}% Complete: [ResourceType] Looking up documentation: {key}")
            valid_doc_link_check(
                "ResourceTypes",
                key,
                value["Documentation"],
                documentation_lookup
            )
            valid_md_file_check(
                "ResourceTypes",
                key,
                value["Documentation"],
                documentation_lookup
            )
        else:
            print(f"{percentage_done}% Complete: [WARNING][{key}] No Documentation link")
            supported_resources["ResourceTypes"][key]["Documentation"] = ""
            documentation_lookup["ResourceTypes"]["MissingDocLinks"].append(key)
    for key, value in json_contents["PropertyTypes"].items():
        current_lookup += 1
        percentage_done = int(current_lookup / total_lookups * 100)
        supported_resources["PropertyTypes"][key] = {
            "Regions" : [
                master_resource_spec
            ]
        }
        if value.get("Documentation"):
            supported_resources["PropertyTypes"][key]["Documentation"] = value["Documentation"]
            print(f"{percentage_done}% Complete: [PropertyType] Looking up documentation: {key}")
            valid_doc_link_check(
                "PropertyTypes",
                key,
                value["Documentation"],
                documentation_lookup
            )
            valid_md_file_check(
                "PropertyTypes",
                key,
                value["Documentation"],
                documentation_lookup
            )
        else:
            print(f"{percentage_done}% Complete: [WARNING][{key}] No Documentation link")
            supported_resources["PropertyTypes"][key]["Documentation"] = ""
            documentation_lookup["PropertyTypes"]["MissingDocLinks"].append(key)

# Cycle through rest of regions to check for support
for region in regions:
    if region is not master_resource_spec:
        target_cfn = Path.cwd().joinpath(f"{resource_spec_dir}/{region}/{cfn_json}")
        with target_cfn.open('r') as cfn_content:
            json_contents = json.loads(cfn_content.read())
            for key in json_contents["ResourceTypes"].keys():
                if supported_resources["ResourceTypes"].get(key):
                    supported_resources["ResourceTypes"][key]["Regions"].append(region)
                else:
                    supported_resources["ResourceTypes"][key] = {
                        "Regions" : [
                            region
                        ]
                    }
                    if json_contents["ResourceTypes"][key].get("Documentation"):
                        supported_resources["ResourceTypes"][key]["Documentation"] = json_contents["ResourceTypes"][key]["Documentation"]
                        print(f"[ResourceType] Looking up documentation: {key}")
                        valid_doc_link_check(
                            "ResourceTypes",
                            key,
                            json_contents["ResourceTypes"][key]["Documentation"],
                            documentation_lookup
                        )
                        valid_md_file_check(
                            "ResourceTypes",
                            key,
                            json_contents["ResourceTypes"][key]["Documentation"],
                            documentation_lookup
                        )
                    else:
                        print(f"[WARNING][{key}] No Documentation link")
                        supported_resources["ResourceTypes"][key]["Documentation"] = ""
                        documentation_lookup["ResourceTypes"]["MissingDocLinks"].append(key)
            for key in json_contents["PropertyTypes"].keys():
                if supported_resources["PropertyTypes"].get(key):
                    supported_resources["PropertyTypes"][key]["Regions"].append(region)
                else:
                    supported_resources["PropertyTypes"][key] = {
                        "Regions" : [
                            region
                        ]
                    }
                    if json_contents["PropertyTypes"][key].get("Documentation"):
                        supported_resources["PropertyTypes"][key]["Documentation"] = json_contents["PropertyTypes"][key]["Documentation"]
                        print(f"[PropertyType] Looking up documentation: {key}")
                        valid_doc_link_check(
                            "PropertyTypes",
                            key,
                            json_contents["PropertyTypes"][key]["Documentation"],
                            documentation_lookup
                        )
                        valid_md_file_check(
                            "PropertyTypes",
                            key,
                            json_contents["PropertyTypes"][key]["Documentation"],
                            documentation_lookup
                        )
                    else:
                        print(f"[WARNING][{key}] No Documentation link")
                        supported_resources["PropertyTypes"][key]["Documentation"] = ""
                        documentation_lookup["PropertyTypes"]["MissingDocLinks"].append(key)


# Reduce list to "all" if every region has resource supported
global_resources = 0
supported_resources["TypesNotInUSEAST1"] = {
    "Total": 0,
    "ResourceTypes": {},
    "PropertyTypes": {} 
}
for key in supported_resources["ResourceTypes"].keys():
    if len(supported_resources["ResourceTypes"][key]["Regions"]) == len(regions):
        supported_resources["ResourceTypes"][key]["AllRegions"] = True
        global_resources += 1
    else:
        supported_resources["ResourceTypes"][key]["AllRegions"] = False
        if "us-east-1" not in supported_resources["ResourceTypes"][key]["Regions"]:
            supported_resources["TypesNotInUSEAST1"]["Total"] += 1
            supported_resources["TypesNotInUSEAST1"]["ResourceTypes"][key] = {"Regions": supported_resources["ResourceTypes"][key]["Regions"]}

# Reduce list to "all" if every region has property supported
global_properties = 0
for key in supported_resources["PropertyTypes"].keys():
    if len(supported_resources["PropertyTypes"][key]["Regions"]) == len(regions):
        supported_resources["PropertyTypes"][key]["AllRegions"] = True
        global_properties += 1
    else:
        supported_resources["PropertyTypes"][key]["AllRegions"] = False
        if "us-east-1" not in supported_resources["PropertyTypes"][key]["Regions"]:
            supported_resources["TypesNotInUSEAST1"]["Total"] += 1
            supported_resources["TypesNotInUSEAST1"]["PropertyTypes"][key] = {"Regions": supported_resources["PropertyTypes"][key]["Regions"]}

# Add counters
supported_resources["TotalPropertyTypes"] = len(supported_resources["PropertyTypes"].keys())
supported_resources["TotalResourceTypes"] = len(supported_resources["ResourceTypes"].keys())
supported_resources["TotalPropertyTypesSupportedGlobally"] = global_properties
supported_resources["TotalResourceTypesSupportedGlobally"] = global_resources
supported_resources["ResourceSpecificationVersion"] = resource_spec_version
documentation_lookup["ResourceSpecificationVersion"] = resource_spec_version

# Dump sorted results
with open(f"{resource_spec_dir}/supported-regions-per-resource.json", 'w') as file_to_dump:
    json.dump(supported_resources, file_to_dump, indent=2, sort_keys=True)

# Dump sorted results
with open(f"{resource_spec_dir}/documentation-lookup-errors.json", 'w') as file_to_dump:
    json.dump(documentation_lookup, file_to_dump, indent=2, sort_keys=True)
