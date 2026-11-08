# LobbyMatchmakerInfo

Namespace: `C_LobbyMatchmakerInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_LobbyMatchmakerInfo.AbandonQueue](#c_lobbymatchmakerinfoabandonqueue) |  |  |
| ✅ | [C_LobbyMatchmakerInfo.EnterQueue](#c_lobbymatchmakerinfoenterqueue) |  |  |
| ✅ | [C_LobbyMatchmakerInfo.GetCurrQueuePlaylistEntry](#c_lobbymatchmakerinfogetcurrqueueplaylistentry) | 1 value |  |
| ✅ | [C_LobbyMatchmakerInfo.GetCurrQueueState](#c_lobbymatchmakerinfogetcurrqueuestate) | 1 value |  |
| ✅ | [C_LobbyMatchmakerInfo.GetQueueFromMainlineEnabled](#c_lobbymatchmakerinfogetqueuefrommainlineenabled) | 1 value |  |
| ✅ | [C_LobbyMatchmakerInfo.GetQueueStartTime](#c_lobbymatchmakerinfogetqueuestarttime) | 1 value |  |
| ✅ | [C_LobbyMatchmakerInfo.IsInQueue](#c_lobbymatchmakerinfoisinqueue) | 1 value |  |
| ✅ | [C_LobbyMatchmakerInfo.RespondToQueuePop](#c_lobbymatchmakerinforespondtoqueuepop) |  |  |

### C_LobbyMatchmakerInfo.AbandonQueue

`C_LobbyMatchmakerInfo.AbandonQueue()`

- Status: ✅ verified (function)
- Source: client docs `LobbyMatchmakerInfoDocumentation.lua`

### C_LobbyMatchmakerInfo.EnterQueue

`C_LobbyMatchmakerInfo.EnterQueue(playlistEntry: PartyPlaylistEntry)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LobbyMatchmakerInfoDocumentation.lua`

### C_LobbyMatchmakerInfo.GetCurrQueuePlaylistEntry

`C_LobbyMatchmakerInfo.GetCurrQueuePlaylistEntry() → playlistEntry: PartyPlaylistEntry`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `LobbyMatchmakerInfoDocumentation.lua`

### C_LobbyMatchmakerInfo.GetCurrQueueState

`C_LobbyMatchmakerInfo.GetCurrQueueState() → queueState: PlunderstormQueueState`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `LobbyMatchmakerInfoDocumentation.lua`

### C_LobbyMatchmakerInfo.GetQueueFromMainlineEnabled

`C_LobbyMatchmakerInfo.GetQueueFromMainlineEnabled() → queueFromMainlineEnabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `LobbyMatchmakerInfoDocumentation.lua`

### C_LobbyMatchmakerInfo.GetQueueStartTime

`C_LobbyMatchmakerInfo.GetQueueStartTime() → queueStartTime: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `LobbyMatchmakerInfoDocumentation.lua`

### C_LobbyMatchmakerInfo.IsInQueue

`C_LobbyMatchmakerInfo.IsInQueue() → isInQueue: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `LobbyMatchmakerInfoDocumentation.lua`

### C_LobbyMatchmakerInfo.RespondToQueuePop

`C_LobbyMatchmakerInfo.RespondToQueuePop(acceptQueue: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LobbyMatchmakerInfoDocumentation.lua`

## Events

### LOBBY_MATCHMAKER_QUEUE_ABANDONED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LOBBY_MATCHMAKER_QUEUE_ERROR

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LOBBY_MATCHMAKER_QUEUE_EXPIRED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LOBBY_MATCHMAKER_QUEUE_POPPED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LOBBY_MATCHMAKER_QUEUE_STATUS_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### LobbyMatchmakerQueueInfo

- Structure
  - `isQueueActive`: bool
  - `playlistEntryID`: PartyPlaylistEntry
  - `queueState`: PlunderstormQueueState
  - `queueStartTime`: number

### PlunderstormQueueState

- Enumeration — ✅ verified
  - `None` = 0
  - `Queued` = 1
  - `Proposed` = 2
  - `Suspended` = 3
