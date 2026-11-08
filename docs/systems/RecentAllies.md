# RecentAllies

Namespace: `C_RecentAllies`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_RecentAllies.CanSetRecentAllyNote](#c_recentalliescansetrecentallynote) | 1 value | 1 value |
| ✅ | [C_RecentAllies.GetRecentAllies](#c_recentalliesgetrecentallies) | 1 value | 1 value |
| ✅ | [C_RecentAllies.GetRecentAllyByFullName](#c_recentalliesgetrecentallybyfullname) |  |  |
| ✅ | [C_RecentAllies.GetRecentAllyByGUID](#c_recentalliesgetrecentallybyguid) | 1 value | 1 value |
| ✅ | [C_RecentAllies.IsInteractionCategoryFilterSupportedForCurrentGameType](#c_recentalliesisinteractioncategoryfiltersupportedforcurrentgametype) | 1 value | 1 value |
| ✅ | [C_RecentAllies.IsRecentAllyByFullName](#c_recentalliesisrecentallybyfullname) |  |  |
| ✅ | [C_RecentAllies.IsRecentAllyByGUID](#c_recentalliesisrecentallybyguid) | 1 value | 1 value |
| ✅ | [C_RecentAllies.IsRecentAllyDataReady](#c_recentalliesisrecentallydataready) | 1 value | 1 value |
| ✅ | [C_RecentAllies.IsRecentAllyPinned](#c_recentalliesisrecentallypinned) | 1 value | 1 value |
| ✅ | [C_RecentAllies.IsSystemEnabled](#c_recentalliesissystemenabled) | 1 value | 1 value |
| ✅ | [C_RecentAllies.IsSystemSupported](#c_recentalliesissystemsupported) | 1 value | 1 value |
| ✅ | [C_RecentAllies.SearchRecentAllies](#c_recentalliessearchrecentallies) |  |  |
| ✅ | [C_RecentAllies.SetRecentAllyNote](#c_recentalliessetrecentallynote) |  |  |
| ✅ | [C_RecentAllies.SetRecentAllyPinned](#c_recentalliessetrecentallypinned) |  |  |
| ✅ | [C_RecentAllies.TryRequestRecentAlliesData](#c_recentalliestryrequestrecentalliesdata) |  |  |

### C_RecentAllies.CanSetRecentAllyNote

`C_RecentAllies.CanSetRecentAllyNote(characterGUID: WOWGUID) → canSetNote: bool`

- Status: ✅ verified (function)
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `guid`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.GetRecentAllies

`C_RecentAllies.GetRecentAllies() → recentAlliesData: RecentAllyData[]`

- Status: ✅ verified (function)
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `table{[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,...(44)}`
- Called in combat: returned 1 value: `table{[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,...(44)}`
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.GetRecentAllyByFullName

`C_RecentAllies.GetRecentAllyByFullName(fullCharacterName: cstring) → recentAllyData: RecentAllyData?`

- Status: ✅ verified (function)
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.GetRecentAllyByGUID

`C_RecentAllies.GetRecentAllyByGUID(characterGUID: WOWGUID) → recentAllyData: RecentAllyData?`

- Status: ✅ verified (function)
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `guid`: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.IsInteractionCategoryFilterSupportedForCurrentGameType

`C_RecentAllies.IsInteractionCategoryFilterSupportedForCurrentGameType(interactionCategoryFilter: RecentAlliesInteractionCategoryFilter) → isInteractionCategoryFilterSupportedForCurrentGameType: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.IsRecentAllyByFullName

`C_RecentAllies.IsRecentAllyByFullName(fullCharacterName: cstring) → isRecentAlly: bool`

- Status: ✅ verified (function)
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.IsRecentAllyByGUID

`C_RecentAllies.IsRecentAllyByGUID(characterGUID: WOWGUID) → isRecentAlly: bool`

- Status: ✅ verified (function)
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `guid`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.IsRecentAllyDataReady

`C_RecentAllies.IsRecentAllyDataReady() → isReady: bool`

- Status: ✅ verified (function)
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.IsRecentAllyPinned

`C_RecentAllies.IsRecentAllyPinned(characterGUID: WOWGUID) → isPinned: bool`

- Status: ✅ verified (function)
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `guid`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.IsSystemEnabled

`C_RecentAllies.IsSystemEnabled() → isRecentAllySystemEnabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.IsSystemSupported

`C_RecentAllies.IsSystemSupported() → isRecentAllySystemSupported: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.SearchRecentAllies

`C_RecentAllies.SearchRecentAllies(searchInfo: RecentAlliesSearchInfo) → recentAlliesData: RecentAllyData[]`

- Status: ✅ verified (function)
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.SetRecentAllyNote

`C_RecentAllies.SetRecentAllyNote(characterGUID: WOWGUID, note: cstring)`

- Status: ✅ verified (function)
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.SetRecentAllyPinned

`C_RecentAllies.SetRecentAllyPinned(characterGUID: WOWGUID, isPinned: bool)`

- Status: ✅ verified (function)
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.TryRequestRecentAlliesData

`C_RecentAllies.TryRequestRecentAlliesData()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- Source: client docs `RecentAlliesDocumentation.lua`

## Events

### LET_RECENT_ALLIES_SEE_LOCATION_SETTING_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### RECENT_ALLIES_CACHE_UPDATE

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)
- Seen firing 7 times (0 in combat); argument kinds: ``

### RECENT_ALLIES_DATA_READY

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 3 times (0 in combat); argument kinds: ``

### RECENT_ALLIES_SYSTEM_STATUS_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### RECENT_ALLY_DATA_UPDATED

- Status: ✅ verified
- Payload: `characterGUID: WOWGUID`
- fires synchronously (Blizzard's docs)
- Seen firing 89 times (0 in combat); argument kinds: `s`

## Types

### RecentAlliesSearchInfo

- Structure
  - `searchText`: string
  - `isOnline`: bool
  - `isDND`: bool
  - `isAFK`: bool
  - `isOffline`: bool
  - `interactionCategoryFilters`: RecentAlliesInteractionCategoryFilter[]

### RecentAllyCharacterData

- Structure
  - `guid`: WOWGUID
  - `name`: string
  - `fullName`: string
  - `realmName`: string
  - `level`: number
  - `classID`: number
  - `raceID`: number
  - `sex`: UnitSex

### RecentAllyData

- Structure
  - `stateData`: RecentAllyStateData
  - `characterData`: RecentAllyCharacterData
  - `interactionData`: RecentAllyInteractionData

### RecentAllyInteraction

- Structure
  - `type`: RolodexType
  - `description`: cstring
  - `timestamp`: time_t
  - `contextData`: RecentAllyInteractionContextData

### RecentAllyInteractionContextData

- Structure
  - `itemID`: number?
  - `locationName`: cstring?
  - `activityDifficultyID`: number?
  - `activityDifficultyLevel`: number?

### RecentAllyInteractionData

- Structure
  - `interactions`: RecentAllyInteraction[]
  - `note`: string?

### RecentAllyStateData

- Structure
  - `isOnline`: bool
  - `isDND`: bool
  - `isAFK`: bool
  - `isConvertedLegacyFriend`: bool
  - `pinExpirationDate`: time_t?
  - `friendRequestSentThisSession`: bool
  - `currentLocation`: string?
