# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v87-changelog.json`](changelogs/v87-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [87.0.0](#8700-2022-09-04)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [87.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v87.0.0) (2022-09-04)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v87-changelog.json)
  - Change source is a diff between [v87.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v87.0.0) and [v86.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v86.0.0)

### Totals

- TotalPropertyTypes: 3296 **(+2)**
- TotalPropertyTypesSupportedGlobally: 1142 **(+1)**
- TotalResourceTypes: 954 **(+2)**
- TotalResourceTypesSupportedGlobally: 344 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::ControlTower::EnabledControl](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`

- [AWS::Macie::AllowList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-allowlist.html)
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::APS::Workspace.LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`

- [AWS::Macie::AllowList.Criteria](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-allowlist-criteria.html)
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Connect::InstanceStorageConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html)
  - `ap-southeast-2`
  - `ca-central-1`
  - `af-south-1`
  - `ap-northeast-2`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `us-east-1`
  - `ap-northeast-1`

- [AWS::Route53Resolver::ResolverQueryLoggingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html)
  - `ap-northeast-3`
  - `cn-north-1`

- [AWS::AppMesh::Route.TcpRouteMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproutematch.html)
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `us-west-1`
  - `af-south-1`
  - `ap-northeast-3`
  - `ap-northeast-2`
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-2`
  - `eu-south-1`
  - `me-south-1`

- [AWS::AppMesh::VirtualGateway.JsonFormatRef](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-jsonformatref.html)
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `us-west-1`
  - `af-south-1`
  - `ap-northeast-3`
  - `ap-northeast-2`
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-2`
  - `eu-south-1`
  - `me-south-1`

- [AWS::AppMesh::VirtualGateway.LoggingFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-loggingformat.html)
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `us-west-1`
  - `af-south-1`
  - `ap-northeast-3`
  - `ap-northeast-2`
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-2`
  - `eu-south-1`
  - `me-south-1`

- [AWS::AppMesh::VirtualNode.JsonFormatRef](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-jsonformatref.html)
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `us-west-1`
  - `af-south-1`
  - `ap-northeast-3`
  - `ap-northeast-2`
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-2`
  - `eu-south-1`
  - `me-south-1`

- [AWS::AppMesh::VirtualNode.LoggingFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-loggingformat.html)
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `us-west-1`
  - `af-south-1`
  - `ap-northeast-3`
  - `ap-northeast-2`
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-2`
  - `eu-south-1`
  - `me-south-1`

- [AWS::Connect::InstanceStorageConfig.EncryptionConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-encryptionconfig.html)
  - `ap-southeast-2`
  - `ca-central-1`
  - `af-south-1`
  - `ap-northeast-2`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `us-east-1`
  - `ap-northeast-1`

- [AWS::Connect::InstanceStorageConfig.KinesisFirehoseConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisfirehoseconfig.html)
  - `ap-southeast-2`
  - `ca-central-1`
  - `af-south-1`
  - `ap-northeast-2`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `us-east-1`
  - `ap-northeast-1`

- [AWS::Connect::InstanceStorageConfig.KinesisStreamConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisstreamconfig.html)
  - `ap-southeast-2`
  - `ca-central-1`
  - `af-south-1`
  - `ap-northeast-2`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `us-east-1`
  - `ap-northeast-1`

- [AWS::Connect::InstanceStorageConfig.KinesisVideoStreamConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisvideostreamconfig.html)
  - `ap-southeast-2`
  - `ca-central-1`
  - `af-south-1`
  - `ap-northeast-2`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `us-east-1`
  - `ap-northeast-1`

- [AWS::Connect::InstanceStorageConfig.S3Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-s3config.html)
  - `ap-southeast-2`
  - `ca-central-1`
  - `af-south-1`
  - `ap-northeast-2`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `us-east-1`
  - `ap-northeast-1`

- [AWS::RDS::DBInstance.Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-endpoint.html)
  - Now available to **ALL** regions.

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::Logs::MetricFilter.Dimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-dimension.html)
  - `eu-central-1`

- [AWS::RDS::DBCluster.ReadEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-readendpoint.html)
  - `eu-central-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `us-east-1`
  - `eu-west-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `sa-east-1`
  - `ap-northeast-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v86.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v86.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v86.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v86.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v86.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v86.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- PropertyType Still Missing
  - Since v86.0.0: [AWS::Config::OrganizationConfigRule.OrganizationCustomPolicyRuleMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html)
    - `me-south-1`

  - Since v86.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v86.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v86.0.0: [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v86.0.0: [AWS::RDS::DBCluster.ReadEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-readendpoint.html)
    - `us-west-2`

  - Since v86.0.0: [AWS::Redshift::ScheduledAction.PauseClusterMessage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-pauseclustermessage.html)
    - `us-gov-west-1`

  - Since v86.0.0: [AWS::Redshift::ScheduledAction.ResizeClusterMessage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resizeclustermessage.html)
    - `us-gov-west-1`

  - Since v86.0.0: [AWS::Redshift::ScheduledAction.ResumeClusterMessage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resumeclustermessage.html)
    - `us-gov-west-1`

  - Since v86.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v86.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

