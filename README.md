# AWS CloudFormation Library

> *A Completely Tracked and Versioned Collection of CloudFormation Resource Files*

## Purpose

I created this repository as an easy, versioned git repository that shows changes across `CloudFormationResource.json` files over time. It also can work as a location for conversation around errors within CloudFormationResource files, as I was unable to find where else I could log these issues publicly.

* [AWS CloudFormation Resource Specification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html)
  * [Source Code Repo](https://github.com/awsdocs/aws-cloudformation-user-guide/blob/master/doc_source/cfn-resource-specification.md)

> *NOTE: This repository may change in the future, including ownership, depending on the outcome of the following issue: [AWS Docs: Missing CloudFormationResourceSpecification.json Files in This Repository](https://github.com/awsdocs/aws-cloudformation-user-guide/issues/4)*

## Setup 

### Prerequisites

- Python 3.6+
- AWS Access Key configured

### Python Virtual Env

`venv-setup.sh` sets up things, doing mainly the following:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -U pip setuptools
pip install boto3
```

## Generating Resources


