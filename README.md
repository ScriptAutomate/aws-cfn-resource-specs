# AWS CloudFormation Library

> *A Completely Tracked and Versioned Collection of CloudFormation Resource Files*

## Purpose

I created this repository as an easy, versioned git repository that shows changes across `CloudFormationResource.json` files over time. It also can work as a location for conversation around errors within CloudFormationResource files, as I was unable to find where else I could log these issues publicly.

* [AWS CloudFormation Resource Specification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html)
  * [Source Code Repo](https://github.com/awsdocs/aws-cloudformation-user-guide/blob/master/doc_source/cfn-resource-specification.md)

## Directory Structure

```bash
.
├── README.md                   <-- This README file
├── all-cfn-versions.json       <-- Tracks version history
└── example_region_folder       <-- Region resource spec dir
     └── CloudFormationResourceSpecification.json
```
