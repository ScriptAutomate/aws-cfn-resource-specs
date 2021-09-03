# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v41-changelog.json`](changelogs/v41-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [41.0.0](#4100-2021-09-03)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

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

