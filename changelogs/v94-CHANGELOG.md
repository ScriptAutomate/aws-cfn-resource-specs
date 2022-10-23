# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v94-changelog.json`](changelogs/v94-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [94.0.0](#9400-2022-10-23)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [94.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v94.0.0) (2022-10-23)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v94-changelog.json)
  - Change source is a diff between [v94.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v94.0.0) and [v93.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v93.0.0)

### Totals

- TotalPropertyTypes: 3385 **(+21)**
- TotalPropertyTypesSupportedGlobally: 1161 **(+0)**
- TotalResourceTypes: 971 **(+0)**
- TotalResourceTypesSupportedGlobally: 352 **(+4)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::DevOpsGuru::NotificationChannel.NotificationFilterConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationfilterconfig.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`

- [AWS::SageMaker::DataQualityJobDefinition.BatchTransformInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-batchtransforminput.html)
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::SageMaker::DataQualityJobDefinition.Csv](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-csv.html)
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::SageMaker::DataQualityJobDefinition.DatasetFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-datasetformat.html)
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::SageMaker::DataQualityJobDefinition.Json](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-json.html)
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::SageMaker::ModelBiasJobDefinition.BatchTransformInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-batchtransforminput.html)
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::SageMaker::ModelBiasJobDefinition.Csv](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-csv.html)
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::SageMaker::ModelBiasJobDefinition.DatasetFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-datasetformat.html)
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::SageMaker::ModelBiasJobDefinition.Json](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-json.html)
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.BatchTransformInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-batchtransforminput.html)
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.Csv](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-csv.html)
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.DatasetFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-datasetformat.html)
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.Json](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-json.html)
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::SageMaker::ModelQualityJobDefinition.BatchTransformInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-batchtransforminput.html)
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::SageMaker::ModelQualityJobDefinition.Csv](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-csv.html)
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::SageMaker::ModelQualityJobDefinition.DatasetFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-datasetformat.html)
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::SageMaker::ModelQualityJobDefinition.Json](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-json.html)
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::SageMaker::MonitoringSchedule.BatchTransformInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-batchtransforminput.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-northwest-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::SageMaker::MonitoringSchedule.Csv](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-csv.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-northwest-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::SageMaker::MonitoringSchedule.DatasetFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-datasetformat.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-northwest-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::SageMaker::MonitoringSchedule.Json](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-json.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-northwest-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Backup::Framework](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html)
  - `eu-south-1`

- [AWS::Backup::ReportPlan](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html)
  - `eu-south-1`

- [AWS::SES::ContactList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html)
  - `cn-northwest-1`

- [AWS::Transfer::Agreement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html)
  - Now available to **ALL** regions.

- [AWS::Transfer::Certificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html)
  - Now available to **ALL** regions.

- [AWS::Transfer::Connector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-connector.html)
  - Now available to **ALL** regions.

- [AWS::Transfer::Profile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-profile.html)
  - Now available to **ALL** regions.

- [AWS::Backup::Framework.ControlInputParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlinputparameter.html)
  - `eu-south-1`

- [AWS::Backup::Framework.FrameworkControl](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html)
  - `eu-south-1`

- [AWS::Budgets::Budget.AutoAdjustData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-autoadjustdata.html)
  - `ap-northeast-2`
  - `eu-west-3`
  - `ca-central-1`
  - `eu-west-2`
  - `us-west-1`
  - `cn-northwest-1`
  - `us-east-2`

- [AWS::Budgets::Budget.HistoricalOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-historicaloptions.html)
  - `ap-northeast-2`
  - `eu-west-3`
  - `ca-central-1`
  - `eu-west-2`
  - `us-west-1`
  - `cn-northwest-1`
  - `us-east-2`

- [AWS::EC2::EC2Fleet.NetworkBandwidthGbpsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-networkbandwidthgbpsrequest.html)
  - `eu-west-1`
  - `eu-west-3`
  - `sa-east-1`
  - `ap-northeast-3`
  - `eu-west-2`
  - `ap-southeast-2`
  - `us-west-1`
  - `cn-north-1`
  - `ap-southeast-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `ca-central-1`
  - `ap-south-1`
  - `us-east-2`
  - `eu-north-1`

- [AWS::EC2::SpotFleet.NetworkBandwidthGbpsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-networkbandwidthgbpsrequest.html)
  - `eu-west-1`
  - `eu-west-3`
  - `sa-east-1`
  - `ap-northeast-3`
  - `eu-west-2`
  - `ap-southeast-2`
  - `us-west-1`
  - `cn-north-1`
  - `ap-southeast-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `ca-central-1`
  - `ap-south-1`
  - `us-east-2`
  - `eu-north-1`

- [AWS::Glue::Trigger.EventBatchingCondition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-eventbatchingcondition.html)
  - `me-south-1`

- [AWS::IoT::TopicRule.LocationAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-locationaction.html)
  - `eu-west-1`
  - `eu-west-3`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-southeast-2`
  - `us-west-1`
  - `cn-northwest-1`
  - `us-gov-east-1`
  - `ap-southeast-1`
  - `cn-north-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `ap-east-1`
  - `ca-central-1`
  - `me-south-1`
  - `ap-south-1`
  - `us-east-2`
  - `eu-north-1`

- [AWS::IoT::TopicRule.Timestamp](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestamp.html)
  - `eu-west-1`
  - `eu-west-3`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-southeast-2`
  - `us-west-1`
  - `cn-northwest-1`
  - `us-gov-east-1`
  - `ap-southeast-1`
  - `cn-north-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `ap-east-1`
  - `ca-central-1`
  - `me-south-1`
  - `ap-south-1`
  - `us-east-2`
  - `eu-north-1`

- [AWS::Lex::Bot.AllowedInputTypes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-allowedinputtypes.html)
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `us-east-1`
  - `ca-central-1`
  - `af-south-1`
  - `eu-west-2`
  - `ap-southeast-2`
  - `ap-southeast-1`

- [AWS::Lex::Bot.AudioAndDTMFInputSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audioanddtmfinputspecification.html)
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `us-east-1`
  - `ca-central-1`
  - `af-south-1`
  - `eu-west-2`
  - `ap-southeast-2`
  - `ap-southeast-1`

- [AWS::Lex::Bot.AudioSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audiospecification.html)
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `us-east-1`
  - `ca-central-1`
  - `af-south-1`
  - `eu-west-2`
  - `ap-southeast-2`
  - `ap-southeast-1`

- [AWS::Lex::Bot.DTMFSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dtmfspecification.html)
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `us-east-1`
  - `ca-central-1`
  - `af-south-1`
  - `eu-west-2`
  - `ap-southeast-2`
  - `ap-southeast-1`

- [AWS::Lex::Bot.PromptAttemptSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptattemptspecification.html)
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `us-east-1`
  - `ca-central-1`
  - `af-south-1`
  - `eu-west-2`
  - `ap-southeast-2`
  - `ap-southeast-1`

- [AWS::Lex::Bot.TextInputSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-textinputspecification.html)
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `us-east-1`
  - `ca-central-1`
  - `af-south-1`
  - `eu-west-2`
  - `ap-southeast-2`
  - `ap-southeast-1`

- [AWS::NetworkFirewall::FirewallPolicy.StatefulRuleGroupOverride](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupoverride.html)
  - `eu-central-1`

- [AWS::SES::ContactList.Topic](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html)
  - `cn-northwest-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v93.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v93.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v93.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v93.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v93.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v93.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- PropertyType Still Missing
  - Since v93.0.0: [AWS::Config::OrganizationConfigRule.OrganizationCustomPolicyRuleMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html)
    - `me-south-1`

  - Since v93.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v93.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v93.0.0: [AWS::EC2::EC2Fleet.NetworkBandwidthGbpsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-networkbandwidthgbpsrequest.html)
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

  - Since v93.0.0: [AWS::EC2::SpotFleet.NetworkBandwidthGbpsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-networkbandwidthgbpsrequest.html)
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

  - Since v93.0.0: [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v93.0.0: [AWS::IoT::TopicRule.LocationAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-locationaction.html)
    - `ap-east-1`
    - `ap-northeast-1`
    - `ap-northeast-2`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `ca-central-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `sa-east-1`
    - `us-east-2`
    - `us-gov-east-1`
    - `us-west-1`

  - Since v93.0.0: [AWS::IoT::TopicRule.Timestamp](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestamp.html)
    - `ap-east-1`
    - `ap-northeast-1`
    - `ap-northeast-2`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `ca-central-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `sa-east-1`
    - `us-east-2`
    - `us-gov-east-1`
    - `us-west-1`

  - Since v93.0.0: [AWS::NetworkFirewall::FirewallPolicy.StatefulRuleGroupOverride](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupoverride.html)
    - `ap-southeast-2`
    - `eu-central-1`

  - Since v93.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v93.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

