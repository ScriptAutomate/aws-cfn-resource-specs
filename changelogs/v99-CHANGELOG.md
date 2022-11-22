# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v99-changelog.json`](changelogs/v99-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [99.0.0](#9900-2022-11-20)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [99.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v99.0.0) (2022-11-20)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v99-changelog.json)
  - Change source is a diff between [v99.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v99.0.0) and [v97.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v97.0.0)

### Totals

- TotalPropertyTypes: 3464 **(+21)**
- TotalPropertyTypesSupportedGlobally: 1188 **(+8)**
- TotalResourceTypes: 987 **(+2)**
- TotalResourceTypesSupportedGlobally: 359 **(+1)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::CloudFront::ContinuousDeploymentPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-continuousdeploymentpolicy.html)
  - `eu-central-1`

- [AWS::SSM::ResourcePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcepolicy.html)
  - `ap-northeast-1`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-2`
  - `eu-west-3`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::AppSync::FunctionConfiguration.AppSyncRuntime](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-appsyncruntime.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AppSync::Resolver.AppSyncRuntime](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-appsyncruntime.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AutoScaling::AutoScalingGroup.NetworkBandwidthGbpsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-networkbandwidthgbpsrequest.html)
  - Available in **ALL** regions.

- [AWS::CloudFront::ContinuousDeploymentPolicy.ContinuousDeploymentPolicyConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig.html)
  - `eu-central-1`

- [AWS::CloudFront::ContinuousDeploymentPolicy.SessionStickinessConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig.html)
  - `eu-central-1`

- [AWS::CloudFront::ContinuousDeploymentPolicy.SingleHeaderConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderconfig.html)
  - `eu-central-1`

- [AWS::CloudFront::ContinuousDeploymentPolicy.SingleWeightConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleweightconfig.html)
  - `eu-central-1`

- [AWS::CloudFront::ContinuousDeploymentPolicy.TrafficConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-trafficconfig.html)
  - `eu-central-1`

- [AWS::ECS::Cluster.ServiceConnectDefaults](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-serviceconnectdefaults.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::ECS::Service.LogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-logconfiguration.html)
  - Available in **ALL** regions.

- [AWS::ECS::Service.Secret](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-secret.html)
  - Available in **ALL** regions.

- [AWS::ECS::Service.ServiceConnectClientAlias](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnectclientalias.html)
  - Available in **ALL** regions.

- [AWS::ECS::Service.ServiceConnectConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnectconfiguration.html)
  - Available in **ALL** regions.

- [AWS::ECS::Service.ServiceConnectService](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-serviceconnectservice.html)
  - Available in **ALL** regions.

- [AWS::IoTTwinMaker::ComponentType.PropertyGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-componenttype-propertygroup.html)
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::IoTTwinMaker::Entity.PropertyGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iottwinmaker-entity-propertygroup.html)
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::KinesisFirehose::DeliveryStream.AmazonOpenSearchServerlessBufferingHints](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessbufferinghints.html)
  - `cn-north-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::KinesisFirehose::DeliveryStream.AmazonOpenSearchServerlessDestinationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html)
  - `cn-north-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::KinesisFirehose::DeliveryStream.AmazonOpenSearchServerlessRetryOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessretryoptions.html)
  - `cn-north-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::S3::StorageLens.AdvancedCostOptimizationMetrics](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-advancedcostoptimizationmetrics.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::S3::StorageLens.AdvancedDataProtectionMetrics](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-advanceddataprotectionmetrics.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::S3::StorageLens.DetailedStatusCodesMetrics](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-detailedstatuscodesmetrics.html)
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
  - `us-west-1`
  - `us-west-2`

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::AmplifyUIBuilder::Form](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-form.html)
  - `me-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-west-1`

- [AWS::EC2::TransitGatewayConnect](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayconnect.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::EC2::TransitGatewayMulticastDomain](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastdomain.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::EC2::TransitGatewayMulticastDomainAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastdomainassociation.html)
  - `cn-northwest-1`

- [AWS::EC2::TransitGatewayMulticastGroupMember](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupmember.html)
  - `cn-northwest-1`

- [AWS::EC2::TransitGatewayMulticastGroupSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html)
  - `cn-northwest-1`

- [AWS::EC2::TransitGatewayPeeringAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::EMRServerless::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrserverless-application.html)
  - `ap-southeast-1`
  - `eu-central-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`

- [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
  - `ap-southeast-1`

- [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
  - `ap-southeast-1`

- [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
  - `ap-southeast-1`

- [AWS::M2::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html)
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-3`

- [AWS::M2::Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html)
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-3`

- [AWS::Organizations::Account](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-account.html)
  - `me-south-1`
  - `ca-central-1`
  - `cn-northwest-1`
  - `af-south-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-west-1`
  - `eu-north-1`
  - `us-east-2`
  - `ap-east-1`
  - `eu-west-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-south-1`
  - `eu-west-3`
  - `ap-northeast-3`

- [AWS::Organizations::OrganizationalUnit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organizationalunit.html)
  - Now available to **ALL** regions.

- [AWS::Organizations::Policy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-policy.html)
  - `me-south-1`
  - `us-gov-east-1`
  - `ca-central-1`
  - `af-south-1`
  - `us-gov-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-west-1`
  - `eu-north-1`
  - `us-east-2`
  - `ap-east-1`
  - `eu-west-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-south-1`
  - `eu-west-3`
  - `ap-northeast-3`

- [AWS::Scheduler::Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html)
  - `eu-west-1`
  - `eu-north-1`

- [AWS::Scheduler::ScheduleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedulegroup.html)
  - `eu-north-1`

- [AWS::XRay::ResourcePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-xray-resourcepolicy.html)
  - `me-south-1`
  - `eu-central-1`
  - `ca-central-1`
  - `af-south-1`
  - `us-west-2`
  - `eu-west-2`
  - `eu-north-1`
  - `ap-south-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `eu-south-1`
  - `eu-west-3`
  - `ap-northeast-3`

- [AWS::AmplifyUIBuilder::Form.FieldConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldconfig.html)
  - `me-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-west-1`

- [AWS::AmplifyUIBuilder::Form.FieldInputConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldinputconfig.html)
  - `me-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-west-1`

- [AWS::AmplifyUIBuilder::Form.FieldPosition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldposition.html)
  - `me-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-west-1`

- [AWS::AmplifyUIBuilder::Form.FieldValidationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-fieldvalidationconfiguration.html)
  - `me-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-west-1`

- [AWS::AmplifyUIBuilder::Form.FormButton](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formbutton.html)
  - `me-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-west-1`

- [AWS::AmplifyUIBuilder::Form.FormCTA](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formcta.html)
  - `me-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-west-1`

- [AWS::AmplifyUIBuilder::Form.FormDataTypeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formdatatypeconfig.html)
  - `me-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-west-1`

- [AWS::AmplifyUIBuilder::Form.FormInputValueProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-forminputvalueproperty.html)
  - `me-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-west-1`

- [AWS::AmplifyUIBuilder::Form.FormStyle](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyle.html)
  - `me-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-west-1`

- [AWS::AmplifyUIBuilder::Form.FormStyleConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-formstyleconfig.html)
  - `me-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-west-1`

- [AWS::AmplifyUIBuilder::Form.SectionalElement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-sectionalelement.html)
  - `me-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-west-1`

- [AWS::AmplifyUIBuilder::Form.ValueMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-valuemapping.html)
  - `me-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-west-1`

- [AWS::AmplifyUIBuilder::Form.ValueMappings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-form-valuemappings.html)
  - `me-south-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `us-east-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-west-1`

- [AWS::Batch::ComputeEnvironment.EksConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-eksconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::EC2::TransitGatewayConnect.TransitGatewayConnectOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewayconnect-transitgatewayconnectoptions.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::EKS::Cluster.ControlPlanePlacement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-controlplaneplacement.html)
  - Now available to **ALL** regions.

- [AWS::EMRServerless::Application.AutoStartConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-autostartconfiguration.html)
  - `ap-southeast-1`
  - `eu-central-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`

- [AWS::EMRServerless::Application.AutoStopConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-autostopconfiguration.html)
  - `ap-southeast-1`
  - `eu-central-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`

- [AWS::EMRServerless::Application.InitialCapacityConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfig.html)
  - `ap-southeast-1`
  - `eu-central-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`

- [AWS::EMRServerless::Application.InitialCapacityConfigKeyValuePair](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-initialcapacityconfigkeyvaluepair.html)
  - `ap-southeast-1`
  - `eu-central-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`

- [AWS::EMRServerless::Application.MaximumAllowedResources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-maximumallowedresources.html)
  - `ap-southeast-1`
  - `eu-central-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`

- [AWS::EMRServerless::Application.NetworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-networkconfiguration.html)
  - `ap-southeast-1`
  - `eu-central-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`

- [AWS::EMRServerless::Application.WorkerConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrserverless-application-workerconfiguration.html)
  - `ap-southeast-1`
  - `eu-central-1`
  - `ca-central-1`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `us-west-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`
  - `eu-west-3`

- [AWS::GroundStation::Config.AntennaDownlinkConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkconfig.html)
  - `ap-southeast-1`

- [AWS::GroundStation::Config.AntennaDownlinkDemodDecodeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.html)
  - `ap-southeast-1`

- [AWS::GroundStation::Config.AntennaUplinkConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.html)
  - `ap-southeast-1`

- [AWS::GroundStation::Config.ConfigData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-configdata.html)
  - `ap-southeast-1`

- [AWS::GroundStation::Config.DataflowEndpointConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-dataflowendpointconfig.html)
  - `ap-southeast-1`

- [AWS::GroundStation::Config.DecodeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-decodeconfig.html)
  - `ap-southeast-1`

- [AWS::GroundStation::Config.DemodulationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-demodulationconfig.html)
  - `ap-southeast-1`

- [AWS::GroundStation::Config.Eirp](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-eirp.html)
  - `ap-southeast-1`

- [AWS::GroundStation::Config.Frequency](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequency.html)
  - `ap-southeast-1`

- [AWS::GroundStation::Config.FrequencyBandwidth](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-frequencybandwidth.html)
  - `ap-southeast-1`

- [AWS::GroundStation::Config.S3RecordingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.html)
  - `ap-southeast-1`

- [AWS::GroundStation::Config.SpectrumConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-spectrumconfig.html)
  - `ap-southeast-1`

- [AWS::GroundStation::Config.TrackingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-trackingconfig.html)
  - `ap-southeast-1`

- [AWS::GroundStation::Config.UplinkEchoConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkechoconfig.html)
  - `ap-southeast-1`

- [AWS::GroundStation::Config.UplinkSpectrumConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkspectrumconfig.html)
  - `ap-southeast-1`

- [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
  - `ap-southeast-1`

- [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
  - `ap-southeast-1`

- [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
  - `ap-southeast-1`

- [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
  - `ap-southeast-1`

- [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
  - `ap-southeast-1`

- [AWS::M2::Application.Content](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-application-content.html)
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-3`

- [AWS::M2::Application.Definition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-application-definition.html)
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-3`

- [AWS::M2::Application.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-application-s3location.html)
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-3`

- [AWS::M2::Environment.EfsStorageConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-efsstorageconfiguration.html)
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-3`

- [AWS::M2::Environment.FsxStorageConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-fsxstorageconfiguration.html)
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-3`

- [AWS::M2::Environment.HighAvailabilityConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-highavailabilityconfig.html)
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-3`

- [AWS::M2::Environment.StorageConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-environment-storageconfiguration.html)
  - `ap-southeast-1`
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-3`

- [AWS::Panorama::Package.StorageLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-package-storagelocation.html)
  - `us-west-2`
  - `eu-west-1`
  - `us-east-1`

- [AWS::Scheduler::Schedule.AwsVpcConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-awsvpcconfiguration.html)
  - `eu-west-1`
  - `eu-north-1`

- [AWS::Scheduler::Schedule.CapacityProviderStrategyItem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-capacityproviderstrategyitem.html)
  - `eu-west-1`
  - `eu-north-1`

- [AWS::Scheduler::Schedule.DeadLetterConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-deadletterconfig.html)
  - `eu-west-1`
  - `eu-north-1`

- [AWS::Scheduler::Schedule.EcsParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html)
  - `eu-west-1`
  - `eu-north-1`

- [AWS::Scheduler::Schedule.EventBridgeParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-eventbridgeparameters.html)
  - `eu-west-1`
  - `eu-north-1`

- [AWS::Scheduler::Schedule.FlexibleTimeWindow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-flexibletimewindow.html)
  - `eu-west-1`
  - `eu-north-1`

- [AWS::Scheduler::Schedule.KinesisParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-kinesisparameters.html)
  - `eu-west-1`
  - `eu-north-1`

- [AWS::Scheduler::Schedule.NetworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-networkconfiguration.html)
  - `eu-west-1`
  - `eu-north-1`

- [AWS::Scheduler::Schedule.PlacementConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementconstraint.html)
  - `eu-west-1`
  - `eu-north-1`

- [AWS::Scheduler::Schedule.PlacementStrategy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementstrategy.html)
  - `eu-west-1`
  - `eu-north-1`

- [AWS::Scheduler::Schedule.RetryPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-retrypolicy.html)
  - `eu-west-1`
  - `eu-north-1`

- [AWS::Scheduler::Schedule.SageMakerPipelineParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameter.html)
  - `eu-west-1`
  - `eu-north-1`

- [AWS::Scheduler::Schedule.SageMakerPipelineParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameters.html)
  - `eu-west-1`
  - `eu-north-1`

- [AWS::Scheduler::Schedule.SqsParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sqsparameters.html)
  - `eu-west-1`
  - `eu-north-1`

- [AWS::Scheduler::Schedule.TagMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-tagmap.html)
  - `eu-west-1`
  - `eu-north-1`

- [AWS::Scheduler::Schedule.Target](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html)
  - `eu-west-1`
  - `eu-north-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v97.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v97.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v97.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v97.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v97.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v97.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- New ResourceType(s) Missing
  - [AWS::CloudFront::ContinuousDeploymentPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-continuousdeploymentpolicy.html)
    - `eu-central-1`

- PropertyType Still Missing
  - Since v97.0.0: [AWS::Config::OrganizationConfigRule.OrganizationCustomPolicyRuleMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html)
    - `me-south-1`

  - Since v97.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v97.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v97.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v97.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::CloudFront::ContinuousDeploymentPolicy.ContinuousDeploymentPolicyConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig.html)
    - `eu-central-1`

  - [AWS::CloudFront::ContinuousDeploymentPolicy.SessionStickinessConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig.html)
    - `eu-central-1`

  - [AWS::CloudFront::ContinuousDeploymentPolicy.SingleHeaderConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderconfig.html)
    - `eu-central-1`

  - [AWS::CloudFront::ContinuousDeploymentPolicy.SingleWeightConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-singleweightconfig.html)
    - `eu-central-1`

  - [AWS::CloudFront::ContinuousDeploymentPolicy.TrafficConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-continuousdeploymentpolicy-trafficconfig.html)
    - `eu-central-1`

  - [AWS::KinesisFirehose::DeliveryStream.AmazonOpenSearchServerlessBufferingHints](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessbufferinghints.html)
    - `cn-north-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::KinesisFirehose::DeliveryStream.AmazonOpenSearchServerlessDestinationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html)
    - `cn-north-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::KinesisFirehose::DeliveryStream.AmazonOpenSearchServerlessRetryOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessretryoptions.html)
    - `cn-north-1`
    - `eu-central-1`
    - `us-west-2`

