# GameError

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [GetGameMessageInfo](#getgamemessageinfo) | 3 values | 3 values |
| ✅ | [NotWhileDeadError](#notwhiledeaderror) |  |  |

### GetGameMessageInfo

`GetGameMessageInfo(gameErrorIndex: luaIndex) → errorName: cstring, soundKitID: number?, voiceID: number?`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 3 values: `string`, `nil`, `nil`
- Called in combat: returned 3 values: `string`, `nil`, `nil`
- Source: client docs `GameErrorDocumentation.lua`

### NotWhileDeadError

`NotWhileDeadError()`

- Status: ✅ verified (function)
- Source: client docs `GameErrorDocumentation.lua`
