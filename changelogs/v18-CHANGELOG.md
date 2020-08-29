# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v18-changelog.json`](changelogs/v18-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [18.1.0](#1810-2020-08-28)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)
- [18.0.0](#1800-2020-08-24)
  - [Totals](#totals-1)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-1)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-1)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-1)

## [18.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.1.0) (2020-08-28)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v18-changelog.json)
  - Change source is a diff between [v18.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.1.0) and [v18.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.0.0)

### Totals

- TotalPropertyTypes: 1488 **(+3)**
- TotalPropertyTypesSupportedGlobally: 489 **(+0)**
- TotalResourceTypes: 557 **(+3)**
- TotalResourceTypesSupportedGlobally: 187 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::CodeGuruReviewer::RepositoryAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codegurureviewer-repositoryassociation.html)
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::Route53Resolver::ResolverQueryLoggingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html)
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html)
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Cognito::UserPoolClient.TokenValidityUnits](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-tokenvalidityunits.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-2`
  - `us-west-2`

- [AWS::GuardDuty::Detector.CFNDataSourceConfigurations](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::GuardDuty::Detector.CFNS3LogsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfns3logsconfiguration.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Athena::NamedQuery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html)
  - `cn-northwest-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Athena::WorkGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html)
  - `cn-north-1`

- [AWS::ManagedBlockchain::Member](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html)
  - `eu-west-2`

- [AWS::ManagedBlockchain::Node](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-node.html)
  - `eu-west-2`

- [AWS::Athena::WorkGroup.EncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html)
  - `cn-north-1`

- [AWS::Athena::WorkGroup.ResultConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html)
  - `cn-north-1`

- [AWS::Athena::WorkGroup.ResultConfigurationUpdates](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html)
  - `cn-north-1`

- [AWS::Athena::WorkGroup.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-tags.html)
  - `cn-north-1`

- [AWS::Athena::WorkGroup.WorkGroupConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html)
  - `cn-north-1`

- [AWS::Athena::WorkGroup.WorkGroupConfigurationUpdates](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html)
  - `cn-north-1`

- [AWS::ManagedBlockchain::Member.ApprovalThresholdPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-approvalthresholdpolicy.html)
  - `eu-west-2`

- [AWS::ManagedBlockchain::Member.MemberConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberconfiguration.html)
  - `eu-west-2`

- [AWS::ManagedBlockchain::Member.MemberFabricConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberfabricconfiguration.html)
  - `eu-west-2`

- [AWS::ManagedBlockchain::Member.MemberFrameworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberframeworkconfiguration.html)
  - `eu-west-2`

- [AWS::ManagedBlockchain::Member.NetworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkconfiguration.html)
  - `eu-west-2`

- [AWS::ManagedBlockchain::Member.NetworkFabricConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkfabricconfiguration.html)
  - `eu-west-2`

- [AWS::ManagedBlockchain::Member.NetworkFrameworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkframeworkconfiguration.html)
  - `eu-west-2`

- [AWS::ManagedBlockchain::Member.VotingPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-votingpolicy.html)
  - `eu-west-2`

- [AWS::ManagedBlockchain::Node.NodeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-node-nodeconfiguration.html)
  - `eu-west-2`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v18.0.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.0.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.0.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

- New ResourceType(s) Missing
  - [AWS::CodeGuruReviewer::RepositoryAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codegurureviewer-repositoryassociation.html)
    - `ap-northeast-1`
    - `eu-central-1`
    - `us-west-2`

- PropertyType Still Missing
  - Since v18.0.0: [AWS::AppSync::FunctionConfiguration.LambdaConflictHandlerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html)
    - `ap-northeast-2`

  - Since v18.0.0: [AWS::AppSync::FunctionConfiguration.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html)
    - `ap-northeast-2`

  - Since v18.0.0: [AWS::ECR::Repository.LifecyclePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-lifecyclepolicy.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v18.0.0: [AWS::ECS::Cluster.ClusterSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersetting.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `eu-south-1`

  - Since v18.0.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.0.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.0.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.0.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.0.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.0.0: [AWS::SSM::Association.ParameterValues](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-parametervalues.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `eu-south-1`

- New PropertyType(s) Missing
  - [AWS::Cognito::UserPoolClient.TokenValidityUnits](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-tokenvalidityunits.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `ca-central-1`
    - `eu-central-1`
    - `eu-west-2`
    - `us-east-2`
    - `us-west-2`

## [18.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.0.0) (2020-08-24)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v18-changelog.json)
  - Change source is a diff between [v18.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.0.0) and [v17.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v17.0.0)

### Totals

- TotalPropertyTypes: 1485 **(+1)**
- TotalPropertyTypesSupportedGlobally: 489 **(+2)**
- TotalResourceTypes: 554 **(+0)**
- TotalResourceTypesSupportedGlobally: 187 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::AppSync::FunctionConfiguration.LambdaConflictHandlerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html)
  - `ap-northeast-2`

- [AWS::AppSync::FunctionConfiguration.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html)
  - `ap-northeast-2`

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::ECS::TaskDefinition.Options](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-options.html)
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-north-1`
  - `cn-northwest-1`
  - `eu-central-1`
  - `eu-north-1`
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

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::ApplicationInsights::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.Alarm](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarm.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.AlarmMetric](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarmmetric.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.ComponentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentconfiguration.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.ComponentMonitoringSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.ConfigurationDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.CustomComponent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-customcomponent.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.Log](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.LogPattern](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.LogPatternSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpatternset.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.SubComponentConfigurationDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.SubComponentTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponenttypeconfiguration.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.WindowsEvent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html)
  - `eu-central-1`

- [AWS::ECS::TaskDefinition.EnvironmentFile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-environmentfile.html)
  - `eu-central-1`

- [AWS::EKS::Nodegroup.LaunchTemplateSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-launchtemplatespecification.html)
  - `eu-central-1`

- [AWS::KinesisFirehose::DeliveryStream.HttpEndpointCommonAttribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html)
  - `ap-east-1`

- [AWS::KinesisFirehose::DeliveryStream.HttpEndpointConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html)
  - `ap-east-1`

- [AWS::KinesisFirehose::DeliveryStream.HttpEndpointDestinationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html)
  - `ap-east-1`

- [AWS::KinesisFirehose::DeliveryStream.HttpEndpointRequestConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html)
  - `ap-east-1`

- [AWS::KinesisFirehose::DeliveryStream.RetryOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-retryoptions.html)
  - `ap-east-1`

- [AWS::Route53::HostedZone.HostedZoneConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzoneconfig.html)
  - Now available to **ALL** regions.

- [AWS::Route53::HostedZone.QueryLoggingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-queryloggingconfig.html)
  - Now available to **ALL** regions.

- [AWS::SageMaker::MonitoringSchedule.BaselineConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-baselineconfig.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.ClusterConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.ConstraintsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-constraintsresource.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.EndpointInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-environment.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.MonitoringAppSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.MonitoringExecutionSummary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.MonitoringInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringinput.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.MonitoringInputs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringinputs.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.MonitoringJobDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.MonitoringOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutput.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.MonitoringOutputConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutputconfig.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.MonitoringResources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringresources.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.MonitoringScheduleConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.NetworkConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.S3Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.ScheduleConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-scheduleconfig.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.StatisticsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-statisticsresource.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.StoppingCondition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-stoppingcondition.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-vpcconfig.html)
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::StepFunctions::StateMachine](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html)
  - `cn-north-1`

- [AWS::ECR::Repository.LifecyclePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-lifecyclepolicy.html)
  - `us-west-1`
  - `ap-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `sa-east-1`
  - `eu-west-2`
  - `me-south-1`
  - `ap-southeast-2`
  - `eu-west-3`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-2`
  - `ca-central-1`
  - `eu-central-1`

- [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
  - `eu-central-1`

- [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
  - `eu-central-1`

- [AWS::StepFunctions::StateMachine.CloudWatchLogsLogGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup.html)
  - `cn-north-1`

- [AWS::StepFunctions::StateMachine.DefinitionSubstitutions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-definitionsubstitutions.html)
  - `cn-north-1`

- [AWS::StepFunctions::StateMachine.LogDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html)
  - `cn-north-1`

- [AWS::StepFunctions::StateMachine.LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html)
  - `cn-north-1`

- [AWS::StepFunctions::StateMachine.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html)
  - `cn-north-1`

- [AWS::StepFunctions::StateMachine.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html)
  - `cn-north-1`

- [AWS::StepFunctions::StateMachine.TracingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tracingconfiguration.html)
  - `cn-north-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v17.0.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v17.0.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v17.0.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

- PropertyType Still Missing
  - Since v17.0.0: [AWS::ECR::Repository.LifecyclePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-lifecyclepolicy.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v17.0.0: [AWS::ECS::Cluster.ClusterSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersetting.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `eu-south-1`

  - Since v17.0.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v17.0.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v17.0.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v17.0.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v17.0.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v17.0.0: [AWS::SSM::Association.ParameterValues](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-parametervalues.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `eu-south-1`

- New PropertyType(s) Missing
  - [AWS::AppSync::FunctionConfiguration.LambdaConflictHandlerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html)
    - `ap-northeast-2`

  - [AWS::AppSync::FunctionConfiguration.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html)
    - `ap-northeast-2`

