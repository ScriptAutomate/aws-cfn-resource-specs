# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v81-changelog.json`](changelogs/v81-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [81.1.0](#8110-2022-07-24)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)
- [81.0.0](#8100-2022-07-17)
  - [Totals](#totals-1)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-1)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-1)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-1)

## [81.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v81.1.0) (2022-07-24)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v81-changelog.json)
  - Change source is a diff between [v81.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v81.1.0) and [v81.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v81.0.0)

### Totals

- TotalPropertyTypes: 3264 **(+4)**
- TotalPropertyTypesSupportedGlobally: 1133 **(+0)**
- TotalResourceTypes: 947 **(+1)**
- TotalResourceTypesSupportedGlobally: 344 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::Evidently::Segment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::RDS::DBCluster.ReadEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-readendpoint.html)
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::RDS::DBInstance.Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-endpoint.html)
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::SSO::PermissionSet.CustomerManagedPolicyReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-customermanagedpolicyreference.html)
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::SSO::PermissionSet.PermissionsBoundary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-permissionsboundary.html)
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::CloudTrail::EventDataStore](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html)
  - `us-east-2`
  - `ca-central-1`
  - `eu-west-2`
  - `us-west-1`

- [AWS::ElastiCache::GlobalReplicationGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::Lambda::Url](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.html)
  - `cn-north-1`

- [AWS::NetworkManager::ConnectAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html)
  - `us-east-2`
  - `eu-west-2`
  - `eu-west-3`
  - `ca-central-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `eu-south-1`

- [AWS::NetworkManager::ConnectPeer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html)
  - `us-east-2`
  - `eu-west-2`
  - `eu-west-3`
  - `ca-central-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `eu-south-1`

- [AWS::NetworkManager::CoreNetwork](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html)
  - `us-east-2`
  - `eu-west-2`
  - `eu-west-3`
  - `ca-central-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `eu-south-1`

- [AWS::NetworkManager::SiteToSiteVpnAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html)
  - `us-east-2`
  - `eu-west-2`
  - `eu-west-3`
  - `ca-central-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `eu-south-1`

- [AWS::NetworkManager::VpcAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html)
  - `us-east-2`
  - `eu-west-2`
  - `eu-west-3`
  - `ca-central-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `eu-south-1`

- [AWS::CloudTrail::EventDataStore.AdvancedEventSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedeventselector.html)
  - `us-east-2`
  - `ca-central-1`
  - `eu-west-2`
  - `us-west-1`

- [AWS::CloudTrail::EventDataStore.AdvancedFieldSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html)
  - `us-east-2`
  - `ca-central-1`
  - `eu-west-2`
  - `us-west-1`

- [AWS::ElastiCache::GlobalReplicationGroup.GlobalReplicationGroupMember](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-globalreplicationgroupmember.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::ElastiCache::GlobalReplicationGroup.RegionalConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-regionalconfiguration.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::ElastiCache::GlobalReplicationGroup.ReshardingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-reshardingconfiguration.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::Lambda::Url.Cors](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.html)
  - `cn-north-1`

- [AWS::NetworkManager::ConnectAttachment.ConnectAttachmentOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectattachment-connectattachmentoptions.html)
  - `us-east-2`
  - `eu-west-2`
  - `eu-west-3`
  - `ca-central-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `eu-south-1`

- [AWS::NetworkManager::ConnectPeer.BgpOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-bgpoptions.html)
  - `us-east-2`
  - `eu-west-2`
  - `eu-west-3`
  - `ca-central-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `eu-south-1`

- [AWS::NetworkManager::CoreNetwork.CoreNetworkEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworkedge.html)
  - `us-east-2`
  - `eu-west-2`
  - `eu-west-3`
  - `ca-central-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `eu-south-1`

- [AWS::NetworkManager::CoreNetwork.CoreNetworkSegment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworksegment.html)
  - `us-east-2`
  - `eu-west-2`
  - `eu-west-3`
  - `ca-central-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `eu-south-1`

- [AWS::NetworkManager::VpcAttachment.VpcOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-vpcoptions.html)
  - `us-east-2`
  - `eu-west-2`
  - `eu-west-3`
  - `ca-central-1`
  - `us-west-2`
  - `me-south-1`
  - `eu-north-1`
  - `eu-south-1`

- [AWS::SageMaker::NotebookInstance.InstanceMetadataServiceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-notebookinstance-instancemetadataserviceconfiguration.html)
  - `me-south-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `af-south-1`
  - `ap-northeast-2`
  - `eu-north-1`
  - `us-gov-west-1`
  - `ap-east-1`
  - `eu-south-1`

- [AWS::SageMaker::Workteam.OidcMemberDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-oidcmemberdefinition.html)
  - `me-south-1`
  - `eu-west-3`
  - `cn-northwest-1`
  - `af-south-1`
  - `ap-northeast-2`
  - `eu-north-1`
  - `us-gov-west-1`
  - `ap-east-1`
  - `eu-south-1`

- [AWS::Transfer::Server.As2Transport](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-as2transport.html)
  - `eu-west-2`
  - `ap-southeast-2`
  - `eu-west-3`
  - `eu-central-1`
  - `sa-east-1`
  - `af-south-1`
  - `ca-central-1`
  - `us-east-1`
  - `me-south-1`
  - `ap-northeast-3`
  - `us-gov-west-1`
  - `us-west-1`
  - `eu-west-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `us-west-2`
  - `us-gov-east-1`
  - `eu-north-1`
  - `ap-east-1`
  - `ap-southeast-1`
  - `eu-south-1`
  - `ap-northeast-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v81.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v81.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v81.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v81.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v81.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v81.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

  - Since v81.0.0: [AWS::Synthetics::Group](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-group.html)
    - `eu-central-1`

- PropertyType Still Missing
  - Since v81.0.0: [AWS::Config::OrganizationConfigRule.OrganizationCustomPolicyRuleMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html)
    - `me-south-1`

  - Since v81.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v81.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v81.0.0: [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v81.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v81.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::RDS::DBCluster.ReadEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-readendpoint.html)
    - `ap-northeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::RDS::DBInstance.Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-endpoint.html)
    - `ap-northeast-1`
    - `eu-central-1`
    - `us-west-2`

## [81.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v81.0.0) (2022-07-17)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v81-changelog.json)
  - Change source is a diff between [v81.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v81.0.0) and [v79.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v79.0.0)

### Totals

- TotalPropertyTypes: 3260 **(+4)**
- TotalPropertyTypesSupportedGlobally: 1133 **(+1)**
- TotalResourceTypes: 946 **(+2)**
- TotalResourceTypesSupportedGlobally: 344 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::RolesAnywhere::CRL](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-crl.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Synthetics::Group](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-group.html)
  - `eu-central-1`

- [AWS::Config::ConfigRule.CustomPolicyDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-custompolicydetails.html)
  - Available in **ALL** regions.

- [AWS::Config::OrganizationConfigRule.OrganizationCustomPolicyRuleMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html)
  - `me-south-1`

- [AWS::Evidently::Launch.SegmentOverride](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-segmentoverride.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Transfer::Server.As2Transport](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-as2transport.html)
  - `us-east-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::CE::AnomalyMonitor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html)
  - `cn-northwest-1`

- [AWS::CE::AnomalySubscription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html)
  - `cn-northwest-1`

- [AWS::CloudTrail::EventDataStore](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html)
  - `sa-east-1`
  - `ap-southeast-2`
  - `ap-south-1`
  - `eu-west-1`

- [AWS::CE::AnomalyMonitor.ResourceTag](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalymonitor-resourcetag.html)
  - `cn-northwest-1`

- [AWS::CE::AnomalySubscription.ResourceTag](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-resourcetag.html)
  - `cn-northwest-1`

- [AWS::CE::AnomalySubscription.Subscriber](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-subscriber.html)
  - `cn-northwest-1`

- [AWS::CloudTrail::EventDataStore.AdvancedEventSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedeventselector.html)
  - `sa-east-1`
  - `ap-southeast-2`
  - `ap-south-1`
  - `eu-west-1`

- [AWS::CloudTrail::EventDataStore.AdvancedFieldSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html)
  - `sa-east-1`
  - `ap-southeast-2`
  - `ap-south-1`
  - `eu-west-1`

- [AWS::Logs::MetricFilter.Dimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-dimension.html)
  - `ap-northeast-2`
  - `eu-south-1`
  - `us-west-1`
  - `ca-central-1`
  - `eu-west-3`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-east-1`
  - `ap-southeast-2`
  - `me-south-1`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-2`
  - `af-south-1`
  - `eu-north-1`

- [AWS::SageMaker::NotebookInstance.InstanceMetadataServiceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-notebookinstance-instancemetadataserviceconfiguration.html)
  - `ap-southeast-1`
  - `us-west-1`
  - `ca-central-1`
  - `us-east-1`
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-southeast-2`
  - `ap-south-1`
  - `us-east-2`
  - `eu-west-2`
  - `ap-northeast-1`
  - `eu-west-1`

- [AWS::SageMaker::Workteam.OidcMemberDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-oidcmemberdefinition.html)
  - `ap-southeast-1`
  - `us-west-1`
  - `ca-central-1`
  - `us-east-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `ap-south-1`
  - `us-east-2`
  - `eu-west-2`
  - `ap-northeast-1`
  - `eu-west-1`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::AppStream::Stack.StreamingExperienceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-streamingexperiencesettings.html)
  - `eu-central-1`

- [AWS::Config::OrganizationConfigRule.OrganizationCustomCodeRuleMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomcoderulemetadata.html)
  - `me-south-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v79.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v79.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v79.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v79.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v79.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v79.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- New ResourceType(s) Missing
  - [AWS::Synthetics::Group](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-group.html)
    - `eu-central-1`

- PropertyType Still Missing
  - Since v79.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v79.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v79.0.0: [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v79.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v79.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::Config::OrganizationConfigRule.OrganizationCustomPolicyRuleMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html)
    - `me-south-1`

  - [AWS::Transfer::Server.As2Transport](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-as2transport.html)
    - `us-east-2`

