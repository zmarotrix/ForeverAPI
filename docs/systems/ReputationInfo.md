# ReputationInfo

Namespace: `C_Reputation`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_Reputation.AreLegacyReputationsShown](#c_reputationarelegacyreputationsshown) |  |  |
| ❔ | [C_Reputation.CollapseAllFactionHeaders](#c_reputationcollapseallfactionheaders) |  |  |
| ❔ | [C_Reputation.CollapseFactionHeader](#c_reputationcollapsefactionheader) |  |  |
| ❔ | [C_Reputation.ExpandAllFactionHeaders](#c_reputationexpandallfactionheaders) |  |  |
| ❔ | [C_Reputation.ExpandFactionHeader](#c_reputationexpandfactionheader) |  |  |
| ❔ | [C_Reputation.GetFactionDataByID](#c_reputationgetfactiondatabyid) |  |  |
| ❔ | [C_Reputation.GetFactionDataByIndex](#c_reputationgetfactiondatabyindex) |  |  |
| ❔ | [C_Reputation.GetFactionParagonInfo](#c_reputationgetfactionparagoninfo) |  |  |
| ❔ | [C_Reputation.GetGuildFactionData](#c_reputationgetguildfactiondata) |  |  |
| ❔ | [C_Reputation.GetGuildRepExpirationTime](#c_reputationgetguildrepexpirationtime) |  |  |
| ❔ | [C_Reputation.GetNumFactions](#c_reputationgetnumfactions) |  |  |
| ❔ | [C_Reputation.GetReputationSortType](#c_reputationgetreputationsorttype) |  |  |
| ❔ | [C_Reputation.GetSelectedFaction](#c_reputationgetselectedfaction) |  |  |
| ❔ | [C_Reputation.GetWatchedFactionData](#c_reputationgetwatchedfactiondata) |  |  |
| ❔ | [C_Reputation.IsAccountWideReputation](#c_reputationisaccountwidereputation) |  |  |
| ❔ | [C_Reputation.IsFactionActive](#c_reputationisfactionactive) |  |  |
| ❔ | [C_Reputation.IsFactionParagon](#c_reputationisfactionparagon) |  |  |
| ❔ | [C_Reputation.IsFactionParagonForCurrentPlayer](#c_reputationisfactionparagonforcurrentplayer) |  |  |
| ❔ | [C_Reputation.IsMajorFaction](#c_reputationismajorfaction) |  |  |
| ❔ | [C_Reputation.RequestFactionParagonPreloadRewardData](#c_reputationrequestfactionparagonpreloadrewarddata) |  |  |
| ❔ | [C_Reputation.SetFactionActive](#c_reputationsetfactionactive) |  |  |
| ❔ | [C_Reputation.SetLegacyReputationsShown](#c_reputationsetlegacyreputationsshown) |  |  |
| ❔ | [C_Reputation.SetReputationSortType](#c_reputationsetreputationsorttype) |  |  |
| ❔ | [C_Reputation.SetSelectedFaction](#c_reputationsetselectedfaction) |  |  |
| ❔ | [C_Reputation.SetWatchedFactionByID](#c_reputationsetwatchedfactionbyid) |  |  |
| ❔ | [C_Reputation.SetWatchedFactionByIndex](#c_reputationsetwatchedfactionbyindex) |  |  |
| ❔ | [C_Reputation.ToggleFactionAtWar](#c_reputationtogglefactionatwar) |  |  |

### C_Reputation.AreLegacyReputationsShown

`C_Reputation.AreLegacyReputationsShown() → areLegacyReputationsShown: bool`

- Status: ❔ unverified
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.CollapseAllFactionHeaders

`C_Reputation.CollapseAllFactionHeaders()`

- Status: ❔ unverified
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.CollapseFactionHeader

`C_Reputation.CollapseFactionHeader(factionSortIndex: luaIndex)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.ExpandAllFactionHeaders

`C_Reputation.ExpandAllFactionHeaders()`

- Status: ❔ unverified
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.ExpandFactionHeader

`C_Reputation.ExpandFactionHeader(factionSortIndex: luaIndex)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.GetFactionDataByID

`C_Reputation.GetFactionDataByID(factionID: number) → factionData: FactionData?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.GetFactionDataByIndex

`C_Reputation.GetFactionDataByIndex(factionSortIndex: luaIndex) → factionData: FactionData?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.GetFactionParagonInfo

`C_Reputation.GetFactionParagonInfo(factionID: number) → currentValue: number, threshold: number, rewardQuestID: number, hasRewardPending: bool, tooLowLevelForParagon: bool, paragonStorageLevel: number`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.GetGuildFactionData

`C_Reputation.GetGuildFactionData() → guildFactionData: FactionData?`

- Status: ❔ unverified
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.GetGuildRepExpirationTime

`C_Reputation.GetGuildRepExpirationTime() → expirationTime: number?`

- Status: ❔ unverified
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.GetNumFactions

`C_Reputation.GetNumFactions() → numFactions: number`

- Status: ❔ unverified
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.GetReputationSortType

`C_Reputation.GetReputationSortType() → sortType: ReputationSortType`

- Status: ❔ unverified
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.GetSelectedFaction

`C_Reputation.GetSelectedFaction() → selectedFactionSortIndex: luaIndex`

- Status: ❔ unverified
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.GetWatchedFactionData

`C_Reputation.GetWatchedFactionData() → watchedFactionData: FactionData?`

- Status: ❔ unverified
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.IsAccountWideReputation

`C_Reputation.IsAccountWideReputation(factionID: number) → isAccountWide: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.IsFactionActive

`C_Reputation.IsFactionActive(factionSortIndex: luaIndex) → isActive: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.IsFactionParagon

`C_Reputation.IsFactionParagon(factionID: number) → factionIsParagon: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.IsFactionParagonForCurrentPlayer

`C_Reputation.IsFactionParagonForCurrentPlayer(factionID: number) → currentPlayerHasParagon: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.IsMajorFaction

`C_Reputation.IsMajorFaction(factionID: number) → isMajorFaction: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.RequestFactionParagonPreloadRewardData

`C_Reputation.RequestFactionParagonPreloadRewardData(factionID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.SetFactionActive

`C_Reputation.SetFactionActive(factionSortIndex: luaIndex, setActive: bool)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.SetLegacyReputationsShown

`C_Reputation.SetLegacyReputationsShown(showLegacyReputations: bool)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.SetReputationSortType

`C_Reputation.SetReputationSortType(sortType: ReputationSortType)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.SetSelectedFaction

`C_Reputation.SetSelectedFaction(factionSortIndex: luaIndex)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.SetWatchedFactionByID

`C_Reputation.SetWatchedFactionByID(factionID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.SetWatchedFactionByIndex

`C_Reputation.SetWatchedFactionByIndex(factionSortIndex: luaIndex)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.ToggleFactionAtWar

`C_Reputation.ToggleFactionAtWar(factionSortIndex: luaIndex)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

## Events

### FACTION_STANDING_CHANGED

- Status: ❔ unverified
- Payload: `factionID: number`, `updatedStanding: number`
- fires synchronously (Blizzard's docs)

## Types

### FactionData

- Structure
  - `factionID`: number
  - `name`: cstring
  - `description`: cstring
  - `reaction`: luaIndex
  - `currentReactionThreshold`: number
  - `nextReactionThreshold`: number
  - `currentStanding`: number
  - `atWarWith`: bool
  - `canToggleAtWar`: bool
  - `isChild`: bool
  - `isHeader`: bool
  - `isHeaderWithRep`: bool
  - `isCollapsed`: bool
  - `isWatched`: bool
  - `hasBonusRepGain`: bool
  - `canSetInactive`: bool
  - `isAccountWide`: bool

### ReputationSortType

- Enumeration — ❔ unverified
  - `None` = 0
  - `Account` = 1
  - `Character` = 2
