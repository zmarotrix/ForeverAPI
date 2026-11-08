# AddOnProfiler

Namespace: `C_AddOnProfiler`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_AddOnProfiler.AddMeasuredCallEvent](#c_addonprofileraddmeasuredcallevent) |  |  |
| ✅ | [C_AddOnProfiler.AddPerformanceMessageShown](#c_addonprofileraddperformancemessageshown) |  |  |
| ✅ | [C_AddOnProfiler.CheckForPerformanceMessage](#c_addonprofilercheckforperformancemessage) |  |  |
| ✅ | [C_AddOnProfiler.GetAddOnMetric](#c_addonprofilergetaddonmetric) |  |  |
| ✅ | [C_AddOnProfiler.GetApplicationMetric](#c_addonprofilergetapplicationmetric) | 1 value | 1 value |
| ✅ | [C_AddOnProfiler.GetOverallMetric](#c_addonprofilergetoverallmetric) | 1 value | 1 value |
| ✅ | [C_AddOnProfiler.GetTicksPerSecond](#c_addonprofilergettickspersecond) | 1 value | 1 value |
| ✅ | [C_AddOnProfiler.GetTopKAddOnsForMetric](#c_addonprofilergettopkaddonsformetric) |  |  |
| ✅ | [C_AddOnProfiler.IsEnabled](#c_addonprofilerisenabled) | 1 value | 1 value |
| ✅ | [C_AddOnProfiler.MeasureCall](#c_addonprofilermeasurecall) |  |  |

### C_AddOnProfiler.AddMeasuredCallEvent

`C_AddOnProfiler.AddMeasuredCallEvent(name: stringView)`

- Status: ✅ verified (function)
- Blizzard: Adds a measured event to any ongoing measured calls. If no such calls are currently taking place, this function does nothing.
- `name`: User-defined string describing the measured event. This should be kept under 48 bytes to avoid memory allocations.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnProfilerDocumentation.lua`

### C_AddOnProfiler.AddPerformanceMessageShown

`C_AddOnProfiler.AddPerformanceMessageShown(msg: AddOnPerformanceMessage)`

- Status: ✅ verified (function)
- Blizzard: Internal API for telemetry.
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnProfilerDocumentation.lua`

### C_AddOnProfiler.CheckForPerformanceMessage

`C_AddOnProfiler.CheckForPerformanceMessage() → msg: AddOnPerformanceMessage`

- Status: ✅ verified (function)
- Blizzard: Optimized check for determining if AddOns are severely impacting UI performance.
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `AddOnProfilerDocumentation.lua`

### C_AddOnProfiler.GetAddOnMetric

`C_AddOnProfiler.GetAddOnMetric(name: cstring, metric: AddOnProfilerMetric) → result: number`

- Status: ✅ verified (function)
- Blizzard: Gets an AddOn profiler value - all times returned are in milliseconds.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnProfilerDocumentation.lua`

### C_AddOnProfiler.GetApplicationMetric

`C_AddOnProfiler.GetApplicationMetric(metric: AddOnProfilerMetric) → result: number`

- Status: ✅ verified (function)
- Blizzard: Overall profiling data for the entire application (not just the UI)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `AddOnProfilerDocumentation.lua`

### C_AddOnProfiler.GetOverallMetric

`C_AddOnProfiler.GetOverallMetric(metric: AddOnProfilerMetric) → result: number`

- Status: ✅ verified (function)
- Blizzard: Overall profiling data for all addons
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `AddOnProfilerDocumentation.lua`

### C_AddOnProfiler.GetTicksPerSecond

`C_AddOnProfiler.GetTicksPerSecond() → frequency: BigInteger`

- Status: ✅ verified (function)
- Blizzard: Returns the number of profiling clock ticks that occur within a single real-time second.
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `AddOnProfilerDocumentation.lua`

### C_AddOnProfiler.GetTopKAddOnsForMetric

`C_AddOnProfiler.GetTopKAddOnsForMetric(metric: AddOnProfilerMetric, k: number) → results: AddOnProfilerResult[]`

- Status: ✅ verified (function)
- Blizzard: Gets top K AddOns for a given metric.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnProfilerDocumentation.lua`

### C_AddOnProfiler.IsEnabled

`C_AddOnProfiler.IsEnabled() → enabled: bool`

- Status: ✅ verified (function)
- Blizzard: AddOn profiler will be enabled for all users, but this will return false if it ever isn't
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `AddOnProfilerDocumentation.lua`

### C_AddOnProfiler.MeasureCall

`C_AddOnProfiler.MeasureCall(func: LuaValueVariant, arguments: LuaValueVariant) → results: AddOnProfilerCallResults, returns: LuaValueVariant`

- Status: ✅ verified (function)
- Blizzard: Performs a profiled measurement of a single function call with any supplied arguments.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnProfilerDocumentation.lua`

## Types

### AddOnPerformanceMessage

- Structure
  - `type`: AddOnPerformanceMessageType
  - `metric`: AddOnProfilerMetric
  - `addOnName`: string?
  - `metricValue`: number
  - `thresholdValue`: number

### AddOnProfilerCallEvent

- Structure
  - `name`: string
  - `allocatedBytes`: BigUInteger
  - `deallocatedBytes`: BigUInteger
  - `elapsedMilliseconds`: number
  - `elapsedTicks`: BigInteger

### AddOnProfilerCallResults

- Structure
  - `elapsedMilliseconds`: number
  - `elapsedTicks`: BigInteger
  - `allocatedBytes`: BigUInteger
  - `deallocatedBytes`: BigUInteger
  - `events`: AddOnProfilerCallEvent[]

### AddOnProfilerResult

- Structure
  - `addOnName`: cstring
  - `metricValue`: number
