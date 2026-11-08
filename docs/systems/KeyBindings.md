# KeyBindings

Namespace: `C_KeyBindings`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_KeyBindings.ActivateBindingContext](#c_keybindingsactivatebindingcontext) |  |  |
| ✅ | [C_KeyBindings.DeactivateBindingContext](#c_keybindingsdeactivatebindingcontext) |  |  |
| ✅ | [C_KeyBindings.GetBindingByKey](#c_keybindingsgetbindingbykey) |  |  |
| ✅ | [C_KeyBindings.GetBindingContextForAction](#c_keybindingsgetbindingcontextforaction) |  |  |
| ✅ | [C_KeyBindings.GetBindingIndex](#c_keybindingsgetbindingindex) |  |  |
| ✅ | [C_KeyBindings.GetCustomBindingType](#c_keybindingsgetcustombindingtype) |  |  |
| ✅ | [C_KeyBindings.GetSearchTagsForAction](#c_keybindingsgetsearchtagsforaction) |  |  |
| ✅ | [C_KeyBindings.GetTurnStrafeStyle](#c_keybindingsgetturnstrafestyle) |  |  |
| ✅ | [C_KeyBindings.IsBindingContextActive](#c_keybindingsisbindingcontextactive) |  |  |
| ✅ | [C_KeyBindings.SetTurnStrafeStyle](#c_keybindingssetturnstrafestyle) |  |  |
| ✅ | [C_KeyBindings.UpdateTurnStrafeBindingsForCharacter](#c_keybindingsupdateturnstrafebindingsforcharacter) |  |  |

### C_KeyBindings.ActivateBindingContext

`C_KeyBindings.ActivateBindingContext(newContext: BindingContext)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `KeyBindingsDocumentation.lua`

### C_KeyBindings.DeactivateBindingContext

`C_KeyBindings.DeactivateBindingContext(context: BindingContext)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `KeyBindingsDocumentation.lua`

### C_KeyBindings.GetBindingByKey

`C_KeyBindings.GetBindingByKey(action: cstring, context: BindingContext?) → binding: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `KeyBindingsDocumentation.lua`

### C_KeyBindings.GetBindingContextForAction

`C_KeyBindings.GetBindingContextForAction(action: cstring) → context: BindingContext?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `KeyBindingsDocumentation.lua`

### C_KeyBindings.GetBindingIndex

`C_KeyBindings.GetBindingIndex(action: cstring) → bindingIndex: luaIndex?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `KeyBindingsDocumentation.lua`

### C_KeyBindings.GetCustomBindingType

`C_KeyBindings.GetCustomBindingType(bindingIndex: luaIndex) → customBindingType: CustomBindingType?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `KeyBindingsDocumentation.lua`

### C_KeyBindings.GetSearchTagsForAction

`C_KeyBindings.GetSearchTagsForAction(action: cstring) → searchTags: string[]?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `KeyBindingsDocumentation.lua`

### C_KeyBindings.GetTurnStrafeStyle

`C_KeyBindings.GetTurnStrafeStyle() → style: TurnStrafeStyle`

- Status: ✅ verified (function)
- Source: client docs `KeyBindingsDocumentation.lua`

### C_KeyBindings.IsBindingContextActive

`C_KeyBindings.IsBindingContextActive(context: BindingContext) → isActive: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `KeyBindingsDocumentation.lua`

### C_KeyBindings.SetTurnStrafeStyle

`C_KeyBindings.SetTurnStrafeStyle(style: TurnStrafeStyle)`

- Status: ✅ verified (function)
- Blizzard: Can only set to Modern or Legacy.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `KeyBindingsDocumentation.lua`

### C_KeyBindings.UpdateTurnStrafeBindingsForCharacter

`C_KeyBindings.UpdateTurnStrafeBindingsForCharacter()`

- Status: ✅ verified (function)
- Source: client docs `KeyBindingsDocumentation.lua`

## Events

### BINDINGS_LOADED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: ``

### MODIFIER_STATE_CHANGED

- Status: ✅ verified
- Payload: `key: cstring`, `down: number`
- fires synchronously (Blizzard's docs)
- Seen firing 6 times (5 in combat); argument kinds: `s,n`

### NOTIFY_TURN_STRAFE_CHANGE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### UPDATE_BINDINGS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 5 times (0 in combat); argument kinds: ``

## Types

### BindingContext

- Enumeration — ✅ verified
  - `None` = 0
  - `HousingEditor` = 1
  - `HousingEditorBasicDecorMode` = 2
  - `HousingEditorExpertDecorMode` = 3
  - `HousingEditorCustomizeMode` = 4
  - `HousingEditorCleanupMode` = 5
  - `HousingEditorLayoutMode` = 6
  - `HousingEditorBasicAndExpertDecorMode` = 7
  - `HousingEditorExteriorCustomizationMode` = 8
  - `GamepadModeInGameCore` = 9

### BindingSet

- Enumeration — ✅ verified
  - `Default` = 0
  - `Account` = 1
  - `Character` = 2
  - `Current` = 3

### CustomBindingType

- Enumeration — ✅ verified
  - `VoicePushToTalk` = 0

### InputCommandCallback

- CallbackType

### TurnStrafeStyle

- Enumeration — ✅ verified
  - `Modern` = 0
  - `Legacy` = 1
  - `Custom` = 2
