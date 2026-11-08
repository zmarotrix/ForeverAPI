# GamepadTargetingManager

Namespace: `C_GamepadTargeting`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_GamepadTargeting.Disable](#c_gamepadtargetingdisable) |  |  |
| ✅ | [C_GamepadTargeting.Enable](#c_gamepadtargetingenable) |  |  |
| ✅ | [C_GamepadTargeting.SetFilter](#c_gamepadtargetingsetfilter) |  |  |

### C_GamepadTargeting.Disable

`C_GamepadTargeting.Disable() → targetAlreadySelected: bool`

- Status: ✅ verified (function)
- Source: client docs `GamepadTargetingDocumentation.lua`

### C_GamepadTargeting.Enable

`C_GamepadTargeting.Enable()`

- Status: ✅ verified (function)
- Source: client docs `GamepadTargetingDocumentation.lua`

### C_GamepadTargeting.SetFilter

`C_GamepadTargeting.SetFilter(filter: GamepadTargetingFilters)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GamepadTargetingDocumentation.lua`

## Types

### GamepadTargetingFilters

- Enumeration — ✅ verified
  - `Hostile` = 0
  - `Friendly` = 1
  - `All` = 2
