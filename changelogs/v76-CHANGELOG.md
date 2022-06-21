# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v76-changelog.json`](changelogs/v76-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [76.0.0](#7600-2022-06-21)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [76.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v76.0.0) (2022-06-21)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v76-changelog.json)
  - Change source is a diff between [v76.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v76.0.0) and [v73.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v73.1.0)

### Totals

- TotalPropertyTypes: 3196 **(+21)**
- TotalPropertyTypesSupportedGlobally: 1090 **(+5)**
- TotalResourceTypes: 930 **(+2)**
- TotalResourceTypesSupportedGlobally: 341 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::Connect::TaskTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Route53::CidrCollection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-cidrcollection.html)
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

- [AWS::AppStream::Stack.StreamingExperienceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-streamingexperiencesettings.html)
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

- [AWS::Connect::TaskTemplate.DefaultFieldValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-defaultfieldvalue.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Connect::TaskTemplate.Field](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-field.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Connect::TaskTemplate.FieldIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-fieldidentifier.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::EMR::Cluster.AutoTerminationPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-autoterminationpolicy.html)
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

- [AWS::Route53::CidrCollection.Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrcollection-location.html)
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

- [AWS::Route53::RecordSet.CidrRoutingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrroutingconfig.html)
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

- [AWS::Route53::RecordSetGroup.CidrRoutingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrroutingconfig.html)
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

- [AWS::SES::ConfigurationSet.DeliveryOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-deliveryoptions.html)
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

- [AWS::SES::ConfigurationSet.ReputationOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-reputationoptions.html)
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

- [AWS::SES::ConfigurationSet.SendingOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-sendingoptions.html)
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

- [AWS::SES::ConfigurationSet.SuppressionOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-suppressionoptions.html)
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

- [AWS::SES::ConfigurationSet.TrackingOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-trackingoptions.html)
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

- [AWS::SES::ConfigurationSetEventDestination.SnsDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-snsdestination.html)
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

- [AWS::SageMaker::EndpointConfig.ClarifyExplainerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyexplainerconfig.html)
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-central-1`

- [AWS::SageMaker::EndpointConfig.ClarifyFeatureType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyfeaturetype.html)
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-central-1`

- [AWS::SageMaker::EndpointConfig.ClarifyHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyheader.html)
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-central-1`

- [AWS::SageMaker::EndpointConfig.ClarifyInferenceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyinferenceconfig.html)
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-central-1`

- [AWS::SageMaker::EndpointConfig.ClarifyShapBaselineConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyshapbaselineconfig.html)
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-central-1`

- [AWS::SageMaker::EndpointConfig.ClarifyShapConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyshapconfig.html)
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-central-1`

- [AWS::SageMaker::EndpointConfig.ClarifyTextConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifytextconfig.html)
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::AppIntegrations::EventIntegration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html)
  - `af-south-1`
  - `ap-northeast-2`

- [AWS::IoTEvents::AlarmModel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html)
  - `ca-central-1`

- [AWS::IoTEvents::Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html)
  - `ca-central-1`

- [AWS::IoTSiteWise::AccessPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::Asset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::AssetModel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::Dashboard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::Gateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::Portal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::KinesisAnalyticsV2::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html)
  - `ap-northeast-3`

- [AWS::SageMaker::ModelPackage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackage.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::Timestream::Database](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html)
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::Timestream::ScheduledQuery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html)
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::Timestream::Table](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html)
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::AppIntegrations::EventIntegration.EventFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-eventfilter.html)
  - `af-south-1`
  - `ap-northeast-2`

- [AWS::AppIntegrations::EventIntegration.EventIntegrationAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-eventintegrationassociation.html)
  - `af-south-1`
  - `ap-northeast-2`

- [AWS::AppIntegrations::EventIntegration.Metadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-metadata.html)
  - `af-south-1`
  - `ap-northeast-2`

- [AWS::Cognito::UserPool.UserAttributeUpdateSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-userattributeupdatesettings.html)
  - `us-west-1`
  - `us-gov-west-1`

- [AWS::ImageBuilder::DistributionConfiguration.FastLaunchConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::DistributionConfiguration.FastLaunchLaunchTemplateSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification.html)
  - Now available to **ALL** regions.

- [AWS::ImageBuilder::DistributionConfiguration.FastLaunchSnapshotConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::IoTEvents::AlarmModel.AcknowledgeFlow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-acknowledgeflow.html)
  - `ca-central-1`

- [AWS::IoTEvents::AlarmModel.AlarmAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html)
  - `ca-central-1`

- [AWS::IoTEvents::AlarmModel.AlarmCapabilities](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmcapabilities.html)
  - `ca-central-1`

- [AWS::IoTEvents::AlarmModel.AlarmEventActions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmeventactions.html)
  - `ca-central-1`

- [AWS::IoTEvents::AlarmModel.AlarmRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmrule.html)
  - `ca-central-1`

- [AWS::IoTEvents::AlarmModel.AssetPropertyTimestamp](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertytimestamp.html)
  - `ca-central-1`

- [AWS::IoTEvents::AlarmModel.AssetPropertyValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvalue.html)
  - `ca-central-1`

- [AWS::IoTEvents::AlarmModel.AssetPropertyVariant](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvariant.html)
  - `ca-central-1`

- [AWS::IoTEvents::AlarmModel.DynamoDB](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html)
  - `ca-central-1`

- [AWS::IoTEvents::AlarmModel.DynamoDBv2](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodbv2.html)
  - `ca-central-1`

- [AWS::IoTEvents::AlarmModel.Firehose](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-firehose.html)
  - `ca-central-1`

- [AWS::IoTEvents::AlarmModel.InitializationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-initializationconfiguration.html)
  - `ca-central-1`

- [AWS::IoTEvents::AlarmModel.IotEvents](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotevents.html)
  - `ca-central-1`

- [AWS::IoTEvents::AlarmModel.IotSiteWise](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotsitewise.html)
  - `ca-central-1`

- [AWS::IoTEvents::AlarmModel.IotTopicPublish](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iottopicpublish.html)
  - `ca-central-1`

- [AWS::IoTEvents::AlarmModel.Lambda](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-lambda.html)
  - `ca-central-1`

- [AWS::IoTEvents::AlarmModel.Payload](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-payload.html)
  - `ca-central-1`

- [AWS::IoTEvents::AlarmModel.SimpleRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-simplerule.html)
  - `ca-central-1`

- [AWS::IoTEvents::AlarmModel.Sns](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-sns.html)
  - `ca-central-1`

- [AWS::IoTEvents::AlarmModel.Sqs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-sqs.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.AssetPropertyTimestamp](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertytimestamp.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.AssetPropertyValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvalue.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.AssetPropertyVariant](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.ClearTimer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-cleartimer.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.DetectorModelDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-detectormodeldefinition.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.DynamoDB](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.DynamoDBv2](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodbv2.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.Event](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-event.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.Firehose](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-firehose.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.IotEvents](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotevents.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.IotSiteWise](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.IotTopicPublish](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iottopicpublish.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.Lambda](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-lambda.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.OnEnter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onenter.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.OnExit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onexit.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.OnInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-oninput.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.Payload](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-payload.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.ResetTimer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-resettimer.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.SetTimer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-settimer.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.SetVariable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-setvariable.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.Sns](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sns.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.Sqs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sqs.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.State](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html)
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.TransitionEvent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html)
  - `ca-central-1`

- [AWS::IoTEvents::Input.Attribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-attribute.html)
  - `ca-central-1`

- [AWS::IoTEvents::Input.InputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-inputdefinition.html)
  - `ca-central-1`

- [AWS::IoTSiteWise::AccessPolicy.AccessPolicyIdentity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyidentity.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::AccessPolicy.AccessPolicyResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyresource.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::AccessPolicy.IamRole](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-iamrole.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::AccessPolicy.IamUser](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-iamuser.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::AccessPolicy.Portal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-portal.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::AccessPolicy.Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-project.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::AccessPolicy.User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-user.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::Asset.AssetHierarchy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assethierarchy.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::Asset.AssetProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assetproperty.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::AssetModel.AssetModelCompositeModel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::AssetModel.AssetModelHierarchy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelhierarchy.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::AssetModel.AssetModelProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::AssetModel.Attribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-attribute.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::AssetModel.ExpressionVariable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-expressionvariable.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::AssetModel.Metric](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metric.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::AssetModel.MetricWindow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metricwindow.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::AssetModel.PropertyType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertytype.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::AssetModel.Transform](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-transform.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::AssetModel.TumblingWindow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-tumblingwindow.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::AssetModel.VariableValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-variablevalue.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::Gateway.GatewayCapabilitySummary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewaycapabilitysummary.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::Gateway.GatewayPlatform](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewayplatform.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::Gateway.Greengrass](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-greengrass.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::IoTSiteWise::Gateway.GreengrassV2](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-greengrassv2.html)
  - `us-east-2`
  - `ca-central-1`

- [AWS::KinesisAnalyticsV2::Application.ApplicationCodeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.ApplicationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.ApplicationSnapshotConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.CSVMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.CatalogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-catalogconfiguration.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.CheckpointConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.CodeContent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.CustomArtifactConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.DeployAsApplicationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.EnvironmentProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-environmentproperties.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.FlinkApplicationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.GlueDataCatalogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-gluedatacatalogconfiguration.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.InputLambdaProcessor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.InputParallelism](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputparallelism.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.InputProcessingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.InputSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.JSONMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-jsonmappingparameters.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.KinesisFirehoseInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.KinesisStreamsInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisstreamsinput.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.MappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.MavenReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.MonitoringConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.ParallelismConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.PropertyGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.RecordColumn](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.RecordFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.S3ContentBaseLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentbaselocation.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.S3ContentLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.SqlApplicationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-sqlapplicationconfiguration.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.ZeppelinApplicationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html)
  - `ap-northeast-3`

- [AWS::KinesisAnalyticsV2::Application.ZeppelinMonitoringConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinmonitoringconfiguration.html)
  - `ap-northeast-3`

- [AWS::Redshift::Cluster.Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-endpoint.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::SSM::Document.AttachmentsSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html)
  - Now available to **ALL** regions.

- [AWS::SSM::Document.DocumentRequires](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-documentrequires.html)
  - Now available to **ALL** regions.

- [AWS::SageMaker::Domain.RSessionAppSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-rsessionappsettings.html)
  - `eu-west-1`
  - `ap-southeast-2`
  - `eu-west-3`
  - `ap-southeast-1`
  - `cn-northwest-1`
  - `ap-east-1`
  - `us-west-2`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `us-east-1`
  - `eu-south-1`
  - `us-east-2`
  - `me-south-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-north-1`
  - `sa-east-1`
  - `af-south-1`
  - `us-west-1`

- [AWS::SageMaker::ModelPackage.AdditionalInferenceSpecificationDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-additionalinferencespecificationdefinition.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.Bias](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-bias.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.CreatedBy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-createdby.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.DataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-datasource.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.DriftCheckBaselines](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckbaselines.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.DriftCheckBias](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckbias.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.DriftCheckExplainability](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckexplainability.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.DriftCheckModelDataQuality](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckmodeldataquality.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.DriftCheckModelQuality](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-driftcheckmodelquality.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-environment.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.Explainability](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-explainability.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.FileSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-filesource.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.InferenceSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-inferencespecification.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.LastModifiedBy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-lastmodifiedby.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.MetadataProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-metadataproperties.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.MetricsSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-metricssource.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.ModelDataQuality](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modeldataquality.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.ModelMetrics](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelmetrics.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.ModelPackageContainerDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagecontainerdefinition.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.ModelPackageStatusDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagestatusdetails.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.ModelPackageStatusItem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelpackagestatusitem.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.ModelQuality](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-modelquality.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.S3DataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-s3datasource.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.SourceAlgorithm](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-sourcealgorithm.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.SourceAlgorithmSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-sourcealgorithmspecification.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.TransformInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transforminput.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.TransformJobDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformjobdefinition.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.TransformOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformoutput.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.TransformResources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-transformresources.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.ValidationProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-validationprofile.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::SageMaker::ModelPackage.ValidationSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelpackage-validationspecification.html)
  - `ap-northeast-1`
  - `eu-west-2`

- [AWS::Timestream::ScheduledQuery.DimensionMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-dimensionmapping.html)
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::Timestream::ScheduledQuery.ErrorReportConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-errorreportconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::Timestream::ScheduledQuery.MixedMeasureMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-mixedmeasuremapping.html)
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::Timestream::ScheduledQuery.MultiMeasureAttributeMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasureattributemapping.html)
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::Timestream::ScheduledQuery.MultiMeasureMappings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasuremappings.html)
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::Timestream::ScheduledQuery.NotificationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-notificationconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::Timestream::ScheduledQuery.S3Configuration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-s3configuration.html)
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::Timestream::ScheduledQuery.ScheduleConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-scheduleconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::Timestream::ScheduledQuery.SnsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-snsconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::Timestream::ScheduledQuery.TargetConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-targetconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-2`

- [AWS::Timestream::ScheduledQuery.TimestreamConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-timestreamconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-2`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::AppSync::GraphQLApi.AdditionalAuthenticationProviders](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationproviders.html)
  - `us-east-2`

- [AWS::AppSync::GraphQLApi.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-tags.html)
  - `us-east-2`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v73.1.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v73.1.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v73.1.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v73.1.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v73.1.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v73.1.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- PropertyType Still Missing
  - Since v73.1.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v73.1.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v73.1.0: [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v73.1.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v73.1.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::SageMaker::EndpointConfig.ClarifyExplainerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyexplainerconfig.html)
    - `ap-northeast-1`
    - `cn-north-1`
    - `eu-central-1`

  - [AWS::SageMaker::EndpointConfig.ClarifyFeatureType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyfeaturetype.html)
    - `ap-northeast-1`
    - `cn-north-1`
    - `eu-central-1`

  - [AWS::SageMaker::EndpointConfig.ClarifyHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyheader.html)
    - `ap-northeast-1`
    - `cn-north-1`
    - `eu-central-1`

  - [AWS::SageMaker::EndpointConfig.ClarifyInferenceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyinferenceconfig.html)
    - `ap-northeast-1`
    - `cn-north-1`
    - `eu-central-1`

  - [AWS::SageMaker::EndpointConfig.ClarifyShapBaselineConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyshapbaselineconfig.html)
    - `ap-northeast-1`
    - `cn-north-1`
    - `eu-central-1`

  - [AWS::SageMaker::EndpointConfig.ClarifyShapConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifyshapconfig.html)
    - `ap-northeast-1`
    - `cn-north-1`
    - `eu-central-1`

  - [AWS::SageMaker::EndpointConfig.ClarifyTextConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-clarifytextconfig.html)
    - `ap-northeast-1`
    - `cn-north-1`
    - `eu-central-1`

