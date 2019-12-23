# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v10-changelog.json`](changelogs/v10-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [10.2.0](#1020-2019-12-23)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)
- [10.1.0](#1010-2019-12-13)
  - [Totals](#totals-1)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-1)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-1)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-1)
- [10.0.0](#1000-2019-12-05)
  - [Totals](#totals-2)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-2)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-2)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-2)

## [10.2.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.2.0) (2019-12-23)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v10-changelog.json)
  - Change source is a diff between [v10.2.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.2.0) and [v10.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.1.0)

### Totals

- TotalPropertyTypes: 1263 **(+8)**
- TotalPropertyTypesSupportedGlobally: 480 **(+0)**
- TotalResourceTypes: 488 **(+2)**
- TotalResourceTypesSupportedGlobally: 191 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::CodeBuild::ReportGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html)
  - `us-east-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`
  - `ap-east-1`
  - `cn-north-1`
  - `cn-northwest-1`
  - `me-south-1`

- [AWS::EC2::GatewayRouteTableAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-gatewayroutetableassociation.html)
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

- [AWS::CodeBuild::ReportGroup.ReportExportConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-reportexportconfig.html)
  - `us-east-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`
  - `ap-east-1`
  - `cn-north-1`
  - `cn-northwest-1`
  - `me-south-1`

- [AWS::CodeBuild::ReportGroup.S3ReportExportConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html)
  - `us-east-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`
  - `ap-east-1`
  - `cn-north-1`
  - `cn-northwest-1`
  - `me-south-1`

- [AWS::DLM::LifecyclePolicy.CrossRegionCopyRetainRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.html)
  - `us-east-1`
  - `ap-south-1`
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

- [AWS::DLM::LifecyclePolicy.CrossRegionCopyRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html)
  - `us-east-1`
  - `ap-south-1`
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

- [AWS::MSK::Cluster.JmxExporter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-jmxexporter.html)
  - `us-east-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`
  - `ap-east-1`

- [AWS::MSK::Cluster.NodeExporter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-nodeexporter.html)
  - `us-east-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`
  - `ap-east-1`

- [AWS::MSK::Cluster.OpenMonitoring](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html)
  - `us-east-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`
  - `ap-east-1`

- [AWS::MSK::Cluster.Prometheus](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html)
  - `us-east-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`
  - `ap-east-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Route53Resolver::ResolverEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html)
  - `ap-east-1`
  - `eu-north-1`

- [AWS::Route53Resolver::ResolverRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html)
  - `ap-east-1`
  - `eu-north-1`

- [AWS::Route53Resolver::ResolverRuleAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html)
  - `ap-east-1`
  - `eu-north-1`

- [AWS::Route53Resolver::ResolverEndpoint.IpAddressRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html)
  - `ap-east-1`
  - `eu-north-1`

- [AWS::Route53Resolver::ResolverRule.TargetAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html)
  - `ap-east-1`
  - `eu-north-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v10.1.0: [AWS::MediaLive::Channel.MultiplexProgramChannelDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html)
    - `ap-south-1`
    - `eu-west-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`

## [10.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.1.0) (2019-12-13)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v10-changelog.json)
  - Change source is a diff between [v10.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.1.0) and [v10.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.0.0)

### Totals

- TotalPropertyTypes: 1255 **(+1)**
- TotalPropertyTypesSupportedGlobally: 480 **(+0)**
- TotalResourceTypes: 486 **(+0)**
- TotalResourceTypesSupportedGlobally: 191 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::MediaLive::Channel.MultiplexProgramChannelDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html)
  - `ap-south-1`
  - `eu-west-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Glue::MLTransform](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html)
  - `ap-south-1`
  - `ca-central-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`

- [AWS::Glue::MLTransform.FindMatchesParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters-findmatchesparameters.html)
  - `ap-south-1`
  - `ca-central-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`

- [AWS::Glue::MLTransform.GlueTables](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables-gluetables.html)
  - `ap-south-1`
  - `ca-central-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`

- [AWS::Glue::MLTransform.InputRecordTables](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables.html)
  - `ap-south-1`
  - `ca-central-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`

- [AWS::Glue::MLTransform.TransformParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters.html)
  - `ap-south-1`
  - `ca-central-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- New PropertyType(s) Missing
  - [AWS::MediaLive::Channel.MultiplexProgramChannelDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html)
    - `ap-south-1`
    - `eu-west-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`

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

