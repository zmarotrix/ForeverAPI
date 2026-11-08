# NamePlate

Namespace: `C_NamePlate`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_NamePlate.GetNamePlateForUnit](#c_nameplategetnameplateforunit) |  |  |
| ❔ | [C_NamePlate.GetNamePlateSize](#c_nameplategetnameplatesize) |  |  |
| ❔ | [C_NamePlate.GetNamePlates](#c_nameplategetnameplates) |  |  |
| ❔ | [C_NamePlate.SetNamePlateSize](#c_nameplatesetnameplatesize) |  |  |

### C_NamePlate.GetNamePlateForUnit

`C_NamePlate.GetNamePlateForUnit(unitToken: UnitTokenNamePlate, includeForbidden: bool = False) → nameplate: NamePlateFrame`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `NamePlateDocumentation.lua`

### C_NamePlate.GetNamePlateSize

`C_NamePlate.GetNamePlateSize() → width: uiUnit, height: uiUnit`

- Status: ❔ unverified
- Source: client docs `NamePlateDocumentation.lua`

### C_NamePlate.GetNamePlates

`C_NamePlate.GetNamePlates() → nameplates: NamePlateFrame[]`

- Status: ❔ unverified
- Source: client docs `NamePlateDocumentation.lua`

### C_NamePlate.SetNamePlateSize

`C_NamePlate.SetNamePlateSize(width: uiUnit, height: uiUnit)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `NamePlateDocumentation.lua`
