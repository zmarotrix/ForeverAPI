# GamePad

Namespace: `C_GamePad`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_GamePad.AddSDLMapping](#c_gamepadaddsdlmapping) |  |  |
| ✅ | [C_GamePad.ApplyConfigs](#c_gamepadapplyconfigs) |  |  |
| ✅ | [C_GamePad.AxisIndexToConfigName](#c_gamepadaxisindextoconfigname) |  |  |
| ✅ | [C_GamePad.ButtonBindingToIndex](#c_gamepadbuttonbindingtoindex) |  |  |
| ✅ | [C_GamePad.ButtonIndexToBinding](#c_gamepadbuttonindextobinding) |  |  |
| ✅ | [C_GamePad.ButtonIndexToConfigName](#c_gamepadbuttonindextoconfigname) |  |  |
| ✅ | [C_GamePad.ClearLedColor](#c_gamepadclearledcolor) |  |  |
| ✅ | [C_GamePad.DeleteConfig](#c_gamepaddeleteconfig) |  |  |
| ✅ | [C_GamePad.GetActiveDeviceID](#c_gamepadgetactivedeviceid) | 1 value | 1 value |
| ✅ | [C_GamePad.GetAllConfigIDs](#c_gamepadgetallconfigids) | 1 value | 1 value |
| ✅ | [C_GamePad.GetAllDeviceIDs](#c_gamepadgetalldeviceids) | 1 value | 1 value |
| ✅ | [C_GamePad.GetAllowHoverEventsWithFreeLook](#c_gamepadgetallowhovereventswithfreelook) | 1 value | 1 value |
| ✅ | [C_GamePad.GetCombinedDeviceID](#c_gamepadgetcombineddeviceid) | 1 value | 1 value |
| ✅ | [C_GamePad.GetConfig](#c_gamepadgetconfig) |  |  |
| ✅ | [C_GamePad.GetDeviceMappedState](#c_gamepadgetdevicemappedstate) | 1 value | 1 value |
| ✅ | [C_GamePad.GetDeviceRawState](#c_gamepadgetdevicerawstate) |  |  |
| ✅ | [C_GamePad.GetLedColor](#c_gamepadgetledcolor) | 1 value | 1 value |
| ✅ | [C_GamePad.GetPowerLevel](#c_gamepadgetpowerlevel) | 1 value | 1 value |
| ✅ | [C_GamePad.IsEnabled](#c_gamepadisenabled) | 1 value | 1 value |
| ✅ | [C_GamePad.SetAllowHoverEventsWithFreeLook](#c_gamepadsetallowhovereventswithfreelook) |  |  |
| ✅ | [C_GamePad.SetConfig](#c_gamepadsetconfig) |  |  |
| ✅ | [C_GamePad.SetLedColor](#c_gamepadsetledcolor) |  |  |
| ✅ | [C_GamePad.SetVibration](#c_gamepadsetvibration) |  |  |
| ✅ | [C_GamePad.StickIndexToConfigName](#c_gamepadstickindextoconfigname) |  |  |
| ✅ | [C_GamePad.StopVibration](#c_gamepadstopvibration) |  |  |

### C_GamePad.AddSDLMapping

`C_GamePad.AddSDLMapping(platform: ClientPlatformType, mapping: cstring) → success: bool`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.ApplyConfigs

`C_GamePad.ApplyConfigs()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.AxisIndexToConfigName

`C_GamePad.AxisIndexToConfigName(axisIndex: number) → configName: cstring?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.ButtonBindingToIndex

`C_GamePad.ButtonBindingToIndex(bindingName: cstring) → buttonIndex: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.ButtonIndexToBinding

`C_GamePad.ButtonIndexToBinding(buttonIndex: number) → bindingName: cstring?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.ButtonIndexToConfigName

`C_GamePad.ButtonIndexToConfigName(buttonIndex: number) → configName: cstring?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.ClearLedColor

`C_GamePad.ClearLedColor()`

- Status: ✅ verified (function)
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.DeleteConfig

`C_GamePad.DeleteConfig(configID: GamePadConfigID)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.GetActiveDeviceID

`C_GamePad.GetActiveDeviceID() → deviceID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.GetAllConfigIDs

`C_GamePad.GetAllConfigIDs() → configIDs: GamePadConfigID[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.GetAllDeviceIDs

`C_GamePad.GetAllDeviceIDs() → deviceIDs: number[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.GetAllowHoverEventsWithFreeLook

`C_GamePad.GetAllowHoverEventsWithFreeLook() → enabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.GetCombinedDeviceID

`C_GamePad.GetCombinedDeviceID() → deviceID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.GetConfig

`C_GamePad.GetConfig(configID: GamePadConfigID) → config: GamePadConfig?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.GetDeviceMappedState

`C_GamePad.GetDeviceMappedState(deviceID: number?) → state: GamePadMappedState?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.GetDeviceRawState

`C_GamePad.GetDeviceRawState(deviceID: number) → rawState: GamePadRawState?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.GetLedColor

`C_GamePad.GetLedColor() → color: colorRGB`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{GenerateHexColor=function,GenerateHexColorMarkup=function,GenerateHexColorNoAlpha=function,GetHSL=function,GetRGB=function,GetRGBA=function,GetRGBAAsBytes=function,GetRGBAsBytes=function,IsEqualTo=function,IsRGBEqualTo=function,OnLoad=function,SetRGB=function,SetRGBA=function,WrapTextInColorCode=function,b=number,g=number,r=number}`
- Called in combat: returned 1 value: `table{GenerateHexColor=function,GenerateHexColorMarkup=function,GenerateHexColorNoAlpha=function,GetHSL=function,GetRGB=function,GetRGBA=function,GetRGBAAsBytes=function,GetRGBAsBytes=function,IsEqualTo=function,IsRGBEqualTo=function,OnLoad=function,SetRGB=function,SetRGBA=function,WrapTextInColorCode=function,b=number,g=number,r=number}`
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.GetPowerLevel

`C_GamePad.GetPowerLevel(deviceID: number?) → powerLevel: GamePadPowerLevel`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.IsEnabled

`C_GamePad.IsEnabled() → enabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.SetAllowHoverEventsWithFreeLook

`C_GamePad.SetAllowHoverEventsWithFreeLook(enable: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.SetConfig

`C_GamePad.SetConfig(config: GamePadConfig)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.SetLedColor

`C_GamePad.SetLedColor(color: colorRGB)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.SetVibration

`C_GamePad.SetVibration(vibrationType: cstring, intensity: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.StickIndexToConfigName

`C_GamePad.StickIndexToConfigName(stickIndex: number) → configName: cstring?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GamePadDocumentation.lua`

### C_GamePad.StopVibration

`C_GamePad.StopVibration()`

- Status: ✅ verified (function)
- Source: client docs `GamePadDocumentation.lua`

## Events

### GAME_PAD_ACTIVE_CHANGED

- Status: ✅ verified
- Payload: `isActive: bool`
- fires synchronously (Blizzard's docs)

### GAME_PAD_ALLOW_HOVER_EVENTS_WITH_FREE_LOOK_CHANGED

- Status: ✅ verified
- Payload: `enabled: bool`
- fires synchronously (Blizzard's docs)

### GAME_PAD_CONFIGS_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 35 times (0 in combat); argument kinds: ``

### GAME_PAD_CONNECTED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### GAME_PAD_DISCONNECTED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### GAME_PAD_POWER_CHANGED

- Status: ✅ verified
- Payload: `powerLevel: GamePadPowerLevel`
- fires synchronously (Blizzard's docs)

## Types

### GamePadAxisConfig

- Structure
  - `axis`: string
  - `shift`: number?
  - `scale`: number?
  - `deadzone`: number?
  - `buttonThreshold`: number?
  - `buttonPos`: string?
  - `buttonNeg`: string?
  - `comment`: string?

### GamePadConfig

- Structure
  - `comment`: string?
  - `name`: string?
  - `configID`: GamePadConfigID
  - `labelStyle`: string?
  - `rawButtonMappings`: GamePadRawButtonMapping[]
  - `rawAxisMappings`: GamePadRawAxisMapping[]
  - `axisConfigs`: GamePadAxisConfig[]
  - `stickConfigs`: GamePadStickConfig[]

### GamePadConfigID

- Structure
  - `vendorID`: number?
  - `productID`: number?

### GamePadMappedState

- Structure
  - `name`: string
  - `labelStyle`: string
  - `buttonCount`: number
  - `axisCount`: number
  - `stickCount`: number
  - `buttons`: bool[]
  - `axes`: number[]
  - `sticks`: GamePadStick[]

### GamePadRawAxisMapping

- Structure
  - `rawIndex`: number
  - `axis`: string?
  - `comment`: string?

### GamePadRawButtonMapping

- Structure
  - `rawIndex`: number
  - `button`: string?
  - `axis`: string?
  - `axisValue`: number?
  - `comment`: string?

### GamePadRawState

- Structure
  - `name`: string
  - `vendorID`: number
  - `productID`: number
  - `rawButtonCount`: number
  - `rawAxisCount`: number
  - `rawButtons`: bool[]
  - `rawAxes`: number[]

### GamePadStick

- Structure
  - `x`: number
  - `y`: number
  - `len`: number

### GamePadStickConfig

- Structure
  - `stick`: string
  - `axisX`: string?
  - `axisY`: string?
  - `deadzone`: number?
  - `deadzoneX`: number?
  - `deadzoneY`: number?
  - `comment`: string?
