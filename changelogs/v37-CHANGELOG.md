# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v37-changelog.json`](changelogs/v37-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [37.1.0](#3710-2021-05-28)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)
- [37.0.0](#3700-2021-05-21)
  - [Totals](#totals-1)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-1)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-1)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-1)

## [37.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v37.1.0) (2021-05-28)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v37-changelog.json)
  - Change source is a diff between [v37.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v37.1.0) and [v37.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v37.0.0)

### Totals

- TotalPropertyTypes: 2468 **(+1)**
- TotalPropertyTypesSupportedGlobally: 666 **(+9)**
- TotalResourceTypes: 761 **(+1)**
- TotalResourceTypesSupportedGlobally: 221 **(+2)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::CUR::ReportDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html)
  - `cn-northwest-1`
  - `us-east-1`

- [AWS::FraudDetector::Detector.Model](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-model.html)
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::CloudFormation::StackSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html)
  - Now available to **ALL** regions.

- [AWS::Config::ConfigurationAggregator](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html)
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`

- [AWS::LicenseManager::Grant](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::LicenseManager::License](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::NetworkManager::CustomerGatewayAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::NetworkManager::Device](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::NetworkManager::GlobalNetwork](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::NetworkManager::Link](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::NetworkManager::LinkAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::NetworkManager::Site](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::NetworkManager::TransitGatewayRegistration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::ServiceCatalogAppRegistry::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-application.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::ServiceCatalogAppRegistry::AttributeGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-attributegroup.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-attributegroupassociation.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::ServiceCatalogAppRegistry::ResourceAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalogappregistry-resourceassociation.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::Synthetics::Canary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html)
  - Now available to **ALL** regions.

- [AWS::CloudFormation::StackSet.AutoDeployment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-autodeployment.html)
  - Now available to **ALL** regions.

- [AWS::CloudFormation::StackSet.DeploymentTargets](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-deploymenttargets.html)
  - Now available to **ALL** regions.

- [AWS::CloudFormation::StackSet.OperationPreferences](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html)
  - Now available to **ALL** regions.

- [AWS::CloudFormation::StackSet.Parameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-parameter.html)
  - Now available to **ALL** regions.

- [AWS::CloudFormation::StackSet.StackInstances](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-stackinstances.html)
  - Now available to **ALL** regions.

- [AWS::Config::ConfigurationAggregator.AccountAggregationSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html)
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`

- [AWS::Config::ConfigurationAggregator.OrganizationAggregationSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html)
  - `ca-central-1`
  - `ap-south-1`
  - `sa-east-1`

- [AWS::ECR::Repository.EncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-encryptionconfiguration.html)
  - `ap-northeast-1`
  - `us-gov-east-1`
  - `eu-west-2`
  - `cn-north-1`
  - `ap-northeast-2`
  - `eu-north-1`
  - `eu-west-3`
  - `eu-west-1`
  - `us-gov-west-1`
  - `ap-northeast-3`
  - `us-east-2`
  - `eu-south-1`
  - `us-west-1`
  - `sa-east-1`
  - `me-south-1`
  - `us-west-2`
  - `ap-southeast-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-east-1`
  - `af-south-1`
  - `ap-southeast-2`
  - `ap-south-1`

- [AWS::ECR::Repository.ImageScanningConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-imagescanningconfiguration.html)
  - `ap-northeast-1`
  - `us-gov-east-1`
  - `eu-west-2`
  - `cn-north-1`
  - `ap-northeast-2`
  - `eu-north-1`
  - `eu-west-3`
  - `eu-west-1`
  - `us-gov-west-1`
  - `ap-northeast-3`
  - `us-east-2`
  - `eu-south-1`
  - `us-west-1`
  - `sa-east-1`
  - `me-south-1`
  - `us-west-2`
  - `ap-southeast-1`
  - `us-east-1`
  - `ca-central-1`
  - `ap-east-1`
  - `af-south-1`
  - `ap-southeast-2`
  - `ap-south-1`

- [AWS::LicenseManager::License.BorrowConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-borrowconfiguration.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::LicenseManager::License.ConsumptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-consumptionconfiguration.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::LicenseManager::License.Entitlement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::LicenseManager::License.IssuerData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-issuerdata.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::LicenseManager::License.Metadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-metadata.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::LicenseManager::License.ProvisionalConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-provisionalconfiguration.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::LicenseManager::License.ValidityDateFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-validitydateformat.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::NetworkManager::Device.Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::NetworkManager::Link.Bandwidth](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::NetworkManager::Site.Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html)
  - `us-gov-west-1`
  - `us-gov-east-1`

- [AWS::Synthetics::Canary.Code](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html)
  - Now available to **ALL** regions.

- [AWS::Synthetics::Canary.RunConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html)
  - Now available to **ALL** regions.

- [AWS::Synthetics::Canary.Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-schedule.html)
  - Now available to **ALL** regions.

- [AWS::Synthetics::Canary.VPCConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html)
  - Now available to **ALL** regions.

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v37.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v37.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

## [37.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v37.0.0) (2021-05-21)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v37-changelog.json)
  - Change source is a diff between [v37.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v37.0.0) and [v36.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v36.0.0)

### Totals

- TotalPropertyTypes: 2467 **(+14)**
- TotalPropertyTypesSupportedGlobally: 657 **(+0)**
- TotalResourceTypes: 760 **(+3)**
- TotalResourceTypesSupportedGlobally: 219 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::AppRunner::Service](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::EC2::TransitGatewayPeeringAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaypeeringattachment.html)
  - `af-south-1`
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
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::IoTCoreDeviceAdvisor::SuiteDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppRunner::Service.AuthenticationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::AppRunner::Service.CodeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::AppRunner::Service.CodeConfigurationValues](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::AppRunner::Service.CodeRepository](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::AppRunner::Service.EncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-encryptionconfiguration.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::AppRunner::Service.HealthCheckConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::AppRunner::Service.ImageConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::AppRunner::Service.ImageRepository](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::AppRunner::Service.InstanceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::AppRunner::Service.KeyValuePair](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::AppRunner::Service.SourceCodeVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::AppRunner::Service.SourceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html)
  - `ap-northeast-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::ECR::Repository.EncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-encryptionconfiguration.html)
  - `eu-central-1`

- [AWS::ECR::Repository.ImageScanningConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-imagescanningconfiguration.html)
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::DataBrew::Dataset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Job](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Recipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::EC2::TransitGatewayAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html)
  - `ap-northeast-3`

- [AWS::Route53Resolver::ResolverEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html)
  - `ap-northeast-3`

- [AWS::Route53Resolver::ResolverRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html)
  - `ap-northeast-3`

- [AWS::Route53Resolver::ResolverRuleAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html)
  - `ap-northeast-3`

- [AWS::AppFlow::Flow.ZendeskDestinationProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-zendeskdestinationproperties.html)
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `eu-west-2`
  - `eu-central-1`
  - `eu-west-1`
  - `ca-central-1`
  - `sa-east-1`
  - `us-west-1`
  - `us-west-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `us-east-2`
  - `eu-west-3`

- [AWS::DataBrew::Dataset.CsvOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-csvoptions.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Dataset.DataCatalogInputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datacataloginputdefinition.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Dataset.DatabaseInputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-databaseinputdefinition.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Dataset.DatasetParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datasetparameter.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Dataset.DatetimeOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datetimeoptions.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Dataset.ExcelOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-exceloptions.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Dataset.FilesLimit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-fileslimit.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Dataset.FilterExpression](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filterexpression.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Dataset.FilterValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filtervalue.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Dataset.FormatOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-formatoptions.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Dataset.Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-input.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Dataset.JsonOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-jsonoptions.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Dataset.PathOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathoptions.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Dataset.PathParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathparameter.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Dataset.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-s3location.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Job.CsvOutputOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-csvoutputoptions.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Job.JobSample](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-jobsample.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Job.Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Job.OutputFormatOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputformatoptions.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Job.OutputLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputlocation.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Job.Recipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-recipe.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Job.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3location.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Project.Sample](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-project-sample.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Recipe.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-action.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Recipe.ConditionExpression](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-conditionexpression.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Recipe.DataCatalogInputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-datacataloginputdefinition.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Recipe.RecipeParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Recipe.RecipeStep](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipestep.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Recipe.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-s3location.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::DataBrew::Recipe.SecondaryInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-secondaryinput.html)
  - `cn-north-1`
  - `cn-northwest-1`

- [AWS::MediaPackage::Channel.LogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-logconfiguration.html)
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `eu-north-1`
  - `eu-west-2`
  - `us-east-1`
  - `ap-southeast-2`
  - `eu-west-1`
  - `sa-east-1`
  - `us-west-1`
  - `us-west-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `eu-west-3`

- [AWS::MediaPackage::PackagingGroup.LogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-logconfiguration.html)
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `eu-north-1`
  - `eu-west-2`
  - `us-east-1`
  - `ap-southeast-2`
  - `eu-west-1`
  - `sa-east-1`
  - `us-west-1`
  - `us-west-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `eu-west-3`

- [AWS::Route53Resolver::ResolverEndpoint.IpAddressRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html)
  - `ap-northeast-3`

- [AWS::Route53Resolver::ResolverRule.TargetAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html)
  - `ap-northeast-3`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v36.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v36.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::ECR::Repository.EncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-encryptionconfiguration.html)
    - `eu-central-1`

  - [AWS::ECR::Repository.ImageScanningConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-imagescanningconfiguration.html)
    - `eu-central-1`

