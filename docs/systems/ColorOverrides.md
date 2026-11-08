# ColorOverrides

Namespace: `C_ColorOverrides`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_ColorOverrides.ClearColorOverrides](#c_coloroverridesclearcoloroverrides) |  |  |
| ❔ | [C_ColorOverrides.GetColorForQuality](#c_coloroverridesgetcolorforquality) |  |  |
| ❔ | [C_ColorOverrides.GetColorOverrideInfo](#c_coloroverridesgetcoloroverrideinfo) |  |  |
| ❔ | [C_ColorOverrides.GetDefaultColorForQuality](#c_coloroverridesgetdefaultcolorforquality) |  |  |
| ❔ | [C_ColorOverrides.RemoveColorOverride](#c_coloroverridesremovecoloroverride) |  |  |
| ❔ | [C_ColorOverrides.SetColorOverride](#c_coloroverridessetcoloroverride) |  |  |

### C_ColorOverrides.ClearColorOverrides

`C_ColorOverrides.ClearColorOverrides()`

- Status: ❔ unverified
- Source: client docs `ColorOverridesDocumentation.lua`

### C_ColorOverrides.GetColorForQuality

`C_ColorOverrides.GetColorForQuality(quality: ItemQuality) → color: colorRGBA`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ColorOverridesDocumentation.lua`

### C_ColorOverrides.GetColorOverrideInfo

`C_ColorOverrides.GetColorOverrideInfo(overrideType: ColorOverride) → overrideInfo: ColorOverrideInfo?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ColorOverridesDocumentation.lua`

### C_ColorOverrides.GetDefaultColorForQuality

`C_ColorOverrides.GetDefaultColorForQuality(quality: ItemQuality) → color: colorRGBA`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ColorOverridesDocumentation.lua`

### C_ColorOverrides.RemoveColorOverride

`C_ColorOverrides.RemoveColorOverride(overrideType: ColorOverride)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ColorOverridesDocumentation.lua`

### C_ColorOverrides.SetColorOverride

`C_ColorOverrides.SetColorOverride(overrideType: ColorOverride, color: colorRGBA)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ColorOverridesDocumentation.lua`

## Events

### COLOR_OVERRIDES_RESET

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### COLOR_OVERRIDE_UPDATED

- Status: ❔ unverified
- Payload: `overrideType: ColorOverride`
- fires synchronously (Blizzard's docs)

## Types

### ColorOverrideInfo

- Structure
  - `overrideType`: ColorOverride
  - `overrideColor`: colorRGB
  - `overrideColorString`: string
