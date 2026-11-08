# Restrictions seen in game

- Out of combat run: done; restrictions active at start: Map
- In combat run: done; restrictions active at start: Map

## Getters that answered differently in combat

| Function | Out of combat | In combat |
|---|---|---|
| `C_ActionBar.GetActionCharges` | returned 1 value: `table{chargeModRate=number,cooldownDuration=number,cooldownStartTime=number,currentCharges=number,isActive=boolean,maxCharges=number}` | returned 1 value: `table{chargeModRate=secret,cooldownDuration=secret,cooldownStartTime=secret,currentCharges=secret,isActive=boolean,maxCharges=number}` |
| `C_ActionBar.GetActionCooldown` | returned 1 value: `table{duration=number,isActive=boolean,isEnabled=boolean,modRate=number,startTime=number}` | returned 1 value: `table{duration=secret,isActive=boolean,isEnabled=boolean,modRate=secret,startTime=secret}` |
| `C_ActionBar.GetActionDisplayCount` | returned 1 value: `string` | returned 1 value: `secret:string` |
| `C_ActionBar.GetActionLossOfControlCooldownInfo` | returned 1 value: `table{duration=number,isActive=boolean,modRate=number,shouldReplaceNormalCooldown=boolean,startTime=number}` | returned 1 value: `table{duration=secret,isActive=boolean,modRate=secret,shouldReplaceNormalCooldown=boolean,startTime=secret}` |
| `C_ActionBar.GetActionUseCount` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `C_ClassTalents.CanChangeTalents` | returned 3 values: `boolean`, `boolean`, `nil` | returned 3 values: `boolean`, `boolean`, `string` |
| `C_Club.GetAvatarIdList` | returned 1 value: `nil` | returned 1 value: `table{[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,...(106)}` |
| `C_DamageMeter.GetAvailableCombatSessions` | returned 1 value: `table{}` | returned 1 value: `table{[number]=table}` |
| `C_DamageMeter.GetCombatSessionFromType` | returned 1 value: `table{combatSources=table,maxAmount=number,totalAmount=number}` | returned 1 value: `table{combatSources=table,maxAmount=secret,totalAmount=secret}` |
| `C_DamageMeter.GetCombatSessionSourceFromType` | returned 1 value: `table{combatSpells=table,maxAmount=number,totalAmount=number}` | returned 1 value: `table{combatSpells=table,maxAmount=secret,totalAmount=secret}` |
| `C_Discord.GetDiscordChannelName` | ⛔ protected: calling it raised ADDON_ACTION_FORBIDDEN | not called: forbidden |
| `C_Discord.GetNumDiscordChannels` | ⛔ protected: calling it raised ADDON_ACTION_FORBIDDEN | not called: forbidden |
| `C_Discord.GetServerLinkableChannels` | ⛔ protected: calling it raised ADDON_ACTION_FORBIDDEN | not called: forbidden |
| `C_Discord.GetServerName` | ⛔ protected: calling it raised ADDON_ACTION_FORBIDDEN | not called: forbidden |
| `C_Discord.IsGuildSettingSet` | ⛔ protected: calling it raised ADDON_ACTION_FORBIDDEN | not called: forbidden |
| `C_GamepadUI.GetFirstGamepadActionBarStorageSlotIndexForActiveStance` | returned 1 value: `nil` | returned 1 value: `number` |
| `C_NamePlate.GetNamePlates` | returned 1 value: `table{}` | returned 1 value: `table{[number]=table,[number]=table,[number]=table}` |
| `C_Spell.GetSpellCastCount` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `C_Spell.GetSpellCooldown` | returned 1 value: `table{duration=number,isActive=boolean,isEnabled=boolean,modRate=number,startTime=number}` | returned 1 value: `table{duration=secret,isActive=boolean,isEnabled=boolean,modRate=secret,startTime=secret}` |
| `C_Spell.GetSpellDisplayCount` | returned 1 value: `string` | returned 1 value: `secret:string` |
| `C_Spell.GetSpellLossOfControlCooldownInfo` | returned 1 value: `table{duration=number,isActive=boolean,modRate=number,shouldReplaceNormalCooldown=boolean,startTime=number}` | returned 1 value: `table{duration=secret,isActive=boolean,modRate=secret,shouldReplaceNormalCooldown=boolean,startTime=secret}` |
| `C_Spell.GetSpellMaxCumulativeAuraApplications` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `C_Spell.IsActiveSpell` | returned 1 value: `boolean` | returned 1 value: `secret:boolean` |
| `C_SpellBook.GetSpellBookItemCastCount` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `C_SpellBook.GetSpellBookItemCooldown` | returned 1 value: `table{duration=number,isActive=boolean,isEnabled=boolean,modRate=number,startTime=number}` | returned 1 value: `table{duration=secret,isActive=boolean,isEnabled=boolean,modRate=secret,startTime=secret}` |
| `C_SpellBook.GetSpellBookItemLossOfControlCooldownInfo` | returned 1 value: `table{duration=number,isActive=boolean,modRate=number,shouldReplaceNormalCooldown=boolean,startTime=number}` | returned 1 value: `table{duration=secret,isActive=boolean,modRate=secret,shouldReplaceNormalCooldown=boolean,startTime=secret}` |
| `C_TooltipInfo.GetShapeshift` | returned 1 value: `table{dataInstanceID=number,id=number,lines=table,type=number}` | returned 1 value: `table{dataInstanceID=number,hasDynamicData=secret,id=number,lines=table,type=number}` |
| `C_TooltipInfo.GetUnitAura` | returned 0 values | error: `GetUnitAura(): Auras cannot be accessed when secret while tainted by 'ApiProbe'
Lua Taint: ApiProbe` |
| `C_TooltipInfo.GetUnitBuff` | returned 1 value: `table{dataInstanceID=number,id=number,lines=table,type=number}` | error: `GetUnitBuff(): Auras cannot be accessed when secret while tainted by 'ApiProbe'
Lua Taint: ApiProbe` |
| `C_TooltipInfo.GetUnitDebuff` | returned 0 values | error: `GetUnitDebuff(): Auras cannot be accessed when secret while tainted by 'ApiProbe'
Lua Taint: ApiProbe` |
| `C_UnitAuras.GetAuraDataByIndex` | returned 1 value: `table{applications=number,auraInstanceID=number,canActivePlayerDispel=boolean,canApplyAura=boolean,dispelName=string,duration=number,expirationTime=number,hideOnPartyFrames=boolean,icon=number,isBossAura=boolean,isDPSRoleAura=boolean,isFromPlayerOrPlayerPet=boolean,isHarmful=boolean,isHealerRoleAura=boolean,isHelpful=boolean,isNameplateOnly=boolean,isRaid=boolean,isStealable=boolean,isTankRoleAura=boolean,name=string,nameplateShowAll=boolean,nameplateShowPersonal=boolean,points=table,sourceUnit=string,spellId=number,timeMod=number}` | error: `GetAuraDataByIndex(): Auras cannot be accessed when secret while tainted by 'ApiProbe'
Lua Taint: ApiProbe` |
| `C_UnitAuras.GetAuraDataBySlot` | returned 1 value: `table{applications=number,auraInstanceID=number,canActivePlayerDispel=boolean,canApplyAura=boolean,dispelName=string,duration=number,expirationTime=number,hideOnPartyFrames=boolean,icon=number,isBossAura=boolean,isDPSRoleAura=boolean,isFromPlayerOrPlayerPet=boolean,isHarmful=boolean,isHealerRoleAura=boolean,isHelpful=boolean,isNameplateOnly=boolean,isRaid=boolean,isStealable=boolean,isTankRoleAura=boolean,name=string,nameplateShowAll=boolean,nameplateShowPersonal=boolean,points=table,sourceUnit=string,spellId=number,timeMod=number}` | error: `GetAuraDataBySlot(): Auras cannot be accessed when secret while tainted by 'ApiProbe'
Lua Taint: ApiProbe` |
| `C_UnitAuras.GetAuraSlots` | returned 1 value: `nil` | error: `GetAuraSlots(): Auras cannot be accessed when secret while tainted by 'ApiProbe'
Lua Taint: ApiProbe` |
| `C_UnitAuras.GetBuffDataByIndex` | returned 1 value: `table{applications=number,auraInstanceID=number,canActivePlayerDispel=boolean,canApplyAura=boolean,dispelName=string,duration=number,expirationTime=number,hideOnPartyFrames=boolean,icon=number,isBossAura=boolean,isDPSRoleAura=boolean,isFromPlayerOrPlayerPet=boolean,isHarmful=boolean,isHealerRoleAura=boolean,isHelpful=boolean,isNameplateOnly=boolean,isRaid=boolean,isStealable=boolean,isTankRoleAura=boolean,name=string,nameplateShowAll=boolean,nameplateShowPersonal=boolean,points=table,sourceUnit=string,spellId=number,timeMod=number}` | error: `GetBuffDataByIndex(): Auras cannot be accessed when secret while tainted by 'ApiProbe'
Lua Taint: ApiProbe` |
| `C_UnitAuras.GetDebuffDataByIndex` | returned 1 value: `nil` | error: `GetDebuffDataByIndex(): Auras cannot be accessed when secret while tainted by 'ApiProbe'
Lua Taint: ApiProbe` |
| `C_UnitAuras.GetPlayerAuraBySpellID` | returned 1 value: `nil` | returned 0 values |
| `C_UnitAuras.GetUnitAuraBySpellID` | returned 1 value: `nil` | returned 0 values |
| `C_UnitAuras.GetUnitAuraInstanceIDs` | returned 1 value: `table{[number]=number,[number]=number}` | error: `GetUnitAuraInstanceIDs(): Auras cannot be accessed when secret while tainted by 'ApiProbe'
Lua Taint: ApiProbe` |
| `C_UnitAuras.GetUnitAuras` | returned 1 value: `table{[number]=table,[number]=table}` | error: `GetUnitAuras(): Auras cannot be accessed when secret while tainted by 'ApiProbe'
Lua Taint: ApiProbe` |
| `GetArmorPenetration` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetAvoidance` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetBlockChance` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetCombatRating` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetCombatRatingBonus` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetCritChance` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetCurrentEnvironment` | returned 1 value: `table{AddonListClearButton=table,BINDING_NAME_NAMEPLATES=string,BN_UNABLE_TO_RESOLVE_NAME=string,BOOST2_WARRIOR_COLOSSUSSMASH=string,CHAT_HEADER_SUFFIX=string,COVENANT_MISSIONS_HEALTH=string,CanPortGraveyard=function,DH_HAVOC_CORE_ABILITY_2=string,DUNGEON_FLOOR_UPPERBLACKROCKSPIRE3=string,ERROR_CLUB_TICKET_COUNT_AT_MAX_COMMUNITY=string,ERR_OUT_OF_CHI=string,ERR_TRADE_EQUIPPED_BAG=string,FCFDockOverflowButton_OnClick=function,GetTrainerServiceTypeFilter=function,HOUSING_BLUEPRINT_CONTENT_LIST_CLOSE_BUTTON=string,HUD_EDIT_MODE_SETTING_ACTION_BAR_HIDE_BAR_ART=string,LE_GAME_ERR_CHAT_RAID_RESTRICTED_TRIAL=number,LE_GAME_ERR_INVALID_FOLLOW_PVP_COMBAT=number,LE_GAME_ERR_PET_SPELL_TARGETS_DEAD=number,LE_GAME_ERR_RECRUIT_A_FRIEND_FAILED=number,LFGBrowseGroupDataDisplayRoleCount_Update=function,MAIL_LETTER_TOOLTIP=string,MultiBar6Button4Flash=table,MultiBarLeftButton7=table,MultiCastActionButton2Cooldown=table,MultiCastActionButton6Cooldown=table,OPTION_TOOLTIP_ACTION_BUTTON_USE_KEY_DOWN=string,OPTION_TOOLTIP_SHOW_MULTIBAR4=string,PROFESSIONS_COLUMN_REAGENTS_NONE=string,PVPHelperFrame_OnEvent=function,PVPReadyDialogBottomArt=table,PVP_RANK_6_1=string,RecruitAFriendFrame=table,SPELL_FAILED_CUSTOM_ERROR_71=string,SettingsSliderOptionsMixin=table,TutorialFrameLeft19=table,TutorialFrameRight19=table,UNIT_NAMES_COMBATLOG_TOOLTIP=string,UnitFrameManaBar_UnregisterDefaultEvents=function,UpdateOnBarHighlightMarksBySpell=function,...(49515)}` | returned 1 value: `table{AddonListClearButton=table,BINDING_NAME_NAMEPLATES=string,BN_UNABLE_TO_RESOLVE_NAME=string,BOOST2_WARRIOR_COLOSSUSSMASH=string,CHAT_HEADER_SUFFIX=string,COVENANT_MISSIONS_HEALTH=string,CanPortGraveyard=function,DH_HAVOC_CORE_ABILITY_2=string,DUNGEON_FLOOR_UPPERBLACKROCKSPIRE3=string,ERROR_CLUB_TICKET_COUNT_AT_MAX_COMMUNITY=string,ERR_OUT_OF_CHI=string,ERR_TRADE_EQUIPPED_BAG=string,FCFDockOverflowButton_OnClick=function,GetTrainerServiceTypeFilter=function,HOUSING_BLUEPRINT_CONTENT_LIST_CLOSE_BUTTON=string,HUD_EDIT_MODE_SETTING_ACTION_BAR_HIDE_BAR_ART=string,LE_GAME_ERR_CHAT_RAID_RESTRICTED_TRIAL=number,LE_GAME_ERR_INVALID_FOLLOW_PVP_COMBAT=number,LE_GAME_ERR_PET_SPELL_TARGETS_DEAD=number,LE_GAME_ERR_RECRUIT_A_FRIEND_FAILED=number,LFGBrowseGroupDataDisplayRoleCount_Update=function,MAIL_LETTER_TOOLTIP=string,MultiBar6Button4Flash=table,MultiBarLeftButton7=table,MultiCastActionButton2Cooldown=table,MultiCastActionButton6Cooldown=table,OPTION_TOOLTIP_ACTION_BUTTON_USE_KEY_DOWN=string,OPTION_TOOLTIP_SHOW_MULTIBAR4=string,PROFESSIONS_COLUMN_REAGENTS_NONE=string,PVPHelperFrame_OnEvent=function,PVPReadyDialogBottomArt=table,PVP_RANK_6_1=string,RecruitAFriendFrame=table,SPELL_FAILED_CUSTOM_ERROR_71=string,SettingsSliderOptionsMixin=table,TutorialFrameLeft19=table,TutorialFrameRight19=table,UNIT_NAMES_COMBATLOG_TOOLTIP=string,UnitFrameManaBar_UnregisterDefaultEvents=function,UpdateOnBarHighlightMarksBySpell=function,...(49517)}` |
| `GetDodgeChance` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetDodgeChanceFromAttribute` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetExpertise` | returned 3 values: `number`, `number`, `number` | returned 3 values: `secret:number`, `secret:number`, `secret:number` |
| `GetExpertisePercent` | returned 3 values: `number`, `number`, `number` | returned 3 values: `secret:number`, `secret:number`, `secret:number` |
| `GetGlobalEnvironment` | returned 1 value: `table{AddonListClearButton=table,BINDING_NAME_NAMEPLATES=string,BN_UNABLE_TO_RESOLVE_NAME=string,BOOST2_WARRIOR_COLOSSUSSMASH=string,CHAT_HEADER_SUFFIX=string,COVENANT_MISSIONS_HEALTH=string,CanPortGraveyard=function,DH_HAVOC_CORE_ABILITY_2=string,DUNGEON_FLOOR_UPPERBLACKROCKSPIRE3=string,ERROR_CLUB_TICKET_COUNT_AT_MAX_COMMUNITY=string,ERR_OUT_OF_CHI=string,ERR_TRADE_EQUIPPED_BAG=string,FCFDockOverflowButton_OnClick=function,GetTrainerServiceTypeFilter=function,HOUSING_BLUEPRINT_CONTENT_LIST_CLOSE_BUTTON=string,HUD_EDIT_MODE_SETTING_ACTION_BAR_HIDE_BAR_ART=string,LE_GAME_ERR_CHAT_RAID_RESTRICTED_TRIAL=number,LE_GAME_ERR_INVALID_FOLLOW_PVP_COMBAT=number,LE_GAME_ERR_PET_SPELL_TARGETS_DEAD=number,LE_GAME_ERR_RECRUIT_A_FRIEND_FAILED=number,LFGBrowseGroupDataDisplayRoleCount_Update=function,MAIL_LETTER_TOOLTIP=string,MultiBar6Button4Flash=table,MultiBarLeftButton7=table,MultiCastActionButton2Cooldown=table,MultiCastActionButton6Cooldown=table,OPTION_TOOLTIP_ACTION_BUTTON_USE_KEY_DOWN=string,OPTION_TOOLTIP_SHOW_MULTIBAR4=string,PROFESSIONS_COLUMN_REAGENTS_NONE=string,PVPHelperFrame_OnEvent=function,PVPReadyDialogBottomArt=table,PVP_RANK_6_1=string,RecruitAFriendFrame=table,SPELL_FAILED_CUSTOM_ERROR_71=string,SettingsSliderOptionsMixin=table,TutorialFrameLeft19=table,TutorialFrameRight19=table,UNIT_NAMES_COMBATLOG_TOOLTIP=string,UnitFrameManaBar_UnregisterDefaultEvents=function,UpdateOnBarHighlightMarksBySpell=function,...(49515)}` | returned 1 value: `table{AddonListClearButton=table,BINDING_NAME_NAMEPLATES=string,BN_UNABLE_TO_RESOLVE_NAME=string,BOOST2_WARRIOR_COLOSSUSSMASH=string,CHAT_HEADER_SUFFIX=string,COVENANT_MISSIONS_HEALTH=string,CanPortGraveyard=function,DH_HAVOC_CORE_ABILITY_2=string,DUNGEON_FLOOR_UPPERBLACKROCKSPIRE3=string,ERROR_CLUB_TICKET_COUNT_AT_MAX_COMMUNITY=string,ERR_OUT_OF_CHI=string,ERR_TRADE_EQUIPPED_BAG=string,FCFDockOverflowButton_OnClick=function,GetTrainerServiceTypeFilter=function,HOUSING_BLUEPRINT_CONTENT_LIST_CLOSE_BUTTON=string,HUD_EDIT_MODE_SETTING_ACTION_BAR_HIDE_BAR_ART=string,LE_GAME_ERR_CHAT_RAID_RESTRICTED_TRIAL=number,LE_GAME_ERR_INVALID_FOLLOW_PVP_COMBAT=number,LE_GAME_ERR_PET_SPELL_TARGETS_DEAD=number,LE_GAME_ERR_RECRUIT_A_FRIEND_FAILED=number,LFGBrowseGroupDataDisplayRoleCount_Update=function,MAIL_LETTER_TOOLTIP=string,MultiBar6Button4Flash=table,MultiBarLeftButton7=table,MultiCastActionButton2Cooldown=table,MultiCastActionButton6Cooldown=table,OPTION_TOOLTIP_ACTION_BUTTON_USE_KEY_DOWN=string,OPTION_TOOLTIP_SHOW_MULTIBAR4=string,PROFESSIONS_COLUMN_REAGENTS_NONE=string,PVPHelperFrame_OnEvent=function,PVPReadyDialogBottomArt=table,PVP_RANK_6_1=string,RecruitAFriendFrame=table,SPELL_FAILED_CUSTOM_ERROR_71=string,SettingsSliderOptionsMixin=table,TutorialFrameLeft19=table,TutorialFrameRight19=table,UNIT_NAMES_COMBATLOG_TOOLTIP=string,UnitFrameManaBar_UnregisterDefaultEvents=function,UpdateOnBarHighlightMarksBySpell=function,...(49517)}` |
| `GetHaste` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetHitModifier` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetLatestThreeSenders` | returned 1 value: `nil` | returned 1 value: `string` |
| `GetLifesteal` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetManaRegen` | returned 2 values: `number`, `number` | returned 2 values: `secret:number`, `secret:number` |
| `GetMastery` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetMasteryEffect` | returned 2 values: `number`, `number` | returned 2 values: `secret:number`, `secret:number` |
| `GetMeleeHaste` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetModResilienceDamageReduction` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetOffhandHitModifier` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetOverrideAPBySpellPower` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetOverrideSpellPowerByAP` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetParryChance` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetParryChanceFromAttribute` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetPetCritChance` | returned 2 values: `number`, `number` | returned 2 values: `secret:number`, `secret:number` |
| `GetPetDodgeChance` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetPetHitChanceModifier` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetPetMeleeHaste` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetPetSpellBonusDamage` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetPetSpellHitChanceModifier` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetPowerRegen` | returned 2 values: `number`, `number` | returned 2 values: `secret:number`, `secret:number` |
| `GetPvpPowerDamage` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetPvpPowerHealing` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetRangedCritChance` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetRangedHaste` | returned 2 values: `number`, `number` | returned 2 values: `secret:number`, `secret:number` |
| `GetRangedHitModifier` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetShapeshiftFormID` | returned 1 value: `nil` | returned 1 value: `number` |
| `GetShieldBlock` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetSpeed` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetSpellBonusDamage` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetSpellBonusHealing` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetSpellCritChance` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetSpellHitModifier` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetSpellPenetration` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetSturdiness` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetTotemInfo` | returned 7 values: `boolean`, `string`, `number`, `number`, `nil`, `number`, `number` | returned 7 values: `secret:boolean`, `secret:string`, `secret:number`, `secret:number`, `nil`, `secret:number`, `secret:number` |
| `GetUnitSpeed` | returned 4 values: `number`, `number`, `number`, `number` | returned 4 values: `secret:number`, `secret:number`, `secret:number`, `secret:number` |
| `GetVersatilityBonus` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `UnitArmor` | returned 4 values: `number`, `number`, `number`, `number` | returned 4 values: `secret:number`, `secret:number`, `secret:number`, `secret:number` |
| `UnitAttackPower` | returned 3 values: `number`, `number`, `number` | returned 3 values: `secret:number`, `secret:number`, `secret:number` |
| `UnitAttackSpeed` | returned 3 values: `number`, `nil`, `number` | returned 3 values: `secret:number`, `nil`, `secret:number` |
| `UnitDamage` | returned 7 values: `number`, `number`, `number`, `number`, `number`, `number`, `number` | returned 7 values: `secret:number`, `secret:number`, `secret:number`, `secret:number`, `secret:number`, `secret:number`, `secret:number` |
| `UnitDefenseSkill` | returned 2 values: `number`, `number` | returned 2 values: `secret:number`, `secret:number` |
| `UnitIsCharmed` | returned 1 value: `boolean` | returned 1 value: `secret:boolean` |
| `UnitIsPossessed` | returned 1 value: `boolean` | returned 1 value: `secret:boolean` |
| `UnitRangedAttackPower` | returned 3 values: `number`, `number`, `number` | returned 3 values: `secret:number`, `secret:number`, `secret:number` |
| `UnitRangedDamage` | returned 6 values: `number`, `number`, `number`, `number`, `number`, `number` | returned 6 values: `secret:number`, `secret:number`, `secret:number`, `secret:number`, `secret:number`, `secret:number` |
| `UnitSpellHaste` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `UnitStat` | returned 4 values: `number`, `number`, `number`, `number` | returned 4 values: `secret:number`, `secret:number`, `secret:number`, `secret:number` |
| `UnitThreatSituation` | returned 1 value: `nil` | returned 1 value: `number` |
| `UnitWeaponAttackPower` | returned 3 values: `number`, `number`, `number` | returned 3 values: `secret:number`, `secret:number`, `secret:number` |

## Always secret

Getters whose every return was secret even out of combat.

- `UnitGetIncomingHeals`
- `UnitGetTotalAbsorbs`
- `UnitGetTotalHealAbsorbs`
- `UnitHealth`
- `UnitHealthMissing`
- `UnitHealthPercent`
- `UnitInRange`
- `UnitPartialPower`
- `UnitPercentHealthFromGUID`
- `UnitPower`
- `UnitPowerMissing`
- `UnitPowerPercent`
- `UnitThreatPercentageOfLead`

## Blocked actions

- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `event:COMBAT_LOG_EVENT`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `event:COMBAT_LOG_EVENT_UNFILTERED`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `event:UNIT_PING_PIN_ADDED`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `event:UNIT_PING_PIN_REMOVED`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `None`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `C_Discord.GetDiscordUserID`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `C_Discord.GetDisplayNameType`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `C_Discord.GetGuildLinkStatus`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `C_Discord.GetNumDiscordServers`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `C_Discord.IsGuildChannelLinked`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `C_Discord.IsUserOAuthed`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `C_HousingDecor.GetAllPlacedDecor`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `C_Navigation.GetNearestPartyMemberToken`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `C_SocialRestrictions.IsAgeVerificationRestrictedMinor`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `C_Spell.CancelAutoRepeatSpell`
- ADDON_ACTION_BLOCKED: `UNKNOWN()` during `CancelLogout`
- ADDON_ACTION_BLOCKED: `UNKNOWN()` during `CancelTradeAccept`
- ADDON_ACTION_BLOCKED: `UNKNOWN()` during `C_GuildInfo.GetInfoText` (combat)
- ADDON_ACTION_BLOCKED: `UNKNOWN()` during `C_GuildInfo.GetMOTD` (combat)
- ADDON_ACTION_BLOCKED: `UNKNOWN()` during `GetGuildInfoText` (combat)
- ADDON_ACTION_BLOCKED: `UNKNOWN()` during `GetGuildRosterMOTD` (combat)
- ADDON_ACTION_BLOCKED: `UNKNOWN()` during `UnitSetRole` (combat)
- ADDON_ACTION_BLOCKED: `UNKNOWN()` during `UnitSetRoleEnum` (combat)
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `C_Discord.GetDiscordChannelName`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `C_Discord.GetNumDiscordChannels`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `C_Discord.GetServerLinkableChannels`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `C_Discord.GetServerName`
- ADDON_ACTION_FORBIDDEN: `UNKNOWN()` during `C_Discord.IsGuildSettingSet`

## Documented restriction flags

How many documented functions carry each flag (Blizzard's docs, not checked in game).

- `SecretArguments`: 3194
- `HasRestrictions`: 268
- `RequiresClubsInitialized`: 84
- `SecretWhenUnitStatsRestricted`: 63
- `RequiresActiveCommentator`: 53
- `SecretInChatMessagingLockdown`: 38
- `RequiresFriendList`: 32
- `SecretWhenUnitIdentityRestricted`: 32
- `RequiresValidActionSlot`: 25
- `RequiresUnitAuraAccess`: 24
- `SecretWhenUnitAuraRestricted`: 23
- `SecretReturns`: 19
- `SecretWhenCooldownsRestricted`: 15
- `RequiresValidTimelineEvent`: 12
- `RequiresRecentAllies`: 12
- `RequiresCommentator`: 10
- `RequiresValidUnitAuraInstance`: 8
- `SecretWhenUnitPowerRestricted`: 6
- `RequiresValidAndPublicCVar`: 5
- `RequiresLimitedInput`: 5
- `SecretWhenUnitSpellCastRestricted`: 5
- `RequiresNonReadOnlyCVar`: 4
- `RequiresNonSecureCVar`: 4
- `SecretWhenInCombat`: 4
- `RequiresValidInviteTarget`: 4
- `SecretWhenLuaTableHasSecretKeys`: 3
- `RequiresSpellDiminishUI`: 3
- `SecretWhenCurveSecret`: 3
- `RequiresNonSecretAura`: 3
- `SecretWhenEncounterEvent`: 2
- `SecretWhenLossOfControlRestricted`: 2
- `SecretInActivePvPMatch`: 2
- `SecretWhenTotemSlotSecret`: 2
- `SecretWhenUnitThreatValuesRestricted`: 2
- `SecretWhenUnitPossessionRestricted`: 2
- `SecretWhenUnitThreatStateRestricted`: 2
- `RequiresIndexInRange`: 1
- `RequiresDeclassifiedUnitIdentity`: 1
- `RequiresRestrictedAbbreviationBreakpoints`: 1
- `SecretWhenLossOfControlInfoRestricted`: 1
- `IsProtectedFunction`: 1
- `RequiresUnitIdentityAccess`: 1
- `SecretWhenUnitHealthMaxRestricted`: 1
- `RequiresComparableUnitTokens`: 1
- `SecretWhenUnitComparisonRestricted`: 1
- `SecretWhenUnitNameIdentityRestricted`: 1
- `SecretWhenUnitPowerMaxRestricted`: 1
