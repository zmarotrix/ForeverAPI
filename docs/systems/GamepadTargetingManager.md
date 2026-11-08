# GamepadTargetingManager

Namespace: `C_GamepadTargeting`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_GamepadTargeting.Disable](#c_gamepadtargetingdisable) |  |  |
| ❔ | [C_GamepadTargeting.Enable](#c_gamepadtargetingenable) |  |  |
| ❔ | [C_GamepadTargeting.SetFilter](#c_gamepadtargetingsetfilter) |  |  |

### C_GamepadTargeting.Disable

`C_GamepadTargeting.Disable() → targetAlreadySelected: bool`

- Status: ❔ unverified
- Source: client docs `GamepadTargetingDocumentation.lua`

### C_GamepadTargeting.Enable

`C_GamepadTargeting.Enable()`

- Status: ❔ unverified
- Source: client docs `GamepadTargetingDocumentation.lua`

### C_GamepadTargeting.SetFilter

`C_GamepadTargeting.SetFilter(filter: GamepadTargetingFilters)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GamepadTargetingDocumentation.lua`

## Types

### GamepadTargetingFilters

- Enumeration — ❔ unverified
  - `Hostile` = 0
  - `Friendly` = 1
  - `All` = 2
