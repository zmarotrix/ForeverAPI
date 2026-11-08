# DelvesUI

Namespace: `C_DelvesUI`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_DelvesUI.GetActiveDelveTier](#c_delvesuigetactivedelvetier) |  |  |
| ✅ | [C_DelvesUI.GetCompanionInfoForActivePlayer](#c_delvesuigetcompanioninfoforactiveplayer) |  |  |
| ✅ | [C_DelvesUI.GetCreatureDisplayInfoForCompanion](#c_delvesuigetcreaturedisplayinfoforcompanion) |  |  |
| ✅ | [C_DelvesUI.GetCurioLink](#c_delvesuigetcuriolink) |  |  |
| ✅ | [C_DelvesUI.GetCurioNodeForCompanion](#c_delvesuigetcurionodeforcompanion) |  |  |
| ✅ | [C_DelvesUI.GetCurioRarityByTraitCondAccountElementID](#c_delvesuigetcurioraritybytraitcondaccountelementid) |  |  |
| ✅ | [C_DelvesUI.GetCurrentDelvesSeasonNumber](#c_delvesuigetcurrentdelvesseasonnumber) |  |  |
| ✅ | [C_DelvesUI.GetDelveEntranceBackgroundWidgetSetID](#c_delvesuigetdelveentrancebackgroundwidgetsetid) |  |  |
| ✅ | [C_DelvesUI.GetDelveEntranceDescriptionString](#c_delvesuigetdelveentrancedescriptionstring) |  |  |
| ✅ | [C_DelvesUI.GetDelveEntranceHeaderString](#c_delvesuigetdelveentranceheaderstring) |  |  |
| ✅ | [C_DelvesUI.GetDelveEntranceMapID](#c_delvesuigetdelveentrancemapid) |  |  |
| ✅ | [C_DelvesUI.GetDelveEntranceTiers](#c_delvesuigetdelveentrancetiers) |  |  |
| ✅ | [C_DelvesUI.GetDelveEntranceTitleString](#c_delvesuigetdelveentrancetitlestring) |  |  |
| ✅ | [C_DelvesUI.GetDelvesAffixSpellsForSeason](#c_delvesuigetdelvesaffixspellsforseason) |  |  |
| ✅ | [C_DelvesUI.GetDelvesFactionForSeason](#c_delvesuigetdelvesfactionforseason) |  |  |
| ✅ | [C_DelvesUI.GetDelvesMinRequiredLevel](#c_delvesuigetdelvesminrequiredlevel) |  |  |
| ✅ | [C_DelvesUI.GetFactionForCompanion](#c_delvesuigetfactionforcompanion) |  |  |
| ✅ | [C_DelvesUI.GetFlavorNodeForCompanion](#c_delvesuigetflavornodeforcompanion) |  |  |
| ✅ | [C_DelvesUI.GetFlavorNodeNameForCompanion](#c_delvesuigetflavornodenameforcompanion) |  |  |
| ✅ | [C_DelvesUI.GetLockedTextForCompanion](#c_delvesuigetlockedtextforcompanion) |  |  |
| ✅ | [C_DelvesUI.GetModelSceneForCompanion](#c_delvesuigetmodelsceneforcompanion) |  |  |
| ✅ | [C_DelvesUI.GetPlayerCompanionPDEID](#c_delvesuigetplayercompanionpdeid) |  |  |
| ✅ | [C_DelvesUI.GetRoleNodeForCompanion](#c_delvesuigetrolenodeforcompanion) |  |  |
| ✅ | [C_DelvesUI.GetRoleSubtreeForCompanion](#c_delvesuigetrolesubtreeforcompanion) |  |  |
| ✅ | [C_DelvesUI.GetTieredEntranceOptionalAffixTraitTreeID](#c_delvesuigettieredentranceoptionalaffixtraittreeid) |  |  |
| ✅ | [C_DelvesUI.GetTieredEntrancePDEID](#c_delvesuigettieredentrancepdeid) |  |  |
| ✅ | [C_DelvesUI.GetTieredEntranceType](#c_delvesuigettieredentrancetype) |  |  |
| ✅ | [C_DelvesUI.GetTraitTreeForCompanion](#c_delvesuigettraittreeforcompanion) |  |  |
| ✅ | [C_DelvesUI.GetUnseenCuriosBySlotType](#c_delvesuigetunseencuriosbyslottype) |  |  |
| ✅ | [C_DelvesUI.GetWorldTierDifficultyForActivePlayer](#c_delvesuigetworldtierdifficultyforactiveplayer) |  |  |
| ✅ | [C_DelvesUI.HasActiveDelve](#c_delvesuihasactivedelve) |  |  |
| ✅ | [C_DelvesUI.HasActiveLFGLair](#c_delvesuihasactivelfglair) |  |  |
| ✅ | [C_DelvesUI.HasActiveLair](#c_delvesuihasactivelair) |  |  |
| ✅ | [C_DelvesUI.IsDelveEntranceTierEnabled](#c_delvesuiisdelveentrancetierenabled) |  |  |
| ✅ | [C_DelvesUI.IsEligibleForActiveDelveRewards](#c_delvesuiiseligibleforactivedelverewards) |  |  |
| ✅ | [C_DelvesUI.IsInLair](#c_delvesuiisinlair) |  |  |
| ✅ | [C_DelvesUI.IsTraitTreeForCompanion](#c_delvesuiistraittreeforcompanion) |  |  |
| ✅ | [C_DelvesUI.RequestPartyEligibilityForDelveTiers](#c_delvesuirequestpartyeligibilityfordelvetiers) |  |  |
| ✅ | [C_DelvesUI.SaveSeenCuriosBySlotType](#c_delvesuisaveseencuriosbyslottype) |  |  |
| ✅ | [C_DelvesUI.SelectDelveEntranceTier](#c_delvesuiselectdelveentrancetier) |  |  |

### C_DelvesUI.GetActiveDelveTier

`C_DelvesUI.GetActiveDelveTier() → tierInfo: TieredEntranceTierInfo`

- Status: ✅ verified (function)
- Blizzard: Returns the entrance tier information for the active Delve (via party data). Assumes only Delves use this type for now.
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetCompanionInfoForActivePlayer

`C_DelvesUI.GetCompanionInfoForActivePlayer() → playerCompanionInfoID: number`

- Status: ✅ verified (function)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetCreatureDisplayInfoForCompanion

`C_DelvesUI.GetCreatureDisplayInfoForCompanion(companionID: number?) → creatureDisplayInfoID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetCurioLink

`C_DelvesUI.GetCurioLink(spellID: SpellIdentifier, rarity: CurioRarity) → curioLink: cstring`

- Status: ✅ verified (function)
- Blizzard: Given the spell ID for an owned curio and its rarity, return a spell link style hyperlink for the curio spell, since they aren't items when learned
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetCurioNodeForCompanion

`C_DelvesUI.GetCurioNodeForCompanion(curioType: CurioType, companionID: number?) → nodeID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetCurioRarityByTraitCondAccountElementID

`C_DelvesUI.GetCurioRarityByTraitCondAccountElementID(traitCondAccountElementID: number) → rarity: CurioRarity`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetCurrentDelvesSeasonNumber

`C_DelvesUI.GetCurrentDelvesSeasonNumber() → seasonNumber: number`

- Status: ✅ verified (function)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetDelveEntranceBackgroundWidgetSetID

`C_DelvesUI.GetDelveEntranceBackgroundWidgetSetID() → backgroundWidgetSetID: number`

- Status: ✅ verified (function)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetDelveEntranceDescriptionString

`C_DelvesUI.GetDelveEntranceDescriptionString() → description: string?`

- Status: ✅ verified (function)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetDelveEntranceHeaderString

`C_DelvesUI.GetDelveEntranceHeaderString() → header: string?`

- Status: ✅ verified (function)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetDelveEntranceMapID

`C_DelvesUI.GetDelveEntranceMapID() → mapID: number`

- Status: ✅ verified (function)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetDelveEntranceTiers

`C_DelvesUI.GetDelveEntranceTiers() → levelInfo: TieredEntranceTierInfo[]`

- Status: ✅ verified (function)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetDelveEntranceTitleString

`C_DelvesUI.GetDelveEntranceTitleString() → title: cstring?`

- Status: ✅ verified (function)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetDelvesAffixSpellsForSeason

`C_DelvesUI.GetDelvesAffixSpellsForSeason() → affixSpellIDs: number[]`

- Status: ✅ verified (function)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetDelvesFactionForSeason

`C_DelvesUI.GetDelvesFactionForSeason() → factionID: number`

- Status: ✅ verified (function)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetDelvesMinRequiredLevel

`C_DelvesUI.GetDelvesMinRequiredLevel() → minRequiredLevel: number?`

- Status: ✅ verified (function)
- Blizzard: Players must be at or above the min level + offset to enter Delves. This function returns that min level.
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetFactionForCompanion

`C_DelvesUI.GetFactionForCompanion(companionID: number?) → factionID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetFlavorNodeForCompanion

`C_DelvesUI.GetFlavorNodeForCompanion(companionID: number?) → nodeID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetFlavorNodeNameForCompanion

`C_DelvesUI.GetFlavorNodeNameForCompanion(companionID: number?) → name: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetLockedTextForCompanion

`C_DelvesUI.GetLockedTextForCompanion(companionID: number?) → text: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetModelSceneForCompanion

`C_DelvesUI.GetModelSceneForCompanion(companionID: number?) → modelSceneID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetPlayerCompanionPDEID

`C_DelvesUI.GetPlayerCompanionPDEID(companionID: number?) → pdeID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetRoleNodeForCompanion

`C_DelvesUI.GetRoleNodeForCompanion(companionID: number?) → nodeID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetRoleSubtreeForCompanion

`C_DelvesUI.GetRoleSubtreeForCompanion(roleType: CompanionRoleType, companionID: number?) → subTreeID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetTieredEntranceOptionalAffixTraitTreeID

`C_DelvesUI.GetTieredEntranceOptionalAffixTraitTreeID() → treeID: number?`

- Status: ✅ verified (function)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetTieredEntrancePDEID

`C_DelvesUI.GetTieredEntrancePDEID() → pdeID: number`

- Status: ✅ verified (function)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetTieredEntranceType

`C_DelvesUI.GetTieredEntranceType() → entranceType: TieredEntranceType`

- Status: ✅ verified (function)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetTraitTreeForCompanion

`C_DelvesUI.GetTraitTreeForCompanion(companionID: number?) → treeID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetUnseenCuriosBySlotType

`C_DelvesUI.GetUnseenCuriosBySlotType(slotType: CompanionConfigSlotTypes, ownedCurioNodeIDs: number[]) → unseenCurioNodeIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.GetWorldTierDifficultyForActivePlayer

`C_DelvesUI.GetWorldTierDifficultyForActivePlayer() → difficulty: WorldTierDifficulty`

- Status: ✅ verified (function)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.HasActiveDelve

`C_DelvesUI.HasActiveDelve() → result: bool`

- Status: ✅ verified (function)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.HasActiveLFGLair

`C_DelvesUI.HasActiveLFGLair() → result: bool`

- Status: ✅ verified (function)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.HasActiveLair

`C_DelvesUI.HasActiveLair() → result: bool`

- Status: ✅ verified (function)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.IsDelveEntranceTierEnabled

`C_DelvesUI.IsDelveEntranceTierEnabled(tier: number) → isEnabled: bool, failureReason: string?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.IsEligibleForActiveDelveRewards

`C_DelvesUI.IsEligibleForActiveDelveRewards(unit: UnitToken) → result: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.IsInLair

`C_DelvesUI.IsInLair() → result: bool`

- Status: ✅ verified (function)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.IsTraitTreeForCompanion

`C_DelvesUI.IsTraitTreeForCompanion(traitTreeID: number) → isForCompanion: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.RequestPartyEligibilityForDelveTiers

`C_DelvesUI.RequestPartyEligibilityForDelveTiers(mapID: number)`

- Status: ✅ verified (function)
- Blizzard: Queries private party members to see what level they have unlocked for the Delve. Ineligible members are added to the tooltip of dropdown entries.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.SaveSeenCuriosBySlotType

`C_DelvesUI.SaveSeenCuriosBySlotType(slotType: CompanionConfigSlotTypes, ownedCurioNodeIDs: number[])`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

### C_DelvesUI.SelectDelveEntranceTier

`C_DelvesUI.SelectDelveEntranceTier(tier: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DelvesUIDocumentation.lua`

## Events

### ACTIVE_DELVE_DATA_UPDATE

- Status: ✅ verified
- Payload: none
- Blizzard: Signaled when SpellScript calls change the data for players/parties owning a delve or when the delve is shut down.
- fires synchronously (Blizzard's docs)

### DELVES_ACCOUNT_DATA_ELEMENT_CHANGED

- Status: ✅ verified
- Payload: none
- Blizzard: Signaled when player account data element(s) have changed. This drives curio ranks, and the UI should update when this is sent.
- fires synchronously (Blizzard's docs)

### DELVE_ASSIST_ACTION

- Status: ✅ verified
- Payload: `data: DelveAssistActionData`
- Blizzard: Signaled when an assist action occurs in a delve.
- fires synchronously (Blizzard's docs)

### PARTY_ELIGIBILITY_FOR_DELVE_TIERS_CHANGED

- Status: ✅ verified
- Payload: `playerName: string`, `maxEligibleLevel: number`
- Blizzard: Signaled when responses come in from RequestPartyEligibilityForDelveTiers.
- fires synchronously (Blizzard's docs)

### SHOW_DELVES_COMPANION_CONFIGURATION_UI

- Status: ✅ verified
- Payload: none
- Blizzard: Signaled when SpellScript indicates that a curio has been learned or upgraded. Will show the companion config UI.
- fires synchronously (Blizzard's docs)

### WALK_IN_DATA_UPDATE

- Status: ✅ verified
- Payload: none
- Blizzard: Signaled when the player or a private party member join a new walk-in instance or when the instance is shut down.
- fires synchronously (Blizzard's docs)

## Types

### CompanionRoleType

- Enumeration — ✅ verified
  - `Dps` = 0
  - `Heal` = 1
  - `Tank` = 2

### CurioType

- Enumeration — ✅ verified
  - `Combat` = 0
  - `Utility` = 1

### TieredEntranceRewardInfo

- Structure
  - `id`: number
  - `quantity`: number
  - `rewardType`: TieredEntranceRewardType
  - `context`: ItemCreationContext

### TieredEntranceRewardType

- Enumeration — ✅ verified
  - `Item` = 0
  - `Currency` = 1

### TieredEntranceTierInfo

- Structure
  - `tier`: number
  - `suggestedILvl`: number
  - `overrideTooltipSpellID`: number
  - `unlocked`: bool
  - `tierDescription`: string
  - `rewards`: TieredEntranceRewardInfo[]
  - `modifierUIWidgetSetID`: number
  - `lockedReason`: string?
  - `queueAsLFG`: bool
  - `difficultyID`: number
