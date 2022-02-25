# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v58-changelog.json`](changelogs/v58-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [58.0.0](#5800-2022-02-25)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [58.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v58.0.0) (2022-02-25)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v58-changelog.json)
  - Change source is a diff between [v58.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v58.0.0) and [v57.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v57.0.0)

### Totals

- TotalPropertyTypes: 2983 **(+9)**
- TotalPropertyTypesSupportedGlobally: 1065 **(+-1)**
- TotalResourceTypes: 891 **(+0)**
- TotalResourceTypesSupportedGlobally: 335 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::AppFlow::Flow.SAPODataDestinationProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatadestinationproperties.html)
  - `ap-southeast-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppFlow::Flow.SuccessResponseHandlingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-successresponsehandlingconfig.html)
  - `ap-southeast-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Events::Connection.ApiKeyAuthParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-apikeyauthparameters.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::Events::Connection.AuthParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-authparameters.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::Events::Connection.BasicAuthParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-basicauthparameters.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::Events::Connection.ClientParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-clientparameters.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::Events::Connection.ConnectionHttpParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-connectionhttpparameters.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::Events::Connection.OAuthParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-oauthparameters.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::Events::Connection.Parameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-connection-parameter.html)
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
  - `us-west-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::DataSync::LocationFSxLustre](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxlustre.html)
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-2`
  - `me-south-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `us-east-2`
  - `sa-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-northeast-3`
  - `us-east-1`
  - `us-west-2`
  - `eu-north-1`
  - `ap-east-1`
  - `us-gov-east-1`
  - `eu-west-3`
  - `eu-central-1`
  - `ap-south-1`
  - `us-gov-west-1`

- [AWS::SES::ConfigurationSetEventDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html)
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-2`
  - `me-south-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `sa-east-1`
  - `ap-northeast-1`
  - `ap-northeast-3`
  - `eu-north-1`
  - `eu-west-3`
  - `eu-central-1`
  - `ap-south-1`
  - `us-gov-west-1`

- [AWS::SES::Template](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html)
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-2`
  - `me-south-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `sa-east-1`
  - `ap-northeast-1`
  - `ap-northeast-3`
  - `eu-north-1`
  - `eu-west-3`
  - `eu-central-1`
  - `ap-south-1`
  - `us-gov-west-1`

- [AWS::SageMaker::FeatureGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html)
  - `ap-northeast-3`
  - `cn-north-1`

- [AWS::AmplifyUIBuilder::Component.ActionParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html)
  - `eu-west-2`
  - `me-south-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `sa-east-1`
  - `eu-west-1`
  - `us-east-1`
  - `eu-north-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::AmplifyUIBuilder::Component.ComponentEvent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentevent.html)
  - `eu-west-2`
  - `me-south-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `sa-east-1`
  - `eu-west-1`
  - `us-east-1`
  - `eu-north-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::AmplifyUIBuilder::Component.ComponentEvents](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentevents.html)
  - `eu-west-2`
  - `me-south-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `sa-east-1`
  - `eu-west-1`
  - `us-east-1`
  - `eu-north-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::AmplifyUIBuilder::Component.MutationActionSetStateParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-mutationactionsetstateparameter.html)
  - `eu-west-2`
  - `me-south-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `sa-east-1`
  - `eu-west-1`
  - `us-east-1`
  - `eu-north-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::AppMesh::Mesh.MeshServiceDiscovery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshservicediscovery.html)
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-2`
  - `me-south-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `sa-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `us-east-1`
  - `us-west-2`
  - `eu-north-1`
  - `ap-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::Lambda::EventSourceMapping.Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filter.html)
  - `cn-northwest-1`
  - `us-gov-east-1`
  - `ap-east-1`

- [AWS::Lambda::EventSourceMapping.FilterCriteria](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.html)
  - `cn-northwest-1`
  - `us-gov-east-1`
  - `ap-east-1`

- [AWS::SES::ConfigurationSetEventDestination.CloudWatchDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-cloudwatchdestination.html)
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-2`
  - `me-south-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `sa-east-1`
  - `ap-northeast-1`
  - `ap-northeast-3`
  - `eu-north-1`
  - `eu-west-3`
  - `eu-central-1`
  - `ap-south-1`
  - `us-gov-west-1`

- [AWS::SES::ConfigurationSetEventDestination.DimensionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html)
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-2`
  - `me-south-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `sa-east-1`
  - `ap-northeast-1`
  - `ap-northeast-3`
  - `eu-north-1`
  - `eu-west-3`
  - `eu-central-1`
  - `ap-south-1`
  - `us-gov-west-1`

- [AWS::SES::ConfigurationSetEventDestination.EventDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html)
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-2`
  - `me-south-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `sa-east-1`
  - `ap-northeast-1`
  - `ap-northeast-3`
  - `eu-north-1`
  - `eu-west-3`
  - `eu-central-1`
  - `ap-south-1`
  - `us-gov-west-1`

- [AWS::SES::ConfigurationSetEventDestination.KinesisFirehoseDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html)
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-2`
  - `me-south-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `sa-east-1`
  - `ap-northeast-1`
  - `ap-northeast-3`
  - `eu-north-1`
  - `eu-west-3`
  - `eu-central-1`
  - `ap-south-1`
  - `us-gov-west-1`

- [AWS::SES::Template.Template](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html)
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-2`
  - `me-south-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `sa-east-1`
  - `ap-northeast-1`
  - `ap-northeast-3`
  - `eu-north-1`
  - `eu-west-3`
  - `eu-central-1`
  - `ap-south-1`
  - `us-gov-west-1`

- [AWS::SageMaker::FeatureGroup.FeatureDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-featuredefinition.html)
  - `ap-northeast-3`
  - `cn-north-1`

- [AWS::WAFv2::WebACL.FieldIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldidentifier.html)
  - `ap-northeast-3`
  - `cn-northwest-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-2`
  - `me-south-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-east-1`
  - `eu-north-1`
  - `eu-west-3`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `eu-west-1`
  - `ap-south-1`

- [AWS::WAFv2::WebACL.ManagedRuleGroupConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupconfig.html)
  - `ap-northeast-3`
  - `cn-northwest-1`
  - `eu-south-1`
  - `af-south-1`
  - `eu-west-2`
  - `me-south-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-east-1`
  - `eu-north-1`
  - `eu-west-3`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-northeast-2`
  - `us-east-2`
  - `eu-west-1`
  - `ap-south-1`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
  - `cn-north-1`
  - `us-west-2`
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v57.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v57.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v57.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v57.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v57.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v57.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- PropertyType Still Missing
  - Since v57.0.0: [AWS::DevOpsGuru::ResourceCollection.TagCollection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-tagcollection.html)
    - `eu-central-1`

  - Since v57.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v57.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v57.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v57.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

