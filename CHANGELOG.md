# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v78-changelog.json`](changelogs/v78-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [78.1.0](#7810-2022-07-01)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)
- [78.0.0](#7800-2022-06-24)
  - [Totals](#totals-1)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-1)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-1)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-1)

## [78.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v78.1.0) (2022-07-01)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v78-changelog.json)
  - Change source is a diff between [v78.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v78.1.0) and [v78.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v78.0.0)

### Totals

- TotalPropertyTypes: 3251 **(+25)**
- TotalPropertyTypesSupportedGlobally: 1125 **(+0)**
- TotalResourceTypes: 941 **(+5)**
- TotalResourceTypesSupportedGlobally: 342 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::DataSync::LocationFSxONTAP](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxontap.html)
  - `af-south-1`
  - `ap-northeast-2`
  - `us-east-1`

- [AWS::LakeFormation::DataCellsFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datacellsfilter.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::LakeFormation::TagAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tagassociation.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::SES::DedicatedIpPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-dedicatedippool.html)
  - `af-south-1`
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
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::SES::EmailIdentity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html)
  - `af-south-1`
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
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DataSync::LocationFSxONTAP.NFS](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-nfs.html)
  - `af-south-1`
  - `ap-northeast-2`
  - `us-east-1`

- [AWS::DataSync::LocationFSxONTAP.NfsMountOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-nfsmountoptions.html)
  - `af-south-1`
  - `ap-northeast-2`
  - `us-east-1`

- [AWS::DataSync::LocationFSxONTAP.Protocol](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-protocol.html)
  - `af-south-1`
  - `ap-northeast-2`
  - `us-east-1`

- [AWS::DataSync::LocationFSxONTAP.SMB](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smb.html)
  - `af-south-1`
  - `ap-northeast-2`
  - `us-east-1`

- [AWS::DataSync::LocationFSxONTAP.SmbMountOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smbmountoptions.html)
  - `af-south-1`
  - `ap-northeast-2`
  - `us-east-1`

- [AWS::KinesisAnalyticsV2::Application.ApplicationMaintenanceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationmaintenanceconfiguration.html)
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

- [AWS::KinesisAnalyticsV2::Application.ApplicationRestoreConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationrestoreconfiguration.html)
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

- [AWS::KinesisAnalyticsV2::Application.FlinkRunConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkrunconfiguration.html)
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

- [AWS::KinesisAnalyticsV2::Application.RunConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-runconfiguration.html)
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

- [AWS::KinesisAnalyticsV2::Application.VpcConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-vpcconfiguration.html)
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

- [AWS::LakeFormation::DataCellsFilter.ColumnWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-columnwildcard.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::LakeFormation::DataCellsFilter.RowFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datacellsfilter-rowfilter.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::LakeFormation::TagAssociation.CatalogResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-catalogresource.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::LakeFormation::TagAssociation.DatabaseResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-databaseresource.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::LakeFormation::TagAssociation.LFTagPair](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-lftagpair.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::LakeFormation::TagAssociation.Resource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-resource.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::LakeFormation::TagAssociation.TableResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tableresource.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::LakeFormation::TagAssociation.TableWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewildcard.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::LakeFormation::TagAssociation.TableWithColumnsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-tagassociation-tablewithcolumnsresource.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::Logs::MetricFilter.Dimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-dimension.html)
  - `eu-central-1`

- [AWS::QuickSight::DataSet.DataSetUsageConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-datasetusageconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::RefactorSpaces::Route.DefaultRouteInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-defaultrouteinput.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::SES::EmailIdentity.ConfigurationSetAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-configurationsetattributes.html)
  - `af-south-1`
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
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::SES::EmailIdentity.DkimAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimattributes.html)
  - `af-south-1`
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
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::SES::EmailIdentity.DkimSigningAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html)
  - `af-south-1`
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
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::SES::EmailIdentity.FeedbackAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-feedbackattributes.html)
  - `af-south-1`
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
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::SES::EmailIdentity.MailFromAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-mailfromattributes.html)
  - `af-south-1`
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
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::AppSync::GraphQLApi.AdditionalAuthenticationProviders](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationproviders.html)
  - `ap-east-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-north-1`
  - `cn-northwest-1`
  - `eu-north-1`
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-west-1`

- [AWS::AppSync::GraphQLApi.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-tags.html)
  - `ap-east-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-north-1`
  - `cn-northwest-1`
  - `eu-north-1`
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-west-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::CloudTrail::EventDataStore](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html)
  - `eu-central-1`
  - `ap-southeast-1`
  - `us-west-2`
  - `ap-northeast-1`

- [AWS::IoT::CACertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html)
  - `ap-east-1`
  - `cn-northwest-1`
  - `me-south-1`
  - `ap-northeast-2`

- [AWS::LakeFormation::PrincipalPermissions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `us-west-2`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-east-1`
  - `me-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-west-1`
  - `eu-south-1`
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `ap-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `us-east-2`
  - `sa-east-1`
  - `af-south-1`

- [AWS::LakeFormation::Tag](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `us-west-2`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-east-1`
  - `me-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-west-1`
  - `eu-south-1`
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `ap-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `us-east-2`
  - `sa-east-1`
  - `af-south-1`

- [AWS::AppFlow::ConnectorProfile.ApiKeyCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-apikeycredentials.html)
  - `eu-west-1`
  - `ap-northeast-2`
  - `eu-central-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-west-3`
  - `ap-south-1`
  - `us-west-1`
  - `us-west-2`
  - `us-east-2`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::AppFlow::ConnectorProfile.BasicAuthCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-basicauthcredentials.html)
  - `eu-west-1`
  - `ap-northeast-2`
  - `eu-central-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-west-3`
  - `ap-south-1`
  - `us-west-1`
  - `us-west-2`
  - `us-east-2`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::AppFlow::ConnectorProfile.CredentialsMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-credentialsmap.html)
  - `eu-west-1`
  - `ap-northeast-2`
  - `eu-central-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-west-3`
  - `ap-south-1`
  - `us-west-1`
  - `us-west-2`
  - `us-east-2`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::AppFlow::ConnectorProfile.CustomAuthCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customauthcredentials.html)
  - `eu-west-1`
  - `ap-northeast-2`
  - `eu-central-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-west-3`
  - `ap-south-1`
  - `us-west-1`
  - `us-west-2`
  - `us-east-2`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::AppFlow::ConnectorProfile.CustomConnectorProfileCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofilecredentials.html)
  - `eu-west-1`
  - `ap-northeast-2`
  - `eu-central-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-west-3`
  - `ap-south-1`
  - `us-west-1`
  - `us-west-2`
  - `us-east-2`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::AppFlow::ConnectorProfile.CustomConnectorProfileProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofileproperties.html)
  - `eu-west-1`
  - `ap-northeast-2`
  - `eu-central-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-west-3`
  - `ap-south-1`
  - `us-west-1`
  - `us-west-2`
  - `us-east-2`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::AppFlow::ConnectorProfile.OAuth2Credentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2credentials.html)
  - `eu-west-1`
  - `ap-northeast-2`
  - `eu-central-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-west-3`
  - `ap-south-1`
  - `us-west-1`
  - `us-west-2`
  - `us-east-2`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::AppFlow::ConnectorProfile.OAuth2Properties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2properties.html)
  - `eu-west-1`
  - `ap-northeast-2`
  - `eu-central-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-west-3`
  - `ap-south-1`
  - `us-west-1`
  - `us-west-2`
  - `us-east-2`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::AppFlow::ConnectorProfile.ProfileProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-profileproperties.html)
  - `eu-west-1`
  - `ap-northeast-2`
  - `eu-central-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-west-3`
  - `ap-south-1`
  - `us-west-1`
  - `us-west-2`
  - `us-east-2`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::AppFlow::ConnectorProfile.TokenUrlCustomProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-tokenurlcustomproperties.html)
  - `eu-west-1`
  - `ap-northeast-2`
  - `eu-central-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-west-3`
  - `ap-south-1`
  - `us-west-1`
  - `us-west-2`
  - `us-east-2`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::AppFlow::Flow.CustomConnectorDestinationProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectordestinationproperties.html)
  - `eu-west-1`
  - `ap-northeast-2`
  - `eu-central-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-west-3`
  - `ap-south-1`
  - `us-west-1`
  - `us-west-2`
  - `us-east-2`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::AppFlow::Flow.CustomConnectorSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectorsourceproperties.html)
  - `eu-west-1`
  - `ap-northeast-2`
  - `eu-central-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-west-3`
  - `ap-south-1`
  - `us-west-1`
  - `us-west-2`
  - `us-east-2`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::AppFlow::Flow.CustomProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customproperties.html)
  - `eu-west-1`
  - `ap-northeast-2`
  - `eu-central-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-west-3`
  - `ap-south-1`
  - `us-west-1`
  - `us-west-2`
  - `us-east-2`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-northeast-1`

- [AWS::CloudTrail::EventDataStore.AdvancedEventSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedeventselector.html)
  - `eu-central-1`
  - `ap-southeast-1`
  - `us-west-2`
  - `ap-northeast-1`

- [AWS::CloudTrail::EventDataStore.AdvancedFieldSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html)
  - `eu-central-1`
  - `ap-southeast-1`
  - `us-west-2`
  - `ap-northeast-1`

- [AWS::LakeFormation::PrincipalPermissions.CatalogResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-catalogresource.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `us-west-2`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-east-1`
  - `me-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-west-1`
  - `eu-south-1`
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `ap-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `us-east-2`
  - `sa-east-1`
  - `af-south-1`

- [AWS::LakeFormation::PrincipalPermissions.ColumnWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-columnwildcard.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `us-west-2`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-east-1`
  - `me-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-west-1`
  - `eu-south-1`
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `ap-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `us-east-2`
  - `sa-east-1`
  - `af-south-1`

- [AWS::LakeFormation::PrincipalPermissions.DataCellsFilterResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `us-west-2`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-east-1`
  - `me-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-west-1`
  - `eu-south-1`
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `ap-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `us-east-2`
  - `sa-east-1`
  - `af-south-1`

- [AWS::LakeFormation::PrincipalPermissions.DataLakePrincipal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalakeprincipal.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `us-west-2`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-east-1`
  - `me-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-west-1`
  - `eu-south-1`
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `ap-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `us-east-2`
  - `sa-east-1`
  - `af-south-1`

- [AWS::LakeFormation::PrincipalPermissions.DataLocationResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalocationresource.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `us-west-2`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-east-1`
  - `me-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-west-1`
  - `eu-south-1`
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `ap-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `us-east-2`
  - `sa-east-1`
  - `af-south-1`

- [AWS::LakeFormation::PrincipalPermissions.DatabaseResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-databaseresource.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `us-west-2`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-east-1`
  - `me-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-west-1`
  - `eu-south-1`
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `ap-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `us-east-2`
  - `sa-east-1`
  - `af-south-1`

- [AWS::LakeFormation::PrincipalPermissions.LFTag](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftag.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `us-west-2`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-east-1`
  - `me-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-west-1`
  - `eu-south-1`
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `ap-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `us-east-2`
  - `sa-east-1`
  - `af-south-1`

- [AWS::LakeFormation::PrincipalPermissions.LFTagKeyResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `us-west-2`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-east-1`
  - `me-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-west-1`
  - `eu-south-1`
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `ap-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `us-east-2`
  - `sa-east-1`
  - `af-south-1`

- [AWS::LakeFormation::PrincipalPermissions.LFTagPolicyResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `us-west-2`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-east-1`
  - `me-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-west-1`
  - `eu-south-1`
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `ap-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `us-east-2`
  - `sa-east-1`
  - `af-south-1`

- [AWS::LakeFormation::PrincipalPermissions.Resource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `us-west-2`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-east-1`
  - `me-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-west-1`
  - `eu-south-1`
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `ap-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `us-east-2`
  - `sa-east-1`
  - `af-south-1`

- [AWS::LakeFormation::PrincipalPermissions.TableResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `us-west-2`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-east-1`
  - `me-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-west-1`
  - `eu-south-1`
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `ap-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `us-east-2`
  - `sa-east-1`
  - `af-south-1`

- [AWS::LakeFormation::PrincipalPermissions.TableWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewildcard.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `us-west-2`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-east-1`
  - `me-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-west-1`
  - `eu-south-1`
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `ap-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `us-east-2`
  - `sa-east-1`
  - `af-south-1`

- [AWS::LakeFormation::PrincipalPermissions.TableWithColumnsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `us-west-2`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-east-1`
  - `me-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-west-1`
  - `eu-south-1`
  - `ap-east-1`
  - `eu-west-3`
  - `ca-central-1`
  - `ap-south-1`
  - `eu-north-1`
  - `us-west-1`
  - `us-east-2`
  - `sa-east-1`
  - `af-south-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v78.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v78.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v78.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v78.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v78.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v78.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- PropertyType Still Missing
  - Since v78.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v78.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v78.0.0: [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v78.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v78.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::Logs::MetricFilter.Dimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-dimension.html)
    - `eu-central-1`

## [78.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v78.0.0) (2022-06-24)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v78-changelog.json)
  - Change source is a diff between [v78.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v78.0.0) and [v76.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v76.0.0)

### Totals

- TotalPropertyTypes: 3226 **(+30)**
- TotalPropertyTypesSupportedGlobally: 1125 **(+35)**
- TotalResourceTypes: 936 **(+6)**
- TotalResourceTypesSupportedGlobally: 342 **(+1)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::CloudTrail::EventDataStore](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html)
  - `us-east-1`

- [AWS::ConnectCampaigns::Campaign](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaigns-campaign.html)
  - `ap-southeast-2`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::IoT::CACertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html)
  - `ap-northeast-1`
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
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::LakeFormation::PrincipalPermissions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html)
  - `eu-central-1`

- [AWS::LakeFormation::Tag](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html)
  - `eu-central-1`

- [AWS::RedshiftServerless::Namespace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::AppFlow::ConnectorProfile.ApiKeyCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-apikeycredentials.html)
  - `ap-southeast-2`
  - `us-east-1`

- [AWS::AppFlow::ConnectorProfile.BasicAuthCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-basicauthcredentials.html)
  - `ap-southeast-2`
  - `us-east-1`

- [AWS::AppFlow::ConnectorProfile.CredentialsMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-credentialsmap.html)
  - `ap-southeast-2`
  - `us-east-1`

- [AWS::AppFlow::ConnectorProfile.CustomAuthCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customauthcredentials.html)
  - `ap-southeast-2`
  - `us-east-1`

- [AWS::AppFlow::ConnectorProfile.CustomConnectorProfileCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofilecredentials.html)
  - `ap-southeast-2`
  - `us-east-1`

- [AWS::AppFlow::ConnectorProfile.CustomConnectorProfileProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofileproperties.html)
  - `ap-southeast-2`
  - `us-east-1`

- [AWS::AppFlow::ConnectorProfile.OAuth2Credentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2credentials.html)
  - `ap-southeast-2`
  - `us-east-1`

- [AWS::AppFlow::ConnectorProfile.OAuth2Properties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2properties.html)
  - `ap-southeast-2`
  - `us-east-1`

- [AWS::AppFlow::ConnectorProfile.ProfileProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-profileproperties.html)
  - `ap-southeast-2`
  - `us-east-1`

- [AWS::AppFlow::ConnectorProfile.TokenUrlCustomProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-tokenurlcustomproperties.html)
  - `ap-southeast-2`
  - `us-east-1`

- [AWS::AppFlow::Flow.CustomConnectorDestinationProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectordestinationproperties.html)
  - `ap-southeast-2`
  - `us-east-1`

- [AWS::AppFlow::Flow.CustomConnectorSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectorsourceproperties.html)
  - `ap-southeast-2`
  - `us-east-1`

- [AWS::AppFlow::Flow.CustomProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customproperties.html)
  - `ap-southeast-2`
  - `us-east-1`

- [AWS::CloudTrail::EventDataStore.AdvancedEventSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedeventselector.html)
  - `us-east-1`

- [AWS::CloudTrail::EventDataStore.AdvancedFieldSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html)
  - `us-east-1`

- [AWS::ConnectCampaigns::Campaign.DialerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-dialerconfig.html)
  - `ap-southeast-2`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::ConnectCampaigns::Campaign.OutboundCallConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-outboundcallconfig.html)
  - `ap-southeast-2`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::LakeFormation::PrincipalPermissions.CatalogResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-catalogresource.html)
  - `eu-central-1`

- [AWS::LakeFormation::PrincipalPermissions.ColumnWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-columnwildcard.html)
  - `eu-central-1`

- [AWS::LakeFormation::PrincipalPermissions.DataCellsFilterResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html)
  - `eu-central-1`

- [AWS::LakeFormation::PrincipalPermissions.DataLakePrincipal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalakeprincipal.html)
  - `eu-central-1`

- [AWS::LakeFormation::PrincipalPermissions.DataLocationResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalocationresource.html)
  - `eu-central-1`

- [AWS::LakeFormation::PrincipalPermissions.DatabaseResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-databaseresource.html)
  - `eu-central-1`

- [AWS::LakeFormation::PrincipalPermissions.LFTag](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftag.html)
  - `eu-central-1`

- [AWS::LakeFormation::PrincipalPermissions.LFTagKeyResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html)
  - `eu-central-1`

- [AWS::LakeFormation::PrincipalPermissions.LFTagPolicyResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html)
  - `eu-central-1`

- [AWS::LakeFormation::PrincipalPermissions.Resource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html)
  - `eu-central-1`

- [AWS::LakeFormation::PrincipalPermissions.TableResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html)
  - `eu-central-1`

- [AWS::LakeFormation::PrincipalPermissions.TableWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewildcard.html)
  - `eu-central-1`

- [AWS::LakeFormation::PrincipalPermissions.TableWithColumnsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html)
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::AppStream::AppBlock](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-appblock.html)
  - `us-east-2`

- [AWS::AppStream::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-application.html)
  - `us-east-2`

- [AWS::AppStream::ApplicationEntitlementAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-applicationentitlementassociation.html)
  - `us-east-2`

- [AWS::AppStream::ApplicationFleetAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-applicationfleetassociation.html)
  - `us-east-2`

- [AWS::AppStream::Entitlement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-entitlement.html)
  - `us-east-2`

- [AWS::EC2::CapacityReservation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html)
  - `cn-north-1`

- [AWS::EKS::FargateProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::KinesisAnalyticsV2::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html)
  - Now available to **ALL** regions.

- [AWS::Route53::CidrCollection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-cidrcollection.html)
  - `us-west-2`

- [AWS::SSO::Assignment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html)
  - `eu-south-1`

- [AWS::SSO::InstanceAccessControlAttributeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html)
  - `eu-south-1`

- [AWS::SSO::PermissionSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html)
  - `eu-south-1`

- [AWS::AppStream::AppBlock.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblock-s3location.html)
  - `us-east-2`

- [AWS::AppStream::AppBlock.ScriptDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-appblock-scriptdetails.html)
  - `us-east-2`

- [AWS::AppStream::Application.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-application-s3location.html)
  - `us-east-2`

- [AWS::AppStream::Entitlement.Attribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-entitlement-attribute.html)
  - `us-east-2`

- [AWS::EC2::CapacityReservation.TagSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservation-tagspecification.html)
  - `cn-north-1`

- [AWS::EKS::FargateProfile.Label](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-label.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::EKS::FargateProfile.Selector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-selector.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::EMR::Cluster.AutoTerminationPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-autoterminationpolicy.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.ApplicationCodeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.ApplicationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.ApplicationSnapshotConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.CSVMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.CatalogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-catalogconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.CheckpointConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.CodeContent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.CustomArtifactConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.DeployAsApplicationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.EnvironmentProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-environmentproperties.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.FlinkApplicationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.GlueDataCatalogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-gluedatacatalogconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.InputLambdaProcessor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.InputParallelism](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputparallelism.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.InputProcessingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.InputSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.JSONMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-jsonmappingparameters.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.KinesisFirehoseInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.KinesisStreamsInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisstreamsinput.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.MappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.MavenReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.MonitoringConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.ParallelismConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.PropertyGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.RecordColumn](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.RecordFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.S3ContentBaseLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentbaselocation.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.S3ContentLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.SqlApplicationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-sqlapplicationconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.ZeppelinApplicationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.ZeppelinMonitoringConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinmonitoringconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::Route53::CidrCollection.Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrcollection-location.html)
  - `us-west-2`

- [AWS::Route53::RecordSet.CidrRoutingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrroutingconfig.html)
  - Now available to **ALL** regions.

- [AWS::Route53::RecordSetGroup.CidrRoutingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrroutingconfig.html)
  - Now available to **ALL** regions.

- [AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html)
  - `eu-south-1`

- [AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttributeValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html)
  - `eu-south-1`

- [AWS::SageMaker::EndpointConfig.ClarifyExplainerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyexplainerconfig.html)
  - `us-east-1`
  - `us-west-1`
  - `us-gov-west-1`
  - `cn-northwest-1`
  - `eu-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `us-west-2`
  - `eu-west-1`
  - `us-east-2`
  - `me-south-1`
  - `af-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::SageMaker::EndpointConfig.ClarifyFeatureType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyfeaturetype.html)
  - `us-east-1`
  - `us-west-1`
  - `us-gov-west-1`
  - `cn-northwest-1`
  - `eu-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `us-west-2`
  - `eu-west-1`
  - `us-east-2`
  - `me-south-1`
  - `af-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::SageMaker::EndpointConfig.ClarifyHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyheader.html)
  - `us-east-1`
  - `us-west-1`
  - `us-gov-west-1`
  - `cn-northwest-1`
  - `eu-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `us-west-2`
  - `eu-west-1`
  - `us-east-2`
  - `me-south-1`
  - `af-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::SageMaker::EndpointConfig.ClarifyInferenceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyinferenceconfig.html)
  - `us-east-1`
  - `us-west-1`
  - `us-gov-west-1`
  - `cn-northwest-1`
  - `eu-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `us-west-2`
  - `eu-west-1`
  - `us-east-2`
  - `me-south-1`
  - `af-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::SageMaker::EndpointConfig.ClarifyShapBaselineConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyshapbaselineconfig.html)
  - `us-east-1`
  - `us-west-1`
  - `us-gov-west-1`
  - `cn-northwest-1`
  - `eu-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `us-west-2`
  - `eu-west-1`
  - `us-east-2`
  - `me-south-1`
  - `af-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::SageMaker::EndpointConfig.ClarifyShapConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyshapconfig.html)
  - `us-east-1`
  - `us-west-1`
  - `us-gov-west-1`
  - `cn-northwest-1`
  - `eu-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `us-west-2`
  - `eu-west-1`
  - `us-east-2`
  - `me-south-1`
  - `af-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::SageMaker::EndpointConfig.ClarifyTextConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifytextconfig.html)
  - `us-east-1`
  - `us-west-1`
  - `us-gov-west-1`
  - `cn-northwest-1`
  - `eu-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `us-west-2`
  - `eu-west-1`
  - `us-east-2`
  - `me-south-1`
  - `af-south-1`
  - `ap-northeast-2`
  - `ap-east-1`
  - `ap-southeast-1`
  - `ap-northeast-3`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::AppSync::GraphQLApi.AdditionalAuthenticationProviders](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationproviders.html)
  - `ap-northeast-1`
  - `us-east-1`
  - `us-west-2`
  - `eu-central-1`

- [AWS::AppSync::GraphQLApi.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-tags.html)
  - `ap-northeast-1`
  - `us-east-1`
  - `us-west-2`
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v76.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v76.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v76.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v76.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v76.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v76.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- New ResourceType(s) Missing
  - [AWS::LakeFormation::PrincipalPermissions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-principalpermissions.html)
    - `eu-central-1`

  - [AWS::LakeFormation::Tag](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-tag.html)
    - `eu-central-1`

- PropertyType Still Missing
  - Since v76.0.0: [AWS::AppSync::GraphQLApi.AdditionalAuthenticationProviders](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationproviders.html)
    - `ap-east-1`
    - `ap-northeast-2`
    - `ap-northeast-3`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `ca-central-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-north-1`
    - `eu-south-1`
    - `eu-west-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `sa-east-1`
    - `us-west-1`

  - Since v76.0.0: [AWS::AppSync::GraphQLApi.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-tags.html)
    - `ap-east-1`
    - `ap-northeast-2`
    - `ap-northeast-3`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `ca-central-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-north-1`
    - `eu-south-1`
    - `eu-west-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `sa-east-1`
    - `us-west-1`

  - Since v76.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v76.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v76.0.0: [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v76.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v76.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::LakeFormation::PrincipalPermissions.CatalogResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-catalogresource.html)
    - `eu-central-1`

  - [AWS::LakeFormation::PrincipalPermissions.ColumnWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-columnwildcard.html)
    - `eu-central-1`

  - [AWS::LakeFormation::PrincipalPermissions.DataCellsFilterResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datacellsfilterresource.html)
    - `eu-central-1`

  - [AWS::LakeFormation::PrincipalPermissions.DataLakePrincipal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalakeprincipal.html)
    - `eu-central-1`

  - [AWS::LakeFormation::PrincipalPermissions.DataLocationResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-datalocationresource.html)
    - `eu-central-1`

  - [AWS::LakeFormation::PrincipalPermissions.DatabaseResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-databaseresource.html)
    - `eu-central-1`

  - [AWS::LakeFormation::PrincipalPermissions.LFTag](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftag.html)
    - `eu-central-1`

  - [AWS::LakeFormation::PrincipalPermissions.LFTagKeyResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagkeyresource.html)
    - `eu-central-1`

  - [AWS::LakeFormation::PrincipalPermissions.LFTagPolicyResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-lftagpolicyresource.html)
    - `eu-central-1`

  - [AWS::LakeFormation::PrincipalPermissions.Resource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-resource.html)
    - `eu-central-1`

  - [AWS::LakeFormation::PrincipalPermissions.TableResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tableresource.html)
    - `eu-central-1`

  - [AWS::LakeFormation::PrincipalPermissions.TableWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewildcard.html)
    - `eu-central-1`

  - [AWS::LakeFormation::PrincipalPermissions.TableWithColumnsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-principalpermissions-tablewithcolumnsresource.html)
    - `eu-central-1`

