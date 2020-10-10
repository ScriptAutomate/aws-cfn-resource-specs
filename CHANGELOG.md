# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v18-changelog.json`](changelogs/v18-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [18.7.0](#1870-2020-10-08)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)
- [18.6.0](#1860-2020-10-02)
  - [Totals](#totals-1)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-1)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes-1)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-1)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-1)
- [18.5.0](#1850-2020-09-25)
  - [Totals](#totals-2)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-2)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-2)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-2)
- [18.4.0](#1840-2020-09-17)
  - [Totals](#totals-3)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-3)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-3)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-3)
- [18.3.0](#1830-2020-09-10)
  - [Totals](#totals-4)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-4)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-4)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions-1)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-4)
- [18.2.0](#1820-2020-09-05)
  - [Totals](#totals-5)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-5)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-5)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions-2)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-5)
- [18.1.0](#1810-2020-08-28)
  - [Totals](#totals-6)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-6)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-6)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-6)
- [18.0.0](#1800-2020-08-24)
  - [Totals](#totals-7)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-7)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes-2)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-7)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions-3)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-7)

## [18.7.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.7.0) (2020-10-08)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v18-changelog.json)
  - Change source is a diff between [v18.7.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.7.0) and [v18.6.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.6.0)

### Totals

- TotalPropertyTypes: 1736 **(+0)**
- TotalPropertyTypesSupportedGlobally: 495 **(+0)**
- TotalResourceTypes: 576 **(+4)**
- TotalResourceTypesSupportedGlobally: 190 **(+1)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::CodeArtifact::Domain](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-domain.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::CodeArtifact::Repository](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Timestream::Database](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Timestream::Table](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::KinesisFirehose::DeliveryStream.DeliveryStreamEncryptionConfigurationInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html)
  - `cn-north-1`
  - `eu-central-1`
  - `us-west-2`

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::DynamoDB::Table.ContributorInsightsSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-contributorinsightsspecification.html)
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::EC2::GatewayRouteTableAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-gatewayroutetableassociation.html)
  - Now available to **ALL** regions.

- [AWS::IoT::Authorizer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html)
  - `us-gov-east-1`

- [AWS::IoT::ProvisioningTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html)
  - `us-gov-east-1`

- [AWS::Backup::BackupPlan.AdvancedBackupSettingResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-advancedbackupsettingresourcetype.html)
  - `eu-west-1`
  - `cn-northwest-1`
  - `cn-north-1`
  - `eu-central-1`
  - `us-gov-west-1`
  - `us-west-2`
  - `us-gov-east-1`

- [AWS::IoT::Authorizer.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-authorizer-tags.html)
  - `us-gov-east-1`

- [AWS::IoT::Authorizer.TokenSigningPublicKeys](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-authorizer-tokensigningpublickeys.html)
  - `us-gov-east-1`

- [AWS::IoT::ProvisioningTemplate.ProvisioningHook](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-provisioningtemplate-provisioninghook.html)
  - `us-gov-east-1`

- [AWS::IoT::ProvisioningTemplate.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-provisioningtemplate-tags.html)
  - `us-gov-east-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v18.6.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.6.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.6.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

- PropertyType Still Missing
  - Since v18.6.0: [AWS::AppSync::FunctionConfiguration.LambdaConflictHandlerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html)
    - `ap-northeast-2`

  - Since v18.6.0: [AWS::AppSync::FunctionConfiguration.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html)
    - `ap-northeast-2`

  - Since v18.6.0: [AWS::ECS::Cluster.ClusterSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersetting.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `eu-south-1`

  - Since v18.6.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.6.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.6.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.6.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.6.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.6.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v18.6.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::KinesisFirehose::DeliveryStream.DeliveryStreamEncryptionConfigurationInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html)
    - `cn-north-1`
    - `eu-central-1`
    - `us-west-2`

## [18.6.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.6.0) (2020-10-02)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v18-changelog.json)
  - Change source is a diff between [v18.6.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.6.0) and [v18.5.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.5.0)

### Totals

- TotalPropertyTypes: 1736 **(+1)**
- TotalPropertyTypesSupportedGlobally: 495 **(+5)**
- TotalResourceTypes: 572 **(+1)**
- TotalResourceTypesSupportedGlobally: 189 **(+2)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::WorkSpaces::ConnectionAlias](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Backup::BackupPlan.AdvancedBackupSettingResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-advancedbackupsettingresourcetype.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`

- [AWS::DynamoDB::Table.ContributorInsightsSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-contributorinsightsspecification.html)
  - `us-west-2`

- [AWS::WorkSpaces::ConnectionAlias.ConnectionAliasAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::SSM::Document.AttachmentsSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html)
  - `ca-central-1`
  - `us-west-2`

- [AWS::SSM::Document.DocumentRequires](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-documentrequires.html)
  - `ca-central-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::ACMPCA::Certificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ACMPCA::CertificateAuthority](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ACMPCA::CertificateAuthorityActivation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::AccessAnalyzer::Analyzer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ApplicationInsights::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::Chatbot::SlackChannelConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CloudFront::CachePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cachepolicy.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CloudFront::OriginRequestPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originrequestpolicy.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CloudFront::RealtimeLogConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CloudWatch::CompositeAlarm](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::Detective::Graph](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::Detective::MemberInvitation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::EC2::LocalGatewayRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.html)
  - `af-south-1`

- [AWS::EC2::LocalGatewayRouteTableVPCAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetablevpcassociation.html)
  - `af-south-1`

- [AWS::EC2::PrefixList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-prefixlist.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::EFS::AccessPoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-accesspoint.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::EKS::FargateProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::GlobalAccelerator::Accelerator](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-accelerator.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::GlobalAccelerator::EndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-endpointgroup.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::GlobalAccelerator::Listener](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-globalaccelerator-listener.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
  - `af-south-1`

- [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
  - `af-south-1`

- [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
  - `af-south-1`

- [AWS::ImageBuilder::Component](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ImageBuilder::DistributionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ImageBuilder::Image](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ImageBuilder::ImagePipeline](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ImageBuilder::ImageRecipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ImageBuilder::InfrastructureConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::NetworkManager::CustomerGatewayAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::NetworkManager::Device](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::NetworkManager::GlobalNetwork](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::NetworkManager::Link](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::NetworkManager::LinkAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::NetworkManager::Site](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::NetworkManager::TransitGatewayRegistration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ResourceGroups::Group](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html)
  - Now available to **ALL** regions.

- [AWS::Route53Resolver::ResolverQueryLoggingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html)
  - `eu-south-1`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `af-south-1`

- [AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html)
  - `eu-south-1`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `af-south-1`

- [AWS::S3::AccessPoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accesspoint.html)
  - Now available to **ALL** regions.

- [AWS::StepFunctions::StateMachine](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::Synthetics::Canary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::Transfer::Server](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Transfer::User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::WAFv2::IPSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RegexPatternSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACLAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ACMPCA::Certificate.Validity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-validity.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ACMPCA::CertificateAuthority.CrlConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ACMPCA::CertificateAuthority.RevocationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-revocationconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ACMPCA::CertificateAuthority.Subject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::AccessAnalyzer::Analyzer.ArchiveRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::AccessAnalyzer::Analyzer.Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ApiGateway::DomainName.MutualTlsAuthentication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-domainname-mutualtlsauthentication.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ApplicationInsights::Application.Alarm](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarm.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ApplicationInsights::Application.AlarmMetric](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarmmetric.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ApplicationInsights::Application.ComponentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ApplicationInsights::Application.ComponentMonitoringSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ApplicationInsights::Application.ConfigurationDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ApplicationInsights::Application.CustomComponent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-customcomponent.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ApplicationInsights::Application.Log](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ApplicationInsights::Application.LogPattern](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ApplicationInsights::Application.LogPatternSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpatternset.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ApplicationInsights::Application.SubComponentConfigurationDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ApplicationInsights::Application.SubComponentTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponenttypeconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ApplicationInsights::Application.WindowsEvent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CloudFront::CachePolicy.CachePolicyConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CloudFront::CachePolicy.CookiesConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cookiesconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CloudFront::CachePolicy.HeadersConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-headersconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CloudFront::CachePolicy.ParametersInCacheKeyAndForwardedToOrigin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CloudFront::CachePolicy.QueryStringsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-querystringsconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CloudFront::OriginRequestPolicy.CookiesConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-cookiesconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CloudFront::OriginRequestPolicy.HeadersConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-headersconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CloudFront::OriginRequestPolicy.OriginRequestPolicyConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CloudFront::OriginRequestPolicy.QueryStringsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-querystringsconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CloudFront::RealtimeLogConfig.EndPoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-endpoint.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CloudFront::RealtimeLogConfig.KinesisStreamConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-kinesisstreamconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::EC2::LocalGatewayRouteTableVPCAssociation.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-localgatewayroutetablevpcassociation-tags.html)
  - `af-south-1`

- [AWS::EC2::PrefixList.Entry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-prefixlist-entry.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ECS::Service.CapacityProviderStrategyItem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-capacityproviderstrategyitem.html)
  - `eu-west-3`
  - `cn-northwest-1`
  - `ap-east-1`
  - `me-south-1`
  - `us-gov-west-1`
  - `us-gov-east-1`
  - `eu-north-1`

- [AWS::EFS::AccessPoint.AccessPointTag](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-accesspointtag.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::EFS::AccessPoint.CreationInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-creationinfo.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::EFS::AccessPoint.PosixUser](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-posixuser.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::EFS::AccessPoint.RootDirectory](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-accesspoint-rootdirectory.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::EFS::FileSystem.BackupPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-efs-filesystem-backuppolicy.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::EKS::Cluster.KubernetesNetworkConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-kubernetesnetworkconfig.html)
  - `us-west-1`
  - `cn-north-1`
  - `cn-northwest-1`
  - `ap-east-1`

- [AWS::EKS::FargateProfile.Label](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-label.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::EKS::FargateProfile.Selector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-selector.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::GlobalAccelerator::EndpointGroup.EndpointConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-endpointgroup-endpointconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::GlobalAccelerator::Listener.PortRange](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-globalaccelerator-listener-portrange.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
  - `af-south-1`

- [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
  - `af-south-1`

- [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
  - `af-south-1`

- [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
  - `af-south-1`

- [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
  - `af-south-1`

- [AWS::ImageBuilder::DistributionConfiguration.Distribution](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ImageBuilder::Image.ImageTestsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagetestsconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ImageBuilder::ImagePipeline.ImageTestsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ImageBuilder::ImagePipeline.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ImageBuilder::ImageRecipe.ComponentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ImageBuilder::ImageRecipe.EbsInstanceBlockDeviceSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ImageBuilder::ImageRecipe.InstanceBlockDeviceMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ImageBuilder::InfrastructureConfiguration.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-logging.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ImageBuilder::InfrastructureConfiguration.S3Logs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::KinesisFirehose::DeliveryStream.HttpEndpointCommonAttribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::KinesisFirehose::DeliveryStream.HttpEndpointConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::KinesisFirehose::DeliveryStream.HttpEndpointDestinationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::KinesisFirehose::DeliveryStream.HttpEndpointRequestConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::KinesisFirehose::DeliveryStream.RedshiftRetryOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftretryoptions.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::KinesisFirehose::DeliveryStream.RetryOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-retryoptions.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::KinesisFirehose::DeliveryStream.VpcConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::NetworkManager::Device.Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::NetworkManager::Link.Bandwidth](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::NetworkManager::Site.Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::ResourceGroups::Group.Query](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-query.html)
  - Now available to **ALL** regions.

- [AWS::ResourceGroups::Group.ResourceQuery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-resourcequery.html)
  - Now available to **ALL** regions.

- [AWS::ResourceGroups::Group.TagFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-tagfilter.html)
  - Now available to **ALL** regions.

- [AWS::S3::AccessPoint.PublicAccessBlockConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-accesspoint-publicaccessblockconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::S3::AccessPoint.VpcConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-accesspoint-vpcconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::StepFunctions::StateMachine.CloudWatchLogsLogGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::StepFunctions::StateMachine.DefinitionSubstitutions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-definitionsubstitutions.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::StepFunctions::StateMachine.LogDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::StepFunctions::StateMachine.LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::StepFunctions::StateMachine.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::StepFunctions::StateMachine.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::StepFunctions::StateMachine.TracingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tracingconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::Synthetics::Canary.Code](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::Synthetics::Canary.RunConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::Synthetics::Canary.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-schedule.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::Synthetics::Canary.VPCConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::Transfer::Server.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Transfer::Server.IdentityProviderDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Transfer::Server.Protocol]()
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Transfer::User.HomeDirectoryMapEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Transfer::User.SshPublicKey]()
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::WAFv2::RuleGroup.AndStatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-andstatementone.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.AndStatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-andstatementtwo.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.ByteMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.FieldToMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.ForwardedIPConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-forwardedipconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.GeoMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-geomatchstatement.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.IPSetForwardedIPConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.IPSetReferenceStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.NotStatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-notstatementone.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.NotStatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-notstatementtwo.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.OrStatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-orstatementone.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.OrStatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-orstatementtwo.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.RateBasedStatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementone.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.RateBasedStatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementtwo.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.RegexPatternSetReferenceStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.RuleAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.SizeConstraintStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.SqliMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sqlimatchstatement.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.StatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementone.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.StatementThree](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementthree.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.StatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementtwo.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.TextTransformation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-texttransformation.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.VisibilityConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::RuleGroup.XssMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-xssmatchstatement.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.AndStatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-andstatementone.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.AndStatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-andstatementtwo.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.ByteMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.DefaultAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-defaultaction.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.ExcludedRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-excludedrule.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.FieldToMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.ForwardedIPConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-forwardedipconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.GeoMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-geomatchstatement.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.IPSetForwardedIPConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.IPSetReferenceStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.ManagedRuleGroupStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.NotStatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatementone.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.NotStatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatementtwo.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.OrStatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-orstatementone.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.OrStatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-orstatementtwo.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.OverrideAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-overrideaction.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.RateBasedStatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementone.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.RateBasedStatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementtwo.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.RegexPatternSetReferenceStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.RuleAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.RuleGroupReferenceStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rulegroupreferencestatement.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.SizeConstraintStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.SqliMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sqlimatchstatement.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.StatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementone.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.StatementThree](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementthree.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.StatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementtwo.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.TextTransformation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformation.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.VisibilityConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::WAFv2::WebACL.XssMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-xssmatchstatement.html)
  - `eu-south-1`
  - `af-south-1`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::AmazonMQ::Broker.InterBrokerCred](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-interbrokercred.html)
  - `ap-southeast-2`

- [AWS::AmazonMQ::Broker.LdapMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-ldapmetadata.html)
  - `ap-southeast-2`

- [AWS::AmazonMQ::Broker.ServerMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-servermetadata.html)
  - `ap-southeast-2`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v18.5.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.5.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.5.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

- PropertyType Still Missing
  - Since v18.5.0: [AWS::AppSync::FunctionConfiguration.LambdaConflictHandlerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html)
    - `ap-northeast-2`

  - Since v18.5.0: [AWS::AppSync::FunctionConfiguration.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html)
    - `ap-northeast-2`

  - Since v18.5.0: [AWS::ECS::Cluster.ClusterSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersetting.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `eu-south-1`

  - Since v18.5.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.5.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.5.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.5.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.5.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.5.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v18.5.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::DynamoDB::Table.ContributorInsightsSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-contributorinsightsspecification.html)
    - `us-west-2`

## [18.5.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.5.0) (2020-09-25)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v18-changelog.json)
  - Change source is a diff between [v18.5.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.5.0) and [v18.4.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.4.0)

### Totals

- TotalPropertyTypes: 1735 **(+6)**
- TotalPropertyTypesSupportedGlobally: 490 **(+0)**
- TotalResourceTypes: 571 **(+0)**
- TotalResourceTypesSupportedGlobally: 187 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::Batch::JobDefinition.LogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-logconfiguration.html)
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

- [AWS::Batch::JobDefinition.Secret](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-secret.html)
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

- [AWS::Batch::JobDefinition.Tmpfs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-tmpfs.html)
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

- [AWS::EKS::Cluster.KubernetesNetworkConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-kubernetesnetworkconfig.html)
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::SSM::Document.AttachmentsSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html)
  - `ca-central-1`
  - `us-west-2`

- [AWS::SSM::Document.DocumentRequires](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-documentrequires.html)
  - `ca-central-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::CloudWatch::CompositeAlarm](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html)
  - `ap-northeast-3`

- [AWS::ImageBuilder::Component](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::ImageBuilder::DistributionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::ImageBuilder::Image](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::ImageBuilder::ImagePipeline](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::ImageBuilder::ImageRecipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::ImageBuilder::InfrastructureConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::StepFunctions::StateMachine](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html)
  - `ap-northeast-3`
  - `me-south-1`
  - `cn-northwest-1`

- [AWS::ECS::Service.CapacityProviderStrategyItem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-capacityproviderstrategyitem.html)
  - `ap-south-1`
  - `ca-central-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `us-east-2`
  - `sa-east-1`
  - `us-west-1`
  - `eu-west-2`
  - `eu-west-1`

- [AWS::ImageBuilder::DistributionConfiguration.Distribution](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::ImageBuilder::Image.ImageTestsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagetestsconfiguration.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::ImageBuilder::ImagePipeline.ImageTestsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::ImageBuilder::ImagePipeline.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::ImageBuilder::ImageRecipe.ComponentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::ImageBuilder::ImageRecipe.EbsInstanceBlockDeviceSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::ImageBuilder::ImageRecipe.InstanceBlockDeviceMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::ImageBuilder::InfrastructureConfiguration.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-logging.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::ImageBuilder::InfrastructureConfiguration.S3Logs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::StepFunctions::StateMachine.CloudWatchLogsLogGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup.html)
  - `ap-northeast-3`
  - `me-south-1`
  - `cn-northwest-1`

- [AWS::StepFunctions::StateMachine.DefinitionSubstitutions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-definitionsubstitutions.html)
  - `ap-northeast-3`
  - `me-south-1`
  - `cn-northwest-1`

- [AWS::StepFunctions::StateMachine.LogDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html)
  - `ap-northeast-3`
  - `me-south-1`
  - `cn-northwest-1`

- [AWS::StepFunctions::StateMachine.LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html)
  - `ap-northeast-3`
  - `me-south-1`
  - `cn-northwest-1`

- [AWS::StepFunctions::StateMachine.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html)
  - `ap-northeast-3`
  - `me-south-1`
  - `cn-northwest-1`

- [AWS::StepFunctions::StateMachine.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html)
  - `ap-northeast-3`
  - `me-south-1`
  - `cn-northwest-1`

- [AWS::StepFunctions::StateMachine.TracingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tracingconfiguration.html)
  - `ap-northeast-3`
  - `me-south-1`
  - `cn-northwest-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v18.4.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.4.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.4.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

- PropertyType Still Missing
  - Since v18.4.0: [AWS::AppSync::FunctionConfiguration.LambdaConflictHandlerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html)
    - `ap-northeast-2`

  - Since v18.4.0: [AWS::AppSync::FunctionConfiguration.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html)
    - `ap-northeast-2`

  - Since v18.4.0: [AWS::ECS::Cluster.ClusterSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersetting.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `eu-south-1`

  - Since v18.4.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.4.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.4.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.4.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.4.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.4.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v18.4.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::SSM::Document.AttachmentsSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html)
    - `ca-central-1`
    - `us-west-2`

  - [AWS::SSM::Document.DocumentRequires](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-documentrequires.html)
    - `ca-central-1`
    - `us-west-2`

## [18.4.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.4.0) (2020-09-17)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v18-changelog.json)
  - Change source is a diff between [v18.4.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.4.0) and [v18.3.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.3.0)

### Totals

- TotalPropertyTypes: 1729 **(+70)**
- TotalPropertyTypesSupportedGlobally: 490 **(+2)**
- TotalResourceTypes: 571 **(+3)**
- TotalResourceTypesSupportedGlobally: 187 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::AppFlow::ConnectorProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html)
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

- [AWS::AppFlow::Flow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html)
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

- [AWS::CloudFormation::StackSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html)
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

- [AWS::ApiGateway::DomainName.MutualTlsAuthentication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-domainname-mutualtlsauthentication.html)
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

- [AWS::ApiGatewayV2::DomainName.MutualTlsAuthentication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-mutualtlsauthentication.html)
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
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::AppFlow::ConnectorProfile.AmplitudeConnectorProfileCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-amplitudeconnectorprofilecredentials.html)
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

- [AWS::AppFlow::ConnectorProfile.ConnectorOAuthRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectoroauthrequest.html)
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

- [AWS::AppFlow::ConnectorProfile.ConnectorProfileConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileconfig.html)
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

- [AWS::AppFlow::ConnectorProfile.ConnectorProfileCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html)
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

- [AWS::AppFlow::ConnectorProfile.ConnectorProfileProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html)
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

- [AWS::AppFlow::ConnectorProfile.DatadogConnectorProfileCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-datadogconnectorprofilecredentials.html)
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

- [AWS::AppFlow::ConnectorProfile.DatadogConnectorProfileProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-datadogconnectorprofileproperties.html)
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

- [AWS::AppFlow::ConnectorProfile.DynatraceConnectorProfileCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-dynatraceconnectorprofilecredentials.html)
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

- [AWS::AppFlow::ConnectorProfile.DynatraceConnectorProfileProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-dynatraceconnectorprofileproperties.html)
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

- [AWS::AppFlow::ConnectorProfile.GoogleAnalyticsConnectorProfileCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials.html)
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

- [AWS::AppFlow::ConnectorProfile.InforNexusConnectorProfileCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-infornexusconnectorprofilecredentials.html)
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

- [AWS::AppFlow::ConnectorProfile.InforNexusConnectorProfileProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-infornexusconnectorprofileproperties.html)
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

- [AWS::AppFlow::ConnectorProfile.MarketoConnectorProfileCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-marketoconnectorprofilecredentials.html)
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

- [AWS::AppFlow::ConnectorProfile.MarketoConnectorProfileProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-marketoconnectorprofileproperties.html)
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

- [AWS::AppFlow::ConnectorProfile.RedshiftConnectorProfileCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofilecredentials.html)
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

- [AWS::AppFlow::ConnectorProfile.RedshiftConnectorProfileProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html)
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

- [AWS::AppFlow::ConnectorProfile.SalesforceConnectorProfileCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials.html)
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

- [AWS::AppFlow::ConnectorProfile.SalesforceConnectorProfileProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofileproperties.html)
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

- [AWS::AppFlow::ConnectorProfile.ServiceNowConnectorProfileCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-servicenowconnectorprofilecredentials.html)
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

- [AWS::AppFlow::ConnectorProfile.ServiceNowConnectorProfileProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-servicenowconnectorprofileproperties.html)
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

- [AWS::AppFlow::ConnectorProfile.SingularConnectorProfileCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-singularconnectorprofilecredentials.html)
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

- [AWS::AppFlow::ConnectorProfile.SlackConnectorProfileCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-slackconnectorprofilecredentials.html)
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

- [AWS::AppFlow::ConnectorProfile.SlackConnectorProfileProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-slackconnectorprofileproperties.html)
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

- [AWS::AppFlow::ConnectorProfile.SnowflakeConnectorProfileCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofilecredentials.html)
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

- [AWS::AppFlow::ConnectorProfile.SnowflakeConnectorProfileProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties.html)
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

- [AWS::AppFlow::ConnectorProfile.TrendmicroConnectorProfileCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-trendmicroconnectorprofilecredentials.html)
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

- [AWS::AppFlow::ConnectorProfile.VeevaConnectorProfileCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-veevaconnectorprofilecredentials.html)
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

- [AWS::AppFlow::ConnectorProfile.VeevaConnectorProfileProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-veevaconnectorprofileproperties.html)
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

- [AWS::AppFlow::ConnectorProfile.ZendeskConnectorProfileCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-zendeskconnectorprofilecredentials.html)
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

- [AWS::AppFlow::ConnectorProfile.ZendeskConnectorProfileProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-zendeskconnectorprofileproperties.html)
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

- [AWS::AppFlow::Flow.AggregationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-aggregationconfig.html)
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

- [AWS::AppFlow::Flow.AmplitudeSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-amplitudesourceproperties.html)
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

- [AWS::AppFlow::Flow.ConnectorOperator](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html)
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

- [AWS::AppFlow::Flow.DatadogSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-datadogsourceproperties.html)
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

- [AWS::AppFlow::Flow.DestinationConnectorProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html)
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

- [AWS::AppFlow::Flow.DestinationFlowConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationflowconfig.html)
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

- [AWS::AppFlow::Flow.DynatraceSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-dynatracesourceproperties.html)
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

- [AWS::AppFlow::Flow.ErrorHandlingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-errorhandlingconfig.html)
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

- [AWS::AppFlow::Flow.EventBridgeDestinationProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-eventbridgedestinationproperties.html)
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

- [AWS::AppFlow::Flow.GoogleAnalyticsSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-googleanalyticssourceproperties.html)
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

- [AWS::AppFlow::Flow.InforNexusSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-infornexussourceproperties.html)
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

- [AWS::AppFlow::Flow.MarketoSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-marketosourceproperties.html)
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

- [AWS::AppFlow::Flow.PrefixConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-prefixconfig.html)
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

- [AWS::AppFlow::Flow.RedshiftDestinationProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-redshiftdestinationproperties.html)
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

- [AWS::AppFlow::Flow.S3DestinationProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3destinationproperties.html)
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

- [AWS::AppFlow::Flow.S3OutputFormatConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3outputformatconfig.html)
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

- [AWS::AppFlow::Flow.S3SourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3sourceproperties.html)
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

- [AWS::AppFlow::Flow.SalesforceDestinationProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcedestinationproperties.html)
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

- [AWS::AppFlow::Flow.SalesforceSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcesourceproperties.html)
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

- [AWS::AppFlow::Flow.ScheduledTriggerProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-scheduledtriggerproperties.html)
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

- [AWS::AppFlow::Flow.ServiceNowSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-servicenowsourceproperties.html)
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

- [AWS::AppFlow::Flow.SingularSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-singularsourceproperties.html)
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

- [AWS::AppFlow::Flow.SlackSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-slacksourceproperties.html)
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

- [AWS::AppFlow::Flow.SnowflakeDestinationProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-snowflakedestinationproperties.html)
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

- [AWS::AppFlow::Flow.SourceConnectorProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html)
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

- [AWS::AppFlow::Flow.SourceFlowConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceflowconfig.html)
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

- [AWS::AppFlow::Flow.Task](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-task.html)
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

- [AWS::AppFlow::Flow.TaskPropertiesObject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-taskpropertiesobject.html)
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

- [AWS::AppFlow::Flow.TrendmicroSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-trendmicrosourceproperties.html)
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

- [AWS::AppFlow::Flow.TriggerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-triggerconfig.html)
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

- [AWS::AppFlow::Flow.VeevaSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-veevasourceproperties.html)
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

- [AWS::AppFlow::Flow.ZendeskSourceProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-zendesksourceproperties.html)
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

- [AWS::CloudFormation::StackSet.AutoDeployment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-autodeployment.html)
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

- [AWS::CloudFormation::StackSet.DeploymentTargets](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-deploymenttargets.html)
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

- [AWS::CloudFormation::StackSet.OperationPreferences](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html)
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

- [AWS::CloudFormation::StackSet.Parameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-parameter.html)
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

- [AWS::CloudFormation::StackSet.StackInstances](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-stackinstances.html)
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

- [AWS::ECS::Service.CapacityProviderStrategyItem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-capacityproviderstrategyitem.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `us-east-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Route53Resolver::ResolverEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html)
  - `ap-southeast-2`

- [AWS::Route53Resolver::ResolverRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html)
  - `ap-southeast-2`

- [AWS::StepFunctions::StateMachine](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html)
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-west-2`
  - `us-west-1`
  - `ap-southeast-2`

- [AWS::LakeFormation::Permissions.ColumnWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html)
  - `us-east-2`

- [AWS::LakeFormation::Permissions.DataLocationResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html)
  - `us-east-2`

- [AWS::LakeFormation::Permissions.TableWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewildcard.html)
  - `eu-west-1`
  - `us-east-2`
  - `us-east-1`

- [AWS::LakeFormation::Permissions.TableWithColumnsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html)
  - `us-east-2`

- [AWS::MSK::Cluster.Sasl](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html)
  - `ap-south-1`
  - `us-gov-east-1`
  - `sa-east-1`
  - `us-east-2`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`
  - `us-gov-west-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-west-2`
  - `us-west-1`
  - `me-south-1`

- [AWS::MSK::Cluster.Scram](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-scram.html)
  - `ap-south-1`
  - `us-gov-east-1`
  - `sa-east-1`
  - `us-east-2`
  - `eu-west-3`
  - `cn-northwest-1`
  - `eu-north-1`
  - `us-gov-west-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-west-2`
  - `us-west-1`
  - `me-south-1`

- [AWS::MediaLive::Channel.AacSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.Ac3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.ArchiveContainerSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecontainersettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.ArchiveGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivegroupsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.ArchiveOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archiveoutputsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.AribDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aribdestinationsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.AudioChannelMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiochannelmapping.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.AudioCodecSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.AudioDescription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.AudioNormalizationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audionormalizationsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.AudioOnlyHlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.AudioTrack](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrack.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.AudioTrackSelection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrackselection.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.AutomaticInputFailoverSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-automaticinputfailoversettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.AvailBlanking](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availblanking.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.AvailConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availconfiguration.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.AvailSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.BlackoutSlate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.BurnInDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.CaptionDescription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.CaptionDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.CaptionLanguageMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionlanguagemapping.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.ColorSpacePassthroughSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-colorspacepassthroughsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.DvbNitSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbnitsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.DvbSdtSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.DvbSubDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.DvbTdtSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbtdtsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.Eac3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.EbuTtDDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.EmbeddedDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddeddestinationsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.EmbeddedPlusScte20DestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedplusscte20destinationsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.EncoderSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.FeatureActivations](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-featureactivations.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.FecOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fecoutputsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.Fmp4HlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fmp4hlssettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.FrameCaptureGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturegroupsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.FrameCaptureOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptureoutputsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.FrameCaptureSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturesettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.GlobalConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.H264ColorSpaceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264colorspacesettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.H264FilterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264filtersettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.H264Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.H265ColorSpaceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.H265FilterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265filtersettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.H265Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.Hdr10Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hdr10settings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.HlsAkamaiSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.HlsBasicPutSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.HlsCdnSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.HlsGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.HlsMediaStoreSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.HlsOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.HlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.HlsWebdavSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.InputChannelLevel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputchannellevel.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.InputLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlocation.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.InputLossBehavior](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.KeyProviderSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-keyprovidersettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.M2tsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.M3u8Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.MediaPackageGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackagegroupsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.MediaPackageOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackageoutputsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.Mp2Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.MsSmoothGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.MsSmoothOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothoutputsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.MultiplexGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexgroupsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.MultiplexOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexoutputsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.NielsenConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenconfiguration.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.OutputGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroup.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.OutputGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.OutputLocationRef](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputlocationref.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.OutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.PassThroughSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-passthroughsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.Rec601Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rec601settings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.Rec709Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rec709settings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.RemixSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-remixsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.RtmpCaptionInfoDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpcaptioninfodestinationsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.RtmpGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.RtmpOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.Scte20PlusEmbeddedDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20plusembeddeddestinationsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.Scte27DestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte27destinationsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.Scte35SpliceInsert](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35spliceinsert.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.Scte35TimeSignalApos](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35timesignalapos.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.SmpteTtDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-smptettdestinationsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.StandardHlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-standardhlssettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.StaticKeySettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-statickeysettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.TeletextDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-teletextdestinationsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.TemporalFilterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-temporalfiltersettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.TimecodeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-timecodeconfig.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.TtmlDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ttmldestinationsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.UdpContainerSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpcontainersettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.UdpGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpgroupsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.UdpOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.VideoCodecSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.VideoDescription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.WebvttDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-webvttdestinationsettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Input.InputDeviceRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicerequest.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::MediaLive::Input.InputDeviceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicesettings.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `us-east-1`

- [AWS::Route53::HostedZone.HostedZoneConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzoneconfig.html)
  - Now available to **ALL** regions.

- [AWS::Route53::HostedZone.QueryLoggingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-queryloggingconfig.html)
  - Now available to **ALL** regions.

- [AWS::Route53Resolver::ResolverEndpoint.IpAddressRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html)
  - `ap-southeast-2`

- [AWS::Route53Resolver::ResolverRule.TargetAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html)
  - `ap-southeast-2`

- [AWS::StepFunctions::StateMachine.CloudWatchLogsLogGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup.html)
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-west-2`
  - `us-west-1`
  - `ap-southeast-2`

- [AWS::StepFunctions::StateMachine.DefinitionSubstitutions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-definitionsubstitutions.html)
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-west-2`
  - `us-west-1`
  - `ap-southeast-2`

- [AWS::StepFunctions::StateMachine.LogDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html)
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-west-2`
  - `us-west-1`
  - `ap-southeast-2`

- [AWS::StepFunctions::StateMachine.LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html)
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-west-2`
  - `us-west-1`
  - `ap-southeast-2`

- [AWS::StepFunctions::StateMachine.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html)
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-west-2`
  - `us-west-1`
  - `ap-southeast-2`

- [AWS::StepFunctions::StateMachine.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html)
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-west-2`
  - `us-west-1`
  - `ap-southeast-2`

- [AWS::StepFunctions::StateMachine.TracingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tracingconfiguration.html)
  - `ap-south-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`
  - `ap-east-1`
  - `ap-northeast-2`
  - `ca-central-1`
  - `eu-west-2`
  - `us-west-1`
  - `ap-southeast-2`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v18.3.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.3.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.3.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

- PropertyType Still Missing
  - Since v18.3.0: [AWS::AppSync::FunctionConfiguration.LambdaConflictHandlerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html)
    - `ap-northeast-2`

  - Since v18.3.0: [AWS::AppSync::FunctionConfiguration.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html)
    - `ap-northeast-2`

  - Since v18.3.0: [AWS::ECS::Cluster.ClusterSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersetting.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `eu-south-1`

  - Since v18.3.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.3.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.3.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.3.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.3.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.3.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v18.3.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

## [18.3.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.3.0) (2020-09-10)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v18-changelog.json)
  - Change source is a diff between [v18.3.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.3.0) and [v18.2.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.2.0)

### Totals

- TotalPropertyTypes: 1659 **(+50)**
- TotalPropertyTypesSupportedGlobally: 488 **(+0)**
- TotalResourceTypes: 568 **(+6)**
- TotalResourceTypesSupportedGlobally: 187 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::IoT::Authorizer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::Kendra::DataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::Faq](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::Index](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::SSO::Assignment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html)
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
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::SSO::PermissionSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html)
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
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::IoT::Authorizer.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-authorizer-tags.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::IoT::Authorizer.TokenSigningPublicKeys](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-authorizer-tokensigningpublickeys.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.AccessControlListConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-accesscontrollistconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.AclConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-aclconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.ChangeDetectingColumns](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-changedetectingcolumns.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.ColumnConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.ConnectionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.DataSourceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.DataSourceInclusionsExclusionsStrings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceinclusionsexclusionsstrings.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.DataSourceToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmapping.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.DataSourceToIndexFieldMappingList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmappinglist.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.DataSourceVpcConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcevpcconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.DatabaseConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.DocumentsMetadataConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentsmetadataconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.OneDriveConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.OneDriveUserList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveuserlist.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.OneDriveUsers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveusers.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.S3DataSourceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.S3Path](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3path.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.SalesforceChatterFeedConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.SalesforceChatterFeedIncludeFilterTypes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedincludefiltertypes.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.SalesforceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.SalesforceCustomKnowledgeArticleTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.SalesforceCustomKnowledgeArticleTypeConfigurationList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfigurationlist.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.SalesforceKnowledgeArticleConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.SalesforceKnowledgeArticleStateList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticlestatelist.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.SalesforceStandardKnowledgeArticleTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.SalesforceStandardObjectAttachmentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.SalesforceStandardObjectConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.SalesforceStandardObjectConfigurationList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfigurationlist.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.ServiceNowConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.ServiceNowKnowledgeArticleConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.ServiceNowServiceCatalogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.SharePointConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.SqlConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sqlconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::DataSource.TagList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-taglist.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::Faq.S3Path](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-faq-s3path.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::Faq.TagList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-faq-taglist.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::Index.CapacityUnitsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-capacityunitsconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::Index.DocumentMetadataConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::Index.DocumentMetadataConfigurationList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfigurationlist.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::Index.Relevance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::Index.Search](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::Index.ServerSideEncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-serversideencryptionconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::Index.TagList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-taglist.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::Index.ValueImportanceItem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-valueimportanceitem.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::Kendra::Index.ValueImportanceItems](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-valueimportanceitems.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::LakeFormation::Permissions.TableWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewildcard.html)
  - `ap-northeast-1`
  - `us-west-2`

- [AWS::MSK::Cluster.Sasl](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::MSK::Cluster.Scram](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-scram.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Chatbot::SlackChannelConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html)
  - `me-south-1`
  - `ap-east-1`

- [AWS::StepFunctions::StateMachine](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html)
  - `ap-southeast-1`
  - `cn-north-1`

- [AWS::ECR::Repository.LifecyclePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-lifecyclepolicy.html)
  - `ap-south-1`
  - `eu-west-2`
  - `ap-southeast-2`
  - `us-west-1`
  - `ca-central-1`
  - `eu-west-3`
  - `ap-northeast-2`
  - `sa-east-1`
  - `eu-north-1`
  - `us-east-2`
  - `eu-west-1`
  - `ap-east-1`

- [AWS::MediaLive::Channel.AacSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.Ac3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.ArchiveContainerSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecontainersettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.ArchiveGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivegroupsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.ArchiveOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archiveoutputsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.AribDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aribdestinationsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.AudioChannelMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiochannelmapping.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.AudioCodecSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.AudioDescription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.AudioNormalizationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audionormalizationsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.AudioOnlyHlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.AudioTrack](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrack.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.AudioTrackSelection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrackselection.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.AutomaticInputFailoverSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-automaticinputfailoversettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.AvailBlanking](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availblanking.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.AvailConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availconfiguration.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.AvailSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.BlackoutSlate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.BurnInDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.CaptionDescription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.CaptionDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.CaptionLanguageMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionlanguagemapping.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.ColorSpacePassthroughSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-colorspacepassthroughsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.DvbNitSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbnitsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.DvbSdtSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.DvbSubDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.DvbTdtSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbtdtsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.Eac3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.EbuTtDDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.EmbeddedDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddeddestinationsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.EmbeddedPlusScte20DestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedplusscte20destinationsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.EncoderSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.FeatureActivations](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-featureactivations.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.FecOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fecoutputsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.Fmp4HlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fmp4hlssettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.FrameCaptureGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturegroupsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.FrameCaptureOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptureoutputsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.FrameCaptureSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturesettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.GlobalConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.H264ColorSpaceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264colorspacesettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.H264FilterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264filtersettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.H264Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.H265ColorSpaceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.H265FilterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265filtersettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.H265Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.Hdr10Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hdr10settings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.HlsAkamaiSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.HlsBasicPutSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.HlsCdnSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.HlsGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.HlsMediaStoreSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.HlsOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.HlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.HlsWebdavSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.InputChannelLevel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputchannellevel.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.InputLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlocation.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.InputLossBehavior](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.KeyProviderSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-keyprovidersettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.M2tsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.M3u8Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.MediaPackageGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackagegroupsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.MediaPackageOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackageoutputsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.Mp2Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.MsSmoothGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.MsSmoothOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothoutputsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.MultiplexGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexgroupsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.MultiplexOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexoutputsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.NielsenConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenconfiguration.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.OutputGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroup.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.OutputGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.OutputLocationRef](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputlocationref.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.OutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.PassThroughSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-passthroughsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.Rec601Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rec601settings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.Rec709Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rec709settings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.RemixSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-remixsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.RtmpCaptionInfoDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpcaptioninfodestinationsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.RtmpGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.RtmpOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.Scte20PlusEmbeddedDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20plusembeddeddestinationsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.Scte27DestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte27destinationsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.Scte35SpliceInsert](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35spliceinsert.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.Scte35TimeSignalApos](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35timesignalapos.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.SmpteTtDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-smptettdestinationsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.StandardHlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-standardhlssettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.StaticKeySettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-statickeysettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.TeletextDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-teletextdestinationsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.TemporalFilterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-temporalfiltersettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.TimecodeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-timecodeconfig.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.TtmlDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ttmldestinationsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.UdpContainerSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpcontainersettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.UdpGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpgroupsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.UdpOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.VideoCodecSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.VideoDescription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Channel.WebvttDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-webvttdestinationsettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Input.InputDeviceRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicerequest.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::MediaLive::Input.InputDeviceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicesettings.html)
  - `ap-south-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `us-west-2`
  - `eu-west-1`
  - `ap-northeast-1`

- [AWS::StepFunctions::StateMachine.CloudWatchLogsLogGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup.html)
  - `ap-southeast-1`
  - `cn-north-1`

- [AWS::StepFunctions::StateMachine.DefinitionSubstitutions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-definitionsubstitutions.html)
  - `ap-southeast-1`
  - `cn-north-1`

- [AWS::StepFunctions::StateMachine.LogDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html)
  - `ap-southeast-1`
  - `cn-north-1`

- [AWS::StepFunctions::StateMachine.LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html)
  - `ap-southeast-1`
  - `cn-north-1`

- [AWS::StepFunctions::StateMachine.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html)
  - `ap-southeast-1`
  - `cn-north-1`

- [AWS::StepFunctions::StateMachine.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html)
  - `ap-southeast-1`
  - `cn-north-1`

- [AWS::StepFunctions::StateMachine.TracingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tracingconfiguration.html)
  - `ap-southeast-1`
  - `cn-north-1`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
  - `eu-west-2`
  - `us-west-1`
  - `eu-west-3`
  - `ap-northeast-2`
  - `eu-north-1`
  - `us-east-2`
  - `me-south-1`
  - `ap-northeast-3`
  - `ap-east-1`

- [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
  - `eu-west-2`
  - `us-west-1`
  - `eu-west-3`
  - `ap-northeast-2`
  - `eu-north-1`
  - `us-east-2`
  - `me-south-1`
  - `ap-northeast-3`
  - `ap-east-1`

- [AWS::Route53::HostedZone.HostedZoneConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzoneconfig.html)
  - `us-west-2`

- [AWS::Route53::HostedZone.QueryLoggingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-queryloggingconfig.html)
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v18.2.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.2.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.2.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

- PropertyType Still Missing
  - Since v18.2.0: [AWS::AppSync::FunctionConfiguration.LambdaConflictHandlerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html)
    - `ap-northeast-2`

  - Since v18.2.0: [AWS::AppSync::FunctionConfiguration.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html)
    - `ap-northeast-2`

  - Since v18.2.0: [AWS::ECS::Cluster.ClusterSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersetting.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `eu-south-1`

  - Since v18.2.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.2.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.2.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.2.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.2.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.AacSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.Ac3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.ArchiveContainerSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecontainersettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.ArchiveGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivegroupsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.ArchiveOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archiveoutputsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.AribDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aribdestinationsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.AudioChannelMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiochannelmapping.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.AudioCodecSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.AudioDescription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.AudioNormalizationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audionormalizationsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.AudioOnlyHlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.AudioTrack](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrack.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.AudioTrackSelection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrackselection.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.AutomaticInputFailoverSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-automaticinputfailoversettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.AvailBlanking](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availblanking.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.AvailConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availconfiguration.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.AvailSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.BlackoutSlate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.BurnInDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.CaptionDescription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.CaptionDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.CaptionLanguageMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionlanguagemapping.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.ColorSpacePassthroughSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-colorspacepassthroughsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.DvbNitSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbnitsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.DvbSdtSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.DvbSubDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.DvbTdtSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbtdtsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.Eac3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.EbuTtDDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.EmbeddedDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddeddestinationsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.EmbeddedPlusScte20DestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedplusscte20destinationsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.EncoderSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.FeatureActivations](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-featureactivations.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.FecOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fecoutputsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.Fmp4HlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fmp4hlssettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.FrameCaptureGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturegroupsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.FrameCaptureOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptureoutputsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.FrameCaptureSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturesettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.GlobalConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.H264ColorSpaceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264colorspacesettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.H264FilterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264filtersettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.H264Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.H265ColorSpaceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.H265FilterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265filtersettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.H265Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.Hdr10Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hdr10settings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.HlsAkamaiSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.HlsBasicPutSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.HlsCdnSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.HlsGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.HlsMediaStoreSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.HlsOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.HlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.HlsWebdavSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.InputChannelLevel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputchannellevel.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.InputLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlocation.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.InputLossBehavior](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.KeyProviderSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-keyprovidersettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.M2tsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.M3u8Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.MediaPackageGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackagegroupsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.MediaPackageOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackageoutputsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.Mp2Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.MsSmoothGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.MsSmoothOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothoutputsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.MultiplexGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexgroupsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.MultiplexOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexoutputsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.NielsenConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenconfiguration.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.OutputGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroup.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.OutputGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.OutputLocationRef](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputlocationref.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.OutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.PassThroughSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-passthroughsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.Rec601Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rec601settings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.Rec709Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rec709settings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.RemixSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-remixsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.RtmpCaptionInfoDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpcaptioninfodestinationsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.RtmpGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.RtmpOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.Scte20PlusEmbeddedDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20plusembeddeddestinationsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.Scte27DestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte27destinationsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.Scte35SpliceInsert](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35spliceinsert.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.Scte35TimeSignalApos](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35timesignalapos.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.SmpteTtDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-smptettdestinationsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.StandardHlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-standardhlssettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.StaticKeySettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-statickeysettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.TeletextDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-teletextdestinationsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.TemporalFilterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-temporalfiltersettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.TimecodeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-timecodeconfig.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.TtmlDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ttmldestinationsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.UdpContainerSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpcontainersettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.UdpGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpgroupsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.UdpOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.VideoCodecSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.VideoDescription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Channel.WebvttDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-webvttdestinationsettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Input.InputDeviceRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicerequest.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::MediaLive::Input.InputDeviceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicesettings.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-west-1`
    - `us-west-2`

  - Since v18.2.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v18.2.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::LakeFormation::Permissions.TableWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewildcard.html)
    - `ap-northeast-1`
    - `us-west-2`

## [18.2.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.2.0) (2020-09-05)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v18-changelog.json)
  - Change source is a diff between [v18.2.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.2.0) and [v18.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.1.0)

### Totals

- TotalPropertyTypes: 1609 **(+121)**
- TotalPropertyTypesSupportedGlobally: 488 **(+-1)**
- TotalResourceTypes: 562 **(+5)**
- TotalResourceTypesSupportedGlobally: 187 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::CloudFront::CachePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cachepolicy.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFront::OriginRequestPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originrequestpolicy.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFront::RealtimeLogConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-realtimelogconfig.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::EKS::FargateProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::GameLift::GameServerGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFront::CachePolicy.CachePolicyConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cachepolicyconfig.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFront::CachePolicy.CookiesConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-cookiesconfig.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFront::CachePolicy.HeadersConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-headersconfig.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFront::CachePolicy.ParametersInCacheKeyAndForwardedToOrigin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-parametersincachekeyandforwardedtoorigin.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFront::CachePolicy.QueryStringsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cachepolicy-querystringsconfig.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFront::OriginRequestPolicy.CookiesConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-cookiesconfig.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFront::OriginRequestPolicy.HeadersConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-headersconfig.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFront::OriginRequestPolicy.OriginRequestPolicyConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-originrequestpolicyconfig.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFront::OriginRequestPolicy.QueryStringsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originrequestpolicy-querystringsconfig.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFront::RealtimeLogConfig.EndPoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-endpoint.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFront::RealtimeLogConfig.KinesisStreamConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-realtimelogconfig-kinesisstreamconfig.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::EKS::FargateProfile.Label](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-label.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::EKS::FargateProfile.Selector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-selector.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::GameLift::GameServerGroup.AutoScalingPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-autoscalingpolicy.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::GameLift::GameServerGroup.InstanceDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-instancedefinition.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::GameLift::GameServerGroup.InstanceDefinitions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-instancedefinitions.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::GameLift::GameServerGroup.LaunchTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-launchtemplate.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::GameLift::GameServerGroup.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-tags.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::GameLift::GameServerGroup.TargetTrackingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-targettrackingconfiguration.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::GameLift::GameServerGroup.VpcSubnets](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-vpcsubnets.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Macie::FindingsFilter.FindingsFilterListItem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingsfilterlistitem.html)
  - `ap-east-1`
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

- [AWS::MediaLive::Channel.AacSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.Ac3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.ArchiveContainerSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecontainersettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.ArchiveGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivegroupsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.ArchiveOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archiveoutputsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.AribDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aribdestinationsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.AudioChannelMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiochannelmapping.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.AudioCodecSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.AudioDescription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.AudioNormalizationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audionormalizationsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.AudioOnlyHlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.AudioTrack](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrack.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.AudioTrackSelection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrackselection.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.AutomaticInputFailoverSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-automaticinputfailoversettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.AvailBlanking](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availblanking.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.AvailConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availconfiguration.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.AvailSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.BlackoutSlate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.BurnInDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.CaptionDescription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.CaptionDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.CaptionLanguageMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionlanguagemapping.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.ColorSpacePassthroughSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-colorspacepassthroughsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.DvbNitSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbnitsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.DvbSdtSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.DvbSubDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.DvbTdtSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbtdtsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.Eac3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.EbuTtDDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.EmbeddedDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddeddestinationsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.EmbeddedPlusScte20DestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedplusscte20destinationsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.EncoderSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.FeatureActivations](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-featureactivations.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.FecOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fecoutputsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.Fmp4HlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fmp4hlssettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.FrameCaptureGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturegroupsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.FrameCaptureOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptureoutputsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.FrameCaptureSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturesettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.GlobalConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.H264ColorSpaceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264colorspacesettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.H264FilterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264filtersettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.H264Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.H265ColorSpaceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.H265FilterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265filtersettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.H265Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.Hdr10Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hdr10settings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.HlsAkamaiSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.HlsBasicPutSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.HlsCdnSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.HlsGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.HlsMediaStoreSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.HlsOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.HlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.HlsWebdavSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.InputChannelLevel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputchannellevel.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.InputLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlocation.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.InputLossBehavior](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.KeyProviderSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-keyprovidersettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.M2tsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.M3u8Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.MediaPackageGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackagegroupsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.MediaPackageOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackageoutputsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.Mp2Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.MsSmoothGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.MsSmoothOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothoutputsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.MultiplexGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexgroupsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.MultiplexOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexoutputsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.NielsenConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenconfiguration.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.OutputGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroup.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.OutputGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.OutputLocationRef](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputlocationref.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.OutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.PassThroughSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-passthroughsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.Rec601Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rec601settings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.Rec709Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rec709settings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.RemixSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-remixsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.RtmpCaptionInfoDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpcaptioninfodestinationsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.RtmpGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.RtmpOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.Scte20PlusEmbeddedDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20plusembeddeddestinationsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.Scte27DestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte27destinationsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.Scte35SpliceInsert](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35spliceinsert.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.Scte35TimeSignalApos](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35timesignalapos.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.SmpteTtDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-smptettdestinationsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.StandardHlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-standardhlssettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.StaticKeySettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-statickeysettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.TeletextDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-teletextdestinationsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.TemporalFilterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-temporalfiltersettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.TimecodeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-timecodeconfig.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.TtmlDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ttmldestinationsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.UdpContainerSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpcontainersettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.UdpGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpgroupsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.UdpOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.VideoCodecSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.VideoDescription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html)
  - `eu-central-1`

- [AWS::MediaLive::Channel.WebvttDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-webvttdestinationsettings.html)
  - `eu-central-1`

- [AWS::MediaLive::Input.InputDeviceRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicerequest.html)
  - `eu-central-1`

- [AWS::MediaLive::Input.InputDeviceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicesettings.html)
  - `eu-central-1`

- [AWS::Neptune::DBCluster.DBClusterRole](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-neptune-dbcluster-dbclusterrole.html)
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Cassandra::Keyspace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::Cassandra::Table](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::CloudWatch::InsightRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html)
  - `cn-north-1`

- [AWS::CodeGuruReviewer::RepositoryAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codegurureviewer-repositoryassociation.html)
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-north-1`
  - `us-east-1`
  - `eu-west-1`

- [AWS::Detective::Graph](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html)
  - `me-south-1`
  - `ap-east-1`

- [AWS::Detective::MemberInvitation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html)
  - `me-south-1`
  - `ap-east-1`

- [AWS::Cassandra::Table.BillingMode](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-billingmode.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::Cassandra::Table.ClusteringKeyColumn](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-clusteringkeycolumn.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::Cassandra::Table.Column](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-column.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::Cassandra::Table.ProvisionedThroughput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-provisionedthroughput.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::CloudWatch::InsightRule.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-insightrule-tags.html)
  - `cn-north-1`

- [AWS::Cognito::UserPoolClient.TokenValidityUnits](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-tokenvalidityunits.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-2`

- [AWS::ECR::Repository.LifecyclePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-lifecyclepolicy.html)
  - `ap-southeast-1`
  - `us-west-2`
  - `ap-northeast-1`
  - `us-east-1`
  - `eu-central-1`

- [AWS::SSM::Association.ParameterValues](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-parametervalues.html)
  - Now available to **ALL** regions.

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::StepFunctions::StateMachine](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html)
  - `ap-southeast-1`

- [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ap-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `ca-central-1`
  - `eu-west-1`

- [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ap-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `ca-central-1`
  - `eu-west-1`

- [AWS::Route53::HostedZone.HostedZoneConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzoneconfig.html)
  - `ap-northeast-1`
  - `eu-central-1`

- [AWS::Route53::HostedZone.QueryLoggingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-queryloggingconfig.html)
  - `ap-northeast-1`
  - `eu-central-1`

- [AWS::StepFunctions::StateMachine.CloudWatchLogsLogGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination-cloudwatchlogsloggroup.html)
  - `ap-southeast-1`

- [AWS::StepFunctions::StateMachine.DefinitionSubstitutions]()
  - `ap-southeast-1`

- [AWS::StepFunctions::StateMachine.LogDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html)
  - `ap-southeast-1`

- [AWS::StepFunctions::StateMachine.LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html)
  - `ap-southeast-1`

- [AWS::StepFunctions::StateMachine.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html)
  - `ap-southeast-1`

- [AWS::StepFunctions::StateMachine.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html)
  - `ap-southeast-1`

- [AWS::StepFunctions::StateMachine.TracingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tracingconfiguration.html)
  - `ap-southeast-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v18.1.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.1.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.1.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

- PropertyType Still Missing
  - Since v18.1.0: [AWS::AppSync::FunctionConfiguration.LambdaConflictHandlerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html)
    - `ap-northeast-2`

  - Since v18.1.0: [AWS::AppSync::FunctionConfiguration.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html)
    - `ap-northeast-2`

  - Since v18.1.0: [AWS::ECS::Cluster.ClusterSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersetting.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `eu-south-1`

  - Since v18.1.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.1.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.1.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.1.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.1.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.1.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `ap-east-1`
    - `ap-northeast-2`
    - `ap-northeast-3`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-north-1`
    - `eu-south-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `us-east-2`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `us-west-1`

  - Since v18.1.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `ap-east-1`
    - `ap-northeast-2`
    - `ap-northeast-3`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-north-1`
    - `eu-south-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `us-east-2`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `us-west-1`

- New PropertyType(s) Missing
  - [AWS::MediaLive::Channel.AacSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aacsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.Ac3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ac3settings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.ArchiveContainerSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivecontainersettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.ArchiveGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archivegroupsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.ArchiveOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-archiveoutputsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.AribDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aribdestinationsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.AudioChannelMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiochannelmapping.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.AudioCodecSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiocodecsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.AudioDescription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiodescription.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.AudioNormalizationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audionormalizationsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.AudioOnlyHlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioonlyhlssettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.AudioTrack](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrack.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.AudioTrackSelection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiotrackselection.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.AutomaticInputFailoverSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-automaticinputfailoversettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.AvailBlanking](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availblanking.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.AvailConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availconfiguration.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.AvailSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-availsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.BlackoutSlate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-blackoutslate.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.BurnInDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-burnindestinationsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.CaptionDescription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondescription.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.CaptionDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captiondestinationsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.CaptionLanguageMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionlanguagemapping.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.ColorSpacePassthroughSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-colorspacepassthroughsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.DvbNitSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbnitsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.DvbSdtSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsdtsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.DvbSubDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubdestinationsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.DvbTdtSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbtdtsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.Eac3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-eac3settings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.EbuTtDDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ebuttddestinationsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.EmbeddedDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddeddestinationsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.EmbeddedPlusScte20DestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedplusscte20destinationsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.EncoderSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-encodersettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.FeatureActivations](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-featureactivations.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.FecOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fecoutputsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.Fmp4HlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-fmp4hlssettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.FrameCaptureGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturegroupsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.FrameCaptureOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecaptureoutputsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.FrameCaptureSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-framecapturesettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.GlobalConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-globalconfiguration.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.H264ColorSpaceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264colorspacesettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.H264FilterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264filtersettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.H264Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h264settings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.H265ColorSpaceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265colorspacesettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.H265FilterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265filtersettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.H265Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-h265settings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.Hdr10Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hdr10settings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.HlsAkamaiSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsakamaisettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.HlsBasicPutSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsbasicputsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.HlsCdnSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlscdnsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.HlsGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsgroupsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.HlsMediaStoreSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsmediastoresettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.HlsOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsoutputsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.HlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlssettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.HlsWebdavSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlswebdavsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.InputChannelLevel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputchannellevel.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.InputLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlocation.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.InputLossBehavior](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputlossbehavior.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.KeyProviderSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-keyprovidersettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.M2tsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m2tssettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.M3u8Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-m3u8settings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.MediaPackageGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackagegroupsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.MediaPackageOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackageoutputsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.Mp2Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mp2settings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.MsSmoothGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothgroupsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.MsSmoothOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mssmoothoutputsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.MultiplexGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexgroupsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.MultiplexOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexoutputsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.NielsenConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenconfiguration.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-output.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.OutputGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroup.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.OutputGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputgroupsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.OutputLocationRef](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputlocationref.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.OutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.PassThroughSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-passthroughsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.Rec601Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rec601settings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.Rec709Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rec709settings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.RemixSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-remixsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.RtmpCaptionInfoDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpcaptioninfodestinationsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.RtmpGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpgroupsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.RtmpOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-rtmpoutputsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.Scte20PlusEmbeddedDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20plusembeddeddestinationsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.Scte27DestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte27destinationsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.Scte35SpliceInsert](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35spliceinsert.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.Scte35TimeSignalApos](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte35timesignalapos.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.SmpteTtDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-smptettdestinationsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.StandardHlsSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-standardhlssettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.StaticKeySettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-statickeysettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.TeletextDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-teletextdestinationsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.TemporalFilterSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-temporalfiltersettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.TimecodeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-timecodeconfig.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.TtmlDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-ttmldestinationsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.UdpContainerSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpcontainersettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.UdpGroupSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpgroupsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.UdpOutputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-udpoutputsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.VideoCodecSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videocodecsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.VideoDescription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videodescription.html)
    - `eu-central-1`

  - [AWS::MediaLive::Channel.WebvttDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-webvttdestinationsettings.html)
    - `eu-central-1`

  - [AWS::MediaLive::Input.InputDeviceRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicerequest.html)
    - `eu-central-1`

  - [AWS::MediaLive::Input.InputDeviceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdevicesettings.html)
    - `eu-central-1`

## [18.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.1.0) (2020-08-28)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v18-changelog.json)
  - Change source is a diff between [v18.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.1.0) and [v18.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.0.0)

### Totals

- TotalPropertyTypes: 1488 **(+3)**
- TotalPropertyTypesSupportedGlobally: 489 **(+0)**
- TotalResourceTypes: 557 **(+3)**
- TotalResourceTypesSupportedGlobally: 187 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::CodeGuruReviewer::RepositoryAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codegurureviewer-repositoryassociation.html)
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::Route53Resolver::ResolverQueryLoggingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html)
  - `ap-east-1`
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html)
  - `ap-east-1`
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Cognito::UserPoolClient.TokenValidityUnits](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-tokenvalidityunits.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-2`
  - `us-west-2`

- [AWS::GuardDuty::Detector.CFNDataSourceConfigurations](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html)
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

- [AWS::GuardDuty::Detector.CFNS3LogsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfns3logsconfiguration.html)
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

- [AWS::Athena::NamedQuery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html)
  - `cn-northwest-1`
  - `cn-north-1`
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Athena::WorkGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html)
  - `cn-north-1`

- [AWS::ManagedBlockchain::Member](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html)
  - `eu-west-2`

- [AWS::ManagedBlockchain::Node](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-node.html)
  - `eu-west-2`

- [AWS::Athena::WorkGroup.EncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html)
  - `cn-north-1`

- [AWS::Athena::WorkGroup.ResultConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html)
  - `cn-north-1`

- [AWS::Athena::WorkGroup.ResultConfigurationUpdates](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html)
  - `cn-north-1`

- [AWS::Athena::WorkGroup.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-tags.html)
  - `cn-north-1`

- [AWS::Athena::WorkGroup.WorkGroupConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html)
  - `cn-north-1`

- [AWS::Athena::WorkGroup.WorkGroupConfigurationUpdates](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html)
  - `cn-north-1`

- [AWS::ManagedBlockchain::Member.ApprovalThresholdPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-approvalthresholdpolicy.html)
  - `eu-west-2`

- [AWS::ManagedBlockchain::Member.MemberConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberconfiguration.html)
  - `eu-west-2`

- [AWS::ManagedBlockchain::Member.MemberFabricConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberfabricconfiguration.html)
  - `eu-west-2`

- [AWS::ManagedBlockchain::Member.MemberFrameworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberframeworkconfiguration.html)
  - `eu-west-2`

- [AWS::ManagedBlockchain::Member.NetworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkconfiguration.html)
  - `eu-west-2`

- [AWS::ManagedBlockchain::Member.NetworkFabricConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkfabricconfiguration.html)
  - `eu-west-2`

- [AWS::ManagedBlockchain::Member.NetworkFrameworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkframeworkconfiguration.html)
  - `eu-west-2`

- [AWS::ManagedBlockchain::Member.VotingPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-votingpolicy.html)
  - `eu-west-2`

- [AWS::ManagedBlockchain::Node.NodeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-node-nodeconfiguration.html)
  - `eu-west-2`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v18.0.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.0.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.0.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

- New ResourceType(s) Missing
  - [AWS::CodeGuruReviewer::RepositoryAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codegurureviewer-repositoryassociation.html)
    - `ap-northeast-1`
    - `eu-central-1`
    - `us-west-2`

- PropertyType Still Missing
  - Since v18.0.0: [AWS::AppSync::FunctionConfiguration.LambdaConflictHandlerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html)
    - `ap-northeast-2`

  - Since v18.0.0: [AWS::AppSync::FunctionConfiguration.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html)
    - `ap-northeast-2`

  - Since v18.0.0: [AWS::ECR::Repository.LifecyclePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-lifecyclepolicy.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v18.0.0: [AWS::ECS::Cluster.ClusterSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersetting.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `eu-south-1`

  - Since v18.0.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.0.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.0.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.0.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.0.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v18.0.0: [AWS::SSM::Association.ParameterValues](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-parametervalues.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `eu-south-1`

- New PropertyType(s) Missing
  - [AWS::Cognito::UserPoolClient.TokenValidityUnits](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-tokenvalidityunits.html)
    - `ap-northeast-1`
    - `ap-south-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `ca-central-1`
    - `eu-central-1`
    - `eu-west-2`
    - `us-east-2`
    - `us-west-2`

## [18.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.0.0) (2020-08-24)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v18-changelog.json)
  - Change source is a diff between [v18.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v18.0.0) and [v17.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v17.0.0)

### Totals

- TotalPropertyTypes: 1485 **(+1)**
- TotalPropertyTypesSupportedGlobally: 489 **(+2)**
- TotalResourceTypes: 554 **(+0)**
- TotalResourceTypesSupportedGlobally: 187 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::AppSync::FunctionConfiguration.LambdaConflictHandlerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html)
  - `ap-northeast-2`

- [AWS::AppSync::FunctionConfiguration.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html)
  - `ap-northeast-2`

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::ECS::TaskDefinition.Options](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-options.html)
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

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::ApplicationInsights::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.Alarm](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarm.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.AlarmMetric](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarmmetric.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.ComponentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentconfiguration.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.ComponentMonitoringSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.ConfigurationDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.CustomComponent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-customcomponent.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.Log](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.LogPattern](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.LogPatternSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpatternset.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.SubComponentConfigurationDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.SubComponentTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponenttypeconfiguration.html)
  - `eu-central-1`

- [AWS::ApplicationInsights::Application.WindowsEvent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html)
  - `eu-central-1`

- [AWS::ECS::TaskDefinition.EnvironmentFile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-environmentfile.html)
  - `eu-central-1`

- [AWS::EKS::Nodegroup.LaunchTemplateSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-launchtemplatespecification.html)
  - `eu-central-1`

- [AWS::KinesisFirehose::DeliveryStream.HttpEndpointCommonAttribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html)
  - `ap-east-1`

- [AWS::KinesisFirehose::DeliveryStream.HttpEndpointConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html)
  - `ap-east-1`

- [AWS::KinesisFirehose::DeliveryStream.HttpEndpointDestinationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html)
  - `ap-east-1`

- [AWS::KinesisFirehose::DeliveryStream.HttpEndpointRequestConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html)
  - `ap-east-1`

- [AWS::KinesisFirehose::DeliveryStream.RetryOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-retryoptions.html)
  - `ap-east-1`

- [AWS::Route53::HostedZone.HostedZoneConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzoneconfig.html)
  - Now available to **ALL** regions.

- [AWS::Route53::HostedZone.QueryLoggingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-queryloggingconfig.html)
  - Now available to **ALL** regions.

- [AWS::SageMaker::MonitoringSchedule.BaselineConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-baselineconfig.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.ClusterConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.ConstraintsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-constraintsresource.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.EndpointInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-environment.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.MonitoringAppSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.MonitoringExecutionSummary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.MonitoringInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringinput.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.MonitoringInputs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringinputs.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.MonitoringJobDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.MonitoringOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutput.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.MonitoringOutputConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutputconfig.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.MonitoringResources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringresources.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.MonitoringScheduleConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.NetworkConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.S3Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.ScheduleConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-scheduleconfig.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.StatisticsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-statisticsresource.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.StoppingCondition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-stoppingcondition.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-vpcconfig.html)
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::StepFunctions::StateMachine](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html)
  - `cn-north-1`

- [AWS::ECR::Repository.LifecyclePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-lifecyclepolicy.html)
  - `us-west-1`
  - `ap-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `sa-east-1`
  - `eu-west-2`
  - `me-south-1`
  - `ap-southeast-2`
  - `eu-west-3`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-2`
  - `ca-central-1`
  - `eu-central-1`

- [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
  - `eu-central-1`

- [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
  - `eu-central-1`

- [AWS::StepFunctions::StateMachine.CloudWatchLogsLogGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup.html)
  - `cn-north-1`

- [AWS::StepFunctions::StateMachine.DefinitionSubstitutions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-definitionsubstitutions.html)
  - `cn-north-1`

- [AWS::StepFunctions::StateMachine.LogDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html)
  - `cn-north-1`

- [AWS::StepFunctions::StateMachine.LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html)
  - `cn-north-1`

- [AWS::StepFunctions::StateMachine.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html)
  - `cn-north-1`

- [AWS::StepFunctions::StateMachine.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html)
  - `cn-north-1`

- [AWS::StepFunctions::StateMachine.TracingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tracingconfiguration.html)
  - `cn-north-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v17.0.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v17.0.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v17.0.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

- PropertyType Still Missing
  - Since v17.0.0: [AWS::ECR::Repository.LifecyclePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-lifecyclepolicy.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v17.0.0: [AWS::ECS::Cluster.ClusterSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersetting.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `eu-south-1`

  - Since v17.0.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v17.0.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v17.0.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v17.0.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v17.0.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v17.0.0: [AWS::SSM::Association.ParameterValues](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-parametervalues.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `eu-south-1`

- New PropertyType(s) Missing
  - [AWS::AppSync::FunctionConfiguration.LambdaConflictHandlerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html)
    - `ap-northeast-2`

  - [AWS::AppSync::FunctionConfiguration.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html)
    - `ap-northeast-2`

