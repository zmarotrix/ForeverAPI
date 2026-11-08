# HousingInspectModeUI

Namespace: `C_HousingInspectMode`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_HousingInspectMode.EnterInspectMode](#c_housinginspectmodeenterinspectmode) |  |  |
| ❔ | [C_HousingInspectMode.ExitInspectMode](#c_housinginspectmodeexitinspectmode) |  |  |
| ❔ | [C_HousingInspectMode.GetHoveredDecorGUID](#c_housinginspectmodegethovereddecorguid) |  |  |
| ❔ | [C_HousingInspectMode.IsHoveringDecor](#c_housinginspectmodeishoveringdecor) |  |  |
| ❔ | [C_HousingInspectMode.IsInInspectMode](#c_housinginspectmodeisininspectmode) |  |  |

### C_HousingInspectMode.EnterInspectMode

`C_HousingInspectMode.EnterInspectMode()`

- Status: ❔ unverified
- Blizzard: Enters inspect mode, enabling decor inspection
- Source: client docs `HousingInspectModeUIDocumentation.lua`

### C_HousingInspectMode.ExitInspectMode

`C_HousingInspectMode.ExitInspectMode()`

- Status: ❔ unverified
- Blizzard: Exits inspect mode, disabling decor inspection
- Source: client docs `HousingInspectModeUIDocumentation.lua`

### C_HousingInspectMode.GetHoveredDecorGUID

`C_HousingInspectMode.GetHoveredDecorGUID() → decorGUID: WOWGUID`

- Status: ❔ unverified
- Blizzard: Returns the GUID of the decor instance currently being hovered, if there is one
- Source: client docs `HousingInspectModeUIDocumentation.lua`

### C_HousingInspectMode.IsHoveringDecor

`C_HousingInspectMode.IsHoveringDecor() → isHoveringDecor: bool`

- Status: ❔ unverified
- Blizzard: Returns true if a decor instance is currently being hovered in inspect mode
- Source: client docs `HousingInspectModeUIDocumentation.lua`

### C_HousingInspectMode.IsInInspectMode

`C_HousingInspectMode.IsInInspectMode() → isInInspectMode: bool`

- Status: ❔ unverified
- Blizzard: Returns true if the player is currently in inspect mode
- Source: client docs `HousingInspectModeUIDocumentation.lua`

## Events

### HOUSING_INSPECT_MODE_DECOR_HOVERED_CHANGED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### HOUSING_INSPECT_MODE_STATE_UPDATED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)
