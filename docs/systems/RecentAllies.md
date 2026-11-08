# RecentAllies

Namespace: `C_RecentAllies`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_RecentAllies.CanSetRecentAllyNote](#c_recentalliescansetrecentallynote) |  |  |
| ❔ | [C_RecentAllies.GetRecentAllies](#c_recentalliesgetrecentallies) |  |  |
| ❔ | [C_RecentAllies.GetRecentAllyByFullName](#c_recentalliesgetrecentallybyfullname) |  |  |
| ❔ | [C_RecentAllies.GetRecentAllyByGUID](#c_recentalliesgetrecentallybyguid) |  |  |
| ❔ | [C_RecentAllies.IsInteractionCategoryFilterSupportedForCurrentGameType](#c_recentalliesisinteractioncategoryfiltersupportedforcurrentgametype) |  |  |
| ❔ | [C_RecentAllies.IsRecentAllyByFullName](#c_recentalliesisrecentallybyfullname) |  |  |
| ❔ | [C_RecentAllies.IsRecentAllyByGUID](#c_recentalliesisrecentallybyguid) |  |  |
| ❔ | [C_RecentAllies.IsRecentAllyDataReady](#c_recentalliesisrecentallydataready) |  |  |
| ❔ | [C_RecentAllies.IsRecentAllyPinned](#c_recentalliesisrecentallypinned) |  |  |
| ❔ | [C_RecentAllies.IsSystemEnabled](#c_recentalliesissystemenabled) |  |  |
| ❔ | [C_RecentAllies.IsSystemSupported](#c_recentalliesissystemsupported) |  |  |
| ❔ | [C_RecentAllies.SearchRecentAllies](#c_recentalliessearchrecentallies) |  |  |
| ❔ | [C_RecentAllies.SetRecentAllyNote](#c_recentalliessetrecentallynote) |  |  |
| ❔ | [C_RecentAllies.SetRecentAllyPinned](#c_recentalliessetrecentallypinned) |  |  |
| ❔ | [C_RecentAllies.TryRequestRecentAlliesData](#c_recentalliestryrequestrecentalliesdata) |  |  |

### C_RecentAllies.CanSetRecentAllyNote

`C_RecentAllies.CanSetRecentAllyNote(characterGUID: WOWGUID) → canSetNote: bool`

- Status: ❔ unverified
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.GetRecentAllies

`C_RecentAllies.GetRecentAllies() → recentAlliesData: RecentAllyData[]`

- Status: ❔ unverified
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.GetRecentAllyByFullName

`C_RecentAllies.GetRecentAllyByFullName(fullCharacterName: cstring) → recentAllyData: RecentAllyData?`

- Status: ❔ unverified
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.GetRecentAllyByGUID

`C_RecentAllies.GetRecentAllyByGUID(characterGUID: WOWGUID) → recentAllyData: RecentAllyData?`

- Status: ❔ unverified
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.IsInteractionCategoryFilterSupportedForCurrentGameType

`C_RecentAllies.IsInteractionCategoryFilterSupportedForCurrentGameType(interactionCategoryFilter: RecentAlliesInteractionCategoryFilter) → isInteractionCategoryFilterSupportedForCurrentGameType: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.IsRecentAllyByFullName

`C_RecentAllies.IsRecentAllyByFullName(fullCharacterName: cstring) → isRecentAlly: bool`

- Status: ❔ unverified
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.IsRecentAllyByGUID

`C_RecentAllies.IsRecentAllyByGUID(characterGUID: WOWGUID) → isRecentAlly: bool`

- Status: ❔ unverified
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.IsRecentAllyDataReady

`C_RecentAllies.IsRecentAllyDataReady() → isReady: bool`

- Status: ❔ unverified
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.IsRecentAllyPinned

`C_RecentAllies.IsRecentAllyPinned(characterGUID: WOWGUID) → isPinned: bool`

- Status: ❔ unverified
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.IsSystemEnabled

`C_RecentAllies.IsSystemEnabled() → isRecentAllySystemEnabled: bool`

- Status: ❔ unverified
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.IsSystemSupported

`C_RecentAllies.IsSystemSupported() → isRecentAllySystemSupported: bool`

- Status: ❔ unverified
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.SearchRecentAllies

`C_RecentAllies.SearchRecentAllies(searchInfo: RecentAlliesSearchInfo) → recentAlliesData: RecentAllyData[]`

- Status: ❔ unverified
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.SetRecentAllyNote

`C_RecentAllies.SetRecentAllyNote(characterGUID: WOWGUID, note: cstring)`

- Status: ❔ unverified
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.SetRecentAllyPinned

`C_RecentAllies.SetRecentAllyPinned(characterGUID: WOWGUID, isPinned: bool)`

- Status: ❔ unverified
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RecentAlliesDocumentation.lua`

### C_RecentAllies.TryRequestRecentAlliesData

`C_RecentAllies.TryRequestRecentAlliesData()`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- RequiresRecentAllies (Blizzard's docs; not checked in game)
- Source: client docs `RecentAlliesDocumentation.lua`

## Events

### LET_RECENT_ALLIES_SEE_LOCATION_SETTING_UPDATED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### RECENT_ALLIES_CACHE_UPDATE

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

### RECENT_ALLIES_DATA_READY

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### RECENT_ALLIES_SYSTEM_STATUS_UPDATED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### RECENT_ALLY_DATA_UPDATED

- Status: ❔ unverified
- Payload: `characterGUID: WOWGUID`
- fires synchronously (Blizzard's docs)

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
