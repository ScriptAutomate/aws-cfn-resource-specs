# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v39-changelog.json`](changelogs/v39-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [39.10.0](#39100-2021-08-13)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)
- [39.9.0](#3990-2021-08-06)
  - [Totals](#totals-1)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-1)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-1)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-1)
- [39.8.0](#3980-2021-07-30)
  - [Totals](#totals-2)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-2)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-2)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-2)
- [39.7.0](#3970-2021-07-22)
  - [Totals](#totals-3)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-3)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-3)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-3)
- [39.6.0](#3960-2021-07-17)
  - [Totals](#totals-4)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-4)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-4)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-4)
- [39.5.0](#3950-2021-07-09)
  - [Totals](#totals-5)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-5)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-5)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-5)
- [39.3.0](#3930-2021-06-25)
  - [Totals](#totals-6)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-6)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-6)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-6)
- [39.2.0](#3920-2021-06-18)
  - [Totals](#totals-7)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-7)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-7)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-7)
- [39.1.0](#3910-2021-06-11)
  - [Totals](#totals-8)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-8)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-8)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-8)

## [39.10.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.10.0) (2021-08-13)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v39-changelog.json)
  - Change source is a diff between [v39.10.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.10.0) and [v39.9.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.9.0)

### Totals

- TotalPropertyTypes: 2566 **(+4)**
- TotalPropertyTypesSupportedGlobally: 906 **(+12)**
- TotalResourceTypes: 784 **(+1)**
- TotalResourceTypesSupportedGlobally: 322 **(+1)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::WAFv2::LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html)
  - Available in **ALL** regions.

- [AWS::Elasticsearch::Domain.ColdStorageOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-coldstorageoptions.html)
  - Available in **ALL** regions.

- [AWS::IoTAnalytics::Datastore.CustomerManagedS3Storage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3storage.html)
  - `ap-northeast-1`
  - `ap-southeast-2`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::IoTAnalytics::Datastore.IotSiteWiseMultiLayerStorage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-iotsitewisemultilayerstorage.html)
  - `ap-northeast-1`
  - `ap-southeast-2`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::WAFv2::LoggingConfiguration.FieldToMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html)
  - Available in **ALL** regions.

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Cassandra::Table.EncryptionSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html)
  - `cn-northwest-1`
  - `ap-northeast-2`

- [AWS::ECR::Repository.EncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-encryptionconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::ECR::Repository.ImageScanningConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-imagescanningconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::FSx::FileSystem.AuditLogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-auditlogconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Crawler.RecrawlPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-recrawlpolicy.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Database.DataLakePrincipal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-datalakeprincipal.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `ap-east-1`

- [AWS::Glue::Database.DatabaseIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseidentifier.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Database.PrincipalPrivileges](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-principalprivileges.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `ap-east-1`

- [AWS::Glue::MLTransform.MLUserDataEncryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformencryption-mluserdataencryption.html)
  - `ap-east-1`
  - `af-south-1`
  - `me-south-1`

- [AWS::Glue::MLTransform.TransformEncryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformencryption.html)
  - `ap-east-1`
  - `af-south-1`
  - `me-south-1`

- [AWS::Glue::Partition.SchemaId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemaid.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Partition.SchemaReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemareference.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Table.SchemaId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemaid.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Table.SchemaReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemareference.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Table.TableIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableidentifier.html)
  - Now available to **ALL** regions.

- [AWS::IoTAnalytics::Datastore.DatastorePartition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartition.html)
  - `cn-north-1`

- [AWS::IoTAnalytics::Datastore.DatastorePartitions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartitions.html)
  - `cn-north-1`

- [AWS::IoTAnalytics::Datastore.Partition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-partition.html)
  - `cn-north-1`

- [AWS::IoTAnalytics::Datastore.TimestampPartition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-timestamppartition.html)
  - `cn-north-1`

- [AWS::SageMaker::Model.RepositoryAuthConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig-repositoryauthconfig.html)
  - `cn-northwest-1`
  - `us-gov-west-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v39.9.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v39.9.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

## [39.9.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.9.0) (2021-08-06)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v39-changelog.json)
  - Change source is a diff between [v39.9.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.9.0) and [v39.8.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.8.0)

### Totals

- TotalPropertyTypes: 2562 **(+3)**
- TotalPropertyTypesSupportedGlobally: 894 **(+7)**
- TotalResourceTypes: 783 **(+1)**
- TotalResourceTypesSupportedGlobally: 321 **(+1)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::Athena::PreparedStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html)
  - `af-south-1`
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
  - `us-west-1`
  - `us-west-2`

- [AWS::SageMaker::Model.RepositoryAuthConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig-repositoryauthconfig.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-north-1`
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
  - `us-west-1`
  - `us-west-2`

- [AWS::Synthetics::Canary.BaseScreenshot](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-basescreenshot.html)
  - Available in **ALL** regions.

- [AWS::Synthetics::Canary.VisualReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-visualreference.html)
  - Available in **ALL** regions.

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::DataSync::Agent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html)
  - `ap-northeast-3`

- [AWS::DataSync::LocationEFS](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html)
  - `ap-northeast-3`

- [AWS::DataSync::LocationNFS](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html)
  - `ap-northeast-3`

- [AWS::DataSync::LocationObjectStorage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html)
  - `ap-northeast-3`

- [AWS::DataSync::LocationS3](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html)
  - `ap-northeast-3`

- [AWS::DataSync::LocationSMB](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html)
  - `ap-northeast-3`

- [AWS::DataSync::Task](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html)
  - `ap-northeast-3`

- [AWS::FSx::FileSystem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html)
  - Now available to **ALL** regions.

- [AWS::AppSync::GraphQLApi.LambdaAuthorizerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html)
  - `eu-south-1`
  - `ap-south-1`
  - `ap-northeast-3`
  - `us-east-1`
  - `us-west-1`
  - `cn-north-1`
  - `cn-northwest-1`
  - `ap-east-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `eu-west-1`
  - `ca-central-1`

- [AWS::DLM::LifecyclePolicy.CrossRegionCopyDeprecateRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule.html)
  - Now available to **ALL** regions.

- [AWS::DLM::LifecyclePolicy.DeprecateRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html)
  - Now available to **ALL** regions.

- [AWS::DataSync::LocationEFS.Ec2Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationefs-ec2config.html)
  - `ap-northeast-3`

- [AWS::DataSync::LocationNFS.MountOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-mountoptions.html)
  - `ap-northeast-3`

- [AWS::DataSync::LocationNFS.OnPremConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-onpremconfig.html)
  - `ap-northeast-3`

- [AWS::DataSync::LocationS3.S3Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locations3-s3config.html)
  - `ap-northeast-3`

- [AWS::DataSync::LocationSMB.MountOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationsmb-mountoptions.html)
  - `ap-northeast-3`

- [AWS::DataSync::Task.FilterRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-filterrule.html)
  - `ap-northeast-3`

- [AWS::DataSync::Task.Options](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html)
  - `ap-northeast-3`

- [AWS::DataSync::Task.TaskSchedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskschedule.html)
  - `ap-northeast-3`

- [AWS::FSx::FileSystem.AuditLogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-auditlogconfiguration.html)
  - `ap-southeast-2`
  - `eu-central-1`
  - `ap-southeast-1`
  - `eu-north-1`
  - `ap-northeast-1`
  - `ap-northeast-3`
  - `ap-east-1`

- [AWS::FSx::FileSystem.LustreConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::FSx::FileSystem.SelfManagedActiveDirectoryConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::FSx::FileSystem.WindowsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Database.DataLakePrincipal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-datalakeprincipal.html)
  - `us-gov-west-1`

- [AWS::Glue::Database.PrincipalPrivileges](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-principalprivileges.html)
  - `us-gov-west-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v39.8.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v39.8.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

## [39.8.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.8.0) (2021-07-30)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v39-changelog.json)
  - Change source is a diff between [v39.8.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.8.0) and [v39.7.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.7.0)

### Totals

- TotalPropertyTypes: 2559 **(+20)**
- TotalPropertyTypesSupportedGlobally: 887 **(+0)**
- TotalResourceTypes: 782 **(+8)**
- TotalResourceTypesSupportedGlobally: 320 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::Route53RecoveryControl::Cluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-cluster.html)
  - `us-east-1`
  - `us-west-2`

- [AWS::Route53RecoveryControl::ControlPanel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-controlpanel.html)
  - `us-east-1`
  - `us-west-2`

- [AWS::Route53RecoveryControl::RoutingControl](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-routingcontrol.html)
  - `us-east-1`
  - `us-west-2`

- [AWS::Route53RecoveryControl::SafetyRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoverycontrol-safetyrule.html)
  - `us-east-1`
  - `us-west-2`

- [AWS::Route53RecoveryReadiness::Cell](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-cell.html)
  - `us-east-1`
  - `us-west-2`

- [AWS::Route53RecoveryReadiness::ReadinessCheck](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-readinesscheck.html)
  - `us-east-1`
  - `us-west-2`

- [AWS::Route53RecoveryReadiness::RecoveryGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-recoverygroup.html)
  - `us-east-1`
  - `us-west-2`

- [AWS::Route53RecoveryReadiness::ResourceSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53recoveryreadiness-resourceset.html)
  - `us-east-1`
  - `us-west-2`

- [AWS::AppSync::GraphQLApi.LambdaAuthorizerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html)
  - `us-east-2`
  - `us-west-2`

- [AWS::DLM::LifecyclePolicy.CrossRegionCopyDeprecateRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DLM::LifecyclePolicy.DeprecateRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DataBrew::Job.ColumnSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-columnselector.html)
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
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::DataBrew::Job.ColumnStatisticsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-columnstatisticsconfiguration.html)
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
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::DataBrew::Job.DatabaseOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databaseoutput.html)
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
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::DataBrew::Job.ParameterMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-parametermap.html)
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
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::DataBrew::Job.ProfileConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-profileconfiguration.html)
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
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::DataBrew::Job.StatisticOverride](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticoverride.html)
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
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::DataBrew::Job.StatisticsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticsconfiguration.html)
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
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::FSx::FileSystem.AuditLogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-auditlogconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Route53RecoveryControl::Cluster.ClusterEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-cluster-clusterendpoint.html)
  - `us-east-1`
  - `us-west-2`

- [AWS::Route53RecoveryControl::SafetyRule.AssertionRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-assertionrule.html)
  - `us-east-1`
  - `us-west-2`

- [AWS::Route53RecoveryControl::SafetyRule.GatingRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-gatingrule.html)
  - `us-east-1`
  - `us-west-2`

- [AWS::Route53RecoveryControl::SafetyRule.RuleConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoverycontrol-safetyrule-ruleconfig.html)
  - `us-east-1`
  - `us-west-2`

- [AWS::Route53RecoveryReadiness::ResourceSet.DNSTargetResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-dnstargetresource.html)
  - `us-east-1`
  - `us-west-2`

- [AWS::Route53RecoveryReadiness::ResourceSet.NLBResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-nlbresource.html)
  - `us-east-1`
  - `us-west-2`

- [AWS::Route53RecoveryReadiness::ResourceSet.R53ResourceRecord](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord.html)
  - `us-east-1`
  - `us-west-2`

- [AWS::Route53RecoveryReadiness::ResourceSet.Resource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-resource.html)
  - `us-east-1`
  - `us-west-2`

- [AWS::Route53RecoveryReadiness::ResourceSet.TargetResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53recoveryreadiness-resourceset-targetresource.html)
  - `us-east-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Cloud9::EnvironmentEC2](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html)
  - `af-south-1`

- [AWS::DataBrew::Dataset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html)
  - `eu-south-1`

- [AWS::DataBrew::Job](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html)
  - `eu-south-1`

- [AWS::DataBrew::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html)
  - `eu-south-1`

- [AWS::DataBrew::Recipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html)
  - `eu-south-1`

- [AWS::DataBrew::Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html)
  - `eu-south-1`

- [AWS::SSO::Assignment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html)
  - `eu-west-3`

- [AWS::SSO::InstanceAccessControlAttributeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html)
  - `eu-west-3`

- [AWS::SSO::PermissionSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html)
  - `eu-west-3`

- [AWS::Cloud9::EnvironmentEC2.Repository](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloud9-environmentec2-repository.html)
  - `af-south-1`

- [AWS::DataBrew::Dataset.CsvOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-csvoptions.html)
  - `eu-south-1`

- [AWS::DataBrew::Dataset.DataCatalogInputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datacataloginputdefinition.html)
  - `eu-south-1`

- [AWS::DataBrew::Dataset.DatabaseInputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-databaseinputdefinition.html)
  - `eu-south-1`

- [AWS::DataBrew::Dataset.DatasetParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datasetparameter.html)
  - `eu-south-1`

- [AWS::DataBrew::Dataset.DatetimeOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datetimeoptions.html)
  - `eu-south-1`

- [AWS::DataBrew::Dataset.ExcelOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-exceloptions.html)
  - `eu-south-1`

- [AWS::DataBrew::Dataset.FilesLimit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-fileslimit.html)
  - `eu-south-1`

- [AWS::DataBrew::Dataset.FilterExpression](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filterexpression.html)
  - `eu-south-1`

- [AWS::DataBrew::Dataset.FilterValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filtervalue.html)
  - `eu-south-1`

- [AWS::DataBrew::Dataset.FormatOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-formatoptions.html)
  - `eu-south-1`

- [AWS::DataBrew::Dataset.Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-input.html)
  - `eu-south-1`

- [AWS::DataBrew::Dataset.JsonOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-jsonoptions.html)
  - `eu-south-1`

- [AWS::DataBrew::Dataset.PathOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathoptions.html)
  - `eu-south-1`

- [AWS::DataBrew::Dataset.PathParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathparameter.html)
  - `eu-south-1`

- [AWS::DataBrew::Dataset.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-s3location.html)
  - `eu-south-1`

- [AWS::DataBrew::Job.CsvOutputOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-csvoutputoptions.html)
  - `eu-south-1`

- [AWS::DataBrew::Job.DataCatalogOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html)
  - `eu-south-1`

- [AWS::DataBrew::Job.DatabaseTableOutputOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databasetableoutputoptions.html)
  - `eu-south-1`

- [AWS::DataBrew::Job.JobSample](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-jobsample.html)
  - `eu-south-1`

- [AWS::DataBrew::Job.Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html)
  - `eu-south-1`

- [AWS::DataBrew::Job.OutputFormatOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputformatoptions.html)
  - `eu-south-1`

- [AWS::DataBrew::Job.OutputLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputlocation.html)
  - `eu-south-1`

- [AWS::DataBrew::Job.Recipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-recipe.html)
  - `eu-south-1`

- [AWS::DataBrew::Job.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3location.html)
  - `eu-south-1`

- [AWS::DataBrew::Job.S3TableOutputOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3tableoutputoptions.html)
  - `eu-south-1`

- [AWS::DataBrew::Project.Sample](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-project-sample.html)
  - `eu-south-1`

- [AWS::DataBrew::Recipe.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-action.html)
  - `eu-south-1`

- [AWS::DataBrew::Recipe.ConditionExpression](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-conditionexpression.html)
  - `eu-south-1`

- [AWS::DataBrew::Recipe.DataCatalogInputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-datacataloginputdefinition.html)
  - `eu-south-1`

- [AWS::DataBrew::Recipe.ParameterMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-parametermap.html)
  - `eu-south-1`

- [AWS::DataBrew::Recipe.RecipeParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html)
  - `eu-south-1`

- [AWS::DataBrew::Recipe.RecipeStep](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipestep.html)
  - `eu-south-1`

- [AWS::DataBrew::Recipe.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-s3location.html)
  - `eu-south-1`

- [AWS::DataBrew::Recipe.SecondaryInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-secondaryinput.html)
  - `eu-south-1`

- [AWS::LookoutMetrics::Alert.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-action.html)
  - `ap-southeast-2`
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-1`
  - `eu-central-1`

- [AWS::LookoutMetrics::Alert.LambdaConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-lambdaconfiguration.html)
  - `ap-southeast-2`
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-1`
  - `eu-central-1`

- [AWS::LookoutMetrics::Alert.SNSConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-snsconfiguration.html)
  - `ap-southeast-2`
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-1`
  - `eu-central-1`

- [AWS::LookoutMetrics::AnomalyDetector.AnomalyDetectorConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-anomalydetectorconfig.html)
  - `us-east-2`
  - `eu-north-1`
  - `ap-southeast-2`
  - `eu-west-1`

- [AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html)
  - `eu-west-3`

- [AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttributeValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html)
  - `eu-west-3`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::Glue::Crawler.RecrawlPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-recrawlpolicy.html)
  - `cn-northwest-1`

- [AWS::Glue::Database.DataLakePrincipal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-datalakeprincipal.html)
  - `cn-northwest-1`

- [AWS::Glue::Database.DatabaseIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseidentifier.html)
  - `cn-northwest-1`

- [AWS::Glue::Database.PrincipalPrivileges](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-principalprivileges.html)
  - `cn-northwest-1`

- [AWS::Glue::Partition.SchemaId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemaid.html)
  - `cn-northwest-1`

- [AWS::Glue::Partition.SchemaReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemareference.html)
  - `cn-northwest-1`

- [AWS::Glue::Table.SchemaId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemaid.html)
  - `cn-northwest-1`

- [AWS::Glue::Table.SchemaReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemareference.html)
  - `cn-northwest-1`

- [AWS::Glue::Table.TableIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableidentifier.html)
  - `cn-northwest-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v39.7.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v39.7.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::AppSync::GraphQLApi.LambdaAuthorizerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html)
    - `us-east-2`
    - `us-west-2`

## [39.7.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.7.0) (2021-07-22)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v39-changelog.json)
  - Change source is a diff between [v39.7.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.7.0) and [v39.6.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.6.0)

### Totals

- TotalPropertyTypes: 2539 **(+4)**
- TotalPropertyTypesSupportedGlobally: 887 **(+3)**
- TotalResourceTypes: 774 **(+1)**
- TotalResourceTypesSupportedGlobally: 320 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::LookoutEquipment::InferenceScheduler](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html)
  - `ap-northeast-2`
  - `eu-west-1`
  - `us-east-1`

- [AWS::LookoutMetrics::Alert.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-action.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::LookoutMetrics::Alert.LambdaConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-lambdaconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::LookoutMetrics::Alert.SNSConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-snsconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::LookoutMetrics::AnomalyDetector.AnomalyDetectorConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-anomalydetectorconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-east-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::EC2::LocalGatewayRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.html)
  - `ap-northeast-3`

- [AWS::Glue::Registry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-registry.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Glue::Schema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Glue::SchemaVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Glue::SchemaVersionMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversionmetadata.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Cassandra::Table.EncryptionSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html)
  - `eu-west-2`
  - `us-west-2`
  - `ap-southeast-1`
  - `eu-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `sa-east-1`
  - `us-east-2`
  - `me-south-1`
  - `ap-northeast-1`
  - `eu-west-3`
  - `ca-central-1`
  - `cn-north-1`
  - `ap-east-1`
  - `ap-south-1`
  - `us-east-1`
  - `ap-southeast-2`

- [AWS::Glue::Crawler.RecrawlPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-recrawlpolicy.html)
  - `us-west-1`
  - `eu-north-1`
  - `sa-east-1`
  - `eu-south-1`
  - `eu-west-3`
  - `ca-central-1`
  - `cn-north-1`
  - `ap-south-1`

- [AWS::Glue::Database.DataLakePrincipal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-datalakeprincipal.html)
  - `us-west-1`
  - `eu-north-1`
  - `sa-east-1`
  - `eu-south-1`
  - `eu-west-3`
  - `ca-central-1`
  - `cn-north-1`
  - `ap-south-1`
  - `ap-northeast-3`

- [AWS::Glue::Database.DatabaseIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseidentifier.html)
  - `eu-north-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-south-1`

- [AWS::Glue::Database.PrincipalPrivileges](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-principalprivileges.html)
  - `us-west-1`
  - `eu-north-1`
  - `sa-east-1`
  - `eu-south-1`
  - `eu-west-3`
  - `ca-central-1`
  - `cn-north-1`
  - `ap-south-1`
  - `ap-northeast-3`

- [AWS::Glue::MLTransform.MLUserDataEncryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformencryption-mluserdataencryption.html)
  - `eu-north-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-south-1`

- [AWS::Glue::MLTransform.TransformEncryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformencryption.html)
  - `eu-north-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-south-1`

- [AWS::Glue::Partition.SchemaId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemaid.html)
  - `eu-north-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-south-1`

- [AWS::Glue::Partition.SchemaReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemareference.html)
  - `eu-north-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-south-1`

- [AWS::Glue::Schema.Registry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schema-registry.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Glue::Schema.SchemaVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schema-schemaversion.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Glue::SchemaVersion.Schema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schemaversion-schema.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Glue::Table.SchemaId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemaid.html)
  - `eu-north-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-south-1`

- [AWS::Glue::Table.SchemaReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemareference.html)
  - `eu-north-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-south-1`

- [AWS::Glue::Table.TableIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableidentifier.html)
  - `eu-north-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-south-1`

- [AWS::ImageBuilder::ImageRecipe.AdditionalInstanceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-additionalinstanceconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::ImageRecipe.ComponentParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentparameter.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::ImageRecipe.SystemsManagerAgent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-systemsmanageragent.html)
  - Now available to **ALL** regions.

- [AWS::Redshift::Cluster.Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-endpoint.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v39.6.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v39.6.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

## [39.6.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.6.0) (2021-07-17)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v39-changelog.json)
  - Change source is a diff between [v39.6.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.6.0) and [v39.5.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.5.0)

### Totals

- TotalPropertyTypes: 2535 **(+4)**
- TotalPropertyTypesSupportedGlobally: 884 **(+0)**
- TotalResourceTypes: 773 **(+1)**
- TotalResourceTypesSupportedGlobally: 320 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::Logs::ResourcePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-resourcepolicy.html)
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::Cassandra::Table.EncryptionSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html)
  - `eu-central-1`

- [AWS::ImageBuilder::ImageRecipe.AdditionalInstanceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-additionalinstanceconfiguration.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::ImageBuilder::ImageRecipe.ComponentParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentparameter.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::ImageBuilder::ImageRecipe.SystemsManagerAgent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-systemsmanageragent.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::DataBrew::Dataset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html)
  - `ap-east-1`

- [AWS::DataBrew::Job](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html)
  - `ap-east-1`

- [AWS::DataBrew::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html)
  - `ap-east-1`

- [AWS::DataBrew::Recipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html)
  - `ap-east-1`

- [AWS::DataBrew::Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html)
  - `ap-east-1`

- [AWS::IoTWireless::Destination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::IoTWireless::DeviceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::IoTWireless::ServiceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::IoTWireless::TaskDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::IoTWireless::WirelessDevice](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::IoTWireless::WirelessGateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::DataBrew::Dataset.CsvOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-csvoptions.html)
  - `ap-east-1`

- [AWS::DataBrew::Dataset.DataCatalogInputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datacataloginputdefinition.html)
  - `ap-east-1`

- [AWS::DataBrew::Dataset.DatabaseInputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-databaseinputdefinition.html)
  - `ap-east-1`

- [AWS::DataBrew::Dataset.DatasetParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datasetparameter.html)
  - `ap-east-1`

- [AWS::DataBrew::Dataset.DatetimeOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datetimeoptions.html)
  - `ap-east-1`

- [AWS::DataBrew::Dataset.ExcelOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-exceloptions.html)
  - `ap-east-1`

- [AWS::DataBrew::Dataset.FilesLimit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-fileslimit.html)
  - `ap-east-1`

- [AWS::DataBrew::Dataset.FilterExpression](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filterexpression.html)
  - `ap-east-1`

- [AWS::DataBrew::Dataset.FilterValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filtervalue.html)
  - `ap-east-1`

- [AWS::DataBrew::Dataset.FormatOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-formatoptions.html)
  - `ap-east-1`

- [AWS::DataBrew::Dataset.Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-input.html)
  - `ap-east-1`

- [AWS::DataBrew::Dataset.JsonOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-jsonoptions.html)
  - `ap-east-1`

- [AWS::DataBrew::Dataset.PathOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathoptions.html)
  - `ap-east-1`

- [AWS::DataBrew::Dataset.PathParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathparameter.html)
  - `ap-east-1`

- [AWS::DataBrew::Dataset.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-s3location.html)
  - `ap-east-1`

- [AWS::DataBrew::Job.CsvOutputOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-csvoutputoptions.html)
  - `ap-east-1`

- [AWS::DataBrew::Job.DataCatalogOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html)
  - `ca-central-1`
  - `us-east-2`
  - `sa-east-1`
  - `eu-north-1`
  - `eu-west-2`
  - `ap-south-1`
  - `cn-northwest-1`
  - `ap-southeast-2`
  - `ap-east-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-west-1`
  - `us-west-1`

- [AWS::DataBrew::Job.DatabaseTableOutputOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databasetableoutputoptions.html)
  - `ca-central-1`
  - `us-east-2`
  - `sa-east-1`
  - `eu-north-1`
  - `eu-west-2`
  - `ap-south-1`
  - `cn-northwest-1`
  - `ap-southeast-2`
  - `ap-east-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-west-1`
  - `us-west-1`

- [AWS::DataBrew::Job.JobSample](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-jobsample.html)
  - `ap-east-1`

- [AWS::DataBrew::Job.Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html)
  - `ap-east-1`

- [AWS::DataBrew::Job.OutputFormatOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputformatoptions.html)
  - `ap-east-1`

- [AWS::DataBrew::Job.OutputLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputlocation.html)
  - `ap-east-1`

- [AWS::DataBrew::Job.Recipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-recipe.html)
  - `ap-east-1`

- [AWS::DataBrew::Job.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3location.html)
  - `ap-east-1`

- [AWS::DataBrew::Job.S3TableOutputOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3tableoutputoptions.html)
  - `ca-central-1`
  - `us-east-2`
  - `sa-east-1`
  - `eu-north-1`
  - `eu-west-2`
  - `ap-south-1`
  - `cn-northwest-1`
  - `ap-southeast-2`
  - `ap-east-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-west-1`
  - `us-west-1`

- [AWS::DataBrew::Project.Sample](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-project-sample.html)
  - `ap-east-1`

- [AWS::DataBrew::Recipe.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-action.html)
  - `ap-east-1`

- [AWS::DataBrew::Recipe.ConditionExpression](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-conditionexpression.html)
  - `ap-east-1`

- [AWS::DataBrew::Recipe.DataCatalogInputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-datacataloginputdefinition.html)
  - `ap-east-1`

- [AWS::DataBrew::Recipe.ParameterMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-parametermap.html)
  - `ap-east-1`

- [AWS::DataBrew::Recipe.RecipeParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html)
  - `ap-east-1`

- [AWS::DataBrew::Recipe.RecipeStep](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipestep.html)
  - `ap-east-1`

- [AWS::DataBrew::Recipe.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-s3location.html)
  - `ap-east-1`

- [AWS::DataBrew::Recipe.SecondaryInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-secondaryinput.html)
  - `ap-east-1`

- [AWS::Glue::Crawler.RecrawlPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-recrawlpolicy.html)
  - `us-west-2`
  - `ap-southeast-1`
  - `us-east-1`
  - `eu-west-2`
  - `cn-northwest-1`
  - `eu-central-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `ap-southeast-2`

- [AWS::Glue::Database.DataLakePrincipal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-datalakeprincipal.html)
  - `us-west-2`
  - `us-east-2`
  - `ap-southeast-1`
  - `us-east-1`
  - `eu-west-2`
  - `cn-northwest-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `eu-west-1`
  - `ap-southeast-2`

- [AWS::Glue::Database.DatabaseIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseidentifier.html)
  - `cn-northwest-1`

- [AWS::Glue::Database.PrincipalPrivileges](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-principalprivileges.html)
  - `us-west-2`
  - `us-east-2`
  - `ap-southeast-1`
  - `us-east-1`
  - `eu-west-2`
  - `cn-northwest-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `eu-west-1`
  - `ap-southeast-2`

- [AWS::Glue::Partition.SchemaId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemaid.html)
  - `cn-northwest-1`

- [AWS::Glue::Partition.SchemaReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemareference.html)
  - `cn-northwest-1`

- [AWS::Glue::Table.SchemaId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemaid.html)
  - `cn-northwest-1`

- [AWS::Glue::Table.SchemaReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemareference.html)
  - `cn-northwest-1`

- [AWS::Glue::Table.TableIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableidentifier.html)
  - `cn-northwest-1`

- [AWS::IoTWireless::DeviceProfile.LoRaWANDeviceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::IoTWireless::ServiceProfile.LoRaWANServiceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::IoTWireless::TaskDefinition.LoRaWANGatewayVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::IoTWireless::TaskDefinition.LoRaWANUpdateGatewayTaskCreate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::IoTWireless::TaskDefinition.LoRaWANUpdateGatewayTaskEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::IoTWireless::TaskDefinition.UpdateWirelessGatewayTaskCreate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::IoTWireless::WirelessDevice.AbpV10x](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::IoTWireless::WirelessDevice.AbpV11](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::IoTWireless::WirelessDevice.LoRaWANDevice](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::IoTWireless::WirelessDevice.OtaaV10x](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::IoTWireless::WirelessDevice.OtaaV11](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::IoTWireless::WirelessDevice.SessionKeysAbpV10x](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::IoTWireless::WirelessDevice.SessionKeysAbpV11](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::IoTWireless::WirelessGateway.LoRaWANGateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html)
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v39.5.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v39.5.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::Cassandra::Table.EncryptionSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html)
    - `eu-central-1`

## [39.5.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.5.0) (2021-07-09)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v39-changelog.json)
  - Change source is a diff between [v39.5.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.5.0) and [v39.3.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.3.0)

### Totals

- TotalPropertyTypes: 2531 **(+11)**
- TotalPropertyTypesSupportedGlobally: 884 **(+196)**
- TotalResourceTypes: 772 **(+0)**
- TotalResourceTypesSupportedGlobally: 320 **(+85)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::CodeDeploy::DeploymentConfig.TimeBasedCanary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-timebasedcanary.html)
  - Available in **ALL** regions.

- [AWS::CodeDeploy::DeploymentConfig.TimeBasedLinear](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-timebasedlinear.html)
  - Available in **ALL** regions.

- [AWS::CodeDeploy::DeploymentConfig.TrafficRoutingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-trafficroutingconfig.html)
  - Available in **ALL** regions.

- [AWS::CodeDeploy::DeploymentGroup.BlueGreenDeploymentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-bluegreendeploymentconfiguration.html)
  - Available in **ALL** regions.

- [AWS::CodeDeploy::DeploymentGroup.BlueInstanceTerminationOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-blueinstanceterminationoption.html)
  - Available in **ALL** regions.

- [AWS::CodeDeploy::DeploymentGroup.DeploymentReadyOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentreadyoption.html)
  - Available in **ALL** regions.

- [AWS::CodeDeploy::DeploymentGroup.ECSService](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ecsservice.html)
  - Available in **ALL** regions.

- [AWS::CodeDeploy::DeploymentGroup.GreenFleetProvisioningOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-greenfleetprovisioningoption.html)
  - Available in **ALL** regions.

- [AWS::Glue::Crawler.RecrawlPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-recrawlpolicy.html)
  - `ap-northeast-3`
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Glue::Database.DataLakePrincipal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-datalakeprincipal.html)
  - `me-south-1`

- [AWS::Glue::Database.PrincipalPrivileges](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-principalprivileges.html)
  - `me-south-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::AmazonMQ::Broker](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-west-2`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`

- [AWS::AmazonMQ::Configuration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-west-2`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`

- [AWS::AmazonMQ::ConfigurationAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configurationassociation.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-west-2`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`

- [AWS::Amplify::Domain](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html)
  - `eu-north-1`
  - `us-west-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::ApiGateway::VpcLink](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-vpclink.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::ApiGatewayManagedOverrides](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::VpcLink](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html)
  - Now available to **ALL** regions.

- [AWS::AppConfig::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html)
  - Now available to **ALL** regions.

- [AWS::AppConfig::ConfigurationProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html)
  - Now available to **ALL** regions.

- [AWS::AppConfig::Deployment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html)
  - Now available to **ALL** regions.

- [AWS::AppConfig::DeploymentStrategy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html)
  - Now available to **ALL** regions.

- [AWS::AppConfig::Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html)
  - Now available to **ALL** regions.

- [AWS::AppConfig::HostedConfigurationVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html)
  - Now available to **ALL** regions.

- [AWS::AppMesh::GatewayRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::Mesh](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualGateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualNode](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualRouter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualService](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppStream::DirectoryConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-directoryconfig.html)
  - `us-west-1`
  - `cn-northwest-1`
  - `us-east-2`
  - `eu-west-2`

- [AWS::AppStream::Fleet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html)
  - `us-west-1`
  - `cn-northwest-1`
  - `us-east-2`
  - `eu-west-2`

- [AWS::AppStream::ImageBuilder](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html)
  - `us-west-1`
  - `cn-northwest-1`
  - `us-east-2`
  - `eu-west-2`

- [AWS::AppStream::Stack](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html)
  - `us-west-1`
  - `cn-northwest-1`
  - `us-east-2`
  - `eu-west-2`

- [AWS::AppStream::StackFleetAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackfleetassociation.html)
  - `us-west-1`
  - `cn-northwest-1`
  - `us-east-2`
  - `eu-west-2`

- [AWS::AppStream::StackUserAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackuserassociation.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `us-east-2`
  - `cn-northwest-1`
  - `eu-west-2`

- [AWS::AppStream::User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `us-east-2`
  - `cn-northwest-1`
  - `eu-west-2`

- [AWS::AppSync::ApiCache](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::ApiKey](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html)
  - `eu-north-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::AppSync::DataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::FunctionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::GraphQLApi](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::GraphQLSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html)
  - `eu-north-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::Resolver](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AutoScalingPlans::ScalingPlan](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html)
  - `ap-northeast-3`
  - `af-south-1`
  - `eu-south-1`

- [AWS::Batch::ComputeEnvironment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobQueue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html)
  - Now available to **ALL** regions.

- [AWS::Budgets::Budget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html)
  - `eu-west-3`

- [AWS::CloudFront::StreamingDistribution](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html)
  - `eu-north-1`
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `cn-north-1`

- [AWS::CloudWatch::AnomalyDetector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::ReportGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::SourceCredential](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html)
  - Now available to **ALL** regions.

- [AWS::CodeCommit::Repository](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html)
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-west-3`
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-gov-east-1`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::CodePipeline::Webhook](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-webhook.html)
  - `us-gov-west-1`
  - `eu-south-1`
  - `eu-north-1`
  - `ap-east-1`

- [AWS::Cognito::IdentityPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `me-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::IdentityPoolRoleAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolroleattachment.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolClient](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolDomain](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooldomain.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `me-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolIdentityProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolidentityprovider.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolResourceServer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolresourceserver.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolRiskConfigurationAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolriskconfigurationattachment.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolUICustomizationAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluicustomizationattachment.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolUser](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `me-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolUserToGroupAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolusertogroupattachment.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `me-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Config::AggregationAuthorization](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html)
  - `cn-northwest-1`
  - `ap-northeast-2`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::Config::OrganizationConfigRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `cn-north-1`
  - `us-gov-east-1`

- [AWS::Config::RemediationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html)
  - `af-south-1`
  - `me-south-1`
  - `cn-northwest-1`
  - `eu-south-1`
  - `cn-north-1`

- [AWS::DAX::Cluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html)
  - `ap-southeast-1`
  - `us-east-2`
  - `cn-northwest-1`
  - `eu-west-2`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::DAX::ParameterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-parametergroup.html)
  - `ap-southeast-1`
  - `us-east-2`
  - `cn-northwest-1`
  - `eu-west-2`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::DAX::SubnetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-subnetgroup.html)
  - `ap-southeast-1`
  - `us-east-2`
  - `cn-northwest-1`
  - `eu-west-2`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::DLM::LifecyclePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html)
  - Now available to **ALL** regions.

- [AWS::DMS::Certificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html)
  - Now available to **ALL** regions.

- [AWS::DMS::Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html)
  - Now available to **ALL** regions.

- [AWS::DMS::EventSubscription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html)
  - Now available to **ALL** regions.

- [AWS::DMS::ReplicationInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html)
  - Now available to **ALL** regions.

- [AWS::DMS::ReplicationSubnetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html)
  - Now available to **ALL** regions.

- [AWS::DMS::ReplicationTask](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html)
  - Now available to **ALL** regions.

- [AWS::DocDB::DBCluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html)
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-west-3`

- [AWS::DocDB::DBClusterParameterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html)
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-west-3`

- [AWS::DocDB::DBInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html)
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-west-3`

- [AWS::DocDB::DBSubnetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html)
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-west-3`

- [AWS::DynamoDB::GlobalTable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html)
  - `ap-northeast-3`

- [AWS::EC2::CapacityReservation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `sa-east-1`

- [AWS::EC2::ClientVpnAuthorizationRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::EC2::ClientVpnEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::EC2::ClientVpnRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::EC2::ClientVpnTargetNetworkAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpntargetnetworkassociation.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::EC2::LaunchTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html)
  - Now available to **ALL** regions.

- [AWS::EC2::TransitGateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html)
  - Now available to **ALL** regions.

- [AWS::EC2::TransitGatewayAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html)
  - Now available to **ALL** regions.

- [AWS::EC2::TransitGatewayRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html)
  - Now available to **ALL** regions.

- [AWS::EC2::TransitGatewayRouteTable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetable.html)
  - Now available to **ALL** regions.

- [AWS::EC2::TransitGatewayRouteTableAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetableassociation.html)
  - Now available to **ALL** regions.

- [AWS::EC2::TransitGatewayRouteTablePropagation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetablepropagation.html)
  - Now available to **ALL** regions.

- [AWS::EC2::VPCEndpointConnectionNotification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.html)
  - Now available to **ALL** regions.

- [AWS::EC2::VPCEndpointServicePermissions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservicepermissions.html)
  - Now available to **ALL** regions.

- [AWS::EventSchemas::Discoverer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html)
  - `ap-southeast-1`
  - `us-west-1`
  - `eu-north-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::EventSchemas::Registry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html)
  - `ap-southeast-1`
  - `us-west-1`
  - `eu-north-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::EventSchemas::Schema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html)
  - `ap-southeast-1`
  - `us-west-1`
  - `eu-north-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::Events::EventBus](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbus.html)
  - Now available to **ALL** regions.

- [AWS::Events::EventBusPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html)
  - Now available to **ALL** regions.

- [AWS::FSx::FileSystem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `me-south-1`
  - `eu-south-1`

- [AWS::Glue::Classifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-classifier.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Connection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-connection.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Crawler](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html)
  - Now available to **ALL** regions.

- [AWS::Glue::DataCatalogEncryptionSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-datacatalogencryptionsettings.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Database](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-database.html)
  - Now available to **ALL** regions.

- [AWS::Glue::DevEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Job](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html)
  - Now available to **ALL** regions.

- [AWS::Glue::MLTransform](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html)
  - `af-south-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `ap-east-1`
  - `us-gov-east-1`

- [AWS::Glue::Partition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-partition.html)
  - Now available to **ALL** regions.

- [AWS::Glue::SecurityConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-securityconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Table](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Trigger](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Workflow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-workflow.html)
  - Now available to **ALL** regions.

- [AWS::Greengrass::ConnectorDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ConnectorDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::CoreDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::CoreDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::DeviceDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::DeviceDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::FunctionDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::FunctionDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::Group](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::GroupVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::LoggerDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::LoggerDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::SubscriptionDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::SubscriptionDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::GuardDuty::Detector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html)
  - Now available to **ALL** regions.

- [AWS::GuardDuty::Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html)
  - Now available to **ALL** regions.

- [AWS::GuardDuty::IPSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html)
  - Now available to **ALL** regions.

- [AWS::GuardDuty::Master](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html)
  - Now available to **ALL** regions.

- [AWS::GuardDuty::Member](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html)
  - Now available to **ALL** regions.

- [AWS::GuardDuty::ThreatIntelSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html)
  - Now available to **ALL** regions.

- [AWS::IAM::ServiceLinkedRole](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html)
  - Now available to **ALL** regions.

- [AWS::Kinesis::StreamConsumer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-streamconsumer.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalytics::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::ApplicationOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::ApplicationReferenceDataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalyticsV2::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::ApplicationOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::LakeFormation::DataLakeSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::LakeFormation::Permissions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::LakeFormation::Resource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::Lambda::EventInvokeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html)
  - Now available to **ALL** regions.

- [AWS::Lambda::LayerVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html)
  - Now available to **ALL** regions.

- [AWS::Lambda::LayerVersionPermission](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html)
  - Now available to **ALL** regions.

- [AWS::MSK::Cluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html)
  - `eu-south-1`

- [AWS::MediaConvert::JobTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html)
  - `cn-northwest-1`

- [AWS::MediaConvert::Preset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html)
  - `cn-northwest-1`

- [AWS::MediaConvert::Queue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html)
  - `cn-northwest-1`

- [AWS::MediaLive::Channel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::InputSecurityGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaStore::Container](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html)
  - `eu-west-2`
  - `ap-south-1`
  - `sa-east-1`

- [AWS::Neptune::DBCluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `ap-east-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `us-gov-east-1`
  - `ap-northeast-2`

- [AWS::Neptune::DBClusterParameterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `ap-east-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `us-gov-east-1`
  - `ap-northeast-2`
  - `ap-southeast-2`

- [AWS::Neptune::DBInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `ap-east-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `us-gov-east-1`
  - `ap-northeast-2`
  - `ap-southeast-2`

- [AWS::Neptune::DBParameterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `ap-east-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `us-gov-east-1`
  - `ap-northeast-2`
  - `ap-southeast-2`

- [AWS::Neptune::DBSubnetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbsubnetgroup.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `ap-east-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `us-gov-east-1`
  - `ap-northeast-2`
  - `ap-southeast-2`

- [AWS::Pinpoint::ADMChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::APNSChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::APNSSandboxChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::APNSVoipChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::APNSVoipSandboxChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::App](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::ApplicationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::BaiduChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Campaign](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::EmailChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::EmailTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::Pinpoint::EventStream](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::GCMChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::PushTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::Pinpoint::SMSChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Segment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::SmsTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::Pinpoint::VoiceChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::RAM::ResourceShare](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html)
  - Now available to **ALL** regions.

- [AWS::RoboMaker::Fleet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-fleet.html)
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `ap-south-1`

- [AWS::RoboMaker::Robot](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robot.html)
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `ap-south-1`

- [AWS::RoboMaker::RobotApplication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html)
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `ap-south-1`

- [AWS::RoboMaker::RobotApplicationVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplicationversion.html)
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `ap-south-1`

- [AWS::RoboMaker::SimulationApplication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html)
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `ap-south-1`

- [AWS::RoboMaker::SimulationApplicationVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplicationversion.html)
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `ap-south-1`

- [AWS::Route53Resolver::ResolverEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html)
  - Now available to **ALL** regions.

- [AWS::Route53Resolver::ResolverRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html)
  - Now available to **ALL** regions.

- [AWS::Route53Resolver::ResolverRuleAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html)
  - Now available to **ALL** regions.

- [AWS::SSM::MaintenanceWindow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html)
  - Now available to **ALL** regions.

- [AWS::SSM::MaintenanceWindowTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html)
  - Now available to **ALL** regions.

- [AWS::SSM::MaintenanceWindowTask](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html)
  - Now available to **ALL** regions.

- [AWS::SSM::Parameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html)
  - Now available to **ALL** regions.

- [AWS::SSM::PatchBaseline](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html)
  - Now available to **ALL** regions.

- [AWS::SSO::Assignment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html)
  - `sa-east-1`

- [AWS::SSO::InstanceAccessControlAttributeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html)
  - `sa-east-1`

- [AWS::SSO::PermissionSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html)
  - `sa-east-1`

- [AWS::SageMaker::CodeRepository](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `eu-north-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::SageMaker::Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::SageMaker::EndpointConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::SageMaker::Model](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::SageMaker::NotebookInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html)
  - `eu-north-1`
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::SageMaker::NotebookInstanceLifecycleConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::SageMaker::Workteam](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::SecretsManager::ResourcePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-resourcepolicy.html)
  - Now available to **ALL** regions.

- [AWS::SecretsManager::RotationSchedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-rotationschedule.html)
  - Now available to **ALL** regions.

- [AWS::SecretsManager::Secret](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secret.html)
  - Now available to **ALL** regions.

- [AWS::SecretsManager::SecretTargetAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secrettargetattachment.html)
  - Now available to **ALL** regions.

- [AWS::SecurityHub::Hub](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html)
  - Now available to **ALL** regions.

- [AWS::ServiceCatalog::AcceptedPortfolioShare](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html)
  - Now available to **ALL** regions.

- [AWS::ServiceCatalog::CloudFormationProduct](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html)
  - Now available to **ALL** regions.

- [AWS::ServiceCatalog::LaunchNotificationConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html)
  - Now available to **ALL** regions.

- [AWS::ServiceCatalog::LaunchRoleConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html)
  - Now available to **ALL** regions.

- [AWS::ServiceCatalog::LaunchTemplateConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html)
  - Now available to **ALL** regions.

- [AWS::ServiceCatalog::Portfolio](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html)
  - Now available to **ALL** regions.

- [AWS::ServiceCatalog::PortfolioPrincipalAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html)
  - Now available to **ALL** regions.

- [AWS::ServiceCatalog::PortfolioProductAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html)
  - Now available to **ALL** regions.

- [AWS::ServiceCatalog::PortfolioShare](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html)
  - Now available to **ALL** regions.

- [AWS::ServiceCatalog::ResourceUpdateConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html)
  - Now available to **ALL** regions.

- [AWS::ServiceCatalog::StackSetConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html)
  - Now available to **ALL** regions.

- [AWS::ServiceCatalog::TagOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html)
  - Now available to **ALL** regions.

- [AWS::ServiceCatalog::TagOptionAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html)
  - Now available to **ALL** regions.

- [AWS::ServiceDiscovery::HttpNamespace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html)
  - `ap-northeast-1`
  - `eu-west-3`
  - `sa-east-1`

- [AWS::ServiceDiscovery::Instance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html)
  - `sa-east-1`

- [AWS::ServiceDiscovery::PrivateDnsNamespace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html)
  - `sa-east-1`

- [AWS::ServiceDiscovery::PublicDnsNamespace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html)
  - `sa-east-1`

- [AWS::ServiceDiscovery::Service](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html)
  - `sa-east-1`

- [AWS::StepFunctions::Activity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html)
  - Now available to **ALL** regions.

- [AWS::Transfer::User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::WAFRegional::ByteMatchSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::GeoMatchSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-geomatchset.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::IPSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::RateBasedRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::RegexPatternSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-regexpatternset.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::SizeConstraintSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::SqlInjectionMatchSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::WebACL](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::WebACLAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::XssMatchSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [Alexa::ASK::Skill](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html)
  - `ap-northeast-1`

- [AWS::AmazonMQ::Broker.ConfigurationId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-configurationid.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-west-2`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`

- [AWS::AmazonMQ::Broker.EncryptionOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-encryptionoptions.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-west-2`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`

- [AWS::AmazonMQ::Broker.LdapServerMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-west-2`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`

- [AWS::AmazonMQ::Broker.LogList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-loglist.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-west-2`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`

- [AWS::AmazonMQ::Broker.MaintenanceWindow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-west-2`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`

- [AWS::AmazonMQ::Broker.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-tagsentry.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-west-2`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`

- [AWS::AmazonMQ::Broker.User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-user.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-west-2`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`

- [AWS::AmazonMQ::Configuration.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configuration-tagsentry.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-west-2`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`

- [AWS::AmazonMQ::ConfigurationAssociation.ConfigurationId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configurationassociation-configurationid.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-west-2`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`

- [AWS::Amplify::Domain.SubDomainSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-domain-subdomainsetting.html)
  - `eu-north-1`
  - `us-west-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::ApiGatewayV2::ApiGatewayManagedOverrides.AccessLogSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::ApiGatewayManagedOverrides.IntegrationOverrides](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::ApiGatewayManagedOverrides.RouteOverrides](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::ApiGatewayManagedOverrides.RouteSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::ApiGatewayManagedOverrides.StageOverrides](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html)
  - Now available to **ALL** regions.

- [AWS::AppConfig::Application.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-application-tags.html)
  - Now available to **ALL** regions.

- [AWS::AppConfig::ConfigurationProfile.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-tags.html)
  - Now available to **ALL** regions.

- [AWS::AppConfig::ConfigurationProfile.Validators](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-validators.html)
  - Now available to **ALL** regions.

- [AWS::AppConfig::Deployment.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deployment-tags.html)
  - Now available to **ALL** regions.

- [AWS::AppConfig::DeploymentStrategy.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deploymentstrategy-tags.html)
  - Now available to **ALL** regions.

- [AWS::AppConfig::Environment.Monitors](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitors.html)
  - Now available to **ALL** regions.

- [AWS::AppConfig::Environment.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-tags.html)
  - Now available to **ALL** regions.

- [AWS::AppMesh::GatewayRoute.GatewayRouteHostnameMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.GatewayRouteHostnameRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamerewrite.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.GatewayRouteMetadataMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.GatewayRouteRangeMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayrouterangematch.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.GatewayRouteSpec](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.GatewayRouteTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutetarget.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.GatewayRouteVirtualService](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutevirtualservice.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.GrpcGatewayRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroute.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.GrpcGatewayRouteAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouteaction.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.GrpcGatewayRouteMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.GrpcGatewayRouteMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.GrpcGatewayRouteRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouterewrite.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroute.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRouteAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteaction.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRouteHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRouteHeaderMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRouteMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRoutePathRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutepathrewrite.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRoutePrefixRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRouteRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.HttpPathMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httppathmatch.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.HttpQueryParameterMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpqueryparametermatch.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::GatewayRoute.QueryParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-queryparameter.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::Mesh.EgressFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-egressfilter.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Mesh.MeshSpec](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshspec.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.Duration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-duration.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.GrpcRetryPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.GrpcRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.GrpcRouteAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcrouteaction.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.GrpcRouteMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.GrpcRouteMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadata.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.GrpcRouteMetadataMatchMethod](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.GrpcTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpctimeout.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.HeaderMatchMethod](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.HttpPathMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httppathmatch.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.HttpQueryParameterMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpqueryparametermatch.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.HttpRetryPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.HttpRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.HttpRouteAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteaction.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.HttpRouteHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteheader.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.HttpRouteMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.HttpTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httptimeout.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.MatchRange](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-matchrange.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.QueryParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-queryparameter.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.RouteSpec](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.TcpRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.TcpRouteAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcprouteaction.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.TcpTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcptimeout.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::Route.WeightedTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-weightedtarget.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualGateway.SubjectAlternativeNameMatchers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenamematchers.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.SubjectAlternativeNames](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenames.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayAccessLog](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayaccesslog.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayBackendDefaults](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaybackenddefaults.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayClientPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicy.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayClientPolicyTls](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayClientTlsCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayConnectionPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayFileAccessLog](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayfileaccesslog.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayGrpcConnectionPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaygrpcconnectionpool.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayHealthCheckPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayHttp2ConnectionPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttp2connectionpool.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayHttpConnectionPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttpconnectionpool.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayListener](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTls](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsAcmCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsacmcertificate.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsFileCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsSdsCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlssdscertificate.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsValidationContext](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsValidationContextTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayLogging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylogging.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayPortMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayportmapping.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewaySpec](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContext](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContextAcmTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContextFileTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextfiletrust.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContextSdsTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContextTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AppMesh::VirtualNode.AccessLog](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-accesslog.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.AwsCloudMapInstanceAttribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.AwsCloudMapServiceDiscovery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.Backend](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backend.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.BackendDefaults](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backenddefaults.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.ClientPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicy.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.ClientPolicyTls](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.ClientTlsCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clienttlscertificate.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.DnsServiceDiscovery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-dnsservicediscovery.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.Duration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-duration.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.FileAccessLog](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-fileaccesslog.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.GrpcTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-grpctimeout.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.HealthCheck](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.HttpTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-httptimeout.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.Listener](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.ListenerTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.ListenerTls](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.ListenerTlsAcmCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsacmcertificate.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.ListenerTlsCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.ListenerTlsFileCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsfilecertificate.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.ListenerTlsSdsCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlssdscertificate.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.ListenerTlsValidationContext](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontext.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.ListenerTlsValidationContextTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-logging.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.OutlierDetection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.PortMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-portmapping.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.ServiceDiscovery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-servicediscovery.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.SubjectAlternativeNameMatchers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenamematchers.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.SubjectAlternativeNames](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenames.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.TcpTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tcptimeout.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.TlsValidationContext](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontext.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.TlsValidationContextAcmTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextacmtrust.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.TlsValidationContextFileTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextfiletrust.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.TlsValidationContextSdsTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextsdstrust.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.TlsValidationContextTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.VirtualNodeConnectionPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.VirtualNodeGrpcConnectionPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodegrpcconnectionpool.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.VirtualNodeHttp2ConnectionPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttp2connectionpool.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.VirtualNodeHttpConnectionPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttpconnectionpool.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.VirtualNodeSpec](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.VirtualNodeTcpConnectionPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodetcpconnectionpool.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualNode.VirtualServiceBackend](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualservicebackend.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualRouter.PortMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-portmapping.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualRouter.VirtualRouterListener](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterlistener.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualRouter.VirtualRouterSpec](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterspec.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualService.VirtualNodeServiceProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualnodeserviceprovider.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualService.VirtualRouterServiceProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualrouterserviceprovider.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualService.VirtualServiceProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualserviceprovider.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppMesh::VirtualService.VirtualServiceSpec](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualservicespec.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppStream::DirectoryConfig.ServiceAccountCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-directoryconfig-serviceaccountcredentials.html)
  - `us-west-1`
  - `cn-northwest-1`
  - `us-east-2`
  - `eu-west-2`

- [AWS::AppStream::Fleet.ComputeCapacity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-computecapacity.html)
  - `us-west-1`
  - `cn-northwest-1`
  - `us-east-2`
  - `eu-west-2`

- [AWS::AppStream::Fleet.DomainJoinInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-domainjoininfo.html)
  - `us-west-1`
  - `cn-northwest-1`
  - `us-east-2`
  - `eu-west-2`

- [AWS::AppStream::Fleet.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-vpcconfig.html)
  - `us-west-1`
  - `cn-northwest-1`
  - `us-east-2`
  - `eu-west-2`

- [AWS::AppStream::ImageBuilder.AccessEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-accessendpoint.html)
  - `us-west-1`
  - `cn-northwest-1`
  - `us-east-2`
  - `eu-west-2`

- [AWS::AppStream::ImageBuilder.DomainJoinInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-domainjoininfo.html)
  - `us-west-1`
  - `cn-northwest-1`
  - `us-east-2`
  - `eu-west-2`

- [AWS::AppStream::ImageBuilder.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-vpcconfig.html)
  - `us-west-1`
  - `cn-northwest-1`
  - `us-east-2`
  - `eu-west-2`

- [AWS::AppStream::Stack.AccessEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-accessendpoint.html)
  - `us-west-1`
  - `cn-northwest-1`
  - `us-east-2`
  - `eu-west-2`

- [AWS::AppStream::Stack.ApplicationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-applicationsettings.html)
  - `us-west-1`
  - `cn-northwest-1`
  - `us-east-2`
  - `eu-west-2`

- [AWS::AppStream::Stack.StorageConnector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-storageconnector.html)
  - `us-west-1`
  - `cn-northwest-1`
  - `us-east-2`
  - `eu-west-2`

- [AWS::AppStream::Stack.UserSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-usersetting.html)
  - `us-west-1`
  - `cn-northwest-1`
  - `us-east-2`
  - `eu-west-2`

- [AWS::AppSync::DataSource.AuthorizationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::DataSource.AwsIamConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::DataSource.DeltaSyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::DataSource.DynamoDBConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::DataSource.ElasticsearchConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::DataSource.HttpConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::DataSource.LambdaConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-lambdaconfig.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::DataSource.RdsHttpEndpointConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::DataSource.RelationalDatabaseConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::FunctionConfiguration.LambdaConflictHandlerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::FunctionConfiguration.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::GraphQLApi.AdditionalAuthenticationProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::GraphQLApi.AdditionalAuthenticationProviders](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationproviders.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::GraphQLApi.CognitoUserPoolConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::GraphQLApi.LogConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::GraphQLApi.OpenIDConnectConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::GraphQLApi.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-tags.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::GraphQLApi.UserPoolConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::Resolver.CachingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::Resolver.LambdaConflictHandlerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-lambdaconflicthandlerconfig.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::Resolver.PipelineConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-pipelineconfig.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AppSync::Resolver.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html)
  - `eu-north-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::AutoScalingPlans::ScalingPlan.ApplicationSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-applicationsource.html)
  - `ap-northeast-3`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AutoScalingPlans::ScalingPlan.CustomizedLoadMetricSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html)
  - `ap-northeast-3`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AutoScalingPlans::ScalingPlan.CustomizedScalingMetricSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html)
  - `ap-northeast-3`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AutoScalingPlans::ScalingPlan.MetricDimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-metricdimension.html)
  - `ap-northeast-3`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AutoScalingPlans::ScalingPlan.PredefinedLoadMetricSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedloadmetricspecification.html)
  - `ap-northeast-3`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AutoScalingPlans::ScalingPlan.PredefinedScalingMetricSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedscalingmetricspecification.html)
  - `ap-northeast-3`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AutoScalingPlans::ScalingPlan.ScalingInstruction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html)
  - `ap-northeast-3`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AutoScalingPlans::ScalingPlan.TagFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-tagfilter.html)
  - `ap-northeast-3`
  - `af-south-1`
  - `eu-south-1`

- [AWS::AutoScalingPlans::ScalingPlan.TargetTrackingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html)
  - `ap-northeast-3`
  - `af-south-1`
  - `eu-south-1`

- [AWS::Batch::ComputeEnvironment.ComputeResources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html)
  - Now available to **ALL** regions.

- [AWS::Batch::ComputeEnvironment.Ec2ConfigurationObject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-ec2configurationobject.html)
  - Now available to **ALL** regions.

- [AWS::Batch::ComputeEnvironment.LaunchTemplateSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.AuthorizationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-authorizationconfig.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.ContainerProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.Device](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-device.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.EfsVolumeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-environment.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.EvaluateOnExit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-evaluateonexit.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.FargatePlatformConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-fargateplatformconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.LinuxParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-linuxparameters.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.LogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.MountPoints](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-mountpoints.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.NetworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-networkconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.NodeProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-nodeproperties.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.NodeRangeProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-noderangeproperty.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.ResourceRequirement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-resourcerequirement.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.RetryStrategy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-retrystrategy.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.Secret](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-secret.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.Timeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-timeout.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.Tmpfs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-tmpfs.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.Ulimit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ulimit.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.Volumes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumes.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobDefinition.VolumesHost](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumeshost.html)
  - Now available to **ALL** regions.

- [AWS::Batch::JobQueue.ComputeEnvironmentOrder](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobqueue-computeenvironmentorder.html)
  - Now available to **ALL** regions.

- [AWS::Budgets::Budget.BudgetData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html)
  - `eu-west-3`

- [AWS::Budgets::Budget.CostTypes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html)
  - `eu-west-3`

- [AWS::Budgets::Budget.Notification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html)
  - `eu-west-3`

- [AWS::Budgets::Budget.NotificationWithSubscribers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html)
  - `eu-west-3`

- [AWS::Budgets::Budget.Spend](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html)
  - `eu-west-3`

- [AWS::Budgets::Budget.Subscriber](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html)
  - `eu-west-3`

- [AWS::Budgets::Budget.TimePeriod](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html)
  - `eu-west-3`

- [AWS::CloudFront::StreamingDistribution.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-logging.html)
  - `eu-north-1`
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `cn-north-1`

- [AWS::CloudFront::StreamingDistribution.S3Origin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-s3origin.html)
  - `eu-north-1`
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `cn-north-1`

- [AWS::CloudFront::StreamingDistribution.StreamingDistributionConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html)
  - `eu-north-1`
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `cn-north-1`

- [AWS::CloudFront::StreamingDistribution.TrustedSigners](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-trustedsigners.html)
  - `eu-north-1`
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `cn-north-1`

- [AWS::CloudWatch::AnomalyDetector.Configuration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-configuration.html)
  - Now available to **ALL** regions.

- [AWS::CloudWatch::AnomalyDetector.Dimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-dimension.html)
  - Now available to **ALL** regions.

- [AWS::CloudWatch::AnomalyDetector.Range](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-range.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.Artifacts](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.BatchRestrictions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-batchrestrictions.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.BuildStatusConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-buildstatusconfig.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.CloudWatchLogsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-cloudwatchlogsconfig.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.EnvironmentVariable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environmentvariable.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.FilterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-filtergroup.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.GitSubmodulesConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-gitsubmodulesconfig.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.LogsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-logsconfig.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.ProjectBuildBatchConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.ProjectCache](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectcache.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.ProjectFileSystemLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.ProjectSourceVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectsourceversion.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.ProjectTriggers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projecttriggers.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.RegistryCredential](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-registrycredential.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.S3LogsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-s3logsconfig.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.Source](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.SourceAuth](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-sourceauth.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-vpcconfig.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.WebhookFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-webhookfilter.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::ReportGroup.ReportExportConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-reportexportconfig.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::ReportGroup.S3ReportExportConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html)
  - Now available to **ALL** regions.

- [AWS::CodeCommit::Repository.Code](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-code.html)
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-west-3`
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-gov-east-1`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::CodeCommit::Repository.RepositoryTrigger](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html)
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-west-3`
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-gov-east-1`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::CodeCommit::Repository.S3](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-s3.html)
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-west-3`
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-gov-east-1`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::CodePipeline::Webhook.WebhookAuthConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-webhook-webhookauthconfiguration.html)
  - `us-gov-west-1`
  - `eu-south-1`
  - `eu-north-1`
  - `ap-east-1`

- [AWS::CodePipeline::Webhook.WebhookFilterRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-webhook-webhookfilterrule.html)
  - `us-gov-west-1`
  - `eu-south-1`
  - `eu-north-1`
  - `ap-east-1`

- [AWS::Cognito::IdentityPool.CognitoIdentityProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitoidentityprovider.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `me-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::IdentityPool.CognitoStreams](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitostreams.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `me-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::IdentityPool.PushSync](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-pushsync.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `me-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::IdentityPoolRoleAttachment.MappingRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-mappingrule.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::IdentityPoolRoleAttachment.RoleMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rolemapping.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::IdentityPoolRoleAttachment.RulesConfigurationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rulesconfigurationtype.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPool.AccountRecoverySetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-accountrecoverysetting.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPool.AdminCreateUserConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-admincreateuserconfig.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPool.CustomEmailSender](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-customemailsender.html)
  - `eu-north-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `me-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPool.CustomSMSSender](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-customsmssender.html)
  - `eu-north-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `me-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPool.DeviceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-deviceconfiguration.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPool.EmailConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-emailconfiguration.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPool.InviteMessageTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-invitemessagetemplate.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPool.LambdaConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPool.NumberAttributeConstraints](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-numberattributeconstraints.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPool.PasswordPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-passwordpolicy.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPool.Policies](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-policies.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPool.RecoveryOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-recoveryoption.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPool.SchemaAttribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPool.SmsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-smsconfiguration.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPool.StringAttributeConstraints](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-stringattributeconstraints.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPool.UserPoolAddOns](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-userpooladdons.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPool.UsernameConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-usernameconfiguration.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPool.VerificationMessageTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-verificationmessagetemplate.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolClient.AnalyticsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-analyticsconfiguration.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolClient.TokenValidityUnits](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-tokenvalidityunits.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolDomain.CustomDomainConfigType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpooldomain-customdomainconfigtype.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolResourceServer.ResourceServerScopeType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolresourceserver-resourceserverscopetype.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolRiskConfigurationAttachment.AccountTakeoverActionType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolRiskConfigurationAttachment.AccountTakeoverActionsType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolRiskConfigurationAttachment.AccountTakeoverRiskConfigurationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolRiskConfigurationAttachment.CompromisedCredentialsActionsType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsactionstype.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolRiskConfigurationAttachment.CompromisedCredentialsRiskConfigurationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolRiskConfigurationAttachment.NotifyConfigurationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolRiskConfigurationAttachment.NotifyEmailType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-notifyemailtype.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolRiskConfigurationAttachment.RiskExceptionConfigurationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype.html)
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-north-1`
  - `me-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Cognito::UserPoolUser.AttributeType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpooluser-attributetype.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `me-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Config::OrganizationConfigRule.OrganizationCustomRuleMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `cn-north-1`
  - `us-gov-east-1`

- [AWS::Config::OrganizationConfigRule.OrganizationManagedRuleMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `cn-north-1`
  - `us-gov-east-1`

- [AWS::Config::RemediationConfiguration.ExecutionControls](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-executioncontrols.html)
  - `af-south-1`
  - `me-south-1`
  - `cn-northwest-1`
  - `eu-south-1`
  - `cn-north-1`

- [AWS::Config::RemediationConfiguration.RemediationParameterValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-remediationparametervalue.html)
  - `af-south-1`
  - `me-south-1`
  - `cn-northwest-1`
  - `eu-south-1`
  - `cn-north-1`

- [AWS::Config::RemediationConfiguration.ResourceValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-resourcevalue.html)
  - `af-south-1`
  - `me-south-1`
  - `cn-northwest-1`
  - `eu-south-1`
  - `cn-north-1`

- [AWS::Config::RemediationConfiguration.SsmControls](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-ssmcontrols.html)
  - `af-south-1`
  - `me-south-1`
  - `cn-northwest-1`
  - `eu-south-1`
  - `cn-north-1`

- [AWS::Config::RemediationConfiguration.StaticValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-staticvalue.html)
  - `af-south-1`
  - `me-south-1`
  - `cn-northwest-1`
  - `eu-south-1`
  - `cn-north-1`

- [AWS::DAX::Cluster.SSESpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dax-cluster-ssespecification.html)
  - `ap-southeast-1`
  - `us-east-2`
  - `cn-northwest-1`
  - `eu-west-2`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::DLM::LifecyclePolicy.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-action.html)
  - Now available to **ALL** regions.

- [AWS::DLM::LifecyclePolicy.CreateRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html)
  - Now available to **ALL** regions.

- [AWS::DLM::LifecyclePolicy.CrossRegionCopyAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html)
  - Now available to **ALL** regions.

- [AWS::DLM::LifecyclePolicy.CrossRegionCopyRetainRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.html)
  - Now available to **ALL** regions.

- [AWS::DLM::LifecyclePolicy.CrossRegionCopyRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html)
  - Now available to **ALL** regions.

- [AWS::DLM::LifecyclePolicy.EncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-encryptionconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::DLM::LifecyclePolicy.EventParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html)
  - Now available to **ALL** regions.

- [AWS::DLM::LifecyclePolicy.EventSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventsource.html)
  - Now available to **ALL** regions.

- [AWS::DLM::LifecyclePolicy.FastRestoreRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html)
  - Now available to **ALL** regions.

- [AWS::DLM::LifecyclePolicy.Parameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-parameters.html)
  - Now available to **ALL** regions.

- [AWS::DLM::LifecyclePolicy.PolicyDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html)
  - Now available to **ALL** regions.

- [AWS::DLM::LifecyclePolicy.RetainRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html)
  - Now available to **ALL** regions.

- [AWS::DLM::LifecyclePolicy.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html)
  - Now available to **ALL** regions.

- [AWS::DLM::LifecyclePolicy.ShareRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html)
  - Now available to **ALL** regions.

- [AWS::DMS::Endpoint.DocDbSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html)
  - Now available to **ALL** regions.

- [AWS::DMS::Endpoint.DynamoDbSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-dynamodbsettings.html)
  - Now available to **ALL** regions.

- [AWS::DMS::Endpoint.ElasticsearchSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-elasticsearchsettings.html)
  - Now available to **ALL** regions.

- [AWS::DMS::Endpoint.IbmDb2Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html)
  - Now available to **ALL** regions.

- [AWS::DMS::Endpoint.KafkaSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html)
  - Now available to **ALL** regions.

- [AWS::DMS::Endpoint.KinesisSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html)
  - Now available to **ALL** regions.

- [AWS::DMS::Endpoint.MicrosoftSqlServerSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html)
  - Now available to **ALL** regions.

- [AWS::DMS::Endpoint.MongoDbSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html)
  - Now available to **ALL** regions.

- [AWS::DMS::Endpoint.MySqlSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html)
  - Now available to **ALL** regions.

- [AWS::DMS::Endpoint.NeptuneSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html)
  - Now available to **ALL** regions.

- [AWS::DMS::Endpoint.OracleSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html)
  - Now available to **ALL** regions.

- [AWS::DMS::Endpoint.PostgreSqlSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html)
  - Now available to **ALL** regions.

- [AWS::DMS::Endpoint.RedshiftSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html)
  - Now available to **ALL** regions.

- [AWS::DMS::Endpoint.S3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html)
  - Now available to **ALL** regions.

- [AWS::DMS::Endpoint.SybaseSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-sybasesettings.html)
  - Now available to **ALL** regions.

- [AWS::DataBrew::Job.DataCatalogOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html)
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `us-east-1`

- [AWS::DataBrew::Job.DatabaseTableOutputOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databasetableoutputoptions.html)
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `us-east-1`

- [AWS::DataBrew::Job.S3TableOutputOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3tableoutputoptions.html)
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `us-east-1`

- [AWS::DynamoDB::GlobalTable.AttributeDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-attributedefinition.html)
  - `ap-northeast-3`

- [AWS::DynamoDB::GlobalTable.CapacityAutoScalingSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html)
  - `ap-northeast-3`

- [AWS::DynamoDB::GlobalTable.ContributorInsightsSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-contributorinsightsspecification.html)
  - `ap-northeast-3`

- [AWS::DynamoDB::GlobalTable.GlobalSecondaryIndex](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html)
  - `ap-northeast-3`

- [AWS::DynamoDB::GlobalTable.KeySchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-keyschema.html)
  - `ap-northeast-3`

- [AWS::DynamoDB::GlobalTable.LocalSecondaryIndex](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-localsecondaryindex.html)
  - `ap-northeast-3`

- [AWS::DynamoDB::GlobalTable.PointInTimeRecoverySpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-pointintimerecoveryspecification.html)
  - `ap-northeast-3`

- [AWS::DynamoDB::GlobalTable.Projection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-projection.html)
  - `ap-northeast-3`

- [AWS::DynamoDB::GlobalTable.ReadProvisionedThroughputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings.html)
  - `ap-northeast-3`

- [AWS::DynamoDB::GlobalTable.ReplicaGlobalSecondaryIndexSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html)
  - `ap-northeast-3`

- [AWS::DynamoDB::GlobalTable.ReplicaSSESpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicassespecification.html)
  - `ap-northeast-3`

- [AWS::DynamoDB::GlobalTable.ReplicaSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html)
  - `ap-northeast-3`

- [AWS::DynamoDB::GlobalTable.SSESpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-ssespecification.html)
  - `ap-northeast-3`

- [AWS::DynamoDB::GlobalTable.StreamSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-streamspecification.html)
  - `ap-northeast-3`

- [AWS::DynamoDB::GlobalTable.TargetTrackingScalingPolicyConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html)
  - `ap-northeast-3`

- [AWS::DynamoDB::GlobalTable.TimeToLiveSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-timetolivespecification.html)
  - `ap-northeast-3`

- [AWS::DynamoDB::GlobalTable.WriteProvisionedThroughputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-writeprovisionedthroughputsettings.html)
  - `ap-northeast-3`

- [AWS::EC2::CapacityReservation.TagSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservation-tagspecification.html)
  - `eu-north-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `sa-east-1`

- [AWS::EC2::ClientVpnEndpoint.CertificateAuthenticationRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-certificateauthenticationrequest.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::EC2::ClientVpnEndpoint.ClientAuthenticationRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientauthenticationrequest.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::EC2::ClientVpnEndpoint.ClientConnectOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientconnectoptions.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::EC2::ClientVpnEndpoint.ConnectionLogOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-connectionlogoptions.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::EC2::ClientVpnEndpoint.DirectoryServiceAuthenticationRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-directoryserviceauthenticationrequest.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::EC2::ClientVpnEndpoint.FederatedAuthenticationRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-federatedauthenticationrequest.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::EC2::ClientVpnEndpoint.TagSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-tagspecification.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::EC2::LaunchTemplate.BlockDeviceMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.CapacityReservationSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-capacityreservationspecification.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.CapacityReservationTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-capacityreservationtarget.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.CpuOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-cpuoptions.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.CreditSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-creditspecification.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.Ebs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping-ebs.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.ElasticGpuSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-elasticgpuspecification.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.EnclaveOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-enclaveoptions.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.HibernationOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-hibernationoptions.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.IamInstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-iaminstanceprofile.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.InstanceMarketOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-instancemarketoptions.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.Ipv6Add](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-ipv6add.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.LaunchTemplateData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.LaunchTemplateElasticInferenceAccelerator](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplateelasticinferenceaccelerator.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.LaunchTemplateTagSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatetagspecification.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.LicenseSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-licensespecification.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.MetadataOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-metadataoptions.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.Monitoring](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-monitoring.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.NetworkInterface](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.Placement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-placement.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.PrivateIpAdd](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-privateipadd.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.SpotOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-instancemarketoptions-spotoptions.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.TagSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-tagspecification.html)
  - Now available to **ALL** regions.

- [AWS::EventSchemas::Discoverer.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html)
  - `ap-southeast-1`
  - `us-west-1`
  - `eu-north-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::EventSchemas::Registry.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html)
  - `ap-southeast-1`
  - `us-west-1`
  - `eu-north-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::EventSchemas::Schema.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html)
  - `ap-southeast-1`
  - `us-west-1`
  - `eu-north-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::Events::EventBusPolicy.Condition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html)
  - Now available to **ALL** regions.

- [AWS::FSx::FileSystem.LustreConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `me-south-1`
  - `eu-south-1`

- [AWS::FSx::FileSystem.SelfManagedActiveDirectoryConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `me-south-1`
  - `eu-south-1`

- [AWS::FSx::FileSystem.WindowsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `me-south-1`
  - `eu-south-1`

- [AWS::Glue::Classifier.CsvClassifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Classifier.GrokClassifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-grokclassifier.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Classifier.JsonClassifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-jsonclassifier.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Classifier.XMLClassifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-xmlclassifier.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Connection.ConnectionInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-connectioninput.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Connection.PhysicalConnectionRequirements](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-physicalconnectionrequirements.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Crawler.CatalogTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-catalogtarget.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Crawler.DynamoDBTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-dynamodbtarget.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Crawler.JdbcTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-jdbctarget.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Crawler.S3Target](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-s3target.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Crawler.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-schedule.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Crawler.SchemaChangePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-schemachangepolicy.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Crawler.Targets](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-targets.html)
  - Now available to **ALL** regions.

- [AWS::Glue::DataCatalogEncryptionSettings.ConnectionPasswordEncryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-connectionpasswordencryption.html)
  - Now available to **ALL** regions.

- [AWS::Glue::DataCatalogEncryptionSettings.DataCatalogEncryptionSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-datacatalogencryptionsettings.html)
  - Now available to **ALL** regions.

- [AWS::Glue::DataCatalogEncryptionSettings.EncryptionAtRest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-encryptionatrest.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Database.DatabaseIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseidentifier.html)
  - `us-gov-west-1`
  - `me-south-1`
  - `us-gov-east-1`
  - `ap-northeast-3`

- [AWS::Glue::Database.DatabaseInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Job.ConnectionsList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-connectionslist.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Job.ExecutionProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-executionproperty.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Job.JobCommand](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-jobcommand.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Job.NotificationProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-notificationproperty.html)
  - Now available to **ALL** regions.

- [AWS::Glue::MLTransform.FindMatchesParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters-findmatchesparameters.html)
  - `af-south-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `ap-east-1`
  - `us-gov-east-1`

- [AWS::Glue::MLTransform.GlueTables](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables-gluetables.html)
  - `af-south-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `ap-east-1`
  - `us-gov-east-1`

- [AWS::Glue::MLTransform.InputRecordTables](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables.html)
  - `af-south-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `ap-east-1`
  - `us-gov-east-1`

- [AWS::Glue::MLTransform.MLUserDataEncryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformencryption-mluserdataencryption.html)
  - `ap-northeast-3`
  - `us-gov-east-1`

- [AWS::Glue::MLTransform.TransformEncryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformencryption.html)
  - `ap-northeast-3`
  - `us-gov-east-1`

- [AWS::Glue::MLTransform.TransformParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters.html)
  - `af-south-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `ap-east-1`
  - `us-gov-east-1`

- [AWS::Glue::Partition.Column](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-column.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Partition.Order](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-order.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Partition.PartitionInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-partitioninput.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Partition.SchemaId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemaid.html)
  - `us-gov-west-1`
  - `us-gov-east-1`
  - `ap-northeast-3`

- [AWS::Glue::Partition.SchemaReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-schemareference.html)
  - `us-gov-west-1`
  - `us-gov-east-1`
  - `ap-northeast-3`

- [AWS::Glue::Partition.SerdeInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-serdeinfo.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Partition.SkewedInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-skewedinfo.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Partition.StorageDescriptor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html)
  - Now available to **ALL** regions.

- [AWS::Glue::SecurityConfiguration.CloudWatchEncryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-cloudwatchencryption.html)
  - Now available to **ALL** regions.

- [AWS::Glue::SecurityConfiguration.EncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-encryptionconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::Glue::SecurityConfiguration.JobBookmarksEncryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-jobbookmarksencryption.html)
  - Now available to **ALL** regions.

- [AWS::Glue::SecurityConfiguration.S3Encryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-s3encryption.html)
  - Now available to **ALL** regions.

- [AWS::Glue::SecurityConfiguration.S3Encryptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-s3encryptions.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Table.Column](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-column.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Table.Order](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-order.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Table.SchemaId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemaid.html)
  - `us-gov-west-1`
  - `us-gov-east-1`
  - `ap-northeast-3`

- [AWS::Glue::Table.SchemaReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-schemareference.html)
  - `us-gov-west-1`
  - `us-gov-east-1`
  - `ap-northeast-3`

- [AWS::Glue::Table.SerdeInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-serdeinfo.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Table.SkewedInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-skewedinfo.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Table.StorageDescriptor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Table.TableIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableidentifier.html)
  - `us-gov-west-1`
  - `me-south-1`
  - `us-gov-east-1`
  - `ap-northeast-3`

- [AWS::Glue::Table.TableInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Trigger.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-action.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Trigger.Condition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-condition.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Trigger.NotificationProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-notificationproperty.html)
  - Now available to **ALL** regions.

- [AWS::Glue::Trigger.Predicate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-predicate.html)
  - Now available to **ALL** regions.

- [AWS::Greengrass::ConnectorDefinition.Connector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ConnectorDefinition.ConnectorDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connectordefinitionversion.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ConnectorDefinitionVersion.Connector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinitionversion-connector.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::CoreDefinition.Core](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::CoreDefinition.CoreDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-coredefinitionversion.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::CoreDefinitionVersion.Core](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::DeviceDefinition.Device](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::DeviceDefinition.DeviceDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-devicedefinitionversion.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::DeviceDefinitionVersion.Device](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::FunctionDefinition.DefaultConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-defaultconfig.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::FunctionDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::FunctionDefinition.Execution](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-execution.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::FunctionDefinition.Function](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::FunctionDefinition.FunctionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::FunctionDefinition.FunctionDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functiondefinitionversion.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::FunctionDefinition.ResourceAccessPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-resourceaccesspolicy.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::FunctionDefinition.RunAs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-runas.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::FunctionDefinitionVersion.DefaultConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::FunctionDefinitionVersion.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::FunctionDefinitionVersion.Execution](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-execution.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::FunctionDefinitionVersion.Function](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-function.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::FunctionDefinitionVersion.FunctionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::FunctionDefinitionVersion.ResourceAccessPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-resourceaccesspolicy.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::FunctionDefinitionVersion.RunAs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-runas.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::Group.GroupVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::LoggerDefinition.Logger](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::LoggerDefinition.LoggerDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-loggerdefinitionversion.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::LoggerDefinitionVersion.Logger](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinition.GroupOwnerSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-groupownersetting.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinition.LocalDeviceResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localdeviceresourcedata.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinition.LocalVolumeResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinition.ResourceDataContainer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinition.ResourceDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedefinitionversion.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinition.ResourceDownloadOwnerSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinition.ResourceInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinition.S3MachineLearningModelResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinition.SageMakerMachineLearningModelResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinition.SecretsManagerSecretResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-secretsmanagersecretresourcedata.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinitionVersion.GroupOwnerSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-groupownersetting.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinitionVersion.LocalDeviceResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinitionVersion.LocalVolumeResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinitionVersion.ResourceDataContainer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinitionVersion.ResourceDownloadOwnerSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedownloadownersetting.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinitionVersion.ResourceInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinitionVersion.S3MachineLearningModelResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinitionVersion.SageMakerMachineLearningModelResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::ResourceDefinitionVersion.SecretsManagerSecretResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::SubscriptionDefinition.Subscription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::SubscriptionDefinition.SubscriptionDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscriptiondefinitionversion.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::Greengrass::SubscriptionDefinitionVersion.Subscription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html)
  - `us-west-1`
  - `us-gov-east-1`

- [AWS::GuardDuty::Detector.CFNDataSourceConfigurations](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html)
  - Now available to **ALL** regions.

- [AWS::GuardDuty::Detector.CFNS3LogsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfns3logsconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::GuardDuty::Filter.Condition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html)
  - Now available to **ALL** regions.

- [AWS::GuardDuty::Filter.FindingCriteria](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalytics::Application.CSVMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-csvmappingparameters.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::Application.Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::Application.InputLambdaProcessor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::Application.InputParallelism](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputparallelism.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::Application.InputProcessingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputprocessingconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::Application.InputSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::Application.JSONMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-jsonmappingparameters.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::Application.KinesisFirehoseInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisfirehoseinput.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::Application.KinesisStreamsInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisstreamsinput.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::Application.MappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-mappingparameters.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::Application.RecordColumn](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::Application.RecordFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordformat.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::ApplicationOutput.DestinationSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-destinationschema.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::ApplicationOutput.KinesisFirehoseOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::ApplicationOutput.KinesisStreamsOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::ApplicationOutput.LambdaOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-lambdaoutput.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::ApplicationOutput.Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::ApplicationReferenceDataSource.CSVMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::ApplicationReferenceDataSource.JSONMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-jsonmappingparameters.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::ApplicationReferenceDataSource.MappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-mappingparameters.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::ApplicationReferenceDataSource.RecordColumn](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::ApplicationReferenceDataSource.RecordFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordformat.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::ApplicationReferenceDataSource.ReferenceDataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::ApplicationReferenceDataSource.ReferenceSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalytics::ApplicationReferenceDataSource.S3ReferenceDataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::KinesisAnalyticsV2::Application.ApplicationCodeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.ApplicationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.ApplicationSnapshotConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.CSVMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.CatalogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-catalogconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.CheckpointConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.CodeContent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.CustomArtifactConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.CustomArtifactsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactsconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.DeployAsApplicationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.EnvironmentProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-environmentproperties.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.FlinkApplicationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.GlueDataCatalogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-gluedatacatalogconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.InputLambdaProcessor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.InputParallelism](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputparallelism.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.InputProcessingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.InputSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.JSONMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-jsonmappingparameters.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.KinesisFirehoseInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.KinesisStreamsInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisstreamsinput.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.MappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.MavenReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.MonitoringConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.ParallelismConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.PropertyGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.RecordColumn](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.RecordFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.S3ContentBaseLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentbaselocation.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.S3ContentLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.SqlApplicationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-sqlapplicationconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.ZeppelinApplicationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::Application.ZeppelinMonitoringConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinmonitoringconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption.CloudWatchLoggingOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::ApplicationOutput.DestinationSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-destinationschema.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::ApplicationOutput.KinesisFirehoseOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisfirehoseoutput.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::ApplicationOutput.KinesisStreamsOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::ApplicationOutput.LambdaOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-lambdaoutput.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::ApplicationOutput.Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.CSVMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.JSONMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.MappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.RecordColumn](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.RecordFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.ReferenceDataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.ReferenceSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.S3ReferenceDataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `eu-west-3`

- [AWS::LakeFormation::DataLakeSettings.Admins](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-admins.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::LakeFormation::DataLakeSettings.DataLakePrincipal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-datalakeprincipal.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::LakeFormation::Permissions.ColumnWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::LakeFormation::Permissions.DataLakePrincipal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalakeprincipal.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::LakeFormation::Permissions.DataLocationResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::LakeFormation::Permissions.DatabaseResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::LakeFormation::Permissions.Resource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::LakeFormation::Permissions.TableResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::LakeFormation::Permissions.TableWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewildcard.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::LakeFormation::Permissions.TableWithColumnsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::Lambda::EventInvokeConfig.DestinationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig.html)
  - Now available to **ALL** regions.

- [AWS::Lambda::EventInvokeConfig.OnFailure](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onfailure.html)
  - Now available to **ALL** regions.

- [AWS::Lambda::EventInvokeConfig.OnSuccess](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onsuccess.html)
  - Now available to **ALL** regions.

- [AWS::Lambda::LayerVersion.Content](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html)
  - Now available to **ALL** regions.

- [AWS::MSK::Cluster.BrokerLogs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.BrokerNodeGroupInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.ClientAuthentication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.CloudWatchLogs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.ConfigurationInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.EBSStorageInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.EncryptionAtRest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionatrest.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.EncryptionInTransit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.EncryptionInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.Firehose](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.Iam](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-iam.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.JmxExporter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-jmxexporter.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.LoggingInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-logginginfo.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.NodeExporter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-nodeexporter.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.OpenMonitoring](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.Prometheus](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.S3](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.Sasl](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.Scram](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-scram.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.StorageInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-storageinfo.html)
  - `eu-south-1`

- [AWS::MSK::Cluster.Tls](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html)
  - `eu-south-1`

- [AWS::MediaConvert::JobTemplate.AccelerationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-accelerationsettings.html)
  - `cn-northwest-1`

- [AWS::MediaConvert::JobTemplate.HopDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-hopdestination.html)
  - `cn-northwest-1`

- [AWS::MediaLive::Channel.AacSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.Ac3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.AncillarySourceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ancillarysourcesettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.ArchiveCdnSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecdnsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.ArchiveContainerSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecontainersettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.ArchiveGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivegroupsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.ArchiveOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archiveoutputsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.ArchiveS3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archives3settings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.AribDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aribdestinationsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.AribSourceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aribsourcesettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.AudioChannelMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiochannelmapping.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.AudioCodecSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.AudioDescription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.AudioLanguageSelection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiolanguageselection.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.AudioNormalizationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audionormalizationsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.AudioOnlyHlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.AudioPidSelection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiopidselection.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.AudioSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselector.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.AudioSelectorSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselectorsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.AudioSilenceFailoverSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiosilencefailoversettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.AudioTrack](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrack.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.AudioTrackSelection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrackselection.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.AutomaticInputFailoverSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-automaticinputfailoversettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.AvailBlanking](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availblanking.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.AvailConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availconfiguration.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.AvailSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.BlackoutSlate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.BurnInDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.CaptionDescription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.CaptionDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.CaptionLanguageMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionlanguagemapping.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.CaptionRectangle](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionrectangle.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.CaptionSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselector.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.CaptionSelectorSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.CdiInputSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-cdiinputspecification.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.ColorSpacePassthroughSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-colorspacepassthroughsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.DvbNitSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbnitsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.DvbSdtSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.DvbSubDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.DvbSubSourceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubsourcesettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.DvbTdtSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbtdtsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.Eac3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.EbuTtDDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.EmbeddedDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddeddestinationsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.EmbeddedPlusScte20DestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedplusscte20destinationsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.EmbeddedSourceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedsourcesettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.EncoderSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.FailoverCondition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-failovercondition.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.FailoverConditionSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-failoverconditionsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.FeatureActivations](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-featureactivations.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.FecOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fecoutputsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.Fmp4HlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fmp4hlssettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.FrameCaptureCdnSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturecdnsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.FrameCaptureGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturegroupsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.FrameCaptureHlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturehlssettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.FrameCaptureOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptureoutputsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.FrameCaptureS3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptures3settings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.FrameCaptureSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturesettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.GlobalConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.H264ColorSpaceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264colorspacesettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.H264FilterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264filtersettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.H264Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.H265ColorSpaceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.H265FilterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265filtersettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.H265Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.Hdr10Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hdr10settings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.HlsAkamaiSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.HlsBasicPutSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.HlsCdnSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.HlsGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.HlsInputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsinputsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.HlsMediaStoreSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.HlsOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.HlsS3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlss3settings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.HlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.HlsWebdavSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.HtmlMotionGraphicsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-htmlmotiongraphicssettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.InputAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputattachment.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.InputChannelLevel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputchannellevel.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.InputLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlocation.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.InputLossBehavior](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.InputLossFailoverSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossfailoversettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.InputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.InputSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputspecification.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.KeyProviderSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-keyprovidersettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.M2tsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.M3u8Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.MediaPackageGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackagegroupsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.MediaPackageOutputDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackageoutputdestinationsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.MediaPackageOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackageoutputsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.MotionGraphicsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-motiongraphicsconfiguration.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.MotionGraphicsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-motiongraphicssettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.Mp2Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.Mpeg2FilterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2filtersettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.Mpeg2Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mpeg2settings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.MsSmoothGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.MsSmoothOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothoutputsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.MultiplexGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexgroupsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.MultiplexOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexoutputsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.MultiplexProgramChannelDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.NetworkInputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-networkinputsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.NielsenConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenconfiguration.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.OutputDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestination.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.OutputDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestinationsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.OutputGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroup.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.OutputGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.OutputLocationRef](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputlocationref.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.OutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.PassThroughSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-passthroughsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.RawSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rawsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.Rec601Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rec601settings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.Rec709Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rec709settings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.RemixSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-remixsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.RtmpCaptionInfoDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpcaptioninfodestinationsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.RtmpGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.RtmpOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.Scte20PlusEmbeddedDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20plusembeddeddestinationsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.Scte20SourceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20sourcesettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.Scte27DestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte27destinationsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.Scte27SourceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte27sourcesettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.Scte35SpliceInsert](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35spliceinsert.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.Scte35TimeSignalApos](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35timesignalapos.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.SmpteTtDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-smptettdestinationsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.StandardHlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-standardhlssettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.StaticKeySettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-statickeysettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.TeletextDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-teletextdestinationsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.TeletextSourceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-teletextsourcesettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.TemporalFilterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-temporalfiltersettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.TimecodeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-timecodeconfig.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.TtmlDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ttmldestinationsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.UdpContainerSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpcontainersettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.UdpGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpgroupsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.UdpOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.VideoBlackFailoverSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoblackfailoversettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.VideoCodecSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.VideoDescription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.VideoSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselector.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.VideoSelectorColorSpaceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorcolorspacesettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.VideoSelectorPid](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorpid.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.VideoSelectorProgramId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorprogramid.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.VideoSelectorSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.VpcOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-vpcoutputsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.WavSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-wavsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::Channel.WebvttDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-webvttdestinationsettings.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaLive::InputSecurityGroup.InputWhitelistRuleCidr](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-inputsecuritygroup-inputwhitelistrulecidr.html)
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-west-2`

- [AWS::MediaStore::Container.CorsRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html)
  - `eu-west-2`
  - `ap-south-1`
  - `sa-east-1`

- [AWS::MediaStore::Container.MetricPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-metricpolicy.html)
  - `eu-west-2`
  - `ap-south-1`
  - `sa-east-1`

- [AWS::MediaStore::Container.MetricPolicyRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-metricpolicyrule.html)
  - `eu-west-2`
  - `ap-south-1`
  - `sa-east-1`

- [AWS::Neptune::DBCluster.DBClusterRole](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptune-dbcluster-dbclusterrole.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `ap-east-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `us-gov-east-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::ApplicationSettings.CampaignHook](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::ApplicationSettings.Limits](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::ApplicationSettings.QuietTime](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-quiettime.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Campaign.AttributeDimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-attributedimension.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Campaign.CampaignEmailMessage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Campaign.CampaignEventFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigneventfilter.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Campaign.CampaignHook](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Campaign.CampaignSmsMessage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Campaign.EventDimensions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Campaign.Limits](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Campaign.Message](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Campaign.MessageConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Campaign.MetricDimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-metricdimension.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Campaign.QuietTime](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule-quiettime.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Campaign.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Campaign.SetDimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-setdimension.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Campaign.WriteTreatmentResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::PushTemplate.APNSPushNotificationTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::Pinpoint::PushTemplate.AndroidPushNotificationTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::Pinpoint::PushTemplate.DefaultPushNotificationTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::Pinpoint::Segment.AttributeDimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-attributedimension.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Segment.Behavior](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Segment.Coordinates](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Segment.Demographic](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Segment.GPSPoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Segment.Groups](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Segment.Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Segment.Recency](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior-recency.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Segment.SegmentDimensions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Segment.SegmentGroups](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Segment.SetDimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-setdimension.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::Pinpoint::Segment.SourceSegments](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups-sourcesegments.html)
  - `ap-southeast-1`
  - `us-gov-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ap-northeast-2`

- [AWS::RoboMaker::RobotApplication.RobotSoftwareSuite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-robotsoftwaresuite.html)
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `ap-south-1`

- [AWS::RoboMaker::RobotApplication.SourceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-sourceconfig.html)
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `ap-south-1`

- [AWS::RoboMaker::SimulationApplication.RenderingEngine](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-renderingengine.html)
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `ap-south-1`

- [AWS::RoboMaker::SimulationApplication.RobotSoftwareSuite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-robotsoftwaresuite.html)
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `ap-south-1`

- [AWS::RoboMaker::SimulationApplication.SimulationSoftwareSuite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-simulationsoftwaresuite.html)
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `ap-south-1`

- [AWS::RoboMaker::SimulationApplication.SourceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-sourceconfig.html)
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `ap-south-1`

- [AWS::Route53Resolver::ResolverEndpoint.IpAddressRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html)
  - Now available to **ALL** regions.

- [AWS::Route53Resolver::ResolverRule.TargetAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html)
  - Now available to **ALL** regions.

- [AWS::SSM::MaintenanceWindowTarget.Targets](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtarget-targets.html)
  - Now available to **ALL** regions.

- [AWS::SSM::MaintenanceWindowTask.LoggingInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html)
  - Now available to **ALL** regions.

- [AWS::SSM::MaintenanceWindowTask.MaintenanceWindowAutomationParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowautomationparameters.html)
  - Now available to **ALL** regions.

- [AWS::SSM::MaintenanceWindowTask.MaintenanceWindowLambdaParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html)
  - Now available to **ALL** regions.

- [AWS::SSM::MaintenanceWindowTask.MaintenanceWindowRunCommandParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html)
  - Now available to **ALL** regions.

- [AWS::SSM::MaintenanceWindowTask.MaintenanceWindowStepFunctionsParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.html)
  - Now available to **ALL** regions.

- [AWS::SSM::MaintenanceWindowTask.NotificationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html)
  - Now available to **ALL** regions.

- [AWS::SSM::MaintenanceWindowTask.Target](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-target.html)
  - Now available to **ALL** regions.

- [AWS::SSM::MaintenanceWindowTask.TaskInvocationParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html)
  - Now available to **ALL** regions.

- [AWS::SSM::PatchBaseline.PatchFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfilter.html)
  - Now available to **ALL** regions.

- [AWS::SSM::PatchBaseline.PatchFilterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfiltergroup.html)
  - Now available to **ALL** regions.

- [AWS::SSM::PatchBaseline.PatchSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html)
  - Now available to **ALL** regions.

- [AWS::SSM::PatchBaseline.PatchStringDate]()
  - Now available to **ALL** regions.

- [AWS::SSM::PatchBaseline.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html)
  - Now available to **ALL** regions.

- [AWS::SSM::PatchBaseline.RuleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rulegroup.html)
  - Now available to **ALL** regions.

- [AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html)
  - `sa-east-1`

- [AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttributeValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html)
  - `sa-east-1`

- [AWS::SageMaker::CodeRepository.GitConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `eu-north-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::SageMaker::Endpoint.Alarm](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-alarm.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::SageMaker::Endpoint.AutoRollbackConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-autorollbackconfig.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::SageMaker::Endpoint.BlueGreenUpdatePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::SageMaker::Endpoint.CapacitySize](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-capacitysize.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::SageMaker::Endpoint.DeploymentConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-deploymentconfig.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::SageMaker::Endpoint.TrafficRoutingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::SageMaker::Endpoint.VariantProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-variantproperty.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::SageMaker::EndpointConfig.CaptureContentTypeHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::SageMaker::EndpointConfig.CaptureOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-captureoption.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::SageMaker::EndpointConfig.DataCaptureConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::SageMaker::EndpointConfig.ProductionVariant](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::SageMaker::Model.ContainerDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::SageMaker::Model.ImageConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::SageMaker::Model.InferenceExecutionConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-inferenceexecutionconfig.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::SageMaker::Model.MultiModelConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-multimodelconfig.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::SageMaker::Model.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-vpcconfig.html)
  - `us-gov-west-1`
  - `af-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-east-1`
  - `eu-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::SageMaker::NotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHook](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-central-1`

- [AWS::SageMaker::Workteam.CognitoMemberDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-cognitomemberdefinition.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::SageMaker::Workteam.MemberDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-memberdefinition.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::SageMaker::Workteam.NotificationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-notificationconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `eu-west-2`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`
  - `eu-central-1`

- [AWS::SecretsManager::RotationSchedule.HostedRotationLambda](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.html)
  - Now available to **ALL** regions.

- [AWS::SecretsManager::RotationSchedule.RotationRules](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-rotationrules.html)
  - Now available to **ALL** regions.

- [AWS::SecretsManager::Secret.GenerateSecretString](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-generatesecretstring.html)
  - Now available to **ALL** regions.

- [AWS::SecretsManager::Secret.ReplicaRegion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-replicaregion.html)
  - Now available to **ALL** regions.

- [AWS::ServiceCatalog::CloudFormationProduct.ProvisioningArtifactProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html)
  - Now available to **ALL** regions.

- [AWS::ServiceDiscovery::PrivateDnsNamespace.PrivateDnsPropertiesMutable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-privatednspropertiesmutable.html)
  - `us-east-2`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-1`
  - `eu-west-3`
  - `ap-northeast-2`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `eu-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `eu-south-1`
  - `eu-west-2`
  - `us-east-1`
  - `sa-east-1`
  - `ap-southeast-2`

- [AWS::ServiceDiscovery::PrivateDnsNamespace.Properties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-properties.html)
  - `us-east-2`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-1`
  - `eu-west-3`
  - `ap-northeast-2`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `eu-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `eu-south-1`
  - `eu-west-2`
  - `us-east-1`
  - `sa-east-1`
  - `ap-southeast-2`

- [AWS::ServiceDiscovery::PrivateDnsNamespace.SOA](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-soa.html)
  - `us-east-2`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-1`
  - `eu-west-3`
  - `ap-northeast-2`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `eu-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `eu-south-1`
  - `eu-west-2`
  - `us-east-1`
  - `sa-east-1`
  - `ap-southeast-2`

- [AWS::ServiceDiscovery::PublicDnsNamespace.Properties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-publicdnsnamespace-properties.html)
  - `us-east-2`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-1`
  - `eu-west-3`
  - `ap-northeast-2`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `eu-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `eu-south-1`
  - `eu-west-2`
  - `us-east-1`
  - `sa-east-1`
  - `ap-southeast-2`

- [AWS::ServiceDiscovery::PublicDnsNamespace.PublicDnsPropertiesMutable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-publicdnsnamespace-publicdnspropertiesmutable.html)
  - `us-east-2`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-1`
  - `eu-west-3`
  - `ap-northeast-2`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `eu-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `eu-south-1`
  - `eu-west-2`
  - `us-east-1`
  - `sa-east-1`
  - `ap-southeast-2`

- [AWS::ServiceDiscovery::PublicDnsNamespace.SOA](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-publicdnsnamespace-soa.html)
  - `us-east-2`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `ap-northeast-1`
  - `eu-west-3`
  - `ap-northeast-2`
  - `eu-north-1`
  - `af-south-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `eu-west-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `eu-south-1`
  - `eu-west-2`
  - `us-east-1`
  - `sa-east-1`
  - `ap-southeast-2`

- [AWS::ServiceDiscovery::Service.DnsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsconfig.html)
  - `sa-east-1`

- [AWS::ServiceDiscovery::Service.DnsRecord](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsrecord.html)
  - `sa-east-1`

- [AWS::ServiceDiscovery::Service.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckconfig.html)
  - `sa-east-1`

- [AWS::ServiceDiscovery::Service.HealthCheckCustomConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckcustomconfig.html)
  - `sa-east-1`

- [AWS::StepFunctions::Activity.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html)
  - Now available to **ALL** regions.

- [AWS::Transfer::User.HomeDirectoryMapEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::Transfer::User.PosixProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::Transfer::User.SshPublicKey]()
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::WAFRegional::ByteMatchSet.ByteMatchTuple](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::ByteMatchSet.FieldToMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-fieldtomatch.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::GeoMatchSet.GeoMatchConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-geomatchset-geomatchconstraint.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::IPSet.IPSetDescriptor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ipset-ipsetdescriptor.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::RateBasedRule.Predicate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ratebasedrule-predicate.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::Rule.Predicate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::SizeConstraintSet.FieldToMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-fieldtomatch.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::SizeConstraintSet.SizeConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::SqlInjectionMatchSet.FieldToMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-fieldtomatch.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::SqlInjectionMatchSet.SqlInjectionMatchTuple](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::WebACL.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-action.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::WebACL.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::XssMatchSet.FieldToMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-fieldtomatch.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [AWS::WAFRegional::XssMatchSet.XssMatchTuple](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-xssmatchtuple.html)
  - `af-south-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `eu-south-1`
  - `ap-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`
  - `cn-north-1`
  - `eu-west-3`

- [Alexa::ASK::Skill.AuthenticationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-authenticationconfiguration.html)
  - `ap-northeast-1`

- [Alexa::ASK::Skill.Overrides](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-overrides.html)
  - `ap-northeast-1`

- [Alexa::ASK::Skill.SkillPackage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html)
  - `ap-northeast-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v39.3.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v39.3.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::Glue::Crawler.RecrawlPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-recrawlpolicy.html)
    - `ap-northeast-3`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - [AWS::Glue::Database.DataLakePrincipal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-datalakeprincipal.html)
    - `me-south-1`

  - [AWS::Glue::Database.PrincipalPrivileges](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-principalprivileges.html)
    - `me-south-1`

## [39.3.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.3.0) (2021-06-25)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v39-changelog.json)
  - Change source is a diff between [v39.3.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.3.0) and [v39.2.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.2.0)

### Totals

- TotalPropertyTypes: 2513 **(+12)**
- TotalPropertyTypesSupportedGlobally: 688 **(+0)**
- TotalResourceTypes: 772 **(+4)**
- TotalResourceTypesSupportedGlobally: 233 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::CloudFormation::PublicTypeVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFormation::Publisher](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFormation::TypeActivation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::Connect::QuickConnect](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::AppSync::GraphQLApi.LambdaAuthorizerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::CloudFormation::TypeActivation.LoggingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-typeactivation-loggingconfig.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::Connect::QuickConnect.PhoneNumberQuickConnectConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-phonenumberquickconnectconfig.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::Connect::QuickConnect.QueueQuickConnectConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-queuequickconnectconfig.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::Connect::QuickConnect.QuickConnectConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::Connect::QuickConnect.UserQuickConnectConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-userquickconnectconfig.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::FSx::FileSystem.AuditLogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-auditlogconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::IoTAnalytics::Datastore.DatastorePartition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartition.html)
  - `us-east-2`

- [AWS::IoTAnalytics::Datastore.DatastorePartitions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartitions.html)
  - `us-east-2`

- [AWS::IoTAnalytics::Datastore.Partition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-partition.html)
  - `us-east-2`

- [AWS::IoTAnalytics::Datastore.TimestampPartition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-timestamppartition.html)
  - `us-east-2`

- [AWS::Redshift::Cluster.Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-endpoint.html)
  - `ap-northeast-1`
  - `ap-northeast-3`
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

- [AWS::Config::ConfigurationAggregator](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html)
  - `eu-west-3`
  - `ap-northeast-2`

- [AWS::EC2::CarrierGateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-carriergateway.html)
  - `us-east-2`
  - `eu-central-1`

- [AWS::EC2::TransitGateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html)
  - `eu-north-1`

- [AWS::AppMesh::GatewayRoute.GatewayRouteHostnameMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch.html)
  - `us-west-1`
  - `eu-west-3`
  - `eu-north-1`
  - `me-south-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-east-1`
  - `ap-northeast-2`

- [AWS::AppMesh::GatewayRoute.GatewayRouteHostnameRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamerewrite.html)
  - `us-west-1`
  - `eu-west-3`
  - `eu-north-1`
  - `me-south-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-east-1`
  - `ap-northeast-2`

- [AWS::AppMesh::GatewayRoute.GatewayRouteMetadataMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html)
  - `us-west-1`
  - `eu-west-3`
  - `eu-north-1`
  - `me-south-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-east-1`
  - `ap-northeast-2`

- [AWS::AppMesh::GatewayRoute.GatewayRouteRangeMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayrouterangematch.html)
  - `us-west-1`
  - `eu-west-3`
  - `eu-north-1`
  - `me-south-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-east-1`
  - `ap-northeast-2`

- [AWS::AppMesh::GatewayRoute.GrpcGatewayRouteMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html)
  - `us-west-1`
  - `eu-west-3`
  - `eu-north-1`
  - `me-south-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-east-1`
  - `ap-northeast-2`

- [AWS::AppMesh::GatewayRoute.GrpcGatewayRouteRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouterewrite.html)
  - `us-west-1`
  - `eu-west-3`
  - `eu-north-1`
  - `me-south-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-east-1`
  - `ap-northeast-2`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRouteHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html)
  - `us-west-1`
  - `eu-west-3`
  - `eu-north-1`
  - `me-south-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-east-1`
  - `ap-northeast-2`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRouteHeaderMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html)
  - `us-west-1`
  - `eu-west-3`
  - `eu-north-1`
  - `me-south-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-east-1`
  - `ap-northeast-2`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRoutePathRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutepathrewrite.html)
  - `us-west-1`
  - `eu-west-3`
  - `eu-north-1`
  - `me-south-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-east-1`
  - `ap-northeast-2`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRoutePrefixRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite.html)
  - `us-west-1`
  - `eu-west-3`
  - `eu-north-1`
  - `me-south-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-east-1`
  - `ap-northeast-2`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRouteRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html)
  - `us-west-1`
  - `eu-west-3`
  - `eu-north-1`
  - `me-south-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-east-1`
  - `ap-northeast-2`

- [AWS::AppMesh::GatewayRoute.HttpPathMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httppathmatch.html)
  - `us-west-1`
  - `eu-west-3`
  - `eu-north-1`
  - `me-south-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-east-1`
  - `ap-northeast-2`

- [AWS::AppMesh::GatewayRoute.HttpQueryParameterMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpqueryparametermatch.html)
  - `us-west-1`
  - `eu-west-3`
  - `eu-north-1`
  - `me-south-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-east-1`
  - `ap-northeast-2`

- [AWS::AppMesh::GatewayRoute.QueryParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-queryparameter.html)
  - `us-west-1`
  - `eu-west-3`
  - `eu-north-1`
  - `me-south-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-east-1`
  - `ap-northeast-2`

- [AWS::AppMesh::Route.HttpPathMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httppathmatch.html)
  - `us-west-1`
  - `us-east-2`
  - `eu-west-2`
  - `ap-northeast-2`

- [AWS::AppMesh::Route.HttpQueryParameterMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpqueryparametermatch.html)
  - `us-west-1`
  - `us-east-2`
  - `eu-west-2`
  - `ap-northeast-2`

- [AWS::AppMesh::Route.QueryParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-queryparameter.html)
  - `us-west-1`
  - `us-east-2`
  - `eu-west-2`
  - `ap-northeast-2`

- [AWS::Config::ConfigurationAggregator.AccountAggregationSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html)
  - `eu-west-3`
  - `ap-northeast-2`

- [AWS::Config::ConfigurationAggregator.OrganizationAggregationSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html)
  - `eu-west-3`
  - `ap-northeast-2`

- [AWS::DataBrew::Recipe.ParameterMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-parametermap.html)
  - `eu-north-1`
  - `cn-northwest-1`

- [AWS::Transfer::Server.ProtocolDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocoldetails.html)
  - `us-west-2`
  - `eu-north-1`
  - `eu-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-northeast-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v39.2.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v39.2.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::IoTAnalytics::Datastore.DatastorePartition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartition.html)
    - `us-east-2`

  - [AWS::IoTAnalytics::Datastore.DatastorePartitions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartitions.html)
    - `us-east-2`

  - [AWS::IoTAnalytics::Datastore.Partition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-partition.html)
    - `us-east-2`

  - [AWS::IoTAnalytics::Datastore.TimestampPartition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-timestamppartition.html)
    - `us-east-2`

## [39.2.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.2.0) (2021-06-18)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v39-changelog.json)
  - Change source is a diff between [v39.2.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.2.0) and [v39.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.1.0)

### Totals

- TotalPropertyTypes: 2501 **(+19)**
- TotalPropertyTypesSupportedGlobally: 688 **(+22)**
- TotalResourceTypes: 768 **(+1)**
- TotalResourceTypesSupportedGlobally: 233 **(+12)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::KMS::ReplicaKey](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html)
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

- [AWS::AppMesh::GatewayRoute.GatewayRouteHostnameMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.GatewayRouteHostnameRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamerewrite.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.GatewayRouteMetadataMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.GatewayRouteRangeMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayrouterangematch.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.GrpcGatewayRouteMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.GrpcGatewayRouteRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouterewrite.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRouteHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRouteHeaderMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRoutePathRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutepathrewrite.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRoutePrefixRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRouteRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.HttpPathMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httppathmatch.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.HttpQueryParameterMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpqueryparametermatch.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.QueryParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-queryparameter.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::Route.HttpPathMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httppathmatch.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::Route.HttpQueryParameterMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpqueryparametermatch.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::Route.QueryParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-queryparameter.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::DataBrew::Recipe.ParameterMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-parametermap.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Transfer::Server.ProtocolDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocoldetails.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::ApiGateway::VpcLink](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-vpclink.html)
  - `eu-west-3`
  - `eu-central-1`

- [AWS::ApiGatewayV2::Api](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::ApiGatewayManagedOverrides](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html)
  - `cn-northwest-1`
  - `cn-north-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `ap-southeast-1`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-1`
  - `me-south-1`
  - `ap-southeast-2`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `af-south-1`
  - `eu-central-1`
  - `us-east-2`
  - `eu-west-3`

- [AWS::ApiGatewayV2::ApiMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Authorizer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Deployment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::DomainName](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Integration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::IntegrationResponse](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Model](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Route](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::RouteResponse](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Stage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::VpcLink](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html)
  - `cn-northwest-1`
  - `cn-north-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `us-west-1`
  - `ap-southeast-1`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-1`
  - `me-south-1`
  - `ap-southeast-2`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `af-south-1`
  - `eu-central-1`
  - `us-east-2`
  - `eu-west-3`

- [AWS::Config::ConfigurationAggregator](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html)
  - `eu-west-2`

- [AWS::EC2::EC2Fleet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html)
  - Now available to **ALL** regions.

- [AWS::GuardDuty::Detector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html)
  - `ap-northeast-3`

- [AWS::GuardDuty::Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html)
  - `ap-northeast-3`

- [AWS::GuardDuty::IPSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html)
  - `ap-northeast-3`

- [AWS::GuardDuty::Master](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html)
  - `ap-northeast-3`

- [AWS::GuardDuty::Member](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html)
  - `ap-northeast-3`

- [AWS::GuardDuty::ThreatIntelSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html)
  - `ap-northeast-3`

- [AWS::ApiGatewayV2::Api.BodyS3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Api.Cors](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::ApiGatewayManagedOverrides.AccessLogSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings.html)
  - `cn-northwest-1`
  - `cn-north-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `ap-southeast-1`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-1`
  - `me-south-1`
  - `ap-southeast-2`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `af-south-1`
  - `eu-central-1`
  - `us-east-2`
  - `eu-west-3`

- [AWS::ApiGatewayV2::ApiGatewayManagedOverrides.IntegrationOverrides](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html)
  - `cn-northwest-1`
  - `cn-north-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `ap-southeast-1`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-1`
  - `me-south-1`
  - `ap-southeast-2`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `af-south-1`
  - `eu-central-1`
  - `us-east-2`
  - `eu-west-3`

- [AWS::ApiGatewayV2::ApiGatewayManagedOverrides.RouteOverrides](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html)
  - `cn-northwest-1`
  - `cn-north-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `ap-southeast-1`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-1`
  - `me-south-1`
  - `ap-southeast-2`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `af-south-1`
  - `eu-central-1`
  - `us-east-2`
  - `eu-west-3`

- [AWS::ApiGatewayV2::ApiGatewayManagedOverrides.RouteSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html)
  - `cn-northwest-1`
  - `cn-north-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `ap-southeast-1`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-1`
  - `me-south-1`
  - `ap-southeast-2`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `af-south-1`
  - `eu-central-1`
  - `us-east-2`
  - `eu-west-3`

- [AWS::ApiGatewayV2::ApiGatewayManagedOverrides.StageOverrides](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html)
  - `cn-northwest-1`
  - `cn-north-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `ap-southeast-1`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-1`
  - `me-south-1`
  - `ap-southeast-2`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `af-south-1`
  - `eu-central-1`
  - `us-east-2`
  - `eu-west-3`

- [AWS::ApiGatewayV2::Authorizer.JWTConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::DomainName.DomainNameConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::DomainName.MutualTlsAuthentication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-mutualtlsauthentication.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Integration.ResponseParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameter.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Integration.ResponseParameterList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameterlist.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Integration.TlsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-tlsconfig.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Route.ParameterConstraints](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-route-parameterconstraints.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::RouteResponse.ParameterConstraints](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-routeresponse-parameterconstraints.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Stage.AccessLogSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-accesslogsettings.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Stage.RouteSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html)
  - Now available to **ALL** regions.

- [AWS::Config::ConfigurationAggregator.AccountAggregationSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html)
  - `eu-west-2`

- [AWS::Config::ConfigurationAggregator.OrganizationAggregationSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html)
  - `eu-west-2`

- [AWS::EC2::EC2Fleet.CapacityReservationOptionsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-capacityreservationoptionsrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.FleetLaunchTemplateConfigRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateconfigrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.FleetLaunchTemplateOverridesRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.FleetLaunchTemplateSpecificationRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.OnDemandOptionsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-ondemandoptionsrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.Placement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-placement.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.SpotOptionsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-spotoptionsrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.TagSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-tagspecification.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.TargetCapacitySpecificationRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-targetcapacityspecificationrequest.html)
  - Now available to **ALL** regions.

- [AWS::EKS::Nodegroup.UpdateConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-updateconfig.html)
  - Now available to **ALL** regions.

- [AWS::GuardDuty::Detector.CFNDataSourceConfigurations](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html)
  - `ap-northeast-3`

- [AWS::GuardDuty::Detector.CFNS3LogsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfns3logsconfiguration.html)
  - `ap-northeast-3`

- [AWS::GuardDuty::Filter.Condition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html)
  - `ap-northeast-3`

- [AWS::GuardDuty::Filter.FindingCriteria](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html)
  - `ap-northeast-3`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v39.1.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v39.1.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

## [39.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.1.0) (2021-06-11)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v39-changelog.json)
  - Change source is a diff between [v39.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.1.0) and [v38.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v38.0.0)

### Totals

- TotalPropertyTypes: 2482 **(+3)**
- TotalPropertyTypesSupportedGlobally: 666 **(+0)**
- TotalResourceTypes: 767 **(+0)**
- TotalResourceTypesSupportedGlobally: 221 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::EKS::Nodegroup.UpdateConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-updateconfig.html)
  - `ap-northeast-2`

- [AWS::SSMContacts::Contact.ChannelTargetInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-channeltargetinfo.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::SSMContacts::Contact.ContactTargetInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-contacttargetinfo.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::AuditManager::Assessment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html)
  - `ap-south-1`
  - `ca-central-1`

- [AWS::EC2::CarrierGateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-carriergateway.html)
  - `eu-west-2`

- [AWS::AuditManager::Assessment.AWSAccount](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsaccount.html)
  - `ap-south-1`
  - `ca-central-1`

- [AWS::AuditManager::Assessment.AWSService](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsservice.html)
  - `ap-south-1`
  - `ca-central-1`

- [AWS::AuditManager::Assessment.AssessmentReportsDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-assessmentreportsdestination.html)
  - `ap-south-1`
  - `ca-central-1`

- [AWS::AuditManager::Assessment.Delegation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html)
  - `ap-south-1`
  - `ca-central-1`

- [AWS::AuditManager::Assessment.Role](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-role.html)
  - `ap-south-1`
  - `ca-central-1`

- [AWS::AuditManager::Assessment.Scope](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-scope.html)
  - `ap-south-1`
  - `ca-central-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v38.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v38.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::EKS::Nodegroup.UpdateConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-updateconfig.html)
    - `ap-northeast-2`

