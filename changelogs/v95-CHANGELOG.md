# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v95-changelog.json`](changelogs/v95-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [95.0.0](#9500-2022-10-30)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [95.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v95.0.0) (2022-10-30)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v95-changelog.json)
  - Change source is a diff between [v95.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v95.0.0) and [v94.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v94.0.0)

### Totals

- TotalPropertyTypes: 3389 **(+4)**
- TotalPropertyTypesSupportedGlobally: 1165 **(+4)**
- TotalResourceTypes: 972 **(+1)**
- TotalResourceTypesSupportedGlobally: 356 **(+4)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::FSx::DataRepositoryAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-datarepositoryassociation.html)
  - Available in **ALL** regions.

- [AWS::FSx::DataRepositoryAssociation.AutoExportPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-datarepositoryassociation-autoexportpolicy.html)
  - Available in **ALL** regions.

- [AWS::FSx::DataRepositoryAssociation.AutoImportPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-datarepositoryassociation-autoimportpolicy.html)
  - Available in **ALL** regions.

- [AWS::FSx::DataRepositoryAssociation.S3](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-datarepositoryassociation-s3.html)
  - Available in **ALL** regions.

- [AWS::IoT::TopicRule.RepublishActionHeaders](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishactionheaders.html)
  - `eu-central-1`

- [AWS::IoT::TopicRule.UserProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-userproperty.html)
  - `eu-central-1`

- [AWS::RUM::AppMonitor.MetricDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-metricdefinition.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::RUM::AppMonitor.MetricDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-metricdestination.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Rekognition::StreamProcessor.Polygon](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-polygon.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::AppFlow::ConnectorProfile.CredentialsMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customauthcredentials.html#cfn-appflow-connectorprofile-customauthcredentials-credentialsmap)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AppFlow::ConnectorProfile.ProfileProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-profileproperties.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AppFlow::ConnectorProfile.TokenUrlCustomProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-tokenurlcustomproperties.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AppFlow::Flow.CustomProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customproperties.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Route53Resolver::FirewallDomainList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html)
  - Now available to **ALL** regions.

- [AWS::Route53Resolver::FirewallRuleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html)
  - Now available to **ALL** regions.

- [AWS::Route53Resolver::FirewallRuleGroupAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html)
  - Now available to **ALL** regions.

- [AWS::DevOpsGuru::NotificationChannel.NotificationFilterConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationfilterconfig.html)
  - `us-east-2`
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-north-1`
  - `eu-west-3`
  - `eu-west-2`
  - `us-west-1`
  - `sa-east-1`
  - `us-west-2`
  - `ap-southeast-2`

- [AWS::EC2::EC2Fleet.NetworkBandwidthGbpsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-networkbandwidthgbpsrequest.html)
  - `us-west-2`

- [AWS::EC2::SpotFleet.NetworkBandwidthGbpsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-networkbandwidthgbpsrequest.html)
  - `us-west-2`

- [AWS::IoT::TopicRule.LocationAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-locationaction.html)
  - `us-west-2`
  - `us-east-1`

- [AWS::IoT::TopicRule.Timestamp](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestamp.html)
  - `us-west-2`
  - `us-east-1`

- [AWS::Lambda::EventSourceMapping.AmazonManagedKafkaEventSourceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::Lambda::EventSourceMapping.SelfManagedKafkaEventSourceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::Lex::Bot.AllowedInputTypes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-allowedinputtypes.html)
  - `us-west-2`

- [AWS::Lex::Bot.AudioAndDTMFInputSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audioanddtmfinputspecification.html)
  - `us-west-2`

- [AWS::Lex::Bot.AudioSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audiospecification.html)
  - `us-west-2`

- [AWS::Lex::Bot.DTMFSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dtmfspecification.html)
  - `us-west-2`

- [AWS::Lex::Bot.PromptAttemptSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptattemptspecification.html)
  - `us-west-2`

- [AWS::Lex::Bot.TextInputSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-textinputspecification.html)
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.StatefulRuleGroupOverride](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupoverride.html)
  - `us-west-2`

- [AWS::Route53Resolver::FirewallRuleGroup.FirewallRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html)
  - Now available to **ALL** regions.

- [AWS::SageMaker::DataQualityJobDefinition.BatchTransformInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-batchtransforminput.html)
  - `ap-east-1`
  - `us-west-2`

- [AWS::SageMaker::DataQualityJobDefinition.Csv](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-csv.html)
  - `ap-east-1`
  - `us-west-2`

- [AWS::SageMaker::DataQualityJobDefinition.DatasetFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-datasetformat.html)
  - `ap-east-1`
  - `us-west-2`

- [AWS::SageMaker::DataQualityJobDefinition.Json](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-json.html)
  - `ap-east-1`
  - `us-west-2`

- [AWS::SageMaker::ModelBiasJobDefinition.BatchTransformInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-batchtransforminput.html)
  - `ap-east-1`
  - `us-west-2`

- [AWS::SageMaker::ModelBiasJobDefinition.Csv](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-csv.html)
  - `ap-east-1`
  - `us-west-2`

- [AWS::SageMaker::ModelBiasJobDefinition.DatasetFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-datasetformat.html)
  - `ap-east-1`
  - `us-west-2`

- [AWS::SageMaker::ModelBiasJobDefinition.Json](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-json.html)
  - `ap-east-1`
  - `us-west-2`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.BatchTransformInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-batchtransforminput.html)
  - `ap-east-1`
  - `us-west-2`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.Csv](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-csv.html)
  - `ap-east-1`
  - `us-west-2`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.DatasetFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-datasetformat.html)
  - `ap-east-1`
  - `us-west-2`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.Json](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-json.html)
  - `ap-east-1`
  - `us-west-2`

- [AWS::SageMaker::ModelQualityJobDefinition.BatchTransformInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput.html)
  - `ap-east-1`
  - `us-west-2`

- [AWS::SageMaker::ModelQualityJobDefinition.Csv](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-csv.html)
  - `ap-east-1`
  - `us-west-2`

- [AWS::SageMaker::ModelQualityJobDefinition.DatasetFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-datasetformat.html)
  - `ap-east-1`
  - `us-west-2`

- [AWS::SageMaker::ModelQualityJobDefinition.Json](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-json.html)
  - `ap-east-1`
  - `us-west-2`

- [AWS::SageMaker::MonitoringSchedule.BatchTransformInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-batchtransforminput.html)
  - `ap-east-1`
  - `us-west-2`

- [AWS::SageMaker::MonitoringSchedule.Csv](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-csv.html)
  - `ap-east-1`
  - `us-west-2`

- [AWS::SageMaker::MonitoringSchedule.DatasetFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-datasetformat.html)
  - `ap-east-1`
  - `us-west-2`

- [AWS::SageMaker::MonitoringSchedule.Json](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-json.html)
  - `ap-east-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v94.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v94.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v94.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v94.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v94.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v94.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- PropertyType Still Missing
  - Since v94.0.0: [AWS::Config::OrganizationConfigRule.OrganizationCustomPolicyRuleMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html)
    - `me-south-1`

  - Since v94.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v94.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v94.0.0: [AWS::EC2::EC2Fleet.NetworkBandwidthGbpsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-networkbandwidthgbpsrequest.html)
    - `ap-northeast-1`
    - `ap-northeast-2`
    - `ap-northeast-3`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `ca-central-1`
    - `cn-north-1`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `eu-west-2`
    - `eu-west-3`
    - `sa-east-1`
    - `us-east-2`
    - `us-west-1`
    - `us-west-2`

  - Since v94.0.0: [AWS::EC2::SpotFleet.NetworkBandwidthGbpsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-networkbandwidthgbpsrequest.html)
    - `ap-northeast-1`
    - `ap-northeast-2`
    - `ap-northeast-3`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `ca-central-1`
    - `cn-north-1`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `eu-west-2`
    - `eu-west-3`
    - `sa-east-1`
    - `us-east-2`
    - `us-west-1`
    - `us-west-2`

  - Since v94.0.0: [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v94.0.0: [AWS::NetworkFirewall::FirewallPolicy.StatefulRuleGroupOverride](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupoverride.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `us-west-2`

  - Since v94.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v94.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::IoT::TopicRule.RepublishActionHeaders](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishactionheaders.html)
    - `eu-central-1`

  - [AWS::IoT::TopicRule.UserProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-userproperty.html)
    - `eu-central-1`

