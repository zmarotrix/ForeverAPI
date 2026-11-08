# CurveUtil

Namespace: `C_CurveUtil`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_CurveUtil.CreateColorCurve](#c_curveutilcreatecolorcurve) |  |  |
| ❔ | [C_CurveUtil.CreateCurve](#c_curveutilcreatecurve) |  |  |
| ❔ | [C_CurveUtil.EvaluateColorFromBoolean](#c_curveutilevaluatecolorfromboolean) |  |  |
| ❔ | [C_CurveUtil.EvaluateColorValueFromBoolean](#c_curveutilevaluatecolorvaluefromboolean) |  |  |
| ❔ | [C_CurveUtil.EvaluateGameCurve](#c_curveutilevaluategamecurve) |  |  |

### C_CurveUtil.CreateColorCurve

`C_CurveUtil.CreateColorCurve() → curve: LuaColorCurveObject`

- Status: ❔ unverified
- Blizzard: Returns a new color curve object with no assigned points.
- Source: client docs `CurveUtilDocumentation.lua`

### C_CurveUtil.CreateCurve

`C_CurveUtil.CreateCurve() → curve: LuaCurveObject`

- Status: ❔ unverified
- Blizzard: Returns a new curve object with no assigned points.
- Source: client docs `CurveUtilDocumentation.lua`

### C_CurveUtil.EvaluateColorFromBoolean

`C_CurveUtil.EvaluateColorFromBoolean(boolean: bool, valueIfTrue: colorRGBA, valueIfFalse: colorRGBA) → value: colorRGBA`

- Status: ❔ unverified
- Blizzard: Evaluates a potentially-secret boolean value and returns a color.
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `CurveUtilDocumentation.lua`

### C_CurveUtil.EvaluateColorValueFromBoolean

`C_CurveUtil.EvaluateColorValueFromBoolean(boolean: bool, valueIfTrue: SingleColorValue, valueIfFalse: SingleColorValue) → value: SingleColorValue`

- Status: ❔ unverified
- Blizzard: Evaluates a potentially-secret boolean value and returns a single color component (eg. alpha).
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `CurveUtilDocumentation.lua`

### C_CurveUtil.EvaluateGameCurve

`C_CurveUtil.EvaluateGameCurve(curveID: number, x: number) → y: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CurveUtilDocumentation.lua`
