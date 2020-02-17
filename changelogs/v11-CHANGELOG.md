# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v11-changelog.json`](changelogs/v11-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [11.0.0](#1100-2020-02-17)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [11.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v11.0.0) (2020-02-17)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v11-changelog.json)
  - Change source is a diff between [v11.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v11.0.0) and [v10.5.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v10.5.0)

### Totals

- TotalPropertyTypes: 1305 **(+12)**
- TotalPropertyTypesSupportedGlobally: 509 **(+7)**
- TotalResourceTypes: 503 **(+6)**
- TotalResourceTypesSupportedGlobally: 192 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::Config::ConformancePack](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html)
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

- [AWS::Config::OrganizationConformancePack](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html)
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

- [AWS::EC2::LocalGatewayRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.html)
  - `us-east-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::EC2::LocalGatewayRouteTableVPCAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetablevpcassociation.html)
  - `us-east-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::FMS::NotificationChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html)
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

- [AWS::FMS::Policy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html)
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

- [AWS::Config::ConformancePack.ConformancePackInputParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-conformancepackinputparameter.html)
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

- [AWS::Config::OrganizationConformancePack.ConformancePackInputParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconformancepack-conformancepackinputparameter.html)
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

- [AWS::EC2::LocalGatewayRouteTableVPCAssociation.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-localgatewayroutetablevpcassociation-tags.html)
  - `us-east-1`
  - `eu-west-3`
  - `eu-west-2`
  - `eu-west-1`
  - `ap-northeast-1`
  - `ca-central-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::ElasticLoadBalancingV2::Listener.ForwardConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-forwardconfig.html)
  - Available in **ALL** regions.

- [AWS::ElasticLoadBalancingV2::Listener.TargetGroupStickinessConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-targetgroupstickinessconfig.html)
  - Available in **ALL** regions.

- [AWS::ElasticLoadBalancingV2::Listener.TargetGroupTuple](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-targetgrouptuple.html)
  - Available in **ALL** regions.

- [AWS::ElasticLoadBalancingV2::ListenerRule.ForwardConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-forwardconfig.html)
  - Available in **ALL** regions.

- [AWS::ElasticLoadBalancingV2::ListenerRule.TargetGroupStickinessConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-targetgroupstickinessconfig.html)
  - Available in **ALL** regions.

- [AWS::ElasticLoadBalancingV2::ListenerRule.TargetGroupTuple](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listenerrule-targetgrouptuple.html)
  - Available in **ALL** regions.

- [AWS::FMS::Policy.IEMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html)
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

- [AWS::FMS::Policy.PolicyTag](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html)
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

- [AWS::FMS::Policy.ResourceTag](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html)
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

- [AWS::AppSync::ApiKey](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html)
  - `cn-north-1`

- [AWS::AppSync::DataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html)
  - `cn-north-1`

- [AWS::AppSync::FunctionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html)
  - `cn-north-1`

- [AWS::AppSync::GraphQLApi](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html)
  - `cn-north-1`

- [AWS::AppSync::GraphQLSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html)
  - `cn-north-1`

- [AWS::AppSync::Resolver](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html)
  - `cn-north-1`

- [AWS::Backup::BackupPlan](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::CodeStarNotifications::NotificationRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::ACMPCA::CertificateAuthority.CrlConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html)
  - `us-west-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-2`
  - `eu-central-1`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-3`
  - `ap-southeast-1`
  - `ca-central-1`
  - `sa-east-1`

- [AWS::ACMPCA::CertificateAuthority.RevocationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-revocationconfiguration.html)
  - `us-west-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-2`
  - `eu-central-1`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-3`
  - `ap-southeast-1`
  - `ca-central-1`
  - `sa-east-1`

- [AWS::ACMPCA::CertificateAuthority.Subject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html)
  - `us-west-1`
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-2`
  - `eu-central-1`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-3`
  - `ap-southeast-1`
  - `ca-central-1`
  - `sa-east-1`

- [AWS::AppSync::DataSource.AuthorizationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html)
  - `cn-north-1`

- [AWS::AppSync::DataSource.AwsIamConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html)
  - `cn-north-1`

- [AWS::AppSync::DataSource.DeltaSyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html)
  - `cn-north-1`

- [AWS::AppSync::DataSource.DynamoDBConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html)
  - `cn-north-1`

- [AWS::AppSync::DataSource.ElasticsearchConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html)
  - `cn-north-1`

- [AWS::AppSync::DataSource.HttpConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html)
  - `cn-north-1`

- [AWS::AppSync::DataSource.LambdaConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-lambdaconfig.html)
  - `cn-north-1`

- [AWS::AppSync::DataSource.RdsHttpEndpointConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html)
  - `cn-north-1`

- [AWS::AppSync::DataSource.RelationalDatabaseConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html)
  - `cn-north-1`

- [AWS::AppSync::GraphQLApi.AdditionalAuthenticationProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html)
  - `cn-north-1`

- [AWS::AppSync::GraphQLApi.AdditionalAuthenticationProviders](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationproviders.html)
  - `cn-north-1`

- [AWS::AppSync::GraphQLApi.CognitoUserPoolConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html)
  - `cn-north-1`

- [AWS::AppSync::GraphQLApi.LogConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html)
  - `cn-north-1`

- [AWS::AppSync::GraphQLApi.OpenIDConnectConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html)
  - `cn-north-1`

- [AWS::AppSync::GraphQLApi.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-tags.html)
  - `cn-north-1`

- [AWS::AppSync::GraphQLApi.UserPoolConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html)
  - `cn-north-1`

- [AWS::AppSync::Resolver.CachingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html)
  - `cn-north-1`

- [AWS::AppSync::Resolver.LambdaConflictHandlerConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-lambdaconflicthandlerconfig.html)
  - `cn-north-1`

- [AWS::AppSync::Resolver.PipelineConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-pipelineconfig.html)
  - `cn-north-1`

- [AWS::AppSync::Resolver.SyncConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html)
  - `cn-north-1`

- [AWS::Backup::BackupPlan.BackupPlanResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::Backup::BackupPlan.BackupRuleResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::Backup::BackupPlan.CopyActionResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::Backup::BackupPlan.LifecycleResourceType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-lifecycleresourcetype.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::CodeStarNotifications::NotificationRule.Target](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestarnotifications-notificationrule-target.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::EC2::LaunchTemplate.MetadataOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-metadataoptions.html)
  - Now available to **ALL** regions.

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v10.5.0: [AWS::CloudFront::Distribution.OriginGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html)
    - `ap-south-1`

  - Since v10.5.0: [AWS::CloudFront::Distribution.OriginGroupFailoverCriteria](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupfailovercriteria.html)
    - `ap-south-1`

  - Since v10.5.0: [AWS::CloudFront::Distribution.OriginGroupMember](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmember.html)
    - `ap-south-1`

  - Since v10.5.0: [AWS::CloudFront::Distribution.OriginGroupMembers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmembers.html)
    - `ap-south-1`

  - Since v10.5.0: [AWS::CloudFront::Distribution.OriginGroups](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroups.html)
    - `ap-south-1`

  - Since v10.5.0: [AWS::CloudFront::Distribution.StatusCodes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-statuscodes.html)
    - `ap-south-1`

  - Since v10.5.0: [AWS::Cognito::UserPool.UsernameConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-usernameconfiguration.html)
    - `ap-south-1`
    - `ca-central-1`
    - `us-east-2`

  - Since v10.5.0: [AWS::LakeFormation::Permissions.ColumnWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html)
    - `ap-northeast-1`
    - `us-west-2`

  - Since v10.5.0: [AWS::LakeFormation::Permissions.DataLocationResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html)
    - `ap-northeast-1`
    - `us-west-2`

  - Since v10.5.0: [AWS::LakeFormation::Permissions.TableWithColumnsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html)
    - `ap-northeast-1`
    - `us-west-2`

