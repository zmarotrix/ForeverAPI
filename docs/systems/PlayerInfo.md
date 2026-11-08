# PlayerInfo

Namespace: `C_PlayerInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_PlayerInfo.CanPlayerEnterChromieTime](#c_playerinfocanplayerenterchromietime) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.CanPlayerUseAreaLoot](#c_playerinfocanplayerusearealoot) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.CanPlayerUseMountEquipment](#c_playerinfocanplayerusemountequipment) | 2 values | 2 values |
| ✅ | [C_PlayerInfo.CanUseItem](#c_playerinfocanuseitem) |  |  |
| ✅ | [C_PlayerInfo.GetAlternateFormInfo](#c_playerinfogetalternateforminfo) | 2 values | 2 values |
| ✅ | [C_PlayerInfo.GetContentDifficultyCreatureForPlayer](#c_playerinfogetcontentdifficultycreatureforplayer) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.GetContentDifficultyQuestForPlayer](#c_playerinfogetcontentdifficultyquestforplayer) |  |  |
| ✅ | [C_PlayerInfo.GetDisplayID](#c_playerinfogetdisplayid) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.GetGlidingInfo](#c_playerinfogetglidinginfo) | 3 values | 3 values |
| ✅ | [C_PlayerInfo.GetInstancesUnlockedAtLevel](#c_playerinfogetinstancesunlockedatlevel) |  |  |
| ✅ | [C_PlayerInfo.GetNativeDisplayID](#c_playerinfogetnativedisplayid) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.GetPetStableCreatureDisplayInfoID](#c_playerinfogetpetstablecreaturedisplayinfoid) |  |  |
| ✅ | [C_PlayerInfo.GetPlayerCharacterData](#c_playerinfogetplayercharacterdata) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.GetPlayerMythicPlusRatingSummary](#c_playerinfogetplayermythicplusratingsummary) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.HasAccountInventoryLock](#c_playerinfohasaccountinventorylock) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.HasVisibleInvSlot](#c_playerinfohasvisibleinvslot) |  |  |
| ✅ | [C_PlayerInfo.IsAccountBankEnabled](#c_playerinfoisaccountbankenabled) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.IsCharacterBankEnabled](#c_playerinfoischaracterbankenabled) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.IsDisplayRaceNative](#c_playerinfoisdisplayracenative) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.IsExpansionLandingPageUnlockedForPlayer](#c_playerinfoisexpansionlandingpageunlockedforplayer) |  |  |
| ✅ | [C_PlayerInfo.IsMirrorImage](#c_playerinfoismirrorimage) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.IsPlayerEligibleForNPE](#c_playerinfoisplayereligiblefornpe) | 2 values | 2 values |
| ✅ | [C_PlayerInfo.IsPlayerEligibleForNPEv2](#c_playerinfoisplayereligiblefornpev2) | 2 values | 2 values |
| ✅ | [C_PlayerInfo.IsPlayerInChromieTime](#c_playerinfoisplayerinchromietime) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.IsPlayerInRPE](#c_playerinfoisplayerinrpe) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.IsPlayerInTimerunningHeroicWorldTier](#c_playerinfoisplayerintimerunningheroicworldtier) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.IsPlayerNPERestricted](#c_playerinfoisplayernperestricted) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.IsReturningCharacter](#c_playerinfoisreturningcharacter) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.IsSelfFoundActive](#c_playerinfoisselffoundactive) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.IsTradingPostAvailable](#c_playerinfoistradingpostavailable) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.IsTravelersLogAvailable](#c_playerinfoistravelerslogavailable) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.IsTutorialsTabAvailable](#c_playerinfoistutorialstabavailable) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.ShouldDisplaySurname](#c_playerinfoshoulddisplaysurname) | 1 value | 1 value |

### C_PlayerInfo.CanPlayerEnterChromieTime

`C_PlayerInfo.CanPlayerEnterChromieTime() → canEnter: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.CanPlayerUseAreaLoot

`C_PlayerInfo.CanPlayerUseAreaLoot() → canUseAreaLoot: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.CanPlayerUseMountEquipment

`C_PlayerInfo.CanPlayerUseMountEquipment() → canUseMountEquipment: bool, failureReason: string`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `string`
- Called in combat: returned 2 values: `boolean`, `string`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.CanUseItem

`C_PlayerInfo.CanUseItem(itemID: number) → isUseable: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.GetAlternateFormInfo

`C_PlayerInfo.GetAlternateFormInfo() → hasAlternateForm: bool, inAlternateForm: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `boolean`
- Called in combat: returned 2 values: `boolean`, `boolean`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.GetContentDifficultyCreatureForPlayer

`C_PlayerInfo.GetContentDifficultyCreatureForPlayer(unitToken: UnitToken) → difficulty: RelativeContentDifficulty`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `player`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.GetContentDifficultyQuestForPlayer

`C_PlayerInfo.GetContentDifficultyQuestForPlayer(questID: number) → difficulty: RelativeContentDifficulty`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.GetDisplayID

`C_PlayerInfo.GetDisplayID() → displayID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.GetGlidingInfo

`C_PlayerInfo.GetGlidingInfo() → isGliding: bool, canGlide: bool, forwardSpeed: number`

- Status: ✅ verified (function)
- Called out of combat: returned 3 values: `boolean`, `boolean`, `number`
- Called in combat: returned 3 values: `boolean`, `boolean`, `number`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.GetInstancesUnlockedAtLevel

`C_PlayerInfo.GetInstancesUnlockedAtLevel(level: number, isRaid: bool) → dungeonID: number[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.GetNativeDisplayID

`C_PlayerInfo.GetNativeDisplayID() → nativeDisplayID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.GetPetStableCreatureDisplayInfoID

`C_PlayerInfo.GetPetStableCreatureDisplayInfoID(index: number) → creatureDisplayInfoID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.GetPlayerCharacterData

`C_PlayerInfo.GetPlayerCharacterData() → characterData: PlayerInfoCharacterData`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `table{createScreenIconAtlas=string,fileName=string,name=string,sex=number}`
- Called in combat: returned 1 value: `table{createScreenIconAtlas=string,fileName=string,name=string,sex=number}`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.GetPlayerMythicPlusRatingSummary

`C_PlayerInfo.GetPlayerMythicPlusRatingSummary(playerToken: UnitToken) → ratingSummary: MythicPlusRatingSummary`

- Status: ✅ verified (function)
- Blizzard: Returns the players mythic+ rating summary which includes the runs they've completed as well as their current season m+ rating
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `player`: returned 1 value: `table{currentSeasonScore=number,runs=table}`
- Called in combat: returned 1 value: `table{currentSeasonScore=number,runs=table}`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.HasAccountInventoryLock

`C_PlayerInfo.HasAccountInventoryLock() → hasAccountInventoryLock: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.HasVisibleInvSlot

`C_PlayerInfo.HasVisibleInvSlot(slot: luaIndex) → isVisible: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.IsAccountBankEnabled

`C_PlayerInfo.IsAccountBankEnabled() → isAccountBankEnabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.IsCharacterBankEnabled

`C_PlayerInfo.IsCharacterBankEnabled() → isCharacterBankEnabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.IsDisplayRaceNative

`C_PlayerInfo.IsDisplayRaceNative() → isDisplayRaceNative: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.IsExpansionLandingPageUnlockedForPlayer

`C_PlayerInfo.IsExpansionLandingPageUnlockedForPlayer(expansionID: number) → isUnlocked: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.IsMirrorImage

`C_PlayerInfo.IsMirrorImage() → isMirrorImage: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.IsPlayerEligibleForNPE

`C_PlayerInfo.IsPlayerEligibleForNPE() → isEligible: bool, failureReason: string`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `string`
- Called in combat: returned 2 values: `boolean`, `string`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.IsPlayerEligibleForNPEv2

`C_PlayerInfo.IsPlayerEligibleForNPEv2() → isEligible: bool, failureReason: string`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `string`
- Called in combat: returned 2 values: `boolean`, `string`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.IsPlayerInChromieTime

`C_PlayerInfo.IsPlayerInChromieTime() → inChromieTime: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.IsPlayerInRPE

`C_PlayerInfo.IsPlayerInRPE() → isInRPE: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.IsPlayerInTimerunningHeroicWorldTier

`C_PlayerInfo.IsPlayerInTimerunningHeroicWorldTier() → inTimerunningHeroicWorldTier: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.IsPlayerNPERestricted

`C_PlayerInfo.IsPlayerNPERestricted() → isRestricted: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.IsReturningCharacter

`C_PlayerInfo.IsReturningCharacter() → isReturning: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.IsSelfFoundActive

`C_PlayerInfo.IsSelfFoundActive() → active: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.IsTradingPostAvailable

`C_PlayerInfo.IsTradingPostAvailable() → isAvailable: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.IsTravelersLogAvailable

`C_PlayerInfo.IsTravelersLogAvailable() → isAvailable: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.IsTutorialsTabAvailable

`C_PlayerInfo.IsTutorialsTabAvailable() → isAvailable: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerInfoDocumentation.lua`

### C_PlayerInfo.ShouldDisplaySurname

`C_PlayerInfo.ShouldDisplaySurname() → display: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `PlayerInfoDocumentation.lua`

## Types

### MythicPlusRatingMapSummary

- Structure
- Blizzard: Specific information about a completed mythic plus run.
  - `challengeModeID`: number
  - `mapScore`: number
  - `bestRunLevel`: number
  - `bestRunDurationMS`: number
  - `finishedSuccess`: bool

### MythicPlusRatingSummary

- Structure
- Blizzard: The current season rating and well as a list of completed mythic plus runs.
  - `currentSeasonScore`: number
  - `runs`: MythicPlusRatingMapSummary[]
