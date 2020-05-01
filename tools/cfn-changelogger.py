import json
from pathlib import Path


def compare_regions(new_list_type, old_list_type):
    expanded_regions = list(set(new_list_type["Regions"]) - set(old_list_type["Regions"]))
    reduced_regions = list(set(old_list_type["Regions"]) - set(new_list_type["Regions"]))
    if expanded_regions or reduced_regions:
        if new_list_type["AllRegions"] == True:
            return {'Expanded': expanded_regions, 'AllRegions': True}
        else:
            return {'Expanded': expanded_regions, 'Reduced': reduced_regions, 'AllRegions': False}
    else:
        return None


changelog = {
    "PropertyTypes" : {},
    "ResourceTypes" : {},
    "Totals": {},
    "TypesNotInUSEAST1": {"ResourceTypes": {}, "PropertyTypes": {}}
}

totals = [
    "TotalPropertyTypes",
    "TotalPropertyTypesSupportedGlobally",
    "TotalResourceTypes",
    "TotalResourceTypesSupportedGlobally"
]

# Import old
with open('supported-regions-per-resource-old.json', 'r') as file_to_read:
    supported_old = json.loads(file_to_read.read())

# Import new
with open('supported-regions-per-resource.json', 'r') as file_to_read:
    supported_new = json.loads(file_to_read.read())

if supported_new["ResourceSpecificationVersion"] == supported_old["ResourceSpecificationVersion"]:
    print("No new version.")
    exit()

# Change = [increase, decrease]
for total in totals:
    changelog["Totals"][total] = {"Value": supported_new[total], "Change": [supported_new[total] - supported_old[total]]}
changelog["TypesNotInUSEAST1"]["Total"] = {"Value": supported_new["TypesNotInUSEAST1"]["Total"], "Change": [0,0]}
changelog["ResourceSpecificationVersionOld"] = supported_old["ResourceSpecificationVersion"]

for each_type in ["ResourceTypes", "PropertyTypes"]:
    for resource in supported_new[each_type].keys():
        # Check for change in regions for existing types
        if supported_old[each_type].get(resource):
            diff = compare_regions(supported_new[each_type][resource], supported_old[each_type][resource])
            if diff:
                diff["Type"] = 'Existing'
                diff["Documentation"] = supported_new[each_type][resource]["Documentation"]
                changelog[each_type][resource] = diff
        # Or is entirely new type
        else:
            changelog[each_type][resource] =  {
                "Type": "New",
                "AllRegions": supported_new[each_type][resource]["AllRegions"],
                "Regions": supported_new[each_type][resource]["Regions"],
                "Documentation": supported_new[each_type][resource]["Documentation"]
            }
    # Types found entirely deleted
    for resource in supported_old[each_type].keys():
        if resource not in supported_new[each_type].keys():
            changelog[each_type][resource] =  {
                "Type": "Deleted",
                "Regions": supported_old[each_type][resource]["Regions"],
                "Documentation": supported_old[each_type][resource]["Documentation"]
            }
    # "TypesNotInUSEAST1" types either still missing or newly missing
    for resource in supported_new["TypesNotInUSEAST1"][each_type].keys():
        if supported_old[each_type].get(resource):
            changelog["TypesNotInUSEAST1"][each_type][resource] = {
                "Since": supported_old["ResourceSpecificationVersion"],
                "Fixed": False,
                "Regions": supported_new["TypesNotInUSEAST1"][each_type][resource]["Regions"],
                "Documentation": supported_new[each_type][resource]["Documentation"]
            }
        else:
            changelog["TypesNotInUSEAST1"][each_type][resource] = {
                "Since": supported_new["ResourceSpecificationVersion"],
                "Fixed": False,
                "Regions": supported_new["TypesNotInUSEAST1"][each_type][resource]["Regions"],
                "Documentation": supported_new[each_type][resource]["Documentation"]
            }
            changelog["TypesNotInUSEAST1"]["Total"]["Change"][0] += 1
    # "TypesNotInUSEAST1" types no longer missing in latest version
    for resource in supported_old["TypesNotInUSEAST1"][each_type].keys():
        if not supported_new["TypesNotInUSEAST1"][each_type].get(resource):
            changelog["TypesNotInUSEAST1"][each_type][resource] = {
                "Since": supported_old["TypesNotInUSEAST1"][each_type][resource]["Since"],
                "Fixed": True,
                "Documentation": supported_old[each_type][resource]["Documentation"]
            }
            changelog["TypesNotInUSEAST1"]["Total"]["Change"][1] += 1


changelog_major_version = supported_new["ResourceSpecificationVersion"].split('.')[0]
target_json = Path(f"changelogs/v{changelog_major_version}-changelog.json")

# Check if existing changelog
if target_json.exists():
    with open(target_json, 'r') as file_to_read:
        current_changelog = json.loads(file_to_read.read())
    current_changelog[supported_new["ResourceSpecificationVersion"]] = changelog
else:
    current_changelog = {supported_new["ResourceSpecificationVersion"]: changelog}

# Write changelog
with open(target_json, 'w') as file_to_dump:
    json.dump(current_changelog, file_to_dump, indent=2, sort_keys=True)