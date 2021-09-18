# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v41-changelog.json`](changelogs/v41-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [41.2.0](#4120-2021-09-18)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)
- [41.1.0](#4110-2021-09-11)
  - [Totals](#totals-1)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-1)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-1)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-1)
- [41.0.0](#4100-2021-09-03)
  - [Totals](#totals-2)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-2)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-2)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions-1)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-2)

## [41.2.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v41.2.0) (2021-09-18)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v41-changelog.json)
  - Change source is a diff between [v41.2.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v41.2.0) and [v41.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v41.1.0)

### Totals

- TotalPropertyTypes: 2605 **(+18)**
- TotalPropertyTypesSupportedGlobally: 937 **(+15)**
- TotalResourceTypes: 792 **(+4)**
- TotalResourceTypesSupportedGlobally: 326 **(+1)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::ACMPCA::Permission](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html)
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

- [AWS::APS::Workspace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html)
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::HealthLake::FHIRDatastore](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html)
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::OpenSearchService::Domain](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html)
  - Available in **ALL** regions.

- [AWS::AppSync::DataSource.OpenSearchServiceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-opensearchserviceconfig.html)
  - `us-east-2`
  - `us-west-2`

- [AWS::Backup::BackupVault.LockConfigurationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html)
  - `eu-central-1`

- [AWS::HealthLake::FHIRDatastore.KmsEncryptionConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html)
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::HealthLake::FHIRDatastore.PreloadDataConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-preloaddataconfig.html)
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::HealthLake::FHIRDatastore.SseConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-sseconfiguration.html)
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::IoT::TopicRule.OpenSearchAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html)
  - `cn-north-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::OpenSearchService::Domain.AdvancedSecurityOptionsInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html)
  - Available in **ALL** regions.

- [AWS::OpenSearchService::Domain.ClusterConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html)
  - Available in **ALL** regions.

- [AWS::OpenSearchService::Domain.CognitoOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html)
  - Available in **ALL** regions.

- [AWS::OpenSearchService::Domain.DomainEndpointOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html)
  - Available in **ALL** regions.

- [AWS::OpenSearchService::Domain.EBSOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html)
  - Available in **ALL** regions.

- [AWS::OpenSearchService::Domain.EncryptionAtRestOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-encryptionatrestoptions.html)
  - Available in **ALL** regions.

- [AWS::OpenSearchService::Domain.LogPublishingOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-logpublishingoption.html)
  - Available in **ALL** regions.

- [AWS::OpenSearchService::Domain.MasterUserOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-masteruseroptions.html)
  - Available in **ALL** regions.

- [AWS::OpenSearchService::Domain.NodeToNodeEncryptionOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-nodetonodeencryptionoptions.html)
  - Available in **ALL** regions.

- [AWS::OpenSearchService::Domain.SnapshotOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-snapshotoptions.html)
  - Available in **ALL** regions.

- [AWS::OpenSearchService::Domain.VPCOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-vpcoptions.html)
  - Available in **ALL** regions.

- [AWS::OpenSearchService::Domain.ZoneAwarenessConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-zoneawarenessconfig.html)
  - Available in **ALL** regions.

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Kendra::DataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html)
  - `us-east-2`

- [AWS::Route53Resolver::FirewallDomainList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html)
  - `ap-northeast-3`

- [AWS::Route53Resolver::FirewallRuleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html)
  - `ap-northeast-3`

- [AWS::Route53Resolver::FirewallRuleGroupAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html)
  - `ap-northeast-3`

- [AWS::SageMaker::DataQualityJobDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelBiasJobDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelExplainabilityJobDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelQualityJobDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html)
  - `ap-northeast-3`

- [AWS::SageMaker::MonitoringSchedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html)
  - `ap-northeast-3`

- [AWS::ECS::Cluster.ClusterConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clusterconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::ECS::Cluster.ExecuteCommandConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::ECS::Cluster.ExecuteCommandLogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::Kendra::DataSource.AccessControlListConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-accesscontrollistconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.AclConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-aclconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.ColumnConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.ConfluenceAttachmentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmentconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.ConfluenceAttachmentToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmenttoindexfieldmapping.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.ConfluenceBlogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.ConfluenceBlogToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogtoindexfieldmapping.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.ConfluenceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.ConfluencePageConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepageconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.ConfluencePageToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagetoindexfieldmapping.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.ConfluenceSpaceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.ConfluenceSpaceToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.ConnectionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.DataSourceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.DataSourceToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmapping.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.DataSourceVpcConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcevpcconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.DatabaseConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.DocumentsMetadataConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentsmetadataconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.GoogleDriveConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.OneDriveConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.OneDriveUsers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveusers.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.S3DataSourceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.S3Path](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3path.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.SalesforceChatterFeedConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.SalesforceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.SalesforceCustomKnowledgeArticleTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.SalesforceKnowledgeArticleConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.SalesforceStandardKnowledgeArticleTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.SalesforceStandardObjectAttachmentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.SalesforceStandardObjectConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.ServiceNowConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.ServiceNowKnowledgeArticleConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.ServiceNowServiceCatalogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.SharePointConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html)
  - `us-east-2`

- [AWS::Kendra::DataSource.SqlConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sqlconfiguration.html)
  - `us-east-2`

- [AWS::Route53Resolver::FirewallRuleGroup.FirewallRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html)
  - `ap-northeast-3`

- [AWS::SageMaker::DataQualityJobDefinition.ClusterConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::DataQualityJobDefinition.ConstraintsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-constraintsresource.html)
  - `ap-northeast-3`

- [AWS::SageMaker::DataQualityJobDefinition.DataQualityAppSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html)
  - `ap-northeast-3`

- [AWS::SageMaker::DataQualityJobDefinition.DataQualityBaselineConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::DataQualityJobDefinition.DataQualityJobInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityjobinput.html)
  - `ap-northeast-3`

- [AWS::SageMaker::DataQualityJobDefinition.EndpointInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html)
  - `ap-northeast-3`

- [AWS::SageMaker::DataQualityJobDefinition.MonitoringOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutput.html)
  - `ap-northeast-3`

- [AWS::SageMaker::DataQualityJobDefinition.MonitoringOutputConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutputconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::DataQualityJobDefinition.MonitoringResources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringresources.html)
  - `ap-northeast-3`

- [AWS::SageMaker::DataQualityJobDefinition.NetworkConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-networkconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::DataQualityJobDefinition.S3Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-s3output.html)
  - `ap-northeast-3`

- [AWS::SageMaker::DataQualityJobDefinition.StatisticsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-statisticsresource.html)
  - `ap-northeast-3`

- [AWS::SageMaker::DataQualityJobDefinition.StoppingCondition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-stoppingcondition.html)
  - `ap-northeast-3`

- [AWS::SageMaker::DataQualityJobDefinition.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-vpcconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelBiasJobDefinition.ClusterConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelBiasJobDefinition.ConstraintsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-constraintsresource.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelBiasJobDefinition.EndpointInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelBiasJobDefinition.ModelBiasAppSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelBiasJobDefinition.ModelBiasBaselineConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelBiasJobDefinition.MonitoringGroundTruthS3Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelBiasJobDefinition.MonitoringOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutput.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelBiasJobDefinition.MonitoringOutputConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutputconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelBiasJobDefinition.MonitoringResources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringresources.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelBiasJobDefinition.NetworkConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-networkconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelBiasJobDefinition.S3Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-s3output.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelBiasJobDefinition.StoppingCondition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-stoppingcondition.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelBiasJobDefinition.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-vpcconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.ClusterConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.ConstraintsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-constraintsresource.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.EndpointInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityAppSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.MonitoringOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutput.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.MonitoringOutputConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.MonitoringResources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringresources.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.NetworkConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-networkconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.S3Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-s3output.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.StoppingCondition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-stoppingcondition.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-vpcconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelQualityJobDefinition.ClusterConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelQualityJobDefinition.ConstraintsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-constraintsresource.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelQualityJobDefinition.EndpointInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelQualityJobDefinition.ModelQualityAppSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelQualityJobDefinition.ModelQualityBaselineConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelQualityJobDefinition.MonitoringGroundTruthS3Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelQualityJobDefinition.MonitoringOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutput.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelQualityJobDefinition.MonitoringOutputConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutputconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelQualityJobDefinition.MonitoringResources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringresources.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelQualityJobDefinition.NetworkConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-networkconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelQualityJobDefinition.S3Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-s3output.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelQualityJobDefinition.StoppingCondition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-stoppingcondition.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelQualityJobDefinition.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-vpcconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::MonitoringSchedule.BaselineConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-baselineconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::MonitoringSchedule.ClusterConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::MonitoringSchedule.ConstraintsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-constraintsresource.html)
  - `ap-northeast-3`

- [AWS::SageMaker::MonitoringSchedule.EndpointInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html)
  - `ap-northeast-3`

- [AWS::SageMaker::MonitoringSchedule.MonitoringAppSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html)
  - `ap-northeast-3`

- [AWS::SageMaker::MonitoringSchedule.MonitoringExecutionSummary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html)
  - `ap-northeast-3`

- [AWS::SageMaker::MonitoringSchedule.MonitoringInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringinput.html)
  - `ap-northeast-3`

- [AWS::SageMaker::MonitoringSchedule.MonitoringJobDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html)
  - `ap-northeast-3`

- [AWS::SageMaker::MonitoringSchedule.MonitoringOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutput.html)
  - `ap-northeast-3`

- [AWS::SageMaker::MonitoringSchedule.MonitoringOutputConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutputconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::MonitoringSchedule.MonitoringResources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringresources.html)
  - `ap-northeast-3`

- [AWS::SageMaker::MonitoringSchedule.MonitoringScheduleConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::MonitoringSchedule.NetworkConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::MonitoringSchedule.S3Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html)
  - `ap-northeast-3`

- [AWS::SageMaker::MonitoringSchedule.ScheduleConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-scheduleconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::MonitoringSchedule.StatisticsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-statisticsresource.html)
  - `ap-northeast-3`

- [AWS::SageMaker::MonitoringSchedule.StoppingCondition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-stoppingcondition.html)
  - `ap-northeast-3`

- [AWS::SageMaker::MonitoringSchedule.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-vpcconfig.html)
  - `ap-northeast-3`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v41.1.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v41.1.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v41.1.0: [AWS::SageMaker::DataQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v41.1.0: [AWS::SageMaker::ModelBiasJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-environment.html)
    - `eu-west-3`

  - Since v41.1.0: [AWS::SageMaker::ModelExplainabilityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v41.1.0: [AWS::SageMaker::ModelQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v41.1.0: [AWS::SageMaker::MonitoringSchedule.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-environment.html)
    - `cn-northwest-1`
    - `eu-west-3`

- New PropertyType(s) Missing
  - [AWS::AppSync::DataSource.OpenSearchServiceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-opensearchserviceconfig.html)
    - `us-east-2`
    - `us-west-2`

  - [AWS::Backup::BackupVault.LockConfigurationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html)
    - `eu-central-1`

  - [AWS::IoT::TopicRule.OpenSearchAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html)
    - `cn-north-1`
    - `eu-central-1`
    - `us-west-2`

## [41.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v41.1.0) (2021-09-11)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v41-changelog.json)
  - Change source is a diff between [v41.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v41.1.0) and [v41.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v41.0.0)

### Totals

- TotalPropertyTypes: 2587 **(+0)**
- TotalPropertyTypesSupportedGlobally: 922 **(+1)**
- TotalResourceTypes: 788 **(+1)**
- TotalResourceTypesSupportedGlobally: 325 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::EC2::TransitGatewayVpcAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayvpcattachment.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
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
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Athena::PreparedStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html)
  - `ap-northeast-3`

- [AWS::IoT::FleetMetric](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html)
  - `us-east-2`
  - `cn-northwest-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `eu-north-1`
  - `me-south-1`
  - `ap-south-1`
  - `eu-west-3`
  - `us-gov-west-1`
  - `sa-east-1`
  - `us-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `us-gov-east-1`
  - `ap-southeast-2`

- [AWS::IoTAnalytics::Channel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html)
  - `ap-south-1`

- [AWS::ServiceDiscovery::HttpNamespace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::ServiceDiscovery::Instance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::ServiceDiscovery::PrivateDnsNamespace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::ServiceDiscovery::Service](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::CloudTrail::Trail.InsightSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-insightselector.html)
  - Now available to **ALL** regions.

- [AWS::IoT::FleetMetric.AggregationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-fleetmetric-aggregationtype.html)
  - `us-east-2`
  - `cn-northwest-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `eu-north-1`
  - `me-south-1`
  - `ap-south-1`
  - `eu-west-3`
  - `us-gov-west-1`
  - `sa-east-1`
  - `us-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `us-gov-east-1`
  - `ap-southeast-2`

- [AWS::IoTAnalytics::Channel.ChannelStorage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-channelstorage.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Channel.CustomerManagedS3](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-customermanageds3.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Channel.RetentionPeriod](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-retentionperiod.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Channel.ServiceManagedS3](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-servicemanageds3.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-action.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.ContainerAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-containeraction.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.DatasetContentDeliveryRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryrule.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.DatasetContentDeliveryRuleDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryruledestination.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.DatasetContentVersionValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable-datasetcontentversionvalue.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.DeltaTime](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatime.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.DeltaTimeSessionWindowConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatimesessionwindowconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-filter.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.GlueConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-glueconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.IotEventsDestinationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-ioteventsdestinationconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.LateDataRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-latedatarule.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.LateDataRuleConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-latedataruleconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.OutputFileUriValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable-outputfileurivalue.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.QueryAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-queryaction.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.ResourceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-resourceconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.RetentionPeriod](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-retentionperiod.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.S3DestinationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-s3destinationconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-trigger-schedule.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.Trigger](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-trigger.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.TriggeringDataset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-triggeringdataset.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.Variable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.VersioningConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-versioningconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.Column](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-column.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.CustomerManagedS3](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.CustomerManagedS3Storage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3storage.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.DatastorePartition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartition.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.DatastorePartitions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartitions.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.DatastoreStorage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorestorage.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.FileFormatConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-fileformatconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.IotSiteWiseMultiLayerStorage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-iotsitewisemultilayerstorage.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.JsonConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-jsonconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.ParquetConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-parquetconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.Partition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-partition.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.RetentionPeriod](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-retentionperiod.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.SchemaDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-schemadefinition.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.ServiceManagedS3](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-servicemanageds3.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.TimestampPartition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-timestamppartition.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.Activity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.AddAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-addattributes.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.Channel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-channel.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.Datastore](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-datastore.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.DeviceRegistryEnrich](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.DeviceShadowEnrich](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-filter.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.Lambda](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-lambda.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.Math](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-math.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.RemoveAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-removeattributes.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.SelectAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-selectattributes.html)
  - `ap-south-1`

- [AWS::ServiceDiscovery::PrivateDnsNamespace.PrivateDnsPropertiesMutable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-privatednspropertiesmutable.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::ServiceDiscovery::PrivateDnsNamespace.Properties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-properties.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::ServiceDiscovery::PrivateDnsNamespace.SOA](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-soa.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::ServiceDiscovery::Service.DnsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsconfig.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::ServiceDiscovery::Service.DnsRecord](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsrecord.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::ServiceDiscovery::Service.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckconfig.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::ServiceDiscovery::Service.HealthCheckCustomConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckcustomconfig.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::KinesisAnalyticsV2::Application.CustomArtifactsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactsconfiguration.html)
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v41.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v41.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v41.0.0: [AWS::SageMaker::DataQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v41.0.0: [AWS::SageMaker::ModelBiasJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-environment.html)
    - `eu-west-3`

  - Since v41.0.0: [AWS::SageMaker::ModelExplainabilityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v41.0.0: [AWS::SageMaker::ModelQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v41.0.0: [AWS::SageMaker::MonitoringSchedule.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-environment.html)
    - `cn-northwest-1`
    - `eu-west-3`

## [41.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v41.0.0) (2021-09-03)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v41-changelog.json)
  - Change source is a diff between [v41.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v41.0.0) and [v40.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v40.1.0)

### Totals

- TotalPropertyTypes: 2587 **(+12)**
- TotalPropertyTypesSupportedGlobally: 921 **(+5)**
- TotalResourceTypes: 787 **(+3)**
- TotalResourceTypesSupportedGlobally: 325 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::IoT::FleetMetric](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::S3::MultiRegionAccessPoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
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
  - `us-west-2`

- [AWS::S3::MultiRegionAccessPointPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspointpolicy.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
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
  - `us-west-2`

- [AWS::ACMPCA::CertificateAuthority.OcspConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-ocspconfiguration.html)
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

- [AWS::CloudTrail::Trail.InsightSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-insightselector.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Events::Rule.CapacityProviderStrategyItem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-capacityproviderstrategyitem.html)
  - Available in **ALL** regions.

- [AWS::Events::Rule.PlacementConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-placementconstraint.html)
  - Available in **ALL** regions.

- [AWS::Events::Rule.PlacementStrategy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-placementstrategy.html)
  - Available in **ALL** regions.

- [AWS::Events::Rule.Tag](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-tag.html)
  - Available in **ALL** regions.

- [AWS::IoT::FleetMetric.AggregationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-fleetmetric-aggregationtype.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::KinesisFirehose::DeliveryStream.DynamicPartitioningConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration.html)
  - Available in **ALL** regions.

- [AWS::S3::MultiRegionAccessPoint.PublicAccessBlockConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspoint-publicaccessblockconfiguration.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
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
  - `us-west-2`

- [AWS::S3::MultiRegionAccessPoint.Region](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspoint-region.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
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
  - `us-west-2`

- [AWS::Transfer::Server.WorkflowDetail](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetail.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
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

- [AWS::Transfer::Server.WorkflowDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetails.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
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

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::CustomerProfiles::Domain](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::ObjectType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html)
  - `ca-central-1`

- [AWS::DataSync::LocationFSxWindows](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html)
  - `ap-northeast-3`

- [AWS::CustomerProfiles::Integration.ConnectorOperator](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.FlowDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.IncrementalPullConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-incrementalpullconfig.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.MarketoSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-marketosourceproperties.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.S3SourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.SalesforceSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.ScheduledTriggerProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.ServiceNowSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-servicenowsourceproperties.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.SourceConnectorProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.SourceFlowConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.Task](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.TaskPropertiesMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.TriggerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.TriggerProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerproperties.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.ZendeskSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-zendesksourceproperties.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::ObjectType.FieldMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::ObjectType.KeyMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::ObjectType.ObjectTypeField](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::ObjectType.ObjectTypeKey](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html)
  - `ca-central-1`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::SageMaker::DataQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-environment.html)
  - `ap-south-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `ap-southeast-2`
  - `eu-west-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `us-east-1`
  - `eu-west-1`
  - `us-west-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `us-east-2`

- [AWS::SageMaker::ModelBiasJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-environment.html)
  - `ap-south-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `ap-southeast-2`
  - `eu-west-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `us-east-1`
  - `eu-west-1`
  - `us-west-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `us-east-2`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-environment.html)
  - `ap-south-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `ap-southeast-2`
  - `eu-west-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `us-east-1`
  - `eu-west-1`
  - `us-west-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `us-east-2`

- [AWS::SageMaker::ModelQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-environment.html)
  - `ap-south-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `ap-southeast-2`
  - `eu-west-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `us-east-1`
  - `eu-west-1`
  - `us-west-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `us-east-2`

- [AWS::SageMaker::MonitoringSchedule.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-environment.html)
  - `ap-south-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `ap-southeast-2`
  - `eu-west-2`
  - `cn-north-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `sa-east-1`
  - `us-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-west-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `us-east-2`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v40.1.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v40.1.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v40.1.0: [AWS::SageMaker::DataQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v40.1.0: [AWS::SageMaker::ModelBiasJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-environment.html)
    - `eu-west-3`

  - Since v40.1.0: [AWS::SageMaker::ModelExplainabilityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v40.1.0: [AWS::SageMaker::ModelQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v40.1.0: [AWS::SageMaker::MonitoringSchedule.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-environment.html)
    - `cn-northwest-1`
    - `eu-west-3`

