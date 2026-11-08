# PerformanceScript

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [GetAddOnCPUUsage](#getaddoncpuusage) | 1 value | 1 value |
| ✅ | [GetAddOnMemoryUsage](#getaddonmemoryusage) | 1 value | 1 value |
| ✅ | [GetEventCPUUsage](#geteventcpuusage) | 2 values | 2 values |
| ✅ | [GetFrameCPUUsage](#getframecpuusage) |  |  |
| ✅ | [GetFunctionCPUUsage](#getfunctioncpuusage) | error | error |
| ✅ | [GetScriptCPUUsage](#getscriptcpuusage) | 1 value | 1 value |
| ✅ | [ResetCPUUsage](#resetcpuusage) |  |  |
| ✅ | [UpdateAddOnCPUUsage](#updateaddoncpuusage) |  |  |
| ✅ | [UpdateAddOnMemoryUsage](#updateaddonmemoryusage) |  |  |

### GetAddOnCPUUsage

`GetAddOnCPUUsage(name: uiAddon) → result: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `s:ApiProbe`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PerformanceDocumentation.lua`

### GetAddOnMemoryUsage

`GetAddOnMemoryUsage(name: uiAddon) → result: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `s:ApiProbe`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PerformanceDocumentation.lua`

### GetEventCPUUsage

`GetEventCPUUsage() → call_time: number, call_count: number`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `number`, `number`
- Called in combat: returned 2 values: `number`, `number`
- Source: client docs `PerformanceDocumentation.lua`

### GetFrameCPUUsage

`GetFrameCPUUsage(frame: SimpleFrame, includeChildren: bool = False) → call_time: number, call_count: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerformanceDocumentation.lua`

### GetFunctionCPUUsage

`GetFunctionCPUUsage() → call_time: number, call_count: number`

- Status: ✅ verified (function)
- Called out of combat: error: `Usage: GetFunctionCPUUsage(function[, includeSubroutines])`
- Called in combat: error: `Usage: GetFunctionCPUUsage(function[, includeSubroutines])`
- Source: client docs `PerformanceDocumentation.lua`

### GetScriptCPUUsage

`GetScriptCPUUsage() → result: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `PerformanceDocumentation.lua`

### ResetCPUUsage

`ResetCPUUsage()`

- Status: ✅ verified (function)
- Source: client docs `PerformanceDocumentation.lua`

### UpdateAddOnCPUUsage

`UpdateAddOnCPUUsage()`

- Status: ✅ verified (function)
- Source: client docs `PerformanceDocumentation.lua`

### UpdateAddOnMemoryUsage

`UpdateAddOnMemoryUsage()`

- Status: ✅ verified (function)
- Source: client docs `PerformanceDocumentation.lua`
