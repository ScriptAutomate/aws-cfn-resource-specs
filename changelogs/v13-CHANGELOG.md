# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v13-changelog.json`](changelogs/v13-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [13.0.0](#1300-2020-04-17)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [13.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v13.0.0) (2020-04-17)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v13-changelog.json)
  - Change source is a diff between [v13.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v13.0.0) and [v12.3.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v12.3.0)

### Totals

- TotalPropertyTypes: 1325 **(+-7)**
- TotalPropertyTypesSupportedGlobally: 520 **(+0)**
- TotalResourceTypes: 523 **(+-5)**
- TotalResourceTypesSupportedGlobally: 193 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::MediaConvert::JobTemplate.HopDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-hopdestination.html)
  - `us-east-1`
  - `eu-west-1`

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::ImageBuilder::Component](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::ImageBuilder::DistributionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::ImageBuilder::ImagePipeline](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::ImageBuilder::ImageRecipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::ImageBuilder::InfrastructureConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::ImageBuilder::DistributionConfiguration.Distribution](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::ImageBuilder::ImagePipeline.ImageTestsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::ImageBuilder::ImagePipeline.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::ImageBuilder::ImageRecipe.ComponentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::ImageBuilder::ImageRecipe.EbsInstanceBlockDeviceSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::ImageBuilder::ImageRecipe.InstanceBlockDeviceMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::ImageBuilder::InfrastructureConfiguration.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-logging.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::ImageBuilder::InfrastructureConfiguration.S3Logs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Glue::Classifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-classifier.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Connection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-connection.html)
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Crawler](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::DataCatalogEncryptionSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-datacatalogencryptionsettings.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Database](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-database.html)
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::DevEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Job](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html)
  - `cn-northwest-1`

- [AWS::Glue::MLTransform](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html)
  - `eu-north-1`
  - `eu-west-3`

- [AWS::Glue::Partition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-partition.html)
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::SecurityConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-securityconfiguration.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Table](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.html)
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Trigger](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html)
  - `cn-northwest-1`

- [AWS::Glue::Workflow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-workflow.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::NetworkManager::CustomerGatewayAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html)
  - `ap-east-1`
  - `me-south-1`
  - `eu-north-1`

- [AWS::NetworkManager::Device](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html)
  - `ap-east-1`
  - `me-south-1`
  - `eu-north-1`

- [AWS::NetworkManager::GlobalNetwork](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html)
  - `ap-east-1`
  - `me-south-1`
  - `eu-north-1`

- [AWS::NetworkManager::Link](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html)
  - `ap-east-1`
  - `me-south-1`
  - `eu-north-1`

- [AWS::NetworkManager::LinkAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html)
  - `ap-east-1`
  - `me-south-1`
  - `eu-north-1`

- [AWS::NetworkManager::Site](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html)
  - `ap-east-1`
  - `me-south-1`
  - `eu-north-1`

- [AWS::NetworkManager::TransitGatewayRegistration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html)
  - `ap-east-1`
  - `me-south-1`
  - `eu-north-1`

- [AWS::Glue::Classifier.CsvClassifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Classifier.GrokClassifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-grokclassifier.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Classifier.JsonClassifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-jsonclassifier.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Classifier.XMLClassifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-xmlclassifier.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Connection.ConnectionInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-connectioninput.html)
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Connection.PhysicalConnectionRequirements](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-physicalconnectionrequirements.html)
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Crawler.CatalogTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-catalogtarget.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Crawler.DynamoDBTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-dynamodbtarget.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Crawler.JdbcTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-jdbctarget.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Crawler.S3Target](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-s3target.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Crawler.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-schedule.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Crawler.SchemaChangePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-schemachangepolicy.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Crawler.Targets](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-targets.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::DataCatalogEncryptionSettings.ConnectionPasswordEncryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-connectionpasswordencryption.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::DataCatalogEncryptionSettings.DataCatalogEncryptionSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-datacatalogencryptionsettings.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::DataCatalogEncryptionSettings.EncryptionAtRest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-encryptionatrest.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Database.DatabaseInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html)
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Job.ConnectionsList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-connectionslist.html)
  - `cn-northwest-1`

- [AWS::Glue::Job.ExecutionProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-executionproperty.html)
  - `cn-northwest-1`

- [AWS::Glue::Job.JobCommand](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-jobcommand.html)
  - `cn-northwest-1`

- [AWS::Glue::Job.NotificationProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-notificationproperty.html)
  - `cn-northwest-1`

- [AWS::Glue::MLTransform.FindMatchesParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters-findmatchesparameters.html)
  - `eu-north-1`
  - `eu-west-3`

- [AWS::Glue::MLTransform.GlueTables](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables-gluetables.html)
  - `eu-north-1`
  - `eu-west-3`

- [AWS::Glue::MLTransform.InputRecordTables](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables.html)
  - `eu-north-1`
  - `eu-west-3`

- [AWS::Glue::MLTransform.TransformParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters.html)
  - `eu-north-1`
  - `eu-west-3`

- [AWS::Glue::Partition.Column](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-column.html)
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Partition.Order](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-order.html)
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Partition.PartitionInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-partitioninput.html)
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Partition.SerdeInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-serdeinfo.html)
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Partition.SkewedInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-skewedinfo.html)
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Partition.StorageDescriptor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html)
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::SecurityConfiguration.CloudWatchEncryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-cloudwatchencryption.html)
  - `eu-north-1`

- [AWS::Glue::SecurityConfiguration.EncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-encryptionconfiguration.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::SecurityConfiguration.JobBookmarksEncryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-jobbookmarksencryption.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::SecurityConfiguration.S3Encryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-s3encryption.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::SecurityConfiguration.S3Encryptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-s3encryptions.html)
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Table.Column](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-column.html)
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Table.Order](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-order.html)
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Table.SerdeInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-serdeinfo.html)
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Table.SkewedInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-skewedinfo.html)
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Table.StorageDescriptor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html)
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Table.TableInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html)
  - `us-west-1`
  - `eu-west-2`
  - `ca-central-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`

- [AWS::Glue::Trigger.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-action.html)
  - `cn-northwest-1`

- [AWS::Glue::Trigger.Condition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-condition.html)
  - `cn-northwest-1`

- [AWS::Glue::Trigger.NotificationProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-notificationproperty.html)
  - `cn-northwest-1`

- [AWS::Glue::Trigger.Predicate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-predicate.html)
  - `cn-northwest-1`

- [AWS::LakeFormation::Permissions.ColumnWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html)
  - `eu-west-1`
  - `us-east-1`

- [AWS::LakeFormation::Permissions.DataLocationResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html)
  - `eu-west-1`
  - `us-east-1`

- [AWS::LakeFormation::Permissions.TableWithColumnsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html)
  - `eu-west-1`
  - `us-east-1`

- [AWS::NetworkManager::Device.Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html)
  - `ap-east-1`
  - `me-south-1`
  - `eu-north-1`

- [AWS::NetworkManager::Link.Bandwidth](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html)
  - `ap-east-1`
  - `me-south-1`
  - `eu-north-1`

- [AWS::NetworkManager::Site.Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html)
  - `ap-east-1`
  - `me-south-1`
  - `eu-north-1`

- [AWS::SSM::PatchBaseline.PatchStringDate]()
  - `ap-southeast-1`
  - `us-east-1`
  - `ap-northeast-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v12.3.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

  - Since v12.3.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

  - Since v12.3.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

- PropertyType Still Missing
  - Since v12.3.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

  - Since v12.3.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

  - Since v12.3.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

  - Since v12.3.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

  - Since v12.3.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

- PropertyType(s) No Longer Missing
  - [AWS::LakeFormation::Permissions.ColumnWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html)
    - Was missing since v12.3.0

  - [AWS::LakeFormation::Permissions.DataLocationResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html)
    - Was missing since v12.3.0

  - [AWS::LakeFormation::Permissions.TableWithColumnsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html)
    - Was missing since v12.3.0

  - [AWS::SSM::PatchBaseline.PatchStringDate]()
    - Was missing since v12.3.0

