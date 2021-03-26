# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v31-changelog.json`](changelogs/v31-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [31.2.0](#3120-2021-03-26)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)
- [31.1.0](#3110-2021-03-19)
  - [Totals](#totals-1)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-1)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes-1)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-1)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-1)
- [31.0.0](#3100-2021-03-12)
  - [Totals](#totals-2)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-2)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes-2)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-2)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-2)

## [31.2.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v31.2.0) (2021-03-26)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v31-changelog.json)
  - Change source is a diff between [v31.2.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v31.2.0) and [v31.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v31.1.0)

### Totals

- TotalPropertyTypes: 2290 **(+24)**
- TotalPropertyTypesSupportedGlobally: 574 **(+26)**
- TotalResourceTypes: 724 **(+6)**
- TotalResourceTypesSupportedGlobally: 211 **(+12)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::AppIntegrations::EventIntegration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::Domain](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::Integration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::ObjectType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::LookoutMetrics::Alert](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::LookoutMetrics::AnomalyDetector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::AppIntegrations::EventIntegration.EventFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-eventfilter.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppIntegrations::EventIntegration.EventIntegrationAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-eventintegrationassociation.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppIntegrations::EventIntegration.Metadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-metadata.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Batch::JobDefinition.AuthorizationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-authorizationconfig.html)
  - `af-south-1`
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
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Batch::JobDefinition.EfsVolumeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-efsvolumeconfiguration.html)
  - `af-south-1`
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
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFront::Distribution.LegacyCustomOrigin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html)
  - `eu-central-1`

- [AWS::CloudFront::Distribution.LegacyS3Origin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacys3origin.html)
  - `eu-central-1`

- [AWS::CustomerProfiles::ObjectType.FieldMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::ObjectType.KeyMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::ObjectType.ObjectTypeField](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::ObjectType.ObjectTypeKey](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::LookoutMetrics::AnomalyDetector.AppFlowConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-appflowconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::LookoutMetrics::AnomalyDetector.CloudwatchConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-cloudwatchconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::LookoutMetrics::AnomalyDetector.CsvFormatDescriptor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::LookoutMetrics::AnomalyDetector.FileFormatDescriptor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-fileformatdescriptor.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::LookoutMetrics::AnomalyDetector.JsonFormatDescriptor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-jsonformatdescriptor.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::LookoutMetrics::AnomalyDetector.Metric](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::LookoutMetrics::AnomalyDetector.MetricSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::LookoutMetrics::AnomalyDetector.MetricSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::LookoutMetrics::AnomalyDetector.RDSSourceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::LookoutMetrics::AnomalyDetector.RedshiftSourceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::LookoutMetrics::AnomalyDetector.S3SourceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::LookoutMetrics::AnomalyDetector.SecurityGroupIdList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-securitygroupidlist.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::LookoutMetrics::AnomalyDetector.SubnetIdList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-subnetidlist.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::LookoutMetrics::AnomalyDetector.TimestampColumn](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-timestampcolumn.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::LookoutMetrics::AnomalyDetector.VpcConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-vpcconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

### Complete Removal of ResourceTypes and/or PropertyTypes

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

- [AWS::EC2::LaunchTemplate.TagSpecifications](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-tagspecifications.html)
  - `ap-east-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ca-central-1`
  - `cn-northwest-1`
  - `eu-north-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::AccessAnalyzer::Analyzer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html)
  - Now available to **ALL** regions.

- [AWS::Backup::BackupPlan](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html)
  - Now available to **ALL** regions.

- [AWS::Backup::BackupSelection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html)
  - Now available to **ALL** regions.

- [AWS::Backup::BackupVault](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html)
  - Now available to **ALL** regions.

- [AWS::CloudFront::CloudFrontOriginAccessIdentity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html)
  - `cn-north-1`

- [AWS::EFS::AccessPoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::Component](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::ContainerRecipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::DistributionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::Image](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::ImagePipeline](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::ImageRecipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::InfrastructureConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::StepFunctions::Activity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html)
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `cn-north-1`
  - `af-south-1`
  - `eu-north-1`
  - `eu-west-2`
  - `ap-south-1`
  - `cn-northwest-1`
  - `sa-east-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ap-southeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `me-south-1`
  - `eu-west-3`
  - `ca-central-1`
  - `ap-southeast-1`

- [AWS::AccessAnalyzer::Analyzer.ArchiveRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html)
  - Now available to **ALL** regions.

- [AWS::AccessAnalyzer::Analyzer.Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html)
  - Now available to **ALL** regions.

- [AWS::Backup::BackupPlan.AdvancedBackupSettingResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-advancedbackupsettingresourcetype.html)
  - Now available to **ALL** regions.

- [AWS::Backup::BackupPlan.BackupPlanResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html)
  - Now available to **ALL** regions.

- [AWS::Backup::BackupPlan.BackupRuleResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html)
  - Now available to **ALL** regions.

- [AWS::Backup::BackupPlan.CopyActionResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html)
  - Now available to **ALL** regions.

- [AWS::Backup::BackupPlan.LifecycleResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-lifecycleresourcetype.html)
  - Now available to **ALL** regions.

- [AWS::Backup::BackupSelection.BackupSelectionResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html)
  - Now available to **ALL** regions.

- [AWS::Backup::BackupSelection.ConditionResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html)
  - Now available to **ALL** regions.

- [AWS::Backup::BackupVault.NotificationObjectType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-notificationobjecttype.html)
  - Now available to **ALL** regions.

- [AWS::CloudFront::CloudFrontOriginAccessIdentity.CloudFrontOriginAccessIdentityConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cloudfrontoriginaccessidentity-cloudfrontoriginaccessidentityconfig.html)
  - `cn-north-1`

- [AWS::EFS::AccessPoint.AccessPointTag](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-accesspointtag.html)
  - Now available to **ALL** regions.

- [AWS::EFS::AccessPoint.CreationInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-creationinfo.html)
  - Now available to **ALL** regions.

- [AWS::EFS::AccessPoint.PosixUser](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-posixuser.html)
  - Now available to **ALL** regions.

- [AWS::EFS::AccessPoint.RootDirectory](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-rootdirectory.html)
  - Now available to **ALL** regions.

- [AWS::EFS::FileSystem.BackupPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-backuppolicy.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::ContainerRecipe.ComponentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::ContainerRecipe.TargetContainerRepository](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-targetcontainerrepository.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::DistributionConfiguration.Distribution](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::Image.ImageTestsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagetestsconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::ImagePipeline.ImageTestsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::ImagePipeline.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::ImageRecipe.ComponentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::ImageRecipe.EbsInstanceBlockDeviceSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::ImageRecipe.InstanceBlockDeviceMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::InfrastructureConfiguration.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-logging.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::InfrastructureConfiguration.S3Logs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html)
  - Now available to **ALL** regions.

- [AWS::MediaLive::Channel.ArchiveCdnSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecdnsettings.html)
  - `us-east-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `us-west-2`

- [AWS::MediaLive::Channel.ArchiveS3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archives3settings.html)
  - `us-east-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `us-west-2`

- [AWS::MediaLive::Channel.CaptionRectangle](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionrectangle.html)
  - `us-east-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `us-west-2`

- [AWS::MediaLive::Channel.FrameCaptureCdnSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturecdnsettings.html)
  - `us-east-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `us-west-2`

- [AWS::MediaLive::Channel.FrameCaptureHlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturehlssettings.html)
  - `us-east-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `us-west-2`

- [AWS::MediaLive::Channel.FrameCaptureS3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptures3settings.html)
  - `us-east-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `us-west-2`

- [AWS::MediaLive::Channel.HlsS3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlss3settings.html)
  - `us-east-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `us-west-2`

- [AWS::StepFunctions::Activity.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html)
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `cn-north-1`
  - `af-south-1`
  - `eu-north-1`
  - `eu-west-2`
  - `ap-south-1`
  - `cn-northwest-1`
  - `sa-east-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ap-southeast-2`
  - `ap-east-1`
  - `eu-south-1`
  - `me-south-1`
  - `eu-west-3`
  - `ca-central-1`
  - `ap-southeast-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v31.1.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

- PropertyType Still Missing
  - Since v31.1.0: [AWS::GroundStation::Config.AntennaDownlinkConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::Config.AntennaDownlinkDemodDecodeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::Config.AntennaUplinkConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::Config.ConfigData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::Config.DataflowEndpointConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-dataflowendpointconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::Config.DecodeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-decodeconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::Config.DemodulationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-demodulationconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::Config.Eirp](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-eirp.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::Config.Frequency](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequency.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::Config.FrequencyBandwidth](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequencybandwidth.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::Config.S3RecordingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::Config.SpectrumConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::Config.TrackingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-trackingconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::Config.UplinkEchoConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkechoconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::Config.UplinkSpectrumConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkspectrumconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.1.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v31.1.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
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

## [31.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v31.1.0) (2021-03-19)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v31-changelog.json)
  - Change source is a diff between [v31.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v31.1.0) and [v31.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v31.0.0)

### Totals

- TotalPropertyTypes: 2266 **(+17)**
- TotalPropertyTypesSupportedGlobally: 548 **(+0)**
- TotalResourceTypes: 718 **(+3)**
- TotalResourceTypesSupportedGlobally: 199 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::FIS::ExperimentTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::S3ObjectLambda::AccessPoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::S3ObjectLambda::AccessPointPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::FIS::ExperimentTemplate.ExperimentTemplateAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::FIS::ExperimentTemplate.ExperimentTemplateActionItemParameterMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateactionitemparametermap.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::FIS::ExperimentTemplate.ExperimentTemplateActionItemStartAfterList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateactionitemstartafterlist.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::FIS::ExperimentTemplate.ExperimentTemplateActionItemTargetMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateactionitemtargetmap.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::FIS::ExperimentTemplate.ExperimentTemplateStopCondition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatestopcondition.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::FIS::ExperimentTemplate.ExperimentTemplateTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::FIS::ExperimentTemplate.ExperimentTemplateTargetFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::FIS::ExperimentTemplate.ExperimentTemplateTargetFilterList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetargetfilterlist.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::FIS::ExperimentTemplate.ExperimentTemplateTargetFilterValues](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetargetfiltervalues.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::FIS::ExperimentTemplate.ResourceArnList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-resourcearnlist.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::FIS::ExperimentTemplate.TagMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-tagmap.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::MediaLive::Channel.ArchiveCdnSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecdnsettings.html)
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`

- [AWS::MediaLive::Channel.ArchiveS3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archives3settings.html)
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`

- [AWS::MediaLive::Channel.CaptionRectangle](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionrectangle.html)
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`

- [AWS::MediaLive::Channel.FrameCaptureCdnSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturecdnsettings.html)
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`

- [AWS::MediaLive::Channel.FrameCaptureHlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturehlssettings.html)
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`

- [AWS::MediaLive::Channel.FrameCaptureS3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptures3settings.html)
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`

- [AWS::MediaLive::Channel.HlsS3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlss3settings.html)
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`

- [AWS::S3ObjectLambda::AccessPoint.ObjectLambdaConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::S3ObjectLambda::AccessPoint.TransformationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-transformationconfiguration.html)
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
  - `us-west-1`
  - `us-west-2`

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::CloudFront::Distribution.LegacyCustomOrigin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html)
  - `eu-central-1`

- [AWS::CloudFront::Distribution.LegacyS3Origin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacys3origin.html)
  - `eu-central-1`

- [AWS::ServiceCatalogAppRegistry::AttributeGroup.Attributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalogappregistry-attributegroup-attributes.html)
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

- [AWS::Batch::ComputeEnvironment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html)
  - `af-south-1`

- [AWS::Batch::JobQueue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html)
  - `af-south-1`

- [AWS::CodeBuild::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::ReportGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::SourceCredential](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::DataBrew::Dataset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html)
  - `sa-east-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::DataBrew::Job](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html)
  - `sa-east-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::DataBrew::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html)
  - `sa-east-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::DataBrew::Recipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html)
  - `sa-east-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::DataBrew::Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html)
  - `sa-east-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::GlobalAccelerator::Accelerator](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html)
  - `ap-northeast-3`

- [AWS::GlobalAccelerator::EndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html)
  - `ap-northeast-3`

- [AWS::GlobalAccelerator::Listener](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html)
  - `ap-northeast-3`

- [AWS::GreengrassV2::ComponentVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrassv2-componentversion.html)
  - `cn-north-1`

- [AWS::NetworkFirewall::Firewall](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::FirewallPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::SSM::ResourceDataSync](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html)
  - `eu-north-1`

- [AWS::Batch::ComputeEnvironment.ComputeResources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html)
  - `af-south-1`

- [AWS::Batch::ComputeEnvironment.Ec2ConfigurationObject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-ec2configurationobject.html)
  - `af-south-1`

- [AWS::Batch::ComputeEnvironment.LaunchTemplateSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition.ContainerProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition.Device](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-device.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-environment.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition.EvaluateOnExit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-evaluateonexit.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition.FargatePlatformConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-fargateplatformconfiguration.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition.LinuxParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-linuxparameters.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition.LogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition.MountPoints](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-mountpoints.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition.NetworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-networkconfiguration.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition.NodeProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-nodeproperties.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition.NodeRangeProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-noderangeproperty.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition.ResourceRequirement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-resourcerequirement.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition.RetryStrategy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-retrystrategy.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition.Secret](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-secret.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition.Timeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-timeout.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition.Tmpfs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-tmpfs.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition.Ulimit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ulimit.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition.Volumes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumes.html)
  - `af-south-1`

- [AWS::Batch::JobDefinition.VolumesHost](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumeshost.html)
  - `af-south-1`

- [AWS::Batch::JobQueue.ComputeEnvironmentOrder](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobqueue-computeenvironmentorder.html)
  - `af-south-1`

- [AWS::CodeBuild::Project.Artifacts](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.BatchRestrictions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-batchrestrictions.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.BuildStatusConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-buildstatusconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.CloudWatchLogsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-cloudwatchlogsconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.EnvironmentVariable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environmentvariable.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.FilterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-filtergroup.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.GitSubmodulesConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-gitsubmodulesconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.LogsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-logsconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.ProjectBuildBatchConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.ProjectCache](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectcache.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.ProjectFileSystemLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.ProjectSourceVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectsourceversion.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.ProjectTriggers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projecttriggers.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.RegistryCredential](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-registrycredential.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.S3LogsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-s3logsconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.Source](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.SourceAuth](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-sourceauth.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-vpcconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.WebhookFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-webhookfilter.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::ReportGroup.ReportExportConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-reportexportconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::ReportGroup.S3ReportExportConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::DataBrew::Job.CsvOutputOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-csvoutputoptions.html)
  - `sa-east-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::DataBrew::Job.Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html)
  - `sa-east-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::DataBrew::Job.OutputFormatOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputformatoptions.html)
  - `sa-east-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::DataBrew::Job.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3location.html)
  - `sa-east-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::DataBrew::Recipe.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-action.html)
  - `sa-east-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::DataBrew::Recipe.ConditionExpression](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-conditionexpression.html)
  - `sa-east-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::DataBrew::Recipe.DataCatalogInputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-datacataloginputdefinition.html)
  - `sa-east-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::DataBrew::Recipe.RecipeParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html)
  - `sa-east-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::DataBrew::Recipe.RecipeStep](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipestep.html)
  - `sa-east-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::DataBrew::Recipe.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-s3location.html)
  - `sa-east-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::DataBrew::Recipe.SecondaryInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-secondaryinput.html)
  - `sa-east-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::ECS::Cluster.ClusterConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clusterconfiguration.html)
  - `eu-south-1`
  - `ap-east-1`
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::ECS::Cluster.ExecuteCommandConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandconfiguration.html)
  - `eu-south-1`
  - `ap-east-1`
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::ECS::Cluster.ExecuteCommandLogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html)
  - `eu-south-1`
  - `ap-east-1`
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::GlobalAccelerator::EndpointGroup.EndpointConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-endpointconfiguration.html)
  - `ap-northeast-3`

- [AWS::GlobalAccelerator::EndpointGroup.PortOverride](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-portoverride.html)
  - `ap-northeast-3`

- [AWS::GlobalAccelerator::Listener.PortRange](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-listener-portrange.html)
  - `ap-northeast-3`

- [AWS::GreengrassV2::ComponentVersion.ComponentDependencyRequirement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentdependencyrequirement.html)
  - `cn-north-1`

- [AWS::GreengrassV2::ComponentVersion.ComponentPlatform](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-componentplatform.html)
  - `cn-north-1`

- [AWS::GreengrassV2::ComponentVersion.LambdaContainerParams](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdacontainerparams.html)
  - `cn-north-1`

- [AWS::GreengrassV2::ComponentVersion.LambdaDeviceMount](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdadevicemount.html)
  - `cn-north-1`

- [AWS::GreengrassV2::ComponentVersion.LambdaEventSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaeventsource.html)
  - `cn-north-1`

- [AWS::GreengrassV2::ComponentVersion.LambdaExecutionParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdaexecutionparameters.html)
  - `cn-north-1`

- [AWS::GreengrassV2::ComponentVersion.LambdaFunctionRecipeSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdafunctionrecipesource.html)
  - `cn-north-1`

- [AWS::GreengrassV2::ComponentVersion.LambdaLinuxProcessParams](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdalinuxprocessparams.html)
  - `cn-north-1`

- [AWS::GreengrassV2::ComponentVersion.LambdaVolumeMount](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrassv2-componentversion-lambdavolumemount.html)
  - `cn-north-1`

- [AWS::NetworkFirewall::Firewall.SubnetMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewall-subnetmapping.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::FirewallPolicy.ActionDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-actiondefinition.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::FirewallPolicy.CustomAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customaction.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::FirewallPolicy.Dimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-dimension.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::FirewallPolicy.FirewallPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::FirewallPolicy.PublishMetricAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-publishmetricaction.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::FirewallPolicy.StatefulRuleGroupReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::FirewallPolicy.StatelessRuleGroupReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::LoggingConfiguration.LogDestinationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::LoggingConfiguration.LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-loggingconfiguration.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.ActionDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-actiondefinition.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.Address](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-address.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.CustomAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customaction.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.Dimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-dimension.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.Header](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.IPSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipset.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.MatchAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.PortRange](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portrange.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.PortSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portset.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.PublishMetricAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-publishmetricaction.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.RuleDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruledefinition.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.RuleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.RuleOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoption.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.RuleVariables](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulevariables.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.RulesSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.RulesSourceList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.StatefulRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.StatelessRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrule.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.StatelessRulesAndCustomActions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::NetworkFirewall::RuleGroup.TCPFlagField](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflagfield.html)
  - `eu-north-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-2`

- [AWS::SSM::ResourceDataSync.AwsOrganizationsSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-awsorganizationssource.html)
  - `eu-north-1`

- [AWS::SSM::ResourceDataSync.S3Destination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html)
  - `eu-north-1`

- [AWS::SSM::ResourceDataSync.SyncSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html)
  - `eu-north-1`

- [AWS::Transfer::Server.Protocol]()
  - `ap-east-1`

- [AWS::Transfer::User.HomeDirectoryMapEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html)
  - `ap-east-1`

- [AWS::Transfer::User.PosixProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html)
  - `ap-east-1`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::EC2::LaunchTemplate.TagSpecifications](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-tagspecifications.html)
  - `ap-southeast-2`
  - `eu-west-1`
  - `us-west-2`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-east-1`
  - `ap-northeast-1`
  - `ap-south-1`
  - `cn-north-1`
  - `sa-east-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v31.0.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

- PropertyType Still Missing
  - Since v31.0.0: [AWS::EC2::LaunchTemplate.TagSpecifications](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-tagspecifications.html)
    - `ap-east-1`
    - `ap-northeast-2`
    - `ap-northeast-3`
    - `ca-central-1`
    - `cn-northwest-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `us-east-2`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `us-west-1`

  - Since v31.0.0: [AWS::GroundStation::Config.AntennaDownlinkConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::Config.AntennaDownlinkDemodDecodeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::Config.AntennaUplinkConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::Config.ConfigData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::Config.DataflowEndpointConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-dataflowendpointconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::Config.DecodeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-decodeconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::Config.DemodulationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-demodulationconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::Config.Eirp](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-eirp.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::Config.Frequency](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequency.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::Config.FrequencyBandwidth](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequencybandwidth.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::Config.S3RecordingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::Config.SpectrumConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::Config.TrackingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-trackingconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::Config.UplinkEchoConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkechoconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::Config.UplinkSpectrumConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkspectrumconfig.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v31.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v31.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::MediaLive::Channel.ArchiveCdnSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecdnsettings.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`

  - [AWS::MediaLive::Channel.ArchiveS3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archives3settings.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`

  - [AWS::MediaLive::Channel.CaptionRectangle](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionrectangle.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`

  - [AWS::MediaLive::Channel.FrameCaptureCdnSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturecdnsettings.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`

  - [AWS::MediaLive::Channel.FrameCaptureHlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturehlssettings.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`

  - [AWS::MediaLive::Channel.FrameCaptureS3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptures3settings.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`

  - [AWS::MediaLive::Channel.HlsS3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlss3settings.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`

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

