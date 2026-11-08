# Client

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [FlashClientIcon](#flashclienticon) |  |  |
| ✅ | [GetBillingTimeRested](#getbillingtimerested) | 1 value | 1 value |
| ✅ | [GetFileIDFromPath](#getfileidfrompath) |  |  |
| ✅ | [GetFramerate](#getframerate) | 1 value | 1 value |
| ✅ | [IsCpuBound](#iscpubound) | 1 value | 1 value |
| ✅ | [PlatformIsHandheld](#platformishandheld) |  |  |
| ✅ | [ReportBug](#reportbug) |  |  |
| ✅ | [ReportSuggestion](#reportsuggestion) |  |  |
| ✅ | [RestartGx](#restartgx) |  |  |
| ✅ | [Screenshot](#screenshot) |  |  |
| ✅ | [UIReload](#uireload) |  |  |
| ✅ | [UpdateWindow](#updatewindow) |  |  |

### FlashClientIcon

`FlashClientIcon(briefly: bool = False)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClientDocumentation.lua`

### GetBillingTimeRested

`GetBillingTimeRested() → billingTimeRested: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ClientDocumentation.lua`

### GetFileIDFromPath

`GetFileIDFromPath(filePath: cstring) → fileID: fileID`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClientDocumentation.lua`

### GetFramerate

`GetFramerate() → framerate: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ClientDocumentation.lua`

### IsCpuBound

`IsCpuBound() → isCpuBound: bool?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `ClientDocumentation.lua`

### PlatformIsHandheld

`PlatformIsHandheld() → isHandheld: bool`

- Status: ✅ verified (function)
- Source: client docs `ClientDocumentation.lua`

### ReportBug

`ReportBug(description: cstring)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClientDocumentation.lua`

### ReportSuggestion

`ReportSuggestion(description: cstring)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClientDocumentation.lua`

### RestartGx

`RestartGx()`

- Status: ✅ verified (function)
- Source: client docs `ClientDocumentation.lua`

### Screenshot

`Screenshot()`

- Status: ✅ verified (function)
- Source: client docs `ClientDocumentation.lua`

### UIReload

`UIReload()`

- Status: ✅ verified (function)
- Source: client docs `ClientDocumentation.lua`

### UpdateWindow

`UpdateWindow()`

- Status: ✅ verified (function)
- Source: client docs `ClientDocumentation.lua`
