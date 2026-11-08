# SystemTime

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [GetGameTime](#getgametime) | 2 values |  |
| ✅ | [GetLocalGameTime](#getlocalgametime) | 2 values |  |
| ✅ | [GetServerTime](#getservertime) | 1 value |  |
| ✅ | [GetSessionTime](#getsessiontime) | 1 value |  |
| ✅ | [GetTickTime](#getticktime) | 1 value |  |
| ✅ | [GetTime](#gettime) | 1 value |  |
| ✅ | [IsUsingFixedTimeStep](#isusingfixedtimestep) | 1 value |  |

### GetGameTime

`GetGameTime() → hour: number, minute: number`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `number`, `number`
- Source: client docs `SystemTimeDocumentation.lua`

### GetLocalGameTime

`GetLocalGameTime() → hour: number, minute: number`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `number`, `number`
- Source: client docs `SystemTimeDocumentation.lua`

### GetServerTime

`GetServerTime() → time: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `SystemTimeDocumentation.lua`

### GetSessionTime

`GetSessionTime() → time: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `SystemTimeDocumentation.lua`

### GetTickTime

`GetTickTime() → time: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `SystemTimeDocumentation.lua`

### GetTime

`GetTime() → time: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `SystemTimeDocumentation.lua`

### IsUsingFixedTimeStep

`IsUsingFixedTimeStep() → isUsingFixedTimeStep: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `SystemTimeDocumentation.lua`
