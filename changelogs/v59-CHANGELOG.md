# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v59-changelog.json`](changelogs/v59-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [59.0.0](#5900-2022-03-04)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [59.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v59.0.0) (2022-03-04)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v59-changelog.json)
  - Change source is a diff between [v59.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v59.0.0) and [v58.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v58.0.0)

### Totals

- TotalPropertyTypes: 2986 **(+3)**
- TotalPropertyTypesSupportedGlobally: 1066 **(+1)**
- TotalResourceTypes: 894 **(+3)**
- TotalResourceTypesSupportedGlobally: 338 **(+3)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::EKS::IdentityProviderConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-identityproviderconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::MSK::BatchScramSecret](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html)
  - Available in **ALL** regions.

- [AWS::MSK::Configuration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html)
  - Available in **ALL** regions.

- [AWS::EKS::IdentityProviderConfig.OidcIdentityProviderConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-identityproviderconfig-oidcidentityproviderconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::EKS::IdentityProviderConfig.RequiredClaim](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-identityproviderconfig-requiredclaim.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::FIS::ExperimentTemplate.ExperimentTemplateLogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatelogconfiguration.html)
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::AutoScaling::WarmPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-warmpool.html)
  - Now available to **ALL** regions.

- [AWS::CloudFront::Distribution](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::AppFlow::Flow.SAPODataDestinationProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatadestinationproperties.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `eu-central-1`
  - `ca-central-1`
  - `ap-south-1`
  - `us-east-2`
  - `eu-west-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `ap-northeast-1`
  - `eu-west-2`
  - `us-west-1`

- [AWS::AppFlow::Flow.SuccessResponseHandlingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-successresponsehandlingconfig.html)
  - `ap-northeast-2`
  - `sa-east-1`
  - `eu-central-1`
  - `ca-central-1`
  - `ap-south-1`
  - `us-east-2`
  - `eu-west-1`
  - `ap-southeast-1`
  - `eu-west-3`
  - `ap-northeast-1`
  - `eu-west-2`
  - `us-west-1`

- [AWS::AutoScaling::WarmPool.InstanceReusePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-warmpool-instancereusepolicy.html)
  - Now available to **ALL** regions.

- [AWS::CloudFront::Distribution.CacheBehavior](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.Cookies](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cookies.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.CustomErrorResponse](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customerrorresponse.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.CustomOriginConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-customoriginconfig.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.DefaultCacheBehavior](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-defaultcachebehavior.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.DistributionConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.ForwardedValues](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-forwardedvalues.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.FunctionAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-functionassociation.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.GeoRestriction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-georestriction.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.LambdaFunctionAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-lambdafunctionassociation.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.LegacyCustomOrigin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacycustomorigin.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.LegacyS3Origin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-legacys3origin.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-logging.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.Origin](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.OriginCustomHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origincustomheader.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.OriginGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.OriginGroupFailoverCriteria](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupfailovercriteria.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.OriginGroupMember](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmember.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.OriginGroupMembers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmembers.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.OriginGroups](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroups.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.OriginShield](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-originshield.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.Restrictions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-restrictions.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.S3OriginConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-s3originconfig.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.StatusCodes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-statuscodes.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

- [AWS::CloudFront::Distribution.ViewerCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-viewercertificate.html)
  - `eu-south-1`
  - `me-south-1`
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-3`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v58.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v58.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v58.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v58.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v58.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v58.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- PropertyType Still Missing
  - Since v58.0.0: [AWS::DevOpsGuru::ResourceCollection.TagCollection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-tagcollection.html)
    - `eu-central-1`

  - Since v58.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v58.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v58.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v58.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::FIS::ExperimentTemplate.ExperimentTemplateLogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatelogconfiguration.html)
    - `eu-central-1`

