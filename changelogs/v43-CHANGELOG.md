# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v43-changelog.json`](changelogs/v43-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [43.1.0](#4310-2021-10-09)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)
- [43.0.0](#4300-2021-10-01)
  - [Totals](#totals-1)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-1)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-1)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-1)

## [43.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v43.1.0) (2021-10-09)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v43-changelog.json)
  - Change source is a diff between [v43.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v43.1.0) and [v43.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v43.0.0)

### Totals

- TotalPropertyTypes: 2642 **(+-1)**
- TotalPropertyTypesSupportedGlobally: 947 **(+11)**
- TotalResourceTypes: 803 **(+1)**
- TotalResourceTypesSupportedGlobally: 326 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::IoT::JobTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html)
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-north-1`
  - `cn-northwest-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::Synthetics::Canary.ArtifactConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-artifactconfig.html)
  - Available in **ALL** regions.

- [AWS::Synthetics::Canary.S3Encryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-s3encryption.html)
  - Available in **ALL** regions.

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::EKS::Cluster.ClusterLogging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-clusterlogging.html)
  - `sa-east-1`

- [AWS::EKS::Cluster.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-logging.html)
  - `sa-east-1`

- [AWS::EKS::Cluster.LoggingTypeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-loggingtypeconfig.html)
  - `sa-east-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Backup::Framework](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html)
  - `us-east-2`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `sa-east-1`

- [AWS::Backup::ReportPlan](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html)
  - `us-east-2`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `sa-east-1`

- [AWS::IoTSiteWise::AccessPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::Asset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::AssetModel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::Dashboard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::Gateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::Portal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::Backup::BackupVault.LockConfigurationType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html)
  - `af-south-1`
  - `ap-northeast-3`
  - `eu-south-1`

- [AWS::Backup::Framework.ControlInputParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlinputparameter.html)
  - `us-east-2`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `sa-east-1`

- [AWS::Backup::Framework.FrameworkControl](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html)
  - `us-east-2`
  - `ap-northeast-2`
  - `ap-east-1`
  - `eu-west-3`
  - `us-west-1`
  - `me-south-1`
  - `sa-east-1`

- [AWS::EC2::LaunchTemplate.AcceleratorCount](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-acceleratorcount.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.AcceleratorTotalMemoryMiB](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-acceleratortotalmemorymib.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.BaselineEbsBandwidthMbps](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-baselineebsbandwidthmbps.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.MemoryGiBPerVCpu](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-memorygibpervcpu.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.MemoryMiB](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-memorymib.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.NetworkInterfaceCount](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterfacecount.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.TotalLocalStorageGB](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-totallocalstoragegb.html)
  - Now available to **ALL** regions.

- [AWS::EC2::LaunchTemplate.VCpuCount](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-vcpucount.html)
  - Now available to **ALL** regions.

- [AWS::EKS::Cluster.Provider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-provider.html)
  - Now available to **ALL** regions.

- [AWS::IoTSiteWise::AccessPolicy.AccessPolicyIdentity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyidentity.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::AccessPolicy.AccessPolicyResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyresource.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::AccessPolicy.IamRole](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-iamrole.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::AccessPolicy.IamUser](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-iamuser.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::AccessPolicy.Portal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-portal.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::AccessPolicy.Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-project.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::AccessPolicy.User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-user.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::Asset.AssetHierarchy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assethierarchy.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::Asset.AssetProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assetproperty.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::AssetModel.AssetModelCompositeModel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::AssetModel.AssetModelHierarchy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelhierarchy.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::AssetModel.AssetModelProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::AssetModel.Attribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-attribute.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::AssetModel.ExpressionVariable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-expressionvariable.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::AssetModel.Metric](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metric.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::AssetModel.MetricWindow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metricwindow.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::AssetModel.PropertyType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertytype.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::AssetModel.Transform](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-transform.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::AssetModel.TumblingWindow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-tumblingwindow.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::AssetModel.VariableValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-variablevalue.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::Gateway.GatewayCapabilitySummary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewaycapabilitysummary.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::Gateway.GatewayPlatform](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewayplatform.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

- [AWS::IoTSiteWise::Gateway.Greengrass](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-greengrass.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v43.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v43.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v43.0.0: [AWS::SageMaker::DataQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v43.0.0: [AWS::SageMaker::ModelBiasJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-environment.html)
    - `eu-west-3`

  - Since v43.0.0: [AWS::SageMaker::ModelExplainabilityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v43.0.0: [AWS::SageMaker::ModelQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v43.0.0: [AWS::SageMaker::MonitoringSchedule.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-environment.html)
    - `cn-northwest-1`
    - `eu-west-3`

## [43.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v43.0.0) (2021-10-01)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v43-changelog.json)
  - Change source is a diff between [v43.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v43.0.0) and [v42.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v42.0.0)

### Totals

- TotalPropertyTypes: 2630 **(+15)**
- TotalPropertyTypesSupportedGlobally: 936 **(+-1)**
- TotalResourceTypes: 798 **(+1)**
- TotalResourceTypesSupportedGlobally: 326 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::APS::RuleGroupsNamespace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::EC2::LaunchTemplate.AcceleratorCount](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-acceleratorcount.html)
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::EC2::LaunchTemplate.AcceleratorTotalMemoryMiB](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-acceleratortotalmemorymib.html)
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::EC2::LaunchTemplate.BaselineEbsBandwidthMbps](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-baselineebsbandwidthmbps.html)
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::EC2::LaunchTemplate.MemoryGiBPerVCpu](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-memorygibpervcpu.html)
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::EC2::LaunchTemplate.MemoryMiB](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-memorymib.html)
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::EC2::LaunchTemplate.NetworkInterfaceCount](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterfacecount.html)
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::EC2::LaunchTemplate.TotalLocalStorageGB](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-totallocalstoragegb.html)
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::EC2::LaunchTemplate.VCpuCount](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-vcpucount.html)
  - `ap-northeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::ECR::ReplicationConfiguration.RepositoryFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-replicationconfiguration-repositoryfilter.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
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

- [AWS::EKS::Cluster.ClusterLogging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-clusterlogging.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::EKS::Cluster.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-logging.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::EKS::Cluster.LoggingTypeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-loggingtypeconfig.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::KinesisFirehose::DeliveryStream.AmazonopensearchserviceBufferingHints](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-north-1`
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
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::KinesisFirehose::DeliveryStream.AmazonopensearchserviceDestinationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-north-1`
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
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::KinesisFirehose::DeliveryStream.AmazonopensearchserviceRetryOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserviceretryoptions.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-north-1`
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
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::APS::Workspace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html)
  - `ap-northeast-1`
  - `eu-north-1`
  - `ap-southeast-1`
  - `ap-southeast-2`

- [AWS::DataBrew::Dataset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html)
  - `af-south-1`

- [AWS::DataBrew::Job](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html)
  - `af-south-1`

- [AWS::DataBrew::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html)
  - `af-south-1`

- [AWS::DataBrew::Recipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html)
  - `af-south-1`

- [AWS::DataBrew::Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html)
  - `af-south-1`

- [AWS::IoTEvents::DetectorModel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AccessPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::Asset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AssetModel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::Dashboard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::Gateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::Portal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html)
  - `us-gov-west-1`

- [AWS::MWAA::Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html)
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-south-1`
  - `ca-central-1`

- [AWS::DataBrew::Dataset.CsvOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-csvoptions.html)
  - `af-south-1`

- [AWS::DataBrew::Dataset.DataCatalogInputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datacataloginputdefinition.html)
  - `af-south-1`

- [AWS::DataBrew::Dataset.DatabaseInputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-databaseinputdefinition.html)
  - `af-south-1`

- [AWS::DataBrew::Dataset.DatasetParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datasetparameter.html)
  - `af-south-1`

- [AWS::DataBrew::Dataset.DatetimeOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datetimeoptions.html)
  - `af-south-1`

- [AWS::DataBrew::Dataset.ExcelOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-exceloptions.html)
  - `af-south-1`

- [AWS::DataBrew::Dataset.FilesLimit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-fileslimit.html)
  - `af-south-1`

- [AWS::DataBrew::Dataset.FilterExpression](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filterexpression.html)
  - `af-south-1`

- [AWS::DataBrew::Dataset.FilterValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filtervalue.html)
  - `af-south-1`

- [AWS::DataBrew::Dataset.FormatOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-formatoptions.html)
  - `af-south-1`

- [AWS::DataBrew::Dataset.Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-input.html)
  - `af-south-1`

- [AWS::DataBrew::Dataset.JsonOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-jsonoptions.html)
  - `af-south-1`

- [AWS::DataBrew::Dataset.PathOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathoptions.html)
  - `af-south-1`

- [AWS::DataBrew::Dataset.PathParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathparameter.html)
  - `af-south-1`

- [AWS::DataBrew::Dataset.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-s3location.html)
  - `af-south-1`

- [AWS::DataBrew::Job.ColumnSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-columnselector.html)
  - `af-south-1`

- [AWS::DataBrew::Job.ColumnStatisticsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-columnstatisticsconfiguration.html)
  - `af-south-1`

- [AWS::DataBrew::Job.CsvOutputOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-csvoutputoptions.html)
  - `af-south-1`

- [AWS::DataBrew::Job.DataCatalogOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html)
  - `af-south-1`

- [AWS::DataBrew::Job.DatabaseOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databaseoutput.html)
  - `af-south-1`

- [AWS::DataBrew::Job.DatabaseTableOutputOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databasetableoutputoptions.html)
  - `af-south-1`

- [AWS::DataBrew::Job.JobSample](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-jobsample.html)
  - `af-south-1`

- [AWS::DataBrew::Job.Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html)
  - `af-south-1`

- [AWS::DataBrew::Job.OutputFormatOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputformatoptions.html)
  - `af-south-1`

- [AWS::DataBrew::Job.OutputLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputlocation.html)
  - `af-south-1`

- [AWS::DataBrew::Job.ParameterMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-parametermap.html)
  - `af-south-1`

- [AWS::DataBrew::Job.ProfileConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-profileconfiguration.html)
  - `af-south-1`

- [AWS::DataBrew::Job.Recipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-recipe.html)
  - `af-south-1`

- [AWS::DataBrew::Job.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3location.html)
  - `af-south-1`

- [AWS::DataBrew::Job.S3TableOutputOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3tableoutputoptions.html)
  - `af-south-1`

- [AWS::DataBrew::Job.StatisticOverride](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticoverride.html)
  - `af-south-1`

- [AWS::DataBrew::Job.StatisticsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticsconfiguration.html)
  - `af-south-1`

- [AWS::DataBrew::Project.Sample](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-project-sample.html)
  - `af-south-1`

- [AWS::DataBrew::Recipe.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-action.html)
  - `af-south-1`

- [AWS::DataBrew::Recipe.ConditionExpression](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-conditionexpression.html)
  - `af-south-1`

- [AWS::DataBrew::Recipe.DataCatalogInputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-datacataloginputdefinition.html)
  - `af-south-1`

- [AWS::DataBrew::Recipe.ParameterMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-parametermap.html)
  - `af-south-1`

- [AWS::DataBrew::Recipe.RecipeParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html)
  - `af-south-1`

- [AWS::DataBrew::Recipe.RecipeStep](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipestep.html)
  - `af-south-1`

- [AWS::DataBrew::Recipe.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-s3location.html)
  - `af-south-1`

- [AWS::DataBrew::Recipe.SecondaryInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-secondaryinput.html)
  - `af-south-1`

- [AWS::IoTEvents::DetectorModel.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.AssetPropertyTimestamp](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertytimestamp.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.AssetPropertyValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvalue.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.AssetPropertyVariant](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.ClearTimer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-cleartimer.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.DetectorModelDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-detectormodeldefinition.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.DynamoDB](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.DynamoDBv2](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodbv2.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.Event](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-event.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.Firehose](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-firehose.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.IotEvents](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotevents.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.IotSiteWise](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.IotTopicPublish](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iottopicpublish.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.Lambda](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-lambda.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.OnEnter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onenter.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.OnExit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onexit.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.OnInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-oninput.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.Payload](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-payload.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.ResetTimer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-resettimer.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.SetTimer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-settimer.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.SetVariable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-setvariable.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.Sns](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sns.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.Sqs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sqs.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.State](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::DetectorModel.TransitionEvent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::Input.Attribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-attribute.html)
  - `us-gov-west-1`

- [AWS::IoTEvents::Input.InputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-inputdefinition.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AccessPolicy.AccessPolicyIdentity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyidentity.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AccessPolicy.AccessPolicyResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyresource.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AccessPolicy.IamRole](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-iamrole.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AccessPolicy.IamUser](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-iamuser.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AccessPolicy.Portal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-portal.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AccessPolicy.Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-project.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AccessPolicy.User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-user.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::Asset.AssetHierarchy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assethierarchy.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::Asset.AssetProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assetproperty.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AssetModel.AssetModelCompositeModel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AssetModel.AssetModelHierarchy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelhierarchy.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AssetModel.AssetModelProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AssetModel.Attribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-attribute.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AssetModel.ExpressionVariable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-expressionvariable.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AssetModel.Metric](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metric.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AssetModel.MetricWindow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metricwindow.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AssetModel.PropertyType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertytype.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AssetModel.Transform](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-transform.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AssetModel.TumblingWindow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-tumblingwindow.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::AssetModel.VariableValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-variablevalue.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::Gateway.GatewayCapabilitySummary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewaycapabilitysummary.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::Gateway.GatewayPlatform](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewayplatform.html)
  - `us-gov-west-1`

- [AWS::IoTSiteWise::Gateway.Greengrass](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-greengrass.html)
  - `us-gov-west-1`

- [AWS::Kendra::DataSource.ProxyConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-proxyconfiguration.html)
  - `eu-west-1`
  - `us-west-2`
  - `us-east-1`
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.WebCrawlerAuthenticationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerauthenticationconfiguration.html)
  - `eu-west-1`
  - `us-west-2`
  - `us-east-1`
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.WebCrawlerBasicAuthentication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerbasicauthentication.html)
  - `eu-west-1`
  - `us-west-2`
  - `us-east-1`
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.WebCrawlerConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html)
  - `eu-west-1`
  - `us-west-2`
  - `us-east-1`
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.WebCrawlerSeedUrlConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerseedurlconfiguration.html)
  - `eu-west-1`
  - `us-west-2`
  - `us-east-1`
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.WebCrawlerSiteMapsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlersitemapsconfiguration.html)
  - `eu-west-1`
  - `us-west-2`
  - `us-east-1`
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.WebCrawlerUrls](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerurls.html)
  - `eu-west-1`
  - `us-west-2`
  - `us-east-1`
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.WorkDocsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html)
  - `eu-west-1`
  - `us-west-2`
  - `us-east-1`
  - `ap-southeast-2`

- [AWS::MWAA::Environment.LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html)
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-south-1`
  - `ca-central-1`

- [AWS::MWAA::Environment.ModuleLoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html)
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-south-1`
  - `ca-central-1`

- [AWS::MWAA::Environment.NetworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-networkconfiguration.html)
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-south-1`
  - `ca-central-1`

- [AWS::MWAA::Environment.TagMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-tagmap.html)
  - `ap-northeast-2`
  - `eu-west-3`
  - `eu-west-2`
  - `sa-east-1`
  - `ap-south-1`
  - `ca-central-1`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::EKS::Cluster.Provider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-provider.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `cn-north-1`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `sa-east-1`
  - `us-west-2`
  - `us-east-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v42.0.0: [AWS::EKS::Cluster.Provider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-provider.html)
    - `af-south-1`
    - `ap-east-1`
    - `ap-northeast-3`
    - `ap-south-1`
    - `ca-central-1`
    - `cn-northwest-1`
    - `eu-north-1`
    - `eu-south-1`
    - `eu-west-2`
    - `eu-west-3`
    - `me-south-1`
    - `us-east-2`
    - `us-gov-east-1`
    - `us-gov-west-1`
    - `us-west-1`

  - Since v42.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v42.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v42.0.0: [AWS::SageMaker::DataQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v42.0.0: [AWS::SageMaker::ModelBiasJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-environment.html)
    - `eu-west-3`

  - Since v42.0.0: [AWS::SageMaker::ModelExplainabilityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v42.0.0: [AWS::SageMaker::ModelQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-environment.html)
    - `eu-west-3`

  - Since v42.0.0: [AWS::SageMaker::MonitoringSchedule.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-environment.html)
    - `cn-northwest-1`
    - `eu-west-3`

