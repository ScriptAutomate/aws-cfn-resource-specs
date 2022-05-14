# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v72-changelog.json`](changelogs/v72-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [72.0.0](#7200-2022-05-14)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [72.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v72.0.0) (2022-05-14)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v72-changelog.json)
  - Change source is a diff between [v72.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v72.0.0) and [v69.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v69.0.0)

### Totals

- TotalPropertyTypes: 3159 **(+32)**
- TotalPropertyTypesSupportedGlobally: 1085 **(+0)**
- TotalResourceTypes: 926 **(+1)**
- TotalResourceTypesSupportedGlobally: 340 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::SageMaker::ModelPackage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html)
  - `eu-central-1`

- [AWS::SSMIncidents::ResponsePlan.DynamicSsmParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-dynamicssmparameter.html)
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::SSMIncidents::ResponsePlan.DynamicSsmParameterValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-dynamicssmparametervalue.html)
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::SageMaker::ModelPackage.AdditionalInferenceSpecificationDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-additionalinferencespecificationdefinition.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.Bias](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-bias.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.CreatedBy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-createdby.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.DataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-datasource.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.DriftCheckBaselines](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckbaselines.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.DriftCheckBias](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckbias.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.DriftCheckExplainability](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckexplainability.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.DriftCheckModelDataQuality](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckmodeldataquality.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.DriftCheckModelQuality](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckmodelquality.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-environment.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.Explainability](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-explainability.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.FileSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-filesource.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.InferenceSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-inferencespecification.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.LastModifiedBy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-lastmodifiedby.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.MetadataProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-metadataproperties.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.MetricsSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-metricssource.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.ModelDataQuality](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modeldataquality.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.ModelMetrics](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelmetrics.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.ModelPackageContainerDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.ModelPackageStatusDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagestatusdetails.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.ModelPackageStatusItem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagestatusitem.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.ModelQuality](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelquality.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.S3DataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-s3datasource.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.SourceAlgorithm](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-sourcealgorithm.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.SourceAlgorithmSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-sourcealgorithmspecification.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.TransformInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transforminput.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.TransformJobDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformjobdefinition.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.TransformOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformoutput.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.TransformResources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformresources.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.ValidationProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-validationprofile.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelPackage.ValidationSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-validationspecification.html)
  - `eu-central-1`

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::MediaTailor::PlaybackConfiguration.DashConfigurationForPut](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-dashconfigurationforput.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `us-east-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::IoT::RoleAlias](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html)
  - `us-east-2`
  - `us-gov-west-1`
  - `cn-northwest-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`
  - `us-east-1`
  - `us-gov-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-southeast-1`
  - `ap-south-1`
  - `ap-northeast-1`
  - `cn-north-1`
  - `me-south-1`
  - `us-west-1`
  - `eu-west-3`
  - `ap-east-1`

- [AWS::NetworkManager::ConnectAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html)
  - `us-east-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `af-south-1`
  - `us-west-1`
  - `eu-central-1`

- [AWS::NetworkManager::ConnectPeer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html)
  - `us-east-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `af-south-1`
  - `us-west-1`
  - `eu-central-1`

- [AWS::NetworkManager::CoreNetwork](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html)
  - `us-east-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `af-south-1`
  - `us-west-1`
  - `eu-central-1`

- [AWS::NetworkManager::SiteToSiteVpnAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html)
  - `us-east-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `af-south-1`
  - `us-west-1`
  - `eu-central-1`

- [AWS::NetworkManager::VpcAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html)
  - `us-east-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `af-south-1`
  - `us-west-1`
  - `eu-central-1`

- [AWS::MediaTailor::PlaybackConfiguration.DashConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-dashconfiguration.html)
  - `us-east-1`
  - `us-west-2`
  - `ap-southeast-2`
  - `ap-northeast-1`
  - `ap-southeast-1`

- [AWS::MediaTailor::PlaybackConfiguration.HlsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediatailor-playbackconfiguration-hlsconfiguration.html)
  - `us-east-1`
  - `us-west-2`
  - `ap-southeast-2`
  - `ap-northeast-1`
  - `ap-southeast-1`

- [AWS::NetworkManager::ConnectAttachment.ConnectAttachmentOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectattachment-connectattachmentoptions.html)
  - `us-east-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `af-south-1`
  - `us-west-1`
  - `eu-central-1`

- [AWS::NetworkManager::ConnectPeer.BgpOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-bgpoptions.html)
  - `us-east-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `af-south-1`
  - `us-west-1`
  - `eu-central-1`

- [AWS::NetworkManager::CoreNetwork.CoreNetworkEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworkedge.html)
  - `us-east-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `af-south-1`
  - `us-west-1`
  - `eu-central-1`

- [AWS::NetworkManager::CoreNetwork.CoreNetworkSegment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworksegment.html)
  - `us-east-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `af-south-1`
  - `us-west-1`
  - `eu-central-1`

- [AWS::NetworkManager::VpcAttachment.VpcOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-vpcoptions.html)
  - `us-east-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `af-south-1`
  - `us-west-1`
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v69.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v69.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v69.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v69.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v69.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v69.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- New ResourceType(s) Missing
  - [AWS::SageMaker::ModelPackage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html)
    - `eu-central-1`

- PropertyType Still Missing
  - Since v69.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v69.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v69.0.0: [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v69.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v69.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::SSMIncidents::ResponsePlan.DynamicSsmParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-dynamicssmparameter.html)
    - `ap-northeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::SSMIncidents::ResponsePlan.DynamicSsmParameterValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-dynamicssmparametervalue.html)
    - `ap-northeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::SageMaker::ModelPackage.AdditionalInferenceSpecificationDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-additionalinferencespecificationdefinition.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.Bias](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-bias.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.CreatedBy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-createdby.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.DataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-datasource.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.DriftCheckBaselines](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckbaselines.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.DriftCheckBias](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckbias.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.DriftCheckExplainability](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckexplainability.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.DriftCheckModelDataQuality](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckmodeldataquality.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.DriftCheckModelQuality](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckmodelquality.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-environment.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.Explainability](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-explainability.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.FileSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-filesource.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.InferenceSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-inferencespecification.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.LastModifiedBy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-lastmodifiedby.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.MetadataProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-metadataproperties.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.MetricsSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-metricssource.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.ModelDataQuality](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modeldataquality.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.ModelMetrics](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelmetrics.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.ModelPackageContainerDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.ModelPackageStatusDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagestatusdetails.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.ModelPackageStatusItem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagestatusitem.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.ModelQuality](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelquality.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.S3DataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-s3datasource.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.SourceAlgorithm](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-sourcealgorithm.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.SourceAlgorithmSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-sourcealgorithmspecification.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.TransformInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transforminput.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.TransformJobDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformjobdefinition.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.TransformOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformoutput.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.TransformResources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformresources.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.ValidationProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-validationprofile.html)
    - `eu-central-1`

  - [AWS::SageMaker::ModelPackage.ValidationSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-validationspecification.html)
    - `eu-central-1`

