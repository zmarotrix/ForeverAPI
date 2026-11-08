# PlayerLocationInfo

Namespace: `C_PlayerInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_PlayerInfo.GUIDIsPlayer](#c_playerinfoguidisplayer) |  |  |
| ❔ | [C_PlayerInfo.GetClass](#c_playerinfogetclass) |  |  |
| ❔ | [C_PlayerInfo.GetName](#c_playerinfogetname) |  |  |
| ❔ | [C_PlayerInfo.GetRace](#c_playerinfogetrace) |  |  |
| ❔ | [C_PlayerInfo.GetSex](#c_playerinfogetsex) |  |  |
| ❔ | [C_PlayerInfo.IsConnected](#c_playerinfoisconnected) |  |  |
| ❔ | [C_PlayerInfo.UnitIsSameServer](#c_playerinfounitissameserver) |  |  |

### C_PlayerInfo.GUIDIsPlayer

`C_PlayerInfo.GUIDIsPlayer(guid: WOWGUID) → isPlayer: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerLocationDocumentation.lua`

### C_PlayerInfo.GetClass

`C_PlayerInfo.GetClass(playerLocation: PlayerLocation) → className: cstring?, classFilename: cstring?, classID: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerLocationDocumentation.lua`

### C_PlayerInfo.GetName

`C_PlayerInfo.GetName(playerLocation: PlayerLocation) → name: string`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerLocationDocumentation.lua`

### C_PlayerInfo.GetRace

`C_PlayerInfo.GetRace(playerLocation: PlayerLocation) → raceID: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerLocationDocumentation.lua`

### C_PlayerInfo.GetSex

`C_PlayerInfo.GetSex(playerLocation: PlayerLocation) → sex: UnitSex?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerLocationDocumentation.lua`

### C_PlayerInfo.IsConnected

`C_PlayerInfo.IsConnected(playerLocation: PlayerLocation?) → isConnected: bool?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerLocationDocumentation.lua`

### C_PlayerInfo.UnitIsSameServer

`C_PlayerInfo.UnitIsSameServer(playerLocation: PlayerLocation) → unitIsSameServer: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PlayerLocationDocumentation.lua`
