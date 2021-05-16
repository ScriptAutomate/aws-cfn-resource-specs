# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v36-changelog.json`](changelogs/v36-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [36.0.0](#3600-2021-05-15)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [36.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v36.0.0) (2021-05-15)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v36-changelog.json)
  - Change source is a diff between [v36.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v36.0.0) and [v35.2.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v35.2.0)

### Totals

- TotalPropertyTypes: 2453 **(+45)**
- TotalPropertyTypesSupportedGlobally: 657 **(+61)**
- TotalResourceTypes: 757 **(+5)**
- TotalResourceTypesSupportedGlobally: 219 **(+6)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::DynamoDB::GlobalTable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html)
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::SSMContacts::Contact](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::SSMContacts::ContactChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::SSMIncidents::ReplicationSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::SSMIncidents::ResponsePlan](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::AppFlow::Flow.ZendeskDestinationProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-zendeskdestinationproperties.html)
  - `ap-southeast-2`
  - `us-east-1`

- [AWS::CustomerProfiles::Integration.ConnectorOperator](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::Integration.FlowDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::Integration.IncrementalPullConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-incrementalpullconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::Integration.MarketoSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-marketosourceproperties.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::Integration.S3SourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::Integration.SalesforceSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::Integration.ScheduledTriggerProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::Integration.ServiceNowSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-servicenowsourceproperties.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::Integration.SourceConnectorProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::Integration.SourceFlowConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::Integration.Task](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::Integration.TaskPropertiesMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::Integration.TriggerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::Integration.TriggerProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerproperties.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::CustomerProfiles::Integration.ZendeskSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-zendesksourceproperties.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::DynamoDB::GlobalTable.AttributeDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-attributedefinition.html)
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DynamoDB::GlobalTable.CapacityAutoScalingSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-capacityautoscalingsettings.html)
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DynamoDB::GlobalTable.ContributorInsightsSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-contributorinsightsspecification.html)
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DynamoDB::GlobalTable.GlobalSecondaryIndex](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-globalsecondaryindex.html)
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DynamoDB::GlobalTable.KeySchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-keyschema.html)
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DynamoDB::GlobalTable.LocalSecondaryIndex](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-localsecondaryindex.html)
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DynamoDB::GlobalTable.PointInTimeRecoverySpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-pointintimerecoveryspecification.html)
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DynamoDB::GlobalTable.Projection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-projection.html)
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DynamoDB::GlobalTable.ReadProvisionedThroughputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings.html)
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DynamoDB::GlobalTable.ReplicaGlobalSecondaryIndexSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html)
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DynamoDB::GlobalTable.ReplicaSSESpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicassespecification.html)
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DynamoDB::GlobalTable.ReplicaSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-replicaspecification.html)
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DynamoDB::GlobalTable.SSESpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-ssespecification.html)
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DynamoDB::GlobalTable.StreamSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-streamspecification.html)
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DynamoDB::GlobalTable.TargetTrackingScalingPolicyConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html)
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DynamoDB::GlobalTable.TimeToLiveSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-timetolivespecification.html)
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::DynamoDB::GlobalTable.WriteProvisionedThroughputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-globaltable-writeprovisionedthroughputsettings.html)
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::MediaPackage::Channel.LogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-logconfiguration.html)
  - `eu-central-1`

- [AWS::MediaPackage::PackagingGroup.LogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-logconfiguration.html)
  - `eu-central-1`

- [AWS::SSMContacts::Contact.Stage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-stage.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::SSMContacts::Contact.Targets](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-targets.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::SSMIncidents::ReplicationSet.RegionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-replicationset-regionconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::SSMIncidents::ReplicationSet.ReplicationRegion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-replicationset-replicationregion.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::SSMIncidents::ResponsePlan.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-action.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::SSMIncidents::ResponsePlan.ChatChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-chatchannel.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::SSMIncidents::ResponsePlan.IncidentTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::SSMIncidents::ResponsePlan.NotificationTargetItem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-notificationtargetitem.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::SSMIncidents::ResponsePlan.SsmAutomation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::SSMIncidents::ResponsePlan.SsmParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmparameter.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::ACMPCA::Certificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::CertificateAuthority](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::CertificateAuthorityActivation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html)
  - `ap-northeast-3`

- [AWS::CloudFront::Function](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-function.html)
  - `us-east-2`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `af-south-1`
  - `eu-west-3`
  - `eu-central-1`
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-south-1`
  - `ap-east-1`
  - `eu-west-1`
  - `eu-north-1`
  - `ca-central-1`
  - `eu-south-1`
  - `us-west-1`
  - `ap-southeast-1`
  - `me-south-1`

- [AWS::CloudWatch::CompositeAlarm](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html)
  - Now available to **ALL** regions.

- [AWS::Kendra::DataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html)
  - `ap-southeast-1`

- [AWS::Kendra::Faq](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html)
  - `ap-southeast-1`

- [AWS::Kendra::Index](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html)
  - `ap-southeast-1`

- [AWS::NetworkFirewall::Firewall](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::FirewallPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::WAFv2::IPSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RegexPatternSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACLAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html)
  - Now available to **ALL** regions.

- [AWS::ACMPCA::Certificate.ApiPassthrough](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-apipassthrough.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::Certificate.EdiPartyName](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-edipartyname.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::Certificate.ExtendedKeyUsage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extendedkeyusage.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::Certificate.Extensions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extensions.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::Certificate.GeneralName](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::Certificate.KeyUsage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::Certificate.OtherName](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-othername.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::Certificate.PolicyInformation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyinformation.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::Certificate.PolicyQualifierInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyqualifierinfo.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::Certificate.Qualifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-qualifier.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::Certificate.Subject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::Certificate.Validity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-validity.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::CertificateAuthority.AccessDescription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessdescription.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::CertificateAuthority.AccessMethod](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessmethod.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::CertificateAuthority.CrlConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::CertificateAuthority.CsrExtensions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-csrextensions.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::CertificateAuthority.EdiPartyName](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-edipartyname.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::CertificateAuthority.GeneralName](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::CertificateAuthority.KeyUsage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::CertificateAuthority.OtherName](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-othername.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::CertificateAuthority.RevocationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-revocationconfiguration.html)
  - `ap-northeast-3`

- [AWS::ACMPCA::CertificateAuthority.Subject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html)
  - `ap-northeast-3`

- [AWS::Athena::WorkGroup.EngineVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-engineversion.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::CloudFront::Function.FunctionConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-function-functionconfig.html)
  - `us-east-2`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `af-south-1`
  - `eu-west-3`
  - `eu-central-1`
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-south-1`
  - `ap-east-1`
  - `eu-west-1`
  - `eu-north-1`
  - `ca-central-1`
  - `eu-south-1`
  - `us-west-1`
  - `ap-southeast-1`
  - `me-south-1`

- [AWS::CloudFront::Function.FunctionMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-function-functionmetadata.html)
  - `us-east-2`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `af-south-1`
  - `eu-west-3`
  - `eu-central-1`
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-south-1`
  - `ap-east-1`
  - `eu-west-1`
  - `eu-north-1`
  - `ca-central-1`
  - `eu-south-1`
  - `us-west-1`
  - `ap-southeast-1`
  - `me-south-1`

- [AWS::EKS::Nodegroup.Taint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-taint.html)
  - Now available to **ALL** regions.

- [AWS::Kendra::DataSource.AccessControlListConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-accesscontrollistconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.AclConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-aclconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.ColumnConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.ConfluenceAttachmentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmentconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.ConfluenceAttachmentToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmenttoindexfieldmapping.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.ConfluenceBlogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.ConfluenceBlogToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogtoindexfieldmapping.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.ConfluenceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.ConfluencePageConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepageconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.ConfluencePageToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagetoindexfieldmapping.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.ConfluenceSpaceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.ConfluenceSpaceToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.ConnectionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.DataSourceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.DataSourceToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmapping.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.DataSourceVpcConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcevpcconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.DatabaseConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.DocumentsMetadataConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentsmetadataconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.GoogleDriveConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.OneDriveConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.OneDriveUsers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveusers.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.S3DataSourceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.S3Path](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3path.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.SalesforceChatterFeedConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.SalesforceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.SalesforceCustomKnowledgeArticleTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.SalesforceKnowledgeArticleConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.SalesforceStandardKnowledgeArticleTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.SalesforceStandardObjectAttachmentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.SalesforceStandardObjectConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.ServiceNowConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.ServiceNowKnowledgeArticleConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.ServiceNowServiceCatalogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.SharePointConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::DataSource.SqlConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sqlconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::Faq.S3Path](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-faq-s3path.html)
  - `ap-southeast-1`

- [AWS::Kendra::Index.CapacityUnitsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-capacityunitsconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::Index.DocumentMetadataConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::Index.JsonTokenTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jsontokentypeconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::Index.JwtTokenTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::Index.Relevance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html)
  - `ap-southeast-1`

- [AWS::Kendra::Index.Search](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html)
  - `ap-southeast-1`

- [AWS::Kendra::Index.ServerSideEncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-serversideencryptionconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::Index.UserTokenConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-usertokenconfiguration.html)
  - `ap-southeast-1`

- [AWS::Kendra::Index.ValueImportanceItem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-valueimportanceitem.html)
  - `ap-southeast-1`

- [AWS::NetworkFirewall::Firewall.SubnetMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewall-subnetmapping.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::FirewallPolicy.ActionDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-actiondefinition.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::FirewallPolicy.CustomAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customaction.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::FirewallPolicy.Dimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-dimension.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::FirewallPolicy.FirewallPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::FirewallPolicy.PublishMetricAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-publishmetricaction.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::FirewallPolicy.StatefulRuleGroupReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::FirewallPolicy.StatelessRuleGroupReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::LoggingConfiguration.LogDestinationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::LoggingConfiguration.LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-loggingconfiguration.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.ActionDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-actiondefinition.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.Address](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-address.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.CustomAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customaction.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.Dimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-dimension.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.Header](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.IPSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipset.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.MatchAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.PortRange](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portrange.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.PortSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portset.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.PublishMetricAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-publishmetricaction.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.RuleDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruledefinition.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.RuleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.RuleOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoption.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.RuleVariables](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulevariables.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.RulesSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.RulesSourceList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.StatefulRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.StatelessRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrule.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.StatelessRulesAndCustomActions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::NetworkFirewall::RuleGroup.TCPFlagField](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflagfield.html)
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`

- [AWS::WAFv2::RuleGroup.AndStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-andstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.ByteMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.CustomResponseBody](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customresponsebody.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.FieldToMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.ForwardedIPConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-forwardedipconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.GeoMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-geomatchstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.IPSetForwardedIPConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.IPSetReferenceStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.JsonBody](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonbody.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.JsonMatchPattern](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonmatchpattern.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.Label](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-label.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.LabelMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelmatchstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.LabelSummary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelsummary.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.NotStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-notstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.OrStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-orstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.RateBasedStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.RegexPatternSetReferenceStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.RuleAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.SizeConstraintStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.SqliMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sqlimatchstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.Statement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.TextTransformation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-texttransformation.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.VisibilityConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::RuleGroup.XssMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-xssmatchstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.AllowAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-allowaction.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.AndStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-andstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.BlockAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-blockaction.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.ByteMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.CountAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-countaction.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.CustomHTTPHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customhttpheader.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.CustomRequestHandling](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customrequesthandling.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.CustomResponse](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponse.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.CustomResponseBody](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponsebody.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.DefaultAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-defaultaction.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.ExcludedRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-excludedrule.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.FieldToMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.ForwardedIPConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-forwardedipconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.GeoMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-geomatchstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.IPSetForwardedIPConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.IPSetReferenceStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.JsonBody](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonbody.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.JsonMatchPattern](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonmatchpattern.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.Label](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-label.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.LabelMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-labelmatchstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.ManagedRuleGroupStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.NotStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.OrStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-orstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.OverrideAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-overrideaction.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.RateBasedStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.RegexPatternSetReferenceStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.RuleAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.RuleGroupReferenceStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rulegroupreferencestatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.SizeConstraintStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.SqliMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sqlimatchstatement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.Statement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.TextTransformation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformation.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.VisibilityConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html)
  - Now available to **ALL** regions.

- [AWS::WAFv2::WebACL.XssMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-xssmatchstatement.html)
  - Now available to **ALL** regions.

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v35.2.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v35.2.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::MediaPackage::Channel.LogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-logconfiguration.html)
    - `eu-central-1`

  - [AWS::MediaPackage::PackagingGroup.LogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-logconfiguration.html)
    - `eu-central-1`

