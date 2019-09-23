# AWS CloudFormation Resource Specification Audit Library

> *A Completely Tracked and Versioned Collection of CloudFormation Resource Files*

## Purpose

I created this repository as an easy, versioned git repository that shows changes across `CloudFormationResource.json` files over time. It also can work as a location for conversation around errors within CloudFormationResource files, as I was unable to find where else I could log these issues publicly.

* [AWS CloudFormation Resource Specification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html)
  * [Source Code Repo](https://github.com/awsdocs/aws-cloudformation-user-guide/blob/master/doc_source/cfn-resource-specification.md)

## Directory Structure

```
.
├── LICENSE                     <-- Repo code license
├── README.md                   <-- This README file
├── all-cfn-versions.json       <-- Tracks version history
├── documentation-broken...json <-- Detailed info on BrokenDocLinks
├── documentation-lookup...json <-- All Documentation property errors
├── regions.json                <-- Non-API-generated list of regions
├── supported-regions...json    <-- What types are supported in what regions
└── tools                       
     ├── cfn-resource-list.py   <-- Checks for and downloads latest spec files
     ├── cfn-supported...py     <-- Audits supported services and cfn docs
     └── create-pull-request.py <-- Creates PR if audit files update
└── specs                       <-- Region resource spec dir
     ├── us-east-1
     │    └── CloudFormationResourceSpecification.json
     ├── ...
     ├── ...
```
