# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v26-changelog.json`](changelogs/v26-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [26.0.0](#2600-2021-01-29)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [26.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v26.0.0) (2021-01-29)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v26-changelog.json)
  - Change source is a diff between [v26.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v26.0.0) and [v25.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v25.0.0)

### Totals

- TotalPropertyTypes: 2165 **(+4)**
- TotalPropertyTypesSupportedGlobally: 523 **(+0)**
- TotalResourceTypes: 672 **(+1)**
- TotalResourceTypesSupportedGlobally: 192 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::LookoutVision::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutvision-project.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::AppFlow::Flow.IdFieldNamesList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-idfieldnameslist.html)
  - `ap-southeast-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::DataBrew::Job.CsvOutputOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-csvoutputoptions.html)
  - `eu-central-1`

- [AWS::DataBrew::Job.OutputFormatOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputformatoptions.html)
  - `eu-central-1`

- [AWS::SageMaker::Model.InferenceExecutionConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-inferenceexecutionconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `us-east-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::DataBrew::Dataset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html)
  - `eu-west-3`
  - `us-west-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-2`
  - `ap-southeast-1`

- [AWS::DataBrew::Job](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html)
  - `eu-west-3`
  - `us-west-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-2`
  - `ap-southeast-1`

- [AWS::DataBrew::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html)
  - `eu-west-3`
  - `us-west-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-2`
  - `ap-southeast-1`

- [AWS::DataBrew::Recipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html)
  - `eu-west-3`
  - `us-west-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-2`
  - `ap-southeast-1`

- [AWS::DataBrew::Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html)
  - `eu-west-3`
  - `us-west-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-2`
  - `ap-southeast-1`

- [AWS::EKS::Cluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html)
  - `ap-northeast-3`

- [AWS::ApiGatewayV2::Integration.ResponseParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameter.html)
  - `sa-east-1`

- [AWS::ApiGatewayV2::Integration.ResponseParameterList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameterlist.html)
  - `sa-east-1`

- [AWS::DataBrew::Job.Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html)
  - `eu-west-3`
  - `us-west-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-2`
  - `ap-southeast-1`

- [AWS::DataBrew::Job.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3location.html)
  - `eu-west-3`
  - `us-west-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-2`
  - `ap-southeast-1`

- [AWS::DataBrew::Recipe.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-action.html)
  - `eu-west-3`
  - `us-west-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-2`
  - `ap-southeast-1`

- [AWS::DataBrew::Recipe.ConditionExpression](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-conditionexpression.html)
  - `eu-west-3`
  - `us-west-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-2`
  - `ap-southeast-1`

- [AWS::DataBrew::Recipe.DataCatalogInputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-datacataloginputdefinition.html)
  - `eu-west-3`
  - `us-west-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-2`
  - `ap-southeast-1`

- [AWS::DataBrew::Recipe.RecipeParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html)
  - `eu-west-3`
  - `us-west-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-2`
  - `ap-southeast-1`

- [AWS::DataBrew::Recipe.RecipeStep](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipestep.html)
  - `eu-west-3`
  - `us-west-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-2`
  - `ap-southeast-1`

- [AWS::DataBrew::Recipe.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-s3location.html)
  - `eu-west-3`
  - `us-west-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-2`
  - `ap-southeast-1`

- [AWS::DataBrew::Recipe.SecondaryInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-secondaryinput.html)
  - `eu-west-3`
  - `us-west-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-2`
  - `ap-southeast-1`

- [AWS::ECS::Cluster.ClusterConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clusterconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `me-south-1`
  - `cn-northwest-1`
  - `ap-northeast-2`
  - `eu-west-2`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-gov-east-1`
  - `us-west-1`
  - `eu-west-1`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-northeast-1`
  - `ap-east-1`
  - `sa-east-1`

- [AWS::ECS::Cluster.ExecuteCommandConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `me-south-1`
  - `cn-northwest-1`
  - `ap-northeast-2`
  - `eu-west-2`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-gov-east-1`
  - `us-west-1`
  - `eu-west-1`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-northeast-1`
  - `ap-east-1`
  - `sa-east-1`

- [AWS::ECS::Cluster.ExecuteCommandLogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-executecommandlogconfiguration.html)
  - `us-gov-west-1`
  - `eu-north-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-south-1`
  - `me-south-1`
  - `cn-northwest-1`
  - `ap-northeast-2`
  - `eu-west-2`
  - `ap-southeast-1`
  - `eu-west-3`
  - `us-gov-east-1`
  - `us-west-1`
  - `eu-west-1`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-northeast-1`
  - `ap-east-1`
  - `sa-east-1`

- [AWS::EKS::Cluster.EncryptionConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-encryptionconfig.html)
  - `ap-northeast-3`

- [AWS::EKS::Cluster.KubernetesNetworkConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-kubernetesnetworkconfig.html)
  - `ap-northeast-3`

- [AWS::EKS::Cluster.Provider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-provider.html)
  - `ap-northeast-3`

- [AWS::EKS::Cluster.ResourcesVpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-resourcesvpcconfig.html)
  - `ap-northeast-3`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v25.0.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v25.0.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v25.0.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

- PropertyType Still Missing
  - Since v25.0.0: [AWS::ECS::Cluster.ClusterSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersetting.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `eu-south-1`

  - Since v25.0.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v25.0.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v25.0.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v25.0.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v25.0.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v25.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v25.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::DataBrew::Job.CsvOutputOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-csvoutputoptions.html)
    - `eu-central-1`

  - [AWS::DataBrew::Job.OutputFormatOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputformatoptions.html)
    - `eu-central-1`

