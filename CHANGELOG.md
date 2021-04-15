# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v33-changelog.json`](changelogs/v33-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [33.1.0](#3310-2021-04-15)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)
- [33.0.0](#3300-2021-04-10)
  - [Totals](#totals-1)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-1)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-1)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-1)

## [33.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v33.1.0) (2021-04-15)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v33-changelog.json)
  - Change source is a diff between [v33.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v33.1.0) and [v33.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v33.0.0)

### Totals

- TotalPropertyTypes: 2401 **(+5)**
- TotalPropertyTypesSupportedGlobally: 586 **(+4)**
- TotalResourceTypes: 733 **(+2)**
- TotalResourceTypesSupportedGlobally: 213 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::EC2::EnclaveCertificateIamRoleAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-enclavecertificateiamroleassociation.html)
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

- [AWS::IVS::RecordingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::IVS::RecordingConfiguration.DestinationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-destinationconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::IVS::RecordingConfiguration.S3DestinationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-s3destinationconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::ImageBuilder::ContainerRecipe.EbsInstanceBlockDeviceSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html)
  - Available in **ALL** regions.

- [AWS::ImageBuilder::ContainerRecipe.InstanceBlockDeviceMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html)
  - Available in **ALL** regions.

- [AWS::ImageBuilder::ContainerRecipe.InstanceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceconfiguration.html)
  - Available in **ALL** regions.

- [AWS::ImageBuilder::DistributionConfiguration.LaunchTemplateConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchtemplateconfiguration.html)
  - Available in **ALL** regions.

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::MWAA::Environment.AirflowConfigurationOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-airflowconfigurationoptions.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Athena::DataCatalog](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html)
  - `af-south-1`
  - `eu-south-1`

- [AWS::Athena::NamedQuery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html)
  - `af-south-1`
  - `eu-south-1`

- [AWS::Athena::WorkGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html)
  - `af-south-1`
  - `eu-south-1`

- [AWS::Chatbot::SlackChannelConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html)
  - `ap-northeast-3`

- [AWS::CodeArtifact::Domain](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-domain.html)
  - `eu-west-2`
  - `eu-west-3`
  - `eu-south-1`

- [AWS::CodeArtifact::Repository](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html)
  - `eu-west-2`
  - `eu-west-3`
  - `eu-south-1`

- [AWS::EMRContainers::VirtualCluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html)
  - `ap-south-1`
  - `us-west-1`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `eu-west-2`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html)
  - `cn-north-1`

- [AWS::IoTEvents::Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html)
  - `cn-north-1`

- [AWS::Logs::QueryDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-querydefinition.html)
  - `af-south-1`
  - `eu-west-3`
  - `eu-south-1`
  - `us-east-2`
  - `eu-north-1`

- [AWS::Athena::WorkGroup.EncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html)
  - `af-south-1`
  - `eu-south-1`

- [AWS::Athena::WorkGroup.EngineVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-engineversion.html)
  - `eu-north-1`
  - `af-south-1`
  - `eu-south-1`

- [AWS::Athena::WorkGroup.ResultConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html)
  - `af-south-1`
  - `eu-south-1`

- [AWS::Athena::WorkGroup.ResultConfigurationUpdates](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html)
  - `af-south-1`
  - `eu-south-1`

- [AWS::Athena::WorkGroup.WorkGroupConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html)
  - `af-south-1`
  - `eu-south-1`

- [AWS::Athena::WorkGroup.WorkGroupConfigurationUpdates](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html)
  - `af-south-1`
  - `eu-south-1`

- [AWS::EMRContainers::VirtualCluster.ContainerInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerinfo.html)
  - `ap-south-1`
  - `us-west-1`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `eu-west-2`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::EMRContainers::VirtualCluster.ContainerProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html)
  - `ap-south-1`
  - `us-west-1`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `eu-west-2`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::EMRContainers::VirtualCluster.EksInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-eksinfo.html)
  - `ap-south-1`
  - `us-west-1`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `eu-central-1`
  - `ap-northeast-1`
  - `eu-west-2`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::IoT::TopicRule.CloudwatchLogsAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchlogsaction.html)
  - `us-gov-east-1`
  - `me-south-1`
  - `eu-west-3`
  - `ap-east-1`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-west-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `eu-north-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::IoT::TopicRule.KafkaAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html)
  - `us-gov-east-1`
  - `me-south-1`
  - `eu-west-3`
  - `ap-east-1`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-west-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `eu-north-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::IoT::TopicRule.TimestreamAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html)
  - `us-gov-east-1`
  - `me-south-1`
  - `eu-west-3`
  - `ap-east-1`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-west-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `eu-north-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::IoT::TopicRule.TimestreamDimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamdimension.html)
  - `us-gov-east-1`
  - `me-south-1`
  - `eu-west-3`
  - `ap-east-1`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-west-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `eu-north-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::IoT::TopicRule.TimestreamDimensionsList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamdimensionslist.html)
  - `us-gov-east-1`
  - `me-south-1`
  - `eu-west-3`
  - `ap-east-1`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-west-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `eu-north-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::IoT::TopicRule.TimestreamTimestamp](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamtimestamp.html)
  - `us-gov-east-1`
  - `me-south-1`
  - `eu-west-3`
  - `ap-east-1`
  - `eu-west-2`
  - `cn-northwest-1`
  - `us-west-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `eu-north-1`
  - `ap-northeast-2`
  - `ca-central-1`

- [AWS::IoTEvents::DetectorModel.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.AssetPropertyTimestamp](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertytimestamp.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.AssetPropertyValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvalue.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.AssetPropertyVariant](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.ClearTimer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-cleartimer.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.DetectorModelDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-detectormodeldefinition.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.DynamoDB](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.DynamoDBv2](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodbv2.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.Event](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-event.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.Firehose](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-firehose.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.IotEvents](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotevents.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.IotSiteWise](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.IotTopicPublish](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iottopicpublish.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.Lambda](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-lambda.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.OnEnter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onenter.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.OnExit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onexit.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.OnInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-oninput.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.Payload](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-payload.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.ResetTimer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-resettimer.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.SetTimer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-settimer.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.SetVariable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-setvariable.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.Sns](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sns.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.Sqs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sqs.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.State](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html)
  - `cn-north-1`

- [AWS::IoTEvents::DetectorModel.TransitionEvent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html)
  - `cn-north-1`

- [AWS::IoTEvents::Input.Attribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-attribute.html)
  - `cn-north-1`

- [AWS::IoTEvents::Input.InputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-inputdefinition.html)
  - `cn-north-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v33.0.0: [AWS::CloudFront::Distribution.LegacyCustomOrigin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html)
    - `eu-central-1`

  - Since v33.0.0: [AWS::CloudFront::Distribution.LegacyS3Origin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacys3origin.html)
    - `eu-central-1`

  - Since v33.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v33.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v33.0.0: [AWS::SSM::Document.AttachmentsSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html)
    - `us-west-2`

  - Since v33.0.0: [AWS::SSM::Document.DocumentRequires](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-documentrequires.html)
    - `us-west-2`

## [33.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v33.0.0) (2021-04-10)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v33-changelog.json)
  - Change source is a diff between [v33.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v33.0.0) and [v32.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v32.0.0)

### Totals

- TotalPropertyTypes: 2396 **(+9)**
- TotalPropertyTypesSupportedGlobally: 582 **(+8)**
- TotalResourceTypes: 731 **(+0)**
- TotalResourceTypesSupportedGlobally: 213 **(+2)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::CloudFront::Distribution.LegacyCustomOrigin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html)
  - `eu-central-1`

- [AWS::CloudFront::Distribution.LegacyS3Origin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacys3origin.html)
  - `eu-central-1`

- [AWS::DynamoDB::Table.KinesisStreamSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-kinesisstreamspecification.html)
  - Available in **ALL** regions.

- [AWS::IoT::TopicRule.CloudwatchLogsAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchlogsaction.html)
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

- [AWS::IoT::TopicRule.KafkaAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html)
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

- [AWS::IoT::TopicRule.TimestreamAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html)
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

- [AWS::IoT::TopicRule.TimestreamDimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamdimension.html)
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

- [AWS::IoT::TopicRule.TimestreamDimensionsList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamdimensionslist.html)
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

- [AWS::IoT::TopicRule.TimestreamTimestamp](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamtimestamp.html)
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

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::AmazonMQ::Broker](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html)
  - `ap-northeast-3`

- [AWS::AmazonMQ::Configuration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html)
  - `ap-northeast-3`

- [AWS::AmazonMQ::ConfigurationAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configurationassociation.html)
  - `ap-northeast-3`

- [AWS::Config::AggregationAuthorization](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html)
  - `af-south-1`
  - `eu-south-1`

- [AWS::Config::ConfigurationAggregator](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html)
  - `af-south-1`
  - `eu-south-1`

- [AWS::EKS::Cluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html)
  - Now available to **ALL** regions.

- [AWS::EKS::Nodegroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html)
  - Now available to **ALL** regions.

- [AWS::IoT::DomainConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html)
  - `ap-northeast-2`
  - `us-west-2`
  - `eu-west-1`
  - `us-east-2`
  - `ap-south-1`
  - `us-west-1`
  - `ap-east-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `eu-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `ca-central-1`
  - `me-south-1`
  - `sa-east-1`

- [AWS::Route53Resolver::FirewallDomainList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html)
  - `ap-northeast-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `us-west-1`
  - `af-south-1`
  - `us-gov-east-1`
  - `ap-east-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `eu-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-south-1`
  - `me-south-1`
  - `sa-east-1`

- [AWS::Route53Resolver::FirewallRuleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html)
  - `ap-northeast-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `us-west-1`
  - `af-south-1`
  - `us-gov-east-1`
  - `ap-east-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `eu-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-south-1`
  - `me-south-1`
  - `sa-east-1`

- [AWS::Route53Resolver::FirewallRuleGroupAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html)
  - `ap-northeast-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `us-west-1`
  - `af-south-1`
  - `us-gov-east-1`
  - `ap-east-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `eu-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-south-1`
  - `me-south-1`
  - `sa-east-1`

- [AWS::AmazonMQ::Broker.ConfigurationId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-configurationid.html)
  - `ap-northeast-3`

- [AWS::AmazonMQ::Broker.EncryptionOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-encryptionoptions.html)
  - `ap-northeast-3`

- [AWS::AmazonMQ::Broker.LdapServerMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapservermetadata.html)
  - `ap-northeast-3`

- [AWS::AmazonMQ::Broker.LogList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-loglist.html)
  - `ap-northeast-3`

- [AWS::AmazonMQ::Broker.MaintenanceWindow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html)
  - `ap-northeast-3`

- [AWS::AmazonMQ::Broker.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-tagsentry.html)
  - `ap-northeast-3`

- [AWS::AmazonMQ::Broker.User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-user.html)
  - `ap-northeast-3`

- [AWS::AmazonMQ::Configuration.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configuration-tagsentry.html)
  - `ap-northeast-3`

- [AWS::AmazonMQ::ConfigurationAssociation.ConfigurationId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configurationassociation-configurationid.html)
  - `ap-northeast-3`

- [AWS::Config::ConfigurationAggregator.AccountAggregationSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html)
  - `af-south-1`
  - `eu-south-1`

- [AWS::Config::ConfigurationAggregator.OrganizationAggregationSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html)
  - `af-south-1`
  - `eu-south-1`

- [AWS::EKS::Cluster.EncryptionConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-encryptionconfig.html)
  - Now available to **ALL** regions.

- [AWS::EKS::Cluster.KubernetesNetworkConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-kubernetesnetworkconfig.html)
  - Now available to **ALL** regions.

- [AWS::EKS::Cluster.Provider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-provider.html)
  - Now available to **ALL** regions.

- [AWS::EKS::Cluster.ResourcesVpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-resourcesvpcconfig.html)
  - Now available to **ALL** regions.

- [AWS::EKS::Nodegroup.LaunchTemplateSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-launchtemplatespecification.html)
  - Now available to **ALL** regions.

- [AWS::EKS::Nodegroup.RemoteAccess](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-remoteaccess.html)
  - Now available to **ALL** regions.

- [AWS::EKS::Nodegroup.ScalingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html)
  - Now available to **ALL** regions.

- [AWS::IoT::DomainConfiguration.AuthorizerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-authorizerconfig.html)
  - `ap-northeast-2`
  - `us-west-2`
  - `eu-west-1`
  - `us-east-2`
  - `ap-south-1`
  - `us-west-1`
  - `ap-east-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `eu-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `ca-central-1`
  - `me-south-1`
  - `sa-east-1`

- [AWS::IoT::DomainConfiguration.ServerCertificateSummary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-servercertificatesummary.html)
  - `ap-northeast-2`
  - `us-west-2`
  - `eu-west-1`
  - `us-east-2`
  - `ap-south-1`
  - `us-west-1`
  - `ap-east-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `eu-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `ca-central-1`
  - `me-south-1`
  - `sa-east-1`

- [AWS::MediaLive::Channel.HtmlMotionGraphicsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-htmlmotiongraphicssettings.html)
  - `ap-northeast-2`
  - `us-east-1`
  - `sa-east-1`

- [AWS::MediaLive::Channel.MotionGraphicsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-motiongraphicsconfiguration.html)
  - `ap-northeast-2`
  - `us-east-1`
  - `sa-east-1`

- [AWS::MediaLive::Channel.MotionGraphicsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-motiongraphicssettings.html)
  - `ap-northeast-2`
  - `us-east-1`
  - `sa-east-1`

- [AWS::MediaLive::Channel.VideoSelectorColorSpaceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorcolorspacesettings.html)
  - `ap-northeast-2`
  - `us-east-1`
  - `sa-east-1`

- [AWS::Route53Resolver::FirewallRuleGroup.FirewallRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html)
  - `ap-northeast-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `us-west-1`
  - `af-south-1`
  - `us-gov-east-1`
  - `ap-east-1`
  - `ca-central-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `eu-north-1`
  - `eu-west-3`
  - `ap-southeast-2`
  - `eu-south-1`
  - `me-south-1`
  - `sa-east-1`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::MWAA::Environment.AirflowConfigurationOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-airflowconfigurationoptions.html)
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v32.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v32.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v32.0.0: [AWS::SSM::Document.AttachmentsSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html)
    - `us-west-2`

  - Since v32.0.0: [AWS::SSM::Document.DocumentRequires](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-documentrequires.html)
    - `us-west-2`

- New PropertyType(s) Missing
  - [AWS::CloudFront::Distribution.LegacyCustomOrigin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html)
    - `eu-central-1`

  - [AWS::CloudFront::Distribution.LegacyS3Origin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacys3origin.html)
    - `eu-central-1`

