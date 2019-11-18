# AWS CloudFormation Resource Specification Auditor

> *A Completely Tracked, Versioned, and Audited Collection Store of CloudFormationResource.json Resource Specification Files*

## Purpose

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

#### Yet to Automate

The following is still manually managed:

- `documentation-broken-links-detailed.json`

Some of the troubleshooting steps for finding a fix to the documentation errors can be rather involved. I'd like to reduce this to the most helpful potential-fix steps done in an automated fashion.

> ***NOTE:*** _This doc also tracks the amount of days passed since certain bugs were discovered. This has helped in understanding that the [AWS CloudFormation User Guide source](https://github.com/awsdocs/aws-cloudformation-user-guide/) is being managed in a confusing (mostly manual) fashion by AWS._
