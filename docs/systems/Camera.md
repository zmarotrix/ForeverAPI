# Camera

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [GetCameraFOVDefaults](#getcamerafovdefaults) | 3 values | 3 values |
| ✅ | [GetUICameraInfo](#getuicamerainfo) |  |  |

### GetCameraFOVDefaults

`GetCameraFOVDefaults() → fieldOfViewDegreesDefault: number, fieldOfViewDegreesPlayerMin: number, fieldOfViewDegreesPlayerMax: number`

- Status: ✅ verified (function)
- Called out of combat: returned 3 values: `number`, `number`, `number`
- Called in combat: returned 3 values: `number`, `number`, `number`
- Source: client docs `CameraDocumentation.lua`

### GetUICameraInfo

`GetUICameraInfo(uiCameraID: number) → posX: number, posY: number, posZ: number, lookAtX: number, lookAtY: number, lookAtZ: number, animID: number, animVariation: number, animFrame: number, useModelCenter: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CameraDocumentation.lua`
