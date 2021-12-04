# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v50-changelog.json`](changelogs/v50-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [50.0.0](#5000-2021-12-04)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Complete Removal of ResourceTypes and/or PropertyTypes](#complete-removal-of-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [50.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v50.0.0) (2021-12-04)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v50-changelog.json)
  - Change source is a diff between [v50.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v50.0.0) and [v49.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v49.0.0)

### Totals

- TotalPropertyTypes: 2824 **(+57)**
- TotalPropertyTypesSupportedGlobally: 1008 **(+4)**
- TotalResourceTypes: 862 **(+23)**
- TotalResourceTypesSupportedGlobally: 330 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::AmplifyUIBuilder::Component](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-component.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Theme](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplifyuibuilder-theme.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFormation::HookDefaultVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookdefaultversion.html)
  - `eu-central-1`

- [AWS::CloudFormation::HookTypeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hooktypeconfig.html)
  - `eu-central-1`

- [AWS::Connect::ContactFlow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Connect::ContactFlowModule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::EC2::IPAM](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipam.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::EC2::IPAMAllocation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamallocation.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::EC2::IPAMPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampool.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::EC2::IPAMScope](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamscope.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Evidently::Experiment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Evidently::Feature](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Evidently::Launch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Evidently::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::RUM::AppMonitor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rum-appmonitor.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::RefactorSpaces::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::RefactorSpaces::Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::RefactorSpaces::Route](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::RefactorSpaces::Service](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::ResilienceHub::App](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::ResilienceHub::ResiliencyPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Timestream::ScheduledQuery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html)
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Transfer::Workflow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html)
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
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Component.ComponentBindingPropertiesValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalue.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Component.ComponentBindingPropertiesValueProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentbindingpropertiesvalueproperties.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Component.ComponentChild](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentchild.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Component.ComponentConditionProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentconditionproperty.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Component.ComponentDataConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentdataconfiguration.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Component.ComponentOverrides](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentoverrides.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Component.ComponentOverridesValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentoverridesvalue.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Component.ComponentProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperties.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Component.ComponentProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentproperty.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Component.ComponentPropertyBindingProperties](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentpropertybindingproperties.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Component.ComponentVariant](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentvariant.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Component.ComponentVariantValues](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentvariantvalues.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Component.FormBindings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-formbindings.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Component.Predicate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-predicate.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Component.SortProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-sortproperty.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Theme.ThemeValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-theme-themevalue.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Theme.ThemeValues](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-theme-themevalues.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::EC2::IPAM.IpamOperatingRegion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ipam-ipamoperatingregion.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::EC2::IPAMPool.ProvisionedCidr](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ipampool-provisionedcidr.html)
  - `af-south-1`
  - `ap-east-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::EC2::LaunchTemplate.InstanceRequirements](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-instancerequirements.html)
  - `sa-east-1`

- [AWS::Evidently::Experiment.MetricGoalObject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Evidently::Experiment.OnlineAbConfigObject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-onlineabconfigobject.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Evidently::Experiment.TreatmentObject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmentobject.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Evidently::Experiment.TreatmentToWeight](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmenttoweight.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Evidently::Feature.EntityOverride](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-entityoverride.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Evidently::Feature.VariationObject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Evidently::Launch.GroupToWeight](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-grouptoweight.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Evidently::Launch.LaunchGroupObject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-launchgroupobject.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Evidently::Launch.MetricDefinitionObject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Evidently::Launch.StepConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-stepconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Evidently::Project.DataDeliveryObject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-datadeliveryobject.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Evidently::Project.S3Destination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-s3destination.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::FSx::FileSystem.ClientConfigurations](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports-clientconfigurations.html)
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
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::FSx::FileSystem.NfsExports](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports.html)
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
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::FSx::FileSystem.OpenZFSConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html)
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
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::FSx::FileSystem.RootVolumeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration.html)
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
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::FSx::FileSystem.UserAndGroupQuotas](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-userandgroupquotas.html)
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
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::Kinesis::Stream.StreamModeDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesis-stream-streammodedetails.html)
  - `eu-central-1`

- [AWS::RUM::AppMonitor.AppMonitorConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-appmonitorconfiguration.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::RefactorSpaces::Application.ApiGatewayProxyInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-application-apigatewayproxyinput.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::RefactorSpaces::Route.UriPathRouteInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-uripathrouteinput.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::RefactorSpaces::Service.LambdaEndpointInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-service-lambdaendpointinput.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::RefactorSpaces::Service.UrlEndpointInput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-service-urlendpointinput.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::ResilienceHub::App.PhysicalResourceId](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-physicalresourceid.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::ResilienceHub::App.ResourceMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::ResilienceHub::ResiliencyPolicy.FailurePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-resiliencypolicy-failurepolicy.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::S3::Bucket.EventBridgeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfig-eventbridgeconfig.html)
  - Available in **ALL** regions.

- [AWS::S3::Bucket.NoncurrentVersionExpiration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lifecycleconfig-rule-noncurrentversionexpiration.html)
  - Available in **ALL** regions.

- [AWS::S3::StorageLens.CloudWatchMetrics](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-cloudwatchmetrics.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::SageMaker::EndpointConfig.ServerlessConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant-serverlessconfig.html)
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

- [AWS::Timestream::ScheduledQuery.DimensionMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-dimensionmapping.html)
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Timestream::ScheduledQuery.ErrorReportConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-errorreportconfiguration.html)
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Timestream::ScheduledQuery.MixedMeasureMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-mixedmeasuremapping.html)
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Timestream::ScheduledQuery.MultiMeasureAttributeMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasureattributemapping.html)
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Timestream::ScheduledQuery.MultiMeasureMappings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasuremappings.html)
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Timestream::ScheduledQuery.NotificationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-notificationconfiguration.html)
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Timestream::ScheduledQuery.S3Configuration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-s3configuration.html)
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Timestream::ScheduledQuery.ScheduleConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-scheduleconfiguration.html)
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Timestream::ScheduledQuery.SnsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-snsconfiguration.html)
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Timestream::ScheduledQuery.TargetConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-targetconfiguration.html)
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Timestream::ScheduledQuery.TimestreamConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-timestreamconfiguration.html)
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Transfer::Workflow.WorkflowStep](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html)
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
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

### Complete Removal of ResourceTypes and/or PropertyTypes

- [AWS::SageMaker::DataQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-environment.html)
  - `eu-west-3`

- [AWS::SageMaker::ModelBiasJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-environment.html)
  - `eu-west-3`

- [AWS::SageMaker::ModelExplainabilityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-environment.html)
  - `eu-west-3`

- [AWS::SageMaker::ModelQualityJobDefinition.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-environment.html)
  - `eu-west-3`

- [AWS::SageMaker::MonitoringSchedule.Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-environment.html)
  - `cn-northwest-1`
  - `eu-west-3`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::FMS::Policy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html)
  - `ap-northeast-3`

- [AWS::Route53::DNSSEC](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-dnssec.html)
  - `af-south-1`
  - `eu-south-1`

- [AWS::Route53::KeySigningKey](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html)
  - `af-south-1`
  - `eu-south-1`

- [AWS::EC2::EC2Fleet.CapacityRebalance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-capacityrebalance.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.MaintenanceStrategies](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-maintenancestrategies.html)
  - Now available to **ALL** regions.

- [AWS::FMS::Policy.IEMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html)
  - `ap-northeast-3`

- [AWS::FMS::Policy.PolicyTag](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html)
  - `ap-northeast-3`

- [AWS::FMS::Policy.ResourceTag](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html)
  - `ap-northeast-3`

- [AWS::MediaLive::Channel.AudioHlsRenditionSelection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiohlsrenditionselection.html)
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `us-west-2`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-south-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.AudioWatermarkSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-audiowatermarksettings.html)
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `us-west-2`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-south-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.NielsenCBET](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsencbet.html)
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `us-west-2`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-south-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.NielsenNaesIiNw](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsennaesiinw.html)
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `us-west-2`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-south-1`
  - `us-east-1`

- [AWS::MediaLive::Channel.NielsenWatermarksSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-medialive-channel-nielsenwatermarkssettings.html)
  - `eu-west-1`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `us-west-2`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-south-1`
  - `us-east-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v49.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v49.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v49.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v49.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v49.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v49.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- New ResourceType(s) Missing
  - [AWS::CloudFormation::HookDefaultVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookdefaultversion.html)
    - `eu-central-1`

  - [AWS::CloudFormation::HookTypeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hooktypeconfig.html)
    - `eu-central-1`

- PropertyType Still Missing
  - Since v49.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v49.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v49.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v49.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::EC2::LaunchTemplate.InstanceRequirements](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-instancerequirements.html)
    - `sa-east-1`

  - [AWS::Kinesis::Stream.StreamModeDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesis-stream-streammodedetails.html)
    - `eu-central-1`

