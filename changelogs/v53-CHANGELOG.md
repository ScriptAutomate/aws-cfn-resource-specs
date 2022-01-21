# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v53-changelog.json`](changelogs/v53-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [53.0.0](#5300-2022-01-14)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [53.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v53.0.0) (2022-01-14)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v53-changelog.json)
  - Change source is a diff between [v53.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v53.0.0) and [v52.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v52.0.0)

### Totals

- TotalPropertyTypes: 2912 **(+7)**
- TotalPropertyTypesSupportedGlobally: 1051 **(+1)**
- TotalResourceTypes: 881 **(+2)**
- TotalResourceTypesSupportedGlobally: 333 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::Forecast::Dataset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-dataset.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Forecast::DatasetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-forecast-datasetgroup.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::ApplicationInsights::Application.HAClusterPrometheusExporter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-haclusterprometheusexporter.html)
  - `cn-north-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::ApplicationInsights::Application.HANAPrometheusExporter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-hanaprometheusexporter.html)
  - `cn-north-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::AutoScaling::WarmPool.InstanceReusePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-warmpool-instancereusepolicy.html)
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

- [AWS::DMS::Endpoint.GcpMySQLSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`

- [AWS::Glue::Crawler.MongoDBTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-crawler-mongodbtarget.html)
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

- [AWS::IoTSiteWise::Gateway.GreengrassV2](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-greengrassv2.html)
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::SSM::MaintenanceWindowTask.CloudWatchOutputConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig.html)
  - `ap-northeast-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::CloudFront::ResponseHeadersPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-responseheaderspolicy.html)
  - `cn-northwest-1`

- [AWS::EMR::Studio](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html)
  - `us-west-1`

- [AWS::Panorama::ApplicationInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html)
  - `ap-southeast-2`
  - `ap-southeast-1`

- [AWS::Panorama::Package](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-package.html)
  - `ap-southeast-2`
  - `ap-southeast-1`

- [AWS::Panorama::PackageVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html)
  - `ap-southeast-2`
  - `ap-southeast-1`

- [AWS::RDS::DBProxy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxy.html)
  - `eu-south-1`
  - `sa-east-1`
  - `eu-north-1`
  - `ap-northeast-3`
  - `ap-east-1`
  - `me-south-1`
  - `eu-west-3`
  - `af-south-1`

- [AWS::RDS::DBProxyEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxyendpoint.html)
  - `eu-south-1`
  - `sa-east-1`
  - `eu-north-1`
  - `ap-northeast-3`
  - `ap-east-1`
  - `me-south-1`
  - `eu-west-3`
  - `af-south-1`

- [AWS::RDS::DBProxyTargetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxytargetgroup.html)
  - `eu-south-1`
  - `sa-east-1`
  - `eu-north-1`
  - `ap-northeast-3`
  - `ap-east-1`
  - `me-south-1`
  - `eu-west-3`
  - `af-south-1`

- [AWS::SES::ConfigurationSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html)
  - `ap-northeast-2`

- [AWS::Backup::BackupVault.LockConfigurationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html)
  - Now available to **ALL** regions.

- [AWS::CloudFront::ResponseHeadersPolicy.AccessControlAllowHeaders](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowheaders.html)
  - `cn-northwest-1`

- [AWS::CloudFront::ResponseHeadersPolicy.AccessControlAllowMethods](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolallowmethods.html)
  - `cn-northwest-1`

- [AWS::CloudFront::ResponseHeadersPolicy.AccessControlAllowOrigins](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolalloworigins.html)
  - `cn-northwest-1`

- [AWS::CloudFront::ResponseHeadersPolicy.AccessControlExposeHeaders](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-accesscontrolexposeheaders.html)
  - `cn-northwest-1`

- [AWS::CloudFront::ResponseHeadersPolicy.ContentSecurityPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-contentsecuritypolicy.html)
  - `cn-northwest-1`

- [AWS::CloudFront::ResponseHeadersPolicy.ContentTypeOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-contenttypeoptions.html)
  - `cn-northwest-1`

- [AWS::CloudFront::ResponseHeadersPolicy.CorsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-corsconfig.html)
  - `cn-northwest-1`

- [AWS::CloudFront::ResponseHeadersPolicy.CustomHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheader.html)
  - `cn-northwest-1`

- [AWS::CloudFront::ResponseHeadersPolicy.CustomHeadersConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-customheadersconfig.html)
  - `cn-northwest-1`

- [AWS::CloudFront::ResponseHeadersPolicy.FrameOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-frameoptions.html)
  - `cn-northwest-1`

- [AWS::CloudFront::ResponseHeadersPolicy.ReferrerPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-referrerpolicy.html)
  - `cn-northwest-1`

- [AWS::CloudFront::ResponseHeadersPolicy.ResponseHeadersPolicyConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-responseheaderspolicyconfig.html)
  - `cn-northwest-1`

- [AWS::CloudFront::ResponseHeadersPolicy.SecurityHeadersConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-securityheadersconfig.html)
  - `cn-northwest-1`

- [AWS::CloudFront::ResponseHeadersPolicy.StrictTransportSecurity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-stricttransportsecurity.html)
  - `cn-northwest-1`

- [AWS::CloudFront::ResponseHeadersPolicy.XSSProtection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-xssprotection.html)
  - `cn-northwest-1`

- [AWS::EC2::ClientVpnEndpoint.ClientLoginBannerOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientloginbanneroptions.html)
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-northeast-1`
  - `us-west-1`
  - `us-west-2`
  - `us-gov-east-1`
  - `eu-west-2`
  - `eu-central-1`
  - `af-south-1`
  - `eu-west-1`
  - `us-gov-west-1`
  - `ap-southeast-1`
  - `us-east-2`
  - `eu-south-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-east-1`
  - `eu-west-3`

- [AWS::Panorama::ApplicationInstance.ManifestOverridesPayload](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-applicationinstance-manifestoverridespayload.html)
  - `ap-southeast-2`
  - `ap-southeast-1`

- [AWS::Panorama::ApplicationInstance.ManifestPayload](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-applicationinstance-manifestpayload.html)
  - `ap-southeast-2`
  - `ap-southeast-1`

- [AWS::RDS::DBProxy.AuthFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxy-authformat.html)
  - `eu-south-1`
  - `sa-east-1`
  - `eu-north-1`
  - `ap-northeast-3`
  - `ap-east-1`
  - `me-south-1`
  - `eu-west-3`
  - `af-south-1`

- [AWS::RDS::DBProxy.TagFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxy-tagformat.html)
  - `eu-south-1`
  - `sa-east-1`
  - `eu-north-1`
  - `ap-northeast-3`
  - `ap-east-1`
  - `me-south-1`
  - `eu-west-3`
  - `af-south-1`

- [AWS::RDS::DBProxyEndpoint.TagFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxyendpoint-tagformat.html)
  - `eu-south-1`
  - `sa-east-1`
  - `eu-north-1`
  - `ap-northeast-3`
  - `ap-east-1`
  - `me-south-1`
  - `eu-west-3`
  - `af-south-1`

- [AWS::RDS::DBProxyTargetGroup.ConnectionPoolConfigurationInfoFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbproxytargetgroup-connectionpoolconfigurationinfoformat.html)
  - `eu-south-1`
  - `sa-east-1`
  - `eu-north-1`
  - `ap-northeast-3`
  - `ap-east-1`
  - `me-south-1`
  - `eu-west-3`
  - `af-south-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v52.0.0: [AWS::CloudFormation::HookDefaultVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookdefaultversion.html)
    - `eu-central-1`

  - Since v52.0.0: [AWS::CloudFormation::HookTypeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hooktypeconfig.html)
    - `eu-central-1`

  - Since v52.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v52.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v52.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v52.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v52.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v52.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- PropertyType Still Missing
  - Since v52.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v52.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v52.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v52.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::ApplicationInsights::Application.HAClusterPrometheusExporter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-haclusterprometheusexporter.html)
    - `cn-north-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::ApplicationInsights::Application.HANAPrometheusExporter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-hanaprometheusexporter.html)
    - `cn-north-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::DMS::Endpoint.GcpMySQLSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html)
    - `ap-northeast-2`
    - `ap-southeast-2`
    - `ca-central-1`
    - `eu-central-1`

  - [AWS::SSM::MaintenanceWindowTask.CloudWatchOutputConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig.html)
    - `ap-northeast-1`
    - `us-west-2`
