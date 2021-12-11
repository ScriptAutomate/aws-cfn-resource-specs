# Changelog

This changelog is auto-managed by [`tools/create-changelog.py`](tools/create-changelog.py) with the [`changelogs/v51-changelog.json`](changelogs/v51-changelog.json) data source. All JSON data in [changelogs](changelogs) is generated and managed by [`tools/cfn-changelogger.py`](tools/cfn-changelogger.py)

Changelogs are duplicated to the [changelogs](changelogs) sub-directory with each new major version.

> _**NOTE:** Additional information related to Release History for CloudFormation specifications can be found in the official AWS CloudFormation User Guide documentation: [Release History](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/ReleaseHistory.html)_

## Table of Contents

- [51.0.0](#5100-2021-12-10)
  - [Totals](#totals)
  - [Introduction of New ResourceTypes and/or PropertyTypes](#introduction-of-new-resourcetypes-andor-propertytypes)
  - [Existing ResourceTypes and PropertyTypes: Added Regions](#existing-resourcetypes-and-propertytypes-added-regions)
  - [Existing ResourceTypes and PropertyTypes Not in `us-east-1`](#existing-resourcetypes-and-propertytypes-not-in-us-east-1)

## [51.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v51.0.0) (2021-12-10)

- [ChangeLog Source JSON](https://github.com/ScriptAutomate/aws-cfn-resource-specs/blob/master/changelogs/v51-changelog.json)
  - Change source is a diff between [v51.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v51.0.0) and [v50.0.0](https://github.com/ScriptAutomate/aws-cfn-resource-specs/releases/tag/v50.0.0)

### Totals

- TotalPropertyTypes: 2888 **(+64)**
- TotalPropertyTypesSupportedGlobally: 1013 **(+5)**
- TotalResourceTypes: 868 **(+6)**
- TotalResourceTypesSupportedGlobally: 332 **(+2)**

### Introduction of New ResourceTypes and/or PropertyTypes

- [AWS::AppSync::DomainName](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html)
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

- [AWS::AppSync::DomainNameApiAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainnameapiassociation.html)
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

- [AWS::Lex::Bot](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::BotAlias](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::BotVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botversion.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::ResourcePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-resourcepolicy.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::EC2::ClientVpnEndpoint.ClientLoginBannerOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientloginbanneroptions.html)
  - `eu-north-1`

- [AWS::Lex::Bot.BotLocale](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.Button](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-button.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.CustomPayload](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-custompayload.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.DialogCodeHookSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogcodehooksetting.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.ExternalSourceSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-externalsourcesetting.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.FulfillmentCodeHookSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentcodehooksetting.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.FulfillmentStartResponseSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentstartresponsespecification.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.FulfillmentUpdateResponseSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdateresponsespecification.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.FulfillmentUpdatesSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.GrammarSlotTypeSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesetting.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.GrammarSlotTypeSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesource.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.ImageResponseCard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.InputContext](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-inputcontext.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.Intent](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.IntentClosingSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentclosingsetting.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.IntentConfirmationSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.KendraConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-kendraconfiguration.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.Message](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.MessageGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-messagegroup.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.MultipleValuesSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-multiplevaluessetting.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.ObfuscationSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-obfuscationsetting.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.OutputContext](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-outputcontext.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.PlainTextMessage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-plaintextmessage.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.PostFulfillmentStatusSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.PromptSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.ResponseSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-responsespecification.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.S3Location](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3location.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.SSMLMessage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-ssmlmessage.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.SampleUtterance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-sampleutterance.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.SampleValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-samplevalue.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.Slot](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.SlotDefaultValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotdefaultvalue.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.SlotDefaultValueSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotdefaultvaluespecification.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.SlotPriority](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotpriority.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.SlotType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.SlotTypeValue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottypevalue.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.SlotValueElicitationSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.SlotValueRegexFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueregexfilter.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.SlotValueSelectionSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueselectionsetting.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.StillWaitingResponseSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.VoiceSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-voicesettings.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::Bot.WaitAndContinueSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::BotAlias.AudioLogDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologdestination.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::BotAlias.AudioLogSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologsetting.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::BotAlias.BotAliasLocaleSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettings.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::BotAlias.BotAliasLocaleSettingsItem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettingsitem.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::BotAlias.CloudWatchLogGroupLogDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-cloudwatchloggrouplogdestination.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::BotAlias.CodeHookSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-codehookspecification.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::BotAlias.ConversationLogSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-conversationlogsettings.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::BotAlias.LambdaCodeHook](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-lambdacodehook.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::BotAlias.S3BucketLogDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-s3bucketlogdestination.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::BotAlias.TextLogDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogdestination.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::BotAlias.TextLogSetting](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogsetting.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::BotVersion.BotVersionLocaleDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocaledetails.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::BotVersion.BotVersionLocaleSpecification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocalespecification.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::Lex::ResourcePolicy.Policy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-resourcepolicy-policy.html)
  - `af-south-1`
  - `ap-northeast-1`
  - `ap-northeast-2`
  - `ap-southeast-1`
  - `ap-southeast-2`
  - `ca-central-1`
  - `eu-central-1`
  - `eu-west-1`
  - `eu-west-2`
  - `us-east-1`
  - `us-west-2`

- [AWS::WAFv2::RuleGroup.CaptchaConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-captchaconfig.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::WAFv2::RuleGroup.ImmunityTimeProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-immunitytimeproperty.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::WAFv2::RuleGroup.RegexMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexmatchstatement.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::WAFv2::WebACL.CaptchaAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-captchaaction.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::WAFv2::WebACL.CaptchaConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-captchaconfig.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::WAFv2::WebACL.ImmunityTimeProperty](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-immunitytimeproperty.html)
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
  - `us-west-1`
  - `us-west-2`

- [AWS::WAFv2::WebACL.RegexMatchStatement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexmatchstatement.html)
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
  - `us-west-1`
  - `us-west-2`

### Existing ResourceTypes and PropertyTypes: Added Regions

- [AWS::ElastiCache::User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html)
  - Now available to **ALL** regions.

- [AWS::ElastiCache::UserGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html)
  - Now available to **ALL** regions.

- [AWS::SES::ConfigurationSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html)
  - `ap-northeast-1`

- [AWS::SES::ContactList](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html)
  - `ap-northeast-1`

- [AWS::FSx::FileSystem.ClientConfigurations](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports-clientconfigurations.html)
  - Now available to **ALL** regions.

- [AWS::FSx::FileSystem.NfsExports](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-nfsexports.html)
  - Now available to **ALL** regions.

- [AWS::FSx::FileSystem.OpenZFSConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::FSx::FileSystem.RootVolumeConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration.html)
  - Now available to **ALL** regions.

- [AWS::FSx::FileSystem.UserAndGroupQuotas](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration-userandgroupquotas.html)
  - Now available to **ALL** regions.

- [AWS::Kinesis::Stream.StreamModeDetails](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesis-stream-streammodedetails.html)
  - `ap-southeast-1`
  - `af-south-1`
  - `us-west-2`
  - `cn-northwest-1`
  - `cn-north-1`
  - `ap-northeast-3`
  - `me-south-1`
  - `eu-west-2`
  - `eu-south-1`
  - `ap-southeast-2`
  - `sa-east-1`
  - `us-east-2`
  - `us-east-1`
  - `ap-south-1`
  - `ap-northeast-1`
  - `eu-west-3`
  - `us-west-1`
  - `ap-northeast-2`
  - `eu-north-1`
  - `eu-west-1`
  - `ap-east-1`
  - `ca-central-1`

- [AWS::SES::ContactList.Topic](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html)
  - `ap-northeast-1`

### Existing ResourceTypes and PropertyTypes Not in `us-east-1`

- ResourceType Still Missing
  - Since v50.0.0: [AWS::CloudFormation::HookDefaultVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hookdefaultversion.html)
    - `eu-central-1`

  - Since v50.0.0: [AWS::CloudFormation::HookTypeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-hooktypeconfig.html)
    - `eu-central-1`

  - Since v50.0.0: [AWS::DeviceFarm::DevicePool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-devicepool.html)
    - `us-west-2`

  - Since v50.0.0: [AWS::DeviceFarm::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-instanceprofile.html)
    - `us-west-2`

  - Since v50.0.0: [AWS::DeviceFarm::NetworkProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-networkprofile.html)
    - `us-west-2`

  - Since v50.0.0: [AWS::DeviceFarm::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-project.html)
    - `us-west-2`

  - Since v50.0.0: [AWS::DeviceFarm::TestGridProject](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-testgridproject.html)
    - `us-west-2`

  - Since v50.0.0: [AWS::DeviceFarm::VPCEConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devicefarm-vpceconfiguration.html)
    - `us-west-2`

- PropertyType Still Missing
  - Since v50.0.0: [AWS::DeviceFarm::DevicePool.Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-devicepool-rule.html)
    - `us-west-2`

  - Since v50.0.0: [AWS::DeviceFarm::TestGridProject.VpcConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devicefarm-testgridproject-vpcconfig.html)
    - `us-west-2`

  - Since v50.0.0: [AWS::EC2::LaunchTemplate.InstanceRequirements](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-instancerequirements.html)
    - `sa-east-1`

  - Since v50.0.0: [AWS::Route53::HealthCheck.AlarmIdentifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

  - Since v50.0.0: [AWS::Route53::HealthCheck.HealthCheckConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html)
    - `af-south-1`
    - `cn-north-1`
    - `cn-northwest-1`
    - `eu-south-1`
    - `us-gov-east-1`
    - `us-gov-west-1`

- New PropertyType(s) Missing
  - [AWS::EC2::ClientVpnEndpoint.ClientLoginBannerOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientloginbanneroptions.html)
    - `eu-north-1`

