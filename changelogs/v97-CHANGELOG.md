# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v97-changelog.json`](changelogs/v97-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [97.0.0](#9700-2022-11-13)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [97.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v97.0.0) (2022-11-13)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v97-changelog.json)
  - Change source is a diff between [v97.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v97.0.0) and [v95.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v95.0.0)

### Totals

- TotalPropertyTypes: 3443 **(+54)**
- TotalPropertyTypesSupportedGlobally: 1180 **(+15)**
- TotalResourceTypes: 985 **(+13)**
- TotalResourceTypesSupportedGlobally: 358 **(+2)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::AmplifyUIBuilder::Form](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::AppRunner::VpcIngressConnection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Organizations::Account](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-account.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Organizations::OrganizationalUnit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organizationalunit.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::Organizations::Policy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-policy.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::ResourceExplorer2::DefaultViewAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-defaultviewassociation.html)
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

- [AWS::ResourceExplorer2::Index](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-index.html)
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

- [AWS::ResourceExplorer2::View](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourceexplorer2-view.html)
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

- [AWS::SES::VdmAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-vdmattributes.html)
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

- [AWS::Scheduler::Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Scheduler::ScheduleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedulegroup.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::SupportApp::SlackWorkspaceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackworkspaceconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::XRay::ResourcePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-resourcepolicy.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::AmplifyUIBuilder::Form.FieldConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Form.FieldInputConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Form.FieldPosition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldposition.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Form.FieldValidationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Form.FormButton](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formbutton.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Form.FormCTA](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formcta.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Form.FormDataTypeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formdatatypeconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Form.FormInputValueProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-forminputvalueproperty.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Form.FormStyle](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyle.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Form.FormStyleConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyleconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Form.SectionalElement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-sectionalelement.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Form.ValueMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-valuemapping.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Form.ValueMappings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-valuemappings.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::AppRunner::Service.IngressConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-ingressconfiguration.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::AppRunner::VpcIngressConnection.IngressVpcConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-vpcingressconnection-ingressvpcconfiguration.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::AppStream::DirectoryConfig.CertificateBasedAuthProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-directoryconfig-certificatebasedauthproperties.html)
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
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::Batch::ComputeEnvironment.EksConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-eksconfiguration.html)
  - `ap-northeast-1`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Batch::JobDefinition.EksContainer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer.html)
  - Available in **ALL** regions.

- [AWS::Batch::JobDefinition.EksContainerEnvironmentVariable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainerenvironmentvariable.html)
  - Available in **ALL** regions.

- [AWS::Batch::JobDefinition.EksContainerVolumeMount](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainervolumemount.html)
  - Available in **ALL** regions.

- [AWS::Batch::JobDefinition.EksProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksproperties.html)
  - Available in **ALL** regions.

- [AWS::Batch::JobDefinition.EksVolume](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksvolume.html)
  - Available in **ALL** regions.

- [AWS::Batch::JobDefinition.EmptyDir](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksvolume-emptydir.html)
  - Available in **ALL** regions.

- [AWS::Batch::JobDefinition.HostPath](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-eksvolume-hostpath.html)
  - Available in **ALL** regions.

- [AWS::Batch::JobDefinition.PodProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-podproperties.html)
  - Available in **ALL** regions.

- [AWS::Batch::JobDefinition.Resources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer-resources.html)
  - Available in **ALL** regions.

- [AWS::Batch::JobDefinition.SecurityContext](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ekscontainer-securitycontext.html)
  - Available in **ALL** regions.

- [AWS::EC2::LaunchTemplate.NetworkBandwidthGbps](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkbandwidthgbps.html)
  - Available in **ALL** regions.

- [AWS::EKS::Cluster.ControlPlanePlacement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-controlplaneplacement.html)
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

- [AWS::MediaPackage::PackagingConfiguration.EncryptionContractConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-encryptioncontractconfiguration.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
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

- [AWS::Panorama::Package.StorageLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-package-storagelocation.html)
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`

- [AWS::ResourceExplorer2::View.Filters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourceexplorer2-view-filters.html)
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

- [AWS::ResourceExplorer2::View.IncludedProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourceexplorer2-view-includedproperty.html)
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

- [AWS::SES::ConfigurationSet.DashboardOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-dashboardoptions.html)
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

- [AWS::SES::ConfigurationSet.GuardianOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-guardianoptions.html)
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

- [AWS::SES::ConfigurationSet.VdmOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-vdmoptions.html)
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

- [AWS::SES::VdmAttributes.DashboardAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-vdmattributes-dashboardattributes.html)
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

- [AWS::SES::VdmAttributes.GuardianAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-vdmattributes-guardianattributes.html)
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

- [AWS::Scheduler::Schedule.AwsVpcConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-awsvpcconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Scheduler::Schedule.CapacityProviderStrategyItem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-capacityproviderstrategyitem.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Scheduler::Schedule.DeadLetterConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-deadletterconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Scheduler::Schedule.EcsParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Scheduler::Schedule.EventBridgeParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-eventbridgeparameters.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Scheduler::Schedule.FlexibleTimeWindow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-flexibletimewindow.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Scheduler::Schedule.KinesisParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-kinesisparameters.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Scheduler::Schedule.NetworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-networkconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Scheduler::Schedule.PlacementConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementconstraint.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Scheduler::Schedule.PlacementStrategy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementstrategy.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Scheduler::Schedule.RetryPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-retrypolicy.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Scheduler::Schedule.SageMakerPipelineParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameter.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Scheduler::Schedule.SageMakerPipelineParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameters.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Scheduler::Schedule.SqsParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sqsparameters.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Scheduler::Schedule.TagMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-tagmap.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Scheduler::Schedule.Target](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::CloudTrail::EventDataStore](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html)
  - `ap-east-1`
  - `ap-northeast-3`
  - `me-south-1`

- [AWS::EC2::CarrierGateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-carriergateway.html)
  - `eu-west-1`

- [AWS::MSK::ServerlessCluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html)
  - `ap-south-1`
  - `ca-central-1`

- [AWS::S3ObjectLambda::AccessPoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html)
  - Now available to **ALL** regions.

- [AWS::S3ObjectLambda::AccessPointPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspointpolicy.html)
  - Now available to **ALL** regions.

- [AWS::VoiceID::Domain](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-voiceid-domain.html)
  - `af-south-1`
  - `ca-central-1`

- [AWS::CloudTrail::EventDataStore.AdvancedEventSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedeventselector.html)
  - `ap-east-1`
  - `ap-northeast-3`
  - `me-south-1`

- [AWS::CloudTrail::EventDataStore.AdvancedFieldSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html)
  - `ap-east-1`
  - `ap-northeast-3`
  - `me-south-1`

- [AWS::EC2::EC2Fleet.NetworkBandwidthGbpsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-networkbandwidthgbpsrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::SpotFleet.NetworkBandwidthGbpsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-networkbandwidthgbpsrequest.html)
  - Now available to **ALL** regions.

- [AWS::IoT::TopicRule.LocationAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-locationaction.html)
  - `us-gov-west-1`

- [AWS::IoT::TopicRule.RepublishActionHeaders](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishactionheaders.html)
  - `ap-east-1`
  - `cn-north-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-west-2`
  - `us-west-1`
  - `us-gov-east-1`
  - `ap-northeast-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `cn-northwest-1`
  - `eu-north-1`
  - `me-south-1`
  - `ca-central-1`
  - `us-gov-west-1`
  - `ap-southeast-1`
  - `ap-south-1`
  - `eu-west-3`
  - `us-east-1`
  - `us-east-2`

- [AWS::IoT::TopicRule.Timestamp](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestamp.html)
  - `us-gov-west-1`

- [AWS::IoT::TopicRule.UserProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-userproperty.html)
  - `ap-east-1`
  - `cn-north-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-west-2`
  - `us-west-1`
  - `us-gov-east-1`
  - `ap-northeast-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `cn-northwest-1`
  - `eu-north-1`
  - `me-south-1`
  - `ca-central-1`
  - `us-gov-west-1`
  - `ap-southeast-1`
  - `ap-south-1`
  - `eu-west-3`
  - `us-east-1`
  - `us-east-2`

- [AWS::MSK::ServerlessCluster.ClientAuthentication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-clientauthentication.html)
  - `ap-south-1`
  - `ca-central-1`

- [AWS::MSK::ServerlessCluster.Iam](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-iam.html)
  - `ap-south-1`
  - `ca-central-1`

- [AWS::MSK::ServerlessCluster.Sasl](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-sasl.html)
  - `ap-south-1`
  - `ca-central-1`

- [AWS::MSK::ServerlessCluster.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-vpcconfig.html)
  - `ap-south-1`
  - `ca-central-1`

- [AWS::NetworkFirewall::FirewallPolicy.StatefulRuleGroupOverride](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupoverride.html)
  - `ap-east-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-west-1`
  - `us-gov-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `eu-west-2`
  - `af-south-1`
  - `ap-northeast-3`
  - `eu-north-1`
  - `me-south-1`
  - `ca-central-1`
  - `eu-south-1`
  - `us-gov-west-1`
  - `ap-southeast-1`
  - `ap-south-1`
  - `eu-west-3`
  - `us-east-1`
  - `us-east-2`

- [AWS::S3ObjectLambda::AccessPoint.ObjectLambdaConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-objectlambdaconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::S3ObjectLambda::AccessPoint.TransformationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3objectlambda-accesspoint-transformationconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::VoiceID::Domain.ServerSideEncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-voiceid-domain-serversideencryptionconfiguration.html)
  - `af-south-1`
  - `ca-central-1`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::SES::ContactList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html)
  - `cn-northwest-1`

- [AWS::SES::ContactList.Topic](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html)
  - `cn-northwest-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v95.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v95.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v95.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v95.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v95.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v95.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- New ResourceType(s) Missing
  - [AWS::AmplifyUIBuilder::Form](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html)
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::Organizations::OrganizationalUnit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organizationalunit.html)
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `cn-north-1`
    - `eu-central-1`
    - `us-west-2`

- PropertyType Still Missing
  - Since v95.0.0: [AWS::Config::OrganizationConfigRule.OrganizationCustomPolicyRuleMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html)
    - `me-south-1`

  - Since v95.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v95.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v95.0.0: [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v95.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v95.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::AmplifyUIBuilder::Form.FieldConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldconfig.html)
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::AmplifyUIBuilder::Form.FieldInputConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html)
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::AmplifyUIBuilder::Form.FieldPosition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldposition.html)
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::AmplifyUIBuilder::Form.FieldValidationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration.html)
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::AmplifyUIBuilder::Form.FormButton](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formbutton.html)
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::AmplifyUIBuilder::Form.FormCTA](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formcta.html)
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::AmplifyUIBuilder::Form.FormDataTypeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formdatatypeconfig.html)
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::AmplifyUIBuilder::Form.FormInputValueProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-forminputvalueproperty.html)
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::AmplifyUIBuilder::Form.FormStyle](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyle.html)
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::AmplifyUIBuilder::Form.FormStyleConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyleconfig.html)
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::AmplifyUIBuilder::Form.SectionalElement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-sectionalelement.html)
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::AmplifyUIBuilder::Form.ValueMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-valuemapping.html)
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::AmplifyUIBuilder::Form.ValueMappings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-valuemappings.html)
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::Panorama::Package.StorageLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-package-storagelocation.html)
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `ca-central-1`

