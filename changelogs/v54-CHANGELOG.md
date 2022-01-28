# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v54-changelog.json`](changelogs/v54-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [54.0.0](#5400-2022-01-28)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [54.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v54.0.0) (2022-01-28)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v54-changelog.json)
  - Change source is a diff between [v54.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v54.0.0) and [v53.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v53.1.0)

### Totals

- TotalPropertyTypes: 2949 **(+3)**
- TotalPropertyTypesSupportedGlobally: 1057 **(+5)**
- TotalResourceTypes: 887 **(+2)**
- TotalResourceTypesSupportedGlobally: 333 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::AppIntegrations::DataIntegration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Rekognition::Collection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-collection.html)
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
  - `us-west-2`

- [AWS::AppIntegrations::DataIntegration.ScheduleConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-scheduleconfig.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::IVS::RecordingConfiguration.ThumbnailConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::MSK::Cluster.ProvisionedThroughput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-provisionedthroughput.html)
  - Available in **ALL** regions.

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::EC2::CarrierGateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-carriergateway.html)
  - `ca-central-1`

- [AWS::KafkaConnect::Connector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html)
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-2`
  - `eu-west-2`

- [AWS::Lightsail::Certificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-certificate.html)
  - `ca-central-1`
  - `ap-southeast-2`
  - `eu-north-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `eu-west-3`
  - `ap-south-1`
  - `eu-west-2`

- [AWS::Lightsail::Container](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html)
  - `ca-central-1`
  - `ap-southeast-2`
  - `eu-north-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `eu-west-3`
  - `ap-south-1`
  - `eu-west-2`

- [AWS::SES::ContactList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html)
  - `ap-northeast-3`
  - `ap-southeast-1`

- [AWS::ApplicationInsights::Application.HAClusterPrometheusExporter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-haclusterprometheusexporter.html)
  - Now available to **ALL** regions.

- [AWS::ApplicationInsights::Application.HANAPrometheusExporter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-hanaprometheusexporter.html)
  - Now available to **ALL** regions.

- [AWS::AutoScaling::WarmPool.InstanceReusePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-warmpool-instancereusepolicy.html)
  - `me-south-1`
  - `ap-east-1`
  - `eu-north-1`
  - `eu-west-3`
  - `ap-northeast-3`
  - `eu-south-1`
  - `cn-northwest-1`
  - `af-south-1`

- [AWS::GuardDuty::Detector.CFNKubernetesAuditLogsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnkubernetesauditlogsconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::GuardDuty::Detector.CFNKubernetesConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnkubernetesconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::IoTSiteWise::Gateway.GreengrassV2](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-greengrassv2.html)
  - `cn-north-1`

- [AWS::KafkaConnect::Connector.ApacheKafkaCluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-apachekafkacluster.html)
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-2`
  - `eu-west-2`

- [AWS::KafkaConnect::Connector.AutoScaling](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html)
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-2`
  - `eu-west-2`

- [AWS::KafkaConnect::Connector.Capacity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-capacity.html)
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-2`
  - `eu-west-2`

- [AWS::KafkaConnect::Connector.CloudWatchLogsLogDelivery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-cloudwatchlogslogdelivery.html)
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-2`
  - `eu-west-2`

- [AWS::KafkaConnect::Connector.CustomPlugin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-customplugin.html)
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-2`
  - `eu-west-2`

- [AWS::KafkaConnect::Connector.FirehoseLogDelivery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-firehoselogdelivery.html)
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-2`
  - `eu-west-2`

- [AWS::KafkaConnect::Connector.KafkaCluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkacluster.html)
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-2`
  - `eu-west-2`

- [AWS::KafkaConnect::Connector.KafkaClusterClientAuthentication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterclientauthentication.html)
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-2`
  - `eu-west-2`

- [AWS::KafkaConnect::Connector.KafkaClusterEncryptionInTransit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterencryptionintransit.html)
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-2`
  - `eu-west-2`

- [AWS::KafkaConnect::Connector.LogDelivery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-logdelivery.html)
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-2`
  - `eu-west-2`

- [AWS::KafkaConnect::Connector.Plugin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-plugin.html)
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-2`
  - `eu-west-2`

- [AWS::KafkaConnect::Connector.ProvisionedCapacity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-provisionedcapacity.html)
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-2`
  - `eu-west-2`

- [AWS::KafkaConnect::Connector.S3LogDelivery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html)
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-2`
  - `eu-west-2`

- [AWS::KafkaConnect::Connector.ScaleInPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleinpolicy.html)
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-2`
  - `eu-west-2`

- [AWS::KafkaConnect::Connector.ScaleOutPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleoutpolicy.html)
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-2`
  - `eu-west-2`

- [AWS::KafkaConnect::Connector.Vpc](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-vpc.html)
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-2`
  - `eu-west-2`

- [AWS::KafkaConnect::Connector.WorkerConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerconfiguration.html)
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-2`
  - `eu-west-2`

- [AWS::KafkaConnect::Connector.WorkerLogDelivery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html)
  - `ap-northeast-2`
  - `eu-north-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-south-1`
  - `sa-east-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-southeast-2`
  - `us-east-2`
  - `us-west-2`
  - `eu-west-2`

- [AWS::Lightsail::Container.Container](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-container.html)
  - `ca-central-1`
  - `ap-southeast-2`
  - `eu-north-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `eu-west-3`
  - `ap-south-1`
  - `eu-west-2`

- [AWS::Lightsail::Container.ContainerServiceDeployment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-containerservicedeployment.html)
  - `ca-central-1`
  - `ap-southeast-2`
  - `eu-north-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `eu-west-3`
  - `ap-south-1`
  - `eu-west-2`

- [AWS::Lightsail::Container.EnvironmentVariable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-environmentvariable.html)
  - `ca-central-1`
  - `ap-southeast-2`
  - `eu-north-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `eu-west-3`
  - `ap-south-1`
  - `eu-west-2`

- [AWS::Lightsail::Container.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-healthcheckconfig.html)
  - `ca-central-1`
  - `ap-southeast-2`
  - `eu-north-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `eu-west-3`
  - `ap-south-1`
  - `eu-west-2`

- [AWS::Lightsail::Container.PortInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-portinfo.html)
  - `ca-central-1`
  - `ap-southeast-2`
  - `eu-north-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `eu-west-3`
  - `ap-south-1`
  - `eu-west-2`

- [AWS::Lightsail::Container.PublicDomainName](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicdomainname.html)
  - `ca-central-1`
  - `ap-southeast-2`
  - `eu-north-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `eu-west-3`
  - `ap-south-1`
  - `eu-west-2`

- [AWS::Lightsail::Container.PublicEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicendpoint.html)
  - `ca-central-1`
  - `ap-southeast-2`
  - `eu-north-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `eu-west-3`
  - `ap-south-1`
  - `eu-west-2`

- [AWS::SES::ContactList.Topic](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html)
  - `ap-northeast-3`
  - `ap-southeast-1`

- [AWS::SSM::MaintenanceWindowTask.CloudWatchOutputConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig.html)
  - `me-south-1`
  - `ap-east-1`
  - `eu-north-1`
  - `ap-northeast-2`
  - `us-gov-east-1`
  - `eu-central-1`
  - `us-gov-west-1`
  - `eu-south-1`
  - `af-south-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v53.1.0: [AWS::CloudFormation::HookDefaultVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookdefaultversion.html)
    - `eu-central-1`

  - Since v53.1.0: [AWS::CloudFormation::HookTypeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hooktypeconfig.html)
    - `eu-central-1`

  - Since v53.1.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v53.1.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v53.1.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v53.1.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v53.1.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v53.1.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- PropertyType Still Missing
  - Since v53.1.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v53.1.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v53.1.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v53.1.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

