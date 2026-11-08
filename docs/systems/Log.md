# Log

Namespace: `C_Log`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Log.LogErrorMessage](#c_loglogerrormessage) |  |  |
| ✅ | [C_Log.LogMessage](#c_loglogmessage) |  |  |
| ✅ | [C_Log.LogMessageWithPriority](#c_loglogmessagewithpriority) |  |  |
| ✅ | [C_Log.LogWarningMessage](#c_loglogwarningmessage) |  |  |

### C_Log.LogErrorMessage

`C_Log.LogErrorMessage(message: cstring)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LogDocumentation.lua`

### C_Log.LogMessage

`C_Log.LogMessage(message: cstring)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LogDocumentation.lua`

### C_Log.LogMessageWithPriority

`C_Log.LogMessageWithPriority(priority: LogPriority, message: cstring)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LogDocumentation.lua`

### C_Log.LogWarningMessage

`C_Log.LogWarningMessage(message: cstring)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LogDocumentation.lua`
