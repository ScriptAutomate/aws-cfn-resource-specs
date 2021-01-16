# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v24-changelog.json`](changelogs/v24-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [24.0.0](#2400-2021-01-16)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [24.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v24.0.0) (2021-01-16)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v24-changelog.json)
  - Change source is a diff between [v24.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v24.0.0) and [v23.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v23.0.0)

### Totals

- TotalPropertyTypes: 2144 **(+36)**
- TotalPropertyTypesSupportedGlobally: 523 **(+0)**
- TotalResourceTypes: 670 **(+9)**
- TotalResourceTypesSupportedGlobally: 192 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::EMRContainers::VirtualCluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::QuickSight::Analysis](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Dashboard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Template](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Theme](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::ServiceCatalogAppRegistry::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-application.html)
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

- [AWS::ServiceCatalogAppRegistry::AttributeGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-attributegroup.html)
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

- [AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-attributegroupassociation.html)
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

- [AWS::ServiceCatalogAppRegistry::ResourceAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-resourceassociation.html)
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

- [AWS::EMRContainers::VirtualCluster.ContainerInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerinfo.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::EMRContainers::VirtualCluster.ContainerProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::EMRContainers::VirtualCluster.EksInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-eksinfo.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.ExcludeMimeTypesList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-excludemimetypeslist.html)
  - `ap-southeast-2`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.ExcludeSharedDrivesList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-excludeshareddriveslist.html)
  - `ap-southeast-2`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.ExcludeUserAccountsList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-excludeuseraccountslist.html)
  - `ap-southeast-2`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.GoogleDriveConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html)
  - `ap-southeast-2`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::QuickSight::Analysis.AnalysisError](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysiserror.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Analysis.AnalysisSourceEntity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourceentity.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Analysis.AnalysisSourceTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-analysissourcetemplate.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Analysis.DataSetReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datasetreference.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Analysis.DateTimeParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-datetimeparameter.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Analysis.DecimalParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-decimalparameter.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Analysis.IntegerParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-integerparameter.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Analysis.Parameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-parameters.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Analysis.ResourcePermission](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-resourcepermission.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Analysis.Sheet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-sheet.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Analysis.StringParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-analysis-stringparameter.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Dashboard.AdHocFilteringOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-adhocfilteringoption.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Dashboard.DashboardError](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboarderror.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Dashboard.DashboardPublishOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardpublishoptions.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Dashboard.DashboardSourceEntity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourceentity.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Dashboard.DashboardSourceTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardsourcetemplate.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Dashboard.DashboardVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-dashboardversion.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Dashboard.DataSetReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datasetreference.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Dashboard.DateTimeParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-datetimeparameter.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Dashboard.DecimalParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-decimalparameter.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Dashboard.ExportToCSVOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-exporttocsvoption.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Dashboard.IntegerParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-integerparameter.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Dashboard.Parameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-parameters.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Dashboard.ResourcePermission](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-resourcepermission.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Dashboard.Sheet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-sheet.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Dashboard.SheetControlsOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-sheetcontrolsoption.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Dashboard.StringParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dashboard-stringparameter.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Template.ColumnGroupColumnSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-columngroupcolumnschema.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Template.ColumnGroupSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-columngroupschema.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Template.ColumnSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-columnschema.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Template.DataSetConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetconfiguration.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Template.DataSetReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetreference.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Template.DataSetSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-datasetschema.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Template.ResourcePermission](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-resourcepermission.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Template.Sheet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-sheet.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Template.TemplateError](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templateerror.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Template.TemplateSourceAnalysis](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceanalysis.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Template.TemplateSourceEntity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourceentity.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Template.TemplateSourceTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templatesourcetemplate.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Template.TemplateVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-template-templateversion.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Theme.BorderStyle](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-borderstyle.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Theme.DataColorPalette](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-datacolorpalette.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Theme.Font](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-font.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Theme.GutterStyle](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-gutterstyle.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Theme.MarginStyle](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-marginstyle.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Theme.ResourcePermission](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-resourcepermission.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Theme.SheetStyle](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-sheetstyle.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Theme.ThemeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeconfiguration.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Theme.ThemeError](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeerror.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Theme.ThemeVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-themeversion.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Theme.TileLayoutStyle](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilelayoutstyle.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Theme.TileStyle](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-tilestyle.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Theme.Typography](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-typography.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::QuickSight::Theme.UIColorPalette](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-theme-uicolorpalette.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-2`

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

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::ElastiCache::User.Authentication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-user-authentication.html)
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

- [AWS::ElastiCache::UserGroup.UserGroupPendingChanges](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-usergroup-usergrouppendingchanges.html)
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

- [AWS::LicenseManager::Grant.Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-grant-filter.html)
  - `ap-southeast-2`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`

- [AWS::LicenseManager::Grant.StringList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-grant-stringlist.html)
  - `ap-southeast-2`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`

- [AWS::LicenseManager::License.Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-filter.html)
  - `ap-southeast-2`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`

- [AWS::LicenseManager::License.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-rule.html)
  - `ap-southeast-2`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`

- [AWS::LicenseManager::License.RuleList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-rulelist.html)
  - `ap-southeast-2`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`

- [AWS::LicenseManager::License.StringList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-stringlist.html)
  - `ap-southeast-2`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`

- [AWS::NetworkFirewall::FirewallPolicy.CustomActions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customactions.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.Dimensions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-dimensions.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.StatefulRuleGroupReferences](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreferences.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.StatelessActions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessactions.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.StatelessRuleGroupReferences](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreferences.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::LoggingConfiguration.LogDestinationConfigs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfigs.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.Addresses](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-addresses.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.CustomActions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customactions.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.Dimensions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-dimensions.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.Flags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-flags.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.PortRanges](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portranges.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.ProtocolNumbers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-protocolnumbers.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.RuleOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoptions.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.StatefulRules](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrules.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.StatelessRules](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrules.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.TCPFlags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflags.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.TargetTypes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-targettypes.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.VariableDefinitionList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-variabledefinitionlist.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::EC2::CarrierGateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-carriergateway.html)
  - `ap-northeast-1`

- [AWS::FSx::FileSystem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html)
  - `cn-north-1`
  - `ap-south-1`
  - `cn-northwest-1`
  - `us-gov-west-1`
  - `us-gov-east-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-west-3`
  - `sa-east-1`

- [AWS::Glue::DataCatalogEncryptionSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-datacatalogencryptionsettings.html)
  - `us-gov-west-1`

- [AWS::NetworkFirewall::Firewall](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::FirewallPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html)
  - `ap-southeast-2`

- [AWS::ACMPCA::Certificate.Validity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-validity.html)
  - `ap-east-1`
  - `me-south-1`
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::ECS::Service.DeploymentCircuitBreaker](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentcircuitbreaker.html)
  - `cn-north-1`

- [AWS::FSx::FileSystem.LustreConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html)
  - `cn-north-1`
  - `ap-south-1`
  - `cn-northwest-1`
  - `us-gov-west-1`
  - `us-gov-east-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-west-3`
  - `sa-east-1`

- [AWS::FSx::FileSystem.SelfManagedActiveDirectoryConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html)
  - `cn-north-1`
  - `ap-south-1`
  - `cn-northwest-1`
  - `us-gov-west-1`
  - `us-gov-east-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-west-3`
  - `sa-east-1`

- [AWS::FSx::FileSystem.WindowsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html)
  - `cn-north-1`
  - `ap-south-1`
  - `cn-northwest-1`
  - `us-gov-west-1`
  - `us-gov-east-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-west-3`
  - `sa-east-1`

- [AWS::Glue::DataCatalogEncryptionSettings.ConnectionPasswordEncryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-connectionpasswordencryption.html)
  - `us-gov-west-1`

- [AWS::Glue::DataCatalogEncryptionSettings.DataCatalogEncryptionSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-datacatalogencryptionsettings.html)
  - `us-gov-west-1`

- [AWS::Glue::DataCatalogEncryptionSettings.EncryptionAtRest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-encryptionatrest.html)
  - `us-gov-west-1`

- [AWS::IoTAnalytics::Datastore.Column](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-column.html)
  - `eu-west-1`
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`

- [AWS::IoTAnalytics::Datastore.FileFormatConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-fileformatconfiguration.html)
  - `eu-west-1`
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`

- [AWS::IoTAnalytics::Datastore.JsonConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-jsonconfiguration.html)
  - `eu-west-1`
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`

- [AWS::IoTAnalytics::Datastore.ParquetConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-parquetconfiguration.html)
  - `eu-west-1`
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`

- [AWS::IoTAnalytics::Datastore.SchemaDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-schemadefinition.html)
  - `eu-west-1`
  - `us-west-2`
  - `ap-northeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`

- [AWS::NetworkFirewall::Firewall.SubnetMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewall-subnetmapping.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::FirewallPolicy.ActionDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-actiondefinition.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::FirewallPolicy.CustomAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customaction.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::FirewallPolicy.Dimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-dimension.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::FirewallPolicy.FirewallPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::FirewallPolicy.PublishMetricAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-publishmetricaction.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::FirewallPolicy.StatefulRuleGroupReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::FirewallPolicy.StatelessRuleGroupReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::LoggingConfiguration.LogDestinationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::LoggingConfiguration.LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-loggingconfiguration.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.ActionDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-actiondefinition.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.Address](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-address.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.CustomAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customaction.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.Dimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-dimension.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.Header](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.IPSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipset.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.MatchAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.PortRange](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portrange.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.PortSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portset.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.PublishMetricAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-publishmetricaction.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.RuleDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruledefinition.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.RuleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.RuleOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoption.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.RuleVariables](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulevariables.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.RulesSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.RulesSourceList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.StatefulRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.StatelessRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrule.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.StatelessRulesAndCustomActions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.TCPFlagField](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflagfield.html)
  - `ap-southeast-2`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v23.0.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v23.0.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v23.0.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

- PropertyType Still Missing
  - Since v23.0.0: [AWS::AuditManager::Assessment.AWSAccounts](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsaccounts.html)
    - `ap-northeast-1`

  - Since v23.0.0: [AWS::AuditManager::Assessment.AWSServices](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsservices.html)
    - `ap-northeast-1`

  - Since v23.0.0: [AWS::ECS::Cluster.ClusterSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersetting.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `eu-south-1`

  - Since v23.0.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v23.0.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v23.0.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v23.0.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v23.0.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v23.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v23.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

