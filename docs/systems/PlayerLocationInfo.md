# PlayerLocationInfo

Namespace: `C_PlayerInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_PlayerInfo.GUIDIsPlayer](#c_playerinfoguidisplayer) |  |  |
| ✅ | [C_PlayerInfo.GetClass](#c_playerinfogetclass) |  |  |
| ✅ | [C_PlayerInfo.GetName](#c_playerinfogetname) |  |  |
| ✅ | [C_PlayerInfo.GetRace](#c_playerinfogetrace) |  |  |
| ✅ | [C_PlayerInfo.GetSex](#c_playerinfogetsex) |  |  |
| ✅ | [C_PlayerInfo.IsConnected](#c_playerinfoisconnected) | 1 value | 1 value |
| ✅ | [C_PlayerInfo.UnitIsSameServer](#c_playerinfounitissameserver) |  |  |

### C_PlayerInfo.GUIDIsPlayer

`C_PlayerInfo.GUIDIsPlayer(guid: WOWGUID) → isPlayer: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerLocationDocumentation.lua`

### C_PlayerInfo.GetClass

`C_PlayerInfo.GetClass(playerLocation: PlayerLocation) → className: cstring?, classFilename: cstring?, classID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerLocationDocumentation.lua`

### C_PlayerInfo.GetName

`C_PlayerInfo.GetName(playerLocation: PlayerLocation) → name: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerLocationDocumentation.lua`

### C_PlayerInfo.GetRace

`C_PlayerInfo.GetRace(playerLocation: PlayerLocation) → raceID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerLocationDocumentation.lua`

### C_PlayerInfo.GetSex

`C_PlayerInfo.GetSex(playerLocation: PlayerLocation) → sex: UnitSex?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerLocationDocumentation.lua`

### C_PlayerInfo.IsConnected

`C_PlayerInfo.IsConnected(playerLocation: PlayerLocation?) → isConnected: bool?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `PlayerLocationDocumentation.lua`

### C_PlayerInfo.UnitIsSameServer

`C_PlayerInfo.UnitIsSameServer(playerLocation: PlayerLocation) → unitIsSameServer: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerLocationDocumentation.lua`
