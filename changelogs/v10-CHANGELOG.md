# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v10-changelog.json`](changelogs/v8-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [10.0.0](#1000-2019-12-05)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [10.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.0.0) (2019-12-05)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v10-changelog.json)
  - Change source is a diff between [v10.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.0.0) and [v9.1.1](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v9.1.1)

### Totals

- TotalPropertyTypes: 1254 **(+0)**
- TotalPropertyTypesSupportedGlobally: 480 **(+2)**
- TotalResourceTypes: 486 **(+5)**
- TotalResourceTypesSupportedGlobally: 191 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::AccessAnalyzer::Analyzer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::EventSchemas::Discoverer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::EventSchemas::Registry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::EventSchemas::Schema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::S3::AccessPoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accesspoint.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AccessAnalyzer::Analyzer.ArchiveRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AccessAnalyzer::Analyzer.Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::EventSchemas::Discoverer.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::EventSchemas::Registry.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::EventSchemas::Schema.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Lambda::Alias.ProvisionedConcurrencyConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-provisionedconcurrencyconfiguration.html)
  - Available in **ALL** regions.

- [AWS::Lambda::Version.ProvisionedConcurrencyConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-version-provisionedconcurrencyconfiguration.html)
  - Available in **ALL** regions.

- [AWS::S3::AccessPoint.PublicAccessBlockConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-accesspoint-publicaccessblockconfiguration.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::S3::AccessPoint.VpcConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-accesspoint-vpcconfiguration.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::StepFunctions::StateMachine.CloudWatchLogsLogGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination-cloudwatchlogsloggroup.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::StepFunctions::StateMachine.LogDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::StepFunctions::StateMachine.LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-2`

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::WAFv2::IPSet.IPSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-ipset-ipset.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::WAFv2::IPSet.IPSetSummary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-ipset-ipsetsummary.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::WAFv2::IPSet.IPSets](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-ipset-ipsets.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::WAFv2::RegexPatternSet.RegexPatternSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-regexpatternset-regexpatternset.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::WAFv2::RegexPatternSet.RegexPatternSetSummary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-regexpatternset-regexpatternsetsummary.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::WAFv2::RegexPatternSet.RegexPatternSets](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-regexpatternset-regexpatternsets.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::WAFv2::RuleGroup.RuleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rulegroup.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::WAFv2::RuleGroup.RuleGroupSummary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rulegroupsummary.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::WAFv2::RuleGroup.RuleGroups](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rulegroups.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::WAFv2::WebACL.WebACL](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-webacl.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::WAFv2::WebACL.WebACLSummary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-webaclsummary.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::WAFv2::WebACL.WebACLs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-webacls.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::ApiGatewayV2::Api.BodyS3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html)
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `eu-west-1`
  - `eu-central-1`
  - `ap-southeast-2`
  - `eu-west-2`
  - `us-west-2`
  - `ap-northeast-1`

- [AWS::ApiGatewayV2::Api.Cors](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html)
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `eu-west-1`
  - `eu-central-1`
  - `ap-southeast-2`
  - `eu-west-2`
  - `us-west-2`
  - `ap-northeast-1`

- [AWS::ApiGatewayV2::Authorizer.JWTConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html)
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `eu-west-1`
  - `eu-central-1`
  - `ap-southeast-2`
  - `eu-west-2`
  - `us-west-2`
  - `ap-northeast-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType(s) No Longer Missing
  - [AWS::ApiGatewayV2::Api.BodyS3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html)
    - Was missing since v9.1.1

  - [AWS::ApiGatewayV2::Api.Cors](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html)
    - Was missing since v9.1.1

  - [AWS::ApiGatewayV2::Authorizer.JWTConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html)
    - Was missing since v9.1.1

