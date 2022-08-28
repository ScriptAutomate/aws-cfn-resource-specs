# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v86-changelog.json`](changelogs/v86-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [86.0.0](#8600-2022-08-28)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [86.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v86.0.0) (2022-08-28)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v86-changelog.json)
  - Change source is a diff between [v86.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v86.0.0) and [v85.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v85.0.0)

### Totals

- TotalPropertyTypes: 3294 **(+15)**
- TotalPropertyTypesSupportedGlobally: 1141 **(+4)**
- TotalResourceTypes: 952 **(+3)**
- TotalResourceTypesSupportedGlobally: 344 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::Connect::InstanceStorageConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html)
  - `eu-central-1`

- [AWS::SupportApp::AccountAlias](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-accountalias.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::SupportApp::SlackChannelConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-supportapp-slackchannelconfiguration.html)
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::Route.TcpRouteMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproutematch.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::VirtualGateway.JsonFormatRef](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-jsonformatref.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::VirtualGateway.LoggingFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-loggingformat.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::VirtualNode.JsonFormatRef](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-jsonformatref.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::VirtualNode.LoggingFormat](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-loggingformat.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::CloudFront::ResponseHeadersPolicy.ServerTimingHeadersConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-responseheaderspolicy-servertimingheadersconfig.html)
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

- [AWS::Connect::InstanceStorageConfig.EncryptionConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-encryptionconfig.html)
  - `eu-central-1`

- [AWS::Connect::InstanceStorageConfig.KinesisFirehoseConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisfirehoseconfig.html)
  - `eu-central-1`

- [AWS::Connect::InstanceStorageConfig.KinesisStreamConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisstreamconfig.html)
  - `eu-central-1`

- [AWS::Connect::InstanceStorageConfig.KinesisVideoStreamConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisvideostreamconfig.html)
  - `eu-central-1`

- [AWS::Connect::InstanceStorageConfig.S3Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-s3config.html)
  - `eu-central-1`

- [AWS::DynamoDB::Table.Csv](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-csv.html)
  - Available in **ALL** regions.

- [AWS::DynamoDB::Table.ImportSourceSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-importsourcespecification.html)
  - Available in **ALL** regions.

- [AWS::DynamoDB::Table.InputFormatOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-inputformatoptions.html)
  - Available in **ALL** regions.

- [AWS::DynamoDB::Table.S3BucketSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-s3bucketsource.html)
  - Available in **ALL** regions.

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::AppMesh::GatewayRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-gatewayroute.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Mesh](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualgateway.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualRouter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualService](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html)
  - `ap-northeast-3`

- [AWS::Cassandra::Keyspace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Cassandra::Table](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Connect::Instance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instance.html)
  - `ap-south-1`
  - `eu-west-2`
  - `us-gov-west-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `af-south-1`
  - `ca-central-1`
  - `us-east-1`

- [AWS::EC2::TransitGatewayConnect](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayconnect.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::EC2::TransitGatewayMulticastDomain](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastdomain.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::EC2::TransitGatewayMulticastDomainAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastdomainassociation.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::EC2::TransitGatewayMulticastGroupMember](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupmember.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::EC2::TransitGatewayMulticastGroupSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::EC2::TransitGatewayVpcAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayvpcattachment.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::AppMesh::GatewayRoute.GatewayRouteHostnameMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.GatewayRouteHostnameRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamerewrite.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.GatewayRouteMetadataMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.GatewayRouteRangeMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayrouterangematch.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.GatewayRouteSpec](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutespec.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.GatewayRouteTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutetarget.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.GatewayRouteVirtualService](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutevirtualservice.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.GrpcGatewayRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroute.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.GrpcGatewayRouteAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouteaction.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.GrpcGatewayRouteMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutematch.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.GrpcGatewayRouteMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.GrpcGatewayRouteRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouterewrite.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroute.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRouteAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteaction.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRouteHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRouteHeaderMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRouteMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutematch.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRoutePathRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutepathrewrite.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRoutePrefixRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRouteRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.HttpPathMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httppathmatch.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.HttpQueryParameterMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpqueryparametermatch.html)
  - `ap-northeast-3`

- [AWS::AppMesh::GatewayRoute.QueryParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-queryparameter.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Mesh.EgressFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-egressfilter.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Mesh.MeshServiceDiscovery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshservicediscovery.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Mesh.MeshSpec](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-mesh-meshspec.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.Duration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-duration.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.GrpcRetryPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcretrypolicy.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.GrpcRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroute.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.GrpcRouteAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcrouteaction.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.GrpcRouteMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutematch.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.GrpcRouteMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadata.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.GrpcRouteMetadataMatchMethod](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpcroutemetadatamatchmethod.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.GrpcTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-grpctimeout.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.HeaderMatchMethod](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-headermatchmethod.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.HttpPathMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httppathmatch.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.HttpQueryParameterMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpqueryparametermatch.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.HttpRetryPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpretrypolicy.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.HttpRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproute.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.HttpRouteAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteaction.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.HttpRouteHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httprouteheader.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.HttpRouteMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httproutematch.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.HttpTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httptimeout.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.MatchRange](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-matchrange.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.QueryParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-queryparameter.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.RouteSpec](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-routespec.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.TcpRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcproute.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.TcpRouteAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcprouteaction.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.TcpTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-tcptimeout.html)
  - `ap-northeast-3`

- [AWS::AppMesh::Route.WeightedTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-weightedtarget.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.SubjectAlternativeNameMatchers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenamematchers.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.SubjectAlternativeNames](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-subjectalternativenames.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayAccessLog](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayaccesslog.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayBackendDefaults](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaybackenddefaults.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayClientPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicy.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayClientPolicyTls](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclientpolicytls.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayClientTlsCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayConnectionPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayFileAccessLog](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayfileaccesslog.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayGrpcConnectionPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaygrpcconnectionpool.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayHealthCheckPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayHttp2ConnectionPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttp2connectionpool.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayHttpConnectionPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayhttpconnectionpool.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayListener](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTls](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsAcmCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsacmcertificate.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsFileCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsSdsCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlssdscertificate.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsValidationContext](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayListenerTlsValidationContextTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayLogging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaylogging.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayPortMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayportmapping.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewaySpec](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewayspec.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContext](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContextAcmTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContextFileTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextfiletrust.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContextSdsTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualGateway.VirtualGatewayTlsValidationContextTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.AccessLog](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-accesslog.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.AwsCloudMapInstanceAttribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapinstanceattribute.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.AwsCloudMapServiceDiscovery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-awscloudmapservicediscovery.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.Backend](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backend.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.BackendDefaults](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backenddefaults.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.ClientPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicy.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.ClientPolicyTls](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clientpolicytls.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.ClientTlsCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-clienttlscertificate.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.DnsServiceDiscovery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-dnsservicediscovery.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.Duration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-duration.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.FileAccessLog](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-fileaccesslog.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.GrpcTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-grpctimeout.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.HealthCheck](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-healthcheck.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.HttpTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-httptimeout.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.Listener](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listener.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.ListenerTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertimeout.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.ListenerTls](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertls.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.ListenerTlsAcmCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsacmcertificate.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.ListenerTlsCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlscertificate.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.ListenerTlsFileCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsfilecertificate.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.ListenerTlsSdsCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlssdscertificate.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.ListenerTlsValidationContext](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontext.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.ListenerTlsValidationContextTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.Logging](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-logging.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.OutlierDetection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-outlierdetection.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.PortMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-portmapping.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.ServiceDiscovery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-servicediscovery.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.SubjectAlternativeNameMatchers](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenamematchers.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.SubjectAlternativeNames](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-subjectalternativenames.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.TcpTimeout](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tcptimeout.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.TlsValidationContext](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontext.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.TlsValidationContextAcmTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextacmtrust.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.TlsValidationContextFileTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextfiletrust.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.TlsValidationContextSdsTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontextsdstrust.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.TlsValidationContextTrust](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.VirtualNodeConnectionPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodeconnectionpool.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.VirtualNodeGrpcConnectionPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodegrpcconnectionpool.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.VirtualNodeHttp2ConnectionPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttp2connectionpool.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.VirtualNodeHttpConnectionPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodehttpconnectionpool.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.VirtualNodeSpec](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodespec.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.VirtualNodeTcpConnectionPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualnodetcpconnectionpool.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualNode.VirtualServiceBackend](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-virtualservicebackend.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualRouter.PortMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-portmapping.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualRouter.VirtualRouterListener](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterlistener.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualRouter.VirtualRouterSpec](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualrouter-virtualrouterspec.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualService.VirtualNodeServiceProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualnodeserviceprovider.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualService.VirtualRouterServiceProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualrouterserviceprovider.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualService.VirtualServiceProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualserviceprovider.html)
  - `ap-northeast-3`

- [AWS::AppMesh::VirtualService.VirtualServiceSpec](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualservice-virtualservicespec.html)
  - `ap-northeast-3`

- [AWS::Cassandra::Table.BillingMode](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-billingmode.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Cassandra::Table.ClusteringKeyColumn](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-clusteringkeycolumn.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Cassandra::Table.Column](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-column.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Cassandra::Table.EncryptionSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Cassandra::Table.ProvisionedThroughput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-provisionedthroughput.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::Connect::Instance.Attributes](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instance-attributes.html)
  - `ap-south-1`
  - `eu-west-2`
  - `us-gov-west-1`
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `ap-southeast-1`
  - `af-south-1`
  - `ca-central-1`
  - `us-east-1`

- [AWS::EC2::NetworkInsightsAnalysis.AdditionalDetail](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinsightsanalysis-additionaldetail.html)
  - `us-east-2`
  - `eu-north-1`
  - `eu-west-3`
  - `ap-east-1`
  - `eu-west-2`
  - `eu-south-1`
  - `ap-northeast-2`
  - `us-west-1`
  - `me-south-1`
  - `af-south-1`
  - `sa-east-1`

- [AWS::EC2::TransitGatewayConnect.TransitGatewayConnectOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-transitgatewayconnect-transitgatewayconnectoptions.html)
  - `us-gov-east-1`
  - `us-gov-west-1`

- [AWS::RDS::DBCluster.ReadEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbcluster-readendpoint.html)
  - `ap-south-1`
  - `eu-west-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `ap-southeast-1`
  - `sa-east-1`
  - `us-east-1`

- [AWS::RDS::DBInstance.Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbinstance-endpoint.html)
  - `cn-northwest-1`
  - `cn-north-1`

- [AWS::SSM::MaintenanceWindowTask.CloudWatchOutputConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig.html)
  - `cn-north-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v85.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v85.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v85.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v85.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v85.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v85.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- New ResourceType(s) Missing
  - [AWS::Connect::InstanceStorageConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html)
    - `eu-central-1`

- PropertyType Still Missing
  - Since v85.0.0: [AWS::Config::OrganizationConfigRule.OrganizationCustomPolicyRuleMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html)
    - `me-south-1`

  - Since v85.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v85.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v85.0.0: [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v85.0.0: [AWS::Redshift::ScheduledAction.PauseClusterMessage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-pauseclustermessage.html)
    - `us-gov-west-1`

  - Since v85.0.0: [AWS::Redshift::ScheduledAction.ResizeClusterMessage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resizeclustermessage.html)
    - `us-gov-west-1`

  - Since v85.0.0: [AWS::Redshift::ScheduledAction.ResumeClusterMessage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-scheduledaction-resumeclustermessage.html)
    - `us-gov-west-1`

  - Since v85.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v85.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::Connect::InstanceStorageConfig.EncryptionConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-encryptionconfig.html)
    - `eu-central-1`

  - [AWS::Connect::InstanceStorageConfig.KinesisFirehoseConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisfirehoseconfig.html)
    - `eu-central-1`

  - [AWS::Connect::InstanceStorageConfig.KinesisStreamConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisstreamconfig.html)
    - `eu-central-1`

  - [AWS::Connect::InstanceStorageConfig.KinesisVideoStreamConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisvideostreamconfig.html)
    - `eu-central-1`

  - [AWS::Connect::InstanceStorageConfig.S3Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-s3config.html)
    - `eu-central-1`

