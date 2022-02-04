# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v55-changelog.json`](changelogs/v55-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [55.0.0](#5500-2022-02-04)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [55.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v55.0.0) (2022-02-04)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v55-changelog.json)
  - Change source is a diff between [v55.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v55.0.0) and [v54.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v54.0.0)

### Totals

- TotalPropertyTypes: 2953 **(+4)**
- TotalPropertyTypesSupportedGlobally: 1059 **(+2)**
- TotalResourceTypes: 887 **(+0)**
- TotalResourceTypesSupportedGlobally: 333 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::CustomerProfiles::Integration.ObjectTypeMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-objecttypemapping.html)
  - `eu-central-1`

- [AWS::EC2::LaunchTemplate.PrivateDnsNameOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-privatednsnameoptions.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Events::Rule.SageMakerPipelineParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sagemakerpipelineparameter.html)
  - Available in **ALL** regions.

- [AWS::Events::Rule.SageMakerPipelineParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sagemakerpipelineparameters.html)
  - Available in **ALL** regions.

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Rekognition::Collection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-collection.html)
  - `us-gov-west-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::ResilienceHub::App](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-north-1`
  - `me-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `af-south-1`
  - `ap-east-1`
  - `us-west-1`
  - `eu-west-3`
  - `eu-south-1`

- [AWS::ResilienceHub::ResiliencyPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-north-1`
  - `me-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `af-south-1`
  - `ap-east-1`
  - `us-west-1`
  - `eu-west-3`
  - `eu-south-1`

- [AWS::SES::ContactList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html)
  - `eu-north-1`
  - `me-south-1`
  - `us-gov-west-1`
  - `us-east-2`
  - `af-south-1`
  - `us-west-1`
  - `eu-west-3`

- [AWS::ResilienceHub::App.PhysicalResourceId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-physicalresourceid.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-north-1`
  - `me-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `af-south-1`
  - `ap-east-1`
  - `us-west-1`
  - `eu-west-3`
  - `eu-south-1`

- [AWS::ResilienceHub::App.ResourceMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-north-1`
  - `me-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `af-south-1`
  - `ap-east-1`
  - `us-west-1`
  - `eu-west-3`
  - `eu-south-1`

- [AWS::ResilienceHub::ResiliencyPolicy.FailurePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-resiliencypolicy-failurepolicy.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-north-1`
  - `me-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `af-south-1`
  - `ap-east-1`
  - `us-west-1`
  - `eu-west-3`
  - `eu-south-1`

- [AWS::SES::ContactList.Topic](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html)
  - `eu-north-1`
  - `me-south-1`
  - `us-gov-west-1`
  - `us-east-2`
  - `af-south-1`
  - `us-west-1`
  - `eu-west-3`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v54.0.0: [AWS::CloudFormation::HookDefaultVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookdefaultversion.html)
    - `eu-central-1`

  - Since v54.0.0: [AWS::CloudFormation::HookTypeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hooktypeconfig.html)
    - `eu-central-1`

  - Since v54.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v54.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v54.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v54.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v54.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v54.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- PropertyType Still Missing
  - Since v54.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v54.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v54.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v54.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::CustomerProfiles::Integration.ObjectTypeMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-objecttypemapping.html)
    - `eu-central-1`

