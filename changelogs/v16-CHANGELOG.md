# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v16-changelog.json`](changelogs/v16-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [16.0.0](#1600-2020-06-26)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [16.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v16.0.0) (2020-06-26)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v16-changelog.json)
  - Change source is a diff between [v16.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v16.0.0) and [v15.3.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v15.3.0)

### Totals

- TotalPropertyTypes: 1386 **(+11)**
- TotalPropertyTypesSupportedGlobally: 488 **(+0)**
- TotalResourceTypes: 544 **(+0)**
- TotalResourceTypesSupportedGlobally: 187 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::AppMesh::Route.GrpcTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpctimeout.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AppMesh::Route.HttpTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httptimeout.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AppMesh::Route.TcpTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcptimeout.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AppMesh::VirtualNode.Duration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-duration.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AppMesh::VirtualNode.GrpcTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-grpctimeout.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AppMesh::VirtualNode.HttpTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-httptimeout.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AppMesh::VirtualNode.ListenerTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AppMesh::VirtualNode.TcpTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tcptimeout.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::SageMaker::EndpointConfig.CaptureContentTypeHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html)
  - `us-west-2`

- [AWS::SageMaker::EndpointConfig.CaptureOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-captureoption.html)
  - `us-west-2`

- [AWS::SageMaker::EndpointConfig.DataCaptureConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html)
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::CloudWatch::InsightRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::EC2::LocalGatewayRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.html)
  - `sa-east-1`
  - `ap-south-1`

- [AWS::EC2::LocalGatewayRouteTableVPCAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetablevpcassociation.html)
  - `sa-east-1`
  - `ap-south-1`

- [AWS::CloudWatch::InsightRule.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-insightrule-tags.html)
  - `eu-south-1`
  - `af-south-1`

- [AWS::CodeBuild::Project.ProjectFileSystemLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::EC2::LocalGatewayRouteTableVPCAssociation.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-localgatewayroutetablevpcassociation-tags.html)
  - `sa-east-1`
  - `ap-south-1`

- [AWS::Glue::SecurityConfiguration.CloudWatchEncryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-cloudwatchencryption.html)
  - `cn-northwest-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v15.3.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `ap-southeast-2`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v15.3.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `ap-southeast-2`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v15.3.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `ap-southeast-2`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

- PropertyType Still Missing
  - Since v15.3.0: [AWS::ECS::Cluster.ClusterSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersetting.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `eu-south-1`

  - Since v15.3.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `ap-southeast-2`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v15.3.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `ap-southeast-2`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v15.3.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `ap-southeast-2`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v15.3.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `ap-southeast-2`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v15.3.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `ap-southeast-2`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v15.3.0: [AWS::SSM::Association.ParameterValues](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-parametervalues.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `eu-south-1`

- New PropertyType(s) Missing
  - [AWS::SageMaker::EndpointConfig.CaptureContentTypeHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html)
    - `us-west-2`

  - [AWS::SageMaker::EndpointConfig.CaptureOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-captureoption.html)
    - `us-west-2`

  - [AWS::SageMaker::EndpointConfig.DataCaptureConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html)
    - `us-west-2`

