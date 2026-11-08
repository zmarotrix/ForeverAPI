# Relocated API

Classic (1.15) globals that Forever dropped or moved, where each one went and how the call changed. Every name in this table was checked against an in-game dump of client 1.60.1.70862.

- **gone**: the old name doesn't exist on Forever. Calling it errors.
- **shim**: the old name still works, through Blizzard's own deprecation add-ons (Blizzard_Deprecated*). Blizzard says these will be removed, so switch.
- Sources: *guide* is Blizzard's spell book transition guide in the client; *shim* a Blizzard deprecation add-on; *classic shim* one Blizzard ships for classic only, which Forever doesn't load; *curated* our own sources/relocated.json; *same-name* only a function of the same name in a C_ namespace (a lead).

Note: Forever reports `WOW_PROJECT_ID` = 18 (`WOW_PROJECT_CAMELOT`), not `WOW_PROJECT_MAINLINE` (1) or `WOW_PROJECT_CLASSIC` (2), but it loads Blizzard's *mainline* deprecation shims, not the classic ones. Add-ons that branch on the project ID take neither branch.

## Gone on Forever (138)

| Classic | Forever | How it changed | Source |
|---|---|---|---|
| `GetQuestLogTitle` | `C_QuestLog.GetInfo` | Returns one QuestInfo table instead of a list of values. Classic: `title, level, suggestedGroup, isHeader, isCollapsed, isComplete, frequency, questID, ... = GetQuestLogTitle(index)`. Called 4× by Questie. | curated |
| `ExpandFactionHeader` | `C_Reputation.ExpandFactionHeader` | Same argument. Called 3× by Questie. | curated |
| `GetFactionInfo` | `C_Reputation.GetFactionDataByIndex` | Returns one FactionData table instead of a list of values. Called 3× by Questie. | curated |
| `GetNumFactions` | `C_Reputation.GetNumFactions` | Same return. Called 3× by Questie. | curated |
| `GetNumQuestLogEntries` | `C_QuestLog.GetNumQuestLogEntries` | Same returns (entries, quests). Called 2× by Questie. | curated |
| `GetSkillLineInfo` | `C_SkillInfo.GetSkillLineInfo` | Check the return shape in Blizzard's docs: the C_SkillInfo version may return a table. Called 2× by Questie. | curated |
| `GetSpellInfo` | `C_Spell.GetSpellInfo` | Returns one SpellInfo table (name, iconID, originalIconID, castTime, minRange, maxRange, spellID) instead of eight values, and no rank. For just the name or icon, C_Spell.GetSpellName / C_Spell.GetSpellTexture are cheaper. Rank text: C_Spell.GetSpellSubtext. Classic: `name, rank, icon, castTime, minRange, maxRange, spellID, originalIcon = GetSpellInfo(spellID \| name)`. Called 2× by Questie. | curated |
| `RemoveTrackedAchievement` | `C_ContentTracking.StopTracking` | Takes the tracking type, the achievement ID and a stop type (Enum.ContentTrackingStopType.Manual). Called 2× by Questie. | curated |
| `AbandonQuest` | `C_QuestLog.AbandonQuest` | Same: abandons the quest set with SetAbandonQuest. Called 1× by Questie. | curated |
| `ExpandSkillHeader` | `C_SkillInfo.ExpandSkillHeader` | Same argument, if it exists: the table says whether it's in game. Called 1× by Questie. | curated |
| `GetAbandonQuestItems` | `C_QuestLog.GetAbandonQuestItems` | Same return. Called 1× by Questie. | curated |
| `GetAbandonQuestName` | `C_QuestLog.GetTitleForQuestID`<br>`C_QuestLog.GetAbandonQuest` | C_QuestLog.GetAbandonQuest() gives the quest ID; its title comes from C_QuestLog.GetTitleForQuestID. Called 1× by Questie. | curated |
| `GetContainerItemInfo` | `C_Container.GetContainerItemInfo` | Returns one ContainerItemInfo table (iconFileID, stackCount, isLocked, quality, isReadable, hasLoot, hyperlink, isFiltered, hasNoValue, itemID, isBound) instead of eleven values. Classic: `texture, count, locked, quality, readable, lootable, link, filtered, noValue, itemID, isBound = GetContainerItemInfo(bag, slot)`. Called 1× by Questie. | curated |
| `GetContainerNumSlots` | `C_Container.GetContainerNumSlots` | Same argument and return. Called 1× by Questie. | curated |
| `GetFactionInfoByID` | `C_Reputation.GetFactionDataByID` | Returns one FactionData table instead of a list of values. Called 1× by Questie. | curated |
| `GetGossipActiveQuests` | `C_GossipInfo.GetActiveQuests` | Returns a list of GossipQuestUIInfo tables instead of a flat list of values per quest. Called 1× by Questie. | curated |
| `GetGossipAvailableQuests` | `C_GossipInfo.GetAvailableQuests` | Returns a list of GossipQuestUIInfo tables instead of a flat list of values per quest. Called 1× by Questie. | curated |
| `GetItemCooldown` | `C_Container.GetItemCooldown`<br>`C_Item.GetItemCooldown` | C_Container.GetItemCooldown(itemID) is the drop-in: same three returns, enable is still a number. C_Item.GetItemCooldown takes any item (ID, name, link) and returns enable as true/false. Classic: `start, duration, enable = GetItemCooldown(itemID)`. Called 1× by Questie. | curated |
| `GetMouseFocus` | `GetMouseFoci` | Returns a list of every frame under the cursor; the old single answer is GetMouseFoci()[1]. Called 1× by Questie. | curated |
| `GetNumGossipActiveQuests` | `C_GossipInfo.GetNumActiveQuests` | Same return. Called 1× by Questie. | curated |
| `GetNumGossipAvailableQuests` | `C_GossipInfo.GetNumAvailableQuests` | Same return. Called 1× by Questie. | curated |
| `GetNumQuestWatches` | `C_QuestLog.GetNumQuestWatches` | Same return. Called 1× by Questie. | curated |
| `GetNumSkillLines` | `C_SkillInfo.GetNumSkillLines` | Same return. Check in game before relying on the order matching the old skill list. Called 1× by Questie. | curated |
| `GetQuestIDFromLogIndex` | `C_QuestLog.GetQuestIDForLogIndex` | Same argument and return. Called 1× by Questie. | curated |
| `GetQuestIndexForWatch` | `C_QuestLog.GetQuestIDForQuestWatchIndex` | Returns a quest ID instead of a log index. Called 1× by Questie. | curated |
| `GetQuestLogIndexByID` | `C_QuestLog.GetLogIndexForQuestID` | Same argument and return. Called 1× by Questie. | curated |
| `GetQuestLogSelection` | `C_QuestLog.GetSelectedQuest` | Returns a quest ID instead of a log index. Called 1× by Questie. | curated |
| `GetQuestObjectives` | `C_QuestLog.GetQuestObjectives` | Takes a quest ID; returns a list of QuestObjectiveInfo tables. Called 1× by Questie. | curated |
| `GetQuestsCompleted` | `C_QuestLog.GetAllCompletedQuestIDs` | Returns a list of quest IDs instead of a table keyed by quest ID. Called 1× by Questie. | curated |
| `GetQuestTagInfo` | `C_QuestLog.GetQuestTagInfo` | Returns one QuestTagInfo table (or nil). Called 1× by Questie. | curated |
| `GetQuestTimers` | `C_QuestLog.GetTimeAllowed` | Per quest: C_QuestLog.GetTimeAllowed(questID) returns totalTime, elapsedTime. Called 1× by Questie. | curated |
| `GetStablePetFoodTypes` | `C_StableInfo.GetStablePetFoodTypes` | **Lead.** Called 1× by Questie. | same-name |
| `GetTrackedAchievements` | `C_ContentTracking.GetTrackedIDs` | Takes the tracking type (Enum.ContentTrackingType.Achievement) and returns a list. Called 1× by Questie. | curated |
| `RegisterAddonMessagePrefix` | `C_ChatInfo.RegisterAddonMessagePrefix` | Same argument; returns a result code (Enum.RegisterAddonMessagePrefixResult) instead of true/false. Called 1× by Questie. | curated |
| `RemoveQuestWatch` | `C_QuestLog.RemoveQuestWatch` | Takes a quest ID instead of a log index. Called 1× by Questie. | curated |
| `SelectGossipActiveQuest` | `C_GossipInfo.SelectActiveQuest` | Takes the quest ID instead of the list index. Called 1× by Questie. | curated |
| `SelectGossipAvailableQuest` | `C_GossipInfo.SelectAvailableQuest` | Takes the quest ID instead of the list index. Called 1× by Questie. | curated |
| `SelectQuestLogEntry` | `C_QuestLog.SetSelectedQuest` | Takes a quest ID instead of a log index. Called 1× by Questie. | curated |
| `SetAbandonQuest` | `C_QuestLog.SetAbandonQuest` | Uses the selected quest (C_QuestLog.SetSelectedQuest) as before. Called 1× by Questie. | curated |
| `UnitAura` | `C_UnitAuras.GetAuraDataByIndex` *secret in combat*<br>`AuraUtil.UnpackAuraData` | Returns one AuraData table instead of a list of values; AuraUtil.UnpackAuraData(aura) turns it back into the old list. Classic shims it (Deprecated_1_15_8.lua), Forever doesn't load that shim. In combat, aura reads from add-on code may error or return secrets: see the secrets guide. Classic: `name, icon, count, debuffType, duration, expirationTime, source, isStealable, nameplateShowPersonal, spellId, ... = UnitAura(unit, index [, filter])`. Called 1× by Questie. | curated, classic shim |
| `AddQuestWatch` | `C_QuestLog.AddQuestWatch` | Takes a quest ID instead of a log index. | curated |
| `C_SpellBook.GetDeadlyDebuffInfo` | `C_Spell.GetDeadlyDebuffInfo` | Moved as is. | guide |
| `C_SpellBook.GetOverrideSpell` | `C_Spell.GetOverrideSpell` | Moved as is. | guide |
| `C_SpellBook.GetSpellInfo` | `C_Spell.GetSpellInfo` | Moved as is. | guide |
| `C_SpellBook.GetSpellLinkFromSpellID` | `C_Spell.GetSpellLink` | Moved as is. | guide |
| `C_SpellBook.IsSpellDisabled` | `C_Spell.IsSpellDisabled` | Moved as is. | guide |
| `CastingInfo` | `UnitCastingInfo` *secret in combat* | Classic: `CastingInfo()`. | classic shim |
| `ChannelInfo` | `UnitChannelInfo` *secret in combat* | Classic: `ChannelInfo()`. | classic shim |
| `CollapseFactionHeader` | `C_Reputation.CollapseFactionHeader` | Same argument. | curated |
| `CombatLogAddFilter` | `C_CombatLog.AddEventFilter` (not visible to add-ons) |  | shim |
| `CombatLogGetCurrentEntry` | `C_CombatLog.GetCurrentEntryInfo` (not visible to add-ons) |  | shim |
| `CombatLogGetCurrentEventInfo` | `C_CombatLog.GetCurrentEventInfo` (not visible to add-ons) |  | shim |
| `CombatLogGetNumEntries` | `C_CombatLog.GetEntryCount` (not visible to add-ons) |  | shim |
| `CombatLogResetFilter` | `C_CombatLog.ClearEventFilters` (not visible to add-ons) |  | shim |
| `CombatLogShowCurrentEntry` | `C_CombatLog.ShouldShowCurrentEntry` (not visible to add-ons) |  | shim |
| `DisableAddOn` | `C_AddOns.DisableAddOn` | Same arguments. | curated |
| `DisableSpellAutocast` | `C_Spell.SetSpellAutoCastEnabled`<br>`C_SpellBook.SetSpellBookItemAutoCastEnabled` | Now `C_Spell.SetSpellAutoCastEnabled(spellIdentifier, bool)`. Blizzard: Enable/Disable auto cast functions have been merged into single Set Enabled functions. Classic: `DisableSpellAutocast(spellID/name)`. | guide |
| `DoesSpellExist` | `C_Spell.DoesSpellExist` | Now `C_Spell.DoesSpellExist(spellIdentifier)`. Classic: `DoesSpellExist(spellID/name)`. | guide |
| `EnableAddOn` | `C_AddOns.EnableAddOn` | Same arguments. | curated |
| `EnableSpellAutocast` | `C_Spell.SetSpellAutoCastEnabled`<br>`C_SpellBook.SetSpellBookItemAutoCastEnabled` | Now `C_Spell.SetSpellAutoCastEnabled(spellIdentifier, bool)`. Blizzard: Enable/Disable auto cast functions have been merged into single Set Enabled functions. Classic: `EnableSpellAutocast(spellID/name)`. | guide |
| `GetActiveSpecGroup` | `C_SpecializationInfo.GetActiveSpecGroup` |  | classic shim |
| `GetActiveTalentGroup` | `C_SpecializationInfo.GetActiveSpecGroup` |  | classic shim |
| `GetAddOnInfo` | `C_AddOns.GetAddOnInfo` | Same argument; returns name, title, notes, loadable, reason, security, updateAvailable. | curated |
| `GetAddOnMetadata` | `C_AddOns.GetAddOnMetadata` | Same arguments and return. | curated |
| `GetContainerItemID` | `C_Container.GetContainerItemID` | Same arguments and return. | curated |
| `GetContainerItemLink` | `C_Container.GetContainerItemLink` | Same arguments and return. | curated |
| `GetContainerNumFreeSlots` | `C_Container.GetContainerNumFreeSlots` | Same argument and returns. | curated |
| `GetGossipOptions` | `C_GossipInfo.GetOptions` | Returns a list of GossipOptionUIInfo tables. | curated |
| `GetItemCount` | `C_Item.GetItemCount` | Same arguments (item, includeBank, includeUses, includeReagentBank) and return. | curated |
| `GetItemIcon` | `C_Item.GetItemIconByID` | Same argument and return. | curated |
| `GetItemInfo` | `C_Item.GetItemInfo` | Same returns in the same order, plus an 18th (itemDescription). Same argument (item ID, name or link). Still returns nothing until the item is cached: wait for ITEM_DATA_LOAD_RESULT / GET_ITEM_INFO_RECEIVED, or use C_Item.GetItemInfoInstant for the fields that need no cache. Classic: `name, link, quality, itemLevel, minLevel, type, subType, stackCount, equipLoc, texture, sellPrice, classID, subclassID, bindType, expansionID, setID, isCraftingReagent = GetItemInfo(item)`. | curated |
| `GetItemInfoInstant` | `C_Item.GetItemInfoInstant` | Same arguments and returns. | curated |
| `GetItemQualityColor` | `C_Item.GetItemQualityColor` | Same argument and returns (r, g, b, hex). | curated |
| `GetItemStats` | `C_Item.GetItemStats` | Takes only the link; the optional table to fill is gone, it always returns a new table. Classic: `stats = GetItemStats(itemLink [, statTable])`. | curated |
| `GetMapInfo` | `C_Map.GetMapInfo` | Takes a uiMapID and returns a UiMapDetails table. | curated |
| `GetNumAddOns` | `C_AddOns.GetNumAddOns` | Same return. | curated |
| `GetNumSpecializationsForClassID` | `C_SpecializationInfo.GetNumSpecializationsForClassID` |  | classic shim |
| `GetNumSpellTabs` | `C_SpellBook.GetNumSpellBookSkillLines` | Now `C_SpellBook.GetNumSpellBookSkillLines()`. Classic: `GetNumSpellTabs()`. | guide |
| `GetPrimaryTalentTree` | `C_SpecializationInfo.GetSpecialization` |  | classic shim |
| `GetSpecialization` | `C_SpecializationInfo.GetSpecialization` |  | classic shim |
| `GetSpecializationInfo` | `C_SpecializationInfo.GetSpecializationInfo` |  | classic shim |
| `GetSpecializationMasterySpells` | `C_SpecializationInfo.GetSpecializationMasterySpells` | Classic: `GetSpecializationMasterySpells(specIndex, isInspect, isPet)`. | classic shim |
| `GetSpellAutocast` | `C_Spell.GetSpellAutoCast`<br>`C_SpellBook.GetSpellBookItemAutoCast` | Now `C_Spell.GetSpellAutoCast(spellIdentifier)`. Classic: `GetSpellAutocast(spellID/name)`. | guide |
| `GetSpellAvailableLevel` | `C_Spell.GetSpellLevelLearned`<br>`C_SpellBook.GetSpellBookItemLevelLearned` | Now `C_Spell.GetSpellLevelLearned(spellIdentifier)`. Blizzard: GetSpellAvailableLevel and GetSpellLevelLearned have been unified. Classic: `GetSpellAvailableLevel(spellID/name)`. | guide |
| `GetSpellBookItemInfo` | `C_SpellBook.GetSpellBookItemType` | Now `C_SpellBook.GetSpellBookItemType(index, spellBank)`. spellBank is Enum.SpellBookSpellBank.Player or .Pet instead of the "spell" / "pet" book type. Blizzard: C_SpellBook.GetSpellBookItemType is the direct replacement for just the type info that the old GetSpellBookItemInfo returned (+spellID as a new bonus 3rd return value). Classic: `GetSpellBookItemInfo(index, bookType)`. | guide |
| `GetSpellBookItemName` | `C_SpellBook.GetSpellBookItemName` | Now `C_SpellBook.GetSpellBookItemName(index, spellBank)`. spellBank is Enum.SpellBookSpellBank.Player or .Pet instead of the "spell" / "pet" book type. Classic: `GetSpellBookItemName(index, bookType)`. | guide |
| `GetSpellBookItemTexture` | `C_SpellBook.GetSpellBookItemTexture` | Now `C_SpellBook.GetSpellBookItemTexture(index, spellBank)`. spellBank is Enum.SpellBookSpellBank.Player or .Pet instead of the "spell" / "pet" book type. Classic: `GetSpellBookItemTexture(index, bookType)`. | guide |
| `GetSpellCharges` | `C_Spell.GetSpellCharges` *secret in combat*<br>`C_SpellBook.GetSpellBookItemCharges` *secret in combat* | Now `C_Spell.GetSpellCharges(spellIdentifier)`. Blizzard: Both return new SpellChargeInfo table (see SpellSharedDocumentation.lua). Classic: `GetSpellCharges(spellID/name)`. | guide |
| `GetSpellCooldown` | `C_Spell.GetSpellCooldown` *secret in combat*<br>`C_SpellBook.GetSpellBookItemCooldown` *secret in combat* | Returns one SpellCooldownInfo table (startTime, duration, isEnabled, modRate) instead of four values. The spell book form moved to C_SpellBook.GetSpellBookItemCooldown(index, spellBank). Classic: `start, duration, enabled, modRate = GetSpellCooldown(spellID \| name)`. | curated, guide |
| `GetSpellCount` | `C_Spell.GetSpellCastCount` *secret in combat*<br>`C_SpellBook.GetSpellBookItemCastCount` *secret in combat* | Now `C_Spell.GetSpellCastCount(spellIdentifier)`. Classic: `GetSpellCount(spellID/name)`. | guide |
| `GetSpellDescription` | `C_Spell.GetSpellDescription` | Now `C_Spell.GetSpellDescription(spellIdentifier)`. Classic: `GetSpellDescription(spellID)`. | guide |
| `GetSpellLevelLearned` | `C_Spell.GetSpellLevelLearned`<br>`C_SpellBook.GetSpellBookItemLevelLearned` | Now `C_Spell.GetSpellLevelLearned(spellIdentifier)`. Classic: `GetSpellLevelLearned(spellID/name)`. | guide |
| `GetSpellLink` | `C_Spell.GetSpellLink`<br>`C_SpellBook.GetSpellBookItemLink` | Now `C_Spell.GetSpellLink(spellIdentifier)`. Classic: `GetSpellLink(spellID/name)`. | guide |
| `GetSpellLossOfControlCooldown` | `C_Spell.GetSpellLossOfControlCooldown`<br>`C_SpellBook.GetSpellBookItemLossOfControlCooldown` | Now `C_Spell.GetSpellLossOfControlCooldown(spellIdentifier)`. Classic: `GetSpellLossOfControlCooldown(spellID/name)`. | guide |
| `GetSpellPowerCost` | `C_Spell.GetSpellPowerCost`<br>`C_SpellBook.GetSpellBookItemPowerCost` | Now `C_Spell.GetSpellPowerCost(spellIdentifier)`. Blizzard: Both return array of new SpellPowerCostInfo tables (see SpellSharedDocumentation.lua) which matches old return table structure. Classic: `GetSpellPowerCost(spellID/name)`. | guide |
| `GetSpellRank` | `C_Spell.GetSpellSkillLineAbilityRank` | Now `C_Spell.GetSpellSkillLineAbilityRank(spellIdentifier)`. Classic: `GetSpellRank(spellID)`. | guide |
| `GetSpellSubtext` | `C_Spell.GetSpellSubtext` | Now `C_Spell.GetSpellSubtext(spellIdentifier)`. Classic: `GetSpellSubtext(spellID)`. | guide |
| `GetSpellTabInfo` | `C_SpellBook.GetSpellBookSkillLineInfo` | Now `C_SpellBook.GetSpellBookSkillLineInfo(index)`. Blizzard: Returns new SpellBookSkillLineInfo table. Classic: `GetSpellTabInfo(index)`. | guide |
| `GetSpellTexture` | `C_Spell.GetSpellTexture` | Now `C_Spell.GetSpellTexture(spellIdentifier)`. Classic: `GetSpellTexture(spellID)`. | guide |
| `GetSpellTradeSkillLink` | `C_Spell.GetSpellTradeSkillLink`<br>`C_SpellBook.GetSpellBookItemTradeSkillLink` | Now `C_Spell.GetSpellTradeSkillLink(spellIdentifier)`. Classic: `GetSpellTradeSkillLink(spellID/name)`. | guide |
| `GetTalentInfo` | `C_SpecializationInfo.GetTalentInfo` | Classic: `GetTalentInfo(tabIndex, talentIndex, isInspect, isPet, groupIndex)`. | classic shim |
| `GetTalentTabInfo` | `C_SpecializationInfo.GetSpecializationInfo` | Classic: `GetTalentTabInfo(specializationIndex, isInspect, isPet, groupIndex)`. | classic shim |
| `GetTalentTreeMasterySpells` | `C_SpecializationInfo.GetSpecializationMasterySpells` | Classic: `GetTalentTreeMasterySpells(specIndex, isInspect, isPet)`. | classic shim |
| `GetWatchedFactionInfo` | `C_Reputation.GetWatchedFactionData` | Returns one FactionData table (or nil) instead of a list of values. | curated |
| `GetZonePVPInfo` | `C_PvP.GetZonePVPInfo` | Same returns (pvpType, isSubZonePvP, factionName). | curated |
| `HasPetSpells` | `C_SpellBook.HasPetSpells` | Now `C_SpellBook.HasPetSpells()`. | guide |
| `IsAddOnLoaded` | `C_AddOns.IsAddOnLoaded` | Same argument; returns loadedOrLoading, loaded. | curated |
| `IsAddonMessagePrefixRegistered` | `C_ChatInfo.IsAddonMessagePrefixRegistered` | Same argument and return. | curated |
| `IsAttackSpell` | `C_Spell.IsAutoAttackSpell`<br>`C_SpellBook.IsAutoAttackSpellBookItem` | Now `C_Spell.IsAutoAttackSpell(spellIdentifier)`. Classic: `IsAttackSpell(spellName)`. | guide |
| `IsAutoRepeatSpell` | `C_Spell.IsAutoRepeatSpell` | Now `C_Spell.IsAutoRepeatSpell(spellIdentifier)`. Classic: `IsAutoRepeatSpell(spellID/name)`. | guide |
| `IsCurrentSpell` | `C_Spell.IsCurrentSpell` | Now `C_Spell.IsCurrentSpell(spellIdentifier)`. Classic: `IsCurrentSpell(spellID/name)`. | guide |
| `IsEquippedItem` | `C_Item.IsEquippedItem` | Same argument and return. | curated |
| `IsHarmfulSpell` | `C_Spell.IsSpellHarmful`<br>`C_SpellBook.IsSpellBookItemHarmful` | Now `C_Spell.IsSpellHarmful(spellIdentifier)`. Classic: `IsHarmfulSpell(spellID/name)`. | guide |
| `IsHelpfulSpell` | `C_Spell.IsSpellHelpful`<br>`C_SpellBook.IsSpellBookItemHelpful` | Now `C_Spell.IsSpellHelpful(spellIdentifier)`. Classic: `IsHelpfulSpell(spellID/name)`. | guide |
| `IsPassiveSpell` | `C_Spell.IsSpellPassive`<br>`C_SpellBook.IsSpellBookItemPassive` | Now `C_Spell.IsSpellPassive(spellIdentifier)`. Classic: `IsPassiveSpell(spellID/name)`. | guide |
| `IsPressHoldReleaseSpell` | `C_Spell.IsPressHoldReleaseSpell` | Now `C_Spell.IsPressHoldReleaseSpell(spellIdentifier)`. Classic: `IsPressHoldReleaseSpell(spellID/name)`. | guide |
| `IsPvpTalentSpell` | `C_Spell.IsPvPTalentSpell`<br>`C_SpellBook.IsPvPTalentSpellBookItem` | Now `C_Spell.IsPvPTalentSpell(spellIdentifier)`. Classic: `IsPvpTalentSpell(spellID/name)`. | guide |
| `IsQuestFlaggedCompleted` | `C_QuestLog.IsQuestFlaggedCompleted` | Same argument and return. | curated |
| `IsSpellInRange` | `C_Spell.IsSpellInRange`<br>`C_SpellBook.IsSpellBookItemInRange` | Now `C_Spell.IsSpellInRange(spellIdentifier)`. Classic: `IsSpellInRange(spellID/name)`. | guide |
| `IsTalentSpell` | `C_Spell.IsClassTalentSpell`<br>`C_SpellBook.IsClassTalentSpellBookItem` | Now `C_Spell.IsClassTalentSpell(spellIdentifier)`. Classic: `IsTalentSpell(spellID/name)`. | guide |
| `IsUsableSpell` | `C_Spell.IsSpellUsable`<br>`C_SpellBook.IsSpellBookItemUsable` | Now `C_Spell.IsSpellUsable(spellIdentifier)`. Classic: `IsUsableSpell(spellID/name)`. | guide |
| `LoadAddOn` | `C_AddOns.LoadAddOn` | Same argument and returns. | curated |
| `math.randomseed` | none | **Removed.** Removed from the add-on Lua environment: add-ons can't seed the random generator. math.random and the global random / fastrandom still work. | curated |
| `PickupContainerItem` | `C_Container.PickupContainerItem` | Same arguments. | curated |
| `PickupSpell` | `C_Spell.PickupSpell` | Now `C_Spell.PickupSpell(spellIdentifier)`. Classic: `PickupSpell(spellID/name)`. | guide |
| `PickupSpellBookItem` | `C_SpellBook.PickupSpellBookItem` | Now `C_SpellBook.PickupSpellBookItem(index, spellBank)`. spellBank is Enum.SpellBookSpellBank.Player or .Pet instead of the "spell" / "pet" book type. Classic: `PickupSpellBookItem(index, bookType)`. | guide |
| `searcher.OldGetAllSearchItems` | none | Classic: `searcher.OldGetAllSearchItems(self)`. | shim |
| `searcher.OldGetCatalogSearchResults` | none | Classic: `searcher.OldGetCatalogSearchResults(self)`. | shim |
| `SendAddonMessage` | `C_ChatInfo.SendAddonMessage` | Same arguments; returns a result code (Enum.SendAddonMessageResult). | curated |
| `SetActiveTalentGroup` | `C_SpecializationInfo.SetActiveSpecGroup` |  | classic shim |
| `SpellHasRange` | `C_Spell.SpellHasRange`<br>`C_SpellBook.SpellBookItemHasRange` | Now `C_Spell.SpellHasRange(spellIdentifier)`. Classic: `SpellHasRange(spellID/name)`. | guide |
| `ToggleSpellAutocast` | `C_Spell.ToggleSpellAutoCast`<br>`C_SpellBook.ToggleSpellBookItemAutoCast` | Now `C_Spell.ToggleSpellAutoCast(spellIdentifier)`. Classic: `ToggleSpellAutocast(spellID/name)`. | guide |
| `UnitBuff` | `C_UnitAuras.GetBuffDataByIndex` *secret in combat*<br>`AuraUtil.UnpackAuraData` | Returns one AuraData table; AuraUtil.UnpackAuraData(aura) gives the old list. Same in-combat caveats as UnitAura. Classic: `UnitBuff(unitToken, index, filter)`. | curated, classic shim |
| `UnitCharacterPoints` | `GetNumUnspentTalents`<br>`C_ClassTalents.HasUnspentTalentPoints` | **Closest.** No direct replacement. GetNumUnspentTalents() returns the player's unspent talent points (no unit argument); C_ClassTalents.HasUnspentTalentPoints() only says whether there are any. Check the result in game before relying on it. Classic: `talentPoints = UnitCharacterPoints("player")`. | curated |
| `UnitDebuff` | `C_UnitAuras.GetDebuffDataByIndex` *secret in combat*<br>`AuraUtil.UnpackAuraData` | Returns one AuraData table; AuraUtil.UnpackAuraData(aura) gives the old list. Same in-combat caveats as UnitAura. Classic: `UnitDebuff(unitToken, index, filter)`. | curated, classic shim |
| `UnitMaxHealth` | `UnitHealthMax` *secret in combat* | **Name mix-up.** UnitMaxHealth was never a Blizzard function: the classic (and Forever) name is UnitHealthMax. It still exists, but for party, raid and enemy units it can return a secret value. | curated |
| `UseContainerItem` | `C_Container.UseContainerItem` | Same arguments. Protected in combat for some items, as before. | curated |
| `variantID.entrySubtype` | `Enum.HousingCatalogEntrySubtype.Unowned` |  | shim |

## Still works through Blizzard's deprecation add-ons (to be removed) (262)

| Classic | Forever | How it changed | Source |
|---|---|---|---|
| `IsSpellKnown` | `C_SpellBook.IsSpellInSpellBook` | Classic: `IsSpellKnown(spellID, isPet)`. Called 16× by Questie. | shim |
| `ChatEdit_GetActiveWindow` | `ChatFrameUtil.GetActiveWindow` |  Called 12× by Questie. | shim |
| `ChatEdit_InsertLink` | `ChatFrameUtil.InsertLink` |  Called 11× by Questie. | shim |
| `ChatFrame_OpenChat` | `ChatFrameUtil.OpenChat` |  Called 3× by Questie. | shim |
| `SendChatMessage` | `C_ChatInfo.SendChatMessage` | Classic: `SendChatMessage(message, chatType, languageID, target)`. Called 2× by Questie. | shim |
| `ChatFrame_AddMessageEventFilter` | `ChatFrameUtil.AddMessageEventFilter` |  Called 1× by Questie. | shim |
| `ChatFrame_RemoveMessageEventFilter` | `ChatFrameUtil.RemoveMessageEventFilter` |  Called 1× by Questie. | shim |
| `IsPlayerSpell` | `C_SpellBook.IsSpellKnown` | Classic: `IsPlayerSpell(spellID)`. Called 1× by Questie. | shim |
| `ActionHasRange` | `C_ActionBar.HasRangeRequirements` | Classic: `ActionHasRange(actionID)`. | shim |
| `Blizzard_CombatLog_BitToBraceCode` | `CombatLogUtil.GetRaidTargetBraceCode` |  | shim |
| `BNGetFriendInviteInfo` | `C_BattleNet.GetFriendInviteInfo` | Classic: `BNGetFriendInviteInfo(inviteIndex)`. | shim |
| `BNInviteFriend` | `C_BattleNet.InviteFriend` | Classic: `BNInviteFriend(gameAccountID)`. | shim |
| `BNSendGameData` | `C_BattleNet.SendGameData` | Classic: `BNSendGameData(gameAccountID, prefix, data)`. | shim |
| `BNSendVerifiedBattleTagInvite` | `C_BattleNet.SendVerifiedBattleNetFriendInvite` | Classic: `BNSendVerifiedBattleTagInvite()`. | shim |
| `BNSendWhisper` | `C_BattleNet.SendWhisper` | Classic: `BNSendWhisper(bnetAccountID, text)`. | shim |
| `BNSetBlocked` | `C_BattleNet.SetBlocked` | Classic: `BNSetBlocked(bnetAccountID, block)`. | shim |
| `BNSetCustomMessage` | `C_BattleNet.SetCustomMessage` | Classic: `BNSetCustomMessage(text)`. | shim |
| `C_ActionBar.GetActionLossOfControlCooldown` | `C_ActionBar.GetActionLossOfControlCooldownInfo` *secret in combat* | Classic: `C_ActionBar.GetActionLossOfControlCooldown(actionID)`. | shim |
| `C_ClickBindings.GetStringFromModifiers` | `GetStringFromModifiers` | Classic: `C_ClickBindings.GetStringFromModifiers(modifiers)`. | shim |
| `C_ClickBindings.MakeModifiers` | none | Classic: `C_ClickBindings.MakeModifiers(...)`. | shim |
| `C_DyeColor.GetDyeColorForItem` | `C_DyeColor.GetDyeColorsForItem` | Classic: `C_DyeColor.GetDyeColorForItem(itemLinkOrID)`. | shim |
| `C_DyeColor.GetDyeColorForItemLocation` | `C_DyeColor.GetDyeColorsForItemLocation` | Classic: `C_DyeColor.GetDyeColorForItemLocation(itemLocation)`. | shim |
| `C_Housing.IsInsideOwnHouse` | `C_Housing.IsInsideOwnedHouse` |  | shim |
| `C_HousingBasicMode.StartPlacingNewDecor` | none | Classic: `C_HousingBasicMode.StartPlacingNewDecor(catalogEntryIDOrVariantID)`. | shim |
| `C_HousingCatalog.CanDestroyEntry` | none | Classic: `C_HousingCatalog.CanDestroyEntry(entryIDOrVariantID)`. | shim |
| `C_HousingCatalog.CreateCatalogSearcher` | none | Classic: `C_HousingCatalog.CreateCatalogSearcher()`. | shim |
| `C_HousingCatalog.DestroyEntry` | none | Classic: `C_HousingCatalog.DestroyEntry(entryIDOrVariantID, destroyAll)`. | shim |
| `C_HousingCatalog.GetCatalogCategoryInfo` | none | Classic: `C_HousingCatalog.GetCatalogCategoryInfo(categoryID)`. | shim |
| `C_HousingCatalog.GetCatalogEntryInfo` | none | Classic: `C_HousingCatalog.GetCatalogEntryInfo(entryID)`. | shim |
| `C_HousingCatalog.GetCatalogEntryInfoByItem` | none | Classic: `C_HousingCatalog.GetCatalogEntryInfoByItem(itemInfo, _tryGetOwnedInfo)`. | shim |
| `C_HousingCatalog.GetCatalogEntryInfoByRecordID` | none | Classic: `C_HousingCatalog.GetCatalogEntryInfoByRecordID(entryType, recordID, _tryGetOwnedInfo)`. | shim |
| `C_HousingCatalog.GetCatalogSubcategoryInfo` | none | Classic: `C_HousingCatalog.GetCatalogSubcategoryInfo(subcategoryID)`. | shim |
| `C_HousingCatalog.GetFeaturedDecor` | `C_HousingCatalog.GetFeaturedSmallProducts` | Classic: `C_HousingCatalog.GetFeaturedDecor()`. | shim |
| `C_HousingCatalog.SearchCatalogCategories` | none | Classic: `C_HousingCatalog.SearchCatalogCategories(searchParams)`. | shim |
| `C_HousingCatalog.SearchCatalogSubcategories` | none | Classic: `C_HousingCatalog.SearchCatalogSubcategories(searchParams)`. | shim |
| `C_HousingDecor.GetMaxPlacementBudget` | none | Classic: `C_HousingDecor.GetMaxPlacementBudget()`. | shim |
| `C_HousingDecor.GetSpentPlacementBudget` | none | Classic: `C_HousingDecor.GetSpentPlacementBudget()`. | shim |
| `C_HousingLayout.GetNumFloors` | `C_HousingLayout.GetHighestOccupiedFloorIndex`<br>`C_HousingLayout.GetLowestOccupiedFloorIndex` | Classic: `C_HousingLayout.GetNumFloors()`. | shim |
| `C_HousingLayout.GetRoomPlacementBudget` | none | Classic: `C_HousingLayout.GetRoomPlacementBudget()`. | shim |
| `C_HousingLayout.GetSpentPlacementBudget` | none | Classic: `C_HousingLayout.GetSpentPlacementBudget()`. | shim |
| `C_Spell.GetMawPowerBorderAtlasBySpellID` | `C_Spell.GetMawPowerRarityInfoBySpellID` | Classic: `C_Spell.GetMawPowerBorderAtlasBySpellID(spellID)`. | shim |
| `C_Spell.GetSpellLossOfControlCooldown` | `C_Spell.GetSpellLossOfControlCooldownInfo` *secret in combat* | Classic: `C_Spell.GetSpellLossOfControlCooldown(spellIdentifier)`. | shim |
| `C_SpellBook.GetSpellBookItemLossOfControlCooldown` | `C_SpellBook.GetSpellBookItemLossOfControlCooldownInfo` *secret in combat* | Classic: `C_SpellBook.GetSpellBookItemLossOfControlCooldown(spellBookItem)`. | shim |
| `C_SuperTrack.GetNextWaypointForMap` | `C_Navigation.GetNextWaypointForMap` |  | shim |
| `C_TransmogOutfitInfo.GetWeaponOptionsForSlot` | `C_TransmogOutfitInfo.GetOptionsForSlot` |  | shim |
| `C_TransmogOutfitInfo.SetViewedWeaponOptionForSlot` | `C_TransmogOutfitInfo.SetViewedOptionForSlot` |  | shim |
| `C_UnitAuras.AddPrivateAuraAppliedSound` | `C_UnitAuras.AddAuraSound` | Classic: `C_UnitAuras.AddPrivateAuraAppliedSound(sound)`. | shim |
| `C_UnitAuras.RemovePrivateAuraAppliedSound` | `C_UnitAuras.RemoveAuraSound` |  | shim |
| `CancelEmote` | `C_ChatInfo.CancelEmote` | Classic: `CancelEmote()`. | shim |
| `CancelItemTempEnchantment` | `C_PaperDollInfo.CancelTemporaryEnchantment` | Classic: `CancelItemTempEnchantment(index)`. | shim |
| `ChangeActionBarPage` | `C_ActionBar.SetActionBarPage` | Classic: `ChangeActionBarPage(pageIndex)`. | shim |
| `Chat_AddSystemMessage` | `ChatFrameUtil.AddSystemMessage` |  | shim |
| `Chat_GetChannelColor` | `ChatFrameUtil.GetChannelColor` |  | shim |
| `Chat_GetChannelShortcutName` | `ChatFrameUtil.GetChannelShortcutName` |  | shim |
| `Chat_GetChatCategory` | `ChatFrameUtil.GetChatCategory` |  | shim |
| `Chat_GetChatFrame` | `ChatFrameUtil.GetChatFrame` |  | shim |
| `Chat_GetColoredChatName` | `ChatFrameUtil.GetColoredChatName` |  | shim |
| `Chat_GetCommunitiesChannel` | `ChatFrameUtil.GetCommunitiesChannel` |  | shim |
| `Chat_GetCommunitiesChannelColor` | `ChatFrameUtil.GetCommunitiesChannelColor` |  | shim |
| `Chat_GetCommunitiesChannelName` | `ChatFrameUtil.GetCommunitiesChannelName` |  | shim |
| `Chat_ShouldColorChatByClass` | `ChatFrameUtil.ShouldColorChatByClass` |  | shim |
| `ChatEdit_ActivateChat` | `ChatFrameUtil.ActivateChat` |  | shim |
| `ChatEdit_AddHistory` | `ChatFrameEditBoxMixin.AddHistory` |  | shim |
| `ChatEdit_ChooseBoxForSend` | `ChatFrameUtil.ChooseBoxForSend` |  | shim |
| `ChatEdit_ClearChat` | `ChatFrameEditBoxMixin.ClearChat` |  | shim |
| `ChatEdit_DeactivateChat` | `ChatFrameUtil.DeactivateChat` |  | shim |
| `ChatEdit_DoesCurrentChannelTargetMatch` | `ChatFrameEditBoxMixin.DoesCurrentChannelTargetMatch` |  | shim |
| `ChatEdit_ExtractChannel` | `ChatFrameEditBoxMixin.ExtractChannel` |  | shim |
| `ChatEdit_ExtractTellTarget` | `ChatFrameEditBoxMixin.ExtractTellTarget` |  | shim |
| `ChatEdit_FocusActiveWindow` | `ChatFrameUtil.FocusActiveWindow` |  | shim |
| `ChatEdit_GetActiveChatType` | `ChatFrameUtil.GetActiveChatType` |  | shim |
| `ChatEdit_GetChannelTarget` | `ChatFrameEditBoxMixin.GetChannelTarget` |  | shim |
| `ChatEdit_GetLastActiveWindow` | `ChatFrameUtil.GetLastActiveWindow` |  | shim |
| `ChatEdit_GetLastTellTarget` | `ChatFrameUtil.GetLastTellTarget` |  | shim |
| `ChatEdit_GetLastToldTarget` | `ChatFrameUtil.GetLastToldTarget` |  | shim |
| `ChatEdit_GetNextTellTarget` | `ChatFrameUtil.GetNextTellTarget` |  | shim |
| `ChatEdit_HandleChatType` | `ChatFrameEditBoxMixin.HandleChatType` |  | shim |
| `ChatEdit_HasStickyFocus` | `ChatFrameUtil.HasStickyFocus` |  | shim |
| `ChatEdit_LinkItem` | `ChatFrameUtil.LinkItem` |  | shim |
| `ChatEdit_ParseText` | `ChatFrameEditBoxMixin.ParseText` |  | shim |
| `ChatEdit_ResetChatType` | `ChatFrameEditBoxMixin.ResetChatType` |  | shim |
| `ChatEdit_ResetChatTypeToSticky` | `ChatFrameEditBoxMixin.ResetChatTypeToSticky` |  | shim |
| `ChatEdit_SendText` | `ChatFrameEditBoxMixin.SendText` |  | shim |
| `ChatEdit_SetDeactivated` | `ChatFrameEditBoxMixin.Deactivate` |  | shim |
| `ChatEdit_SetLastActiveWindow` | `ChatFrameUtil.SetLastActiveWindow` |  | shim |
| `ChatEdit_SetLastTellTarget` | `ChatFrameUtil.SetLastTellTarget` |  | shim |
| `ChatEdit_SetLastToldTarget` | `ChatFrameUtil.SetLastToldTarget` |  | shim |
| `ChatEdit_TryInsertChatLink` | `ChatFrameUtil.TryInsertChatLink` |  | shim |
| `ChatEdit_TryInsertQuestLinkForQuestID` | `ChatFrameUtil.TryInsertQuestLinkForQuestID` |  | shim |
| `ChatEdit_UpdateHeader` | `ChatFrameEditBoxMixin.UpdateHeader` |  | shim |
| `ChatFrame_AddCommunitiesChannel` | `ChatFrameUtil.AddCommunitiesChannel` |  | shim |
| `ChatFrame_AddMessage` | `ChatFrameMixin.AddMessage` |  | shim |
| `ChatFrame_AddMessageGroup` | `ChatFrameMixin.AddMessageGroup` |  | shim |
| `ChatFrame_AddPrivateMessageTarget` | `ChatFrameMixin.AddPrivateMessageTarget` |  | shim |
| `ChatFrame_AddSingleMessageType` | `ChatFrameMixin.AddSingleMessageType` |  | shim |
| `ChatFrame_CanAddChannel` | `ChatFrameUtil.CanAddChannel` |  | shim |
| `ChatFrame_CanChatGroupPerformExpressionExpansion` | `ChatFrameUtil.CanChatGroupPerformExpressionExpansion` |  | shim |
| `ChatFrame_ChatPageDown` | `ChatFrameUtil.ChatPageDown` |  | shim |
| `ChatFrame_ChatPageUp` | `ChatFrameUtil.ChatPageUp` |  | shim |
| `ChatFrame_ClearChatFocusOverride` | `ChatFrameUtil.ClearChatFocusOverride` |  | shim |
| `ChatFrame_ContainsChannel` | `ChatFrameMixin.ContainsChannel` |  | shim |
| `ChatFrame_ContainsMessageGroup` | `ChatFrameMixin.ContainsMessageGroup` |  | shim |
| `ChatFrame_DisplayChatHelp` | `ChatFrameUtil.DisplayChatHelp` |  | shim |
| `ChatFrame_DisplayGameTime` | `ChatFrameUtil.DisplayGameTime` |  | shim |
| `ChatFrame_DisplayGMOTD` | `ChatFrameUtil.DisplayGMOTD` |  | shim |
| `ChatFrame_DisplayHelpText` | `ChatFrameUtil.DisplayHelpText` |  | shim |
| `ChatFrame_DisplayHelpTextSimple` | `ChatFrameUtil.DisplayHelpTextSimple` |  | shim |
| `ChatFrame_DisplayMacroHelpText` | `ChatFrameUtil.DisplayMacroHelpText` |  | shim |
| `ChatFrame_DisplaySystemMessage` | `ChatFrameUtil.DisplaySystemMessage` |  | shim |
| `ChatFrame_DisplaySystemMessageInCurrent` | `ChatFrameUtil.DisplaySystemMessageInCurrent` |  | shim |
| `ChatFrame_DisplaySystemMessageInPrimary` | `ChatFrameUtil.DisplaySystemMessageInPrimary` |  | shim |
| `ChatFrame_DisplayTimePlayed` | `ChatFrameUtil.DisplayTimePlayed` |  | shim |
| `ChatFrame_DisplayUsageError` | `ChatFrameUtil.DisplayUsageError` |  | shim |
| `ChatFrame_ExcludePrivateMessageTarget` | `ChatFrameMixin.ExcludePrivateMessageTarget` |  | shim |
| `ChatFrame_GetChatFocusOverride` | `ChatFrameUtil.GetChatFocusOverride` |  | shim |
| `ChatFrame_GetCommunitiesChannelLocalID` | `ChatFrameUtil.GetCommunitiesChannelLocalID` |  | shim |
| `ChatFrame_GetCommunityAndStreamFromChannel` | `ChatFrameUtil.GetCommunityAndStreamFromChannel` |  | shim |
| `ChatFrame_GetCommunityAndStreamName` | `ChatFrameUtil.GetCommunityAndStreamName` |  | shim |
| `ChatFrame_GetDefaultChatTarget` | `ChatFrameMixin.GetDefaultChatTarget` |  | shim |
| `ChatFrame_GetFullChannelInfo` | `ChatFrameUtil.GetFullChannelInfo` |  | shim |
| `ChatFrame_GetMobileEmbeddedTexture` | `ChatFrameUtil.GetMobileEmbeddedTexture` |  | shim |
| `ChatFrame_ReceiveAllPrivateMessages` | `ChatFrameMixin.ReceiveAllPrivateMessages` |  | shim |
| `ChatFrame_RegisterForChannels` | `ChatFrameMixin.RegisterForChannels` |  | shim |
| `ChatFrame_RegisterForMessages` | `ChatFrameMixin.RegisterForMessages` |  | shim |
| `ChatFrame_RemoveAllChannels` | `ChatFrameMixin.RemoveAllChannels` |  | shim |
| `ChatFrame_RemoveAllMessageGroups` | `ChatFrameMixin.RemoveAllMessageGroups` |  | shim |
| `ChatFrame_RemoveChannel` | `ChatFrameMixin.RemoveChannel` |  | shim |
| `ChatFrame_RemoveCommunitiesChannel` | `ChatFrameUtil.RemoveCommunitiesChannel` |  | shim |
| `ChatFrame_RemoveExcludePrivateMessageTarget` | `ChatFrameMixin.RemoveExcludePrivateMessageTarget` |  | shim |
| `ChatFrame_RemoveMessageGroup` | `ChatFrameMixin.RemoveMessageGroup` |  | shim |
| `ChatFrame_RemovePrivateMessageTarget` | `ChatFrameMixin.RemovePrivateMessageTarget` |  | shim |
| `ChatFrame_ReplyTell` | `ChatFrameUtil.ReplyTell` |  | shim |
| `ChatFrame_ReplyTell2` | `ChatFrameUtil.ReplyTell2` |  | shim |
| `ChatFrame_ResolveChannelName` | `ChatFrameUtil.ResolveChannelName` |  | shim |
| `ChatFrame_ResolvePrefixedChannelName` | `ChatFrameUtil.ResolvePrefixedChannelName` |  | shim |
| `ChatFrame_ScrollDown` | `ChatFrameUtil.ScrollDown` |  | shim |
| `ChatFrame_ScrollToBottom` | `ChatFrameUtil.ScrollToBottom` |  | shim |
| `ChatFrame_ScrollUp` | `ChatFrameUtil.ScrollUp` |  | shim |
| `ChatFrame_SendTell` | `ChatFrameUtil.SendTell` |  | shim |
| `ChatFrame_SendTellWithMessage` | `ChatFrameUtil.SendTellWithMessage` |  | shim |
| `ChatFrame_SetChatFocusOverride` | `ChatFrameUtil.SetChatFocusOverride` |  | shim |
| `ChatFrame_TimeBreakDown` | `ChatFrameUtil.TimeBreakDown` |  | shim |
| `ChatFrame_TruncateToMaxLength` | `ChatFrameUtil.TruncateToMaxLength` |  | shim |
| `ChatFrame_UnregisterAllMessageGroups` | `ChatFrameMixin.UnregisterAllMessageGroups` |  | shim |
| `ChatFrame_UpdateChatFrames` | `ChatFrameUtil.UpdateChatFrames` |  | shim |
| `ChatFrame_UpdateColorByID` | `ChatFrameMixin.UpdateColorByID` |  | shim |
| `ChatFrame_UpdateDefaultChatTarget` | `ChatFrameMixin.UpdateDefaultChatTarget` |  | shim |
| `CombatLog_Color_ColorArrayByEventType` | `CombatLogUtil.GetColorByEventType` | Classic: `CombatLog_Color_ColorArrayByEventType(event, filterSettings)`. | shim |
| `CombatLog_Color_ColorArrayBySchool` | `CombatLogUtil.GetColorBySchool` | Classic: `CombatLog_Color_ColorArrayBySchool(school, filterSettings)`. | shim |
| `CombatLog_Color_ColorArrayByUnitType` | `CombatLogUtil.GetColorByUnitType` | Classic: `CombatLog_Color_ColorArrayByUnitType(unitFlags, filterSettings)`. | shim |
| `CombatLog_Color_ColorStringByEventType` | none | Classic: `CombatLog_Color_ColorStringByEventType(unitFlags, filterSettings)`. | shim |
| `CombatLog_Color_ColorStringBySchool` | none | Classic: `CombatLog_Color_ColorStringBySchool(school, filterSettings)`. | shim |
| `CombatLog_Color_ColorStringByUnitType` | none | Classic: `CombatLog_Color_ColorStringByUnitType(unitFlags, filterSettings)`. | shim |
| `CombatLog_Color_FloatToText` | none | Classic: `CombatLog_Color_FloatToText(r, g, b, a)`. | shim |
| `CombatLog_Color_HighlightColorArray` | `CombatLogUtil.HighlightColor` |  | shim |
| `CombatLog_Object_IsA` | `C_CombatLog.DoesObjectMatchFilter` |  | shim |
| `CombatLog_String_DamageResultString` | `CombatLogUtil.GenerateDamageResultString` |  | shim |
| `CombatLog_String_GetIcon` | `CombatLogUtil.GetUnitIcon` |  | shim |
| `CombatLog_String_PowerType` | `CombatLogUtil.GetPowerTypeString` |  | shim |
| `CombatLog_String_SchoolString` | `CombatLogUtil.GetSpellSchoolString` |  | shim |
| `CombatLogClearEntries` | `C_CombatLog.ClearEntries` |  | shim |
| `CombatLogGetRetentionTime` | `C_CombatLog.GetEntryRetentionTime` |  | shim |
| `CombatLogSetRetentionTime` | `C_CombatLog.SetEntryRetentionTime` |  | shim |
| `CombatTextSetActiveUnit` | `C_CombatText.SetActiveUnit` |  | shim |
| `ConfirmReadyCheck` | `C_PartyInfo.ConfirmReadyCheck` | Classic: `ConfirmReadyCheck(isReady)`. | shim |
| `DeathRecap_GetEvents` | `C_DeathRecap.GetRecapEvents` |  | shim |
| `DeathRecap_HasEvents` | `C_DeathRecap.HasRecapEvents` |  | shim |
| `DemoteAssistant` | `C_PartyInfo.DemoteAssistant` | Classic: `DemoteAssistant(name, exactNameMatch)`. | shim |
| `DoEmote` | `C_ChatInfo.PerformEmote`<br>`C_ChatInfo.CancelEmote` | Classic: `DoEmote(emoteName, targetName, suppressMoveError)`. | shim |
| `DoReadyCheck` | `C_PartyInfo.DoReadyCheck` | Classic: `DoReadyCheck()`. | shim |
| `FindBaseSpellByID` | `C_SpellBook.FindBaseSpellByID` | Classic: `FindBaseSpellByID(spellID)`. | shim |
| `FindFlyoutSlotBySpellID` | `C_SpellBook.FindFlyoutSlotBySpellID` | Classic: `FindFlyoutSlotBySpellID(spellID)`. | shim |
| `FindSpellOverrideByID` | `C_SpellBook.FindSpellOverrideByID` | Classic: `FindSpellOverrideByID(spellID)`. | shim |
| `GetActionAutocast` | `C_ActionBar.GetActionAutocast` | Classic: `GetActionAutocast(actionID)`. | shim |
| `GetActionBarPage` | `C_ActionBar.GetActionBarPage` | Classic: `GetActionBarPage()`. | shim |
| `GetActionCharges` | `C_ActionBar.GetActionCharges` *secret in combat* | Classic: `GetActionCharges(actionID)`. | shim |
| `GetActionCooldown` | `C_ActionBar.GetActionCooldown` *secret in combat* | Classic: `GetActionCooldown(actionID)`. | shim |
| `GetActionCount` | `C_ActionBar.GetActionUseCount` *secret in combat* | Classic: `GetActionCount(actionID)`. | shim |
| `GetActionLossOfControlCooldown` | `C_ActionBar.GetActionLossOfControlCooldown` | Classic: `GetActionLossOfControlCooldown(actionID)`. | shim |
| `GetActionText` | `C_ActionBar.GetActionText` | Classic: `GetActionText(actionID)`. | shim |
| `GetActionTexture` | `C_ActionBar.GetActionTexture` | Classic: `GetActionTexture(actionID)`. | shim |
| `GetAutoCompletePresenceID` | `C_AutoComplete.GetAutoCompletePresenceID` | Classic: `GetAutoCompletePresenceID(name)`. | shim |
| `GetAutoCompleteRealms` | `C_AutoComplete.GetAutoCompleteRealms` | Classic: `GetAutoCompleteRealms()`. | shim |
| `GetAutoCompleteResults` | `C_AutoComplete.GetAutoCompleteResults` | Classic: `GetAutoCompleteResults(name, numResults, cursorPosition, allowFullMatch, includeFlags, excludeFlags)`. | shim |
| `GetBattlefieldScore` | `C_PvP.GetScoreInfo` | Classic: `GetBattlefieldScore(playerIndex)`. | shim |
| `GetBattlefieldStatData` | `C_PvP.GetScoreInfo` | Classic: `GetBattlefieldStatData(playerIndex, statIndex)`. | shim |
| `GetBonusBarIndex` | `C_ActionBar.GetBonusBarIndex` | Classic: `GetBonusBarIndex()`. | shim |
| `GetBonusBarOffset` | `C_ActionBar.GetBonusBarOffset` | Classic: `GetBonusBarOffset()`. | shim |
| `GetChatTimestampFormat` | `ChatFrameUtil.GetTimestampFormat` |  | shim |
| `GetCurrentCombatTextEventInfo` | `C_CombatText.GetCurrentEventInfo` *always secret* |  | shim |
| `GetDeathRecapLink` | `C_DeathRecap.GetRecapLink` |  | shim |
| `GetExtraBarIndex` | `C_ActionBar.GetExtraBarIndex` | Classic: `GetExtraBarIndex()`. | shim |
| `getglobal` | none | Classic: `getglobal(var)`. | shim |
| `GetGuildInfoText` | `C_GuildInfo.GetInfoText` |  | shim |
| `GetGuildRosterMOTD` | `C_GuildInfo.GetMOTD` |  | shim |
| `GetInspectSpecialization` | `C_SpecializationInfo.GetInspectSpecialization` *secret in combat* |  | shim |
| `GetInventorySlotInfo` | `C_PaperDollInfo.GetInventorySlotInfo` |  | shim |
| `GetMaxSpellStartRecoveryOffset` | `C_Spell.GetSpellQueueWindow` |  | shim |
| `GetMerchantCurrencies` | `C_MerchantFrame.GetMerchantCurrencies` | Classic: `GetMerchantCurrencies()`. | shim |
| `GetMultiCastBarIndex` | `C_ActionBar.GetMultiCastBarIndex` | Classic: `GetMultiCastBarIndex()`. | shim |
| `GetOverrideBarIndex` | `C_ActionBar.GetOverrideBarIndex` | Classic: `GetOverrideBarIndex()`. | shim |
| `GetOverrideBarSkin` | `C_ActionBar.GetOverrideBarSkin` | Classic: `GetOverrideBarSkin()`. | shim |
| `GetSchoolString` | `C_Spell.GetSchoolString` |  | shim |
| `GetSpellQueueWindow` | `C_Spell.GetSpellQueueWindow` |  | shim |
| `GetTempShapeshiftBarIndex` | `C_ActionBar.GetTempShapeshiftBarIndex` | Classic: `GetTempShapeshiftBarIndex()`. | shim |
| `GetVehicleBarIndex` | `C_ActionBar.GetVehicleBarIndex` | Classic: `GetVehicleBarIndex()`. | shim |
| `GetWeaponEnchantInfo` | `C_PaperDollInfo.GetTemporaryEnchantmentInfo` | Classic: `GetWeaponEnchantInfo()`. | shim |
| `GuildDemote` | `C_GuildInfo.Demote` |  | shim |
| `GuildDisband` | `C_GuildInfo.Disband` |  | shim |
| `GuildInvite` | `C_GuildInfo.Invite` |  | shim |
| `GuildLeave` | `C_GuildInfo.Leave` |  | shim |
| `GuildPromote` | `C_GuildInfo.Promote` |  | shim |
| `GuildSetLeader` | `C_GuildInfo.SetLeader` |  | shim |
| `GuildSetMOTD` | `C_GuildInfo.SetMOTD` |  | shim |
| `GuildUninvite` | `C_GuildInfo.Uninvite` |  | shim |
| `HasAction` | `C_ActionBar.HasAction` | Classic: `HasAction(actionID)`. | shim |
| `HasBonusActionBar` | `C_ActionBar.HasBonusActionBar` | Classic: `HasBonusActionBar()`. | shim |
| `HasExtraActionBar` | `C_ActionBar.HasExtraActionBar` | Classic: `HasExtraActionBar()`. | shim |
| `HasOverrideActionBar` | `C_ActionBar.HasOverrideActionBar` | Classic: `HasOverrideActionBar()`. | shim |
| `HasTempShapeshiftActionBar` | `C_ActionBar.HasTempShapeshiftActionBar` | Classic: `HasTempShapeshiftActionBar()`. | shim |
| `HasVehicleActionBar` | `C_ActionBar.HasVehicleActionBar` | Classic: `HasVehicleActionBar()`. | shim |
| `IsActionInRange` | `C_ActionBar.IsActionInRange` | Classic: `IsActionInRange(actionID)`. | shim |
| `IsAttackAction` | `C_ActionBar.IsAttackAction` | Classic: `IsAttackAction(actionID)`. | shim |
| `IsAutoRepeatAction` | `C_ActionBar.IsAutoRepeatAction` | Classic: `IsAutoRepeatAction(actionID)`. | shim |
| `IsConsumableAction` | `C_ActionBar.IsConsumableAction` | Classic: `IsConsumableAction(actionID)`. | shim |
| `IsCurrentAction` | `C_ActionBar.IsCurrentAction` | Classic: `IsCurrentAction(actionID)`. | shim |
| `IsEncounterInProgress` | `C_InstanceEncounter.IsEncounterInProgress` | Classic: `IsEncounterInProgress()`. | shim |
| `IsEncounterLimitingResurrections` | `C_InstanceEncounter.IsEncounterLimitingResurrections` | Classic: `IsEncounterLimitingResurrections()`. | shim |
| `IsEncounterSuppressingRelease` | `C_InstanceEncounter.IsEncounterSuppressingRelease` | Classic: `IsEncounterSuppressingRelease()`. | shim |
| `IsEquippedAction` | `C_ActionBar.IsEquippedAction` | Classic: `IsEquippedAction(actionID)`. | shim |
| `IsGUIDInGroup` | `C_PartyInfo.IsGUIDInGroup` | Classic: `IsGUIDInGroup(guid, category)`. | shim |
| `IsItemAction` | `C_ActionBar.IsItemAction` | Classic: `IsItemAction(actionID)`. | shim |
| `IsPossessBarVisible` | `C_ActionBar.IsPossessBarVisible` | Classic: `IsPossessBarVisible()`. | shim |
| `IsRecognizedName` | `C_AutoComplete.IsRecognizedName` | Classic: `IsRecognizedName(name, includeFlags, excludeFlags)`. | shim |
| `IsSpellKnownOrOverridesKnown` | `C_SpellBook.IsSpellInSpellBook` | Classic: `IsSpellKnownOrOverridesKnown(spellID, isPet)`. | shim |
| `IsStackableAction` | `C_ActionBar.IsStackableAction` | Classic: `IsStackableAction(actionID)`. | shim |
| `IsUsableAction` | `C_ActionBar.IsUsableAction` | Classic: `IsUsableAction(actionID)`. | shim |
| `MenuUtil.HideTooltip` | `MenuUtil.HideTooltipEx`<br>`GetAppropriateTooltip` | Classic: `MenuUtil.HideTooltip(owner)`. | shim |
| `MenuUtil.ShowTooltip` | `MenuUtil.ShowTooltipEx`<br>`GetAppropriateTooltip` | Classic: `MenuUtil.ShowTooltip(owner, func, ...)`. | shim |
| `OptionsListButton_OnClick` | none | Classic: `OptionsListButton_OnClick(self, mouseButton)`. | shim |
| `OptionsListButton_OnEnter` | none | Classic: `OptionsListButton_OnEnter(self)`. | shim |
| `OptionsListButton_OnLeave` | `GetAppropriateTooltip` | Classic: `OptionsListButton_OnLeave(self)`. | shim |
| `OptionsListButton_OnLoad` | none | Classic: `OptionsListButton_OnLoad(self, toggleFunc)`. | shim |
| `OptionsListButtonToggle_OnClick` | none | Classic: `OptionsListButtonToggle_OnClick(self)`. | shim |
| `PromoteToAssistant` | `C_PartyInfo.PromoteToAssistant` | Classic: `PromoteToAssistant(name, exactNameMatch)`. | shim |
| `PromoteToLeader` | `C_PartyInfo.PromoteToLeader` | Classic: `PromoteToLeader(name, exactNameMatch)`. | shim |
| `RaidNotice_AddMessage` | `RaidWarningUtil.AddMessage` | Classic: `RaidNotice_AddMessage(_noticeFrame, textString, colorInfo, displayTime)`. | shim |
| `RaidNotice_Clear` | none | Classic: `RaidNotice_Clear(noticeFrame)`. | shim |
| `RaidNotice_FadeInit` | none | Classic: `RaidNotice_FadeInit(slotFrame)`. | shim |
| `RaidNotice_UpdateSlot` | none | Classic: `RaidNotice_UpdateSlot(slotFrame, timings, elapsedTime, hasFading)`. | shim |
| `SetActionUIButton` | `C_ActionBar.RegisterActionUIButton` | Classic: `SetActionUIButton(checkboxFrame, actionID, cooldownFrame)`. | shim |
| `SetEveryoneIsAssistant` | `C_PartyInfo.SetEveryoneIsAssistant` | Classic: `SetEveryoneIsAssistant(isAssistant)`. | shim |
| `setglobal` | none | Classic: `setglobal(var, val)`. | shim |
| `SetGuildInfoText` | `C_GuildInfo.SetInfoText` |  | shim |
| `ShowBossFrameWhenUninteractable` | `UnitIsVisible` | Classic: `ShowBossFrameWhenUninteractable(unit)`. | shim |
| `SpellGetVisibilityInfo` | `C_Spell.GetVisibilityInfo` | Classic: `SpellGetVisibilityInfo(spellID, visiblityTypeName)`. | shim |
| `SpellIsPriorityAura` | `C_Spell.IsPriorityAura` | Classic: `SpellIsPriorityAura(spellID)`. | shim |
| `SpellIsSelfBuff` | `C_Spell.IsSelfBuff` | Classic: `SpellIsSelfBuff(spellID)`. | shim |
| `SubstituteChatMessageBeforeSend` | `ChatFrameUtil.SubstituteChatMessageBeforeSend` |  | shim |
| `TargetSpellReplacesBonusTree` | `C_Spell.TargetSpellReplacesBonusTree` |  | shim |
| `UninviteUnit` | `C_PartyInfo.UninviteUnit` | Classic: `UninviteUnit(unit, reason, exactNameMatch)`. | shim |
| `UnitIsSpellTarget` | `PlayerIsSpellTarget` *always secret* | Classic: `UnitIsSpellTarget(unit, target)`. | shim |

## Still there (1)

| Classic | Forever | How it changed | Source |
|---|---|---|---|
| `SelectGossipOption` | `C_GossipInfo.SelectOption` | Takes the option's gossipOptionID (from GetOptions) instead of its index. | curated |

## Classic add-on calls with no known home yet

Globals the scanned classic add-ons call that aren't in the game, and nothing above maps. Some are the add-ons' own helpers that the scan couldn't tell apart; the rest need an entry in sources/relocated.json.

- `os.exit` (10× by Questie)
- `GetMinimapShape` (3× by AlexAtlasLoot, Questie)
- `C_QuestLog_GetQuestObjectives` (2× by Questie)
- `C_TimerAfter` (2× by Questie)
- `AchievementFrameAchievements_ForceUpdate` (1× by Questie)
- `AchievementFrame_SelectAchievement` (1× by Questie)
- `AchievementFrame_ToggleAchievementFrame` (1× by Questie)
- `ActionStatus_DisplayMessage` (1× by Questie)
- `C_ChallengeMode.GetChallengeModeMapTimes` (1× by Questie)
- `C_DateAndTime.GetTodaysDate` (1× by Questie)
- `C_QuestLog.GetAbandonQuestName` (1× by Questie)
- `C_QuestLog.GetQuestLink` (1× by Questie)
- `HandleCommand` (1× by Questie)
- `IsDoable` (1× by Questie)
- `IsLevelRequirementsFulfilled` (1× by Questie)
- `MouseIsOver` (1× by Questie)
- `OnQuestAdded` (1× by Questie)
- `OnScenarioCriteriaAdded` (1× by Questie)
- `OnTrackedQuestClick` (1× by Questie)
- `QIsComplete` (1× by Questie)
- `QuestLog_SetSelection` (1× by Questie)
- `QuestLog_Update` (1× by Questie)
- `QuestLog_UpdateQuestDetails` (1× by Questie)
- `QuestWatch_Update` (1× by Questie)
- `StaticPopup_Resize` (1× by Questie)
- `debug.getinfo` (1× by Questie)
