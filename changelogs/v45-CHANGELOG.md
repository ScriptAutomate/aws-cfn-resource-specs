# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v45-changelog.json`](changelogs/v45-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [45.0.0](#4500-2021-10-22)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [45.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v45.0.0) (2021-10-22)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v45-changelog.json)
  - Change source is a diff between [v45.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v45.0.0) and [v44.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v44.0.0)

### Totals

- TotalPropertyTypes: 2689 **(+30)**
- TotalPropertyTypesSupportedGlobally: 964 **(+14)**
- TotalResourceTypes: 819 **(+7)**
- TotalResourceTypesSupportedGlobally: 328 **(+1)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::Connect::HoursOfOperation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::Connect::User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::Connect::UserHierarchyGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::Panorama::ApplicationInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html)
  - `ca-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Panorama::Package](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-package.html)
  - `ca-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Panorama::PackageVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html)
  - `ca-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Rekognition::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-project.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Connect::HoursOfOperation.HoursOfOperationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationconfig.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::Connect::HoursOfOperation.HoursOfOperationTimeSlice](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationtimeslice.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::Connect::User.UserIdentityInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::Connect::User.UserPhoneConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-gov-west-1`
  - `us-west-2`

- [AWS::DMS::Endpoint.RedisSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`

- [AWS::EC2::EC2Fleet.AcceleratorCountRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-acceleratorcountrequest.html)
  - `eu-central-1`

- [AWS::EC2::EC2Fleet.AcceleratorTotalMemoryMiBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-acceleratortotalmemorymibrequest.html)
  - `eu-central-1`

- [AWS::EC2::EC2Fleet.BaselineEbsBandwidthMbpsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-baselineebsbandwidthmbpsrequest.html)
  - `eu-central-1`

- [AWS::EC2::EC2Fleet.InstanceRequirementsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html)
  - `eu-central-1`

- [AWS::EC2::EC2Fleet.MemoryGiBPerVCpuRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-memorygibpervcpurequest.html)
  - `eu-central-1`

- [AWS::EC2::EC2Fleet.MemoryMiBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-memorymibrequest.html)
  - `eu-central-1`

- [AWS::EC2::EC2Fleet.NetworkInterfaceCountRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-networkinterfacecountrequest.html)
  - `eu-central-1`

- [AWS::EC2::EC2Fleet.TotalLocalStorageGBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-totallocalstoragegbrequest.html)
  - `eu-central-1`

- [AWS::EC2::EC2Fleet.VCpuCountRangeRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-vcpucountrangerequest.html)
  - `eu-central-1`

- [AWS::EC2::SpotFleet.AcceleratorCountRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-acceleratorcountrequest.html)
  - `eu-central-1`

- [AWS::EC2::SpotFleet.AcceleratorTotalMemoryMiBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-acceleratortotalmemorymibrequest.html)
  - `eu-central-1`

- [AWS::EC2::SpotFleet.BaselineEbsBandwidthMbpsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-baselineebsbandwidthmbpsrequest.html)
  - `eu-central-1`

- [AWS::EC2::SpotFleet.InstanceRequirementsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html)
  - `eu-central-1`

- [AWS::EC2::SpotFleet.MemoryGiBPerVCpuRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-memorygibpervcpurequest.html)
  - `eu-central-1`

- [AWS::EC2::SpotFleet.MemoryMiBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-memorymibrequest.html)
  - `eu-central-1`

- [AWS::EC2::SpotFleet.NetworkInterfaceCountRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-networkinterfacecountrequest.html)
  - `eu-central-1`

- [AWS::EC2::SpotFleet.TotalLocalStorageGBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-totallocalstoragegbrequest.html)
  - `eu-central-1`

- [AWS::EC2::SpotFleet.VCpuCountRangeRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-vcpucountrangerequest.html)
  - `eu-central-1`

- [AWS::ImageBuilder::InfrastructureConfiguration.InstanceMetadataOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-instancemetadataoptions.html)
  - Available in **ALL** regions.

- [AWS::Panorama::ApplicationInstance.ManifestOverridesPayload](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-applicationinstance-manifestoverridespayload.html)
  - `ca-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Panorama::ApplicationInstance.ManifestPayload](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-applicationinstance-manifestpayload.html)
  - `ca-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Pinpoint::Campaign.CampaignInAppMessage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigninappmessage.html)
  - `eu-west-1`

- [AWS::Pinpoint::Campaign.DefaultButtonConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html)
  - `eu-west-1`

- [AWS::Pinpoint::Campaign.InAppMessageBodyConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebodyconfig.html)
  - `eu-west-1`

- [AWS::Pinpoint::Campaign.InAppMessageButton](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html)
  - `eu-west-1`

- [AWS::Pinpoint::Campaign.InAppMessageContent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html)
  - `eu-west-1`

- [AWS::Pinpoint::Campaign.InAppMessageHeaderConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessageheaderconfig.html)
  - `eu-west-1`

- [AWS::Pinpoint::Campaign.OverrideButtonConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-overridebuttonconfiguration.html)
  - `eu-west-1`

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::MWAA::Environment.TagMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-tagmap.html)
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
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.StatefulEngineOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulengineoptions.html)
  - `ap-southeast-2`

- [AWS::NetworkFirewall::RuleGroup.StatefulRuleOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulruleoptions.html)
  - `ap-southeast-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::ApplicationInsights::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html)
  - Now available to **ALL** regions.

- [AWS::ApplicationInsights::Application.Alarm](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarm.html)
  - Now available to **ALL** regions.

- [AWS::ApplicationInsights::Application.AlarmMetric](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarmmetric.html)
  - Now available to **ALL** regions.

- [AWS::ApplicationInsights::Application.ComponentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::ApplicationInsights::Application.ComponentMonitoringSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html)
  - Now available to **ALL** regions.

- [AWS::ApplicationInsights::Application.ConfigurationDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html)
  - Now available to **ALL** regions.

- [AWS::ApplicationInsights::Application.CustomComponent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-customcomponent.html)
  - Now available to **ALL** regions.

- [AWS::ApplicationInsights::Application.JMXPrometheusExporter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html)
  - Now available to **ALL** regions.

- [AWS::ApplicationInsights::Application.Log](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html)
  - Now available to **ALL** regions.

- [AWS::ApplicationInsights::Application.LogPattern](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html)
  - Now available to **ALL** regions.

- [AWS::ApplicationInsights::Application.LogPatternSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpatternset.html)
  - Now available to **ALL** regions.

- [AWS::ApplicationInsights::Application.SubComponentConfigurationDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html)
  - Now available to **ALL** regions.

- [AWS::ApplicationInsights::Application.SubComponentTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponenttypeconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::ApplicationInsights::Application.WindowsEvent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html)
  - Now available to **ALL** regions.

- [AWS::MediaLive::Channel.AudioHlsRenditionSelection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiohlsrenditionselection.html)
  - `eu-west-3`
  - `eu-west-2`
  - `ap-northeast-2`
  - `eu-north-1`
  - `sa-east-1`

- [AWS::MediaLive::Channel.AudioWatermarkSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiowatermarksettings.html)
  - `eu-west-3`
  - `eu-west-2`
  - `ap-northeast-2`
  - `eu-north-1`
  - `sa-east-1`

- [AWS::MediaLive::Channel.NielsenCBET](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsencbet.html)
  - `eu-west-3`
  - `eu-west-2`
  - `ap-northeast-2`
  - `eu-north-1`
  - `sa-east-1`

- [AWS::MediaLive::Channel.NielsenNaesIiNw](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsennaesiinw.html)
  - `eu-west-3`
  - `eu-west-2`
  - `ap-northeast-2`
  - `eu-north-1`
  - `sa-east-1`

- [AWS::MediaLive::Channel.NielsenWatermarksSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenwatermarkssettings.html)
  - `eu-west-3`
  - `eu-west-2`
  - `ap-northeast-2`
  - `eu-north-1`
  - `sa-east-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v44.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v44.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v44.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v44.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v44.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v44.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- PropertyType Still Missing
  - Since v44.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v44.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v44.0.0: [AWS::MediaLive::Channel.AudioHlsRenditionSelection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiohlsrenditionselection.html)
    - `ap-northeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `sa-east-1`

  - Since v44.0.0: [AWS::MediaLive::Channel.AudioWatermarkSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiowatermarksettings.html)
    - `ap-northeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `sa-east-1`

  - Since v44.0.0: [AWS::MediaLive::Channel.NielsenCBET](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsencbet.html)
    - `ap-northeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `sa-east-1`

  - Since v44.0.0: [AWS::MediaLive::Channel.NielsenNaesIiNw](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsennaesiinw.html)
    - `ap-northeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `sa-east-1`

  - Since v44.0.0: [AWS::MediaLive::Channel.NielsenWatermarksSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenwatermarkssettings.html)
    - `ap-northeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-2`
    - `eu-west-3`
    - `sa-east-1`

  - Since v44.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v44.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v44.0.0: [AWS::SageMaker::DataQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v44.0.0: [AWS::SageMaker::ModelBiasJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-environment.html)
    - `eu-west-3`

  - Since v44.0.0: [AWS::SageMaker::ModelExplainabilityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v44.0.0: [AWS::SageMaker::ModelQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v44.0.0: [AWS::SageMaker::MonitoringSchedule.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-environment.html)
    - `cn-northwest-1`
    - `eu-west-3`

- New PropertyType(s) Missing
  - [AWS::DMS::Endpoint.RedisSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html)
    - `ap-northeast-2`
    - `ap-southeast-2`
    - `ca-central-1`
    - `eu-central-1`

  - [AWS::EC2::EC2Fleet.AcceleratorCountRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-acceleratorcountrequest.html)
    - `eu-central-1`

  - [AWS::EC2::EC2Fleet.AcceleratorTotalMemoryMiBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-acceleratortotalmemorymibrequest.html)
    - `eu-central-1`

  - [AWS::EC2::EC2Fleet.BaselineEbsBandwidthMbpsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-baselineebsbandwidthmbpsrequest.html)
    - `eu-central-1`

  - [AWS::EC2::EC2Fleet.InstanceRequirementsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-instancerequirementsrequest.html)
    - `eu-central-1`

  - [AWS::EC2::EC2Fleet.MemoryGiBPerVCpuRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-memorygibpervcpurequest.html)
    - `eu-central-1`

  - [AWS::EC2::EC2Fleet.MemoryMiBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-memorymibrequest.html)
    - `eu-central-1`

  - [AWS::EC2::EC2Fleet.NetworkInterfaceCountRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-networkinterfacecountrequest.html)
    - `eu-central-1`

  - [AWS::EC2::EC2Fleet.TotalLocalStorageGBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-totallocalstoragegbrequest.html)
    - `eu-central-1`

  - [AWS::EC2::EC2Fleet.VCpuCountRangeRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-vcpucountrangerequest.html)
    - `eu-central-1`

  - [AWS::EC2::SpotFleet.AcceleratorCountRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-acceleratorcountrequest.html)
    - `eu-central-1`

  - [AWS::EC2::SpotFleet.AcceleratorTotalMemoryMiBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-acceleratortotalmemorymibrequest.html)
    - `eu-central-1`

  - [AWS::EC2::SpotFleet.BaselineEbsBandwidthMbpsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-baselineebsbandwidthmbpsrequest.html)
    - `eu-central-1`

  - [AWS::EC2::SpotFleet.InstanceRequirementsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instancerequirementsrequest.html)
    - `eu-central-1`

  - [AWS::EC2::SpotFleet.MemoryGiBPerVCpuRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-memorygibpervcpurequest.html)
    - `eu-central-1`

  - [AWS::EC2::SpotFleet.MemoryMiBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-memorymibrequest.html)
    - `eu-central-1`

  - [AWS::EC2::SpotFleet.NetworkInterfaceCountRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-networkinterfacecountrequest.html)
    - `eu-central-1`

  - [AWS::EC2::SpotFleet.TotalLocalStorageGBRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-totallocalstoragegbrequest.html)
    - `eu-central-1`

  - [AWS::EC2::SpotFleet.VCpuCountRangeRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-vcpucountrangerequest.html)
    - `eu-central-1`

  - [AWS::Pinpoint::Campaign.CampaignInAppMessage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigninappmessage.html)
    - `eu-west-1`

  - [AWS::Pinpoint::Campaign.DefaultButtonConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-defaultbuttonconfiguration.html)
    - `eu-west-1`

  - [AWS::Pinpoint::Campaign.InAppMessageBodyConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebodyconfig.html)
    - `eu-west-1`

  - [AWS::Pinpoint::Campaign.InAppMessageButton](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagebutton.html)
    - `eu-west-1`

  - [AWS::Pinpoint::Campaign.InAppMessageContent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessagecontent.html)
    - `eu-west-1`

  - [AWS::Pinpoint::Campaign.InAppMessageHeaderConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-inappmessageheaderconfig.html)
    - `eu-west-1`

  - [AWS::Pinpoint::Campaign.OverrideButtonConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-overridebuttonconfiguration.html)
    - `eu-west-1`

