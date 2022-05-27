# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v73-changelog.json`](changelogs/v73-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [73.1.0](#7310-2022-05-27)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [73.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v73.1.0) (2022-05-27)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v73-changelog.json)
  - Change source is a diff between [v73.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v73.1.0) and [v72.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v72.1.0)

### Totals

- TotalPropertyTypes: 3175 **(+11)**
- TotalPropertyTypesSupportedGlobally: 1085 **(+0)**
- TotalResourceTypes: 928 **(+2)**
- TotalResourceTypesSupportedGlobally: 341 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::EMRServerless::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::IoTWireless::NetworkAnalyzerConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-2`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::EMRServerless::Application.AutoStartConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-autostartconfiguration.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::EMRServerless::Application.AutoStopConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-autostopconfiguration.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::EMRServerless::Application.InitialCapacityConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfig.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::EMRServerless::Application.InitialCapacityConfigKeyValuePair](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfigkeyvaluepair.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::EMRServerless::Application.MaximumAllowedResources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-maximumallowedresources.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::EMRServerless::Application.NetworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-networkconfiguration.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::EMRServerless::Application.WorkerConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workerconfiguration.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::ImageBuilder::DistributionConfiguration.FastLaunchConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html)
  - `cn-north-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::ImageBuilder::DistributionConfiguration.FastLaunchLaunchTemplateSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification.html)
  - `cn-north-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::ImageBuilder::DistributionConfiguration.FastLaunchSnapshotConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration.html)
  - `cn-north-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::SageMaker::Domain.RSessionAppSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-rsessionappsettings.html)
  - `cn-north-1`
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::EC2::LocalGatewayRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.html)
  - `eu-south-1`

- [AWS::EC2::LocalGatewayRouteTableVPCAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetablevpcassociation.html)
  - `ap-northeast-3`
  - `eu-south-1`

- [AWS::Redshift::EventSubscription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::SSO::Assignment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html)
  - `ap-northeast-3`

- [AWS::SSO::InstanceAccessControlAttributeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html)
  - `ap-northeast-3`

- [AWS::SSO::PermissionSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelPackage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::Cognito::UserPool.UserAttributeUpdateSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-userattributeupdatesettings.html)
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `ap-south-1`
  - `ap-southeast-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `eu-north-1`
  - `ap-southeast-1`
  - `us-east-1`
  - `us-west-2`
  - `eu-central-1`
  - `us-east-2`
  - `ca-central-1`

- [AWS::Pinpoint::Campaign.CampaignCustomMessage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigncustommessage.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `us-gov-west-1`
  - `ap-northeast-1`
  - `eu-west-2`
  - `us-east-1`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-central-1`
  - `ca-central-1`

- [AWS::Pinpoint::Campaign.CustomDeliveryConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-customdeliveryconfiguration.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `us-gov-west-1`
  - `ap-northeast-1`
  - `eu-west-2`
  - `us-east-1`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-central-1`
  - `ca-central-1`

- [AWS::Pinpoint::Campaign.Template](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-template.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `us-gov-west-1`
  - `ap-northeast-1`
  - `eu-west-2`
  - `us-east-1`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-central-1`
  - `ca-central-1`

- [AWS::Pinpoint::Campaign.TemplateConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-templateconfiguration.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `us-gov-west-1`
  - `ap-northeast-1`
  - `eu-west-2`
  - `us-east-1`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-central-1`
  - `ca-central-1`

- [AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html)
  - `ap-northeast-3`

- [AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttributeValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelPackage.AdditionalInferenceSpecificationDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-additionalinferencespecificationdefinition.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.Bias](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-bias.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.CreatedBy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-createdby.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.DataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-datasource.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.DriftCheckBaselines](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckbaselines.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.DriftCheckBias](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckbias.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.DriftCheckExplainability](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckexplainability.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.DriftCheckModelDataQuality](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckmodeldataquality.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.DriftCheckModelQuality](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckmodelquality.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-environment.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.Explainability](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-explainability.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.FileSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-filesource.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.InferenceSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-inferencespecification.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.LastModifiedBy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-lastmodifiedby.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.MetadataProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-metadataproperties.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.MetricsSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-metricssource.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.ModelDataQuality](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modeldataquality.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.ModelMetrics](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelmetrics.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.ModelPackageContainerDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.ModelPackageStatusDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagestatusdetails.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.ModelPackageStatusItem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagestatusitem.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.ModelQuality](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelquality.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.S3DataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-s3datasource.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.SourceAlgorithm](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-sourcealgorithm.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.SourceAlgorithmSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-sourcealgorithmspecification.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.TransformInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transforminput.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.TransformJobDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformjobdefinition.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.TransformOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformoutput.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.TransformResources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformresources.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.ValidationProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-validationprofile.html)
  - `ap-southeast-2`
  - `cn-north-1`

- [AWS::SageMaker::ModelPackage.ValidationSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-validationspecification.html)
  - `ap-southeast-2`
  - `cn-north-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v72.1.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v72.1.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v72.1.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v72.1.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v72.1.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v72.1.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- PropertyType Still Missing
  - Since v72.1.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v72.1.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v72.1.0: [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v72.1.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v72.1.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::ImageBuilder::DistributionConfiguration.FastLaunchConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html)
    - `cn-north-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::ImageBuilder::DistributionConfiguration.FastLaunchLaunchTemplateSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification.html)
    - `cn-north-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::ImageBuilder::DistributionConfiguration.FastLaunchSnapshotConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration.html)
    - `cn-north-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::SageMaker::Domain.RSessionAppSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-rsessionappsettings.html)
    - `cn-north-1`
    - `eu-central-1`

