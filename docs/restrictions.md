# Restrictions seen in game

- Out of combat run: done; restrictions active at start: none
- In combat run: not run; restrictions active at start: unknown

## Getters that answered differently in combat

| Function | Out of combat | In combat |
|---|---|---|

## Always secret

Getters whose every return was secret even out of combat.

- `UnitGetIncomingHeals`
- `UnitGetTotalAbsorbs`
- `UnitGetTotalHealAbsorbs`
- `UnitHealth`
- `UnitHealthMissing`
- `UnitHealthPercent`
- `UnitInRange`
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
