# AWS CloudFormation Resource Specification Auditor

> *A Completely Tracked, Versioned, and Audited Collection Store of CloudFormationResource.json Resource Specification Files*

## Quick Rundown and Example Use Case

Do you auto-generate toolsets, sdks, modules, packages, etc. from AWS CFN Resource Specification files? Or do you wish there was a more detailed breakdown of all the newly supported resourcetypes and propertytypes in CloudFormation? Or do you wish it was easier to know what regions seem to support certain resourcetypes/propertytypes? I have an auditing repository that monitors CFN resource specs provided by AWS, and then generates JSON files that can be ingested by other tools. For example, some workflows out there depend on looking at the `us-east-1` region resource spec, but they end up missing the types that aren't listed in that region:
- JSON output of the latest audit of all regions, with what is missing from `us-east-1` along with the regions these types are found in: https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v19-changelog.json#L1979-L2220
- A more human-readable version of the JSON converted into markdown: https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/CHANGELOG.md#existing-resourcetypes-and-propertytypes-not-in-us-east-1

It also does things like audit documentation links to see if they truly exist, both in the AWS published docs and the GitHub repo:
- https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/documentation-lookup-errors.json

If people were wanting to make a tool for easily viewing what CFN resource/property types are supported by what regions, this may act as a good datasource as I have them compiled into a single massive JSON:
- https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/supported-regions-per-resource.json

I made this repo in early 2020, and it is mostly self-writing with GitHub Actions that are auditing the CFN resource specs each day for updates, along with the CFN GitHub-hosted official AWS docs. Auto-updates result in PRs (I could never get the auto-merge GitHub Action to work properly, so I go hit the merge button periodically). I don't really update it much, and the code was hacked out since I was originally needing it for a project where I was auto-generating help documentation for some CFN tools.

### Example Use Case

You find yourself generating CFN templates, but aren't sure whether your target region is supported for certain resources. This repository compiles audits of all supported services in:
- https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/supported-regions-per-resource.json

```
# Download json
wget https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/supported-regions-per-resource.json
```

```
# Parse json, using jq for easy examples
## jq: https://stedolan.github.io/jq/
$ cat supported-regions-per-resource.json | jq '.ResourceTypes."AWS::ACMPCA::Certificate".AllRegions'
false
$ cat supported-regions-per-resource.json | jq '.ResourceTypes."AWS::ACMPCA::Certificate".Regions'
[
  "af-south-1",
  "ap-east-1",
  "ap-northeast-1",
  "ap-northeast-2",
  "ap-south-1",
  "ap-southeast-1",
  "ap-southeast-2",
  "ca-central-1",
  "eu-central-1",
  "eu-north-1",
  "eu-south-1",
  "eu-west-1",
  "eu-west-2",
  "eu-west-3",
  "me-south-1",
  "sa-east-1",
  "us-east-1",
  "us-east-2",
  "us-gov-east-1",
  "us-gov-west-1",
  "us-west-1",
  "us-west-2"
]
```

Hmmm, `AWS::ACMPCA::Certificate` isn't supported in *all* regions, but it is supported in most. And likely would be in your targeted regions.

What about **AWS Workspaces**?

```
# Parse json, using jq for easy examples
## jq: https://stedolan.github.io/jq/
$ cat supported-regions-per-resource.json | jq '.ResourceTypes."AWS::WorkSpaces::Workspace".AllRegions'
true
```

You now know that `AWS::WorkSpaces::Workspace` is supported in all regions (as of Oct. 2020)!

## Why This Repo was Created

I created this repository as an easy, versioned git repository that shows changes across `CloudFormationResource.json` files over time. It also can work as a location for conversation around errors within CloudFormationResource files, as I was unable to find where else I could log these issues publicly.

* [AWS CloudFormation Resource Specification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html)
  * [Source Code Repo](https://github.com/awsdocs/aws-cloudformation-user-guide/blob/master/doc_source/cfn-resource-specification.md)

For more information, please read the following blog post:

- [AWS CloudFormation Resource Specification Auditor: How wanting to generate code, from CloudFormation specification files, led to auditing AWS docs with Python and GitHub Actions](https://dev.to/scriptautomate/aws-cloudformation-resource-specification-auditor-26g)

## Directory Structure

```
.
├── LICENSE                     <-- Repo code license
├── README.md                   <-- This README file
├── CHANGELOG.md                <-- Changelog of current major version
├── all-cfn-versions.json       <-- Tracks version history
├── documentation-broken...json <-- Detailed info on BrokenDocLinks
├── documentation-lookup...json <-- All Documentation property errors
├── regions.json                <-- Non-API-generated list of regions
├── supported-regions...json    <-- What types are supported in what regions
└── tools
     ├── iampolicy.json         <-- Copy of AWS IAM policy perms to read s3
     ├── cfn-resource-list.py   <-- Checks for and downloads latest spec files
     ├── cfn-supported...py     <-- Audits supported services and cfn docs
     ├── cfn-changelogger.py    <-- Creates changelogs/*.json changelogs
     ├── create-changelog.py    <-- Creates changelogs/*.md and CHANGELOG.md
     └── create-pull-request.py <-- Creates PR if audit files update
└── changelogs
     ├── v8-changelog.json      <-- Machine-readable changelog of v8.*.*
     ├── v8-changelog.md        <-- Human-readable changelog of v8.*.*
     ├── ...
     └── ...
└── specs                       <-- Region resource spec dir
     ├── us-east-1
     │    └── CloudFormationResourceSpecification.json
     ├── ...
     ├── ...
```

## GitHub Actions

This repository automatically updates itself over time.

### Build Steps

- Checkout repo
- Install Python 3.7
- Install dependencies via Pipenv
- Lint with flake8
- Look for and update new CFN specs if found
- Audit documentation links and cfn user guide
- Generate changelog source file
- Generate changelog markdown file
- Create pull request if any files were updated

> ***NOTE:*** _The **Install dependencies via Pipenv** step also updates the `aws-cloudformation-user-guide` submodule, if any updates are available._

#### Step: Look for and update new CFN specs if found

The following is executed:

- `tools/cfn-resource-list.py`

I went the _Continuous Deployment_ route when it comes to how the repository updates the specification files in the `spec` directory, meaning I don't need to visit the repo and accept a PR whenever new spec files are published.

The following JSON file is also auto-updated / merged to `master` whenever the `spec` dir is updated:

- `all-cfn-versions.json`

#### Step: Audit documentation links and cfn user guide

The following is executed:

- `tools/cfn-supported-region-generator.py`

The following files may be updated:

- `supported-regions-per-resource.json`
- `documentation-lookup-errors.json`

> ***NOTE:*** _If any files are updated, either the JSON files listed above or the `aws-cloudformation-user-guide` submodule, then the last build step creates a new branch with a PR: **Create pull request if any files were updated**_

#### Step: Generate changelog source file

The following is executed:

- `tools/cfn-changelogger.py`

The following files may be updated:

- `changelogs/v*-changelog.json`
- `changelogs/v*-CHANGELOG.md`

#### Step: Generate changelog markdown file

TODO: Not documented

#### Yet to Automate

The following was manually managed:

- `documentation-broken-links-detailed.json`

Some of the troubleshooting steps for finding a fix to the documentation errors can be rather involved. I'd like to reduce this to the most helpful potential-fix steps done in an automated fashion. Though, this isn't currently supported and the json file is no longer manually updated.

> ***NOTE:*** _`documentation-broken-links-detailed.json` was also used to track the amount of days passed since certain bugs were discovered. This had helped in understanding that the [AWS CloudFormation User Guide source](https://github.com/awsdocs/aws-cloudformation-user-guide/) is being managed in a confusing (mostly manual) fashion by AWS:_
> - Issues I made as a result of this project: https://github.com/awsdocs/aws-cloudformation-user-guide/issues?q=is%3Aissue+author%3Ascriptautomate+
