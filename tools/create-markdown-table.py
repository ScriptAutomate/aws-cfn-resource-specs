'''
Print MarkDown Table for GitHub
  Issue in aws-cloudformation-user-guide
'''
import json
from pathlib import Path

with open(Path.cwd().joinpath("documentation-broken-links-detailed.json"), 'r') as file_to_read:
    broken_docs = json.loads(file_to_read.read())

issues = {
    'ResourceTypes': {},
    'PropertyTypes': {},
    'ResourceSpecificationVersion': broken_docs['ResourceSpecificationVersion']
}

print('|Resource|DaysBrokenAtLeast|Error|')
print('|---|---|---|')
for spec_type in ['ResourceTypes','PropertyTypes']:
    for key, value in broken_docs[spec_type].items():
        if value:
            for resource, info in value.items():
                if info['DaysBrokenAtLeast'] > 14:
                    if not issues[spec_type].get(key):
                        issues[spec_type][key] = {}
                    issues[spec_type][key][resource] = broken_docs[spec_type][key][resource]
                    print(f"|{resource}|{info['DaysBrokenAtLeast']}|{key}|")
