# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v79-changelog.json`](changelogs/v79-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [79.0.0](#7900-2022-07-08)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [79.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v79.0.0) (2022-07-08)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v79-changelog.json)
  - Change source is a diff between [v79.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v79.0.0) and [v78.1.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v78.1.0)

### Totals

- TotalPropertyTypes: 3256 **(+5)**
- TotalPropertyTypesSupportedGlobally: 1132 **(+7)**
- TotalResourceTypes: 944 **(+3)**
- TotalResourceTypesSupportedGlobally: 344 **(+2)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::RedshiftServerless::Workgroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::RolesAnywhere::Profile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::RolesAnywhere::TrustAnchor](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-trustanchor.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::RedshiftServerless::Workgroup.ConfigParameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-configparameter.html)
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `eu-central-1`
  - `eu-north-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-east-2`
  - `us-west-2`

- [AWS::RolesAnywhere::TrustAnchor.Source](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-source.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::RolesAnywhere::TrustAnchor.SourceData](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-sourcedata.html)
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
  - `eu-west-1`
  - `eu-west-2`
  - `eu-west-3`
  - `me-south-1`
  - `sa-east-1`
  - `us-east-1`
  - `us-east-2`
  - `us-west-1`
  - `us-west-2`

- [AWS::SageMaker::NotebookInstance.InstanceMetadataServiceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-notebookinstance-instancemetadataserviceconfiguration.html)
  - `cn-north-1`
  - `eu-central-1`
  - `us-west-2`

- [AWS::SageMaker::Workteam.OidcMemberDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-oidcmemberdefinition.html)
  - `cn-north-1`
  - `eu-central-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::DataSync::LocationFSxONTAP](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxontap.html)
  - `ap-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `me-south-1`
  - `us-gov-west-1`
  - `eu-west-1`
  - `ap-southeast-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-central-1`
  - `us-gov-east-1`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `ap-southeast-2`
  - `eu-west-2`

- [AWS::EC2::CapacityReservation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html)
  - Now available to **ALL** regions.

- [AWS::EC2::PrefixList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-prefixlist.html)
  - Now available to **ALL** regions.

- [AWS::SSO::Assignment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html)
  - `me-south-1`
  - `ap-east-1`

- [AWS::SSO::InstanceAccessControlAttributeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html)
  - `me-south-1`
  - `ap-east-1`

- [AWS::SSO::PermissionSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html)
  - `me-south-1`
  - `ap-east-1`

- [AWS::DataSync::LocationFSxONTAP.NFS](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-nfs.html)
  - `ap-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `me-south-1`
  - `us-gov-west-1`
  - `eu-west-1`
  - `ap-southeast-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-central-1`
  - `us-gov-east-1`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `ap-southeast-2`
  - `eu-west-2`

- [AWS::DataSync::LocationFSxONTAP.NfsMountOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-nfsmountoptions.html)
  - `ap-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `me-south-1`
  - `us-gov-west-1`
  - `eu-west-1`
  - `ap-southeast-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-central-1`
  - `us-gov-east-1`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `ap-southeast-2`
  - `eu-west-2`

- [AWS::DataSync::LocationFSxONTAP.Protocol](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-protocol.html)
  - `ap-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `me-south-1`
  - `us-gov-west-1`
  - `eu-west-1`
  - `ap-southeast-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-central-1`
  - `us-gov-east-1`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `ap-southeast-2`
  - `eu-west-2`

- [AWS::DataSync::LocationFSxONTAP.SMB](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smb.html)
  - `ap-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `me-south-1`
  - `us-gov-west-1`
  - `eu-west-1`
  - `ap-southeast-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-central-1`
  - `us-gov-east-1`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `ap-southeast-2`
  - `eu-west-2`

- [AWS::DataSync::LocationFSxONTAP.SmbMountOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationfsxontap-smbmountoptions.html)
  - `ap-south-1`
  - `ap-east-1`
  - `sa-east-1`
  - `us-west-2`
  - `ca-central-1`
  - `me-south-1`
  - `us-gov-west-1`
  - `eu-west-1`
  - `ap-southeast-1`
  - `us-east-2`
  - `eu-west-3`
  - `eu-central-1`
  - `us-gov-east-1`
  - `ap-northeast-1`
  - `eu-south-1`
  - `eu-north-1`
  - `ap-southeast-2`
  - `eu-west-2`

- [AWS::EC2::CapacityReservation.TagSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservation-tagspecification.html)
  - Now available to **ALL** regions.

- [AWS::EC2::PrefixList.Entry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-prefixlist-entry.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.ApplicationMaintenanceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationmaintenanceconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.ApplicationRestoreConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationrestoreconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.FlinkRunConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkrunconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.RunConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-runconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::KinesisAnalyticsV2::Application.VpcConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-vpcconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::Logs::MetricFilter.Dimension](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-dimension.html)
  - `eu-west-1`
  - `ap-southeast-1`
  - `us-east-1`
  - `us-west-2`
  - `ap-northeast-1`

- [AWS::QuickSight::DataSet.DataSetUsageConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-quicksight-dataset-datasetusageconfiguration.html)
  - `ap-south-1`
  - `us-east-2`
  - `ap-northeast-2`
  - `sa-east-1`
  - `ca-central-1`
  - `us-gov-west-1`
  - `eu-west-2`

- [AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html)
  - `me-south-1`
  - `ap-east-1`

- [AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttributeValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html)
  - `me-south-1`
  - `ap-east-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v78.1.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v78.1.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v78.1.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v78.1.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v78.1.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v78.1.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- PropertyType Still Missing
  - Since v78.1.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v78.1.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v78.1.0: [AWS::EC2::Subnet.PrivateDnsNameOptionsOnLaunch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-subnet-privatednsnameoptionsonlaunch.html)
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v78.1.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v78.1.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::SageMaker::NotebookInstance.InstanceMetadataServiceConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-notebookinstance-instancemetadataserviceconfiguration.html)
    - `cn-north-1`
    - `eu-central-1`
    - `us-west-2`

  - [AWS::SageMaker::Workteam.OidcMemberDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-oidcmemberdefinition.html)
    - `cn-north-1`
    - `eu-central-1`
    - `us-west-2`

