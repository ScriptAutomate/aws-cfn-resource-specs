# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v64-changelog.json`](changelogs/v64-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [64.0.0](#6400-2022-04-02)
  - [Totals](#totals)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [64.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v64.0.0) (2022-04-02)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v64-changelog.json)
  - Change source is a diff between [v64.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v64.0.0) and [v63.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v63.0.0)

### Totals

- TotalPropertyTypes: 3064 **(+0)**
- TotalPropertyTypesSupportedGlobally: 1079 **(+0)**
- TotalResourceTypes: 907 **(+0)**
- TotalResourceTypesSupportedGlobally: 339 **(+0)**

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::AppStream::DirectoryConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-directoryconfig.html)
  - `ca-central-1`

- [AWS::AppStream::Fleet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html)
  - `ca-central-1`

- [AWS::AppStream::ImageBuilder](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html)
  - `ca-central-1`

- [AWS::AppStream::Stack](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html)
  - `ca-central-1`

- [AWS::AppStream::StackFleetAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackfleetassociation.html)
  - `ca-central-1`

- [AWS::AppStream::StackUserAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackuserassociation.html)
  - `ca-central-1`

- [AWS::AppStream::User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.html)
  - `ca-central-1`

- [AWS::EC2::TransitGatewayConnect](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayconnect.html)
  - `eu-west-2`

- [AWS::KinesisVideo::SignalingChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisvideo-signalingchannel.html)
  - `ap-south-1`

- [AWS::KinesisVideo::Stream](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisvideo-stream.html)
  - `ap-south-1`

- [AWS::AppStream::DirectoryConfig.ServiceAccountCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-directoryconfig-serviceaccountcredentials.html)
  - `ca-central-1`

- [AWS::AppStream::Fleet.ComputeCapacity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-computecapacity.html)
  - `ca-central-1`

- [AWS::AppStream::Fleet.DomainJoinInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-domainjoininfo.html)
  - `ca-central-1`

- [AWS::AppStream::Fleet.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-vpcconfig.html)
  - `ca-central-1`

- [AWS::AppStream::ImageBuilder.AccessEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-accessendpoint.html)
  - `ca-central-1`

- [AWS::AppStream::ImageBuilder.DomainJoinInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-domainjoininfo.html)
  - `ca-central-1`

- [AWS::AppStream::ImageBuilder.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-vpcconfig.html)
  - `ca-central-1`

- [AWS::AppStream::Stack.AccessEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-accessendpoint.html)
  - `ca-central-1`

- [AWS::AppStream::Stack.ApplicationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-applicationsettings.html)
  - `ca-central-1`

- [AWS::AppStream::Stack.StorageConnector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-storageconnector.html)
  - `ca-central-1`

- [AWS::AppStream::Stack.UserSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-usersetting.html)
  - `ca-central-1`

- [AWS::EC2::TransitGatewayConnect.TransitGatewayConnectOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewayconnect-transitgatewayconnectoptions.html)
  - `eu-west-2`

- [AWS::SageMaker::Domain.DomainSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-domainsettings.html)
  - `me-south-1`
  - `us-east-2`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `eu-south-1`
  - `ap-northeast-2`
  - `ca-central-1`
  - `ap-east-1`
  - `us-east-1`
  - `ap-south-1`
  - `cn-northwest-1`
  - `eu-north-1`
  - `af-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::SageMaker::Domain.RStudioServerProAppSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-rstudioserverproappsettings.html)
  - `me-south-1`
  - `us-east-2`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `eu-south-1`
  - `ap-northeast-2`
  - `ca-central-1`
  - `ap-east-1`
  - `us-east-1`
  - `ap-south-1`
  - `cn-northwest-1`
  - `eu-north-1`
  - `af-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::SageMaker::Domain.RStudioServerProDomainSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-rstudioserverprodomainsettings.html)
  - `me-south-1`
  - `us-east-2`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `eu-south-1`
  - `ap-northeast-2`
  - `ca-central-1`
  - `ap-east-1`
  - `us-east-1`
  - `ap-south-1`
  - `cn-northwest-1`
  - `eu-north-1`
  - `af-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::SageMaker::UserProfile.RStudioServerProAppSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-rstudioserverproappsettings.html)
  - `me-south-1`
  - `us-east-2`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `eu-south-1`
  - `ap-northeast-2`
  - `ca-central-1`
  - `ap-east-1`
  - `us-east-1`
  - `ap-south-1`
  - `eu-north-1`
  - `af-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `ap-northeast-1`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::Events::Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-endpoint.html)
  - `us-east-2`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `us-west-2`
  - `ap-northeast-2`
  - `ca-central-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-northeast-3`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::Events::Endpoint.EndpointEventBus](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-endpointeventbus.html)
  - `us-east-2`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `us-west-2`
  - `ap-northeast-2`
  - `ca-central-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-northeast-3`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::Events::Endpoint.FailoverConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-failoverconfig.html)
  - `us-east-2`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `us-west-2`
  - `ap-northeast-2`
  - `ca-central-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-northeast-3`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::Events::Endpoint.Primary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-primary.html)
  - `us-east-2`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `us-west-2`
  - `ap-northeast-2`
  - `ca-central-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-northeast-3`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::Events::Endpoint.ReplicationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-replicationconfig.html)
  - `us-east-2`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `us-west-2`
  - `ap-northeast-2`
  - `ca-central-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-northeast-3`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::Events::Endpoint.RoutingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-routingconfig.html)
  - `us-east-2`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `us-west-2`
  - `ap-northeast-2`
  - `ca-central-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-northeast-3`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::Events::Endpoint.Secondary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-secondary.html)
  - `us-east-2`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `us-west-2`
  - `ap-northeast-2`
  - `ca-central-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-northeast-3`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `ap-northeast-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v63.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v63.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v63.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v63.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v63.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v63.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

  - Since v63.0.0: [AWS::Events::Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-endpoint.html)
    - `eu-central-1`

- PropertyType Still Missing
  - Since v63.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v63.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v63.0.0: [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v63.0.0: [AWS::Events::Endpoint.EndpointEventBus](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-endpointeventbus.html)
    - `eu-central-1`

  - Since v63.0.0: [AWS::Events::Endpoint.FailoverConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-failoverconfig.html)
    - `eu-central-1`

  - Since v63.0.0: [AWS::Events::Endpoint.Primary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-primary.html)
    - `eu-central-1`

  - Since v63.0.0: [AWS::Events::Endpoint.ReplicationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-replicationconfig.html)
    - `eu-central-1`

  - Since v63.0.0: [AWS::Events::Endpoint.RoutingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-routingconfig.html)
    - `eu-central-1`

  - Since v63.0.0: [AWS::Events::Endpoint.Secondary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-endpoint-secondary.html)
    - `eu-central-1`

  - Since v63.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v63.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

