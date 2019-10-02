from pathlib import Path
import json
import re
import mmap

# Tool is meant to be run with: pipenv run python tools/aws-doc-region-updater.py
#   with cwd as repository root
with open(Path.cwd().joinpath("supported-regions-per-resource.json"), 'r') as file_to_read:
    supported_regions = json.loads(file_to_read.read())

# First requires:
# git clone <forked-repo> aws-cloudformation-user-guide-fork
forked_docs = 'aws-cloudformation-user-guide-fork'
spec_types = ['ResourceTypes', 'PropertyTypes']
duplicate_links = []
for key in supported_regions['ResourceTypes'].keys():
    for other_key in supported_regions['PropertyTypes'].keys():
        if supported_regions['ResourceTypes'][key]['Documentation'] == supported_regions['PropertyTypes'][other_key]['Documentation']:
            duplicate_links.append(supported_regions['ResourceTypes'][key]['Documentation'])
for spec_type in spec_types:
    for key in supported_regions[spec_type].keys():
        if supported_regions[spec_type][key]['Documentation'] in duplicate_links:
            spec_type_name = "ResourceType and PropertyType"
        else:
            spec_type_name = spec_type.rstrip('s')
        markdown = re.sub(
            '.*\/',
            '',
            supported_regions[spec_type][key]['Documentation'].replace('.html','.md')
        )
        markdown_path = Path.cwd().joinpath(forked_docs, 'doc_source', markdown)
        if markdown_path.is_file() and markdown_path.exists():
            # Check if file already has Supported Regions header
            new_header = True
            new_lines = ''
            # Reference:
            # https://stackoverflow.com/questions/4940032/how-to-search-for-a-string-in-text-files
            with open(markdown_path, 'rb', 0) as markdown_file, \
                mmap.mmap(markdown_file.fileno(), 0, access=mmap.ACCESS_READ) as content:
                if content.find(b'## Supported Regions') != -1:
                    new_header = False
            # If Supported Regions header does not exist...
            if not new_header:
                # Reference:
                # https://stackoverflow.com/questions/4710067/using-python-for-deleting-a-specific-line-in-a-file
                with open(markdown_path, "r") as input:
                    new_markdown_path = Path.cwd().joinpath(forked_docs, 'doc_source', markdown.replace('.md','.md.new'))
                    with open(new_markdown_path, "w") as output:
                        for line in input:
                            if line.strip("\n") != "## Supported Regions":
                                output.write(line)
                            else:
                                break
                Path(new_markdown_path).replace(markdown_path)
            else:
                new_lines += '\n\n'
            with open(markdown_path, 'a') as markdown_append:
                added_lines = [f"{new_lines}## Supported Regions\n\n"]
                if supported_regions[spec_type][key]['AllRegions']:
                    added_lines.append(f"This {spec_type_name} is supported by ***all*** regions.")
                    markdown_append.writelines(added_lines)
                else:
                    added_lines.append(f"This {spec_type_name} is supported by the following regions:\n\n")
                    for region in sorted(supported_regions[spec_type][key]['Regions']):
                        added_lines.append(f"- `{region}`\n")
                    markdown_append.writelines(added_lines)
