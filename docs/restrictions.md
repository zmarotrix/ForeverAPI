# Restrictions seen in game

- Out of combat run: done; restrictions active at start: none
- In combat run: done; restrictions active at start: none

## Getters that answered differently in combat

| Function | Out of combat | In combat |
|---|---|---|
| `C_ClassTalents.CanChangeTalents` | returned 3 values: `boolean`, `boolean`, `nil` | returned 3 values: `boolean`, `boolean`, `string` |
| `C_DamageMeter.GetAvailableCombatSessions` | returned 1 value: `table{[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table}` | returned 1 value: `table{[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table}` |
| `C_GamepadUI.GetFirstGamepadActionBarStorageSlotIndexForActiveStance` | returned 1 value: `nil` | returned 1 value: `number` |
| `C_NamePlate.GetNamePlates` | returned 1 value: `table{}` | returned 1 value: `table{[number]=table}` |
| `C_UnitAuras.GetAuraSlots` | returned 1 value: `nil` | error: `GetAuraSlots(): Auras cannot be accessed when secret while tainted by 'ApiProbe'
Lua Taint: ApiProbe` |
| `GetArmorPenetration` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetAvoidance` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetBlockChance` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetCritChance` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetDodgeChance` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetDodgeChanceFromAttribute` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetExpertise` | returned 3 values: `number`, `number`, `number` | returned 3 values: `secret:number`, `secret:number`, `secret:number` |
| `GetExpertisePercent` | returned 3 values: `number`, `number`, `number` | returned 3 values: `secret:number`, `secret:number`, `secret:number` |
| `GetHaste` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetHitModifier` | returned 1 value: `number` | returned 1 value: `secret:number` |
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
| `GetSpellBonusHealing` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetSpellCritChance` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetSpellHitModifier` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetSpellPenetration` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetSturdiness` | returned 1 value: `number` | returned 1 value: `secret:number` |
| `GetUnitSpeed` | returned 4 values: `number`, `number`, `number`, `number` | returned 4 values: `secret:number`, `secret:number`, `secret:number`, `secret:number` |
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
- `UnitSpellTargetClass`
- `UnitSpellTargetName`

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
