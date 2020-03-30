# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v12-changelog.json`](changelogs/v12-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [12.0.0](#1200-2020-03-30)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes: Removed Regions](#existing-resourcetypes-and-propertytypes-removed-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [12.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v12.0.0) (2020-03-30)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v12-changelog.json)
  - Change source is a diff between [v12.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v12.0.0) and [v11.6.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v11.6.0)

### Totals

- TotalPropertyTypes: 1322 **(+12)**
- TotalPropertyTypesSupportedGlobally: 518 **(+9)**
- TotalResourceTypes: 523 **(+2)**
- TotalResourceTypesSupportedGlobally: 193 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::Detective::Graph](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`

- [AWS::Detective::MemberInvitation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html)
  - `ap-south-1`
  - `ap-northeast-2`
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`

- [AWS::EC2::EC2Fleet.CapacityReservationOptionsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-capacityreservationoptionsrequest.html)
  - `eu-central-1`
  - `us-west-2`
  - `cn-north-1`

- [AWS::EC2::EC2Fleet.Placement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-placement.html)
  - `eu-central-1`
  - `us-west-2`
  - `cn-north-1`

- [AWS::IoT::TopicRule.AssetPropertyTimestamp](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertytimestamp.html)
  - Available in **ALL** regions.

- [AWS::IoT::TopicRule.AssetPropertyValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvalue.html)
  - Available in **ALL** regions.

- [AWS::IoT::TopicRule.AssetPropertyVariant](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvariant.html)
  - Available in **ALL** regions.

- [AWS::IoT::TopicRule.HttpAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpaction.html)
  - Available in **ALL** regions.

- [AWS::IoT::TopicRule.HttpActionHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpactionheader.html)
  - Available in **ALL** regions.

- [AWS::IoT::TopicRule.HttpAuthorization](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpauthorization.html)
  - Available in **ALL** regions.

- [AWS::IoT::TopicRule.IotEventsAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-ioteventsaction.html)
  - Available in **ALL** regions.

- [AWS::IoT::TopicRule.IotSiteWiseAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotsitewiseaction.html)
  - Available in **ALL** regions.

- [AWS::IoT::TopicRule.PutAssetPropertyValueEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html)
  - Available in **ALL** regions.

- [AWS::IoT::TopicRule.SigV4Authorization](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sigv4authorization.html)
  - Available in **ALL** regions.

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::Cassandra::Keyspace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html)
  - `eu-west-1`
  - `eu-west-3`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `ap-south-1`
  - `us-west-1`
  - `eu-west-2`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `me-south-1`
  - `sa-east-1`
  - `eu-central-1`

- [AWS::Cassandra::Table](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html)
  - `eu-west-1`
  - `eu-west-3`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `ap-south-1`
  - `us-west-1`
  - `eu-west-2`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `me-south-1`
  - `sa-east-1`
  - `eu-central-1`

- [AWS::CodeStarConnections::Connection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-connection.html)
  - `eu-north-1`

- [AWS::ResourceGroups::Group](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html)
  - `ap-northeast-3`

- [AWS::Route53Resolver::ResolverEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html)
  - `sa-east-1`
  - `me-south-1`

- [AWS::Route53Resolver::ResolverRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html)
  - `sa-east-1`
  - `me-south-1`

- [AWS::Route53Resolver::ResolverRuleAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html)
  - `sa-east-1`
  - `me-south-1`

- [AWS::WAFv2::IPSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RegexPatternSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::Cassandra::Table.BillingMode](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-billingmode.html)
  - `eu-west-1`
  - `eu-west-3`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `ap-south-1`
  - `us-west-1`
  - `eu-west-2`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `me-south-1`
  - `sa-east-1`
  - `eu-central-1`

- [AWS::Cassandra::Table.ClusteringKeyColumn](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-clusteringkeycolumn.html)
  - `eu-west-1`
  - `eu-west-3`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `ap-south-1`
  - `us-west-1`
  - `eu-west-2`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `me-south-1`
  - `sa-east-1`
  - `eu-central-1`

- [AWS::Cassandra::Table.Column](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-column.html)
  - `eu-west-1`
  - `eu-west-3`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `ap-south-1`
  - `us-west-1`
  - `eu-west-2`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `me-south-1`
  - `sa-east-1`
  - `eu-central-1`

- [AWS::Cassandra::Table.ProvisionedThroughput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-provisionedthroughput.html)
  - `eu-west-1`
  - `eu-west-3`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `ap-south-1`
  - `us-west-1`
  - `eu-west-2`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `me-south-1`
  - `sa-east-1`
  - `eu-central-1`

- [AWS::CloudFront::Distribution.OriginGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroup.html)
  - `eu-north-1`

- [AWS::CloudFront::Distribution.OriginGroupFailoverCriteria](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupfailovercriteria.html)
  - `eu-north-1`

- [AWS::CloudFront::Distribution.OriginGroupMember](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmember.html)
  - `eu-north-1`

- [AWS::CloudFront::Distribution.OriginGroupMembers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroupmembers.html)
  - `eu-north-1`

- [AWS::CloudFront::Distribution.OriginGroups](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origingroups.html)
  - `eu-north-1`

- [AWS::CloudFront::Distribution.StatusCodes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-statuscodes.html)
  - `eu-north-1`

- [AWS::ResourceGroups::Group.Query](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-query.html)
  - `ap-northeast-3`

- [AWS::ResourceGroups::Group.ResourceQuery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-resourcequery.html)
  - `ap-northeast-3`

- [AWS::ResourceGroups::Group.TagFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-tagfilter.html)
  - `ap-northeast-3`

- [AWS::Route53Resolver::ResolverEndpoint.IpAddressRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html)
  - `sa-east-1`
  - `me-south-1`

- [AWS::Route53Resolver::ResolverRule.TargetAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html)
  - `sa-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.AndStatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-andstatementone.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.AndStatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-andstatementtwo.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.ByteMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.FieldToMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.GeoMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-geomatchstatement.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.IPSetReferenceStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.NotStatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-notstatementone.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.NotStatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-notstatementtwo.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.OrStatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-orstatementone.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.OrStatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-orstatementtwo.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.RateBasedStatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementone.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.RateBasedStatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatementtwo.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.RegexPatternSetReferenceStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.RuleAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.SizeConstraintStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.SqliMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sqlimatchstatement.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.StatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementone.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.StatementThree](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementthree.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.StatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statementtwo.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.TextTransformation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-texttransformation.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.VisibilityConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::RuleGroup.XssMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-xssmatchstatement.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.AndStatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-andstatementone.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.AndStatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-andstatementtwo.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.ByteMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.DefaultAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-defaultaction.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.ExcludedRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-excludedrule.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.FieldToMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.GeoMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-geomatchstatement.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.IPSetReferenceStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.ManagedRuleGroupStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.NotStatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatementone.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.NotStatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatementtwo.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.OrStatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-orstatementone.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.OrStatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-orstatementtwo.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.OverrideAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-overrideaction.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.RateBasedStatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementone.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.RateBasedStatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatementtwo.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.RegexPatternSetReferenceStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.RuleAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.RuleGroupReferenceStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rulegroupreferencestatement.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.SizeConstraintStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.SqliMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sqlimatchstatement.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.StatementOne](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementone.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.StatementThree](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementthree.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.StatementTwo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statementtwo.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.TextTransformation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformation.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.VisibilityConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html)
  - `ap-east-1`
  - `me-south-1`

- [AWS::WAFv2::WebACL.XssMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-xssmatchstatement.html)
  - `ap-east-1`
  - `me-south-1`

### Existing ResourceTypes and PropertyTypes: Removed Regions

- [AWS::EC2::EC2Fleet.TagRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-tagrequest.html)
  - `us-west-2`
  - `cn-north-1`
  - `eu-central-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v11.6.0: [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

  - Since v11.6.0: [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

  - Since v11.6.0: [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

- New ResourceType(s) Missing
  - [AWS::Detective::Graph](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html)
    - `ap-south-1`
    - `ap-northeast-2`
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `ap-southeast-2`

  - [AWS::Detective::MemberInvitation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html)
    - `ap-south-1`
    - `ap-northeast-2`
    - `ap-northeast-1`
    - `ap-southeast-1`
    - `ap-southeast-2`

- PropertyType Still Missing
  - Since v11.6.0: [AWS::GroundStation::DataflowEndpointGroup.DataflowEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

  - Since v11.6.0: [AWS::GroundStation::DataflowEndpointGroup.EndpointDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

  - Since v11.6.0: [AWS::GroundStation::DataflowEndpointGroup.SecurityDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-securitydetails.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

  - Since v11.6.0: [AWS::GroundStation::DataflowEndpointGroup.SocketAddress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-socketaddress.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

  - Since v11.6.0: [AWS::GroundStation::MissionProfile.DataflowEdge](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-missionprofile-dataflowedge.html)
    - `eu-north-1`
    - `eu-west-1`
    - `ap-southeast-2`
    - `us-east-2`
    - `us-west-2`
    - `me-south-1`

  - Since v11.6.0: [AWS::LakeFormation::Permissions.ColumnWildcard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html)
    - `ap-northeast-1`
    - `us-west-2`

  - Since v11.6.0: [AWS::LakeFormation::Permissions.DataLocationResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html)
    - `ap-northeast-1`
    - `us-west-2`

  - Since v11.6.0: [AWS::LakeFormation::Permissions.TableWithColumnsResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html)
    - `ap-northeast-1`
    - `us-west-2`

- New PropertyType(s) Missing
  - [AWS::EC2::EC2Fleet.CapacityReservationOptionsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-capacityreservationoptionsrequest.html)
    - `eu-central-1`
    - `us-west-2`
    - `cn-north-1`

  - [AWS::EC2::EC2Fleet.Placement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-placement.html)
    - `eu-central-1`
    - `us-west-2`
    - `cn-north-1`

