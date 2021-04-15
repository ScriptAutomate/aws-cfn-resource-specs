# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v34-changelog.json`](changelogs/v34-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [34.0.0](#3400-2021-04-15)
  - [Totals](#totals)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [34.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v34.0.0) (2021-04-15)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v34-changelog.json)
  - Change source is a diff between [v34.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v34.0.0) and [v33.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v33.1.0)

### Totals

- TotalPropertyTypes: 2401 **(+0)**
- TotalPropertyTypesSupportedGlobally: 586 **(+0)**
- TotalResourceTypes: 733 **(+0)**
- TotalResourceTypesSupportedGlobally: 213 **(+0)**

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::AppFlow::Flow.IdFieldNamesList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-idfieldnameslist.html)
  - `ap-southeast-2`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v33.1.0: [AWS::CloudFront::Distribution.LegacyCustomOrigin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html)
    - `eu-central-1`

  - Since v33.1.0: [AWS::CloudFront::Distribution.LegacyS3Origin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacys3origin.html)
    - `eu-central-1`

  - Since v33.1.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v33.1.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v33.1.0: [AWS::SSM::Document.AttachmentsSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html)
    - `us-west-2`

  - Since v33.1.0: [AWS::SSM::Document.DocumentRequires](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-documentrequires.html)
    - `us-west-2`

