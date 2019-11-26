# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v9-changelog.json`](changelogs/v8-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## [9.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v9.0.0) (2019-11-25)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v9-changelog.json)
  - Change source is a diff between [v9.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v9.0.0) and [v8.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v8.1.0)

### Totals

- TotalPropertyTypes: 1152 **(+23)**
- TotalPropertyTypesSupportedGlobally: 478 **(+9)**
- TotalResourceTypes: 476 **(+9)**
- TotalResourceTypesSupportedGlobally: 191 **(+2)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::AppSync::ApiCache](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-2`
  - `cn-north-1`

- [AWS::ECS::PrimaryTaskSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-primarytaskset.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::ECS::TaskSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::EKS::Nodegroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html)
  - `us-east-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`
  - `ap-east-1`
  - `me-south-1`

- [AWS::GameLift::GameSessionQueue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`
  - `cn-north-1`

- [AWS::GameLift::MatchmakingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`
  - `cn-north-1`

- [AWS::GameLift::MatchmakingRuleSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`
  - `cn-north-1`

- [AWS::GameLift::Script](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`
  - `cn-north-1`

- [AWS::Lambda::EventInvokeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html)
  - Available in **ALL** regions.

- [AWS::AppSync::Resolver.CachingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::AppSync::Resolver.LambdaConflictHandlerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-lambdaconflicthandlerconfig.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::DLM::LifecyclePolicy.FastRestoreRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::ECS::Cluster.ClusterSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersetting.html)
  - Available in **ALL** regions.

- [AWS::ECS::Service.DeploymentController](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-service-deploymentcontroller.html)
  - Available in **ALL** regions.

- [AWS::ECS::TaskDefinition.FirelensConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-firelensconfiguration.html)
  - Available in **ALL** regions.

- [AWS::ECS::TaskSet.AwsVpcConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-awsvpcconfiguration.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::ECS::TaskSet.LoadBalancer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-loadbalancer.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::ECS::TaskSet.NetworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-networkconfiguration.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::ECS::TaskSet.Scale](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-scale.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::ECS::TaskSet.ServiceRegistry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskset-serviceregistry.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::EKS::Nodegroup.RemoteAccess](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-remoteaccess.html)
  - `us-east-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`
  - `ap-east-1`
  - `me-south-1`

- [AWS::EKS::Nodegroup.ScalingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html)
  - `us-east-1`
  - `eu-north-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`
  - `ap-east-1`
  - `me-south-1`

- [AWS::Elasticsearch::Domain.CognitoOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html)
  - Available in **ALL** regions.

- [AWS::GameLift::GameSessionQueue.Destination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-destination.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`
  - `cn-north-1`

- [AWS::GameLift::GameSessionQueue.PlayerLatencyPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-playerlatencypolicy.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`
  - `cn-north-1`

- [AWS::GameLift::MatchmakingConfiguration.GameProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-matchmakingconfiguration-gameproperty.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`
  - `cn-north-1`

- [AWS::GameLift::Script.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html)
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`
  - `cn-north-1`

- [AWS::Lambda::Alias.ProvisionedConcurrencyConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-provisionedconcurrencyconfiguration.html)
  - Available in **ALL** regions.

- [AWS::Lambda::EventInvokeConfig.DestinationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig.html)
  - Available in **ALL** regions.

- [AWS::Lambda::EventInvokeConfig.OnFailure](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onfailure.html)
  - Available in **ALL** regions.

- [AWS::Lambda::EventInvokeConfig.OnSuccess](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-destinationconfig-onsuccess.html)
  - Available in **ALL** regions.

- [AWS::Lambda::Version.ProvisionedConcurrencyConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-version-provisionedconcurrencyconfiguration.html)
  - Available in **ALL** regions.

- [AWS::SageMaker::Endpoint.VariantProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-variantproperty.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `us-east-2`
  - `us-west-2`

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::AppSync::Resolver.LambdaConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-lambdaconfig.html)
  - `us-east-2`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::EC2::TrafficMirrorFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilter.html)
  - `ap-southeast-2`
  - `ap-east-1`

- [AWS::EC2::TrafficMirrorFilterRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilterrule.html)
  - `ap-southeast-2`
  - `ap-east-1`

- [AWS::EC2::TrafficMirrorSession](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorsession.html)
  - `ap-southeast-2`
  - `ap-east-1`

- [AWS::EC2::TrafficMirrorTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrortarget.html)
  - `ap-southeast-2`
  - `ap-east-1`

- [AWS::EC2::VPCEndpointService](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservice.html)
  - Now available to **ALL** regions.

- [AWS::EKS::Cluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html)
  - `us-west-1`
  - `me-south-1`
  - `sa-east-1`
  - `ca-central-1`

- [AWS::QLDB::Ledger](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html)
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-central-1`
  - `ap-southeast-1`

- [AWS::AppSync::DataSource.DeltaSyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html)
  - `ap-northeast-2`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-1`
  - `ap-southeast-2`
  - `ap-southeast-1`

- [AWS::AppSync::Resolver.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html)
  - `ap-northeast-2`
  - `eu-central-1`
  - `ap-northeast-1`
  - `us-east-1`
  - `ap-south-1`
  - `eu-west-1`
  - `ap-southeast-2`
  - `ap-southeast-1`

- [AWS::EC2::TrafficMirrorFilterRule.TrafficMirrorPortRange](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-trafficmirrorfilterrule-trafficmirrorportrange.html)
  - `ap-southeast-2`
  - `ap-east-1`

- [AWS::EKS::Cluster.ResourcesVpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-resourcesvpcconfig.html)
  - `us-west-1`
  - `me-south-1`
  - `sa-east-1`
  - `ca-central-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v8.1.0: [AWS::ApiGatewayV2::Api.BodyS3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html)
    - `us-west-1`

  - Since v8.1.0: [AWS::ApiGatewayV2::Api.Cors](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html)
    - `us-west-1`

  - Since v8.1.0: [AWS::ApiGatewayV2::Authorizer.JWTConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html)
    - `us-west-1`

- PropertyType(s) No Longer Missing
  - [AWS::AppSync::DataSource.DeltaSyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html)
    - Was missing since v8.1.0

  - [AWS::AppSync::Resolver.LambdaConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-lambdaconfig.html)
    - Was missing since v8.1.0

  - [AWS::AppSync::Resolver.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html)
    - Was missing since v8.1.0

