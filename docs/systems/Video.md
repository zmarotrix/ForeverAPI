# Video

Namespace: `C_VideoOptions`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_VideoOptions.AreHighResTexturesAvailable](#c_videooptionsarehighrestexturesavailable) | 1 value | 1 value |
| ✅ | [C_VideoOptions.GetCurrentGameWindowSize](#c_videooptionsgetcurrentgamewindowsize) | 1 value | 1 value |
| ✅ | [C_VideoOptions.GetDefaultGameWindowSize](#c_videooptionsgetdefaultgamewindowsize) |  |  |
| ✅ | [C_VideoOptions.GetGameWindowSizes](#c_videooptionsgetgamewindowsizes) |  |  |
| ✅ | [C_VideoOptions.GetGxAdapterInfo](#c_videooptionsgetgxadapterinfo) | 1 value | 1 value |
| ✅ | [C_VideoOptions.IsLinearEnabledOnStart](#c_videooptionsislinearenabledonstart) | 1 value | 1 value |
| ✅ | [C_VideoOptions.IsOutlineModeSupported](#c_videooptionsisoutlinemodesupported) | 1 value | 1 value |
| ✅ | [C_VideoOptions.IsPBRWaterSupported](#c_videooptionsispbrwatersupported) | 1 value | 1 value |
| ✅ | [C_VideoOptions.IsSecondaryLightingSupported](#c_videooptionsissecondarylightingsupported) | 1 value | 1 value |
| ✅ | [C_VideoOptions.IsSpellVisualDensitySystemSupported](#c_videooptionsisspellvisualdensitysystemsupported) | 1 value | 1 value |
| ✅ | [C_VideoOptions.SetGameWindowSize](#c_videooptionssetgamewindowsize) |  |  |

### C_VideoOptions.AreHighResTexturesAvailable

`C_VideoOptions.AreHighResTexturesAvailable() → areAvailable: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `VideoDocumentation.lua`

### C_VideoOptions.GetCurrentGameWindowSize

`C_VideoOptions.GetCurrentGameWindowSize() → size: vector2`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{Add=function,Clone=function,Cross=function,DivideBy=function,Dot=function,GetLength=function,GetLengthSquared=function,GetXY=function,IsEqualTo=function,IsZero=function,Normalize=function,OnLoad=function,RotateDirection=function,ScaleBy=function,SetXY=function,Subtract=function,x=number,y=number}`
- Called in combat: returned 1 value: `table{Add=function,Clone=function,Cross=function,DivideBy=function,Dot=function,GetLength=function,GetLengthSquared=function,GetXY=function,IsEqualTo=function,IsZero=function,Normalize=function,OnLoad=function,RotateDirection=function,ScaleBy=function,SetXY=function,Subtract=function,x=number,y=number}`
- Source: client docs `VideoDocumentation.lua`

### C_VideoOptions.GetDefaultGameWindowSize

`C_VideoOptions.GetDefaultGameWindowSize(monitor: number) → size: vector2`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `VideoDocumentation.lua`

### C_VideoOptions.GetGameWindowSizes

`C_VideoOptions.GetGameWindowSizes(monitor: number, fullscreen: bool) → sizes: vector2[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `VideoDocumentation.lua`

### C_VideoOptions.GetGxAdapterInfo

`C_VideoOptions.GetGxAdapterInfo() → adapters: GxAdapterInfoDetails[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{[number]=table,[number]=table}`
- Called in combat: returned 1 value: `table{[number]=table,[number]=table}`
- Source: client docs `VideoDocumentation.lua`

### C_VideoOptions.IsLinearEnabledOnStart

`C_VideoOptions.IsLinearEnabledOnStart() → isEnabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `VideoDocumentation.lua`

### C_VideoOptions.IsOutlineModeSupported

`C_VideoOptions.IsOutlineModeSupported() → isSupported: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `VideoDocumentation.lua`

### C_VideoOptions.IsPBRWaterSupported

`C_VideoOptions.IsPBRWaterSupported() → isSupported: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `VideoDocumentation.lua`

### C_VideoOptions.IsSecondaryLightingSupported

`C_VideoOptions.IsSecondaryLightingSupported() → isSupported: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `VideoDocumentation.lua`

### C_VideoOptions.IsSpellVisualDensitySystemSupported

`C_VideoOptions.IsSpellVisualDensitySystemSupported() → isSupported: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `VideoDocumentation.lua`

### C_VideoOptions.SetGameWindowSize

`C_VideoOptions.SetGameWindowSize(x: number, y: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `VideoDocumentation.lua`

## Events

### ADAPTER_LIST_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### DISPLAY_SIZE_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 72 times (0 in combat); argument kinds: ``

### GLUE_SCREENSHOT_FAILED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### GLUE_SCREENSHOT_STARTED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### GLUE_SCREENSHOT_SUCCEEDED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### GX_RESTARTED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SCREENSHOT_FAILED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SCREENSHOT_STARTED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SCREENSHOT_SUCCEEDED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### GraphicsValidationResult

- Enumeration — ✅ verified
  - `Supported` = 0
  - `Illegal` = 1
  - `Unsupported` = 2
  - `Graphics` = 3
  - `DualCore` = 4
  - `QuadCore` = 5
  - `CpuMem_2` = 6
  - `CpuMem_4` = 7
  - `CpuMem_8` = 8
  - `Needs_5_0` = 9
  - `Needs_6_0` = 10
  - `NeedsRt` = 11
  - `NeedsDx12` = 12
  - `NeedsDx12Vrs2` = 13
  - `NeedsAppleGpu` = 14
  - `NeedsAmdGpu` = 15
  - `NeedsIntelGpu` = 16
  - `NeedsNvidiaGpu` = 17
  - `NeedsQualcommGpu` = 18
  - `NeedsMacOs_10_13` = 19
  - `NeedsMacOs_10_14` = 20
  - `NeedsMacOs_10_15` = 21
  - `NeedsMacOs_11_0` = 22
  - `NeedsMacOs_12_0` = 23
  - `NeedsMacOs_13_0` = 24
  - `NeedsWindows_10` = 25
  - `NeedsWindows_11` = 26
  - `MacOsUnsupported` = 27
  - `WindowsUnsupported` = 28
  - `LegacyUnsupported` = 29
  - `Dx11Unsupported` = 30
  - `Dx12Win7Unsupported` = 31
  - `RemoteDesktopUnsupported` = 32
  - `WineUnsupported` = 33
  - `NvapiWineUnsupported` = 34
  - `AppleGpuUnsupported` = 35
  - `AmdGpuUnsupported` = 36
  - `IntelGpuUnsupported` = 37
  - `NvidiaGpuUnsupported` = 38
  - `QualcommGpuUnsupported` = 39
  - `GpuDriver` = 40
  - `CompatMode` = 41
  - `Unknown` = 42

### GxAdapterInfoDetails

- Structure
  - `name`: string
  - `isLowPower`: bool
  - `isExternal`: bool
