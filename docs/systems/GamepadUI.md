# GamepadUI

Namespace: `C_GamepadUI`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_GamepadUI.GetFirstGamepadActionBarStorageSlotIndexForActiveStance](#c_gamepaduigetfirstgamepadactionbarstorageslotindexforactivestance) | 1 value |  |
| ✅ | [C_GamepadUI.GetFirstGamepadActionStorageSlotIndex](#c_gamepaduigetfirstgamepadactionstorageslotindex) | 1 value |  |
| ✅ | [C_GamepadUI.GetFirstGamepadPetActionStorageSlotIndex](#c_gamepaduigetfirstgamepadpetactionstorageslotindex) | 1 value |  |
| ✅ | [C_GamepadUI.IsValidGamepadActionStorageSlotIndex](#c_gamepaduiisvalidgamepadactionstorageslotindex) |  |  |
| ✅ | [C_GamepadUI.IsValidGamepadPossessBarStorageSlotIndex](#c_gamepaduiisvalidgamepadpossessbarstorageslotindex) |  |  |

### C_GamepadUI.GetFirstGamepadActionBarStorageSlotIndexForActiveStance

`C_GamepadUI.GetFirstGamepadActionBarStorageSlotIndexForActiveStance() → activeStanceFirstGamepadStorageSlotIndex: luaIndex?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `GamepadUIDocumentation.lua`

### C_GamepadUI.GetFirstGamepadActionStorageSlotIndex

`C_GamepadUI.GetFirstGamepadActionStorageSlotIndex() → firstGamepadActionStorageSlotIndex: luaIndex`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `GamepadUIDocumentation.lua`

### C_GamepadUI.GetFirstGamepadPetActionStorageSlotIndex

`C_GamepadUI.GetFirstGamepadPetActionStorageSlotIndex() → firstGamepadPetActionStorageSlotID: luaIndex`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `GamepadUIDocumentation.lua`

### C_GamepadUI.IsValidGamepadActionStorageSlotIndex

`C_GamepadUI.IsValidGamepadActionStorageSlotIndex(gamepadActionStorageSlotIndex: luaIndex) → isValid: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GamepadUIDocumentation.lua`

### C_GamepadUI.IsValidGamepadPossessBarStorageSlotIndex

`C_GamepadUI.IsValidGamepadPossessBarStorageSlotIndex(gamepadPossessBarStorageSlotIndex: luaIndex) → isValid: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GamepadUIDocumentation.lua`

## Events

### GAMEPAD_POSSESS_BAR_OVERRIDE_CHANGED

- Status: ✅ verified
- Payload: `oldOverride: GamepadPossessBarOverride`, `newOverride: GamepadPossessBarOverride`
- unique event (Blizzard's docs)

### GAMEPAD_STANCE_BAR_OVERRIDE_CHANGED

- Status: ✅ verified
- Payload: `oldOverride: GamepadStanceBarOverride`, `newOverride: GamepadStanceBarOverride`
- unique event (Blizzard's docs)

## Types

### GamepadActionBarConstants

- Constants — ✅ verified
  - `NUM_SLOTS_PER_GAMEPAD_ACTION_BAR_GROUP` = 4
  - `NUM_GROUPS_PER_GAMEPAD_ACTION_BAR` = 2
  - `NUM_SLOTS_PER_GAMEPAD_ACTION_BAR` = Constants.GamepadActionBarConstants.NUM_SLOTS_PER_GAMEPAD_ACTION_BAR_GROUP * Constants.GamepadActionBarConstants.NUM_GROUPS_PER_GAMEPAD_ACTION_BAR
  - `NUM_PAGEABLE_BARS_IN_GAMEPAD_ACTION_BAR_PAGE_UNIT` = 4
  - `NUM_PAGEABLE_SLOTS_PER_GAMEPAD_ACTION_BAR_PAGE_UNIT_STANDARD_PAGE` = Constants.GamepadActionBarConstants.NUM_PAGEABLE_BARS_IN_GAMEPAD_ACTION_BAR_PAGE_UNIT * Constants.GamepadActionBarConstants.NUM_SLOTS_PER_GAMEPAD_ACTION_BAR
  - `NUM_RESERVED_SLOTS_PER_GAMEPAD_ACTION_BAR_PAGE_UNIT` = 4
  - `NUM_PAGES_PER_GAMEPAD_ACTION_BAR_PAGE_UNIT` = 4
  - `NUM_STANDARD_PAGES_PER_GAMEPAD_ACTION_BAR_PAGE_UNIT` = 3
  - `GAMEPAD_ACTION_BAR_PAGE_UNIT_SPECIAL_PAGE_INDEX` = 4
  - `NUM_PAGEABLE_SLOTS_PER_GAMEPAD_ACTION_BAR_PAGE_UNIT` = Constants.GamepadActionBarConstants.NUM_PAGEABLE_SLOTS_PER_GAMEPAD_ACTION_BAR_PAGE_UNIT_STANDARD_PAGE * Constants.GamepadActionBarConstants.NUM_STANDARD_PAGES_PER_GAMEPAD_ACTION_BAR_PAGE_UNIT
  - `NUM_GAMEPAD_STANCE_ACTION_BARS` = 5

### GamepadPossessBarOverride

- Enumeration — ✅ verified
  - `SpecialPageTopBar` = 1
  - `Page1LeftBar` = 2
  - `Page1RightBar` = 3
  - `Page1BottomBar` = 4
  - `Page2TopBar` = 5
  - `Page2LeftBar` = 6
  - `Page2RightBar` = 7
  - `Page2BottomBar` = 8
  - `Page3TopBar` = 9
  - `Page3LeftBar` = 10
  - `Page3RightBar` = 11
  - `Page3BottomBar` = 12

### GamepadStanceBarOverride

- Enumeration — ✅ verified
  - `None` = 1
  - `Page1LeftBar` = 2
  - `Page1RightBar` = 3
  - `Page1BottomBar` = 4
  - `Page2TopBar` = 5
  - `Page2LeftBar` = 6
  - `Page2RightBar` = 7
  - `Page2BottomBar` = 8
  - `Page3TopBar` = 9
  - `Page3LeftBar` = 10
  - `Page3RightBar` = 11
  - `Page3BottomBar` = 12
