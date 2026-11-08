# PerformanceScript

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [GetAddOnCPUUsage](#getaddoncpuusage) |  |  |
| ✅ | [GetAddOnMemoryUsage](#getaddonmemoryusage) |  |  |
| ✅ | [GetEventCPUUsage](#geteventcpuusage) |  |  |
| ✅ | [GetFrameCPUUsage](#getframecpuusage) |  |  |
| ✅ | [GetFunctionCPUUsage](#getfunctioncpuusage) |  |  |
| ✅ | [GetScriptCPUUsage](#getscriptcpuusage) |  |  |
| ✅ | [ResetCPUUsage](#resetcpuusage) |  |  |
| ✅ | [UpdateAddOnCPUUsage](#updateaddoncpuusage) |  |  |
| ✅ | [UpdateAddOnMemoryUsage](#updateaddonmemoryusage) |  |  |

### GetAddOnCPUUsage

`GetAddOnCPUUsage(name: uiAddon) → result: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerformanceDocumentation.lua`

### GetAddOnMemoryUsage

`GetAddOnMemoryUsage(name: uiAddon) → result: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerformanceDocumentation.lua`

### GetEventCPUUsage

`GetEventCPUUsage() → call_time: number, call_count: number`

- Status: ✅ verified (function)
- Source: client docs `PerformanceDocumentation.lua`

### GetFrameCPUUsage

`GetFrameCPUUsage(frame: SimpleFrame, includeChildren: bool = False) → call_time: number, call_count: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PerformanceDocumentation.lua`

### GetFunctionCPUUsage

`GetFunctionCPUUsage() → call_time: number, call_count: number`

- Status: ✅ verified (function)
- Source: client docs `PerformanceDocumentation.lua`

### GetScriptCPUUsage

`GetScriptCPUUsage() → result: number`

- Status: ✅ verified (function)
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
