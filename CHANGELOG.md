# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v39-changelog.json`](changelogs/v39-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [39.2.0](#3920-2021-06-18)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)
- [39.1.0](#3910-2021-06-11)
  - [Totals](#totals-1)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes-1)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions-1)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1-1)

## [39.2.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.2.0) (2021-06-18)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v39-changelog.json)
  - Change source is a diff between [v39.2.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.2.0) and [v39.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.1.0)

### Totals

- TotalPropertyTypes: 2501 **(+19)**
- TotalPropertyTypesSupportedGlobally: 688 **(+22)**
- TotalResourceTypes: 768 **(+1)**
- TotalResourceTypesSupportedGlobally: 233 **(+12)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::KMS::ReplicaKey](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html)
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
  - `us-gov-east-1`
  - `us-gov-west-1`
  - `us-west-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.GatewayRouteHostnameMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.GatewayRouteHostnameRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutehostnamerewrite.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.GatewayRouteMetadataMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayroutemetadatamatch.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.GatewayRouteRangeMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-gatewayrouterangematch.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.GrpcGatewayRouteMetadata](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayroutemetadata.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.GrpcGatewayRouteRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-grpcgatewayrouterewrite.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRouteHeader](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRouteHeaderMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRoutePathRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayroutepathrewrite.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRoutePrefixRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.HttpGatewayRouteRewrite](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.HttpPathMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httppathmatch.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.HttpQueryParameterMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-httpqueryparametermatch.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::GatewayRoute.QueryParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-gatewayroute-queryparameter.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::Route.HttpPathMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httppathmatch.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::Route.HttpQueryParameterMatch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-httpqueryparametermatch.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::AppMesh::Route.QueryParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-route-queryparameter.html)
  - `ap-northeast-1`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-west-2`

- [AWS::DataBrew::Recipe.ParameterMap](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-databrew-recipe-parametermap.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-south-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `cn-north-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::Transfer::Server.ProtocolDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocoldetails.html)
  - `ap-northeast-2`
  - `ap-southeast-2`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-gov-east-1`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::ApiGateway::VpcLink](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-vpclink.html)
  - `eu-west-3`
  - `eu-central-1`

- [AWS::ApiGatewayV2::Api](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::ApiGatewayManagedOverrides](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html)
  - `cn-northwest-1`
  - `cn-north-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `ap-southeast-1`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-1`
  - `me-south-1`
  - `ap-southeast-2`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `af-south-1`
  - `eu-central-1`
  - `us-east-2`
  - `eu-west-3`

- [AWS::ApiGatewayV2::ApiMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Authorizer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Deployment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::DomainName](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Integration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::IntegrationResponse](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Model](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Route](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::RouteResponse](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Stage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::VpcLink](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html)
  - `cn-northwest-1`
  - `cn-north-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `us-west-1`
  - `ap-southeast-1`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-1`
  - `me-south-1`
  - `ap-southeast-2`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `af-south-1`
  - `eu-central-1`
  - `us-east-2`
  - `eu-west-3`

- [AWS::Config::ConfigurationAggregator](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html)
  - `eu-west-2`

- [AWS::EC2::EC2Fleet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html)
  - Now available to **ALL** regions.

- [AWS::GuardDuty::Detector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html)
  - `ap-northeast-3`

- [AWS::GuardDuty::Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html)
  - `ap-northeast-3`

- [AWS::GuardDuty::IPSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html)
  - `ap-northeast-3`

- [AWS::GuardDuty::Master](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html)
  - `ap-northeast-3`

- [AWS::GuardDuty::Member](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html)
  - `ap-northeast-3`

- [AWS::GuardDuty::ThreatIntelSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html)
  - `ap-northeast-3`

- [AWS::ApiGatewayV2::Api.BodyS3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Api.Cors](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::ApiGatewayManagedOverrides.AccessLogSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings.html)
  - `cn-northwest-1`
  - `cn-north-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `ap-southeast-1`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-1`
  - `me-south-1`
  - `ap-southeast-2`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `af-south-1`
  - `eu-central-1`
  - `us-east-2`
  - `eu-west-3`

- [AWS::ApiGatewayV2::ApiGatewayManagedOverrides.IntegrationOverrides](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html)
  - `cn-northwest-1`
  - `cn-north-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `ap-southeast-1`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-1`
  - `me-south-1`
  - `ap-southeast-2`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `af-south-1`
  - `eu-central-1`
  - `us-east-2`
  - `eu-west-3`

- [AWS::ApiGatewayV2::ApiGatewayManagedOverrides.RouteOverrides](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html)
  - `cn-northwest-1`
  - `cn-north-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `ap-southeast-1`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-1`
  - `me-south-1`
  - `ap-southeast-2`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `af-south-1`
  - `eu-central-1`
  - `us-east-2`
  - `eu-west-3`

- [AWS::ApiGatewayV2::ApiGatewayManagedOverrides.RouteSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html)
  - `cn-northwest-1`
  - `cn-north-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `ap-southeast-1`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-1`
  - `me-south-1`
  - `ap-southeast-2`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `af-south-1`
  - `eu-central-1`
  - `us-east-2`
  - `eu-west-3`

- [AWS::ApiGatewayV2::ApiGatewayManagedOverrides.StageOverrides](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html)
  - `cn-northwest-1`
  - `cn-north-1`
  - `ap-northeast-2`
  - `ap-northeast-3`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `ap-east-1`
  - `ap-southeast-1`
  - `eu-west-2`
  - `ap-south-1`
  - `eu-west-1`
  - `me-south-1`
  - `ap-southeast-2`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `af-south-1`
  - `eu-central-1`
  - `us-east-2`
  - `eu-west-3`

- [AWS::ApiGatewayV2::Authorizer.JWTConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::DomainName.DomainNameConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::DomainName.MutualTlsAuthentication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-mutualtlsauthentication.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Integration.ResponseParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameter.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Integration.ResponseParameterList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameterlist.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Integration.TlsConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-tlsconfig.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Route.ParameterConstraints](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-route-parameterconstraints.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::RouteResponse.ParameterConstraints](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-routeresponse-parameterconstraints.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Stage.AccessLogSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-accesslogsettings.html)
  - Now available to **ALL** regions.

- [AWS::ApiGatewayV2::Stage.RouteSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html)
  - Now available to **ALL** regions.

- [AWS::Config::ConfigurationAggregator.AccountAggregationSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html)
  - `eu-west-2`

- [AWS::Config::ConfigurationAggregator.OrganizationAggregationSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html)
  - `eu-west-2`

- [AWS::EC2::EC2Fleet.CapacityReservationOptionsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-capacityreservationoptionsrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.FleetLaunchTemplateConfigRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateconfigrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.FleetLaunchTemplateOverridesRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.FleetLaunchTemplateSpecificationRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.OnDemandOptionsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-ondemandoptionsrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.Placement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-placement.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.SpotOptionsRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-spotoptionsrequest.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.TagSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-tagspecification.html)
  - Now available to **ALL** regions.

- [AWS::EC2::EC2Fleet.TargetCapacitySpecificationRequest](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-targetcapacityspecificationrequest.html)
  - Now available to **ALL** regions.

- [AWS::EKS::Nodegroup.UpdateConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-updateconfig.html)
  - Now available to **ALL** regions.

- [AWS::GuardDuty::Detector.CFNDataSourceConfigurations](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html)
  - `ap-northeast-3`

- [AWS::GuardDuty::Detector.CFNS3LogsConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfns3logsconfiguration.html)
  - `ap-northeast-3`

- [AWS::GuardDuty::Filter.Condition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html)
  - `ap-northeast-3`

- [AWS::GuardDuty::Filter.FindingCriteria](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html)
  - `ap-northeast-3`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v39.1.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v39.1.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

## [39.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.1.0) (2021-06-11)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v39-changelog.json)
  - Change source is a diff between [v39.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v39.1.0) and [v38.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v38.0.0)

### Totals

- TotalPropertyTypes: 2482 **(+3)**
- TotalPropertyTypesSupportedGlobally: 666 **(+0)**
- TotalResourceTypes: 767 **(+0)**
- TotalResourceTypesSupportedGlobally: 221 **(+0)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::EKS::Nodegroup.UpdateConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-updateconfig.html)
  - `ap-northeast-2`

- [AWS::SSMContacts::Contact.ChannelTargetInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-channeltargetinfo.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::SSMContacts::Contact.ContactTargetInfo](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-contacttargetinfo.html)
  - `ap-northeast-1`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::AuditManager::Assessment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html)
  - `ap-south-1`
  - `ca-central-1`

- [AWS::EC2::CarrierGateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-carriergateway.html)
  - `eu-west-2`

- [AWS::AuditManager::Assessment.AWSAccount](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsaccount.html)
  - `ap-south-1`
  - `ca-central-1`

- [AWS::AuditManager::Assessment.AWSService](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsservice.html)
  - `ap-south-1`
  - `ca-central-1`

- [AWS::AuditManager::Assessment.AssessmentReportsDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-assessmentreportsdestination.html)
  - `ap-south-1`
  - `ca-central-1`

- [AWS::AuditManager::Assessment.Delegation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html)
  - `ap-south-1`
  - `ca-central-1`

- [AWS::AuditManager::Assessment.Role](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-role.html)
  - `ap-south-1`
  - `ca-central-1`

- [AWS::AuditManager::Assessment.Scope](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-scope.html)
  - `ap-south-1`
  - `ca-central-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- PropertyType Still Missing
  - Since v38.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v38.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::EKS::Nodegroup.UpdateConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-updateconfig.html)
    - `ap-northeast-2`

