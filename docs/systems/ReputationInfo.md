# ReputationInfo

Namespace: `C_Reputation`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Reputation.AreLegacyReputationsShown](#c_reputationarelegacyreputationsshown) | 1 value | 1 value |
| ✅ | [C_Reputation.CollapseAllFactionHeaders](#c_reputationcollapseallfactionheaders) |  |  |
| ✅ | [C_Reputation.CollapseFactionHeader](#c_reputationcollapsefactionheader) |  |  |
| ✅ | [C_Reputation.ExpandAllFactionHeaders](#c_reputationexpandallfactionheaders) |  |  |
| ✅ | [C_Reputation.ExpandFactionHeader](#c_reputationexpandfactionheader) |  |  |
| ✅ | [C_Reputation.GetFactionDataByID](#c_reputationgetfactiondatabyid) | 1 value | 1 value |
| ✅ | [C_Reputation.GetFactionDataByIndex](#c_reputationgetfactiondatabyindex) | 1 value | 1 value |
| ✅ | [C_Reputation.GetFactionParagonInfo](#c_reputationgetfactionparagoninfo) | 0 values | 0 values |
| ✅ | [C_Reputation.GetGuildFactionData](#c_reputationgetguildfactiondata) | 1 value | 1 value |
| ✅ | [C_Reputation.GetGuildRepExpirationTime](#c_reputationgetguildrepexpirationtime) | 1 value | 1 value |
| ✅ | [C_Reputation.GetNumFactions](#c_reputationgetnumfactions) | 1 value | 1 value |
| ✅ | [C_Reputation.GetReputationSortType](#c_reputationgetreputationsorttype) | 1 value | 1 value |
| ✅ | [C_Reputation.GetSelectedFaction](#c_reputationgetselectedfaction) | 1 value | 1 value |
| ✅ | [C_Reputation.GetWatchedFactionData](#c_reputationgetwatchedfactiondata) | 1 value | 1 value |
| ✅ | [C_Reputation.IsAccountWideReputation](#c_reputationisaccountwidereputation) | 1 value | 1 value |
| ✅ | [C_Reputation.IsFactionActive](#c_reputationisfactionactive) | 1 value | 1 value |
| ✅ | [C_Reputation.IsFactionParagon](#c_reputationisfactionparagon) | 1 value | 1 value |
| ✅ | [C_Reputation.IsFactionParagonForCurrentPlayer](#c_reputationisfactionparagonforcurrentplayer) | 1 value | 1 value |
| ✅ | [C_Reputation.IsMajorFaction](#c_reputationismajorfaction) | 1 value | 1 value |
| ✅ | [C_Reputation.RequestFactionParagonPreloadRewardData](#c_reputationrequestfactionparagonpreloadrewarddata) |  |  |
| ✅ | [C_Reputation.SetFactionActive](#c_reputationsetfactionactive) |  |  |
| ✅ | [C_Reputation.SetLegacyReputationsShown](#c_reputationsetlegacyreputationsshown) |  |  |
| ✅ | [C_Reputation.SetReputationSortType](#c_reputationsetreputationsorttype) |  |  |
| ✅ | [C_Reputation.SetSelectedFaction](#c_reputationsetselectedfaction) |  |  |
| ✅ | [C_Reputation.SetWatchedFactionByID](#c_reputationsetwatchedfactionbyid) |  |  |
| ✅ | [C_Reputation.SetWatchedFactionByIndex](#c_reputationsetwatchedfactionbyindex) |  |  |
| ✅ | [C_Reputation.ToggleFactionAtWar](#c_reputationtogglefactionatwar) |  |  |

### C_Reputation.AreLegacyReputationsShown

`C_Reputation.AreLegacyReputationsShown() → areLegacyReputationsShown: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.CollapseAllFactionHeaders

`C_Reputation.CollapseAllFactionHeaders()`

- Status: ✅ verified (function)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.CollapseFactionHeader

`C_Reputation.CollapseFactionHeader(factionSortIndex: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.ExpandAllFactionHeaders

`C_Reputation.ExpandAllFactionHeaders()`

- Status: ✅ verified (function)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.ExpandFactionHeader

`C_Reputation.ExpandFactionHeader(factionSortIndex: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.GetFactionDataByID

`C_Reputation.GetFactionDataByID(factionID: number) → factionData: FactionData?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:72`: returned 1 value: `table{atWarWith=boolean,canSetInactive=boolean,canToggleAtWar=boolean,currentReactionThreshold=number,currentStanding=number,description=string,factionID=number,hasBonusRepGain=boolean,isAccountWide=boolean,isChild=boolean,isCollapsed=boolean,isHeader=boolean,isHeaderWithRep=boolean,isWatched=boolean,name=string,nextReactionThreshold=number,reaction=number}`
- Called in combat: returned 1 value: `table{atWarWith=boolean,canSetInactive=boolean,canToggleAtWar=boolean,currentReactionThreshold=number,currentStanding=number,description=string,factionID=number,hasBonusRepGain=boolean,isAccountWide=boolean,isChild=boolean,isCollapsed=boolean,isHeader=boolean,isHeaderWithRep=boolean,isWatched=boolean,name=string,nextReactionThreshold=number,reaction=number}`
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.GetFactionDataByIndex

`C_Reputation.GetFactionDataByIndex(factionSortIndex: luaIndex) → factionData: FactionData?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `table{atWarWith=boolean,canSetInactive=boolean,canToggleAtWar=boolean,currentReactionThreshold=number,currentStanding=number,description=string,factionID=number,hasBonusRepGain=boolean,isAccountWide=boolean,isChild=boolean,isCollapsed=boolean,isHeader=boolean,isHeaderWithRep=boolean,isWatched=boolean,name=string,nextReactionThreshold=number,reaction=number}`
- Called in combat: returned 1 value: `table{atWarWith=boolean,canSetInactive=boolean,canToggleAtWar=boolean,currentReactionThreshold=number,currentStanding=number,description=string,factionID=number,hasBonusRepGain=boolean,isAccountWide=boolean,isChild=boolean,isCollapsed=boolean,isHeader=boolean,isHeaderWithRep=boolean,isWatched=boolean,name=string,nextReactionThreshold=number,reaction=number}`
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.GetFactionParagonInfo

`C_Reputation.GetFactionParagonInfo(factionID: number) → currentValue: number, threshold: number, rewardQuestID: number, hasRewardPending: bool, tooLowLevelForParagon: bool, paragonStorageLevel: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:72`: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.GetGuildFactionData

`C_Reputation.GetGuildFactionData() → guildFactionData: FactionData?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.GetGuildRepExpirationTime

`C_Reputation.GetGuildRepExpirationTime() → expirationTime: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.GetNumFactions

`C_Reputation.GetNumFactions() → numFactions: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.GetReputationSortType

`C_Reputation.GetReputationSortType() → sortType: ReputationSortType`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.GetSelectedFaction

`C_Reputation.GetSelectedFaction() → selectedFactionSortIndex: luaIndex`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.GetWatchedFactionData

`C_Reputation.GetWatchedFactionData() → watchedFactionData: FactionData?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.IsAccountWideReputation

`C_Reputation.IsAccountWideReputation(factionID: number) → isAccountWide: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:72`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.IsFactionActive

`C_Reputation.IsFactionActive(factionSortIndex: luaIndex) → isActive: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.IsFactionParagon

`C_Reputation.IsFactionParagon(factionID: number) → factionIsParagon: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:72`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.IsFactionParagonForCurrentPlayer

`C_Reputation.IsFactionParagonForCurrentPlayer(factionID: number) → currentPlayerHasParagon: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:72`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.IsMajorFaction

`C_Reputation.IsMajorFaction(factionID: number) → isMajorFaction: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:72`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.RequestFactionParagonPreloadRewardData

`C_Reputation.RequestFactionParagonPreloadRewardData(factionID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.SetFactionActive

`C_Reputation.SetFactionActive(factionSortIndex: luaIndex, setActive: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.SetLegacyReputationsShown

`C_Reputation.SetLegacyReputationsShown(showLegacyReputations: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.SetReputationSortType

`C_Reputation.SetReputationSortType(sortType: ReputationSortType)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.SetSelectedFaction

`C_Reputation.SetSelectedFaction(factionSortIndex: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.SetWatchedFactionByID

`C_Reputation.SetWatchedFactionByID(factionID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.SetWatchedFactionByIndex

`C_Reputation.SetWatchedFactionByIndex(factionSortIndex: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

### C_Reputation.ToggleFactionAtWar

`C_Reputation.ToggleFactionAtWar(factionSortIndex: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ReputationInfoDocumentation.lua`

## Events

### FACTION_STANDING_CHANGED

- Status: ✅ verified
- Payload: `factionID: number`, `updatedStanding: number`
- fires synchronously (Blizzard's docs)
- Seen firing 263 times (212 in combat); argument kinds: `n,n`

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

- Enumeration — ✅ verified
  - `None` = 0
  - `Account` = 1
  - `Character` = 2
