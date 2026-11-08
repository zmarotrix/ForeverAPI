# Input

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [GetCursorCenterPosition](#getcursorcenterposition) |  |  |
| ✅ | [GetCursorDelta](#getcursordelta) |  |  |
| ✅ | [GetCursorPosition](#getcursorposition) |  |  |
| ✅ | [GetMouseButtonClicked](#getmousebuttonclicked) |  |  |
| ✅ | [GetMouseButtonName](#getmousebuttonname) |  |  |
| ✅ | [GetMouseFoci](#getmousefoci) |  |  |
| ✅ | [GetStringFromModifiers](#getstringfrommodifiers) |  |  |
| ✅ | [IsAltKeyDown](#isaltkeydown) |  |  |
| ✅ | [IsControlKeyDown](#iscontrolkeydown) |  |  |
| ✅ | [IsCursorVisible](#iscursorvisible) |  |  |
| ✅ | [IsKeyDown](#iskeydown) |  |  |
| ✅ | [IsLeftAltKeyDown](#isleftaltkeydown) |  |  |
| ✅ | [IsLeftControlKeyDown](#isleftcontrolkeydown) |  |  |
| ✅ | [IsLeftMetaKeyDown](#isleftmetakeydown) |  |  |
| ✅ | [IsLeftShiftKeyDown](#isleftshiftkeydown) |  |  |
| ✅ | [IsMetaKeyDown](#ismetakeydown) |  |  |
| ✅ | [IsModifierKeyDown](#ismodifierkeydown) |  |  |
| ✅ | [IsMouseButtonDown](#ismousebuttondown) |  |  |
| ✅ | [IsRightAltKeyDown](#isrightaltkeydown) |  |  |
| ✅ | [IsRightControlKeyDown](#isrightcontrolkeydown) |  |  |
| ✅ | [IsRightMetaKeyDown](#isrightmetakeydown) |  |  |
| ✅ | [IsRightShiftKeyDown](#isrightshiftkeydown) |  |  |
| ✅ | [IsShiftKeyDown](#isshiftkeydown) |  |  |
| ✅ | [IsUsingGamepad](#isusinggamepad) |  |  |
| ✅ | [IsUsingMouse](#isusingmouse) |  |  |
| ✅ | [MakeModifiers](#makemodifiers) |  |  |
| ✅ | [SetCursorPosition](#setcursorposition) |  |  |
| ✅ | [SimulateMouseClick](#simulatemouseclick) |  |  |
| ✅ | [SimulateMouseDown](#simulatemousedown) |  |  |
| ✅ | [SimulateMouseUp](#simulatemouseup) |  |  |
| ✅ | [SimulateMouseWheel](#simulatemousewheel) |  |  |

### GetCursorCenterPosition

`GetCursorCenterPosition() → posX: number, posY: number`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### GetCursorDelta

`GetCursorDelta() → deltaX: number, deltaY: number`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### GetCursorPosition

`GetCursorPosition() → posX: number, posY: number`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### GetMouseButtonClicked

`GetMouseButtonClicked() → buttonName: cstring`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### GetMouseButtonName

`GetMouseButtonName(button: mouseButton) → buttonName: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InputDocumentation.lua`

### GetMouseFoci

`GetMouseFoci() → region: ScriptRegion[]`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### GetStringFromModifiers

`GetStringFromModifiers(modifiers: number) → modifierString: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InputDocumentation.lua`

### IsAltKeyDown

`IsAltKeyDown() → down: bool`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### IsControlKeyDown

`IsControlKeyDown() → down: bool`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### IsCursorVisible

`IsCursorVisible() → visible: bool`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### IsKeyDown

`IsKeyDown(keyOrMouseName: cstring, excludeBindingState: bool = False) → down: bool?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InputDocumentation.lua`

### IsLeftAltKeyDown

`IsLeftAltKeyDown() → down: bool`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### IsLeftControlKeyDown

`IsLeftControlKeyDown() → down: bool`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### IsLeftMetaKeyDown

`IsLeftMetaKeyDown() → down: bool`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### IsLeftShiftKeyDown

`IsLeftShiftKeyDown() → down: bool`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### IsMetaKeyDown

`IsMetaKeyDown() → down: bool`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### IsModifierKeyDown

`IsModifierKeyDown() → down: bool`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### IsMouseButtonDown

`IsMouseButtonDown(button: mouseButton?) → down: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InputDocumentation.lua`

### IsRightAltKeyDown

`IsRightAltKeyDown() → down: bool`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### IsRightControlKeyDown

`IsRightControlKeyDown() → down: bool`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### IsRightMetaKeyDown

`IsRightMetaKeyDown() → down: bool`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### IsRightShiftKeyDown

`IsRightShiftKeyDown() → down: bool`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### IsShiftKeyDown

`IsShiftKeyDown() → down: bool`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### IsUsingGamepad

`IsUsingGamepad() → down: bool`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### IsUsingMouse

`IsUsingMouse() → down: bool`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### MakeModifiers

`MakeModifiers() → modifiers: number`

- Status: ✅ verified (function)
- Source: client docs `InputDocumentation.lua`

### SetCursorPosition

`SetCursorPosition(xPosition: uiUnit, yPosition: uiUnit)`

- Status: ✅ verified (function)
- Blizzard: Insecure code can only call this once in response to gamepad input hardware events.
- RequiresLimitedInput (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InputDocumentation.lua`

### SimulateMouseClick

`SimulateMouseClick(button: mouseButton)`

- Status: ✅ verified (function)
- Blizzard: Effectively the same as SimulateMouseDown plus SimulateMouseUp and consumes limited input for both.
- MouseFocusValidForLimitedInput (Blizzard's docs; not checked in game)
- RequiresLimitedInput (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InputDocumentation.lua`

### SimulateMouseDown

`SimulateMouseDown(button: mouseButton)`

- Status: ✅ verified (function)
- Blizzard: Insecure code can only call this once in response to gamepad input hardware events.
- MouseFocusValidForLimitedInput (Blizzard's docs; not checked in game)
- RequiresLimitedInput (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InputDocumentation.lua`

### SimulateMouseUp

`SimulateMouseUp(button: mouseButton)`

- Status: ✅ verified (function)
- Blizzard: Insecure code can only call this once in response to gamepad input hardware events.
- MouseFocusValidForLimitedInput (Blizzard's docs; not checked in game)
- RequiresLimitedInput (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InputDocumentation.lua`

### SimulateMouseWheel

`SimulateMouseWheel(delta: number)`

- Status: ✅ verified (function)
- Blizzard: Insecure code can only call this once in response to gamepad input hardware events.
- MouseFocusValidForLimitedInput (Blizzard's docs; not checked in game)
- RequiresLimitedInput (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InputDocumentation.lua`

## Events

### INPUT_DEVICE_INTERFACE_TRANSITION

- Status: ✅ verified
- Payload: `newMode: InputDeviceInterfaceType`, `oldMode: InputDeviceInterfaceType`
- fires synchronously (Blizzard's docs)
