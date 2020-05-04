# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v14-changelog.json`](changelogs/v14-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [14.1.0](#1410-2020-05-03)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)
- [14.0.0](#1400-2020-04-25)
  - [Totals](#totals-1)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-1)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-1)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-1)

## [14.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v14.1.0) (2020-05-03)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v14-changelog.json)
  - Change source is a diff between [v14.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v14.1.0) and [v14.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v14.0.0)

### Totals

- TotalPropertyTypes: 1346 **(+9)**
- TotalPropertyTypesSupportedGlobally: 483 **(+0)**
- TotalResourceTypes: 531 **(+1)**
- TotalResourceTypesSupportedGlobally: 187 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::EventSchemas::RegistryPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html)
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
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

- [AWS::IoTEvents::DetectorModel.AssetPropertyTimestamp](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertytimestamp.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::IoTEvents::DetectorModel.AssetPropertyValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvalue.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::IoTEvents::DetectorModel.AssetPropertyVariant](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::IoTEvents::DetectorModel.DynamoDB](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::IoTEvents::DetectorModel.DynamoDBv2](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodbv2.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::IoTEvents::DetectorModel.IotSiteWise](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::IoTEvents::DetectorModel.Payload](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-payload.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::MediaStore::Container.MetricPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-metricpolicy.html)
  - `eu-west-1`
  - `us-east-1`

- [AWS::MediaStore::Container.MetricPolicyRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-metricpolicyrule.html)
  - `eu-west-1`
  - `us-east-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::MSK::Cluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::MSK::Cluster.BrokerLogs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::MSK::Cluster.BrokerNodeGroupInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::MSK::Cluster.ClientAuthentication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::MSK::Cluster.CloudWatchLogs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::MSK::Cluster.ConfigurationInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::MSK::Cluster.EBSStorageInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::MSK::Cluster.EncryptionAtRest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionatrest.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::MSK::Cluster.EncryptionInTransit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::MSK::Cluster.EncryptionInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::MSK::Cluster.Firehose](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::MSK::Cluster.JmxExporter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-jmxexporter.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::MSK::Cluster.LoggingInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-logginginfo.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::MSK::Cluster.NodeExporter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-nodeexporter.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::MSK::Cluster.OpenMonitoring](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::MSK::Cluster.Prometheus](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::MSK::Cluster.S3](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::MSK::Cluster.StorageInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-storageinfo.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::MSK::Cluster.Tls](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html)
  - `cn-northwest-1`
  - `cn-north-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v14.0.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `ap-southeast-2`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v14.0.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `ap-southeast-2`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v14.0.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `ap-southeast-2`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v14.0.0: [AWS::ImageBuilder::Component](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html)
    - `ap-east-1`
    - `ap-northeast-2`
    - `ap-southeast-2`
    - `ca-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `sa-east-1`
    - `us-east-2`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `us-west-1`

  - Since v14.0.0: [AWS::ImageBuilder::DistributionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html)
    - `ap-east-1`
    - `ap-northeast-2`
    - `ap-southeast-2`
    - `ca-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `sa-east-1`
    - `us-east-2`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `us-west-1`

  - Since v14.0.0: [AWS::ImageBuilder::ImagePipeline](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html)
    - `ap-east-1`
    - `ap-northeast-2`
    - `ap-south-1`
    - `ap-southeast-2`
    - `ca-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `sa-east-1`
    - `us-east-2`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `us-west-1`

  - Since v14.0.0: [AWS::ImageBuilder::ImageRecipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html)
    - `ap-east-1`
    - `ap-northeast-2`
    - `ap-southeast-2`
    - `ca-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `sa-east-1`
    - `us-east-2`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `us-west-1`

  - Since v14.0.0: [AWS::ImageBuilder::InfrastructureConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html)
    - `ap-east-1`
    - `ap-northeast-2`
    - `ap-south-1`
    - `ap-southeast-2`
    - `ca-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `sa-east-1`
    - `us-east-2`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `us-west-1`

- PropertyType Still Missing
  - Since v14.0.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `ap-southeast-2`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v14.0.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `ap-southeast-2`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v14.0.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `ap-southeast-2`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v14.0.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `ap-southeast-2`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v14.0.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `ap-southeast-2`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v14.0.0: [AWS::ImageBuilder::DistributionConfiguration.Distribution](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html)
    - `ap-east-1`
    - `ap-northeast-2`
    - `ap-southeast-2`
    - `ca-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `sa-east-1`
    - `us-east-2`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `us-west-1`

  - Since v14.0.0: [AWS::ImageBuilder::ImagePipeline.ImageTestsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html)
    - `ap-east-1`
    - `ap-northeast-2`
    - `ap-south-1`
    - `ap-southeast-2`
    - `ca-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `sa-east-1`
    - `us-east-2`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `us-west-1`

  - Since v14.0.0: [AWS::ImageBuilder::ImagePipeline.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html)
    - `ap-east-1`
    - `ap-northeast-2`
    - `ap-south-1`
    - `ap-southeast-2`
    - `ca-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `sa-east-1`
    - `us-east-2`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `us-west-1`

  - Since v14.0.0: [AWS::ImageBuilder::ImageRecipe.ComponentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html)
    - `ap-east-1`
    - `ap-northeast-2`
    - `ap-southeast-2`
    - `ca-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `sa-east-1`
    - `us-east-2`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `us-west-1`

  - Since v14.0.0: [AWS::ImageBuilder::ImageRecipe.EbsInstanceBlockDeviceSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html)
    - `ap-east-1`
    - `ap-northeast-2`
    - `ap-southeast-2`
    - `ca-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `sa-east-1`
    - `us-east-2`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `us-west-1`

  - Since v14.0.0: [AWS::ImageBuilder::ImageRecipe.InstanceBlockDeviceMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html)
    - `ap-east-1`
    - `ap-northeast-2`
    - `ap-southeast-2`
    - `ca-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `sa-east-1`
    - `us-east-2`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `us-west-1`

  - Since v14.0.0: [AWS::ImageBuilder::InfrastructureConfiguration.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-logging.html)
    - `ap-east-1`
    - `ap-northeast-2`
    - `ap-south-1`
    - `ap-southeast-2`
    - `ca-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `sa-east-1`
    - `us-east-2`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `us-west-1`

  - Since v14.0.0: [AWS::ImageBuilder::InfrastructureConfiguration.S3Logs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html)
    - `ap-east-1`
    - `ap-northeast-2`
    - `ap-south-1`
    - `ap-southeast-2`
    - `ca-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `sa-east-1`
    - `us-east-2`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `us-west-1`

## [14.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v14.0.0) (2020-04-25)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v14-changelog.json)
  - Change source is a diff between [v14.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v14.0.0) and [v13.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v13.0.0)

### Totals

- TotalPropertyTypes: 1337 **(+12)**
- TotalPropertyTypesSupportedGlobally: 520 **(+0)**
- TotalResourceTypes: 530 **(+7)**
- TotalResourceTypesSupportedGlobally: 193 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::CE::CostCategory](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html)
  - `us-east-1`

- [AWS::ImageBuilder::Component](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html)
  - `eu-north-1`
  - `eu-west-3`
  - `eu-west-2`
  - `ap-northeast-2`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-1`
  - `ap-east-1`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `me-south-1`

- [AWS::ImageBuilder::DistributionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html)
  - `eu-north-1`
  - `eu-west-3`
  - `eu-west-2`
  - `ap-northeast-2`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-1`
  - `ap-east-1`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `me-south-1`

- [AWS::ImageBuilder::ImagePipeline](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html)
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `ap-northeast-2`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-1`
  - `ap-east-1`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `me-south-1`

- [AWS::ImageBuilder::ImageRecipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html)
  - `eu-north-1`
  - `eu-west-3`
  - `eu-west-2`
  - `ap-northeast-2`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-1`
  - `ap-east-1`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `me-south-1`

- [AWS::ImageBuilder::InfrastructureConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html)
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `ap-northeast-2`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-1`
  - `ap-east-1`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `me-south-1`

- [AWS::Synthetics::Canary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html)
  - `us-east-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::ImageBuilder::DistributionConfiguration.Distribution](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html)
  - `eu-north-1`
  - `eu-west-3`
  - `eu-west-2`
  - `ap-northeast-2`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-1`
  - `ap-east-1`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `me-south-1`

- [AWS::ImageBuilder::ImagePipeline.ImageTestsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html)
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `ap-northeast-2`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-1`
  - `ap-east-1`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `me-south-1`

- [AWS::ImageBuilder::ImagePipeline.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html)
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `ap-northeast-2`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-1`
  - `ap-east-1`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `me-south-1`

- [AWS::ImageBuilder::ImageRecipe.ComponentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html)
  - `eu-north-1`
  - `eu-west-3`
  - `eu-west-2`
  - `ap-northeast-2`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-1`
  - `ap-east-1`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `me-south-1`

- [AWS::ImageBuilder::ImageRecipe.EbsInstanceBlockDeviceSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html)
  - `eu-north-1`
  - `eu-west-3`
  - `eu-west-2`
  - `ap-northeast-2`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-1`
  - `ap-east-1`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `me-south-1`

- [AWS::ImageBuilder::ImageRecipe.InstanceBlockDeviceMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html)
  - `eu-north-1`
  - `eu-west-3`
  - `eu-west-2`
  - `ap-northeast-2`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-1`
  - `ap-east-1`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `me-south-1`

- [AWS::ImageBuilder::InfrastructureConfiguration.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-logging.html)
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `ap-northeast-2`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-1`
  - `ap-east-1`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `me-south-1`

- [AWS::ImageBuilder::InfrastructureConfiguration.S3Logs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html)
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `ap-northeast-2`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-1`
  - `ap-east-1`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `me-south-1`

- [AWS::Synthetics::Canary.Code](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html)
  - `us-east-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Synthetics::Canary.RunConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html)
  - `us-east-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Synthetics::Canary.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-schedule.html)
  - `us-east-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Synthetics::Canary.VPCConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html)
  - `us-east-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Transfer::Server.Protocol]()
  - `us-east-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::StepFunctions::StateMachine.TracingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tracingconfiguration.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::MediaConvert::JobTemplate.HopDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-hopdestination.html)
  - `ap-south-1`
  - `ap-northeast-1`
  - `us-west-2`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `eu-central-1`
  - `ap-northeast-2`
  - `us-west-1`
  - `eu-west-3`
  - `ca-central-1`
  - `eu-north-1`
  - `us-east-2`

- [AWS::SSM::PatchBaseline.PatchStringDate]()
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-1`
  - `us-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v13.0.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

  - Since v13.0.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

  - Since v13.0.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

- New ResourceType(s) Missing
  - [AWS::ImageBuilder::Component](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html)
    - `eu-north-1`
    - `eu-west-3`
    - `eu-west-2`
    - `ap-northeast-2`
    - `sa-east-1`
    - `ca-central-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-1`
    - `ap-east-1`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `me-south-1`

  - [AWS::ImageBuilder::DistributionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html)
    - `eu-north-1`
    - `eu-west-3`
    - `eu-west-2`
    - `ap-northeast-2`
    - `sa-east-1`
    - `ca-central-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-1`
    - `ap-east-1`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `me-south-1`

  - [AWS::ImageBuilder::ImagePipeline](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html)
    - `eu-north-1`
    - `ap-south-1`
    - `eu-west-3`
    - `eu-west-2`
    - `ap-northeast-2`
    - `sa-east-1`
    - `ca-central-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-1`
    - `ap-east-1`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `me-south-1`

  - [AWS::ImageBuilder::ImageRecipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html)
    - `eu-north-1`
    - `eu-west-3`
    - `eu-west-2`
    - `ap-northeast-2`
    - `sa-east-1`
    - `ca-central-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-1`
    - `ap-east-1`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `me-south-1`

  - [AWS::ImageBuilder::InfrastructureConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html)
    - `eu-north-1`
    - `ap-south-1`
    - `eu-west-3`
    - `eu-west-2`
    - `ap-northeast-2`
    - `sa-east-1`
    - `ca-central-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-1`
    - `ap-east-1`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `me-south-1`

- PropertyType Still Missing
  - Since v13.0.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

  - Since v13.0.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

  - Since v13.0.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

  - Since v13.0.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

  - Since v13.0.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

- New PropertyType(s) Missing
  - [AWS::ImageBuilder::DistributionConfiguration.Distribution](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html)
    - `eu-north-1`
    - `eu-west-3`
    - `eu-west-2`
    - `ap-northeast-2`
    - `sa-east-1`
    - `ca-central-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-1`
    - `ap-east-1`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `me-south-1`

  - [AWS::ImageBuilder::ImagePipeline.ImageTestsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html)
    - `eu-north-1`
    - `ap-south-1`
    - `eu-west-3`
    - `eu-west-2`
    - `ap-northeast-2`
    - `sa-east-1`
    - `ca-central-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-1`
    - `ap-east-1`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `me-south-1`

  - [AWS::ImageBuilder::ImagePipeline.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html)
    - `eu-north-1`
    - `ap-south-1`
    - `eu-west-3`
    - `eu-west-2`
    - `ap-northeast-2`
    - `sa-east-1`
    - `ca-central-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-1`
    - `ap-east-1`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `me-south-1`

  - [AWS::ImageBuilder::ImageRecipe.ComponentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html)
    - `eu-north-1`
    - `eu-west-3`
    - `eu-west-2`
    - `ap-northeast-2`
    - `sa-east-1`
    - `ca-central-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-1`
    - `ap-east-1`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `me-south-1`

  - [AWS::ImageBuilder::ImageRecipe.EbsInstanceBlockDeviceSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html)
    - `eu-north-1`
    - `eu-west-3`
    - `eu-west-2`
    - `ap-northeast-2`
    - `sa-east-1`
    - `ca-central-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-1`
    - `ap-east-1`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `me-south-1`

  - [AWS::ImageBuilder::ImageRecipe.InstanceBlockDeviceMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html)
    - `eu-north-1`
    - `eu-west-3`
    - `eu-west-2`
    - `ap-northeast-2`
    - `sa-east-1`
    - `ca-central-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-1`
    - `ap-east-1`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `me-south-1`

  - [AWS::ImageBuilder::InfrastructureConfiguration.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-logging.html)
    - `eu-north-1`
    - `ap-south-1`
    - `eu-west-3`
    - `eu-west-2`
    - `ap-northeast-2`
    - `sa-east-1`
    - `ca-central-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-1`
    - `ap-east-1`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `me-south-1`

  - [AWS::ImageBuilder::InfrastructureConfiguration.S3Logs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html)
    - `eu-north-1`
    - `ap-south-1`
    - `eu-west-3`
    - `eu-west-2`
    - `ap-northeast-2`
    - `sa-east-1`
    - `ca-central-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-1`
    - `ap-east-1`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `me-south-1`

