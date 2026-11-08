# UITimer

Namespace: `C_Timer`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Timer.After](#c_timerafter) |  |  |
| ✅ | [C_Timer.NewTicker](#c_timernewticker) |  |  |
| ✅ | [C_Timer.NewTimedSignalMap](#c_timernewtimedsignalmap) |  |  |
| ✅ | [C_Timer.NewTimer](#c_timernewtimer) |  |  |

### C_Timer.After

`C_Timer.After(seconds: number, callback: TimerCallback)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UITimerDocumentation.lua`

### C_Timer.NewTicker

`C_Timer.NewTicker(seconds: number, callback: TickerCallback, iterations: number?) → cbObject: TickerCallback`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UITimerDocumentation.lua`

### C_Timer.NewTimedSignalMap

`C_Timer.NewTimedSignalMap(callback: TimedSignalMapCallback) → signalMap: TimedSignalMap`

- Status: ✅ verified (function)
- Blizzard: Creates a new timed signal map that invokes the supplied callback with each key as it becomes due.
- `callback`: Callback to execute when each entry becomes due.
- `signalMap`: The newly created timed signal map.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UITimerDocumentation.lua`

### C_Timer.NewTimer

`C_Timer.NewTimer(seconds: number, callback: TickerCallback) → cbObject: TickerCallback`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UITimerDocumentation.lua`

## Types

### TickerCallback

- CallbackType

### TimerCallback

- CallbackType
