# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v57-changelog.json`](changelogs/v57-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [57.0.0](#5700-2022-02-18)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [57.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v57.0.0) (2022-02-18)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v57-changelog.json)
  - Change source is a diff between [v57.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v57.0.0) and [v56.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v56.0.0)

### Totals

- TotalPropertyTypes: 2974 **(+16)**
- TotalPropertyTypesSupportedGlobally: 1066 **(+2)**
- TotalResourceTypes: 891 **(+2)**
- TotalResourceTypesSupportedGlobally: 335 **(+1)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::DataSync::LocationFSxLustre](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxlustre.html)
  - `ap-northeast-2`

- [AWS::ECR::PullThroughCacheRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-pullthroughcacherule.html)
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

- [AWS::AmplifyUIBuilder::Component.ActionParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html)
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Component.ComponentEvent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentevent.html)
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Component.ComponentEvents](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentevents.html)
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::AmplifyUIBuilder::Component.MutationActionSetStateParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-mutationactionsetstateparameter.html)
  - `ap-northeast-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::AppMesh::Mesh.MeshServiceDiscovery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshservicediscovery.html)
  - `eu-central-1`

- [AWS::EC2::Instance.PrivateDnsNameOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-privatednsnameoptions.html)
  - Available in **ALL** regions.

- [AWS::Kendra::DataSource.CustomDocumentEnrichmentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-customdocumentenrichmentconfiguration.html)
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Kendra::DataSource.DocumentAttributeCondition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributecondition.html)
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Kendra::DataSource.DocumentAttributeTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributetarget.html)
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Kendra::DataSource.DocumentAttributeValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributevalue.html)
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Kendra::DataSource.HookConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-hookconfiguration.html)
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Kendra::DataSource.InlineCustomDocumentEnrichmentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-inlinecustomdocumentenrichmentconfiguration.html)
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::Lambda::EventSourceMapping.Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filter.html)
  - `af-south-1`
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
  - `us-west-1`
  - `us-west-2`

- [AWS::Lambda::EventSourceMapping.FilterCriteria](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.html)
  - `af-south-1`
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
  - `us-west-1`
  - `us-west-2`

- [AWS::WAFv2::WebACL.FieldIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldidentifier.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::WAFv2::WebACL.ManagedRuleGroupConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupconfig.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `cn-north-1`
  - `eu-central-1`
  - `us-east-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Kendra::DataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html)
  - `ca-central-1`

- [AWS::Kendra::Faq](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html)
  - `ca-central-1`
  - `us-east-2`

- [AWS::Kendra::Index](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html)
  - `ca-central-1`
  - `us-east-2`

- [AWS::SSO::Assignment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html)
  - `us-gov-east-1`

- [AWS::SSO::InstanceAccessControlAttributeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html)
  - `us-gov-east-1`

- [AWS::SSO::PermissionSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html)
  - `us-gov-east-1`

- [AWS::Transfer::Workflow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html)
  - Now available to **ALL** regions.

- [AWS::Kendra::DataSource.AccessControlListConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-accesscontrollistconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.AclConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-aclconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.ColumnConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.ConfluenceAttachmentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmentconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.ConfluenceAttachmentToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmenttoindexfieldmapping.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.ConfluenceBlogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.ConfluenceBlogToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogtoindexfieldmapping.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.ConfluenceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.ConfluencePageConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepageconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.ConfluencePageToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagetoindexfieldmapping.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.ConfluenceSpaceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.ConfluenceSpaceToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.ConnectionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.DataSourceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.DataSourceToIndexFieldMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmapping.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.DataSourceVpcConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcevpcconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.DatabaseConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.DocumentsMetadataConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentsmetadataconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.GoogleDriveConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.OneDriveConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.OneDriveUsers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveusers.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.ProxyConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-proxyconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.S3DataSourceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.S3Path](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3path.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.SalesforceChatterFeedConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.SalesforceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.SalesforceCustomKnowledgeArticleTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.SalesforceKnowledgeArticleConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.SalesforceStandardKnowledgeArticleTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.SalesforceStandardObjectAttachmentConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.SalesforceStandardObjectConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.ServiceNowConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.ServiceNowKnowledgeArticleConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.ServiceNowServiceCatalogConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.SharePointConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.SqlConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sqlconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.WebCrawlerAuthenticationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerauthenticationconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.WebCrawlerBasicAuthentication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerbasicauthentication.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.WebCrawlerConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.WebCrawlerSeedUrlConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerseedurlconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.WebCrawlerSiteMapsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlersitemapsconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.WebCrawlerUrls](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerurls.html)
  - `ca-central-1`

- [AWS::Kendra::DataSource.WorkDocsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html)
  - `ca-central-1`

- [AWS::Kendra::Faq.S3Path](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-faq-s3path.html)
  - `ca-central-1`
  - `us-east-2`

- [AWS::Kendra::Index.CapacityUnitsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-capacityunitsconfiguration.html)
  - `ca-central-1`
  - `us-east-2`

- [AWS::Kendra::Index.DocumentMetadataConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html)
  - `ca-central-1`
  - `us-east-2`

- [AWS::Kendra::Index.JsonTokenTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jsontokentypeconfiguration.html)
  - `ca-central-1`
  - `us-east-2`

- [AWS::Kendra::Index.JwtTokenTypeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html)
  - `ca-central-1`
  - `us-east-2`

- [AWS::Kendra::Index.Relevance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html)
  - `ca-central-1`
  - `us-east-2`

- [AWS::Kendra::Index.Search](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html)
  - `ca-central-1`
  - `us-east-2`

- [AWS::Kendra::Index.ServerSideEncryptionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-serversideencryptionconfiguration.html)
  - `ca-central-1`
  - `us-east-2`

- [AWS::Kendra::Index.UserTokenConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-usertokenconfiguration.html)
  - `ca-central-1`
  - `us-east-2`

- [AWS::Kendra::Index.ValueImportanceItem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-valueimportanceitem.html)
  - `ca-central-1`
  - `us-east-2`

- [AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html)
  - `us-gov-east-1`

- [AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttributeValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html)
  - `us-gov-east-1`

- [AWS::Transfer::Workflow.WorkflowStep](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html)
  - Now available to **ALL** regions.

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v56.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v56.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v56.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v56.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v56.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v56.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- New ResourceType(s) Missing
  - [AWS::DataSync::LocationFSxLustre](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxlustre.html)
    - `ap-northeast-2`

- PropertyType Still Missing
  - Since v56.0.0: [AWS::DevOpsGuru::ResourceCollection.TagCollection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-tagcollection.html)
    - `eu-central-1`

  - Since v56.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v56.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v56.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v56.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::AmplifyUIBuilder::Component.ActionParameters](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-actionparameters.html)
    - `ap-northeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::AmplifyUIBuilder::Component.ComponentEvent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentevent.html)
    - `ap-northeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::AmplifyUIBuilder::Component.ComponentEvents](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-componentevents.html)
    - `ap-northeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::AmplifyUIBuilder::Component.MutationActionSetStateParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplifyuibuilder-component-mutationactionsetstateparameter.html)
    - `ap-northeast-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::AppMesh::Mesh.MeshServiceDiscovery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshservicediscovery.html)
    - `eu-central-1`

