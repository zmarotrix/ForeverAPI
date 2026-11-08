# NamePlateManager

Namespace: `C_NamePlateManager`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_NamePlateManager.GetNamePlateHitTestInsets](#c_nameplatemanagergetnameplatehittestinsets) |  |  |
| ❔ | [C_NamePlateManager.IsNamePlateUnitBehindCamera](#c_nameplatemanagerisnameplateunitbehindcamera) |  |  |
| ❔ | [C_NamePlateManager.SetNamePlateHitTestInsets](#c_nameplatemanagersetnameplatehittestinsets) |  |  |
| ❔ | [C_NamePlateManager.SetNamePlateSimplified](#c_nameplatemanagersetnameplatesimplified) |  |  |

### C_NamePlateManager.GetNamePlateHitTestInsets

`C_NamePlateManager.GetNamePlateHitTestInsets(type: NamePlateType) → left: uiUnit, right: uiUnit, top: uiUnit, bottom: uiUnit`

- Status: ❔ unverified
- Blizzard: Returns the values used to adjust the hit testing area for nameplates.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `NamePlateManagerDocumentation.lua`

### C_NamePlateManager.IsNamePlateUnitBehindCamera

`C_NamePlateManager.IsNamePlateUnitBehindCamera(unitToken: UnitTokenNamePlate) → isBehindCamera: bool`

- Status: ❔ unverified
- Blizzard: Returns whether the unit to which the nameplate is attached is behind the player's camera.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `NamePlateManagerDocumentation.lua`

### C_NamePlateManager.SetNamePlateHitTestInsets

`C_NamePlateManager.SetNamePlateHitTestInsets(type: NamePlateType, left: uiUnit, right: uiUnit, top: uiUnit, bottom: uiUnit)`

- Status: ❔ unverified
- Blizzard: Provide values to adjust the hit testing area for nameplates. Positive values will decrease the hit test area, negative values will increase it. Note that all hit testing is clamped to the bounds of the nameplate and can not be moved outside it.
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `NamePlateManagerDocumentation.lua`

### C_NamePlateManager.SetNamePlateSimplified

`C_NamePlateManager.SetNamePlateSimplified(unitToken: UnitTokenNamePlate, isSimplified: bool)`

- Status: ❔ unverified
- Blizzard: Set whether the nameplate attached to a unit is considered simplified, which can change the way it's displayed.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `NamePlateManagerDocumentation.lua`

## Events

### FORBIDDEN_NAME_PLATE_CREATED

- Status: ❔ unverified
- Payload: `namePlateFrame: NamePlateFrame`
- fires synchronously (Blizzard's docs)

### FORBIDDEN_NAME_PLATE_UNIT_ADDED

- Status: ❔ unverified
- Payload: `unitToken: UnitTokenType`
- fires synchronously (Blizzard's docs)

### FORBIDDEN_NAME_PLATE_UNIT_REMOVED

- Status: ❔ unverified
- Payload: `unitToken: UnitTokenType`
- fires synchronously (Blizzard's docs)

### NAME_PLATE_CREATED

- Status: ❔ unverified
- Payload: `namePlateFrame: NamePlateFrame`
- fires synchronously (Blizzard's docs)

### NAME_PLATE_UNIT_ADDED

- Status: ❔ unverified
- Payload: `unitToken: UnitTokenType`
- fires synchronously (Blizzard's docs)

### NAME_PLATE_UNIT_BEHIND_CAMERA_CHANGED

- Status: ❔ unverified
- Payload: `unitTarget: UnitTokenVariant`, `isBehindCamera: bool`
- fires synchronously (Blizzard's docs)

### NAME_PLATE_UNIT_REMOVED

- Status: ❔ unverified
- Payload: `unitToken: UnitTokenType`
- fires synchronously (Blizzard's docs)
