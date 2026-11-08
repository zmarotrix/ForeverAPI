# GameError

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [GetGameMessageInfo](#getgamemessageinfo) |  |  |
| ❔ | [NotWhileDeadError](#notwhiledeaderror) |  |  |

### GetGameMessageInfo

`GetGameMessageInfo(gameErrorIndex: luaIndex) → errorName: cstring, soundKitID: number?, voiceID: number?`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GameErrorDocumentation.lua`

### NotWhileDeadError

`NotWhileDeadError()`

- Status: ❔ unverified
- Source: client docs `GameErrorDocumentation.lua`
