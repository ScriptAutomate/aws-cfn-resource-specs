# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v42-changelog.json`](changelogs/v42-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [42.0.0](#4200-2021-09-24)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [42.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v42.0.0) (2021-09-24)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v42-changelog.json)
  - Change source is a diff between [v42.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v42.0.0) and [v41.2.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v41.2.0)

### Totals

- TotalPropertyTypes: 2615 **(+10)**
- TotalPropertyTypesSupportedGlobally: 937 **(+0)**
- TotalResourceTypes: 797 **(+5)**
- TotalResourceTypesSupportedGlobally: 326 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::MemoryDB::ACL](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-acl.html)
  - `ap-south-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MemoryDB::Cluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-cluster.html)
  - `ap-south-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MemoryDB::ParameterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-parametergroup.html)
  - `ap-south-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MemoryDB::SubnetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-subnetgroup.html)
  - `ap-south-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MemoryDB::User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-memorydb-user.html)
  - `ap-south-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`

- [AWS::Kendra::DataSource.ProxyConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-proxyconfiguration.html)
  - `ap-southeast-1`
  - `us-east-2`

- [AWS::Kendra::DataSource.WebCrawlerAuthenticationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerauthenticationconfiguration.html)
  - `ap-southeast-1`
  - `us-east-2`

- [AWS::Kendra::DataSource.WebCrawlerBasicAuthentication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerbasicauthentication.html)
  - `ap-southeast-1`
  - `us-east-2`

- [AWS::Kendra::DataSource.WebCrawlerConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html)
  - `ap-southeast-1`
  - `us-east-2`

- [AWS::Kendra::DataSource.WebCrawlerSeedUrlConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerseedurlconfiguration.html)
  - `ap-southeast-1`
  - `us-east-2`

- [AWS::Kendra::DataSource.WebCrawlerSiteMapsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlersitemapsconfiguration.html)
  - `ap-southeast-1`
  - `us-east-2`

- [AWS::Kendra::DataSource.WebCrawlerUrls](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerurls.html)
  - `ap-southeast-1`
  - `us-east-2`

- [AWS::Kendra::DataSource.WorkDocsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html)
  - `ap-southeast-1`
  - `us-east-2`

- [AWS::MSK::Cluster.Unauthenticated](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-unauthenticated.html)
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

- [AWS::MemoryDB::Cluster.Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-memorydb-cluster-endpoint.html)
  - `ap-south-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::GameLift::GameServerGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html)
  - `cn-northwest-1`

- [AWS::GameLift::GameSessionQueue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html)
  - `cn-northwest-1`

- [AWS::GameLift::MatchmakingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html)
  - `cn-northwest-1`

- [AWS::GameLift::MatchmakingRuleSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html)
  - `cn-northwest-1`

- [AWS::GameLift::Script](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html)
  - `cn-northwest-1`

- [AWS::SSO::Assignment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html)
  - `us-gov-west-1`

- [AWS::SSO::InstanceAccessControlAttributeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html)
  - `us-gov-west-1`

- [AWS::SSO::PermissionSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html)
  - `us-gov-west-1`

- [AWS::AppSync::DataSource.OpenSearchServiceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-opensearchserviceconfig.html)
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-east-1`
  - `ap-southeast-1`
  - `ap-northeast-2`
  - `eu-south-1`
  - `ap-northeast-1`
  - `eu-west-2`
  - `eu-central-1`
  - `us-east-1`
  - `eu-west-3`
  - `eu-west-1`
  - `eu-north-1`
  - `cn-north-1`
  - `cn-northwest-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `me-south-1`
  - `us-west-1`
  - `sa-east-1`

- [AWS::Backup::BackupVault.LockConfigurationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html)
  - `ap-south-1`
  - `ap-east-1`
  - `us-east-2`
  - `ap-southeast-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `eu-west-2`
  - `us-east-1`
  - `eu-west-3`
  - `eu-west-1`
  - `eu-north-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `us-west-2`
  - `me-south-1`
  - `us-west-1`
  - `sa-east-1`

- [AWS::GameLift::GameServerGroup.AutoScalingPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-autoscalingpolicy.html)
  - `cn-northwest-1`

- [AWS::GameLift::GameServerGroup.InstanceDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-instancedefinition.html)
  - `cn-northwest-1`

- [AWS::GameLift::GameServerGroup.LaunchTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-launchtemplate.html)
  - `cn-northwest-1`

- [AWS::GameLift::GameServerGroup.TargetTrackingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-targettrackingconfiguration.html)
  - `cn-northwest-1`

- [AWS::GameLift::GameSessionQueue.Destination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-destination.html)
  - `cn-northwest-1`

- [AWS::GameLift::GameSessionQueue.FilterConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-filterconfiguration.html)
  - `cn-northwest-1`

- [AWS::GameLift::GameSessionQueue.PlayerLatencyPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-playerlatencypolicy.html)
  - `cn-northwest-1`

- [AWS::GameLift::GameSessionQueue.PriorityConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-priorityconfiguration.html)
  - `cn-northwest-1`

- [AWS::GameLift::MatchmakingConfiguration.GameProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-matchmakingconfiguration-gameproperty.html)
  - `cn-northwest-1`

- [AWS::GameLift::Script.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html)
  - `cn-northwest-1`

- [AWS::IoT::TopicRule.OpenSearchAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html)
  - `ap-south-1`
  - `ap-east-1`
  - `us-east-2`
  - `ap-southeast-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `eu-west-2`
  - `us-east-1`
  - `eu-west-3`
  - `eu-west-1`
  - `eu-north-1`
  - `us-gov-west-1`
  - `cn-northwest-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `me-south-1`
  - `us-west-1`
  - `us-gov-east-1`
  - `sa-east-1`

- [AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html)
  - `us-gov-west-1`

- [AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttributeValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html)
  - `us-gov-west-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v41.2.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v41.2.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v41.2.0: [AWS::SageMaker::DataQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v41.2.0: [AWS::SageMaker::ModelBiasJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-environment.html)
    - `eu-west-3`

  - Since v41.2.0: [AWS::SageMaker::ModelExplainabilityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v41.2.0: [AWS::SageMaker::ModelQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v41.2.0: [AWS::SageMaker::MonitoringSchedule.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-environment.html)
    - `cn-northwest-1`
    - `eu-west-3`

- New PropertyType(s) Missing
  - [AWS::Kendra::DataSource.ProxyConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-proxyconfiguration.html)
    - `ap-southeast-1`
    - `us-east-2`

  - [AWS::Kendra::DataSource.WebCrawlerAuthenticationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerauthenticationconfiguration.html)
    - `ap-southeast-1`
    - `us-east-2`

  - [AWS::Kendra::DataSource.WebCrawlerBasicAuthentication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerbasicauthentication.html)
    - `ap-southeast-1`
    - `us-east-2`

  - [AWS::Kendra::DataSource.WebCrawlerConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html)
    - `ap-southeast-1`
    - `us-east-2`

  - [AWS::Kendra::DataSource.WebCrawlerSeedUrlConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerseedurlconfiguration.html)
    - `ap-southeast-1`
    - `us-east-2`

  - [AWS::Kendra::DataSource.WebCrawlerSiteMapsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlersitemapsconfiguration.html)
    - `ap-southeast-1`
    - `us-east-2`

  - [AWS::Kendra::DataSource.WebCrawlerUrls](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerurls.html)
    - `ap-southeast-1`
    - `us-east-2`

  - [AWS::Kendra::DataSource.WorkDocsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html)
    - `ap-southeast-1`
    - `us-east-2`

