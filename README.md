# AWS CloudFormation Library

> *A Completely Tracked and Versioned Collection of CloudFormation Resource Files*

## Purpose

I created this repository as an easy, versioned git repository that shows changes across `CloudFormationResource.json` files over time. It also can work as a location for conversation around errors within CloudFormationResource files, as I was unable to find where else I could log these issues publicly.

* [AWS CloudFormation Resource Specification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html)
  * [Source Code Repo](https://github.com/awsdocs/aws-cloudformation-user-guide/blob/master/doc_source/cfn-resource-specification.md)

### Missing CFN Resource Specifications from AWS Documentation

> _**NOTE:** Some CFN Resource Specifications may be missing because they have yet to be officially published. As a result, I am including the GitHub issue links for reference on conversation around why they aren't included on the official documentation page._

The following CFN resource specifications are missing from the [AWS CloudFormation Resource Specification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html) landing page:

| Region  | Location  | GitHub Issue |
|---|---|---|
|  `ap-east-1` | [Asia Pacific (Hong Kong)](https://aws.amazon.com/blogs/aws/now-open-aws-asia-pacific-hong-kong-region/)  | [No Resource Specification for ap-east-1](https://github.com/awsdocs/aws-cloudformation-user-guide/issues/320) |
| `cn-north-1`  | [China (Beijing)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-sample-templates-cn-north-1.html)  | [Missing CFN Resource Spec File Links for China](https://github.com/awsdocs/aws-cloudformation-user-guide/issues/425) |
| `cn-northwest-1`  | [China (Ningxia)](https://aws.amazon.com/blogs/aws/now-open-aws-china-ningxia-region/)  | [Missing CFN Resource Spec File Links for China](https://github.com/awsdocs/aws-cloudformation-user-guide/issues/425) |
| `us-gov-east-1` | [AWS GovCloud (US-East)](https://aws.amazon.com/blogs/aws/aws-govcloud-us-east-now-open/)  | [Missing CFN Resource Spec File Links for GovCloud](https://github.com/awsdocs/aws-cloudformation-user-guide/issues/426) |
| `us-gov-west-1`  | [AWS GovCloud (US-West)](https://aws.amazon.com/govcloud-us/)  | [Missing CFN Resource Spec File Links for GovCloud](https://github.com/awsdocs/aws-cloudformation-user-guide/issues/426) |
| `me-south-1`  | [Middle East (Bahrain)](https://aws.amazon.com/about-aws/whats-new/2019/07/announcing-the-new-aws-middle-east--bahrain--region-/)  | [Missing me-south-1 Specs](https://github.com/awsdocs/aws-cloudformation-user-guide/issues/421) |

Their links can be found in the `cfn-python-lint` source code, maintained by the AWS CloudFormation team, here:

* [aws-cloudformation/cfn-python-lint/src/cfnlint/maintenance.py](https://github.com/aws-cloudformation/cfn-python-lint/blob/4767ceefd5091a48fe2cb75f5954820aa150aa6b/src/cfnlint/maintenance.py#L31-L53)

> *NOTE: This repository may change in the future, including ownership, depending on the outcome of the following issue: [AWS Docs: Missing CloudFormationResourceSpecification.json Files in This Repository](https://github.com/awsdocs/aws-cloudformation-user-guide/issues/4)*

## Directory Structure

```bash
.
├── README.md                   <-- This README file
├── all-cfn-versions.json       <-- Tracks version history
└── example_region_folder       <-- Region resource spec dir
     └── CloudFormationResourceSpecification.json
```
