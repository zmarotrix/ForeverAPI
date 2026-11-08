# UI

Namespace: `C_UI`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_UI.DoesAnyDisplayHaveNotch](#c_uidoesanydisplayhavenotch) |  |  |
| ✅ | [C_UI.GetTopLeftNotchSafeRegion](#c_uigettopleftnotchsaferegion) |  |  |
| ✅ | [C_UI.GetTopRightNotchSafeRegion](#c_uigettoprightnotchsaferegion) |  |  |
| ✅ | [C_UI.GetUIParent](#c_uigetuiparent) |  |  |
| ✅ | [C_UI.GetWorldFrame](#c_uigetworldframe) |  |  |
| ✅ | [C_UI.Reload](#c_uireload) |  |  |
| ✅ | [C_UI.ShouldUIParentAvoidNotch](#c_uishoulduiparentavoidnotch) |  |  |

### C_UI.DoesAnyDisplayHaveNotch

`C_UI.DoesAnyDisplayHaveNotch() → notchPresent: bool`

- Status: ✅ verified (function)
- Blizzard: True if any display attached has a notch. This does not mean the current view intersects the notch.
- Source: client docs `UIManagerDocumentation.lua`

### C_UI.GetTopLeftNotchSafeRegion

`C_UI.GetTopLeftNotchSafeRegion() → left: number, right: number, top: number, bottom: number`

- Status: ✅ verified (function)
- Blizzard: Region of screen left of screen notch. Zeros if no notch.
- Source: client docs `UIManagerDocumentation.lua`

### C_UI.GetTopRightNotchSafeRegion

`C_UI.GetTopRightNotchSafeRegion() → left: number, right: number, top: number, bottom: number`

- Status: ✅ verified (function)
- Blizzard: Region of screen right of screen notch. Zeros if no notch.
- Source: client docs `UIManagerDocumentation.lua`

### C_UI.GetUIParent

`C_UI.GetUIParent() → uiParent: SimpleFrame`

- Status: ✅ verified (function)
- Source: client docs `UIManagerDocumentation.lua`

### C_UI.GetWorldFrame

`C_UI.GetWorldFrame() → worldFrame: SimpleFrame`

- Status: ✅ verified (function)
- Source: client docs `UIManagerDocumentation.lua`

### C_UI.Reload

`C_UI.Reload()`

- Status: ✅ verified (function)
- Source: client docs `UIManagerDocumentation.lua`

### C_UI.ShouldUIParentAvoidNotch

`C_UI.ShouldUIParentAvoidNotch() → willAvoidNotch: bool`

- Status: ✅ verified (function)
- Blizzard: UIParent will shift down to avoid notch if true. This does not mean there is a notch.
- Source: client docs `UIManagerDocumentation.lua`

## Events

### NOTCHED_DISPLAY_MODE_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### UI_SCALE_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 2 times (0 in combat); argument kinds: ``
