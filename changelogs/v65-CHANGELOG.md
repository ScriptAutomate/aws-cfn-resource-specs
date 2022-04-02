# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v65-changelog.json`](changelogs/v65-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [65.0.0](#6500-2022-04-02)
  - [Totals](#totals)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [65.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v65.0.0) (2022-04-02)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v65-changelog.json)
  - Change source is a diff between [v65.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v65.0.0) and [v64.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v64.0.0)

### Totals

- TotalPropertyTypes: 3058 **(+-6)**
- TotalPropertyTypesSupportedGlobally: 1079 **(+0)**
- TotalResourceTypes: 906 **(+-1)**
- TotalResourceTypesSupportedGlobally: 339 **(+0)**

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::Events::Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-endpoint.html)
  - `eu-central-1`

- [AWS::Events::Endpoint.EndpointEventBus](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-endpointeventbus.html)
  - `eu-central-1`

- [AWS::Events::Endpoint.FailoverConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-failoverconfig.html)
  - `eu-central-1`

- [AWS::Events::Endpoint.Primary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-primary.html)
  - `eu-central-1`

- [AWS::Events::Endpoint.ReplicationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-replicationconfig.html)
  - `eu-central-1`

- [AWS::Events::Endpoint.RoutingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-routingconfig.html)
  - `eu-central-1`

- [AWS::Events::Endpoint.Secondary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-secondary.html)
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::SageMaker::UserProfile.RStudioServerProAppSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-rstudioserverproappsettings.html)
  - `cn-northwest-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v64.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v64.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v64.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v64.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v64.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v64.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- PropertyType Still Missing
  - Since v64.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v64.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v64.0.0: [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v64.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v64.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

