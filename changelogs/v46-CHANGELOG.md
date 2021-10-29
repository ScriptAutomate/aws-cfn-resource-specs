# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v46-changelog.json`](changelogs/v46-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [46.0.0](#4600-2021-10-29)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [46.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v46.0.0) (2021-10-29)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v46-changelog.json)
  - Change source is a diff between [v46.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v46.0.0) and [v45.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v45.0.0)

### Totals

- TotalPropertyTypes: 2711 **(+22)**
- TotalPropertyTypesSupportedGlobally: 990 **(+26)**
- TotalResourceTypes: 823 **(+4)**
- TotalResourceTypesSupportedGlobally: 329 **(+1)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::EC2::CapacityReservationFleet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservationfleet.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::Lightsail::Database](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html)
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
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Lightsail::StaticIp](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html)
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
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Route53Resolver::ResolverConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverconfig.html)
  - Available in **ALL** regions.

- [AWS::AppFlow::ConnectorProfile.OAuthProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthproperties.html)
  - `ap-southeast-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppFlow::ConnectorProfile.SAPODataConnectorProfileCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofilecredentials.html)
  - `ap-southeast-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppFlow::ConnectorProfile.SAPODataConnectorProfileProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html)
  - `ap-southeast-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppFlow::Flow.S3InputFormatConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3inputformatconfig.html)
  - `ap-southeast-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppFlow::Flow.SAPODataSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatasourceproperties.html)
  - `ap-southeast-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::AutoScaling::AutoScalingGroup.AcceleratorCountRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-acceleratorcountrequest.html)
  - Available in **ALL** regions.

- [AWS::AutoScaling::AutoScalingGroup.AcceleratorTotalMemoryMiBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-acceleratortotalmemorymibrequest.html)
  - Available in **ALL** regions.

- [AWS::AutoScaling::AutoScalingGroup.BaselineEbsBandwidthMbpsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-baselineebsbandwidthmbpsrequest.html)
  - Available in **ALL** regions.

- [AWS::AutoScaling::AutoScalingGroup.InstanceRequirements](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-as-mixedinstancespolicy-instancerequirements.html)
  - Available in **ALL** regions.

- [AWS::AutoScaling::AutoScalingGroup.MemoryGiBPerVCpuRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-memorygibpervcpurequest.html)
  - Available in **ALL** regions.

- [AWS::AutoScaling::AutoScalingGroup.MemoryMiBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-memorymibrequest.html)
  - Available in **ALL** regions.

- [AWS::AutoScaling::AutoScalingGroup.NetworkInterfaceCountRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-networkinterfacecountrequest.html)
  - Available in **ALL** regions.

- [AWS::AutoScaling::AutoScalingGroup.TotalLocalStorageGBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-totallocalstoragegbrequest.html)
  - Available in **ALL** regions.

- [AWS::AutoScaling::AutoScalingGroup.VCpuCountRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-vcpucountrequest.html)
  - Available in **ALL** regions.

- [AWS::EC2::CapacityReservationFleet.InstanceTypeSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservationfleet-instancetypespecification.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::EC2::CapacityReservationFleet.TagSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservationfleet-tagspecification.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::EKS::Cluster.ClusterLogging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-clusterlogging.html)
  - `eu-central-1`

- [AWS::EKS::Cluster.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-logging.html)
  - `eu-central-1`

- [AWS::EKS::Cluster.LoggingTypeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-loggingtypeconfig.html)
  - `eu-central-1`

- [AWS::Lightsail::Database.RelationalDatabaseParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html)
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
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.StatefulEngineOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulengineoptions.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.StatefulRuleOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulruleoptions.html)
  - `ap-southeast-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::IoTEvents::DetectorModel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html)
  - `ap-south-1`

- [AWS::IoTEvents::Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html)
  - `ap-south-1`

- [AWS::Backup::BackupVault.LockConfigurationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html)
  - `us-gov-west-1`
  - `cn-north-1`
  - `us-gov-east-1`

- [AWS::DMS::Endpoint.RedisSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html)
  - `us-east-2`
  - `us-west-2`
  - `eu-west-3`
  - `ap-south-1`
  - `ap-northeast-1`
  - `eu-west-2`
  - `cn-north-1`

- [AWS::EC2::EC2Fleet.AcceleratorCountRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-acceleratorcountrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.AcceleratorTotalMemoryMiBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-acceleratortotalmemorymibrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.BaselineEbsBandwidthMbpsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-baselineebsbandwidthmbpsrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.InstanceRequirementsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.MemoryGiBPerVCpuRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-memorygibpervcpurequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.MemoryMiBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-memorymibrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.NetworkInterfaceCountRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-networkinterfacecountrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.TotalLocalStorageGBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-totallocalstoragegbrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.VCpuCountRangeRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-vcpucountrangerequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::SpotFleet.AcceleratorCountRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-acceleratorcountrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::SpotFleet.AcceleratorTotalMemoryMiBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-acceleratortotalmemorymibrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::SpotFleet.BaselineEbsBandwidthMbpsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-baselineebsbandwidthmbpsrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::SpotFleet.InstanceRequirementsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::SpotFleet.MemoryGiBPerVCpuRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-memorygibpervcpurequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::SpotFleet.MemoryMiBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-memorymibrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::SpotFleet.NetworkInterfaceCountRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-networkinterfacecountrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::SpotFleet.TotalLocalStorageGBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-totallocalstoragegbrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::SpotFleet.VCpuCountRangeRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-vcpucountrangerequest.html)
  - Now available to **ALL** regions.

- [AWS::IoTEvents::DetectorModel.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.AssetPropertyTimestamp](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertytimestamp.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.AssetPropertyValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvalue.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.AssetPropertyVariant](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.ClearTimer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-cleartimer.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.DetectorModelDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-detectormodeldefinition.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.DynamoDB](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.DynamoDBv2](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodbv2.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.Event](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-event.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.Firehose](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-firehose.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.IotEvents](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotevents.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.IotSiteWise](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.IotTopicPublish](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iottopicpublish.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.Lambda](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-lambda.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.OnEnter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onenter.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.OnExit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onexit.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.OnInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-oninput.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.Payload](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-payload.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.ResetTimer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-resettimer.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.SetTimer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-settimer.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.SetVariable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-setvariable.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.Sns](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sns.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.Sqs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sqs.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.State](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html)
  - `ap-south-1`

- [AWS::IoTEvents::DetectorModel.TransitionEvent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html)
  - `ap-south-1`

- [AWS::IoTEvents::Input.Attribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-attribute.html)
  - `ap-south-1`

- [AWS::IoTEvents::Input.InputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-inputdefinition.html)
  - `ap-south-1`

- [AWS::Pinpoint::Campaign.CampaignInAppMessage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigninappmessage.html)
  - `ap-northeast-2`
  - `us-east-1`
  - `us-west-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `eu-central-1`
  - `ap-south-1`
  - `ap-northeast-1`
  - `us-gov-west-1`
  - `eu-west-2`
  - `ca-central-1`

- [AWS::Pinpoint::Campaign.DefaultButtonConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html)
  - `ap-northeast-2`
  - `us-east-1`
  - `us-west-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `eu-central-1`
  - `ap-south-1`
  - `ap-northeast-1`
  - `us-gov-west-1`
  - `eu-west-2`
  - `ca-central-1`

- [AWS::Pinpoint::Campaign.InAppMessageBodyConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebodyconfig.html)
  - `ap-northeast-2`
  - `us-east-1`
  - `us-west-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `eu-central-1`
  - `ap-south-1`
  - `ap-northeast-1`
  - `us-gov-west-1`
  - `eu-west-2`
  - `ca-central-1`

- [AWS::Pinpoint::Campaign.InAppMessageButton](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html)
  - `ap-northeast-2`
  - `us-east-1`
  - `us-west-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `eu-central-1`
  - `ap-south-1`
  - `ap-northeast-1`
  - `us-gov-west-1`
  - `eu-west-2`
  - `ca-central-1`

- [AWS::Pinpoint::Campaign.InAppMessageContent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html)
  - `ap-northeast-2`
  - `us-east-1`
  - `us-west-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `eu-central-1`
  - `ap-south-1`
  - `ap-northeast-1`
  - `us-gov-west-1`
  - `eu-west-2`
  - `ca-central-1`

- [AWS::Pinpoint::Campaign.InAppMessageHeaderConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessageheaderconfig.html)
  - `ap-northeast-2`
  - `us-east-1`
  - `us-west-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `eu-central-1`
  - `ap-south-1`
  - `ap-northeast-1`
  - `us-gov-west-1`
  - `eu-west-2`
  - `ca-central-1`

- [AWS::Pinpoint::Campaign.OverrideButtonConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-overridebuttonconfiguration.html)
  - `ap-northeast-2`
  - `us-east-1`
  - `us-west-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `eu-central-1`
  - `ap-south-1`
  - `ap-northeast-1`
  - `us-gov-west-1`
  - `eu-west-2`
  - `ca-central-1`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::EKS::Cluster.Provider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-provider.html)
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v45.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v45.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v45.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v45.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v45.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v45.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- PropertyType Still Missing
  - Since v45.0.0: [AWS::DMS::Endpoint.RedisSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html)
    - `ap-northeast-1`
    - `ap-northeast-2`
    - `ap-south-1`
    - `ap-southeast-2`
    - `ca-central-1`
    - `cn-north-1`
    - `eu-central-1`
    - `eu-west-2`
    - `eu-west-3`
    - `us-east-2`
    - `us-west-2`

  - Since v45.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v45.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v45.0.0: [AWS::MediaLive::Channel.AudioHlsRenditionSelection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiohlsrenditionselection.html)
    - `ap-northeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `sa-east-1`

  - Since v45.0.0: [AWS::MediaLive::Channel.AudioWatermarkSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiowatermarksettings.html)
    - `ap-northeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `sa-east-1`

  - Since v45.0.0: [AWS::MediaLive::Channel.NielsenCBET](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsencbet.html)
    - `ap-northeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `sa-east-1`

  - Since v45.0.0: [AWS::MediaLive::Channel.NielsenNaesIiNw](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsennaesiinw.html)
    - `ap-northeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `sa-east-1`

  - Since v45.0.0: [AWS::MediaLive::Channel.NielsenWatermarksSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenwatermarkssettings.html)
    - `ap-northeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `sa-east-1`

  - Since v45.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v45.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v45.0.0: [AWS::SageMaker::DataQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v45.0.0: [AWS::SageMaker::ModelBiasJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-environment.html)
    - `eu-west-3`

  - Since v45.0.0: [AWS::SageMaker::ModelExplainabilityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v45.0.0: [AWS::SageMaker::ModelQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v45.0.0: [AWS::SageMaker::MonitoringSchedule.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-environment.html)
    - `cn-northwest-1`
    - `eu-west-3`

- New PropertyType(s) Missing
  - [AWS::EKS::Cluster.ClusterLogging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-clusterlogging.html)
    - `eu-central-1`

  - [AWS::EKS::Cluster.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-logging.html)
    - `eu-central-1`

  - [AWS::EKS::Cluster.LoggingTypeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-loggingtypeconfig.html)
    - `eu-central-1`

  - [AWS::NetworkFirewall::FirewallPolicy.StatefulEngineOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulengineoptions.html)
    - `ap-southeast-2`

  - [AWS::NetworkFirewall::RuleGroup.StatefulRuleOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulruleoptions.html)
    - `ap-southeast-2`

