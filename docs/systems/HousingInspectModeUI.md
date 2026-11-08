# HousingInspectModeUI

Namespace: `C_HousingInspectMode`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_HousingInspectMode.EnterInspectMode](#c_housinginspectmodeenterinspectmode) |  |  |
| ✅ | [C_HousingInspectMode.ExitInspectMode](#c_housinginspectmodeexitinspectmode) |  |  |
| ✅ | [C_HousingInspectMode.GetHoveredDecorGUID](#c_housinginspectmodegethovereddecorguid) | 1 value | 1 value |
| ✅ | [C_HousingInspectMode.IsHoveringDecor](#c_housinginspectmodeishoveringdecor) | 1 value | 1 value |
| ✅ | [C_HousingInspectMode.IsInInspectMode](#c_housinginspectmodeisininspectmode) | 1 value | 1 value |

### C_HousingInspectMode.EnterInspectMode

`C_HousingInspectMode.EnterInspectMode()`

- Status: ✅ verified (function)
- Blizzard: Enters inspect mode, enabling decor inspection
- Source: client docs `HousingInspectModeUIDocumentation.lua`

### C_HousingInspectMode.ExitInspectMode

`C_HousingInspectMode.ExitInspectMode()`

- Status: ✅ verified (function)
- Blizzard: Exits inspect mode, disabling decor inspection
- Source: client docs `HousingInspectModeUIDocumentation.lua`

### C_HousingInspectMode.GetHoveredDecorGUID

`C_HousingInspectMode.GetHoveredDecorGUID() → decorGUID: WOWGUID`

- Status: ✅ verified (function)
- Blizzard: Returns the GUID of the decor instance currently being hovered, if there is one
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `HousingInspectModeUIDocumentation.lua`

### C_HousingInspectMode.IsHoveringDecor

`C_HousingInspectMode.IsHoveringDecor() → isHoveringDecor: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if a decor instance is currently being hovered in inspect mode
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HousingInspectModeUIDocumentation.lua`

### C_HousingInspectMode.IsInInspectMode

`C_HousingInspectMode.IsInInspectMode() → isInInspectMode: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the player is currently in inspect mode
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HousingInspectModeUIDocumentation.lua`

## Events

### HOUSING_INSPECT_MODE_DECOR_HOVERED_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### HOUSING_INSPECT_MODE_STATE_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
