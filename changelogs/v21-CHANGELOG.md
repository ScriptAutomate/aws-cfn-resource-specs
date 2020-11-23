# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v21-changelog.json`](changelogs/v21-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [21.0.0](#2100-2020-11-20)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [21.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v21.0.0) (2020-11-20)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v21-changelog.json)
  - Change source is a diff between [v21.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v21.0.0) and [v20.3.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v20.3.0)

### Totals

- TotalPropertyTypes: 1934 **(+105)**
- TotalPropertyTypesSupportedGlobally: 516 **(+0)**
- TotalResourceTypes: 611 **(+14)**
- TotalResourceTypesSupportedGlobally: 191 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::CloudFront::KeyGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-keygroup.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFront::PublicKey](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-publickey.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::Glue::Registry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-registry.html)
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

- [AWS::Glue::Schema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schema.html)
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

- [AWS::Glue::SchemaVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.html)
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

- [AWS::Glue::SchemaVersionMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversionmetadata.html)
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

- [AWS::IoT::TopicRuleDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html)
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

- [AWS::NetworkFirewall::Firewall](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::S3::StorageLens](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-storagelens.html)
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

- [AWS::Signer::ProfilePermission](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html)
  - `af-south-1`
  - `ap-east-1`
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Signer::SigningProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-signingprofile.html)
  - `af-south-1`
  - `ap-east-1`
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Batch::ComputeEnvironment.Ec2ConfigurationObject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-computeenvironment-ec2configurationobject.html)
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
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Batch::JobDefinition.FargatePlatformConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-fargateplatformconfiguration.html)
  - `ap-southeast-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::Batch::JobDefinition.NetworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-networkconfiguration.html)
  - `ap-southeast-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFront::KeyGroup.KeyGroupConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-keygroup-keygroupconfig.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::CloudFront::PublicKey.PublicKeyConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-publickey-publickeyconfig.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::Glue::Database.DataLakePrincipal](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-datalakeprincipal.html)
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Glue::Database.DatabaseIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-databaseidentifier.html)
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Glue::Database.PrincipalPrivileges](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-database-principalprivileges.html)
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Glue::MLTransform.MLUserDataEncryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformencryption-mluserdataencryption.html)
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Glue::MLTransform.TransformEncryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-mltransform-transformencryption.html)
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Glue::Schema.Registry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schema-registry.html)
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

- [AWS::Glue::Schema.SchemaVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schema-schemaversion.html)
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

- [AWS::Glue::SchemaVersion.Schema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-schemaversion-schema.html)
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

- [AWS::Glue::Table.TableIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-glue-table-tableidentifier.html)
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::IoT::TopicRuleDestination.HttpUrlDestinationSummary](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-httpurldestinationsummary.html)
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

- [AWS::Kendra::DataSource.ConfluenceAttachmentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmentconfiguration.html)
  - `us-west-2`

- [AWS::Kendra::DataSource.ConfluenceAttachmentFieldMappingsList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmentfieldmappingslist.html)
  - `us-west-2`

- [AWS::Kendra::DataSource.ConfluenceAttachmentToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmenttoindexfieldmapping.html)
  - `us-west-2`

- [AWS::Kendra::DataSource.ConfluenceBlogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogconfiguration.html)
  - `us-west-2`

- [AWS::Kendra::DataSource.ConfluenceBlogFieldMappingsList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogfieldmappingslist.html)
  - `us-west-2`

- [AWS::Kendra::DataSource.ConfluenceBlogToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogtoindexfieldmapping.html)
  - `us-west-2`

- [AWS::Kendra::DataSource.ConfluenceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html)
  - `us-west-2`

- [AWS::Kendra::DataSource.ConfluencePageConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepageconfiguration.html)
  - `us-west-2`

- [AWS::Kendra::DataSource.ConfluencePageFieldMappingsList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagefieldmappingslist.html)
  - `us-west-2`

- [AWS::Kendra::DataSource.ConfluencePageToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagetoindexfieldmapping.html)
  - `us-west-2`

- [AWS::Kendra::DataSource.ConfluenceSpaceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html)
  - `us-west-2`

- [AWS::Kendra::DataSource.ConfluenceSpaceFieldMappingsList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacefieldmappingslist.html)
  - `us-west-2`

- [AWS::Kendra::DataSource.ConfluenceSpaceList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacelist.html)
  - `us-west-2`

- [AWS::Kendra::DataSource.ConfluenceSpaceToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.html)
  - `us-west-2`

- [AWS::Kendra::Index.JsonTokenTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jsontokentypeconfiguration.html)
  - `us-west-2`

- [AWS::Kendra::Index.JwtTokenTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html)
  - `us-west-2`

- [AWS::Kendra::Index.UserTokenConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-usertokenconfiguration.html)
  - `us-west-2`

- [AWS::Kendra::Index.UserTokenConfigurationList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-usertokenconfigurationlist.html)
  - `us-west-2`

- [AWS::NetworkFirewall::Firewall.SubnetMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewall-subnetmapping.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::Firewall.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewall-tags.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.ActionDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-actiondefinition.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.CustomAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customaction.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.CustomActions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customactions.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.Dimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-dimension.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.Dimensions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-dimensions.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.FirewallPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.PublishMetricAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-publishmetricaction.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.StatefulRuleGroupReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.StatefulRuleGroupReferences](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreferences.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.StatelessActions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessactions.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.StatelessRuleGroupReference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.StatelessRuleGroupReferences](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreferences.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::FirewallPolicy.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-tags.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::LoggingConfiguration.LogDestinationConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::LoggingConfiguration.LogDestinationConfigs](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfigs.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::LoggingConfiguration.LoggingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-loggingconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.ActionDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-actiondefinition.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.Address](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-address.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.Addresses](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-addresses.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.CustomAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customaction.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.CustomActions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customactions.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.Dimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-dimension.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.Dimensions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-dimensions.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.Flags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-flags.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.Header](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.IPSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipset.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.MatchAttributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.PortRange](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portrange.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.PortRanges](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portranges.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.PortSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portset.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.ProtocolNumbers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-protocolnumbers.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.PublishMetricAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-publishmetricaction.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.RuleDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruledefinition.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.RuleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.RuleOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoption.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.RuleOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoptions.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.RuleVariables](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulevariables.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.RulesSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.RulesSourceList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.StatefulRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.StatefulRules](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrules.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.StatelessRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrule.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.StatelessRules](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrules.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.StatelessRulesAndCustomActions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.TCPFlagField](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflagfield.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.TCPFlags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflags.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.Tags](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tags.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.TargetTypes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-targettypes.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::NetworkFirewall::RuleGroup.VariableDefinitionList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-variabledefinitionlist.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::S3::StorageLens.AccountLevel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-accountlevel.html)
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

- [AWS::S3::StorageLens.ActivityMetrics](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-activitymetrics.html)
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

- [AWS::S3::StorageLens.AwsOrg](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-awsorg.html)
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

- [AWS::S3::StorageLens.BucketLevel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-bucketlevel.html)
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

- [AWS::S3::StorageLens.BucketsAndRegions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-bucketsandregions.html)
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

- [AWS::S3::StorageLens.DataExport](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-dataexport.html)
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

- [AWS::S3::StorageLens.Encryption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-encryption.html)
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

- [AWS::S3::StorageLens.PrefixLevel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-prefixlevel.html)
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

- [AWS::S3::StorageLens.PrefixLevelStorageMetrics](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-prefixlevelstoragemetrics.html)
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

- [AWS::S3::StorageLens.S3BucketDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-s3bucketdestination.html)
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

- [AWS::S3::StorageLens.SelectionCriteria](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-selectioncriteria.html)
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

- [AWS::S3::StorageLens.StorageLensConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-storagelens-storagelensconfiguration.html)
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

- [AWS::Signer::SigningProfile.SignatureValidityPeriod](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-signer-signingprofile-signaturevalidityperiod.html)
  - `af-south-1`
  - `ap-east-1`
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
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::WAFv2::RuleGroup.CustomResponseBodies](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customresponsebodies.html)
  - `eu-central-1`

- [AWS::WAFv2::WebACL.AllowAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-allowaction.html)
  - `eu-central-1`

- [AWS::WAFv2::WebACL.BlockAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-blockaction.html)
  - `eu-central-1`

- [AWS::WAFv2::WebACL.CountAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-countaction.html)
  - `eu-central-1`

- [AWS::WAFv2::WebACL.CustomHTTPHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customhttpheader.html)
  - `eu-central-1`

- [AWS::WAFv2::WebACL.CustomRequestHandling](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customrequesthandling.html)
  - `eu-central-1`

- [AWS::WAFv2::WebACL.CustomResponse](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponse.html)
  - `eu-central-1`

- [AWS::WAFv2::WebACL.CustomResponseBodies](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponsebodies.html)
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::CloudWatch::MetricStream](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html)
  - `ap-northeast-1`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-central-1`
  - `us-west-2`
  - `eu-west-1`

- [AWS::Kendra::DataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html)
  - `ap-southeast-2`

- [AWS::Kendra::Faq](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html)
  - `ap-southeast-2`

- [AWS::Kendra::Index](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html)
  - `ap-southeast-2`

- [AWS::Lambda::CodeSigningConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html)
  - `ap-east-1`
  - `ap-northeast-1`
  - `us-east-2`
  - `eu-north-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `eu-west-3`
  - `af-south-1`
  - `ap-northeast-2`
  - `us-east-1`
  - `eu-south-1`
  - `us-west-2`
  - `us-west-1`
  - `eu-west-2`
  - `me-south-1`

- [AWS::CloudWatch::MetricStream.MetricStreamFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamfilter.html)
  - `ap-northeast-1`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `eu-central-1`
  - `us-west-2`
  - `eu-west-1`

- [AWS::DLM::LifecyclePolicy.Action](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-action.html)
  - `ap-northeast-1`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `us-east-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `us-west-1`
  - `us-west-2`
  - `eu-west-2`
  - `eu-west-1`

- [AWS::DLM::LifecyclePolicy.CrossRegionCopyAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html)
  - `ap-northeast-1`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `us-east-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `us-west-1`
  - `us-west-2`
  - `eu-west-2`
  - `eu-west-1`

- [AWS::DLM::LifecyclePolicy.EncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-encryptionconfiguration.html)
  - `ap-northeast-1`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `us-east-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `us-west-1`
  - `us-west-2`
  - `eu-west-2`
  - `eu-west-1`

- [AWS::DLM::LifecyclePolicy.EventParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html)
  - `ap-northeast-1`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `us-east-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `us-west-1`
  - `us-west-2`
  - `eu-west-2`
  - `eu-west-1`

- [AWS::DLM::LifecyclePolicy.EventSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventsource.html)
  - `ap-northeast-1`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `us-east-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `us-west-1`
  - `us-west-2`
  - `eu-west-2`
  - `eu-west-1`

- [AWS::DLM::LifecyclePolicy.ShareRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html)
  - `ap-northeast-1`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `us-east-1`
  - `eu-central-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `us-west-2`
  - `us-west-1`
  - `eu-west-2`

- [AWS::EC2::LaunchTemplate.EnclaveOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-enclaveoptions.html)
  - `ap-east-1`
  - `us-east-2`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-gov-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `us-west-1`
  - `ap-northeast-3`
  - `ap-northeast-1`
  - `ap-southeast-2`
  - `eu-west-3`
  - `ap-northeast-2`
  - `cn-northwest-1`
  - `ap-southeast-1`
  - `ap-south-1`
  - `us-gov-west-1`
  - `eu-west-2`
  - `me-south-1`

- [AWS::Kendra::DataSource.AccessControlListConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-accesscontrollistconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.AclConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-aclconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.ChangeDetectingColumns](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-changedetectingcolumns.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.ColumnConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.ConnectionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.DataSourceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.DataSourceInclusionsExclusionsStrings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceinclusionsexclusionsstrings.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.DataSourceToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmapping.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.DataSourceToIndexFieldMappingList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmappinglist.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.DataSourceVpcConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcevpcconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.DatabaseConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.DocumentsMetadataConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentsmetadataconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.OneDriveConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.OneDriveUserList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveuserlist.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.OneDriveUsers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveusers.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.S3DataSourceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.S3Path](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3path.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.SalesforceChatterFeedConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.SalesforceChatterFeedIncludeFilterTypes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedincludefiltertypes.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.SalesforceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.SalesforceCustomKnowledgeArticleTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.SalesforceCustomKnowledgeArticleTypeConfigurationList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfigurationlist.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.SalesforceKnowledgeArticleConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.SalesforceKnowledgeArticleStateList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticlestatelist.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.SalesforceStandardKnowledgeArticleTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.SalesforceStandardObjectAttachmentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.SalesforceStandardObjectConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.SalesforceStandardObjectConfigurationList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfigurationlist.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.ServiceNowConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.ServiceNowKnowledgeArticleConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.ServiceNowServiceCatalogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.SharePointConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.SqlConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sqlconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::DataSource.TagList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-taglist.html)
  - `ap-southeast-2`

- [AWS::Kendra::Faq.S3Path](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-faq-s3path.html)
  - `ap-southeast-2`

- [AWS::Kendra::Faq.TagList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-faq-taglist.html)
  - `ap-southeast-2`

- [AWS::Kendra::Index.CapacityUnitsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-capacityunitsconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::Index.DocumentMetadataConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::Index.DocumentMetadataConfigurationList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfigurationlist.html)
  - `ap-southeast-2`

- [AWS::Kendra::Index.Relevance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html)
  - `ap-southeast-2`

- [AWS::Kendra::Index.Search](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html)
  - `ap-southeast-2`

- [AWS::Kendra::Index.ServerSideEncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-serversideencryptionconfiguration.html)
  - `ap-southeast-2`

- [AWS::Kendra::Index.TagList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-taglist.html)
  - `ap-southeast-2`

- [AWS::Kendra::Index.ValueImportanceItem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-valueimportanceitem.html)
  - `ap-southeast-2`

- [AWS::Kendra::Index.ValueImportanceItems](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-valueimportanceitems.html)
  - `ap-southeast-2`

- [AWS::Lambda::CodeSigningConfig.AllowedPublishers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-codesigningconfig-allowedpublishers.html)
  - `ap-east-1`
  - `ap-northeast-1`
  - `us-east-2`
  - `eu-north-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `eu-west-3`
  - `af-south-1`
  - `ap-northeast-2`
  - `us-east-1`
  - `eu-south-1`
  - `us-west-2`
  - `us-west-1`
  - `eu-west-2`
  - `me-south-1`

- [AWS::Lambda::CodeSigningConfig.CodeSigningPolicies](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-codesigningconfig-codesigningpolicies.html)
  - `ap-east-1`
  - `ap-northeast-1`
  - `us-east-2`
  - `eu-north-1`
  - `sa-east-1`
  - `ap-southeast-2`
  - `eu-west-3`
  - `af-south-1`
  - `ap-northeast-2`
  - `us-east-1`
  - `eu-south-1`
  - `us-west-2`
  - `us-west-1`
  - `eu-west-2`
  - `me-south-1`

- [AWS::SageMaker::Model.MultiModelConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-multimodelconfig.html)
  - `ap-northeast-1`
  - `us-east-2`
  - `ap-southeast-2`
  - `ap-northeast-2`
  - `us-east-1`
  - `ap-southeast-1`
  - `ca-central-1`
  - `ap-south-1`
  - `eu-west-2`
  - `eu-west-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v20.3.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v20.3.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v20.3.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

- PropertyType Still Missing
  - Since v20.3.0: [AWS::ECS::Cluster.ClusterSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-cluster-clustersetting.html)
    - `af-south-1`
    - `ap-northeast-3`
    - `eu-south-1`

  - Since v20.3.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v20.3.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v20.3.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v20.3.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v20.3.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `af-south-1`
    - `ap-southeast-2`
    - `eu-central-1`
    - `eu-north-1`
    - `eu-west-1`
    - `me-south-1`
    - `us-east-2`
    - `us-west-2`

  - Since v20.3.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v20.3.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::Batch::JobDefinition.FargatePlatformConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-fargateplatformconfiguration.html)
    - `ap-southeast-1`
    - `us-west-1`
    - `us-west-2`

  - [AWS::Batch::JobDefinition.NetworkConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-batch-jobdefinition-containerproperties-networkconfiguration.html)
    - `ap-southeast-1`
    - `us-west-1`
    - `us-west-2`

  - [AWS::Kendra::DataSource.ConfluenceAttachmentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmentconfiguration.html)
    - `us-west-2`

  - [AWS::Kendra::DataSource.ConfluenceAttachmentFieldMappingsList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmentfieldmappingslist.html)
    - `us-west-2`

  - [AWS::Kendra::DataSource.ConfluenceAttachmentToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmenttoindexfieldmapping.html)
    - `us-west-2`

  - [AWS::Kendra::DataSource.ConfluenceBlogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogconfiguration.html)
    - `us-west-2`

  - [AWS::Kendra::DataSource.ConfluenceBlogFieldMappingsList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogfieldmappingslist.html)
    - `us-west-2`

  - [AWS::Kendra::DataSource.ConfluenceBlogToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogtoindexfieldmapping.html)
    - `us-west-2`

  - [AWS::Kendra::DataSource.ConfluenceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html)
    - `us-west-2`

  - [AWS::Kendra::DataSource.ConfluencePageConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepageconfiguration.html)
    - `us-west-2`

  - [AWS::Kendra::DataSource.ConfluencePageFieldMappingsList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagefieldmappingslist.html)
    - `us-west-2`

  - [AWS::Kendra::DataSource.ConfluencePageToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagetoindexfieldmapping.html)
    - `us-west-2`

  - [AWS::Kendra::DataSource.ConfluenceSpaceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html)
    - `us-west-2`

  - [AWS::Kendra::DataSource.ConfluenceSpaceFieldMappingsList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacefieldmappingslist.html)
    - `us-west-2`

  - [AWS::Kendra::DataSource.ConfluenceSpaceList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacelist.html)
    - `us-west-2`

  - [AWS::Kendra::DataSource.ConfluenceSpaceToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.html)
    - `us-west-2`

  - [AWS::Kendra::Index.JsonTokenTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jsontokentypeconfiguration.html)
    - `us-west-2`

  - [AWS::Kendra::Index.JwtTokenTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html)
    - `us-west-2`

  - [AWS::Kendra::Index.UserTokenConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-usertokenconfiguration.html)
    - `us-west-2`

  - [AWS::Kendra::Index.UserTokenConfigurationList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-usertokenconfigurationlist.html)
    - `us-west-2`

  - [AWS::WAFv2::RuleGroup.CustomResponseBodies](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customresponsebodies.html)
    - `eu-central-1`

  - [AWS::WAFv2::WebACL.AllowAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-allowaction.html)
    - `eu-central-1`

  - [AWS::WAFv2::WebACL.BlockAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-blockaction.html)
    - `eu-central-1`

  - [AWS::WAFv2::WebACL.CountAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-countaction.html)
    - `eu-central-1`

  - [AWS::WAFv2::WebACL.CustomHTTPHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customhttpheader.html)
    - `eu-central-1`

  - [AWS::WAFv2::WebACL.CustomRequestHandling](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customrequesthandling.html)
    - `eu-central-1`

  - [AWS::WAFv2::WebACL.CustomResponse](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponse.html)
    - `eu-central-1`

  - [AWS::WAFv2::WebACL.CustomResponseBodies](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponsebodies.html)
    - `eu-central-1`

