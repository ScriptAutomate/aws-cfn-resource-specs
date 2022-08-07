# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v83-changelog.json`](changelogs/v83-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [83.0.0](#8300-2022-08-07)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [83.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v83.0.0) (2022-08-07)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v83-changelog.json)
  - Change source is a diff between [v83.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v83.0.0) and [v81.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v81.1.0)

### Totals

- TotalPropertyTypes: 3275 **(+11)**
- TotalPropertyTypesSupportedGlobally: 1133 **(+0)**
- TotalResourceTypes: 948 **(+1)**
- TotalResourceTypesSupportedGlobally: 344 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::MSK::ServerlessCluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html)
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::FMS::Policy.NetworkFirewallPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::FMS::Policy.PolicyOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policyoption.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::FMS::Policy.SecurityServicePolicyData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-securityservicepolicydata.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::FMS::Policy.ThirdPartyFirewallPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::GuardDuty::Detector.CFNMalwareProtectionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnmalwareprotectionconfiguration.html)
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

- [AWS::GuardDuty::Detector.CFNScanEc2InstanceWithFindingsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfnscanec2instancewithfindingsconfiguration.html)
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

- [AWS::IoT::CACertificate.RegistrationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-cacertificate-registrationconfig.html)
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
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::MSK::ServerlessCluster.ClientAuthentication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-clientauthentication.html)
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::MSK::ServerlessCluster.Iam](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-iam.html)
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::MSK::ServerlessCluster.Sasl](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-sasl.html)
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::MSK::ServerlessCluster.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-vpcconfig.html)
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::CloudTrail::EventDataStore](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html)
  - `eu-north-1`
  - `eu-west-3`
  - `eu-south-1`
  - `af-south-1`
  - `ap-northeast-2`

- [AWS::FIS::ExperimentTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::Synthetics::Group](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-group.html)
  - `ap-southeast-2`
  - `eu-west-1`
  - `ap-southeast-1`
  - `us-west-2`
  - `us-east-1`
  - `ap-south-1`
  - `ap-northeast-1`

- [AWS::XRay::Group](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-group.html)
  - `ap-northeast-3`

- [AWS::XRay::SamplingRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-samplingrule.html)
  - `ap-northeast-3`

- [AWS::CloudTrail::EventDataStore.AdvancedEventSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedeventselector.html)
  - `eu-north-1`
  - `eu-west-3`
  - `eu-south-1`
  - `af-south-1`
  - `ap-northeast-2`

- [AWS::CloudTrail::EventDataStore.AdvancedFieldSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html)
  - `eu-north-1`
  - `eu-west-3`
  - `eu-south-1`
  - `af-south-1`
  - `ap-northeast-2`

- [AWS::FIS::ExperimentTemplate.ExperimentTemplateAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::FIS::ExperimentTemplate.ExperimentTemplateLogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatelogconfiguration.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::FIS::ExperimentTemplate.ExperimentTemplateStopCondition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatestopcondition.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::FIS::ExperimentTemplate.ExperimentTemplateTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::FIS::ExperimentTemplate.ExperimentTemplateTargetFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::SSO::PermissionSet.CustomerManagedPolicyReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-customermanagedpolicyreference.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-gov-east-1`

- [AWS::SSO::PermissionSet.PermissionsBoundary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-permissionsboundary.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-gov-east-1`

- [AWS::XRay::Group.InsightsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-group-insightsconfiguration.html)
  - `ap-northeast-3`

- [AWS::XRay::SamplingRule.SamplingRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrule.html)
  - `ap-northeast-3`

- [AWS::XRay::SamplingRule.SamplingRuleRecord](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingrulerecord.html)
  - `ap-northeast-3`

- [AWS::XRay::SamplingRule.SamplingRuleUpdate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-xray-samplingrule-samplingruleupdate.html)
  - `ap-northeast-3`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::RDS::DBCluster.ReadEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-readendpoint.html)
  - `ap-northeast-1`
  - `us-west-2`

- [AWS::RDS::DBInstance.Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-endpoint.html)
  - `ap-northeast-1`
  - `us-west-2`

- [AWS::Redshift::ScheduledAction.PauseClusterMessage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-pauseclustermessage.html)
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-west-2`

- [AWS::Redshift::ScheduledAction.ResizeClusterMessage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resizeclustermessage.html)
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-west-2`

- [AWS::Redshift::ScheduledAction.ResumeClusterMessage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resumeclustermessage.html)
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v81.1.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v81.1.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v81.1.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v81.1.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v81.1.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v81.1.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- New ResourceType(s) Missing
  - [AWS::MSK::ServerlessCluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html)
    - `ap-northeast-1`
    - `eu-central-1`
    - `us-west-2`

- PropertyType Still Missing
  - Since v81.1.0: [AWS::Config::OrganizationConfigRule.OrganizationCustomPolicyRuleMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html)
    - `me-south-1`

  - Since v81.1.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v81.1.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v81.1.0: [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v81.1.0: [AWS::RDS::DBCluster.ReadEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-readendpoint.html)
    - `eu-central-1`

  - Since v81.1.0: [AWS::RDS::DBInstance.Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-endpoint.html)
    - `eu-central-1`

  - Since v81.1.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v81.1.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::FMS::Policy.NetworkFirewallPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html)
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::FMS::Policy.PolicyOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policyoption.html)
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::FMS::Policy.SecurityServicePolicyData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-securityservicepolicydata.html)
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::FMS::Policy.ThirdPartyFirewallPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html)
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::MSK::ServerlessCluster.ClientAuthentication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-clientauthentication.html)
    - `ap-northeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::MSK::ServerlessCluster.Iam](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-iam.html)
    - `ap-northeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::MSK::ServerlessCluster.Sasl](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-sasl.html)
    - `ap-northeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::MSK::ServerlessCluster.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-vpcconfig.html)
    - `ap-northeast-1`
    - `eu-central-1`
    - `us-west-2`

