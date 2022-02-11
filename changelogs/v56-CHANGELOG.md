# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v56-changelog.json`](changelogs/v56-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [56.0.0](#5600-2022-02-11)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [56.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v56.0.0) (2022-02-11)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v56-changelog.json)
  - Change source is a diff between [v56.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v56.0.0) and [v55.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v55.0.0)

### Totals

- TotalPropertyTypes: 2958 **(+5)**
- TotalPropertyTypesSupportedGlobally: 1064 **(+5)**
- TotalResourceTypes: 889 **(+2)**
- TotalResourceTypesSupportedGlobally: 334 **(+1)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::AppRunner::VpcConnector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::CloudFormation::HookVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookversion.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::AppRunner::Service.EgressConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-egressconfiguration.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::AppRunner::Service.NetworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-networkconfiguration.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::CloudFormation::HookVersion.LoggingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-hookversion-loggingconfig.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DevOpsGuru::ResourceCollection.TagCollection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-tagcollection.html)
  - `eu-central-1`

- [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
  - Available in **ALL** regions.

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::CloudFormation::HookDefaultVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookdefaultversion.html)
  - `us-gov-west-1`
  - `eu-south-1`
  - `us-west-1`
  - `sa-east-1`
  - `us-gov-east-1`
  - `me-south-1`
  - `eu-north-1`
  - `af-south-1`
  - `ca-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `ap-northeast-2`
  - `us-west-2`
  - `eu-west-3`
  - `ap-southeast-2`
  - `ap-northeast-3`
  - `us-east-1`
  - `ap-east-1`
  - `ap-southeast-1`
  - `us-east-2`
  - `ap-northeast-1`
  - `ap-south-1`

- [AWS::CloudFormation::HookTypeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hooktypeconfig.html)
  - `us-gov-west-1`
  - `eu-south-1`
  - `us-west-1`
  - `sa-east-1`
  - `us-gov-east-1`
  - `me-south-1`
  - `eu-north-1`
  - `af-south-1`
  - `ca-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `ap-northeast-2`
  - `us-west-2`
  - `eu-west-3`
  - `ap-southeast-2`
  - `ap-northeast-3`
  - `us-east-1`
  - `ap-east-1`
  - `ap-southeast-1`
  - `us-east-2`
  - `ap-northeast-1`
  - `ap-south-1`

- [AWS::Transfer::Server](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html)
  - `ap-northeast-3`

- [AWS::Transfer::User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html)
  - Now available to **ALL** regions.

- [AWS::CustomerProfiles::Integration.ObjectTypeMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-objecttypemapping.html)
  - `us-west-2`
  - `ap-southeast-2`
  - `us-east-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`

- [AWS::EC2::LaunchTemplate.PrivateDnsNameOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-privatednsnameoptions.html)
  - Now available to **ALL** regions.

- [AWS::Transfer::Server.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html)
  - `ap-northeast-3`

- [AWS::Transfer::Server.IdentityProviderDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html)
  - `ap-northeast-3`

- [AWS::Transfer::Server.Protocol](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocol.html)
  - `ap-northeast-3`

- [AWS::Transfer::Server.ProtocolDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocoldetails.html)
  - `ap-northeast-3`

- [AWS::Transfer::Server.WorkflowDetail](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetail.html)
  - `ap-northeast-3`

- [AWS::Transfer::Server.WorkflowDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetails.html)
  - `ap-northeast-3`

- [AWS::Transfer::User.HomeDirectoryMapEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html)
  - Now available to **ALL** regions.

- [AWS::Transfer::User.PosixProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html)
  - Now available to **ALL** regions.

- [AWS::Transfer::User.SshPublicKey](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-sshpublickey.html)
  - Now available to **ALL** regions.

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v55.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v55.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v55.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v55.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v55.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v55.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- PropertyType Still Missing
  - Since v55.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v55.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v55.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v55.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::DevOpsGuru::ResourceCollection.TagCollection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-tagcollection.html)
    - `eu-central-1`

