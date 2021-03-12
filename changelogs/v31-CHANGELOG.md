# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v31-changelog.json`](changelogs/v31-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [31.0.0](#3100-2021-03-12)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [31.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v31.0.0) (2021-03-12)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v31-changelog.json)
  - Change source is a diff between [v31.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v31.0.0) and [v30.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v30.1.0)

### Totals

- TotalPropertyTypes: 2249 **(+9)**
- TotalPropertyTypesSupportedGlobally: 548 **(+14)**
- TotalResourceTypes: 715 **(+5)**
- TotalResourceTypesSupportedGlobally: 199 **(+6)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::CE::AnomalyMonitor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html)
  - `us-east-1`

- [AWS::CE::AnomalySubscription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html)
  - `us-east-1`

- [AWS::CertificateManager::Account](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-account.html)
  - Available in **ALL** regions.

- [AWS::ECS::ClusterCapacityProviderAssociations](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-clustercapacityproviderassociations.html)
  - Available in **ALL** regions.

- [AWS::RDS::DBProxyEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxyendpoint.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AppSync::GraphQLApi.LambdaAuthorizerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html)
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `cn-north-1`
  - `cn-northwest-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `me-south-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::CE::AnomalySubscription.Subscriber](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-subscriber.html)
  - `us-east-1`

- [AWS::CertificateManager::Account.ExpiryEventsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-account-expiryeventsconfiguration.html)
  - Available in **ALL** regions.

- [AWS::CloudFront::Distribution.LegacyCustomOrigin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html)
  - `eu-central-1`

- [AWS::CloudFront::Distribution.LegacyS3Origin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacys3origin.html)
  - `eu-central-1`

- [AWS::DynamoDB::Table.ContributorInsightsSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-contributorinsightsspecification.html)
  - Available in **ALL** regions.

- [AWS::ECS::Cluster.ClusterConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clusterconfiguration.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
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

- [AWS::ECS::Cluster.ExecuteCommandConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandconfiguration.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
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

- [AWS::ECS::Cluster.ExecuteCommandLogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
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

- [AWS::ECS::ClusterCapacityProviderAssociations.CapacityProviderStrategy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-clustercapacityproviderassociations-capacityproviderstrategy.html)
  - Available in **ALL** regions.

- [AWS::RDS::DBProxyEndpoint.TagFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxyendpoint-tagformat.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::DynamoDB::Table.KinesisStreamSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-kinesisstreamspecification.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-north-1`
  - `cn-northwest-1`
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

- [AWS::ECS::Cluster.ClusterSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersetting.html)
  - `af-south-1`
  - `ap-northeast-3`
  - `eu-south-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Batch::ComputeEnvironment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html)
  - `ap-northeast-3`

- [AWS::Batch::JobQueue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html)
  - `ap-northeast-3`

- [AWS::Detective::Graph](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::Detective::MemberInvitation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::ECS::CapacityProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-capacityprovider.html)
  - Now available to **ALL** regions.

- [AWS::ECS::PrimaryTaskSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-primarytaskset.html)
  - Now available to **ALL** regions.

- [AWS::ECS::TaskSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html)
  - Now available to **ALL** regions.

- [AWS::EKS::Addon](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html)
  - Now available to **ALL** regions.

- [AWS::Batch::ComputeEnvironment.ComputeResources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html)
  - `ap-northeast-3`

- [AWS::Batch::ComputeEnvironment.Ec2ConfigurationObject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-ec2configurationobject.html)
  - `ap-northeast-3`

- [AWS::Batch::ComputeEnvironment.LaunchTemplateSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.ContainerProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.Device](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-device.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-environment.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.EvaluateOnExit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-evaluateonexit.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.FargatePlatformConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-fargateplatformconfiguration.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.LinuxParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-linuxparameters.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.LogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.MountPoints](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-mountpoints.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.NetworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-networkconfiguration.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.NodeProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-nodeproperties.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.NodeRangeProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-noderangeproperty.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.ResourceRequirement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-resourcerequirement.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.RetryStrategy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-retrystrategy.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.Secret](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-secret.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.Timeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-timeout.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.Tmpfs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-tmpfs.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.Ulimit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ulimit.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.Volumes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumes.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.VolumesHost](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumeshost.html)
  - `ap-northeast-3`

- [AWS::Batch::JobQueue.ComputeEnvironmentOrder](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobqueue-computeenvironmentorder.html)
  - `ap-northeast-3`

- [AWS::EC2::LaunchTemplate.TagSpecifications](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-tagspecifications.html)
  - `ap-northeast-1`
  - `us-west-2`
  - `ap-south-1`
  - `ca-central-1`
  - `us-gov-east-1`
  - `ap-southeast-1`
  - `us-east-1`
  - `eu-west-1`
  - `us-west-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `eu-north-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `us-gov-west-1`
  - `ap-southeast-2`
  - `me-south-1`
  - `eu-west-2`
  - `us-east-2`

- [AWS::ECS::CapacityProvider.AutoScalingGroupProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-autoscalinggroupprovider.html)
  - Now available to **ALL** regions.

- [AWS::ECS::CapacityProvider.ManagedScaling](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-capacityprovider-managedscaling.html)
  - Now available to **ALL** regions.

- [AWS::ECS::Cluster.CapacityProviderStrategyItem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-capacityproviderstrategyitem.html)
  - Now available to **ALL** regions.

- [AWS::ECS::Cluster.ClusterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersettings.html)
  - Now available to **ALL** regions.

- [AWS::ECS::TaskDefinition.AuthorizationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-authorizationconfig.html)
  - Now available to **ALL** regions.

- [AWS::ECS::TaskDefinition.EFSVolumeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-efsvolumeconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::ECS::TaskDefinition.EnvironmentFile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-environmentfile.html)
  - Now available to **ALL** regions.

- [AWS::ECS::TaskSet.AwsVpcConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-awsvpcconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::ECS::TaskSet.LoadBalancer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-loadbalancer.html)
  - Now available to **ALL** regions.

- [AWS::ECS::TaskSet.NetworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-networkconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::ECS::TaskSet.Scale](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-scale.html)
  - Now available to **ALL** regions.

- [AWS::ECS::TaskSet.ServiceRegistry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-serviceregistry.html)
  - Now available to **ALL** regions.

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v30.1.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

- PropertyType Still Missing
  - Since v30.1.0: [AWS::GroundStation::Config.AntennaDownlinkConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::Config.AntennaDownlinkDemodDecodeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::Config.AntennaUplinkConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::Config.ConfigData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::Config.DataflowEndpointConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-dataflowendpointconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::Config.DecodeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-decodeconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::Config.DemodulationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-demodulationconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::Config.Eirp](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-eirp.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::Config.Frequency](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequency.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::Config.FrequencyBandwidth](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequencybandwidth.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::Config.S3RecordingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::Config.SpectrumConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::Config.TrackingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-trackingconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::Config.UplinkEchoConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkechoconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::Config.UplinkSpectrumConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkspectrumconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v30.1.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v30.1.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::CloudFront::Distribution.LegacyCustomOrigin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html)
    - `eu-central-1`

  - [AWS::CloudFront::Distribution.LegacyS3Origin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacys3origin.html)
    - `eu-central-1`

