# WoW Forever add-on API

Generated 2026-11-07 19:58 by `tools/apidoc.py build`. Do not edit by hand.

- Client docs: Blizzard_APIDocumentationGenerated from client 1.60.1.70862
- Game dump: ApiProbe 0.1.2 on 1.60.1.70862 (interface 16001), enUS

Statuses: ✅ verified; 🆕 in game, not in Blizzard's docs; ⛔ in Blizzard's docs, not in game; ❔ unverified

| | Functions | Events | Enums and constants |
|---|---|---|---|
| ✅ verified | 5066 | 1807 | 948 |
| 🆕 in game, not in Blizzard's docs | 5919 | 126 | 1034 |
| ⛔ in Blizzard's docs, not in game | 78 | 136 | 18 |
| ❔ unverified | 0 | 0 | 0 |

Rule: only ✅ and 🆕 were confirmed in game. Flags such as "restricted" or "secret" quoted from Blizzard's docs are leads until a probe call shows them; see [restrictions](restrictions.md) for what the probe saw.

## Pages

- [Events](events.md)
- [Enums and constants](enums.md)
- [Widgets](widgets.md)
- [Undocumented global functions](globals-undocumented.md)
- [Restrictions seen in game](restrictions.md)
- [CVars](cvars.md)
- [Lua environment](lua.md)
- [Changes between dumps](changes/)

## Systems

| System | Namespace | ✅ | 🆕 | ⛔ | ❔ |
|---|---|---|---|---|---|
| [AccountConstants](systems/AccountConstants.md) |  | 0 | 0 | 0 | 0 |
| [AccountInfo](systems/AccountInfo.md) | `C_AccountInfo` | 3 | 0 | 0 | 0 |
| [AccountStore](systems/AccountStore.md) | `C_AccountStore` | 11 | 0 | 0 | 0 |
| [AchievementInfo](systems/AchievementInfo.md) | `C_AchievementInfo` | 6 | 0 | 0 | 0 |
| [AchievementTelemetry](systems/AchievementTelemetry.md) | `C_AchievementTelemetry` | 3 | 0 | 0 | 0 |
| [ActionBar](systems/ActionBar.md) | `C_ActionBar` | 73 | 1 | 0 | 0 |
| [ActionBarShared](systems/ActionBarShared.md) |  | 0 | 0 | 0 | 0 |
| [AddOnConstants](systems/AddOnConstants.md) |  | 0 | 0 | 0 | 0 |
| [AddOnProfiler](systems/AddOnProfiler.md) | `C_AddOnProfiler` | 10 | 0 | 0 | 0 |
| [AddOnProfilerConstants](systems/AddOnProfilerConstants.md) |  | 0 | 0 | 0 | 0 |
| [AddOns](systems/AddOns.md) | `C_AddOns` | 29 | 0 | 0 | 0 |
| [AdventureJournal](systems/AdventureJournal.md) |  | 0 | 0 | 0 | 0 |
| [AdventureMap](systems/AdventureMap.md) | `C_AdventureMap` | 5 | 8 | 0 | 0 |
| [AlliedRaces](systems/AlliedRaces.md) | `C_AlliedRaces` | 2 | 0 | 0 | 0 |
| [AnimaDiversionInfo](systems/AnimaDiversionInfo.md) | `C_AnimaDiversion` | 7 | 0 | 0 | 0 |
| [AppearanceSource](systems/AppearanceSource.md) |  | 0 | 0 | 0 | 0 |
| [ArdenwealdGardening](systems/ArdenwealdGardening.md) | `C_ArdenwealdGardening` | 2 | 0 | 0 | 0 |
| [AreaPoiInfo](systems/AreaPoiInfo.md) | `C_AreaPoiInfo` | 8 | 0 | 0 | 0 |
| [ArrowCalloutConstants](systems/ArrowCalloutConstants.md) |  | 0 | 0 | 0 | 0 |
| [ArtifactUI](systems/ArtifactUI.md) | `C_ArtifactUI` | 62 | 0 | 0 | 0 |
| [AssistedCombat](systems/AssistedCombat.md) | `C_AssistedCombat` | 4 | 0 | 0 | 0 |
| [AsyncAssistActionsConstants](systems/AsyncAssistActionsConstants.md) |  | 0 | 0 | 0 | 0 |
| [AuctionHouse](systems/AuctionHouse.md) | `C_AuctionHouse` | 86 | 0 | 0 | 0 |
| [AuctionHouseConstants](systems/AuctionHouseConstants.md) |  | 0 | 0 | 0 | 0 |
| [AuctionHouseEnums](systems/AuctionHouseEnums.md) |  | 0 | 0 | 0 | 0 |
| [AuraContainerShared](systems/AuraContainerShared.md) |  | 0 | 0 | 0 | 0 |
| [AuraContainerUtil](systems/AuraContainerUtil.md) | `C_AuraContainerUtil` | 10 | 0 | 0 | 0 |
| [AutoComplete](systems/AutoComplete.md) | `C_AutoComplete` | 4 | 0 | 0 | 0 |
| [AutoCompleteShared](systems/AutoCompleteShared.md) |  | 0 | 0 | 0 | 0 |
| [AutoLoot](systems/AutoLoot.md) | `C_AutoLoot` | 1 | 0 | 0 | 0 |
| [AzeriteConstants](systems/AzeriteConstants.md) |  | 0 | 0 | 0 | 0 |
| [AzeriteEmpoweredItem](systems/AzeriteEmpoweredItem.md) | `C_AzeriteEmpoweredItem` | 18 | 0 | 0 | 0 |
| [AzeriteEssence](systems/AzeriteEssence.md) | `C_AzeriteEssence` | 21 | 0 | 0 | 0 |
| [AzeriteItem](systems/AzeriteItem.md) | `C_AzeriteItem` | 10 | 0 | 0 | 0 |
| [BNetOutage](systems/BNetOutage.md) |  | 2 | 0 | 0 | 0 |
| [BagConstants](systems/BagConstants.md) |  | 0 | 0 | 0 | 0 |
| [BagIndexConstants](systems/BagIndexConstants.md) |  | 0 | 0 | 0 | 0 |
| [Bank](systems/Bank.md) | `C_Bank` | 26 | 0 | 0 | 0 |
| [BarberShop](systems/BarberShop.md) | `C_BarberShopInternal` | 29 | 0 | 1 | 0 |
| [Base](systems/Base.md) |  | 0 | 0 | 0 | 0 |
| [BattleNet](systems/BattleNet.md) | `C_BattleNet` | 36 | 0 | 0 | 0 |
| [BattleNetShared](systems/BattleNetShared.md) |  | 0 | 0 | 0 | 0 |
| [BattlePet](systems/BattlePet.md) |  | 0 | 0 | 0 | 0 |
| [BattlePetConstants](systems/BattlePetConstants.md) |  | 0 | 0 | 0 | 0 |
| [BattlepayConstants](systems/BattlepayConstants.md) |  | 0 | 0 | 0 | 0 |
| [BehavioralMessaging](systems/BehavioralMessaging.md) | `C_BehavioralMessaging` | 1 | 0 | 0 | 0 |
| [BlackMarketInfo](systems/BlackMarketInfo.md) |  | 0 | 0 | 0 | 0 |
| [BlizzCon2026Scripts](systems/BlizzCon2026Scripts.md) | `C_BlizzCon2026` | 4 | 0 | 0 | 0 |
| [BountyShared](systems/BountyShared.md) |  | 0 | 0 | 0 | 0 |
| [Browser](systems/Browser.md) | `C_Browser` | 1 | 0 | 0 | 0 |
| [Build](systems/Build.md) |  | 12 | 0 | 0 | 0 |
| [CVarScripts](systems/CVarScripts.md) | `C_CVar` | 12 | 0 | 0 | 0 |
| [C_AccountServices](systems/C_AccountServices.md) | `C_AccountServices` | 0 | 10 | 0 | 0 |
| [C_AdventureJournal](systems/C_AdventureJournal.md) | `C_AdventureJournal` | 0 | 8 | 0 | 0 |
| [C_ArrowCalloutManager](systems/C_ArrowCalloutManager.md) | `C_ArrowCalloutManager` | 0 | 2 | 0 | 0 |
| [C_BlackMarket](systems/C_BlackMarket.md) | `C_BlackMarket` | 0 | 8 | 0 | 0 |
| [C_CharacterServices](systems/C_CharacterServices.md) | `C_CharacterServices` | 0 | 23 | 0 | 0 |
| [C_CharacterServicesPublic](systems/C_CharacterServicesPublic.md) | `C_CharacterServicesPublic` | 0 | 1 | 0 | 0 |
| [C_ClassTrial](systems/C_ClassTrial.md) | `C_ClassTrial` | 0 | 2 | 0 | 0 |
| [C_Debug](systems/C_Debug.md) | `C_Debug` | 0 | 8 | 0 | 0 |
| [C_FunctionContainers](systems/C_FunctionContainers.md) | `C_FunctionContainers` | 0 | 1 | 0 | 0 |
| [C_Heirloom](systems/C_Heirloom.md) | `C_Heirloom` | 0 | 24 | 0 | 0 |
| [C_PrototypeDialog](systems/C_PrototypeDialog.md) | `C_PrototypeDialog` | 0 | 2 | 0 | 0 |
| [C_Reincarnation](systems/C_Reincarnation.md) | `C_Reincarnation` | 0 | 4 | 0 | 0 |
| [C_Scenario](systems/C_Scenario.md) | `C_Scenario` | 0 | 9 | 0 | 0 |
| [C_SharedCharacterServices](systems/C_SharedCharacterServices.md) | `C_SharedCharacterServices` | 0 | 10 | 0 | 0 |
| [C_SpectatingUI](systems/C_SpectatingUI.md) | `C_SpectatingUI` | 0 | 6 | 0 | 0 |
| [C_TalkingHead](systems/C_TalkingHead.md) | `C_TalkingHead` | 0 | 6 | 0 | 0 |
| [C_ToyBox](systems/C_ToyBox.md) | `C_ToyBox` | 0 | 26 | 0 | 0 |
| [C_Trophy](systems/C_Trophy.md) | `C_Trophy` | 0 | 9 | 0 | 0 |
| [C_Widget](systems/C_Widget.md) | `C_Widget` | 0 | 3 | 0 | 0 |
| [C_WoWLabsMatchmaking](systems/C_WoWLabsMatchmaking.md) | `C_WoWLabsMatchmaking` | 0 | 25 | 0 | 0 |
| [C_WowLabsDataManager](systems/C_WowLabsDataManager.md) | `C_WowLabsDataManager` | 0 | 7 | 0 | 0 |
| [C_WowTokenPublic](systems/C_WowTokenPublic.md) | `C_WowTokenPublic` | 0 | 11 | 0 | 0 |
| [Calendar](systems/Calendar.md) | `C_Calendar` | 90 | 0 | 0 | 0 |
| [CalendarConstants](systems/CalendarConstants.md) |  | 0 | 0 | 0 | 0 |
| [Camera](systems/Camera.md) |  | 2 | 0 | 0 | 0 |
| [CameraConstants](systems/CameraConstants.md) |  | 0 | 0 | 0 | 0 |
| [CatalogShop](systems/CatalogShop.md) | `C_CatalogShop` | 38 | 0 | 0 | 0 |
| [CatalogShopConstants](systems/CatalogShopConstants.md) |  | 0 | 0 | 0 | 0 |
| [ChallengeModeInfo](systems/ChallengeModeInfo.md) | `C_ChallengeMode` | 29 | 0 | 0 | 0 |
| [CharacterCreationConstants](systems/CharacterCreationConstants.md) |  | 0 | 0 | 0 | 0 |
| [CharacterCustomizationShared](systems/CharacterCustomizationShared.md) |  | 0 | 0 | 0 | 0 |
| [CharacterSelectionConstants](systems/CharacterSelectionConstants.md) |  | 0 | 0 | 0 | 0 |
| [CharacterServicesConstants](systems/CharacterServicesConstants.md) |  | 0 | 0 | 0 | 0 |
| [ChatBubbles](systems/ChatBubbles.md) | `C_ChatBubbles` | 1 | 0 | 0 | 0 |
| [ChatConstants](systems/ChatConstants.md) |  | 0 | 0 | 0 | 0 |
| [ChatInfo](systems/ChatInfo.md) | `C_ChatInfo` | 45 | 0 | 0 | 0 |
| [ChatShared](systems/ChatShared.md) |  | 0 | 0 | 0 | 0 |
| [ChromieTimeInfo](systems/ChromieTimeInfo.md) | `C_ChromieTime` | 4 | 0 | 0 | 0 |
| [Cinematic](systems/Cinematic.md) |  | 7 | 0 | 0 | 0 |
| [CinematicConstants](systems/CinematicConstants.md) |  | 0 | 0 | 0 | 0 |
| [CinematicList](systems/CinematicList.md) | `C_CinematicList` | 0 | 0 | 1 | 0 |
| [ClassColor](systems/ClassColor.md) | `C_ClassColor` | 1 | 0 | 0 | 0 |
| [ClassTalents](systems/ClassTalents.md) | `C_ClassTalents` | 31 | 0 | 0 | 0 |
| [ClassTrial](systems/ClassTrial.md) |  | 0 | 0 | 0 | 0 |
| [ClickBindings](systems/ClickBindings.md) | `C_ClickBindings` | 9 | 2 | 0 | 0 |
| [ClickBindingsConstants](systems/ClickBindingsConstants.md) |  | 0 | 0 | 0 | 0 |
| [Client](systems/Client.md) |  | 12 | 0 | 0 | 0 |
| [ClientScene](systems/ClientScene.md) | `C_ClientScene` | 1 | 0 | 0 | 0 |
| [ClientSettings](systems/ClientSettings.md) |  | 0 | 0 | 0 | 0 |
| [Club](systems/Club.md) | `C_Club` | 84 | 0 | 0 | 0 |
| [ClubFinderInfo](systems/ClubFinderInfo.md) | `C_ClubFinder` | 55 | 0 | 0 | 0 |
| [ClubShared](systems/ClubShared.md) |  | 0 | 0 | 0 | 0 |
| [ColorOverrideConstants](systems/ColorOverrideConstants.md) |  | 0 | 0 | 0 | 0 |
| [ColorOverrides](systems/ColorOverrides.md) | `C_ColorOverrides` | 6 | 0 | 0 | 0 |
| [ColorUtil](systems/ColorUtil.md) | `C_ColorUtil` | 7 | 0 | 0 | 0 |
| [CombatAudioAlert](systems/CombatAudioAlert.md) | `C_CombatAudioAlert` | 16 | 0 | 0 | 0 |
| [CombatAudioAlertConstants](systems/CombatAudioAlertConstants.md) |  | 0 | 0 | 0 | 0 |
| [CombatAudioAlertShared](systems/CombatAudioAlertShared.md) |  | 0 | 0 | 0 | 0 |
| [CombatLog](systems/CombatLog.md) | `C_CombatLog` | 11 | 0 | 0 | 0 |
| [CombatLogConstants](systems/CombatLogConstants.md) |  | 0 | 0 | 0 | 0 |
| [CombatLogInternal](systems/CombatLogInternal.md) | `C_CombatLogInternal` | 0 | 0 | 1 | 0 |
| [CombatLogSecure](systems/CombatLogSecure.md) | `C_CombatLogSecure` | 0 | 0 | 9 | 0 |
| [CombatLogShared](systems/CombatLogShared.md) |  | 0 | 0 | 0 | 0 |
| [CombatText](systems/CombatText.md) | `C_CombatText` | 3 | 0 | 0 | 0 |
| [CombatTextShared](systems/CombatTextShared.md) |  | 0 | 0 | 0 | 0 |
| [CommentatorFrame](systems/CommentatorFrame.md) | `C_Commentator` | 144 | 0 | 0 | 0 |
| [CommentatorShared](systems/CommentatorShared.md) |  | 0 | 0 | 0 | 0 |
| [CompactUnitFrames](systems/CompactUnitFrames.md) |  | 0 | 0 | 0 | 0 |
| [ConfigurationWarningConstants](systems/ConfigurationWarningConstants.md) |  | 0 | 0 | 0 | 0 |
| [ConfigurationWarnings](systems/ConfigurationWarnings.md) | `C_ConfigurationWarnings` | 0 | 0 | 4 | 0 |
| [ConnectionScript](systems/ConnectionScript.md) |  | 13 | 0 | 0 | 0 |
| [Console](systems/Console.md) |  | 10 | 0 | 0 | 0 |
| [ConsoleScriptCollection](systems/ConsoleScriptCollection.md) | `C_ConsoleScriptCollection` | 4 | 0 | 0 | 0 |
| [Container](systems/Container.md) | `C_Container` | 47 | 0 | 0 | 0 |
| [ContentTracking](systems/ContentTracking.md) | `C_ContentTracking` | 18 | 0 | 0 | 0 |
| [ContentTrackingTypes](systems/ContentTrackingTypes.md) |  | 0 | 0 | 0 | 0 |
| [ContributionCollector](systems/ContributionCollector.md) | `C_ContributionCollector` | 18 | 0 | 0 | 0 |
| [CooldownFrameConstants](systems/CooldownFrameConstants.md) |  | 0 | 0 | 0 | 0 |
| [CooldownViewer](systems/CooldownViewer.md) | `C_CooldownViewer` | 7 | 0 | 0 | 0 |
| [CooldownViewerConstants](systems/CooldownViewerConstants.md) |  | 0 | 0 | 0 | 0 |
| [Covenant](systems/Covenant.md) | `C_Covenants` | 3 | 0 | 0 | 0 |
| [CovenantCallings](systems/CovenantCallings.md) | `C_CovenantCallings` | 2 | 0 | 0 | 0 |
| [CovenantCallingsConstants](systems/CovenantCallingsConstants.md) |  | 0 | 0 | 0 | 0 |
| [CovenantPreview](systems/CovenantPreview.md) | `C_CovenantPreview` | 2 | 0 | 0 | 0 |
| [CovenantSanctumUI](systems/CovenantSanctumUI.md) | `C_CovenantSanctumUI` | 16 | 0 | 0 | 0 |
| [CovenantsConstants](systems/CovenantsConstants.md) |  | 0 | 0 | 0 | 0 |
| [CraftingOrderUI](systems/CraftingOrderUI.md) | `C_CraftingOrders` | 36 | 0 | 0 | 0 |
| [CraftingOrderUIConstants](systems/CraftingOrderUIConstants.md) |  | 0 | 0 | 0 | 0 |
| [CraftingOrderUIShared](systems/CraftingOrderUIShared.md) |  | 0 | 0 | 0 | 0 |
| [CreatureInfo](systems/CreatureInfo.md) | `C_CreatureInfo` | 8 | 0 | 0 | 0 |
| [CurrencyConstants](systems/CurrencyConstants.md) |  | 0 | 0 | 0 | 0 |
| [CurrencyConstants_Mainline](systems/CurrencyConstants_Mainline.md) |  | 0 | 0 | 0 | 0 |
| [CurrencySystem](systems/CurrencySystem.md) | `C_CurrencyInfo` | 43 | 0 | 0 | 0 |
| [Cursor](systems/Cursor.md) | `C_Cursor` | 1 | 0 | 0 | 0 |
| [CursorConst](systems/CursorConst.md) |  | 0 | 0 | 0 | 0 |
| [CursorUtil](systems/CursorUtil.md) |  | 0 | 0 | 0 | 0 |
| [CurveUtil](systems/CurveUtil.md) | `C_CurveUtil` | 5 | 0 | 0 | 0 |
| [DamageConstants](systems/DamageConstants.md) |  | 0 | 0 | 0 | 0 |
| [DamageMeter](systems/DamageMeter.md) | `C_DamageMeter` | 8 | 0 | 0 | 0 |
| [DamageMeterConstants](systems/DamageMeterConstants.md) |  | 0 | 0 | 0 | 0 |
| [DateAndTime](systems/DateAndTime.md) | `C_DateAndTime` | 11 | 0 | 0 | 0 |
| [DeathAlert](systems/DeathAlert.md) |  | 0 | 0 | 0 | 0 |
| [DeathInfo](systems/DeathInfo.md) | `C_DeathInfo` | 5 | 0 | 0 | 0 |
| [DeathRecap](systems/DeathRecap.md) | `C_DeathRecap` | 4 | 0 | 0 | 0 |
| [DeathRecapConstants](systems/DeathRecapConstants.md) |  | 0 | 0 | 0 | 0 |
| [DebugToggle](systems/DebugToggle.md) |  | 0 | 0 | 9 | 0 |
| [DelvesConstants](systems/DelvesConstants.md) |  | 0 | 0 | 0 | 0 |
| [DelvesUI](systems/DelvesUI.md) | `C_DelvesUI` | 40 | 0 | 0 | 0 |
| [Discord](systems/Discord.md) | `C_Discord` | 21 | 0 | 0 | 0 |
| [DiscordConstants](systems/DiscordConstants.md) |  | 0 | 0 | 0 | 0 |
| [DistrictConstants](systems/DistrictConstants.md) |  | 0 | 0 | 0 | 0 |
| [DuelInfo](systems/DuelInfo.md) |  | 0 | 0 | 0 | 0 |
| [DungeonEncounterConstants](systems/DungeonEncounterConstants.md) |  | 0 | 0 | 0 | 0 |
| [DurationTextBindingShared](systems/DurationTextBindingShared.md) |  | 0 | 0 | 0 | 0 |
| [DurationUtil](systems/DurationUtil.md) | `C_DurationUtil` | 3 | 0 | 0 | 0 |
| [DyeColorInfo](systems/DyeColorInfo.md) | `C_DyeColor` | 8 | 2 | 0 | 0 |
| [DyeColorInfoShared](systems/DyeColorInfoShared.md) |  | 0 | 0 | 0 | 0 |
| [EditModeManager](systems/EditModeManager.md) | `C_EditMode` | 12 | 0 | 0 | 0 |
| [EditModeManagerConstants](systems/EditModeManagerConstants.md) |  | 0 | 0 | 0 | 0 |
| [EncodingUtil](systems/EncodingUtil.md) | `C_EncodingUtil` | 10 | 0 | 0 | 0 |
| [EncodingUtilConstants](systems/EncodingUtilConstants.md) |  | 0 | 0 | 0 | 0 |
| [EncounterEvents](systems/EncounterEvents.md) | `C_EncounterEvents` | 8 | 0 | 0 | 0 |
| [EncounterEventsShared](systems/EncounterEventsShared.md) |  | 0 | 0 | 0 | 0 |
| [EncounterInfo](systems/EncounterInfo.md) |  | 0 | 0 | 0 | 0 |
| [EncounterJournal](systems/EncounterJournal.md) | `C_EncounterJournal` | 22 | 0 | 0 | 0 |
| [EncounterJournalConstants](systems/EncounterJournalConstants.md) |  | 0 | 0 | 0 | 0 |
| [EncounterTimeline](systems/EncounterTimeline.md) | `C_EncounterTimeline` | 34 | 0 | 0 | 0 |
| [EncounterTimelineConstants](systems/EncounterTimelineConstants.md) |  | 0 | 0 | 0 | 0 |
| [EncounterWarnings](systems/EncounterWarnings.md) | `C_EncounterWarnings` | 10 | 0 | 0 | 0 |
| [EndOfMatchUI](systems/EndOfMatchUI.md) | `C_EndOfMatchUI` | 1 | 0 | 0 | 0 |
| [EquipmentSet](systems/EquipmentSet.md) | `C_EquipmentSet` | 23 | 0 | 0 | 0 |
| [EventSchedulerConstants](systems/EventSchedulerConstants.md) |  | 0 | 0 | 0 | 0 |
| [EventSchedulerUI](systems/EventSchedulerUI.md) | `C_EventScheduler` | 11 | 0 | 0 | 0 |
| [EventUtils](systems/EventUtils.md) | `C_EventUtils` | 2 | 0 | 0 | 0 |
| [Expansion](systems/Expansion.md) |  | 24 | 0 | 0 | 0 |
| [ExpansionConstants](systems/ExpansionConstants.md) |  | 0 | 0 | 0 | 0 |
| [ExpansionInfo](systems/ExpansionInfo.md) |  | 3 | 0 | 0 | 0 |
| [ExpansionLandingPageConstants](systems/ExpansionLandingPageConstants.md) |  | 0 | 0 | 0 | 0 |
| [ExpansionLevelConstants](systems/ExpansionLevelConstants.md) |  | 0 | 0 | 0 | 0 |
| [ExpansionTrial](systems/ExpansionTrial.md) | `C_ExpansionTrial` | 2 | 0 | 0 | 0 |
| [ExternalEventURL](systems/ExternalEventURL.md) | `C_ExternalEventURL` | 4 | 0 | 0 | 0 |
| [Flyout](systems/Flyout.md) | `C_Flyout` | 6 | 0 | 0 | 0 |
| [FogOfWar](systems/FogOfWar.md) | `C_FogOfWar` | 2 | 0 | 0 | 0 |
| [Font](systems/Font.md) |  | 3 | 0 | 0 | 0 |
| [ForbiddenAspectConstants](systems/ForbiddenAspectConstants.md) |  | 0 | 0 | 0 | 0 |
| [FrameAPIModelSceneFrameShared](systems/FrameAPIModelSceneFrameShared.md) |  | 0 | 0 | 0 | 0 |
| [FrameScript](systems/FrameScript.md) |  | 35 | 0 | 3 | 0 |
| [FriendList](systems/FriendList.md) | `C_FriendList` | 32 | 0 | 0 | 0 |
| [GARRISON_FOLLOWER_TYPEConstants](systems/GARRISON_FOLLOWER_TYPEConstants.md) |  | 0 | 0 | 0 | 0 |
| [GARRISON_TYPEConstants](systems/GARRISON_TYPEConstants.md) |  | 0 | 0 | 0 | 0 |
| [GMTicketInfo](systems/GMTicketInfo.md) |  | 0 | 0 | 0 | 0 |
| [GameCursor](systems/GameCursor.md) |  | 19 | 0 | 0 | 0 |
| [GameError](systems/GameError.md) |  | 2 | 0 | 0 | 0 |
| [GamePad](systems/GamePad.md) | `C_GamePad` | 25 | 0 | 0 | 0 |
| [GamePadConst](systems/GamePadConst.md) |  | 0 | 0 | 0 | 0 |
| [GameRules](systems/GameRules.md) | `C_GameRules` | 30 | 0 | 0 | 0 |
| [GameRulesConstants](systems/GameRulesConstants.md) |  | 0 | 0 | 0 | 0 |
| [GameUI](systems/GameUI.md) |  | 2 | 0 | 0 | 0 |
| [GamepadTargetingManager](systems/GamepadTargetingManager.md) | `C_GamepadTargeting` | 3 | 0 | 0 | 0 |
| [GamepadUI](systems/GamepadUI.md) | `C_GamepadUI` | 5 | 0 | 0 | 0 |
| [GarrisonConstants](systems/GarrisonConstants.md) |  | 0 | 0 | 0 | 0 |
| [GarrisonInfo](systems/GarrisonInfo.md) | `C_Garrison` | 40 | 187 | 0 | 0 |
| [GarrisonShared](systems/GarrisonShared.md) |  | 0 | 0 | 0 | 0 |
| [GenericWidgetDisplay](systems/GenericWidgetDisplay.md) | `C_GenericWidgetDisplay` | 2 | 0 | 0 | 0 |
| [Glue](systems/Glue.md) | `C_Glue` | 2 | 0 | 0 | 0 |
| [GlyphInfo](systems/GlyphInfo.md) |  | 0 | 0 | 0 | 0 |
| [GossipConstants](systems/GossipConstants.md) |  | 0 | 0 | 0 | 0 |
| [GossipInfo](systems/GossipInfo.md) | `C_GossipInfo` | 20 | 0 | 0 | 0 |
| [GuildBank](systems/GuildBank.md) | `C_GuildBank` | 1 | 0 | 0 | 0 |
| [GuildConstants](systems/GuildConstants.md) |  | 0 | 0 | 0 | 0 |
| [GuildInfo](systems/GuildInfo.md) | `C_GuildInfo` | 39 | 0 | 0 | 0 |
| [GuildInfoShared](systems/GuildInfoShared.md) |  | 0 | 0 | 0 | 0 |
| [HeirloomInfo](systems/HeirloomInfo.md) | `C_HeirloomInfo` | 8 | 0 | 0 | 0 |
| [HouseEditorUI](systems/HouseEditorUI.md) | `C_HouseEditor` | 10 | 0 | 0 | 0 |
| [HouseExteriorConstants](systems/HouseExteriorConstants.md) |  | 0 | 0 | 0 | 0 |
| [HouseExteriorUI](systems/HouseExteriorUI.md) | `C_HouseExterior` | 20 | 3 | 0 | 0 |
| [HousingBasicModeUI](systems/HousingBasicModeUI.md) | `C_HousingBasicMode` | 22 | 0 | 0 | 0 |
| [HousingBlueprintConstants](systems/HousingBlueprintConstants.md) |  | 0 | 0 | 0 | 0 |
| [HousingBlueprintUI](systems/HousingBlueprintUI.md) | `C_HousingBlueprint` | 19 | 0 | 0 | 0 |
| [HousingCatalogConstants](systems/HousingCatalogConstants.md) |  | 0 | 0 | 0 | 0 |
| [HousingCatalogSearcherAPI](systems/HousingCatalogSearcherAPI.md) |  | 0 | 0 | 0 | 0 |
| [HousingCatalogUI](systems/HousingCatalogUI.md) | `C_HousingCatalog` | 34 | 3 | 0 | 0 |
| [HousingCleanupModeUI](systems/HousingCleanupModeUI.md) | `C_HousingCleanupMode` | 3 | 0 | 0 | 0 |
| [HousingCustomizeModeUI](systems/HousingCustomizeModeUI.md) | `C_HousingCustomizeMode` | 32 | 0 | 0 | 0 |
| [HousingDecorShared](systems/HousingDecorShared.md) |  | 0 | 0 | 0 | 0 |
| [HousingDecorUI](systems/HousingDecorUI.md) | `C_HousingDecor` | 35 | 3 | 0 | 0 |
| [HousingExpertModeUI](systems/HousingExpertModeUI.md) | `C_HousingExpertMode` | 18 | 0 | 0 | 0 |
| [HousingFixturePointFrameAPI](systems/HousingFixturePointFrameAPI.md) |  | 0 | 0 | 0 | 0 |
| [HousingInspectModeUI](systems/HousingInspectModeUI.md) | `C_HousingInspectMode` | 5 | 0 | 0 | 0 |
| [HousingLayoutUI](systems/HousingLayoutUI.md) | `C_HousingLayout` | 41 | 1 | 0 | 0 |
| [HousingLayoutUITypes](systems/HousingLayoutUITypes.md) |  | 0 | 0 | 0 | 0 |
| [HousingNeighborhoodUI](systems/HousingNeighborhoodUI.md) | `C_HousingNeighborhood` | 30 | 0 | 0 | 0 |
| [HousingUI](systems/HousingUI.md) | `C_Housing` | 62 | 1 | 0 | 0 |
| [HousingUIShared](systems/HousingUIShared.md) |  | 0 | 0 | 0 | 0 |
| [ImageSharingConstants](systems/ImageSharingConstants.md) |  | 0 | 0 | 0 | 0 |
| [ImmersiveInteraction](systems/ImmersiveInteraction.md) | `C_ImmersiveInteraction` | 1 | 0 | 0 | 0 |
| [InGameNavigation](systems/InGameNavigation.md) | `C_Navigation` | 7 | 0 | 0 | 0 |
| [IncomingSummon](systems/IncomingSummon.md) | `C_IncomingSummon` | 2 | 0 | 0 | 0 |
| [Input](systems/Input.md) |  | 31 | 0 | 0 | 0 |
| [InputConstants](systems/InputConstants.md) |  | 0 | 0 | 0 | 0 |
| [InputInterfaceStyle](systems/InputInterfaceStyle.md) | `C_InputInterfaceStyle` | 1 | 0 | 0 | 0 |
| [Instance](systems/Instance.md) |  | 18 | 0 | 0 | 0 |
| [InstanceEncounter](systems/InstanceEncounter.md) | `C_InstanceEncounter` | 4 | 0 | 0 | 0 |
| [InstanceLeaverInfo](systems/InstanceLeaverInfo.md) | `C_InstanceLeaver` | 1 | 0 | 0 | 0 |
| [InterfaceFileManifest](systems/InterfaceFileManifest.md) | `C_InterfaceFileManifest` | 1 | 0 | 0 | 0 |
| [Intl](systems/Intl.md) | `C_Intl` | 27 | 0 | 0 | 0 |
| [IntlSharedTypes](systems/IntlSharedTypes.md) |  | 0 | 0 | 0 | 0 |
| [InvasionInfo](systems/InvasionInfo.md) | `C_InvasionInfo` | 4 | 0 | 0 | 0 |
| [IslandsInfo](systems/IslandsInfo.md) |  | 0 | 0 | 0 | 0 |
| [IslandsQueue](systems/IslandsQueue.md) | `C_IslandsQueue` | 6 | 0 | 0 | 0 |
| [Item](systems/Item.md) | `C_Item` | 121 | 0 | 0 | 0 |
| [ItemConstants](systems/ItemConstants.md) |  | 0 | 0 | 0 | 0 |
| [ItemConstants_Mainline](systems/ItemConstants_Mainline.md) |  | 0 | 0 | 0 | 0 |
| [ItemInteractionUI](systems/ItemInteractionUI.md) | `C_ItemInteraction` | 10 | 0 | 0 | 0 |
| [ItemQualities](systems/ItemQualities.md) |  | 0 | 0 | 0 | 0 |
| [ItemSocketInfo](systems/ItemSocketInfo.md) | `C_ItemSocketInfo` | 16 | 0 | 0 | 0 |
| [ItemText](systems/ItemText.md) |  | 0 | 0 | 0 | 0 |
| [ItemUpgrade](systems/ItemUpgrade.md) | `C_ItemUpgrade` | 16 | 0 | 0 | 0 |
| [KeyBindings](systems/KeyBindings.md) | `C_KeyBindings` | 11 | 0 | 0 | 0 |
| [LFGConstants](systems/LFGConstants.md) |  | 0 | 0 | 0 | 0 |
| [LFGInfo](systems/LFGInfo.md) | `C_LFGInfo` | 23 | 0 | 0 | 0 |
| [LFGList](systems/LFGList.md) | `C_LFGList` | 52 | 36 | 0 | 0 |
| [LFGListRoles](systems/LFGListRoles.md) | `C_LFGListRoles` | 3 | 0 | 0 | 0 |
| [LegacyConstants](systems/LegacyConstants.md) |  | 0 | 0 | 0 | 0 |
| [LegendaryCrafting](systems/LegendaryCrafting.md) | `C_LegendaryCrafting` | 20 | 0 | 0 | 0 |
| [LegendaryCraftingTypes](systems/LegendaryCraftingTypes.md) |  | 0 | 0 | 0 | 0 |
| [LevelConstants](systems/LevelConstants.md) |  | 0 | 0 | 0 | 0 |
| [LevelLink](systems/LevelLink.md) | `C_LevelLink` | 2 | 0 | 0 | 0 |
| [LevelSquish](systems/LevelSquish.md) | `C_LevelSquish` | 2 | 0 | 0 | 0 |
| [LimitedInput](systems/LimitedInput.md) | `C_LimitedInput` | 1 | 0 | 0 | 0 |
| [LiveEvent](systems/LiveEvent.md) | `C_LiveEvent` | 0 | 0 | 2 | 0 |
| [LoadingScreen](systems/LoadingScreen.md) |  | 0 | 0 | 0 | 0 |
| [LobbyMatchmakerInfo](systems/LobbyMatchmakerInfo.md) | `C_LobbyMatchmakerInfo` | 8 | 0 | 0 | 0 |
| [Locale](systems/Locale.md) |  | 5 | 0 | 0 | 0 |
| [Localization](systems/Localization.md) |  | 10 | 0 | 1 | 0 |
| [LocalizationShared](systems/LocalizationShared.md) |  | 0 | 0 | 0 | 0 |
| [Log](systems/Log.md) | `C_Log` | 4 | 0 | 0 | 0 |
| [LogConstants](systems/LogConstants.md) |  | 0 | 0 | 0 | 0 |
| [LogicConstants](systems/LogicConstants.md) |  | 0 | 0 | 0 | 0 |
| [Loot](systems/Loot.md) | `C_Loot` | 2 | 0 | 0 | 0 |
| [LootConstants](systems/LootConstants.md) |  | 0 | 0 | 0 | 0 |
| [LootConstants_Mainline](systems/LootConstants_Mainline.md) |  | 0 | 0 | 0 | 0 |
| [LootFrame](systems/LootFrame.md) | `C_LootFrame` | 1 | 0 | 0 | 0 |
| [LootHistory](systems/LootHistory.md) | `C_LootHistory` | 5 | 0 | 0 | 0 |
| [LootJournal](systems/LootJournal.md) | `C_LootJournal` | 2 | 0 | 0 | 0 |
| [LoreText](systems/LoreText.md) | `C_LoreText` | 1 | 0 | 0 | 0 |
| [LossOfControl](systems/LossOfControl.md) | `C_LossOfControl` | 5 | 0 | 0 | 0 |
| [LossOfControlConstants](systems/LossOfControlConstants.md) |  | 0 | 0 | 0 | 0 |
| [LuaColorCurveObjectAPI](systems/LuaColorCurveObjectAPI.md) |  | 0 | 0 | 0 | 0 |
| [LuaCurveObjectConstants](systems/LuaCurveObjectConstants.md) |  | 0 | 0 | 0 | 0 |
| [LuaDurationObjectShared](systems/LuaDurationObjectShared.md) |  | 0 | 0 | 0 | 0 |
| [LuaMathExtensions](systems/LuaMathExtensions.md) | `math` | 11 | 0 | 0 | 0 |
| [LuaStringExtensions](systems/LuaStringExtensions.md) | `string` | 6 | 0 | 0 | 0 |
| [LuaTableExtensions](systems/LuaTableExtensions.md) | `table` | 12 | 0 | 0 | 0 |
| [MacOptions](systems/MacOptions.md) | `C_MacOptions` | 0 | 0 | 10 | 0 |
| [MacroConstants](systems/MacroConstants.md) |  | 0 | 0 | 0 | 0 |
| [MailInfo](systems/MailInfo.md) | `C_Mail` | 5 | 0 | 0 | 0 |
| [MajorFactionsConstants](systems/MajorFactionsConstants.md) |  | 0 | 0 | 0 | 0 |
| [MajorFactionsUI](systems/MajorFactionsUI.md) | `C_MajorFactions` | 14 | 0 | 0 | 0 |
| [MapConstants](systems/MapConstants.md) |  | 0 | 0 | 0 | 0 |
| [MapExplorationInfo](systems/MapExplorationInfo.md) | `C_MapExplorationInfo` | 2 | 0 | 0 | 0 |
| [MapUI](systems/MapUI.md) | `C_Map` | 40 | 0 | 0 | 0 |
| [MerchantFrame](systems/MerchantFrame.md) | `C_MerchantFrame` | 7 | 0 | 0 | 0 |
| [Minimap](systems/Minimap.md) | `C_Minimap` | 23 | 0 | 0 | 0 |
| [MinimapConstants](systems/MinimapConstants.md) |  | 0 | 0 | 0 | 0 |
| [MirrorTimer](systems/MirrorTimer.md) |  | 2 | 0 | 0 | 0 |
| [ModelAnimationShared](systems/ModelAnimationShared.md) |  | 0 | 0 | 0 | 0 |
| [ModelInfo](systems/ModelInfo.md) | `C_ModelInfo` | 8 | 0 | 0 | 0 |
| [MoneyConstants](systems/MoneyConstants.md) |  | 0 | 0 | 0 | 0 |
| [MountConstants](systems/MountConstants.md) |  | 0 | 0 | 0 | 0 |
| [MountJournal](systems/MountJournal.md) | `C_MountJournal` | 50 | 0 | 0 | 0 |
| [Movie](systems/Movie.md) |  | 6 | 0 | 0 | 0 |
| [MythicPlusInfo](systems/MythicPlusInfo.md) | `C_MythicPlus` | 21 | 0 | 0 | 0 |
| [MythicPlusInfoShared](systems/MythicPlusInfoShared.md) |  | 0 | 0 | 0 | 0 |
| [NameGenConstants](systems/NameGenConstants.md) |  | 0 | 0 | 0 | 0 |
| [NamePlate](systems/NamePlate.md) | `C_NamePlate` | 4 | 0 | 0 | 0 |
| [NamePlateConstants](systems/NamePlateConstants.md) |  | 0 | 0 | 0 | 0 |
| [NamePlateManager](systems/NamePlateManager.md) | `C_NamePlateManager` | 4 | 0 | 0 | 0 |
| [NameUtil](systems/NameUtil.md) | `C_NameUtil` | 1 | 0 | 0 | 0 |
| [NeighborhoodInitiative](systems/NeighborhoodInitiative.md) | `C_NeighborhoodInitiative` | 20 | 0 | 0 | 0 |
| [NeighborhoodInitiativesConstants](systems/NeighborhoodInitiativesConstants.md) |  | 0 | 0 | 0 | 0 |
| [NewItems](systems/NewItems.md) | `C_NewItems` | 3 | 0 | 0 | 0 |
| [NumericRuleFormatterShared](systems/NumericRuleFormatterShared.md) |  | 0 | 0 | 0 | 0 |
| [Os](systems/Os.md) |  | 2 | 0 | 0 | 0 |
| [PVPMgrConstants](systems/PVPMgrConstants.md) |  | 0 | 0 | 0 | 0 |
| [PaperDollInfo](systems/PaperDollInfo.md) | `C_PaperDollInfo` | 21 | 0 | 0 | 0 |
| [ParentalControls](systems/ParentalControls.md) |  | 1 | 0 | 0 | 0 |
| [PartyConstants](systems/PartyConstants.md) |  | 0 | 0 | 0 | 0 |
| [PartyInfo](systems/PartyInfo.md) | `C_PartyInfo` | 53 | 0 | 0 | 0 |
| [PartyInfoSystemStatus](systems/PartyInfoSystemStatus.md) | `C_PartyInfo` | 2 | 0 | 0 | 0 |
| [PartyPose](systems/PartyPose.md) | `C_PartyPose` | 4 | 0 | 0 | 0 |
| [PartyPoseUIConstants](systems/PartyPoseUIConstants.md) |  | 0 | 0 | 0 | 0 |
| [PerformanceScript](systems/PerformanceScript.md) |  | 9 | 0 | 0 | 0 |
| [PerksActivities](systems/PerksActivities.md) | `C_PerksActivities` | 10 | 0 | 0 | 0 |
| [PerksProgram](systems/PerksProgram.md) | `C_PerksProgram` | 24 | 0 | 0 | 0 |
| [PerksVendorConstants](systems/PerksVendorConstants.md) |  | 0 | 0 | 0 | 0 |
| [PetBattleConstants](systems/PetBattleConstants.md) |  | 0 | 0 | 0 | 0 |
| [PetBattles](systems/PetBattles.md) | `C_PetBattles` | 5 | 51 | 0 | 0 |
| [PetConstants](systems/PetConstants.md) |  | 0 | 0 | 0 | 0 |
| [PetConstants_Shared](systems/PetConstants_Shared.md) |  | 0 | 0 | 0 | 0 |
| [PetInfo](systems/PetInfo.md) | `C_PetInfo` | 14 | 0 | 0 | 0 |
| [PetJournalInfo](systems/PetJournalInfo.md) | `C_PetJournal` | 25 | 55 | 0 | 0 |
| [PhotoSharingUI](systems/PhotoSharingUI.md) | `C_PhotoSharing` | 11 | 0 | 0 | 0 |
| [PingConstants](systems/PingConstants.md) |  | 0 | 0 | 0 | 0 |
| [PingManager](systems/PingManager.md) | `C_Ping` | 6 | 0 | 0 | 0 |
| [PingManagerSecure](systems/PingManagerSecure.md) | `C_PingSecure` | 0 | 0 | 19 | 0 |
| [PingManagerShared](systems/PingManagerShared.md) |  | 0 | 0 | 0 | 0 |
| [Platform](systems/Platform.md) |  | 0 | 0 | 0 | 0 |
| [PlayerChoice](systems/PlayerChoice.md) | `C_PlayerChoice` | 7 | 0 | 0 | 0 |
| [PlayerChoiceConstants](systems/PlayerChoiceConstants.md) |  | 0 | 0 | 0 | 0 |
| [PlayerDataConstants](systems/PlayerDataConstants.md) |  | 0 | 0 | 0 | 0 |
| [PlayerHousingConstants](systems/PlayerHousingConstants.md) |  | 0 | 0 | 0 | 0 |
| [PlayerInfo](systems/PlayerInfo.md) | `C_PlayerInfo` | 33 | 0 | 0 | 0 |
| [PlayerInfoShared](systems/PlayerInfoShared.md) |  | 0 | 0 | 0 | 0 |
| [PlayerInteractionManager](systems/PlayerInteractionManager.md) | `C_PlayerInteractionManager` | 8 | 0 | 0 | 0 |
| [PlayerInteractionManagerConstants](systems/PlayerInteractionManagerConstants.md) |  | 0 | 0 | 0 | 0 |
| [PlayerLocationInfo](systems/PlayerLocationInfo.md) | `C_PlayerInfo` | 7 | 0 | 0 | 0 |
| [PlayerMentorship](systems/PlayerMentorship.md) | `C_PlayerMentorship` | 5 | 0 | 0 | 0 |
| [PlayerMentorshipConstants](systems/PlayerMentorshipConstants.md) |  | 0 | 0 | 0 | 0 |
| [PlayerScript](systems/PlayerScript.md) |  | 190 | 0 | 0 | 0 |
| [PowerTypeConstants](systems/PowerTypeConstants.md) |  | 0 | 0 | 0 | 0 |
| [ProceduralSpawnConstants](systems/ProceduralSpawnConstants.md) |  | 0 | 0 | 0 | 0 |
| [ProfessionConstants](systems/ProfessionConstants.md) |  | 0 | 0 | 0 | 0 |
| [ProfessionSpecConstants](systems/ProfessionSpecConstants.md) |  | 0 | 0 | 0 | 0 |
| [ProfessionSpecUI](systems/ProfessionSpecUI.md) | `C_ProfSpecs` | 27 | 0 | 0 | 0 |
| [PvPFactionConstants](systems/PvPFactionConstants.md) |  | 0 | 0 | 0 | 0 |
| [PvpInfo](systems/PvpInfo.md) | `C_PvP` | 113 | 0 | 1 | 0 |
| [PvpInfoConstants](systems/PvpInfoConstants.md) |  | 0 | 0 | 0 | 0 |
| [QuestConstants](systems/QuestConstants.md) |  | 0 | 0 | 0 | 0 |
| [QuestHubUI](systems/QuestHubUI.md) | `C_QuestHub` | 2 | 0 | 0 | 0 |
| [QuestInfoShared](systems/QuestInfoShared.md) |  | 0 | 0 | 0 | 0 |
| [QuestInfoSystem](systems/QuestInfoSystem.md) | `C_QuestInfoSystem` | 9 | 0 | 0 | 0 |
| [QuestItemUse](systems/QuestItemUse.md) | `C_QuestItemUse` | 1 | 0 | 0 | 0 |
| [QuestLineUI](systems/QuestLineUI.md) | `C_QuestLine` | 7 | 0 | 0 | 0 |
| [QuestLog](systems/QuestLog.md) | `C_QuestLog` | 93 | 0 | 0 | 0 |
| [QuestOffer](systems/QuestOffer.md) | `C_QuestOffer` | 4 | 0 | 0 | 0 |
| [QuestRewards](systems/QuestRewards.md) |  | 0 | 0 | 0 | 0 |
| [QuestSession](systems/QuestSession.md) | `C_QuestSession` | 14 | 0 | 0 | 0 |
| [QuestSessionConstants](systems/QuestSessionConstants.md) |  | 0 | 0 | 0 | 0 |
| [QuestTaskInfo](systems/QuestTaskInfo.md) | `C_TaskQuest` | 12 | 0 | 0 | 0 |
| [QueueSpecific](systems/QueueSpecific.md) |  | 0 | 0 | 0 | 0 |
| [RaidLocks](systems/RaidLocks.md) | `C_RaidLocks` | 4 | 0 | 0 | 0 |
| [RaidMarkerConstants](systems/RaidMarkerConstants.md) |  | 0 | 0 | 0 | 0 |
| [RaidMarkers](systems/RaidMarkers.md) |  | 9 | 0 | 0 | 0 |
| [RecentAllies](systems/RecentAllies.md) | `C_RecentAllies` | 15 | 0 | 0 | 0 |
| [RecentAlliesConstants](systems/RecentAlliesConstants.md) |  | 0 | 0 | 0 | 0 |
| [RecruitAFriend](systems/RecruitAFriend.md) | `C_RecruitAFriend` | 16 | 0 | 0 | 0 |
| [RecruitAFriendShared](systems/RecruitAFriendShared.md) |  | 0 | 0 | 0 | 0 |
| [RemixArtifactUI](systems/RemixArtifactUI.md) | `C_RemixArtifactUI` | 8 | 0 | 0 | 0 |
| [RenownConstants](systems/RenownConstants.md) |  | 0 | 0 | 0 | 0 |
| [ReportSystem](systems/ReportSystem.md) | `C_ReportSystem` | 12 | 0 | 0 | 0 |
| [ReportSystemConstants](systems/ReportSystemConstants.md) |  | 0 | 0 | 0 | 0 |
| [ReputationInfo](systems/ReputationInfo.md) | `C_Reputation` | 27 | 0 | 0 | 0 |
| [ResearchInfo](systems/ResearchInfo.md) | `C_ResearchInfo` | 1 | 0 | 0 | 0 |
| [RestrictedActions](systems/RestrictedActions.md) | `C_RestrictedActions` | 3 | 0 | 1 | 0 |
| [RestrictedActionsConstants](systems/RestrictedActionsConstants.md) |  | 0 | 0 | 0 | 0 |
| [RolesetSystem](systems/RolesetSystem.md) | `C_Roleset` | 3 | 0 | 0 | 0 |
| [RolodexConstants](systems/RolodexConstants.md) |  | 0 | 0 | 0 | 0 |
| [ScenarioInfo](systems/ScenarioInfo.md) | `C_ScenarioInfo` | 10 | 0 | 0 | 0 |
| [ScrappingMachineUI](systems/ScrappingMachineUI.md) | `C_ScrappingMachineUI` | 11 | 0 | 0 | 0 |
| [Screen](systems/Screen.md) |  | 5 | 0 | 0 | 0 |
| [ScreenLocationConstants](systems/ScreenLocationConstants.md) |  | 0 | 0 | 0 | 0 |
| [ScriptWarnings](systems/ScriptWarnings.md) |  | 0 | 0 | 0 | 0 |
| [ScriptedAnimations](systems/ScriptedAnimations.md) | `C_ScriptedAnimations` | 1 | 0 | 0 | 0 |
| [SeasonInfo](systems/SeasonInfo.md) | `C_SeasonInfo` | 3 | 0 | 0 | 0 |
| [SeasonsConstants](systems/SeasonsConstants.md) |  | 0 | 0 | 0 | 0 |
| [SecondsFormatterShared](systems/SecondsFormatterShared.md) |  | 0 | 0 | 0 | 0 |
| [SecretAspectConstants](systems/SecretAspectConstants.md) |  | 0 | 0 | 0 | 0 |
| [SecretUtil](systems/SecretUtil.md) | `C_Secrets` | 27 | 0 | 0 | 0 |
| [SecretWrapperConstants](systems/SecretWrapperConstants.md) |  | 0 | 0 | 0 | 0 |
| [SecureTransfer](systems/SecureTransfer.md) | `C_SecureTransfer` | 0 | 0 | 14 | 0 |
| [SettingsUtil](systems/SettingsUtil.md) | `C_SettingsUtil` | 2 | 0 | 0 | 0 |
| [SharedScriptObjectModelLight](systems/SharedScriptObjectModelLight.md) |  | 0 | 0 | 0 | 0 |
| [SharedScriptObjectUnitPositionFrame](systems/SharedScriptObjectUnitPositionFrame.md) |  | 0 | 0 | 0 | 0 |
| [SharedTraits](systems/SharedTraits.md) | `C_Traits` | 53 | 0 | 0 | 0 |
| [SimpleFrameAPI](systems/SimpleFrameAPI.md) |  | 0 | 0 | 0 | 0 |
| [SimpleFrameScriptObjectConstants](systems/SimpleFrameScriptObjectConstants.md) |  | 0 | 0 | 0 | 0 |
| [SimpleHTMLShared](systems/SimpleHTMLShared.md) |  | 0 | 0 | 0 | 0 |
| [SimpleStatusBarConstants](systems/SimpleStatusBarConstants.md) |  | 0 | 0 | 0 | 0 |
| [SkillInfo](systems/SkillInfo.md) | `C_SkillInfo` | 8 | 0 | 0 | 0 |
| [SlashCommand](systems/SlashCommand.md) |  | 2 | 0 | 0 | 0 |
| [SocialConstants](systems/SocialConstants.md) |  | 0 | 0 | 0 | 0 |
| [SocialQueue](systems/SocialQueue.md) | `C_SocialQueue` | 8 | 0 | 0 | 0 |
| [SocialQueueSystemStatus](systems/SocialQueueSystemStatus.md) | `C_SocialQueue` | 2 | 0 | 0 | 0 |
| [SocialRestrictions](systems/SocialRestrictions.md) | `C_SocialRestrictions` | 12 | 0 | 0 | 0 |
| [SocialUI](systems/SocialUI.md) | `C_SocialUI` | 1 | 0 | 0 | 0 |
| [SoftTargetConstants](systems/SoftTargetConstants.md) |  | 0 | 0 | 0 | 0 |
| [Soulbinds](systems/Soulbinds.md) | `C_Soulbinds` | 39 | 0 | 0 | 0 |
| [SoulbindsConstants](systems/SoulbindsConstants.md) |  | 0 | 0 | 0 | 0 |
| [Sound](systems/Sound.md) | `C_Sound` | 6 | 0 | 0 | 0 |
| [SpecializationConstants](systems/SpecializationConstants.md) |  | 0 | 0 | 0 | 0 |
| [SpecializationInfo](systems/SpecializationInfo.md) | `C_SpecializationInfo` | 31 | 0 | 0 | 0 |
| [SpecializationShared](systems/SpecializationShared.md) |  | 5 | 0 | 0 | 0 |
| [Spell](systems/Spell.md) | `C_Spell` | 71 | 2 | 0 | 0 |
| [SpellActivationOverlay](systems/SpellActivationOverlay.md) | `C_SpellActivationOverlay` | 1 | 0 | 0 | 0 |
| [SpellBook](systems/SpellBook.md) | `C_SpellBook` | 51 | 1 | 0 | 0 |
| [SpellBookConstants](systems/SpellBookConstants.md) |  | 0 | 0 | 0 | 0 |
| [SpellConstants](systems/SpellConstants.md) |  | 0 | 0 | 0 | 0 |
| [SpellDiminishConstants](systems/SpellDiminishConstants.md) |  | 0 | 0 | 0 | 0 |
| [SpellDiminishUI](systems/SpellDiminishUI.md) | `C_SpellDiminish` | 4 | 0 | 0 | 0 |
| [SpellID](systems/SpellID.md) |  | 0 | 0 | 0 | 0 |
| [SpellShared](systems/SpellShared.md) |  | 0 | 0 | 0 | 0 |
| [SplashScreen](systems/SplashScreen.md) | `C_SplashScreen` | 5 | 0 | 0 | 0 |
| [SplashScreenConstants](systems/SplashScreenConstants.md) |  | 0 | 0 | 0 | 0 |
| [StableInfo](systems/StableInfo.md) | `C_StableInfo` | 17 | 0 | 0 | 0 |
| [StorePublic](systems/StorePublic.md) | `C_StorePublic` | 3 | 0 | 0 | 0 |
| [Streaming](systems/Streaming.md) |  | 4 | 0 | 0 | 0 |
| [StringUtil](systems/StringUtil.md) | `C_StringUtil` | 14 | 1 | 0 | 0 |
| [SummonConstants](systems/SummonConstants.md) |  | 0 | 0 | 0 | 0 |
| [SummonInfo](systems/SummonInfo.md) | `C_SummonInfo` | 7 | 0 | 0 | 0 |
| [SuperTrackManager](systems/SuperTrackManager.md) | `C_SuperTrack` | 20 | 1 | 0 | 0 |
| [SuperTrackManagerShared](systems/SuperTrackManagerShared.md) |  | 0 | 0 | 0 | 0 |
| [SwingTimer](systems/SwingTimer.md) | `C_SwingTimer` | 2 | 0 | 0 | 0 |
| [SystemInfo](systems/SystemInfo.md) | `C_System` | 1 | 0 | 0 | 0 |
| [SystemTime](systems/SystemTime.md) |  | 7 | 0 | 0 | 0 |
| [TTSSettings](systems/TTSSettings.md) | `C_TTSSettings` | 19 | 0 | 0 | 0 |
| [TalentAndGlyphConstants](systems/TalentAndGlyphConstants.md) |  | 0 | 0 | 0 | 0 |
| [TalentConstants](systems/TalentConstants.md) |  | 0 | 0 | 0 | 0 |
| [TalkingHead](systems/TalkingHead.md) |  | 0 | 0 | 0 | 0 |
| [TargetScript](systems/TargetScript.md) |  | 24 | 0 | 0 | 0 |
| [TaxiMap](systems/TaxiMap.md) | `C_TaxiMap` | 3 | 0 | 0 | 0 |
| [TextureUtils](systems/TextureUtils.md) | `C_Texture` | 11 | 0 | 0 | 0 |
| [Threat](systems/Threat.md) |  | 2 | 0 | 0 | 0 |
| [Time](systems/Time.md) |  | 0 | 0 | 0 | 0 |
| [TimedSignalMapShared](systems/TimedSignalMapShared.md) |  | 0 | 0 | 0 | 0 |
| [TimerConstants](systems/TimerConstants.md) |  | 0 | 0 | 0 | 0 |
| [TimerunningConstants](systems/TimerunningConstants.md) |  | 0 | 0 | 0 | 0 |
| [TimerunningUI](systems/TimerunningUI.md) | `C_TimerunningUI` | 1 | 0 | 0 | 0 |
| [Title](systems/Title.md) |  | 5 | 0 | 0 | 0 |
| [TooltipComparison](systems/TooltipComparison.md) | `C_TooltipComparison` | 3 | 0 | 0 | 0 |
| [TooltipConstants](systems/TooltipConstants.md) |  | 0 | 0 | 0 | 0 |
| [TooltipInfo](systems/TooltipInfo.md) | `C_TooltipInfo` | 82 | 0 | 0 | 0 |
| [TooltipInfoShared](systems/TooltipInfoShared.md) |  | 0 | 0 | 0 | 0 |
| [Totem](systems/Totem.md) |  | 7 | 0 | 0 | 0 |
| [ToyBoxInfo](systems/ToyBoxInfo.md) | `C_ToyBoxInfo` | 6 | 0 | 0 | 0 |
| [TradeInfo](systems/TradeInfo.md) | `C_TradeInfo` | 4 | 0 | 0 | 0 |
| [TradeSkillUI](systems/TradeSkillUI.md) | `C_TradeSkillUI` | 89 | 57 | 0 | 0 |
| [TradeSkillUITypes](systems/TradeSkillUITypes.md) |  | 0 | 0 | 0 | 0 |
| [Trainer](systems/Trainer.md) | `C_Trainer` | 3 | 0 | 0 | 0 |
| [TrainerConstants](systems/TrainerConstants.md) |  | 0 | 0 | 0 | 0 |
| [TraitConstants](systems/TraitConstants.md) |  | 0 | 0 | 0 | 0 |
| [TransformManipulatorConstants](systems/TransformManipulatorConstants.md) |  | 0 | 0 | 0 | 0 |
| [TransmogConstants](systems/TransmogConstants.md) |  | 0 | 0 | 0 | 0 |
| [TransmogOutfitConstants](systems/TransmogOutfitConstants.md) |  | 0 | 0 | 0 | 0 |
| [TransmogOutfitInfo](systems/TransmogOutfitInfo.md) | `C_TransmogOutfitInfo` | 67 | 2 | 0 | 0 |
| [TransmogShared](systems/TransmogShared.md) |  | 0 | 0 | 0 | 0 |
| [Transmogrify](systems/Transmogrify.md) | `C_Transmog` | 7 | 0 | 0 | 0 |
| [TransmogrifyCollection](systems/TransmogrifyCollection.md) | `C_TransmogCollection` | 84 | 0 | 0 | 0 |
| [TransmogrifySets](systems/TransmogrifySets.md) | `C_TransmogSets` | 42 | 0 | 0 | 0 |
| [Tutorial](systems/Tutorial.md) | `C_Tutorial` | 4 | 0 | 0 | 0 |
| [UI](systems/UI.md) | `C_UI` | 7 | 0 | 0 | 0 |
| [UIActionConstants](systems/UIActionConstants.md) |  | 0 | 0 | 0 | 0 |
| [UIActionHandlerSystem](systems/UIActionHandlerSystem.md) |  | 0 | 0 | 0 | 0 |
| [UIButtonShared](systems/UIButtonShared.md) |  | 0 | 0 | 0 | 0 |
| [UICharacterClassConstants](systems/UICharacterClassConstants.md) |  | 0 | 0 | 0 | 0 |
| [UIColor](systems/UIColor.md) | `C_UIColor` | 1 | 0 | 0 | 0 |
| [UIColorShared](systems/UIColorShared.md) |  | 0 | 0 | 0 | 0 |
| [UICovenantDisplayInfoConstants](systems/UICovenantDisplayInfoConstants.md) |  | 0 | 0 | 0 | 0 |
| [UIEventToastConstants](systems/UIEventToastConstants.md) |  | 0 | 0 | 0 | 0 |
| [UIEventToastManagerInfo](systems/UIEventToastManagerInfo.md) | `C_EventToastManager` | 3 | 0 | 0 | 0 |
| [UIFileAssetAPI](systems/UIFileAssetAPI.md) | `C_UIFileAsset` | 3 | 0 | 0 | 0 |
| [UIFrameManager](systems/UIFrameManager.md) | `C_FrameManager` | 1 | 0 | 0 | 0 |
| [UIMacros](systems/UIMacros.md) | `C_Macro` | 3 | 0 | 1 | 0 |
| [UIMapPinShared](systems/UIMapPinShared.md) |  | 0 | 0 | 0 | 0 |
| [UIModelInfoShared](systems/UIModelInfoShared.md) |  | 0 | 0 | 0 | 0 |
| [UIModifiedInstance](systems/UIModifiedInstance.md) | `C_ModifiedInstance` | 1 | 0 | 0 | 0 |
| [UIShared](systems/UIShared.md) |  | 0 | 0 | 0 | 0 |
| [UISystemVisibilityManager](systems/UISystemVisibilityManager.md) | `C_SystemVisibilityManager` | 1 | 0 | 0 | 0 |
| [UITextureConstants](systems/UITextureConstants.md) |  | 0 | 0 | 0 | 0 |
| [UITimer](systems/UITimer.md) | `C_Timer` | 4 | 0 | 0 | 0 |
| [UIWidgetManager](systems/UIWidgetManager.md) | `C_UIWidgetManager` | 42 | 0 | 0 | 0 |
| [UIWidgetManagerShared](systems/UIWidgetManagerShared.md) |  | 0 | 0 | 0 | 0 |
| [URL](systems/URL.md) |  | 2 | 0 | 0 | 0 |
| [UiModelSceneConstants](systems/UiModelSceneConstants.md) |  | 0 | 0 | 0 | 0 |
| [Unit](systems/Unit.md) |  | 218 | 0 | 0 | 0 |
| [UnitAuraConstants](systems/UnitAuraConstants.md) |  | 0 | 0 | 0 | 0 |
| [UnitAuraShared](systems/UnitAuraShared.md) |  | 0 | 0 | 0 | 0 |
| [UnitAuras](systems/UnitAuras.md) | `C_UnitAuras` | 38 | 2 | 0 | 0 |
| [UnitConstants](systems/UnitConstants.md) |  | 0 | 0 | 0 | 0 |
| [UnitHealPredictionCalculatorShared](systems/UnitHealPredictionCalculatorShared.md) |  | 0 | 0 | 0 | 0 |
| [UnitRole](systems/UnitRole.md) |  | 6 | 0 | 0 | 0 |
| [UnitSexConstants](systems/UnitSexConstants.md) |  | 0 | 0 | 0 | 0 |
| [UnitShared](systems/UnitShared.md) |  | 0 | 0 | 0 | 0 |
| [UserFeedback](systems/UserFeedback.md) | `C_UserFeedback` | 2 | 0 | 0 | 0 |
| [ValidateNameConstants](systems/ValidateNameConstants.md) |  | 0 | 0 | 0 | 0 |
| [Vehicle](systems/Vehicle.md) |  | 0 | 0 | 0 | 0 |
| [Video](systems/Video.md) | `C_VideoOptions` | 11 | 0 | 0 | 0 |
| [Vignette](systems/Vignette.md) | `C_VignetteInfo` | 6 | 0 | 0 | 0 |
| [VignetteConstants](systems/VignetteConstants.md) |  | 0 | 0 | 0 | 0 |
| [VisualAlertConstants](systems/VisualAlertConstants.md) |  | 0 | 0 | 0 | 0 |
| [VoiceChat](systems/VoiceChat.md) | `C_VoiceChat` | 82 | 0 | 0 | 0 |
| [WarCampaign](systems/WarCampaign.md) | `C_CampaignInfo` | 10 | 0 | 0 | 0 |
| [WarbandSceneInfo](systems/WarbandSceneInfo.md) | `C_WarbandScene` | 7 | 0 | 0 | 0 |
| [WarbandSceneInfoConstants](systems/WarbandSceneInfoConstants.md) |  | 0 | 0 | 0 | 0 |
| [WeatherConstants](systems/WeatherConstants.md) |  | 0 | 0 | 0 | 0 |
| [WeatherScript](systems/WeatherScript.md) | `C_Weather` | 1 | 0 | 0 | 0 |
| [WeeklyRewards](systems/WeeklyRewards.md) | `C_WeeklyRewards` | 21 | 0 | 0 | 0 |
| [WorldElapsedTimerConstants](systems/WorldElapsedTimerConstants.md) |  | 0 | 0 | 0 | 0 |
| [WorldLootObject](systems/WorldLootObject.md) | `C_WorldLootObject` | 8 | 0 | 0 | 0 |
| [WorldSafeLocsUIInternal](systems/WorldSafeLocsUIInternal.md) | `C_WorldSafeLocsUIInternal` | 0 | 0 | 1 | 0 |
| [WorldStateInfo](systems/WorldStateInfo.md) |  | 0 | 0 | 0 | 0 |
| [WowCSConstants](systems/WowCSConstants.md) |  | 0 | 0 | 0 | 0 |
| [WowEntitlementInfo](systems/WowEntitlementInfo.md) |  | 0 | 0 | 0 | 0 |
| [WowSurvey](systems/WowSurvey.md) | `C_WowSurvey` | 2 | 0 | 0 | 0 |
| [WowSurveyConstants](systems/WowSurveyConstants.md) |  | 0 | 0 | 0 | 0 |
| [WowTokenUI](systems/WowTokenUI.md) | `C_WowTokenUI` | 2 | 0 | 0 | 0 |
| [XMLUtil](systems/XMLUtil.md) | `C_XMLUtil` | 2 | 0 | 0 | 0 |
| [ZoneAbility](systems/ZoneAbility.md) | `C_ZoneAbility` | 2 | 0 | 0 | 0 |
| [ZoneScript](systems/ZoneScript.md) |  | 5 | 0 | 0 | 0 |

## Left out

Globals written by add-ons when the dump ran (not API):

- !BugGrabber: 6
- AlexAtlasLoot: 11
- ApiProbe: 3
- BetterForeverChat: 5
- BetterWorldMap: 11
- BlizzMove: 25
- BugSack: 11
- CameraTilt: 7
- Clairvoyance: 12
- Council: 6
- CouncilProbe: 2
- Dimension: 12
- ForeverAutoQuest: 5
- ForeverDungeonJournal: 22
- Guise: 14
- HealProbe: 7
- Mercy: 7
- Muster: 6
- NKThreat: 44
- NorgannonDB: 1
- NorgannonDBCollector: 5
- NorgannonDB_Core: 148
- Oracle: 8
- PlateProbe: 2
- RecruitProbe: 2
- Retrospect: 9
- RoleplayProbe: 2
- Scrap: 7
- SpeedyAutoLoot: 4
- TurnIn: 5
- WhatsTraining: 19
