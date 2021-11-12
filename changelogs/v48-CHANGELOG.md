# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v48-changelog.json`](changelogs/v48-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [48.0.0](#4800-2021-11-12)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [48.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v48.0.0) (2021-11-12)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v48-changelog.json)
  - Change source is a diff between [v48.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v48.0.0) and [v47.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v47.0.0)

### Totals

- TotalPropertyTypes: 2752 **(+10)**
- TotalPropertyTypesSupportedGlobally: 1000 **(+9)**
- TotalResourceTypes: 835 **(+3)**
- TotalResourceTypesSupportedGlobally: 330 **(+1)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::Batch::SchedulingPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-schedulingpolicy.html)
  - Available in **ALL** regions.

- [AWS::IoTWireless::FuotaTask](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html)
  - `ap-northeast-1`
  - `ap-southeast-2`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::IoTWireless::MulticastGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html)
  - `ap-northeast-1`
  - `ap-southeast-2`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Batch::SchedulingPolicy.FairsharePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-fairsharepolicy.html)
  - Available in **ALL** regions.

- [AWS::Batch::SchedulingPolicy.ShareAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-schedulingpolicy-shareattributes.html)
  - Available in **ALL** regions.

- [AWS::CloudWatch::AnomalyDetector.Metric](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html)
  - Available in **ALL** regions.

- [AWS::CloudWatch::AnomalyDetector.MetricDataQueries](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataqueries.html)
  - Available in **ALL** regions.

- [AWS::CloudWatch::AnomalyDetector.MetricDataQuery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html)
  - Available in **ALL** regions.

- [AWS::CloudWatch::AnomalyDetector.MetricStat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html)
  - Available in **ALL** regions.

- [AWS::FSx::FileSystem.DiskIopsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration-diskiopsconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::FSx::FileSystem.OntapConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::FinSpace::Environment.SuperuserParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-superuserparameters.html)
  - `ca-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::IoTWireless::FuotaTask.LoRaWAN](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-fuotatask-lorawan.html)
  - `ap-northeast-1`
  - `ap-southeast-2`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::IoTWireless::MulticastGroup.LoRaWAN](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html)
  - `ap-northeast-1`
  - `ap-southeast-2`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::EKS::Cluster.Provider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-provider.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-northwest-1`
  - `eu-north-1`
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::CloudFront::ResponseHeadersPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-responseheaderspolicy.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::DataSync::LocationHDFS](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationhdfs.html)
  - `us-gov-east-1`
  - `ap-southeast-2`

- [AWS::IoT::Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html)
  - `ap-northeast-2`
  - `cn-northwest-1`
  - `me-south-1`
  - `us-gov-west-1`

- [AWS::IoT::ResourceSpecificLogging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html)
  - `ap-northeast-2`
  - `me-south-1`
  - `cn-northwest-1`

- [AWS::QLDB::Stream](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html)
  - `ca-central-1`

- [AWS::SSMContacts::Contact](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html)
  - `us-west-1`
  - `ap-northeast-2`

- [AWS::SSMContacts::ContactChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html)
  - `us-west-1`
  - `ap-northeast-2`

- [AWS::ServiceCatalog::ServiceAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::ServiceCatalog::ServiceActionAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::CloudFront::ResponseHeadersPolicy.AccessControlAllowHeaders](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowheaders.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::CloudFront::ResponseHeadersPolicy.AccessControlAllowMethods](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowmethods.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::CloudFront::ResponseHeadersPolicy.AccessControlAllowOrigins](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolalloworigins.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::CloudFront::ResponseHeadersPolicy.AccessControlExposeHeaders](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolexposeheaders.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::CloudFront::ResponseHeadersPolicy.ContentSecurityPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-contentsecuritypolicy.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::CloudFront::ResponseHeadersPolicy.ContentTypeOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-contenttypeoptions.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::CloudFront::ResponseHeadersPolicy.CorsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::CloudFront::ResponseHeadersPolicy.CustomHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheader.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::CloudFront::ResponseHeadersPolicy.CustomHeadersConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheadersconfig.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::CloudFront::ResponseHeadersPolicy.FrameOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-frameoptions.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::CloudFront::ResponseHeadersPolicy.ReferrerPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-referrerpolicy.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::CloudFront::ResponseHeadersPolicy.ResponseHeadersPolicyConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::CloudFront::ResponseHeadersPolicy.SecurityHeadersConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::CloudFront::ResponseHeadersPolicy.StrictTransportSecurity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-stricttransportsecurity.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::CloudFront::ResponseHeadersPolicy.XSSProtection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-xssprotection.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::DataSync::LocationHDFS.NameNode](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationhdfs-namenode.html)
  - `us-gov-east-1`
  - `ap-southeast-2`

- [AWS::DataSync::LocationHDFS.QopConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationhdfs-qopconfiguration.html)
  - `us-gov-east-1`
  - `ap-southeast-2`

- [AWS::EC2::EC2Fleet.CapacityRebalance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-capacityrebalance.html)
  - `us-west-1`
  - `ca-central-1`
  - `ap-northeast-3`
  - `us-east-2`
  - `eu-west-2`

- [AWS::EC2::EC2Fleet.MaintenanceStrategies](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-maintenancestrategies.html)
  - `us-west-1`
  - `ca-central-1`
  - `ap-northeast-3`
  - `us-east-2`
  - `eu-west-2`

- [AWS::EC2::TransitGatewayPeeringAttachment.TransitGatewayPeeringAttachmentOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewaypeeringattachment-transitgatewaypeeringattachmentoptions.html)
  - `eu-west-2`

- [AWS::EKS::Cluster.ClusterLogging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-clusterlogging.html)
  - Now available to **ALL** regions.

- [AWS::EKS::Cluster.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-logging.html)
  - Now available to **ALL** regions.

- [AWS::EKS::Cluster.LoggingTypeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-loggingtypeconfig.html)
  - Now available to **ALL** regions.

- [AWS::QLDB::Stream.KinesisConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qldb-stream-kinesisconfiguration.html)
  - `ca-central-1`

- [AWS::SSMContacts::Contact.ChannelTargetInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-channeltargetinfo.html)
  - `us-west-1`
  - `ap-northeast-2`

- [AWS::SSMContacts::Contact.ContactTargetInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-contacttargetinfo.html)
  - `us-west-1`
  - `ap-northeast-2`

- [AWS::SSMContacts::Contact.Stage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-stage.html)
  - `us-west-1`
  - `ap-northeast-2`

- [AWS::SSMContacts::Contact.Targets](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-targets.html)
  - `us-west-1`
  - `ap-northeast-2`

- [AWS::ServiceCatalog::ServiceAction.DefinitionParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-serviceaction-definitionparameter.html)
  - `ap-east-1`
  - `me-south-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v47.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v47.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v47.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v47.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v47.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v47.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- PropertyType Still Missing
  - Since v47.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v47.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v47.0.0: [AWS::MediaLive::Channel.AudioHlsRenditionSelection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiohlsrenditionselection.html)
    - `ap-northeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `sa-east-1`

  - Since v47.0.0: [AWS::MediaLive::Channel.AudioWatermarkSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiowatermarksettings.html)
    - `ap-northeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `sa-east-1`

  - Since v47.0.0: [AWS::MediaLive::Channel.NielsenCBET](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsencbet.html)
    - `ap-northeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `sa-east-1`

  - Since v47.0.0: [AWS::MediaLive::Channel.NielsenNaesIiNw](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsennaesiinw.html)
    - `ap-northeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `sa-east-1`

  - Since v47.0.0: [AWS::MediaLive::Channel.NielsenWatermarksSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenwatermarkssettings.html)
    - `ap-northeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `sa-east-1`

  - Since v47.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v47.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v47.0.0: [AWS::SageMaker::DataQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v47.0.0: [AWS::SageMaker::ModelBiasJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-environment.html)
    - `eu-west-3`

  - Since v47.0.0: [AWS::SageMaker::ModelExplainabilityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v47.0.0: [AWS::SageMaker::ModelQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v47.0.0: [AWS::SageMaker::MonitoringSchedule.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-environment.html)
    - `cn-northwest-1`
    - `eu-west-3`

