# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v89-changelog.json`](changelogs/v89-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [89.0.0](#8900-2022-09-18)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [89.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v89.0.0) (2022-09-18)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v89-changelog.json)
  - Change source is a diff between [v89.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v89.0.0) and [v88.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v88.0.0)

### Totals

- TotalPropertyTypes: 3298 **(+1)**
- TotalPropertyTypesSupportedGlobally: 1138 **(+-4)**
- TotalResourceTypes: 957 **(+0)**
- TotalResourceTypesSupportedGlobally: 345 **(+1)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::Evidently::Project.AppConfigResourceObject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-appconfigresourceobject.html)
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::AppSync::ApiKey](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html)
  - `af-south-1`

- [AWS::AppSync::DataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html)
  - `af-south-1`

- [AWS::AppSync::FunctionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html)
  - `af-south-1`

- [AWS::AppSync::GraphQLApi](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html)
  - `af-south-1`

- [AWS::AppSync::GraphQLSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html)
  - `af-south-1`

- [AWS::AppSync::Resolver](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html)
  - `af-south-1`

- [AWS::DevOpsGuru::NotificationChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-notificationchannel.html)
  - `ap-northeast-2`
  - `ap-south-1`
  - `eu-west-2`
  - `sa-east-1`
  - `eu-west-3`
  - `us-west-1`
  - `ca-central-1`

- [AWS::DevOpsGuru::ResourceCollection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-resourcecollection.html)
  - `ap-northeast-2`
  - `ap-south-1`
  - `eu-west-2`
  - `sa-east-1`
  - `eu-west-3`
  - `us-west-1`
  - `ca-central-1`

- [AWS::IAM::SAMLProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-samlprovider.html)
  - Now available to **ALL** regions.

- [AWS::AppSync::DataSource.AuthorizationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html)
  - `af-south-1`

- [AWS::AppSync::DataSource.AwsIamConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html)
  - `af-south-1`

- [AWS::AppSync::DataSource.DeltaSyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html)
  - `af-south-1`

- [AWS::AppSync::DataSource.DynamoDBConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html)
  - `af-south-1`

- [AWS::AppSync::DataSource.ElasticsearchConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html)
  - `af-south-1`

- [AWS::AppSync::DataSource.HttpConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html)
  - `af-south-1`

- [AWS::AppSync::DataSource.LambdaConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-lambdaconfig.html)
  - `af-south-1`

- [AWS::AppSync::DataSource.OpenSearchServiceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-opensearchserviceconfig.html)
  - `af-south-1`

- [AWS::AppSync::DataSource.RdsHttpEndpointConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html)
  - `af-south-1`

- [AWS::AppSync::DataSource.RelationalDatabaseConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html)
  - `af-south-1`

- [AWS::AppSync::FunctionConfiguration.LambdaConflictHandlerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html)
  - `af-south-1`

- [AWS::AppSync::FunctionConfiguration.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html)
  - `af-south-1`

- [AWS::AppSync::GraphQLApi.AdditionalAuthenticationProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html)
  - `af-south-1`

- [AWS::AppSync::GraphQLApi.CognitoUserPoolConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html)
  - `af-south-1`

- [AWS::AppSync::GraphQLApi.LambdaAuthorizerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html)
  - `af-south-1`

- [AWS::AppSync::GraphQLApi.LogConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html)
  - `af-south-1`

- [AWS::AppSync::GraphQLApi.OpenIDConnectConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html)
  - `af-south-1`

- [AWS::AppSync::GraphQLApi.UserPoolConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html)
  - `af-south-1`

- [AWS::AppSync::Resolver.CachingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html)
  - `af-south-1`

- [AWS::AppSync::Resolver.LambdaConflictHandlerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-lambdaconflicthandlerconfig.html)
  - `af-south-1`

- [AWS::AppSync::Resolver.PipelineConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-pipelineconfig.html)
  - `af-south-1`

- [AWS::AppSync::Resolver.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html)
  - `af-south-1`

- [AWS::DevOpsGuru::NotificationChannel.NotificationChannelConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationchannelconfig.html)
  - `ap-northeast-2`
  - `ap-south-1`
  - `eu-west-2`
  - `sa-east-1`
  - `eu-west-3`
  - `us-west-1`
  - `ca-central-1`

- [AWS::DevOpsGuru::NotificationChannel.SnsChannelConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-snschannelconfig.html)
  - `ap-northeast-2`
  - `ap-south-1`
  - `eu-west-2`
  - `sa-east-1`
  - `eu-west-3`
  - `us-west-1`
  - `ca-central-1`

- [AWS::DevOpsGuru::ResourceCollection.CloudFormationCollectionFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-cloudformationcollectionfilter.html)
  - `ap-northeast-2`
  - `ap-south-1`
  - `eu-west-2`
  - `sa-east-1`
  - `eu-west-3`
  - `us-west-1`
  - `ca-central-1`

- [AWS::DevOpsGuru::ResourceCollection.ResourceCollectionFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-resourcecollectionfilter.html)
  - `ap-northeast-2`
  - `ap-south-1`
  - `eu-west-2`
  - `sa-east-1`
  - `eu-west-3`
  - `us-west-1`
  - `ca-central-1`

- [AWS::DevOpsGuru::ResourceCollection.TagCollection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-tagcollection.html)
  - `ap-northeast-2`
  - `ap-south-1`
  - `eu-west-2`
  - `sa-east-1`
  - `eu-west-3`
  - `us-west-1`
  - `ca-central-1`

- [AWS::EKS::Cluster.OutpostConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-outpostconfig.html)
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-2`
  - `ap-northeast-3`
  - `ap-southeast-2`
  - `ap-east-1`
  - `us-east-2`
  - `eu-west-3`
  - `us-west-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `af-south-1`
  - `us-gov-west-1`
  - `us-gov-east-1`
  - `me-south-1`
  - `eu-west-1`
  - `eu-north-1`
  - `cn-northwest-1`
  - `us-east-1`
  - `ap-northeast-1`
  - `eu-south-1`

- [AWS::Logs::MetricFilter.Dimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-dimension.html)
  - `ap-northeast-1`
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::DynamoDB::Table.Csv](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-csv.html)
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-2`
  - `ap-northeast-3`
  - `ap-southeast-2`
  - `ap-east-1`
  - `us-east-2`
  - `eu-central-1`
  - `eu-west-3`
  - `cn-north-1`
  - `us-west-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `af-south-1`
  - `us-gov-west-1`
  - `us-gov-east-1`
  - `me-south-1`
  - `eu-west-1`
  - `eu-north-1`
  - `cn-northwest-1`
  - `us-east-1`
  - `ap-northeast-1`
  - `eu-south-1`

- [AWS::DynamoDB::Table.ImportSourceSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-importsourcespecification.html)
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-2`
  - `ap-northeast-3`
  - `ap-southeast-2`
  - `ap-east-1`
  - `us-east-2`
  - `eu-central-1`
  - `eu-west-3`
  - `cn-north-1`
  - `us-west-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `af-south-1`
  - `us-gov-west-1`
  - `us-gov-east-1`
  - `me-south-1`
  - `eu-west-1`
  - `eu-north-1`
  - `cn-northwest-1`
  - `us-east-1`
  - `ap-northeast-1`
  - `eu-south-1`

- [AWS::DynamoDB::Table.InputFormatOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-inputformatoptions.html)
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-2`
  - `ap-northeast-3`
  - `ap-southeast-2`
  - `ap-east-1`
  - `us-east-2`
  - `eu-central-1`
  - `eu-west-3`
  - `cn-north-1`
  - `us-west-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `af-south-1`
  - `us-gov-west-1`
  - `us-gov-east-1`
  - `me-south-1`
  - `eu-west-1`
  - `eu-north-1`
  - `cn-northwest-1`
  - `us-east-1`
  - `ap-northeast-1`
  - `eu-south-1`

- [AWS::DynamoDB::Table.S3BucketSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-s3bucketsource.html)
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-2`
  - `ap-northeast-3`
  - `ap-southeast-2`
  - `ap-east-1`
  - `us-east-2`
  - `eu-central-1`
  - `eu-west-3`
  - `cn-north-1`
  - `us-west-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `af-south-1`
  - `us-gov-west-1`
  - `us-gov-east-1`
  - `me-south-1`
  - `eu-west-1`
  - `eu-north-1`
  - `cn-northwest-1`
  - `us-east-1`
  - `ap-northeast-1`
  - `eu-south-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v88.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v88.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v88.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v88.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v88.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v88.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

  - Since v88.0.0: [AWS::M2::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-application.html)
    - `ca-central-1`
    - `eu-central-1`
    - `eu-west-1`
    - `sa-east-1`

- PropertyType Still Missing
  - Since v88.0.0: [AWS::Config::OrganizationConfigRule.OrganizationCustomPolicyRuleMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html)
    - `me-south-1`

  - Since v88.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v88.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v88.0.0: [AWS::DynamoDB::Table.Csv](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-csv.html)
    - `us-west-2`

  - Since v88.0.0: [AWS::DynamoDB::Table.ImportSourceSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-importsourcespecification.html)
    - `us-west-2`

  - Since v88.0.0: [AWS::DynamoDB::Table.InputFormatOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-inputformatoptions.html)
    - `us-west-2`

  - Since v88.0.0: [AWS::DynamoDB::Table.S3BucketSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-s3bucketsource.html)
    - `us-west-2`

  - Since v88.0.0: [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v88.0.0: [AWS::M2::Application.Definition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-m2-application-definition.html)
    - `ca-central-1`
    - `eu-central-1`
    - `eu-west-1`
    - `sa-east-1`

  - Since v88.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v88.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

