# ColorOverrides

Namespace: `C_ColorOverrides`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ColorOverrides.ClearColorOverrides](#c_coloroverridesclearcoloroverrides) |  |  |
| ✅ | [C_ColorOverrides.GetColorForQuality](#c_coloroverridesgetcolorforquality) | 1 value | 1 value |
| ✅ | [C_ColorOverrides.GetColorOverrideInfo](#c_coloroverridesgetcoloroverrideinfo) | 1 value | 1 value |
| ✅ | [C_ColorOverrides.GetDefaultColorForQuality](#c_coloroverridesgetdefaultcolorforquality) | 1 value | 1 value |
| ✅ | [C_ColorOverrides.RemoveColorOverride](#c_coloroverridesremovecoloroverride) |  |  |
| ✅ | [C_ColorOverrides.SetColorOverride](#c_coloroverridessetcoloroverride) |  |  |

### C_ColorOverrides.ClearColorOverrides

`C_ColorOverrides.ClearColorOverrides()`

- Status: ✅ verified (function)
- Source: client docs `ColorOverridesDocumentation.lua`

### C_ColorOverrides.GetColorForQuality

`C_ColorOverrides.GetColorForQuality(quality: ItemQuality) → color: colorRGBA`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `table{GenerateHexColor=function,GenerateHexColorMarkup=function,GenerateHexColorNoAlpha=function,GetHSL=function,GetRGB=function,GetRGBA=function,GetRGBAAsBytes=function,GetRGBAsBytes=function,IsEqualTo=function,IsRGBEqualTo=function,OnLoad=function,SetRGB=function,SetRGBA=function,WrapTextInColorCode=function,a=number,b=number,g=number,r=number}`
- Called in combat: returned 1 value: `table{GenerateHexColor=function,GenerateHexColorMarkup=function,GenerateHexColorNoAlpha=function,GetHSL=function,GetRGB=function,GetRGBA=function,GetRGBAAsBytes=function,GetRGBAsBytes=function,IsEqualTo=function,IsRGBEqualTo=function,OnLoad=function,SetRGB=function,SetRGBA=function,WrapTextInColorCode=function,a=number,b=number,g=number,r=number}`
- Source: client docs `ColorOverridesDocumentation.lua`

### C_ColorOverrides.GetColorOverrideInfo

`C_ColorOverrides.GetColorOverrideInfo(overrideType: ColorOverride) → overrideInfo: ColorOverrideInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `ColorOverridesDocumentation.lua`

### C_ColorOverrides.GetDefaultColorForQuality

`C_ColorOverrides.GetDefaultColorForQuality(quality: ItemQuality) → color: colorRGBA`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `table{GenerateHexColor=function,GenerateHexColorMarkup=function,GenerateHexColorNoAlpha=function,GetHSL=function,GetRGB=function,GetRGBA=function,GetRGBAAsBytes=function,GetRGBAsBytes=function,IsEqualTo=function,IsRGBEqualTo=function,OnLoad=function,SetRGB=function,SetRGBA=function,WrapTextInColorCode=function,a=number,b=number,g=number,r=number}`
- Called in combat: returned 1 value: `table{GenerateHexColor=function,GenerateHexColorMarkup=function,GenerateHexColorNoAlpha=function,GetHSL=function,GetRGB=function,GetRGBA=function,GetRGBAAsBytes=function,GetRGBAsBytes=function,IsEqualTo=function,IsRGBEqualTo=function,OnLoad=function,SetRGB=function,SetRGBA=function,WrapTextInColorCode=function,a=number,b=number,g=number,r=number}`
- Source: client docs `ColorOverridesDocumentation.lua`

### C_ColorOverrides.RemoveColorOverride

`C_ColorOverrides.RemoveColorOverride(overrideType: ColorOverride)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ColorOverridesDocumentation.lua`

### C_ColorOverrides.SetColorOverride

`C_ColorOverrides.SetColorOverride(overrideType: ColorOverride, color: colorRGBA)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ColorOverridesDocumentation.lua`

## Events

### COLOR_OVERRIDES_RESET

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### COLOR_OVERRIDE_UPDATED

- Status: ✅ verified
- Payload: `overrideType: ColorOverride`
- fires synchronously (Blizzard's docs)

## Types

### ColorOverrideInfo

- Structure
  - `overrideType`: ColorOverride
  - `overrideColor`: colorRGB
  - `overrideColorString`: string
