# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v40-changelog.json`](changelogs/v40-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [40.1.0](#4010-2021-08-27)
  - [Totals](#totals)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)
- [40.0.0](#4000-2021-08-20)
  - [Totals](#totals-1)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-1)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-1)

## [40.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v40.1.0) (2021-08-27)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v40-changelog.json)
  - Change source is a diff between [v40.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v40.1.0) and [v40.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v40.0.0)

### Totals

- TotalPropertyTypes: 2575 **(+0)**
- TotalPropertyTypesSupportedGlobally: 916 **(+5)**
- TotalResourceTypes: 784 **(+0)**
- TotalResourceTypesSupportedGlobally: 325 **(+3)**

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Athena::DataCatalog](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html)
  - Now available to **ALL** regions.

- [AWS::Athena::NamedQuery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html)
  - Now available to **ALL** regions.

- [AWS::Athena::WorkGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html)
  - Now available to **ALL** regions.

- [AWS::DataBrew::Dataset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-dataset.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Job](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-job.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-project.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Recipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-recipe.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Schedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-databrew-schedule.html)
  - `us-gov-west-1`

- [AWS::SageMaker::CodeRepository](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html)
  - `ap-northeast-3`

- [AWS::SageMaker::Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html)
  - `ap-northeast-3`

- [AWS::SageMaker::EndpointConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::Model](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html)
  - `ap-northeast-3`

- [AWS::SageMaker::NotebookInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html)
  - `ap-northeast-3`

- [AWS::SageMaker::NotebookInstanceLifecycleConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html)
  - `ap-northeast-3`

- [AWS::Athena::WorkGroup.EncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::Athena::WorkGroup.EngineVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-engineversion.html)
  - `ap-northeast-3`

- [AWS::Athena::WorkGroup.ResultConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::Athena::WorkGroup.ResultConfigurationUpdates](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html)
  - Now available to **ALL** regions.

- [AWS::Athena::WorkGroup.WorkGroupConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::Athena::WorkGroup.WorkGroupConfigurationUpdates](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html)
  - Now available to **ALL** regions.

- [AWS::DataBrew::Dataset.CsvOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-csvoptions.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Dataset.DataCatalogInputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datacataloginputdefinition.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Dataset.DatabaseInputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-databaseinputdefinition.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Dataset.DatasetParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datasetparameter.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Dataset.DatetimeOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-datetimeoptions.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Dataset.ExcelOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-exceloptions.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Dataset.FilesLimit](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-fileslimit.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Dataset.FilterExpression](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filterexpression.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Dataset.FilterValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-filtervalue.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Dataset.FormatOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-formatoptions.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Dataset.Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-input.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Dataset.JsonOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-jsonoptions.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Dataset.PathOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathoptions.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Dataset.PathParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-pathparameter.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Dataset.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-dataset-s3location.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Job.ColumnSelector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-columnselector.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Job.ColumnStatisticsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-columnstatisticsconfiguration.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Job.CsvOutputOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-csvoutputoptions.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Job.DataCatalogOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-datacatalogoutput.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Job.DatabaseOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databaseoutput.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Job.DatabaseTableOutputOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-databasetableoutputoptions.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Job.JobSample](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-jobsample.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Job.Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-output.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Job.OutputFormatOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputformatoptions.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Job.OutputLocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-outputlocation.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Job.ParameterMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-parametermap.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Job.ProfileConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-profileconfiguration.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Job.Recipe](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-recipe.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Job.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3location.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Job.S3TableOutputOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-s3tableoutputoptions.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Job.StatisticOverride](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticoverride.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Job.StatisticsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-job-statisticsconfiguration.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Project.Sample](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-project-sample.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Recipe.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-action.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Recipe.ConditionExpression](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-conditionexpression.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Recipe.DataCatalogInputDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-datacataloginputdefinition.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Recipe.ParameterMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-parametermap.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Recipe.RecipeParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipeparameters.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Recipe.RecipeStep](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-recipestep.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Recipe.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-s3location.html)
  - `us-gov-west-1`

- [AWS::DataBrew::Recipe.SecondaryInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-secondaryinput.html)
  - `us-gov-west-1`

- [AWS::SageMaker::CodeRepository.GitConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::Endpoint.Alarm](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-alarm.html)
  - `ap-northeast-3`

- [AWS::SageMaker::Endpoint.AutoRollbackConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-autorollbackconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::Endpoint.BlueGreenUpdatePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.html)
  - `ap-northeast-3`

- [AWS::SageMaker::Endpoint.CapacitySize](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-capacitysize.html)
  - `ap-northeast-3`

- [AWS::SageMaker::Endpoint.DeploymentConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-deploymentconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::Endpoint.TrafficRoutingConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::Endpoint.VariantProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-variantproperty.html)
  - `ap-northeast-3`

- [AWS::SageMaker::EndpointConfig.AsyncInferenceClientConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceclientconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::EndpointConfig.AsyncInferenceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::EndpointConfig.AsyncInferenceNotificationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferencenotificationconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::EndpointConfig.AsyncInferenceOutputConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceoutputconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::EndpointConfig.CaptureContentTypeHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html)
  - `ap-northeast-3`

- [AWS::SageMaker::EndpointConfig.CaptureOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-captureoption.html)
  - `ap-northeast-3`

- [AWS::SageMaker::EndpointConfig.DataCaptureConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::EndpointConfig.ProductionVariant](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html)
  - `ap-northeast-3`

- [AWS::SageMaker::Model.ContainerDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html)
  - `ap-northeast-3`

- [AWS::SageMaker::Model.ImageConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::Model.InferenceExecutionConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-inferenceexecutionconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::Model.MultiModelConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-multimodelconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::Model.RepositoryAuthConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig-repositoryauthconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::Model.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-vpcconfig.html)
  - `ap-northeast-3`

- [AWS::SageMaker::NotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHook](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook.html)
  - `ap-northeast-3`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::SageMaker::DataQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-environment.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelBiasJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-environment.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-environment.html)
  - `eu-central-1`

- [AWS::SageMaker::ModelQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-environment.html)
  - `eu-central-1`

- [AWS::SageMaker::MonitoringSchedule.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-environment.html)
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v40.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v40.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

## [40.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v40.0.0) (2021-08-20)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v40-changelog.json)
  - Change source is a diff between [v40.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v40.0.0) and [v39.10.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.10.0)

### Totals

- TotalPropertyTypes: 2575 **(+9)**
- TotalPropertyTypesSupportedGlobally: 911 **(+5)**
- TotalResourceTypes: 784 **(+0)**
- TotalResourceTypesSupportedGlobally: 322 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::AutoScaling::ScalingPolicy.PredictiveScalingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingconfiguration.html)
  - Available in **ALL** regions.

- [AWS::AutoScaling::ScalingPolicy.PredictiveScalingMetricSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingmetricspecification.html)
  - Available in **ALL** regions.

- [AWS::AutoScaling::ScalingPolicy.PredictiveScalingPredefinedLoadMetric](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingpredefinedloadmetric.html)
  - Available in **ALL** regions.

- [AWS::AutoScaling::ScalingPolicy.PredictiveScalingPredefinedMetricPair](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingpredefinedmetricpair.html)
  - Available in **ALL** regions.

- [AWS::AutoScaling::ScalingPolicy.PredictiveScalingPredefinedScalingMetric](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingpredefinedscalingmetric.html)
  - Available in **ALL** regions.

- [AWS::SageMaker::EndpointConfig.AsyncInferenceClientConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceclientconfig.html)
  - `af-south-1`
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::SageMaker::EndpointConfig.AsyncInferenceConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceconfig.html)
  - `af-south-1`
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::SageMaker::EndpointConfig.AsyncInferenceNotificationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferencenotificationconfig.html)
  - `af-south-1`
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::SageMaker::EndpointConfig.AsyncInferenceOutputConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-asyncinferenceoutputconfig.html)
  - `af-south-1`
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
  - `eu-south-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Cloud9::EnvironmentEC2](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html)
  - `ap-northeast-3`

- [AWS::Cloud9::EnvironmentEC2.Repository](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloud9-environmentec2-repository.html)
  - `ap-northeast-3`

- [AWS::Redshift::Cluster.Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-endpoint.html)
  - `ap-east-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v39.10.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v39.10.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

