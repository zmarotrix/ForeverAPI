# NamePlateManager

Namespace: `C_NamePlateManager`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_NamePlateManager.GetNamePlateHitTestInsets](#c_nameplatemanagergetnameplatehittestinsets) | 4 values | 4 values |
| ✅ | [C_NamePlateManager.IsNamePlateUnitBehindCamera](#c_nameplatemanagerisnameplateunitbehindcamera) | 1 value | 1 value |
| ✅ | [C_NamePlateManager.SetNamePlateHitTestInsets](#c_nameplatemanagersetnameplatehittestinsets) |  |  |
| ✅ | [C_NamePlateManager.SetNamePlateSimplified](#c_nameplatemanagersetnameplatesimplified) |  |  |

### C_NamePlateManager.GetNamePlateHitTestInsets

`C_NamePlateManager.GetNamePlateHitTestInsets(type: NamePlateType) → left: uiUnit, right: uiUnit, top: uiUnit, bottom: uiUnit`

- Status: ✅ verified (function)
- Blizzard: Returns the values used to adjust the hit testing area for nameplates.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 4 values: `number`, `number`, `number`, `number`
- Called in combat: returned 4 values: `number`, `number`, `number`, `number`
- Source: client docs `NamePlateManagerDocumentation.lua`

### C_NamePlateManager.IsNamePlateUnitBehindCamera

`C_NamePlateManager.IsNamePlateUnitBehindCamera(unitToken: UnitTokenNamePlate) → isBehindCamera: bool`

- Status: ✅ verified (function)
- Blizzard: Returns whether the unit to which the nameplate is attached is behind the player's camera.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `player`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `NamePlateManagerDocumentation.lua`

### C_NamePlateManager.SetNamePlateHitTestInsets

`C_NamePlateManager.SetNamePlateHitTestInsets(type: NamePlateType, left: uiUnit, right: uiUnit, top: uiUnit, bottom: uiUnit)`

- Status: ✅ verified (function)
- Blizzard: Provide values to adjust the hit testing area for nameplates. Positive values will decrease the hit test area, negative values will increase it. Note that all hit testing is clamped to the bounds of the nameplate and can not be moved outside it.
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `NamePlateManagerDocumentation.lua`

### C_NamePlateManager.SetNamePlateSimplified

`C_NamePlateManager.SetNamePlateSimplified(unitToken: UnitTokenNamePlate, isSimplified: bool)`

- Status: ✅ verified (function)
- Blizzard: Set whether the nameplate attached to a unit is considered simplified, which can change the way it's displayed.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `NamePlateManagerDocumentation.lua`

## Events

### FORBIDDEN_NAME_PLATE_CREATED

- Status: ✅ verified
- Payload: `namePlateFrame: NamePlateFrame`
- fires synchronously (Blizzard's docs)
- Seen firing 6 times (0 in combat); argument kinds: `t`

### FORBIDDEN_NAME_PLATE_UNIT_ADDED

- Status: ✅ verified
- Payload: `unitToken: UnitTokenType`
- fires synchronously (Blizzard's docs)
- Seen firing 19 times (0 in combat); argument kinds: `s`

### FORBIDDEN_NAME_PLATE_UNIT_REMOVED

- Status: ✅ verified
- Payload: `unitToken: UnitTokenType`
- fires synchronously (Blizzard's docs)
- Seen firing 19 times (0 in combat); argument kinds: `s`

### NAME_PLATE_CREATED

- Status: ✅ verified
- Payload: `namePlateFrame: NamePlateFrame`
- fires synchronously (Blizzard's docs)
- Seen firing 160 times (49 in combat); argument kinds: `t`

### NAME_PLATE_UNIT_ADDED

- Status: ✅ verified
- Payload: `unitToken: UnitTokenType`
- fires synchronously (Blizzard's docs)
- Seen firing 5094 times (2695 in combat); argument kinds: `s`

### NAME_PLATE_UNIT_BEHIND_CAMERA_CHANGED

- Status: ✅ verified
- Payload: `unitTarget: UnitTokenVariant`, `isBehindCamera: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 27 times (14 in combat); argument kinds: `s,b`

### NAME_PLATE_UNIT_REMOVED

- Status: ✅ verified
- Payload: `unitToken: UnitTokenType`
- fires synchronously (Blizzard's docs)
- Seen firing 5094 times (3032 in combat); argument kinds: `s`
