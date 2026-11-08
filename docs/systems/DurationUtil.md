# DurationUtil

Namespace: `C_DurationUtil`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_DurationUtil.CreateDuration](#c_durationutilcreateduration) |  |  |
| ✅ | [C_DurationUtil.CreateDurationTextBinding](#c_durationutilcreatedurationtextbinding) |  |  |
| ✅ | [C_DurationUtil.CreateManualClock](#c_durationutilcreatemanualclock) |  |  |

### C_DurationUtil.CreateDuration

`C_DurationUtil.CreateDuration() → duration: LuaDurationObject`

- Status: ✅ verified (function)
- Blizzard: Creates a zero duration container that can represent a time span.
- Source: client docs `DurationUtilDocumentation.lua`

### C_DurationUtil.CreateDurationTextBinding

`C_DurationUtil.CreateDurationTextBinding() → binding: DurationTextBinding`

- Status: ✅ verified (function)
- Blizzard: Creates a duration text binding, which automatically updates a font string with formatted text derived from a duration object.
- Source: client docs `DurationUtilDocumentation.lua`

### C_DurationUtil.CreateManualClock

`C_DurationUtil.CreateManualClock() → clock: LuaDurationManualClock`

- Status: ✅ verified (function)
- Blizzard: Creates a manually driven time source for use with duration objects.
- Source: client docs `DurationUtilDocumentation.lua`
