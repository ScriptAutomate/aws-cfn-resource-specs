# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v69-changelog.json`](changelogs/v69-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [69.0.0](#6900-2022-05-06)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [69.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v69.0.0) (2022-05-06)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v69-changelog.json)
  - Change source is a diff between [v69.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v69.0.0) and [v68.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v68.1.0)

### Totals

- TotalPropertyTypes: 3120 **(+18)**
- TotalPropertyTypesSupportedGlobally: 1085 **(+0)**
- TotalResourceTypes: 919 **(+2)**
- TotalResourceTypesSupportedGlobally: 340 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::Rekognition::StreamProcessor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::VoiceID::Domain](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-voiceid-domain.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Rekognition::StreamProcessor.BoundingBox](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Rekognition::StreamProcessor.ConnectedHomeSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-connectedhomesettings.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Rekognition::StreamProcessor.DataSharingPreference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-datasharingpreference.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Rekognition::StreamProcessor.FaceSearchSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-facesearchsettings.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Rekognition::StreamProcessor.KinesisDataStream](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-kinesisdatastream.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Rekognition::StreamProcessor.KinesisVideoStream](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-kinesisvideostream.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Rekognition::StreamProcessor.NotificationChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-notificationchannel.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Rekognition::StreamProcessor.Point](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-point.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Rekognition::StreamProcessor.S3Destination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-s3destination.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::VoiceID::Domain.ServerSideEncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-voiceid-domain-serversideencryptionconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::WAFv2::RuleGroup.Body](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-body.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::WAFv2::RuleGroup.CookieMatchPattern](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-cookiematchpattern.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::WAFv2::RuleGroup.Cookies](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-cookies.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::WAFv2::RuleGroup.HeaderMatchPattern](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-headermatchpattern.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::WAFv2::RuleGroup.Headers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-headers.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::WAFv2::WebACL.Body](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-body.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::WAFv2::WebACL.CookieMatchPattern](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-cookiematchpattern.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::WAFv2::WebACL.Cookies](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-cookies.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::WAFv2::WebACL.HeaderMatchPattern](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-headermatchpattern.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::WAFv2::WebACL.Headers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-headers.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::RDS::DBCluster.ReadEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-readendpoint.html)
  - `eu-central-1`

- [AWS::RDS::DBInstance.Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-endpoint.html)
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::AppIntegrations::DataIntegration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html)
  - `ap-northeast-2`
  - `af-south-1`

- [AWS::EC2::TransitGatewayMulticastDomain](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastdomain.html)
  - `af-south-1`
  - `me-south-1`
  - `eu-south-1`
  - `ap-east-1`

- [AWS::EC2::TransitGatewayMulticastDomainAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastdomainassociation.html)
  - `af-south-1`
  - `me-south-1`
  - `eu-south-1`
  - `ap-east-1`

- [AWS::EC2::TransitGatewayMulticastGroupMember](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupmember.html)
  - `af-south-1`
  - `me-south-1`
  - `eu-south-1`
  - `ap-east-1`

- [AWS::EC2::TransitGatewayMulticastGroupSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html)
  - `af-south-1`
  - `me-south-1`
  - `eu-south-1`
  - `ap-east-1`

- [AWS::EC2::TransitGatewayVpcAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayvpcattachment.html)
  - `me-south-1`
  - `ap-east-1`

- [AWS::RoboMaker::RobotApplication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html)
  - `us-gov-west-1`

- [AWS::RoboMaker::RobotApplicationVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplicationversion.html)
  - `us-gov-west-1`

- [AWS::RoboMaker::SimulationApplication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html)
  - `us-gov-west-1`

- [AWS::RoboMaker::SimulationApplicationVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplicationversion.html)
  - `us-gov-west-1`

- [AWS::ServiceCatalogAppRegistry::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-application.html)
  - `me-south-1`
  - `ap-east-1`

- [AWS::ServiceCatalogAppRegistry::AttributeGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-attributegroup.html)
  - `me-south-1`
  - `ap-east-1`

- [AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-attributegroupassociation.html)
  - `me-south-1`
  - `ap-east-1`

- [AWS::ServiceCatalogAppRegistry::ResourceAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-resourceassociation.html)
  - `me-south-1`
  - `ap-east-1`

- [AWS::AppIntegrations::DataIntegration.ScheduleConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-scheduleconfig.html)
  - `ap-northeast-2`
  - `af-south-1`

- [AWS::EC2::NetworkInsightsAnalysis.TransitGatewayRouteTableRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-transitgatewayroutetableroute.html)
  - `af-south-1`
  - `me-south-1`
  - `eu-south-1`
  - `ap-east-1`

- [AWS::RoboMaker::RobotApplication.RobotSoftwareSuite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-robotsoftwaresuite.html)
  - `us-gov-west-1`

- [AWS::RoboMaker::RobotApplication.SourceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-sourceconfig.html)
  - `us-gov-west-1`

- [AWS::RoboMaker::SimulationApplication.RenderingEngine](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-renderingengine.html)
  - `us-gov-west-1`

- [AWS::RoboMaker::SimulationApplication.RobotSoftwareSuite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-robotsoftwaresuite.html)
  - `us-gov-west-1`

- [AWS::RoboMaker::SimulationApplication.SimulationSoftwareSuite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-simulationsoftwaresuite.html)
  - `us-gov-west-1`

- [AWS::RoboMaker::SimulationApplication.SourceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-sourceconfig.html)
  - `us-gov-west-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v68.1.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v68.1.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v68.1.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v68.1.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v68.1.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v68.1.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- PropertyType Still Missing
  - Since v68.1.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v68.1.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v68.1.0: [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v68.1.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v68.1.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

