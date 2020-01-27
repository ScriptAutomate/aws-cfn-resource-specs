# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v10-changelog.json`](changelogs/v10-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [10.4.0](#1040-2020-01-27)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)
- [10.3.0](#1030-2020-01-20)
  - [Totals](#totals-1)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-1)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-1)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-1)
- [10.2.0](#1020-2019-12-23)
  - [Totals](#totals-2)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-2)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-2)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-2)
- [10.1.0](#1010-2019-12-13)
  - [Totals](#totals-3)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-3)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-3)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-3)
- [10.0.0](#1000-2019-12-05)
  - [Totals](#totals-4)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-4)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-4)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-4)

## [10.4.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.4.0) (2020-01-27)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v10-changelog.json)
  - Change source is a diff between [v10.4.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.4.0) and [v10.3.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.3.0)

### Totals

- TotalPropertyTypes: 1280 **(+6)**
- TotalPropertyTypesSupportedGlobally: 498 **(+17)**
- TotalResourceTypes: 491 **(+3)**
- TotalResourceTypesSupportedGlobally: 193 **(+2)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::ACMPCA::Certificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::ACMPCA::CertificateAuthority](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::ACMPCA::CertificateAuthorityActivation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `sa-east-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFront::Distribution.OriginGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html)
  - `ap-south-1`

- [AWS::CloudFront::Distribution.OriginGroupFailoverCriteria](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupfailovercriteria.html)
  - `ap-south-1`

- [AWS::CloudFront::Distribution.OriginGroupMember](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmember.html)
  - `ap-south-1`

- [AWS::CloudFront::Distribution.OriginGroupMembers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmembers.html)
  - `ap-south-1`

- [AWS::CloudFront::Distribution.OriginGroups](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroups.html)
  - `ap-south-1`

- [AWS::CloudFront::Distribution.StatusCodes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-statuscodes.html)
  - `ap-south-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::AmazonMQ::Broker](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`
  - `eu-west-2`

- [AWS::AmazonMQ::Configuration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`
  - `eu-west-2`

- [AWS::AmazonMQ::ConfigurationAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configurationassociation.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`
  - `eu-west-2`

- [AWS::Amplify::App](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Amplify::Branch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Amplify::Domain](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::ApiGateway::VpcLink](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-vpclink.html)
  - `eu-central-1`
  - `ap-northeast-3`
  - `eu-west-3`

- [AWS::ApiGatewayV2::Api](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html)
  - `ap-northeast-3`

- [AWS::ApiGatewayV2::ApiMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html)
  - `ap-northeast-3`

- [AWS::ApiGatewayV2::Authorizer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html)
  - `ap-northeast-3`

- [AWS::ApiGatewayV2::Deployment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html)
  - `ap-northeast-3`

- [AWS::ApiGatewayV2::DomainName](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html)
  - `ap-northeast-3`

- [AWS::ApiGatewayV2::Integration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html)
  - `ap-northeast-3`

- [AWS::ApiGatewayV2::IntegrationResponse](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html)
  - `ap-northeast-3`

- [AWS::ApiGatewayV2::Model](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html)
  - `ap-northeast-3`

- [AWS::ApiGatewayV2::Route](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html)
  - `ap-northeast-3`

- [AWS::ApiGatewayV2::RouteResponse](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html)
  - `ap-northeast-3`

- [AWS::ApiGatewayV2::Stage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Mesh](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Route](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualNode](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualRouter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualService](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppStream::DirectoryConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-directoryconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppStream::Fleet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppStream::ImageBuilder](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppStream::Stack](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppStream::StackFleetAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackfleetassociation.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppStream::StackUserAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackuserassociation.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppStream::User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::ApiCache](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::ApiKey](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::AppSync::DataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::FunctionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::GraphQLApi](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::GraphQLSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::AppSync::Resolver](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Athena::NamedQuery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AutoScalingPlans::ScalingPlan](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Backup::BackupPlan](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Backup::BackupSelection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Backup::BackupVault](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Batch::ComputeEnvironment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::Batch::JobQueue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::Budgets::Budget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cloud9::EnvironmentEC2](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::CloudFront::CloudFrontOriginAccessIdentity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::CloudFront::Distribution](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html)
  - `ap-northeast-3`

- [AWS::CloudFront::StreamingDistribution](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::CloudWatch::InsightRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html)
  - `ap-northeast-3`

- [AWS::CodeBuild::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::ReportGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html)
  - `ap-northeast-3`

- [AWS::CodeBuild::SourceCredential](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html)
  - `ap-northeast-3`

- [AWS::CodeCommit::Repository](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::CodePipeline::Webhook](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-webhook.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::CodeStar::GitHubRepository](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestar-githubrepository.html)
  - `ap-northeast-3`

- [AWS::CodeStarNotifications::NotificationRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html)
  - `ap-northeast-3`

- [AWS::Cognito::IdentityPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::IdentityPoolRoleAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolroleattachment.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolClient](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolDomain](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooldomain.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolIdentityProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolidentityprovider.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolResourceServer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolresourceserver.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolRiskConfigurationAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolriskconfigurationattachment.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolUICustomizationAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluicustomizationattachment.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolUser](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolUserToGroupAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolusertogroupattachment.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Config::AggregationAuthorization](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Config::ConfigurationAggregator](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Config::OrganizationConfigRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html)
  - `ap-northeast-3`

- [AWS::Config::RemediationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html)
  - `ap-northeast-3`

- [AWS::DAX::Cluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::DAX::ParameterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-parametergroup.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::DAX::SubnetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-subnetgroup.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::DLM::LifecyclePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::DMS::Certificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html)
  - `ap-northeast-3`
  - `eu-west-3`

- [AWS::DMS::Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html)
  - `ap-northeast-3`
  - `eu-west-3`

- [AWS::DMS::EventSubscription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html)
  - `ap-northeast-3`
  - `eu-west-3`

- [AWS::DMS::ReplicationInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html)
  - `ap-northeast-3`
  - `eu-west-3`

- [AWS::DMS::ReplicationSubnetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html)
  - `ap-northeast-3`
  - `eu-west-3`

- [AWS::DMS::ReplicationTask](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html)
  - `ap-northeast-3`
  - `eu-west-3`

- [AWS::DocDB::DBCluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::DocDB::DBClusterParameterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::DocDB::DBInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::DocDB::DBSubnetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::EC2::CapacityReservation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::EC2::ClientVpnAuthorizationRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::EC2::ClientVpnEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::EC2::ClientVpnRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::EC2::ClientVpnTargetNetworkAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpntargetnetworkassociation.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::EC2::TrafficMirrorFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilter.html)
  - `ap-northeast-3`

- [AWS::EC2::TrafficMirrorFilterRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilterrule.html)
  - `ap-northeast-3`

- [AWS::EC2::TrafficMirrorSession](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorsession.html)
  - `ap-northeast-3`

- [AWS::EC2::TrafficMirrorTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrortarget.html)
  - `ap-northeast-3`

- [AWS::EC2::TransitGateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::EC2::TransitGatewayAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::EC2::TransitGatewayRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::EC2::TransitGatewayRouteTable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetable.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::EC2::TransitGatewayRouteTableAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetableassociation.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::EC2::TransitGatewayRouteTablePropagation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetablepropagation.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::EC2::VPCEndpointConnectionNotification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.html)
  - `ap-northeast-1`
  - `us-west-2`
  - `us-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `eu-west-1`
  - `eu-central-1`
  - `us-east-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`

- [AWS::EKS::Cluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html)
  - `ap-northeast-3`

- [AWS::EKS::Nodegroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html)
  - `ap-northeast-3`

- [AWS::EventSchemas::Discoverer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::EventSchemas::Registry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::EventSchemas::Schema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::Events::EventBus](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbus.html)
  - `ap-northeast-3`

- [AWS::Events::EventBusPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html)
  - `ap-northeast-3`

- [AWS::FSx::FileSystem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`

- [AWS::GameLift::GameSessionQueue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::GameLift::MatchmakingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::GameLift::MatchmakingRuleSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::GameLift::Script](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Classifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-classifier.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::Connection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-connection.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Crawler](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::DataCatalogEncryptionSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-datacatalogencryptionsettings.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::Database](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-database.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::DevEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::Job](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html)
  - `ap-northeast-3`
  - `sa-east-1`

- [AWS::Glue::MLTransform](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Partition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-partition.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::SecurityConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-securityconfiguration.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::Table](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Trigger](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html)
  - `ap-northeast-3`
  - `sa-east-1`

- [AWS::Glue::Workflow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-workflow.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Greengrass::ConnectorDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ConnectorDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::CoreDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::CoreDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::DeviceDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::DeviceDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::FunctionDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::FunctionDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::Group](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::GroupVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::LoggerDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::LoggerDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ResourceDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ResourceDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::SubscriptionDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::SubscriptionDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::GuardDuty::Detector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::GuardDuty::Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::GuardDuty::IPSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::GuardDuty::Master](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::GuardDuty::Member](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::GuardDuty::ThreatIntelSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IAM::ServiceLinkedRole](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::Inspector::AssessmentTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttarget.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Inspector::AssessmentTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::Inspector::ResourceGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-resourcegroup.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::IoT1Click::Device](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-device.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoT1Click::Placement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoT1Click::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Channel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Datastore](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Pipeline](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::DetectorModel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTThingsGraph::FlowTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::KinesisAnalytics::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::ApplicationOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::ApplicationReferenceDataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::ApplicationOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::LakeFormation::DataLakeSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::LakeFormation::Permissions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::LakeFormation::Resource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::Lambda::LayerVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::Lambda::LayerVersionPermission](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::MSK::Cluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html)
  - `ap-northeast-3`
  - `me-south-1`

- [AWS::ManagedBlockchain::Member](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-2`
  - `us-west-1`
  - `eu-west-2`
  - `ap-northeast-2`

- [AWS::ManagedBlockchain::Node](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-node.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-2`
  - `us-west-1`
  - `eu-west-2`
  - `ap-northeast-2`

- [AWS::MediaConvert::JobTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html)
  - `ap-northeast-3`

- [AWS::MediaConvert::Preset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html)
  - `ap-northeast-3`

- [AWS::MediaConvert::Queue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html)
  - `ap-northeast-3`

- [AWS::MediaLive::Channel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::InputSecurityGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaStore::Container](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`

- [AWS::Neptune::DBCluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Neptune::DBClusterParameterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Neptune::DBInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Neptune::DBParameterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Neptune::DBSubnetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbsubnetgroup.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::OpsWorksCM::Server](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::ADMChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::APNSChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::APNSSandboxChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::APNSVoipChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::APNSVoipSandboxChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::App](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::ApplicationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::BaiduChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Campaign](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::EmailChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::EmailTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::EventStream](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::GCMChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::PushTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::SMSChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Segment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::SmsTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::VoiceChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::PinpointEmail::ConfigurationSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::PinpointEmail::ConfigurationSetEventDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::PinpointEmail::DedicatedIpPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::PinpointEmail::Identity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::QLDB::Ledger](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::RAM::ResourceShare](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html)
  - `ap-northeast-3`
  - `sa-east-1`

- [AWS::RoboMaker::Fleet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-fleet.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::RoboMaker::Robot](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robot.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::RoboMaker::RobotApplication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::RoboMaker::RobotApplicationVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplicationversion.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::RoboMaker::SimulationApplication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::RoboMaker::SimulationApplicationVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplicationversion.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Route53Resolver::ResolverEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`

- [AWS::Route53Resolver::ResolverRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`

- [AWS::Route53Resolver::ResolverRuleAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `eu-central-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`

- [AWS::SES::ConfigurationSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `ap-southeast-2`
  - `us-west-1`
  - `eu-west-2`
  - `sa-east-1`
  - `eu-central-1`
  - `us-east-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::SES::ConfigurationSetEventDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SES::ReceiptFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SES::ReceiptRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SES::ReceiptRuleSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SES::Template](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SSM::MaintenanceWindow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SSM::MaintenanceWindowTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html)
  - Now available to **ALL** regions.

- [AWS::SSM::MaintenanceWindowTask](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SSM::Parameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SSM::PatchBaseline](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::SSM::ResourceDataSync](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SageMaker::CodeRepository](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::SageMaker::Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SageMaker::EndpointConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SageMaker::Model](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::SageMaker::NotebookInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::SageMaker::NotebookInstanceLifecycleConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SageMaker::Workteam](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SecretsManager::ResourcePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-resourcepolicy.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SecretsManager::RotationSchedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-rotationschedule.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SecretsManager::Secret](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secret.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SecretsManager::SecretTargetAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secrettargetattachment.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SecurityHub::Hub](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html)
  - `ap-northeast-3`

- [AWS::ServiceCatalog::AcceptedPortfolioShare](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::ServiceCatalog::CloudFormationProduct](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html)
  - `ap-northeast-3`

- [AWS::ServiceCatalog::CloudFormationProvisionedProduct](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html)
  - `ap-northeast-3`

- [AWS::ServiceCatalog::LaunchNotificationConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html)
  - `ap-northeast-3`

- [AWS::ServiceCatalog::LaunchRoleConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html)
  - `ap-northeast-3`

- [AWS::ServiceCatalog::LaunchTemplateConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html)
  - `ap-northeast-3`

- [AWS::ServiceCatalog::Portfolio](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html)
  - `ap-northeast-3`

- [AWS::ServiceCatalog::PortfolioPrincipalAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html)
  - `ap-northeast-3`

- [AWS::ServiceCatalog::PortfolioProductAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::ServiceCatalog::PortfolioShare](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::ServiceCatalog::ResourceUpdateConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`

- [AWS::ServiceCatalog::StackSetConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::ServiceCatalog::TagOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html)
  - `ap-northeast-3`

- [AWS::ServiceCatalog::TagOptionAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html)
  - `ap-northeast-3`

- [AWS::ServiceDiscovery::HttpNamespace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html)
  - `eu-west-3`
  - `sa-east-1`
  - `ap-northeast-1`
  - `ap-northeast-3`

- [AWS::ServiceDiscovery::Instance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html)
  - `sa-east-1`
  - `ap-northeast-3`

- [AWS::ServiceDiscovery::PrivateDnsNamespace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html)
  - `sa-east-1`
  - `ap-northeast-3`

- [AWS::ServiceDiscovery::PublicDnsNamespace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html)
  - `sa-east-1`
  - `ap-northeast-3`

- [AWS::ServiceDiscovery::Service](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html)
  - `sa-east-1`
  - `ap-northeast-3`

- [AWS::StepFunctions::Activity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::StepFunctions::StateMachine](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Transfer::Server](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html)
  - `ap-northeast-3`

- [AWS::Transfer::User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html)
  - `ap-northeast-3`

- [AWS::WAFRegional::ByteMatchSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::GeoMatchSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-geomatchset.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::IPSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::RateBasedRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::RegexPatternSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-regexpatternset.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::SizeConstraintSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::SqlInjectionMatchSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::WebACL](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::WebACLAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::XssMatchSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [Alexa::ASK::Skill](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `eu-north-1`

- [AWS::AmazonMQ::Broker.ConfigurationId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-configurationid.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`
  - `eu-west-2`

- [AWS::AmazonMQ::Broker.EncryptionOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-encryptionoptions.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`
  - `eu-west-2`

- [AWS::AmazonMQ::Broker.LogList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-loglist.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`
  - `eu-west-2`

- [AWS::AmazonMQ::Broker.MaintenanceWindow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`
  - `eu-west-2`

- [AWS::AmazonMQ::Broker.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-tagsentry.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`
  - `eu-west-2`

- [AWS::AmazonMQ::Broker.User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-user.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`
  - `eu-west-2`

- [AWS::AmazonMQ::Configuration.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configuration-tagsentry.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`
  - `eu-west-2`

- [AWS::AmazonMQ::ConfigurationAssociation.ConfigurationId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configurationassociation-configurationid.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`
  - `eu-west-2`

- [AWS::Amplify::App.AutoBranchCreationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-autobranchcreationconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Amplify::App.BasicAuthConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Amplify::App.CustomRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-customrule.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Amplify::App.EnvironmentVariable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-environmentvariable.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Amplify::Branch.BasicAuthConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-basicauthconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Amplify::Branch.EnvironmentVariable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-branch-environmentvariable.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Amplify::Domain.SubDomainSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-domain-subdomainsetting.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::ApiGatewayV2::DomainName.DomainNameConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html)
  - `ap-northeast-3`

- [AWS::ApiGatewayV2::Route.ParameterConstraints](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-route-parameterconstraints.html)
  - `ap-northeast-3`

- [AWS::ApiGatewayV2::RouteResponse.ParameterConstraints](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-routeresponse-parameterconstraints.html)
  - `ap-northeast-3`

- [AWS::ApiGatewayV2::Stage.AccessLogSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-accesslogsettings.html)
  - `ap-northeast-3`

- [AWS::ApiGatewayV2::Stage.RouteSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Mesh.EgressFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-egressfilter.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Mesh.MeshSpec](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshspec.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Route.Duration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-duration.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Route.GrpcRetryPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Route.GrpcRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Route.GrpcRouteAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcrouteaction.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Route.GrpcRouteMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Route.GrpcRouteMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadata.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Route.GrpcRouteMetadataMatchMethod](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Route.HeaderMatchMethod](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Route.HttpRetryPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Route.HttpRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Route.HttpRouteAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteaction.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Route.HttpRouteHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteheader.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Route.HttpRouteMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Route.MatchRange](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-matchrange.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Route.RouteSpec](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Route.TcpRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Route.TcpRouteAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcprouteaction.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::Route.WeightedTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-weightedtarget.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualNode.AccessLog](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-accesslog.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualNode.AwsCloudMapInstanceAttribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualNode.AwsCloudMapServiceDiscovery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualNode.Backend](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backend.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualNode.DnsServiceDiscovery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-dnsservicediscovery.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualNode.FileAccessLog](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-fileaccesslog.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualNode.HealthCheck](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualNode.Listener](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualNode.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-logging.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualNode.PortMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-portmapping.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualNode.ServiceDiscovery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-servicediscovery.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualNode.VirtualNodeSpec](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualNode.VirtualServiceBackend](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualservicebackend.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualRouter.PortMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-portmapping.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualRouter.VirtualRouterListener](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterlistener.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualRouter.VirtualRouterSpec](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterspec.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualService.VirtualNodeServiceProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualnodeserviceprovider.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualService.VirtualRouterServiceProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualrouterserviceprovider.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualService.VirtualServiceProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualserviceprovider.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppMesh::VirtualService.VirtualServiceSpec](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualservicespec.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppStream::DirectoryConfig.ServiceAccountCredentials](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-directoryconfig-serviceaccountcredentials.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppStream::Fleet.ComputeCapacity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-computecapacity.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppStream::Fleet.DomainJoinInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-domainjoininfo.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppStream::Fleet.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-fleet-vpcconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppStream::ImageBuilder.AccessEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-accessendpoint.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppStream::ImageBuilder.DomainJoinInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-domainjoininfo.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppStream::ImageBuilder.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-imagebuilder-vpcconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppStream::Stack.AccessEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-accessendpoint.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppStream::Stack.ApplicationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-applicationsettings.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppStream::Stack.StorageConnector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-storageconnector.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppStream::Stack.UserSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appstream-stack-usersetting.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-gov-west-1`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::DataSource.AuthorizationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::DataSource.AwsIamConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::DataSource.DeltaSyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::DataSource.DynamoDBConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::DataSource.ElasticsearchConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::DataSource.HttpConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::DataSource.LambdaConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-lambdaconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::DataSource.RdsHttpEndpointConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::DataSource.RelationalDatabaseConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::GraphQLApi.AdditionalAuthenticationProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::GraphQLApi.AdditionalAuthenticationProviders](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationproviders.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::GraphQLApi.CognitoUserPoolConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::GraphQLApi.LogConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::GraphQLApi.OpenIDConnectConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::GraphQLApi.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-tags.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::GraphQLApi.UserPoolConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::Resolver.CachingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::Resolver.LambdaConflictHandlerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-lambdaconflicthandlerconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::Resolver.PipelineConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-pipelineconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AppSync::Resolver.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AutoScalingPlans::ScalingPlan.ApplicationSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-applicationsource.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AutoScalingPlans::ScalingPlan.CustomizedLoadMetricSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AutoScalingPlans::ScalingPlan.CustomizedScalingMetricSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AutoScalingPlans::ScalingPlan.MetricDimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-metricdimension.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AutoScalingPlans::ScalingPlan.PredefinedLoadMetricSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedloadmetricspecification.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AutoScalingPlans::ScalingPlan.PredefinedScalingMetricSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedscalingmetricspecification.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AutoScalingPlans::ScalingPlan.ScalingInstruction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AutoScalingPlans::ScalingPlan.TagFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-tagfilter.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::AutoScalingPlans::ScalingPlan.TargetTrackingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Backup::BackupPlan.BackupPlanResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Backup::BackupPlan.BackupRuleResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Backup::BackupPlan.CopyActionResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html)
  - `ap-northeast-3`

- [AWS::Backup::BackupPlan.LifecycleResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-lifecycleresourcetype.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Backup::BackupSelection.BackupSelectionResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Backup::BackupSelection.ConditionResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Backup::BackupVault.NotificationObjectType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-notificationobjecttype.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Batch::ComputeEnvironment.ComputeResources](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-computeresources.html)
  - `ap-northeast-3`

- [AWS::Batch::ComputeEnvironment.LaunchTemplateSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-launchtemplatespecification.html)
  - `ap-northeast-3`

- [AWS::Batch::JobDefinition.ContainerProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::Batch::JobDefinition.Device](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-device.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::Batch::JobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-environment.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::Batch::JobDefinition.LinuxParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-linuxparameters.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::Batch::JobDefinition.MountPoints](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-mountpoints.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::Batch::JobDefinition.NodeProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-nodeproperties.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::Batch::JobDefinition.NodeRangeProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-noderangeproperty.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::Batch::JobDefinition.ResourceRequirement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-resourcerequirement.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::Batch::JobDefinition.RetryStrategy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-retrystrategy.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::Batch::JobDefinition.Timeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-timeout.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::Batch::JobDefinition.Ulimit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-ulimit.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::Batch::JobDefinition.Volumes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumes.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::Batch::JobDefinition.VolumesHost](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-volumeshost.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::Batch::JobQueue.ComputeEnvironmentOrder](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobqueue-computeenvironmentorder.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::Budgets::Budget.BudgetData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Budgets::Budget.CostTypes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Budgets::Budget.Notification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Budgets::Budget.NotificationWithSubscribers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Budgets::Budget.Spend](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Budgets::Budget.Subscriber](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Budgets::Budget.TimePeriod](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cloud9::EnvironmentEC2.Repository](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloud9-environmentec2-repository.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::CloudFront::CloudFrontOriginAccessIdentity.CloudFrontOriginAccessIdentityConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-cloudfrontoriginaccessidentity-cloudfrontoriginaccessidentityconfig.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::CloudFront::Distribution.CacheBehavior](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html)
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.Cookies](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cookies.html)
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.CustomErrorResponse](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html)
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.CustomOriginConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html)
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.DefaultCacheBehavior](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html)
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.DistributionConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html)
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.ForwardedValues](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html)
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.GeoRestriction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-georestriction.html)
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.LambdaFunctionAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-lambdafunctionassociation.html)
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-logging.html)
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.Origin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html)
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.OriginCustomHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origincustomheader.html)
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.Restrictions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-restrictions.html)
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.S3OriginConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-s3originconfig.html)
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.ViewerCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html)
  - `ap-northeast-3`

- [AWS::CloudFront::StreamingDistribution.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-logging.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::CloudFront::StreamingDistribution.S3Origin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-s3origin.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::CloudFront::StreamingDistribution.StreamingDistributionConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-streamingdistributionconfig.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::CloudFront::StreamingDistribution.TrustedSigners](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-streamingdistribution-trustedsigners.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::CodeBuild::Project.Artifacts](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.CloudWatchLogsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-cloudwatchlogsconfig.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.EnvironmentVariable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environmentvariable.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.FilterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-filtergroup.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.GitSubmodulesConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-gitsubmodulesconfig.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.LogsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-logsconfig.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.ProjectCache](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectcache.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.ProjectSourceVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectsourceversion.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.ProjectTriggers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projecttriggers.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.RegistryCredential](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-registrycredential.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.S3LogsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-s3logsconfig.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.Source](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.SourceAuth](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-sourceauth.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-vpcconfig.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::Project.WebhookFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-webhookfilter.html)
  - Now available to **ALL** regions.

- [AWS::CodeBuild::ReportGroup.ReportExportConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-reportexportconfig.html)
  - `ap-northeast-3`

- [AWS::CodeBuild::ReportGroup.S3ReportExportConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html)
  - `ap-northeast-3`

- [AWS::CodeCommit::Repository.Code](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-code.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::CodeCommit::Repository.RepositoryTrigger](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::CodeCommit::Repository.S3](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-s3.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::CodePipeline::Webhook.WebhookAuthConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-webhook-webhookauthconfiguration.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::CodePipeline::Webhook.WebhookFilterRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-webhook-webhookfilterrule.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::CodeStar::GitHubRepository.Code](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestar-githubrepository-code.html)
  - `ap-northeast-3`

- [AWS::CodeStar::GitHubRepository.S3](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestar-githubrepository-s3.html)
  - `ap-northeast-3`

- [AWS::CodeStarNotifications::NotificationRule.Target](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestarnotifications-notificationrule-target.html)
  - `ap-northeast-3`

- [AWS::Cognito::IdentityPool.CognitoIdentityProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitoidentityprovider.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::IdentityPool.CognitoStreams](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitostreams.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::IdentityPool.PushSync](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-pushsync.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::IdentityPoolRoleAttachment.MappingRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-mappingrule.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::IdentityPoolRoleAttachment.RoleMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rolemapping.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::IdentityPoolRoleAttachment.RulesConfigurationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rulesconfigurationtype.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPool.AccountRecoverySetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-accountrecoverysetting.html)
  - `ap-northeast-3`
  - `ap-southeast-2`
  - `us-west-2`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-1`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`
  - `us-east-1`

- [AWS::Cognito::UserPool.AdminCreateUserConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-admincreateuserconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPool.DeviceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-deviceconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPool.EmailConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-emailconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPool.InviteMessageTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-invitemessagetemplate.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPool.LambdaConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPool.NumberAttributeConstraints](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-numberattributeconstraints.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPool.PasswordPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-passwordpolicy.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPool.Policies](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-policies.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPool.RecoveryOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-recoveryoption.html)
  - `ap-northeast-3`
  - `ap-southeast-2`
  - `us-west-2`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-1`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`
  - `us-east-1`

- [AWS::Cognito::UserPool.SchemaAttribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPool.SmsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-smsconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPool.StringAttributeConstraints](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-stringattributeconstraints.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPool.UserPoolAddOns](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-userpooladdons.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPool.VerificationMessageTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-verificationmessagetemplate.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolClient.AnalyticsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolclient-analyticsconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolDomain.CustomDomainConfigType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpooldomain-customdomainconfigtype.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolResourceServer.ResourceServerScopeType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolresourceserver-resourceserverscopetype.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolRiskConfigurationAttachment.AccountTakeoverActionType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractiontype.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolRiskConfigurationAttachment.AccountTakeoverActionsType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoveractionstype.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolRiskConfigurationAttachment.AccountTakeoverRiskConfigurationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-accounttakeoverriskconfigurationtype.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolRiskConfigurationAttachment.CompromisedCredentialsActionsType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsactionstype.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolRiskConfigurationAttachment.CompromisedCredentialsRiskConfigurationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolRiskConfigurationAttachment.NotifyConfigurationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-notifyconfigurationtype.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolRiskConfigurationAttachment.NotifyEmailType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-notifyemailtype.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolRiskConfigurationAttachment.RiskExceptionConfigurationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpoolriskconfigurationattachment-riskexceptionconfigurationtype.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Cognito::UserPoolUser.AttributeType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpooluser-attributetype.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Config::ConfigurationAggregator.AccountAggregationSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Config::ConfigurationAggregator.OrganizationAggregationSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Config::OrganizationConfigRule.OrganizationCustomRuleMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html)
  - `ap-northeast-3`

- [AWS::Config::OrganizationConfigRule.OrganizationManagedRuleMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html)
  - `ap-northeast-3`

- [AWS::Config::RemediationConfiguration.ExecutionControls](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-executioncontrols.html)
  - `ap-northeast-3`

- [AWS::Config::RemediationConfiguration.RemediationParameterValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-remediationparametervalue.html)
  - `ap-northeast-3`

- [AWS::Config::RemediationConfiguration.ResourceValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-resourcevalue.html)
  - `ap-northeast-3`

- [AWS::Config::RemediationConfiguration.SsmControls](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-ssmcontrols.html)
  - `ap-northeast-3`

- [AWS::Config::RemediationConfiguration.StaticValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-staticvalue.html)
  - `ap-northeast-3`

- [AWS::DAX::Cluster.SSESpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dax-cluster-ssespecification.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::DLM::LifecyclePolicy.CreateRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::DLM::LifecyclePolicy.CrossRegionCopyRetainRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::DLM::LifecyclePolicy.CrossRegionCopyRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::DLM::LifecyclePolicy.FastRestoreRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::DLM::LifecyclePolicy.Parameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-parameters.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::DLM::LifecyclePolicy.PolicyDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::DLM::LifecyclePolicy.RetainRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::DLM::LifecyclePolicy.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::DMS::Endpoint.DynamoDbSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-dynamodbsettings.html)
  - `ap-northeast-3`
  - `eu-west-3`

- [AWS::DMS::Endpoint.ElasticsearchSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-elasticsearchsettings.html)
  - `ap-northeast-3`
  - `eu-west-3`

- [AWS::DMS::Endpoint.KinesisSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html)
  - `ap-northeast-3`
  - `eu-west-3`

- [AWS::DMS::Endpoint.MongoDbSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html)
  - `ap-northeast-3`
  - `eu-west-3`

- [AWS::DMS::Endpoint.S3Settings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html)
  - `ap-northeast-3`
  - `eu-west-3`

- [AWS::EC2::CapacityReservation.TagSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservation-tagspecification.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::EC2::ClientVpnEndpoint.CertificateAuthenticationRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-certificateauthenticationrequest.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::EC2::ClientVpnEndpoint.ClientAuthenticationRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientauthenticationrequest.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::EC2::ClientVpnEndpoint.ConnectionLogOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-connectionlogoptions.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::EC2::ClientVpnEndpoint.DirectoryServiceAuthenticationRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-directoryserviceauthenticationrequest.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::EC2::ClientVpnEndpoint.TagSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-tagspecification.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`

- [AWS::EC2::TrafficMirrorFilterRule.TrafficMirrorPortRange](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-trafficmirrorfilterrule-trafficmirrorportrange.html)
  - `ap-northeast-3`

- [AWS::EKS::Cluster.ResourcesVpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-resourcesvpcconfig.html)
  - `ap-northeast-3`

- [AWS::EKS::Nodegroup.RemoteAccess](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-remoteaccess.html)
  - `ap-northeast-3`

- [AWS::EKS::Nodegroup.ScalingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html)
  - `ap-northeast-3`

- [AWS::EventSchemas::Discoverer.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::EventSchemas::Registry.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::EventSchemas::Schema.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::Events::EventBusPolicy.Condition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html)
  - `ap-northeast-3`

- [AWS::FSx::FileSystem.LustreConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`

- [AWS::FSx::FileSystem.SelfManagedActiveDirectoryConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-selfmanagedactivedirectoryconfiguration.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`

- [AWS::FSx::FileSystem.WindowsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`

- [AWS::GameLift::GameSessionQueue.Destination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-destination.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::GameLift::GameSessionQueue.PlayerLatencyPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-playerlatencypolicy.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::GameLift::MatchmakingConfiguration.GameProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-matchmakingconfiguration-gameproperty.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::GameLift::Script.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Classifier.CsvClassifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-csvclassifier.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::Classifier.GrokClassifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-grokclassifier.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::Classifier.JsonClassifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-jsonclassifier.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::Classifier.XMLClassifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-classifier-xmlclassifier.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::Connection.ConnectionInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-connectioninput.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Connection.PhysicalConnectionRequirements](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-connection-physicalconnectionrequirements.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Crawler.CatalogTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-catalogtarget.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::Crawler.DynamoDBTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-dynamodbtarget.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::Crawler.JdbcTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-jdbctarget.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::Crawler.S3Target](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-s3target.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::Crawler.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-schedule.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::Crawler.SchemaChangePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-schemachangepolicy.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::Crawler.Targets](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-targets.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::DataCatalogEncryptionSettings.ConnectionPasswordEncryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-connectionpasswordencryption.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::DataCatalogEncryptionSettings.DataCatalogEncryptionSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-datacatalogencryptionsettings.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::DataCatalogEncryptionSettings.EncryptionAtRest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-datacatalogencryptionsettings-encryptionatrest.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::Database.DatabaseInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseinput.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Job.ConnectionsList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-connectionslist.html)
  - `ap-northeast-3`
  - `sa-east-1`

- [AWS::Glue::Job.ExecutionProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-executionproperty.html)
  - `ap-northeast-3`
  - `sa-east-1`

- [AWS::Glue::Job.JobCommand](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-jobcommand.html)
  - `ap-northeast-3`
  - `sa-east-1`

- [AWS::Glue::Job.NotificationProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-job-notificationproperty.html)
  - `ap-northeast-3`
  - `sa-east-1`

- [AWS::Glue::MLTransform.FindMatchesParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters-findmatchesparameters.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::MLTransform.GlueTables](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables-gluetables.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::MLTransform.InputRecordTables](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::MLTransform.TransformParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Partition.Column](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-column.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Partition.Order](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-order.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Partition.PartitionInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-partitioninput.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Partition.SerdeInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-serdeinfo.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Partition.SkewedInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-skewedinfo.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Partition.StorageDescriptor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-partition-storagedescriptor.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::SecurityConfiguration.CloudWatchEncryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-cloudwatchencryption.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::SecurityConfiguration.EncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-encryptionconfiguration.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::SecurityConfiguration.JobBookmarksEncryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-jobbookmarksencryption.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::SecurityConfiguration.S3Encryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-s3encryption.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::SecurityConfiguration.S3Encryptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-securityconfiguration-s3encryptions.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-north-1`

- [AWS::Glue::Table.Column](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-column.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Table.Order](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-order.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Table.SerdeInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-serdeinfo.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Table.SkewedInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-skewedinfo.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Table.StorageDescriptor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-storagedescriptor.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Table.TableInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableinput.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Glue::Trigger.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-action.html)
  - `ap-northeast-3`
  - `sa-east-1`

- [AWS::Glue::Trigger.Condition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-condition.html)
  - `ap-northeast-3`
  - `sa-east-1`

- [AWS::Glue::Trigger.NotificationProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-notificationproperty.html)
  - `ap-northeast-3`
  - `sa-east-1`

- [AWS::Glue::Trigger.Predicate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-trigger-predicate.html)
  - `ap-northeast-3`
  - `sa-east-1`

- [AWS::Greengrass::ConnectorDefinition.Connector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ConnectorDefinition.ConnectorDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connectordefinitionversion.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ConnectorDefinitionVersion.Connector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinitionversion-connector.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::CoreDefinition.Core](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::CoreDefinition.CoreDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-coredefinitionversion.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::CoreDefinitionVersion.Core](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::DeviceDefinition.Device](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::DeviceDefinition.DeviceDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-devicedefinitionversion.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::DeviceDefinitionVersion.Device](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::FunctionDefinition.DefaultConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-defaultconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::FunctionDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::FunctionDefinition.Execution](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-execution.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::FunctionDefinition.Function](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::FunctionDefinition.FunctionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::FunctionDefinition.FunctionDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functiondefinitionversion.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::FunctionDefinition.ResourceAccessPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-resourceaccesspolicy.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::FunctionDefinition.RunAs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-runas.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::FunctionDefinitionVersion.DefaultConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::FunctionDefinitionVersion.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::FunctionDefinitionVersion.Execution](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-execution.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::FunctionDefinitionVersion.Function](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-function.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::FunctionDefinitionVersion.FunctionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::FunctionDefinitionVersion.ResourceAccessPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-resourceaccesspolicy.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::FunctionDefinitionVersion.RunAs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-runas.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::Group.GroupVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::LoggerDefinition.Logger](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::LoggerDefinition.LoggerDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-loggerdefinitionversion.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::LoggerDefinitionVersion.Logger](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ResourceDefinition.GroupOwnerSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-groupownersetting.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ResourceDefinition.LocalDeviceResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localdeviceresourcedata.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ResourceDefinition.LocalVolumeResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ResourceDefinition.ResourceDataContainer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ResourceDefinition.ResourceDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedefinitionversion.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ResourceDefinition.ResourceInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ResourceDefinition.S3MachineLearningModelResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ResourceDefinition.SageMakerMachineLearningModelResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ResourceDefinition.SecretsManagerSecretResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-secretsmanagersecretresourcedata.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ResourceDefinitionVersion.GroupOwnerSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-groupownersetting.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ResourceDefinitionVersion.LocalDeviceResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ResourceDefinitionVersion.LocalVolumeResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ResourceDefinitionVersion.ResourceDataContainer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ResourceDefinitionVersion.ResourceInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ResourceDefinitionVersion.S3MachineLearningModelResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ResourceDefinitionVersion.SageMakerMachineLearningModelResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::ResourceDefinitionVersion.SecretsManagerSecretResourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::SubscriptionDefinition.Subscription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::SubscriptionDefinition.SubscriptionDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscriptiondefinitionversion.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Greengrass::SubscriptionDefinitionVersion.Subscription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::GuardDuty::Filter.Condition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::GuardDuty::Filter.FindingCriteria](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoT1Click::Project.DeviceTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-devicetemplate.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoT1Click::Project.PlacementTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-placementtemplate.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Channel.ChannelStorage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-channelstorage.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Channel.CustomerManagedS3](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-customermanageds3.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Channel.RetentionPeriod](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-retentionperiod.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Channel.ServiceManagedS3](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-servicemanageds3.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-action.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset.ContainerAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-containeraction.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset.DatasetContentDeliveryRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryrule.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset.DatasetContentDeliveryRuleDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryruledestination.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset.DatasetContentVersionValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable-datasetcontentversionvalue.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset.DeltaTime](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatime.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset.Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-filter.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset.GlueConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-glueconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset.IotEventsDestinationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-ioteventsdestinationconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset.OutputFileUriValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable-outputfileurivalue.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset.QueryAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-queryaction.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset.ResourceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-resourceconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset.RetentionPeriod](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-retentionperiod.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset.S3DestinationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-s3destinationconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-trigger-schedule.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset.Trigger](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-trigger.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset.TriggeringDataset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-triggeringdataset.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset.Variable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Dataset.VersioningConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-versioningconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Datastore.CustomerManagedS3](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Datastore.DatastoreStorage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorestorage.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Datastore.RetentionPeriod](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-retentionperiod.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Datastore.ServiceManagedS3](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-servicemanageds3.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Pipeline.Activity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Pipeline.AddAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-addattributes.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Pipeline.Channel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-channel.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Pipeline.Datastore](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-datastore.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Pipeline.DeviceRegistryEnrich](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Pipeline.DeviceShadowEnrich](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Pipeline.Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-filter.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Pipeline.Lambda](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-lambda.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Pipeline.Math](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-math.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Pipeline.RemoveAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-removeattributes.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTAnalytics::Pipeline.SelectAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-selectattributes.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::DetectorModel.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::DetectorModel.ClearTimer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-cleartimer.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::DetectorModel.DetectorModelDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-detectormodeldefinition.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::DetectorModel.Event](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-event.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::DetectorModel.Firehose](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-firehose.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::DetectorModel.IotEvents](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotevents.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::DetectorModel.IotTopicPublish](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iottopicpublish.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::DetectorModel.Lambda](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-lambda.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::DetectorModel.OnEnter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onenter.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::DetectorModel.OnExit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onexit.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::DetectorModel.OnInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-oninput.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::DetectorModel.ResetTimer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-resettimer.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::DetectorModel.SetTimer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-settimer.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::DetectorModel.SetVariable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-setvariable.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::DetectorModel.Sns](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sns.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::DetectorModel.Sqs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sqs.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::DetectorModel.State](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::DetectorModel.TransitionEvent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::Input.Attribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-attribute.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTEvents::Input.InputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-inputdefinition.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::IoTThingsGraph::FlowTemplate.DefinitionDocument](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotthingsgraph-flowtemplate-definitiondocument.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::KinesisAnalytics::Application.CSVMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-csvmappingparameters.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::Application.Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::Application.InputLambdaProcessor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::Application.InputParallelism](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputparallelism.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::Application.InputProcessingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputprocessingconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::Application.InputSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::Application.JSONMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-jsonmappingparameters.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::Application.KinesisFirehoseInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisfirehoseinput.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::Application.KinesisStreamsInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisstreamsinput.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::Application.MappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-mappingparameters.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::Application.RecordColumn](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::Application.RecordFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordformat.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::ApplicationOutput.DestinationSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-destinationschema.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::ApplicationOutput.KinesisFirehoseOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::ApplicationOutput.KinesisStreamsOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::ApplicationOutput.LambdaOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-lambdaoutput.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::ApplicationOutput.Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::ApplicationReferenceDataSource.CSVMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::ApplicationReferenceDataSource.JSONMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-jsonmappingparameters.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::ApplicationReferenceDataSource.MappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-mappingparameters.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::ApplicationReferenceDataSource.RecordColumn](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::ApplicationReferenceDataSource.RecordFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordformat.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::ApplicationReferenceDataSource.ReferenceDataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::ApplicationReferenceDataSource.ReferenceSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalytics::ApplicationReferenceDataSource.S3ReferenceDataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-central-1`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.ApplicationCodeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.ApplicationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.ApplicationSnapshotConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.CSVMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.CheckpointConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.CodeContent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.EnvironmentProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-environmentproperties.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.FlinkApplicationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.InputLambdaProcessor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.InputParallelism](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputparallelism.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.InputProcessingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.InputSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.JSONMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-jsonmappingparameters.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.KinesisFirehoseInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.KinesisStreamsInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisstreamsinput.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.MappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.MonitoringConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.ParallelismConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.PropertyGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.RecordColumn](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.RecordFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.S3ContentLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::Application.SqlApplicationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-sqlapplicationconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption.CloudWatchLoggingOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::ApplicationOutput.DestinationSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-destinationschema.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::ApplicationOutput.KinesisFirehoseOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisfirehoseoutput.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::ApplicationOutput.KinesisStreamsOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::ApplicationOutput.LambdaOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-lambdaoutput.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::ApplicationOutput.Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.CSVMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.JSONMappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.MappingParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.RecordColumn](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.RecordFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.ReferenceDataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.ReferenceSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.S3ReferenceDataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `ap-south-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::LakeFormation::DataLakeSettings.Admins](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-admins.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::LakeFormation::DataLakeSettings.DataLakePrincipal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-datalakeprincipal.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::LakeFormation::Permissions.ColumnWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html)
  - `us-west-1`

- [AWS::LakeFormation::Permissions.DataLakePrincipal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalakeprincipal.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::LakeFormation::Permissions.DataLocationResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html)
  - `us-west-1`

- [AWS::LakeFormation::Permissions.DatabaseResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::LakeFormation::Permissions.Resource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::LakeFormation::Permissions.TableResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::LakeFormation::Permissions.TableWithColumnsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html)
  - `us-west-1`

- [AWS::Lambda::LayerVersion.Content](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-layerversion-content.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::MSK::Cluster.BrokerNodeGroupInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html)
  - `ap-northeast-3`
  - `me-south-1`

- [AWS::MSK::Cluster.ClientAuthentication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html)
  - `ap-northeast-3`
  - `me-south-1`

- [AWS::MSK::Cluster.ConfigurationInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html)
  - `ap-northeast-3`
  - `me-south-1`

- [AWS::MSK::Cluster.EBSStorageInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html)
  - `ap-northeast-3`
  - `me-south-1`

- [AWS::MSK::Cluster.EncryptionAtRest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionatrest.html)
  - `ap-northeast-3`
  - `me-south-1`

- [AWS::MSK::Cluster.EncryptionInTransit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html)
  - `ap-northeast-3`
  - `me-south-1`

- [AWS::MSK::Cluster.EncryptionInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html)
  - `ap-northeast-3`
  - `me-south-1`

- [AWS::MSK::Cluster.JmxExporter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-jmxexporter.html)
  - `ap-northeast-3`
  - `me-south-1`

- [AWS::MSK::Cluster.NodeExporter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-nodeexporter.html)
  - `ap-northeast-3`
  - `me-south-1`

- [AWS::MSK::Cluster.OpenMonitoring](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html)
  - `ap-northeast-3`
  - `me-south-1`

- [AWS::MSK::Cluster.Prometheus](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html)
  - `ap-northeast-3`
  - `me-south-1`

- [AWS::MSK::Cluster.StorageInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-storageinfo.html)
  - `ap-northeast-3`
  - `me-south-1`

- [AWS::MSK::Cluster.Tls](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html)
  - `ap-northeast-3`
  - `me-south-1`

- [AWS::ManagedBlockchain::Member.ApprovalThresholdPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-approvalthresholdpolicy.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-2`
  - `us-west-1`
  - `eu-west-2`
  - `ap-northeast-2`

- [AWS::ManagedBlockchain::Member.MemberConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberconfiguration.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-2`
  - `us-west-1`
  - `eu-west-2`
  - `ap-northeast-2`

- [AWS::ManagedBlockchain::Member.MemberFabricConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberfabricconfiguration.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-2`
  - `us-west-1`
  - `eu-west-2`
  - `ap-northeast-2`

- [AWS::ManagedBlockchain::Member.MemberFrameworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberframeworkconfiguration.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-2`
  - `us-west-1`
  - `eu-west-2`
  - `ap-northeast-2`

- [AWS::ManagedBlockchain::Member.NetworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkconfiguration.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-2`
  - `us-west-1`
  - `eu-west-2`
  - `ap-northeast-2`

- [AWS::ManagedBlockchain::Member.NetworkFabricConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkfabricconfiguration.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-2`
  - `us-west-1`
  - `eu-west-2`
  - `ap-northeast-2`

- [AWS::ManagedBlockchain::Member.NetworkFrameworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkframeworkconfiguration.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-2`
  - `us-west-1`
  - `eu-west-2`
  - `ap-northeast-2`

- [AWS::ManagedBlockchain::Member.VotingPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-votingpolicy.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-2`
  - `us-west-1`
  - `eu-west-2`
  - `ap-northeast-2`

- [AWS::ManagedBlockchain::Node.NodeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-node-nodeconfiguration.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-2`
  - `us-west-1`
  - `eu-west-2`
  - `ap-northeast-2`

- [AWS::MediaConvert::JobTemplate.AccelerationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-accelerationsettings.html)
  - `ap-northeast-3`

- [AWS::MediaLive::Channel.AribSourceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-aribsourcesettings.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.AudioLanguageSelection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiolanguageselection.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.AudioPidSelection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiopidselection.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.AudioSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselector.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.AudioSelectorSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audioselectorsettings.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.CaptionSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselector.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.CaptionSelectorSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-captionselectorsettings.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.DvbSubSourceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-dvbsubsourcesettings.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.EmbeddedSourceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-embeddedsourcesettings.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.HlsInputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-hlsinputsettings.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.InputAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputattachment.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.InputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputsettings.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.InputSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-inputspecification.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.MediaPackageOutputDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-mediapackageoutputdestinationsettings.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.MultiplexProgramChannelDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html)
  - `us-west-1`
  - `eu-west-3`
  - `eu-north-1`
  - `us-east-2`

- [AWS::MediaLive::Channel.NetworkInputSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-networkinputsettings.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.OutputDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestination.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.OutputDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-outputdestinationsettings.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.Scte20SourceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte20sourcesettings.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.Scte27SourceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-scte27sourcesettings.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.TeletextSourceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-teletextsourcesettings.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.VideoSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselector.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.VideoSelectorPid](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorpid.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.VideoSelectorProgramId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorprogramid.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Channel.VideoSelectorSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-videoselectorsettings.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Input.InputDestinationRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputdestinationrequest.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Input.InputSourceRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputsourcerequest.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Input.InputVpcRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-inputvpcrequest.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::Input.MediaConnectFlowRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-input-mediaconnectflowrequest.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaLive::InputSecurityGroup.InputWhitelistRuleCidr](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-inputsecuritygroup-inputwhitelistrulecidr.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `eu-west-2`
  - `us-east-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::MediaStore::Container.CorsRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediastore-container-corsrule.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-south-1`
  - `eu-west-3`

- [AWS::OpsWorksCM::Server.EngineAttribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworkscm-server-engineattribute.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::ApplicationSettings.CampaignHook](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::ApplicationSettings.Limits](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::ApplicationSettings.QuietTime](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-quiettime.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Campaign.AttributeDimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-attributedimension.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Campaign.CampaignEmailMessage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Campaign.CampaignEventFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigneventfilter.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Campaign.CampaignHook](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Campaign.CampaignSmsMessage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Campaign.EventDimensions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Campaign.Limits](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Campaign.Message](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Campaign.MessageConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Campaign.MetricDimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-metricdimension.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Campaign.QuietTime](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule-quiettime.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Campaign.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Campaign.SetDimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-setdimension.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Campaign.WriteTreatmentResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::PushTemplate.APNSPushNotificationTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::PushTemplate.AndroidPushNotificationTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::PushTemplate.DefaultPushNotificationTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Segment.AttributeDimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-attributedimension.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Segment.Behavior](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Segment.Coordinates](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Segment.Demographic](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Segment.GPSPoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Segment.Groups](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Segment.Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Segment.Recency](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior-recency.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Segment.SegmentDimensions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Segment.SegmentGroups](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Segment.SetDimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-setdimension.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Pinpoint::Segment.SourceSegments](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups-sourcesegments.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::PinpointEmail::ConfigurationSet.DeliveryOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-deliveryoptions.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::PinpointEmail::ConfigurationSet.ReputationOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-reputationoptions.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::PinpointEmail::ConfigurationSet.SendingOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-sendingoptions.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::PinpointEmail::ConfigurationSet.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-tags.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::PinpointEmail::ConfigurationSet.TrackingOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-trackingoptions.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::PinpointEmail::ConfigurationSetEventDestination.CloudWatchDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-cloudwatchdestination.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::PinpointEmail::ConfigurationSetEventDestination.DimensionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::PinpointEmail::ConfigurationSetEventDestination.EventDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::PinpointEmail::ConfigurationSetEventDestination.KinesisFirehoseDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-kinesisfirehosedestination.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::PinpointEmail::ConfigurationSetEventDestination.PinpointDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-pinpointdestination.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::PinpointEmail::ConfigurationSetEventDestination.SnsDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-snsdestination.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::PinpointEmail::DedicatedIpPool.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-dedicatedippool-tags.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::PinpointEmail::Identity.MailFromAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-mailfromattributes.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::PinpointEmail::Identity.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-tags.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `us-east-2`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::RoboMaker::RobotApplication.RobotSoftwareSuite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-robotsoftwaresuite.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::RoboMaker::RobotApplication.SourceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-sourceconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::RoboMaker::SimulationApplication.RenderingEngine](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-renderingengine.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::RoboMaker::SimulationApplication.RobotSoftwareSuite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-robotsoftwaresuite.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::RoboMaker::SimulationApplication.SimulationSoftwareSuite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-simulationsoftwaresuite.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::RoboMaker::SimulationApplication.SourceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-sourceconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Route53Resolver::ResolverEndpoint.IpAddressRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`

- [AWS::Route53Resolver::ResolverRule.TargetAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`

- [AWS::SES::ConfigurationSetEventDestination.CloudWatchDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-cloudwatchdestination.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SES::ConfigurationSetEventDestination.DimensionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SES::ConfigurationSetEventDestination.EventDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SES::ConfigurationSetEventDestination.KinesisFirehoseDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SES::ReceiptFilter.Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-filter.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SES::ReceiptFilter.IpFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-ipfilter.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SES::ReceiptRule.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SES::ReceiptRule.AddHeaderAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SES::ReceiptRule.BounceAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SES::ReceiptRule.LambdaAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SES::ReceiptRule.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SES::ReceiptRule.S3Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SES::ReceiptRule.SNSAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SES::ReceiptRule.StopAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SES::ReceiptRule.WorkmailAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SES::Template.Template](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SSM::MaintenanceWindowTarget.Targets](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtarget-targets.html)
  - Now available to **ALL** regions.

- [AWS::SSM::MaintenanceWindowTask.LoggingInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SSM::MaintenanceWindowTask.MaintenanceWindowAutomationParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowautomationparameters.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SSM::MaintenanceWindowTask.MaintenanceWindowLambdaParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SSM::MaintenanceWindowTask.MaintenanceWindowRunCommandParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SSM::MaintenanceWindowTask.MaintenanceWindowStepFunctionsParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SSM::MaintenanceWindowTask.NotificationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SSM::MaintenanceWindowTask.Target](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-target.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SSM::MaintenanceWindowTask.TaskInvocationParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SSM::PatchBaseline.PatchFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfilter.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::SSM::PatchBaseline.PatchFilterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfiltergroup.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::SSM::PatchBaseline.PatchSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::SSM::PatchBaseline.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::SSM::PatchBaseline.RuleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rulegroup.html)
  - `ap-northeast-3`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::SSM::ResourceDataSync.AwsOrganizationsSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-awsorganizationssource.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SSM::ResourceDataSync.S3Destination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SSM::ResourceDataSync.SyncSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SageMaker::CodeRepository.GitConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::SageMaker::Endpoint.VariantProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-variantproperty.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SageMaker::EndpointConfig.ProductionVariant](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SageMaker::Model.ContainerDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::SageMaker::Model.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-vpcconfig.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::SageMaker::NotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHook](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SageMaker::Workteam.CognitoMemberDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-cognitomemberdefinition.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SageMaker::Workteam.MemberDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-memberdefinition.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SageMaker::Workteam.NotificationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-notificationconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `ap-northeast-2`
  - `eu-north-1`

- [AWS::SecretsManager::RotationSchedule.RotationRules](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-rotationschedule-rotationrules.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::SecretsManager::Secret.GenerateSecretString](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-generatesecretstring.html)
  - `ap-northeast-3`
  - `eu-north-1`

- [AWS::ServiceCatalog::CloudFormationProduct.ProvisioningArtifactProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html)
  - `ap-northeast-3`

- [AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningparameter.html)
  - `ap-northeast-3`

- [AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningPreferences](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html)
  - `ap-northeast-3`

- [AWS::ServiceDiscovery::Service.DnsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsconfig.html)
  - `sa-east-1`
  - `ap-northeast-3`

- [AWS::ServiceDiscovery::Service.DnsRecord](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsrecord.html)
  - `sa-east-1`
  - `ap-northeast-3`

- [AWS::ServiceDiscovery::Service.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckconfig.html)
  - `sa-east-1`
  - `ap-northeast-3`

- [AWS::ServiceDiscovery::Service.HealthCheckCustomConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckcustomconfig.html)
  - `sa-east-1`
  - `ap-northeast-3`

- [AWS::StepFunctions::Activity.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::StepFunctions::StateMachine.CloudWatchLogsLogGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination-cloudwatchlogsloggroup.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::StepFunctions::StateMachine.LogDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::StepFunctions::StateMachine.LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::StepFunctions::StateMachine.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html)
  - `ap-northeast-3`
  - `us-west-1`
  - `sa-east-1`
  - `eu-west-2`
  - `ap-south-1`
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-north-1`

- [AWS::Transfer::Server.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html)
  - `ap-northeast-3`

- [AWS::Transfer::Server.IdentityProviderDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html)
  - `ap-northeast-3`

- [AWS::Transfer::User.HomeDirectoryMapEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html)
  - `ap-northeast-3`

- [AWS::Transfer::User.SshPublicKey]()
  - `ap-northeast-3`

- [AWS::WAFRegional::ByteMatchSet.ByteMatchTuple](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::ByteMatchSet.FieldToMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-fieldtomatch.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::GeoMatchSet.GeoMatchConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-geomatchset-geomatchconstraint.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::IPSet.IPSetDescriptor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ipset-ipsetdescriptor.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::RateBasedRule.Predicate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ratebasedrule-predicate.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::Rule.Predicate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::SizeConstraintSet.FieldToMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-fieldtomatch.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::SizeConstraintSet.SizeConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::SqlInjectionMatchSet.FieldToMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-fieldtomatch.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::SqlInjectionMatchSet.SqlInjectionMatchTuple](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::WebACL.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-action.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::WebACL.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::XssMatchSet.FieldToMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-fieldtomatch.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [AWS::WAFRegional::XssMatchSet.XssMatchTuple](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-xssmatchtuple.html)
  - `ap-northeast-3`
  - `sa-east-1`
  - `eu-west-3`
  - `ap-south-1`

- [Alexa::ASK::Skill.AuthenticationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-authenticationconfiguration.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `eu-north-1`

- [Alexa::ASK::Skill.Overrides](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-overrides.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `eu-north-1`

- [Alexa::ASK::Skill.SkillPackage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html)
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `eu-north-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v10.3.0: [AWS::Backup::BackupPlan.CopyActionResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html)
    - `ap-northeast-1`
    - `eu-west-2`
    - `eu-west-1`
    - `ap-northeast-3`
    - `ap-northeast-2`
    - `ca-central-1`
    - `ap-southeast-1`
    - `us-east-2`
    - `us-west-1`
    - `us-west-2`

  - Since v10.3.0: [AWS::LakeFormation::Permissions.ColumnWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html)
    - `ap-northeast-1`
    - `us-west-1`
    - `us-west-2`

  - Since v10.3.0: [AWS::LakeFormation::Permissions.DataLocationResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html)
    - `ap-northeast-1`
    - `us-west-1`
    - `us-west-2`

  - Since v10.3.0: [AWS::LakeFormation::Permissions.TableWithColumnsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html)
    - `ap-northeast-1`
    - `us-west-1`
    - `us-west-2`

  - Since v10.3.0: [AWS::MediaLive::Channel.MultiplexProgramChannelDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html)
    - `ap-northeast-1`
    - `eu-north-1`
    - `ap-south-1`
    - `eu-west-3`
    - `eu-west-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `us-east-2`
    - `us-west-1`
    - `us-west-2`

- New PropertyType(s) Missing
  - [AWS::CloudFront::Distribution.OriginGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html)
    - `ap-south-1`

  - [AWS::CloudFront::Distribution.OriginGroupFailoverCriteria](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupfailovercriteria.html)
    - `ap-south-1`

  - [AWS::CloudFront::Distribution.OriginGroupMember](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmember.html)
    - `ap-south-1`

  - [AWS::CloudFront::Distribution.OriginGroupMembers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmembers.html)
    - `ap-south-1`

  - [AWS::CloudFront::Distribution.OriginGroups](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroups.html)
    - `ap-south-1`

  - [AWS::CloudFront::Distribution.StatusCodes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-statuscodes.html)
    - `ap-south-1`

- PropertyType(s) No Longer Missing
  - [AWS::Cognito::UserPool.AccountRecoverySetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-accountrecoverysetting.html)
    - Was missing since v10.3.0

  - [AWS::Cognito::UserPool.RecoveryOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-recoveryoption.html)
    - Was missing since v10.3.0

## [10.3.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.3.0) (2020-01-20)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v10-changelog.json)
  - Change source is a diff between [v10.3.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.3.0) and [v10.2.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.2.0)

### Totals

- TotalPropertyTypes: 1274 **(+11)**
- TotalPropertyTypesSupportedGlobally: 481 **(+1)**
- TotalResourceTypes: 488 **(+0)**
- TotalResourceTypesSupportedGlobally: 191 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::Backup::BackupPlan.CopyActionResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html)
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Cognito::UserPool.AccountRecoverySetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-accountrecoverysetting.html)
  - `ap-south-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `us-east-2`

- [AWS::Cognito::UserPool.RecoveryOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-recoveryoption.html)
  - `ap-south-1`
  - `eu-west-2`
  - `ap-northeast-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `us-east-2`

- [AWS::EC2::Instance.HibernationOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-hibernationoptions.html)
  - Available in **ALL** regions.

- [AWS::LakeFormation::Permissions.ColumnWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html)
  - `ap-northeast-1`
  - `us-west-2`

- [AWS::LakeFormation::Permissions.DataLocationResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html)
  - `ap-northeast-1`
  - `us-west-2`

- [AWS::LakeFormation::Permissions.TableWithColumnsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html)
  - `ap-northeast-1`
  - `us-west-2`

- [AWS::SSM::ResourceDataSync.AwsOrganizationsSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-awsorganizationssource.html)
  - `us-east-1`
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
  - `cn-north-1`
  - `cn-northwest-1`
  - `us-gov-west-1`

- [AWS::SSM::ResourceDataSync.S3Destination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html)
  - `us-east-1`
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
  - `cn-north-1`
  - `cn-northwest-1`
  - `us-gov-west-1`

- [AWS::SSM::ResourceDataSync.SyncSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html)
  - `us-east-1`
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
  - `cn-north-1`
  - `cn-northwest-1`
  - `us-gov-west-1`

- [AWS::Transfer::User.HomeDirectoryMapEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html)
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

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Athena::NamedQuery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html)
  - `ap-south-1`
  - `ca-central-1`

- [AWS::CloudFront::Distribution](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html)
  - `eu-north-1`

- [AWS::PinpointEmail::DedicatedIpPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html)
  - `us-west-2`

- [AWS::SSM::ResourceDataSync](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html)
  - `cn-northwest-1`

- [AWS::CloudFront::Distribution.CacheBehavior](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html)
  - `eu-north-1`

- [AWS::CloudFront::Distribution.Cookies](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cookies.html)
  - `eu-north-1`

- [AWS::CloudFront::Distribution.CustomErrorResponse](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html)
  - `eu-north-1`

- [AWS::CloudFront::Distribution.CustomOriginConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html)
  - `eu-north-1`

- [AWS::CloudFront::Distribution.DefaultCacheBehavior](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html)
  - `eu-north-1`

- [AWS::CloudFront::Distribution.DistributionConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html)
  - `eu-north-1`

- [AWS::CloudFront::Distribution.ForwardedValues](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html)
  - `eu-north-1`

- [AWS::CloudFront::Distribution.GeoRestriction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-georestriction.html)
  - `eu-north-1`

- [AWS::CloudFront::Distribution.LambdaFunctionAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-lambdafunctionassociation.html)
  - `eu-north-1`

- [AWS::CloudFront::Distribution.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-logging.html)
  - `eu-north-1`

- [AWS::CloudFront::Distribution.Origin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html)
  - `eu-north-1`

- [AWS::CloudFront::Distribution.OriginCustomHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origincustomheader.html)
  - `eu-north-1`

- [AWS::CloudFront::Distribution.Restrictions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-restrictions.html)
  - `eu-north-1`

- [AWS::CloudFront::Distribution.S3OriginConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-s3originconfig.html)
  - `eu-north-1`

- [AWS::CloudFront::Distribution.ViewerCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html)
  - `eu-north-1`

- [AWS::DLM::LifecyclePolicy.CrossRegionCopyRetainRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.html)
  - `ap-northeast-2`

- [AWS::DLM::LifecyclePolicy.CrossRegionCopyRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html)
  - `ap-northeast-2`

- [AWS::MediaLive::Channel.MultiplexProgramChannelDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html)
  - `us-west-2`
  - `ap-northeast-1`

- [AWS::PinpointEmail::DedicatedIpPool.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-dedicatedippool-tags.html)
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v10.2.0: [AWS::MediaLive::Channel.MultiplexProgramChannelDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html)
    - `ap-south-1`
    - `eu-west-1`
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `us-west-2`

- New PropertyType(s) Missing
  - [AWS::Backup::BackupPlan.CopyActionResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html)
    - `eu-west-2`
    - `eu-west-1`
    - `ap-northeast-2`
    - `ap-northeast-1`
    - `ca-central-1`
    - `ap-southeast-1`
    - `us-east-2`
    - `us-west-1`
    - `us-west-2`

  - [AWS::Cognito::UserPool.AccountRecoverySetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-accountrecoverysetting.html)
    - `ap-south-1`
    - `eu-west-2`
    - `ap-northeast-1`
    - `ca-central-1`
    - `ap-southeast-1`
    - `us-east-2`

  - [AWS::Cognito::UserPool.RecoveryOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-recoveryoption.html)
    - `ap-south-1`
    - `eu-west-2`
    - `ap-northeast-1`
    - `ca-central-1`
    - `ap-southeast-1`
    - `us-east-2`

  - [AWS::LakeFormation::Permissions.ColumnWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html)
    - `ap-northeast-1`
    - `us-west-2`

  - [AWS::LakeFormation::Permissions.DataLocationResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html)
    - `ap-northeast-1`
    - `us-west-2`

  - [AWS::LakeFormation::Permissions.TableWithColumnsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html)
    - `ap-northeast-1`
    - `us-west-2`

## [10.2.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.2.0) (2019-12-23)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v10-changelog.json)
  - Change source is a diff between [v10.2.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.2.0) and [v10.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.1.0)

### Totals

- TotalPropertyTypes: 1263 **(+8)**
- TotalPropertyTypesSupportedGlobally: 480 **(+0)**
- TotalResourceTypes: 488 **(+2)**
- TotalResourceTypesSupportedGlobally: 191 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::CodeBuild::ReportGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html)
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
  - `cn-north-1`
  - `cn-northwest-1`
  - `me-south-1`

- [AWS::EC2::GatewayRouteTableAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-gatewayroutetableassociation.html)
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

- [AWS::CodeBuild::ReportGroup.ReportExportConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-reportexportconfig.html)
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
  - `cn-north-1`
  - `cn-northwest-1`
  - `me-south-1`

- [AWS::CodeBuild::ReportGroup.S3ReportExportConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html)
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
  - `cn-north-1`
  - `cn-northwest-1`
  - `me-south-1`

- [AWS::DLM::LifecyclePolicy.CrossRegionCopyRetainRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.html)
  - `us-east-1`
  - `ap-south-1`
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

- [AWS::DLM::LifecyclePolicy.CrossRegionCopyRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html)
  - `us-east-1`
  - `ap-south-1`
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

- [AWS::MSK::Cluster.JmxExporter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-jmxexporter.html)
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

- [AWS::MSK::Cluster.NodeExporter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-nodeexporter.html)
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

- [AWS::MSK::Cluster.OpenMonitoring](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html)
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

- [AWS::MSK::Cluster.Prometheus](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html)
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

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Route53Resolver::ResolverEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html)
  - `ap-east-1`
  - `eu-north-1`

- [AWS::Route53Resolver::ResolverRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html)
  - `ap-east-1`
  - `eu-north-1`

- [AWS::Route53Resolver::ResolverRuleAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html)
  - `ap-east-1`
  - `eu-north-1`

- [AWS::Route53Resolver::ResolverEndpoint.IpAddressRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html)
  - `ap-east-1`
  - `eu-north-1`

- [AWS::Route53Resolver::ResolverRule.TargetAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html)
  - `ap-east-1`
  - `eu-north-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v10.1.0: [AWS::MediaLive::Channel.MultiplexProgramChannelDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html)
    - `ap-south-1`
    - `eu-west-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`

## [10.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.1.0) (2019-12-13)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v10-changelog.json)
  - Change source is a diff between [v10.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.1.0) and [v10.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.0.0)

### Totals

- TotalPropertyTypes: 1255 **(+1)**
- TotalPropertyTypesSupportedGlobally: 480 **(+0)**
- TotalResourceTypes: 486 **(+0)**
- TotalResourceTypesSupportedGlobally: 191 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::MediaLive::Channel.MultiplexProgramChannelDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html)
  - `ap-south-1`
  - `eu-west-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Glue::MLTransform](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html)
  - `ap-south-1`
  - `ca-central-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`

- [AWS::Glue::MLTransform.FindMatchesParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters-findmatchesparameters.html)
  - `ap-south-1`
  - `ca-central-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`

- [AWS::Glue::MLTransform.GlueTables](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables-gluetables.html)
  - `ap-south-1`
  - `ca-central-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`

- [AWS::Glue::MLTransform.InputRecordTables](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-inputrecordtables.html)
  - `ap-south-1`
  - `ca-central-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`

- [AWS::Glue::MLTransform.TransformParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformparameters.html)
  - `ap-south-1`
  - `ca-central-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `us-west-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-west-2`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- New PropertyType(s) Missing
  - [AWS::MediaLive::Channel.MultiplexProgramChannelDestinationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.html)
    - `ap-south-1`
    - `eu-west-1`
    - `ap-southeast-1`
    - `ap-southeast-2`
    - `eu-central-1`

## [10.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.0.0) (2019-12-05)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v10-changelog.json)
  - Change source is a diff between [v10.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.0.0) and [v9.1.1](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v9.1.1)

### Totals

- TotalPropertyTypes: 1254 **(+0)**
- TotalPropertyTypesSupportedGlobally: 480 **(+2)**
- TotalResourceTypes: 486 **(+5)**
- TotalResourceTypesSupportedGlobally: 191 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::AccessAnalyzer::Analyzer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html)
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

- [AWS::EventSchemas::Discoverer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::EventSchemas::Registry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::EventSchemas::Schema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::S3::AccessPoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accesspoint.html)
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

- [AWS::AccessAnalyzer::Analyzer.ArchiveRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html)
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

- [AWS::AccessAnalyzer::Analyzer.Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html)
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

- [AWS::EventSchemas::Discoverer.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::EventSchemas::Registry.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::EventSchemas::Schema.TagsEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Lambda::Alias.ProvisionedConcurrencyConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-alias-provisionedconcurrencyconfiguration.html)
  - Available in **ALL** regions.

- [AWS::Lambda::Version.ProvisionedConcurrencyConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-version-provisionedconcurrencyconfiguration.html)
  - Available in **ALL** regions.

- [AWS::S3::AccessPoint.PublicAccessBlockConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-accesspoint-publicaccessblockconfiguration.html)
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

- [AWS::S3::AccessPoint.VpcConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-accesspoint-vpcconfiguration.html)
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

- [AWS::StepFunctions::StateMachine.CloudWatchLogsLogGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination-cloudwatchlogsloggroup.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::StepFunctions::StateMachine.LogDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::StepFunctions::StateMachine.LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html)
  - `us-east-1`
  - `eu-west-1`
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-2`

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::WAFv2::IPSet.IPSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-ipset-ipset.html)
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

- [AWS::WAFv2::IPSet.IPSetSummary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-ipset-ipsetsummary.html)
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

- [AWS::WAFv2::IPSet.IPSets](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-ipset-ipsets.html)
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

- [AWS::WAFv2::RegexPatternSet.RegexPatternSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-regexpatternset-regexpatternset.html)
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

- [AWS::WAFv2::RegexPatternSet.RegexPatternSetSummary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-regexpatternset-regexpatternsetsummary.html)
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

- [AWS::WAFv2::RegexPatternSet.RegexPatternSets](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-regexpatternset-regexpatternsets.html)
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

- [AWS::WAFv2::RuleGroup.RuleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rulegroup.html)
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

- [AWS::WAFv2::RuleGroup.RuleGroupSummary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rulegroupsummary.html)
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

- [AWS::WAFv2::RuleGroup.RuleGroups](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rulegroups.html)
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

- [AWS::WAFv2::WebACL.WebACL](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-webacl.html)
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

- [AWS::WAFv2::WebACL.WebACLSummary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-webaclsummary.html)
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

- [AWS::WAFv2::WebACL.WebACLs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-webacls.html)
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

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::ApiGatewayV2::Api.BodyS3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html)
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `eu-west-1`
  - `eu-central-1`
  - `ap-southeast-2`
  - `eu-west-2`
  - `us-west-2`
  - `ap-northeast-1`

- [AWS::ApiGatewayV2::Api.Cors](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html)
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `eu-west-1`
  - `eu-central-1`
  - `ap-southeast-2`
  - `eu-west-2`
  - `us-west-2`
  - `ap-northeast-1`

- [AWS::ApiGatewayV2::Authorizer.JWTConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html)
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `eu-west-1`
  - `eu-central-1`
  - `ap-southeast-2`
  - `eu-west-2`
  - `us-west-2`
  - `ap-northeast-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType(s) No Longer Missing
  - [AWS::ApiGatewayV2::Api.BodyS3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html)
    - Was missing since v9.1.1

  - [AWS::ApiGatewayV2::Api.Cors](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html)
    - Was missing since v9.1.1

  - [AWS::ApiGatewayV2::Authorizer.JWTConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html)
    - Was missing since v9.1.1

