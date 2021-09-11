# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v41-changelog.json`](changelogs/v41-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [41.1.0](#4110-2021-09-11)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)
- [41.0.0](#4100-2021-09-03)
  - [Totals](#totals-1)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-1)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-1)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions-1)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-1)

## [41.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v41.1.0) (2021-09-11)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v41-changelog.json)
  - Change source is a diff between [v41.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v41.1.0) and [v41.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v41.0.0)

### Totals

- TotalPropertyTypes: 2587 **(+0)**
- TotalPropertyTypesSupportedGlobally: 922 **(+1)**
- TotalResourceTypes: 788 **(+1)**
- TotalResourceTypesSupportedGlobally: 325 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::EC2::TransitGatewayVpcAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayvpcattachment.html)
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

- [AWS::Athena::PreparedStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html)
  - `ap-northeast-3`

- [AWS::IoT::FleetMetric](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html)
  - `us-east-2`
  - `cn-northwest-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `eu-north-1`
  - `me-south-1`
  - `ap-south-1`
  - `eu-west-3`
  - `us-gov-west-1`
  - `sa-east-1`
  - `us-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `us-gov-east-1`
  - `ap-southeast-2`

- [AWS::IoTAnalytics::Channel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html)
  - `ap-south-1`

- [AWS::ServiceDiscovery::HttpNamespace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::ServiceDiscovery::Instance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::ServiceDiscovery::PrivateDnsNamespace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::ServiceDiscovery::Service](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::CloudTrail::Trail.InsightSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-insightselector.html)
  - Now available to **ALL** regions.

- [AWS::IoT::FleetMetric.AggregationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-fleetmetric-aggregationtype.html)
  - `us-east-2`
  - `cn-northwest-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `eu-north-1`
  - `me-south-1`
  - `ap-south-1`
  - `eu-west-3`
  - `us-gov-west-1`
  - `sa-east-1`
  - `us-west-1`
  - `ca-central-1`
  - `eu-west-2`
  - `us-gov-east-1`
  - `ap-southeast-2`

- [AWS::IoTAnalytics::Channel.ChannelStorage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-channelstorage.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Channel.CustomerManagedS3](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-customermanageds3.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Channel.RetentionPeriod](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-retentionperiod.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Channel.ServiceManagedS3](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-servicemanageds3.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-action.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.ContainerAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-containeraction.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.DatasetContentDeliveryRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryrule.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.DatasetContentDeliveryRuleDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryruledestination.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.DatasetContentVersionValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable-datasetcontentversionvalue.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.DeltaTime](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatime.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.DeltaTimeSessionWindowConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatimesessionwindowconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-filter.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.GlueConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-glueconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.IotEventsDestinationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-ioteventsdestinationconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.LateDataRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-latedatarule.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.LateDataRuleConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-latedataruleconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.OutputFileUriValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable-outputfileurivalue.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.QueryAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-queryaction.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.ResourceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-resourceconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.RetentionPeriod](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-retentionperiod.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.S3DestinationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-s3destinationconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-trigger-schedule.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.Trigger](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-trigger.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.TriggeringDataset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-triggeringdataset.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.Variable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Dataset.VersioningConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-versioningconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.Column](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-column.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.CustomerManagedS3](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.CustomerManagedS3Storage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3storage.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.DatastorePartition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartition.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.DatastorePartitions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartitions.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.DatastoreStorage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorestorage.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.FileFormatConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-fileformatconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.IotSiteWiseMultiLayerStorage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-iotsitewisemultilayerstorage.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.JsonConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-jsonconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.ParquetConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-parquetconfiguration.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.Partition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-partition.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.RetentionPeriod](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-retentionperiod.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.SchemaDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-schemadefinition.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.ServiceManagedS3](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-servicemanageds3.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Datastore.TimestampPartition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-timestamppartition.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.Activity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.AddAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-addattributes.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.Channel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-channel.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.Datastore](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-datastore.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.DeviceRegistryEnrich](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.DeviceShadowEnrich](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-filter.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.Lambda](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-lambda.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.Math](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-math.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.RemoveAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-removeattributes.html)
  - `ap-south-1`

- [AWS::IoTAnalytics::Pipeline.SelectAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-selectattributes.html)
  - `ap-south-1`

- [AWS::ServiceDiscovery::PrivateDnsNamespace.PrivateDnsPropertiesMutable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-privatednspropertiesmutable.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::ServiceDiscovery::PrivateDnsNamespace.Properties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-properties.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::ServiceDiscovery::PrivateDnsNamespace.SOA](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-soa.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::ServiceDiscovery::Service.DnsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsconfig.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::ServiceDiscovery::Service.DnsRecord](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsrecord.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::ServiceDiscovery::Service.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckconfig.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::ServiceDiscovery::Service.HealthCheckCustomConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckcustomconfig.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::KinesisAnalyticsV2::Application.CustomArtifactsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactsconfiguration.html)
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v41.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v41.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v41.0.0: [AWS::SageMaker::DataQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v41.0.0: [AWS::SageMaker::ModelBiasJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-environment.html)
    - `eu-west-3`

  - Since v41.0.0: [AWS::SageMaker::ModelExplainabilityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v41.0.0: [AWS::SageMaker::ModelQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v41.0.0: [AWS::SageMaker::MonitoringSchedule.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-environment.html)
    - `cn-northwest-1`
    - `eu-west-3`

## [41.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v41.0.0) (2021-09-03)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v41-changelog.json)
  - Change source is a diff between [v41.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v41.0.0) and [v40.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v40.1.0)

### Totals

- TotalPropertyTypes: 2587 **(+12)**
- TotalPropertyTypesSupportedGlobally: 921 **(+5)**
- TotalResourceTypes: 787 **(+3)**
- TotalResourceTypesSupportedGlobally: 325 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::IoT::FleetMetric](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::S3::MultiRegionAccessPoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html)
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

- [AWS::S3::MultiRegionAccessPointPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspointpolicy.html)
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

- [AWS::ACMPCA::CertificateAuthority.OcspConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-ocspconfiguration.html)
  - `af-south-1`
  - `ap-east-1`
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
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudTrail::Trail.InsightSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-insightselector.html)
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

- [AWS::Events::Rule.CapacityProviderStrategyItem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-capacityproviderstrategyitem.html)
  - Available in **ALL** regions.

- [AWS::Events::Rule.PlacementConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-placementconstraint.html)
  - Available in **ALL** regions.

- [AWS::Events::Rule.PlacementStrategy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-placementstrategy.html)
  - Available in **ALL** regions.

- [AWS::Events::Rule.Tag](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-tag.html)
  - Available in **ALL** regions.

- [AWS::IoT::FleetMetric.AggregationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-fleetmetric-aggregationtype.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::KinesisFirehose::DeliveryStream.DynamicPartitioningConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration.html)
  - Available in **ALL** regions.

- [AWS::S3::MultiRegionAccessPoint.PublicAccessBlockConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspoint-publicaccessblockconfiguration.html)
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

- [AWS::S3::MultiRegionAccessPoint.Region](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-multiregionaccesspoint-region.html)
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

- [AWS::Transfer::Server.WorkflowDetail](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetail.html)
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
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::Transfer::Server.WorkflowDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetails.html)
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
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::CustomerProfiles::Domain](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::ObjectType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html)
  - `ca-central-1`

- [AWS::DataSync::LocationFSxWindows](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html)
  - `ap-northeast-3`

- [AWS::CustomerProfiles::Integration.ConnectorOperator](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.FlowDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.IncrementalPullConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-incrementalpullconfig.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.MarketoSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-marketosourceproperties.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.S3SourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.SalesforceSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.ScheduledTriggerProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.ServiceNowSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-servicenowsourceproperties.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.SourceConnectorProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.SourceFlowConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.Task](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.TaskPropertiesMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.TriggerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.TriggerProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerproperties.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::Integration.ZendeskSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-zendesksourceproperties.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::ObjectType.FieldMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::ObjectType.KeyMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::ObjectType.ObjectTypeField](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html)
  - `ca-central-1`

- [AWS::CustomerProfiles::ObjectType.ObjectTypeKey](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html)
  - `ca-central-1`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::SageMaker::DataQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-environment.html)
  - `ap-south-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `ap-southeast-2`
  - `eu-west-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `us-east-1`
  - `eu-west-1`
  - `us-west-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `us-east-2`

- [AWS::SageMaker::ModelBiasJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-environment.html)
  - `ap-south-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `ap-southeast-2`
  - `eu-west-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `us-east-1`
  - `eu-west-1`
  - `us-west-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `us-east-2`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-environment.html)
  - `ap-south-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `ap-southeast-2`
  - `eu-west-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `us-east-1`
  - `eu-west-1`
  - `us-west-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `us-east-2`

- [AWS::SageMaker::ModelQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-environment.html)
  - `ap-south-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `ap-southeast-2`
  - `eu-west-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `us-east-1`
  - `eu-west-1`
  - `us-west-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `us-east-2`

- [AWS::SageMaker::MonitoringSchedule.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-environment.html)
  - `ap-south-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `ap-southeast-2`
  - `eu-west-2`
  - `cn-north-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `sa-east-1`
  - `us-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-west-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `us-east-2`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v40.1.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v40.1.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v40.1.0: [AWS::SageMaker::DataQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v40.1.0: [AWS::SageMaker::ModelBiasJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-environment.html)
    - `eu-west-3`

  - Since v40.1.0: [AWS::SageMaker::ModelExplainabilityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v40.1.0: [AWS::SageMaker::ModelQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v40.1.0: [AWS::SageMaker::MonitoringSchedule.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-environment.html)
    - `cn-northwest-1`
    - `eu-west-3`

