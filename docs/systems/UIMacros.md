# UIMacros

Namespace: `C_Macro`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Macro.GetMacroName](#c_macrogetmacroname) | 1 value | 1 value |
| ✅ | [C_Macro.GetSelectedMacroIcon](#c_macrogetselectedmacroicon) | 1 value | 1 value |
| ✅ | [C_Macro.RunMacroText](#c_macrorunmacrotext) |  |  |
| ⛔ | [C_Macro.SetMacroExecuteLineCallback](#c_macrosetmacroexecutelinecallback) |  |  |

### C_Macro.GetMacroName

`C_Macro.GetMacroName(macroId: luaIndex) → name: cstring?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `string`
- Called in combat: returned 1 value: `string`
- Source: client docs `UIMacrosDocumentation.lua`

### C_Macro.GetSelectedMacroIcon

`C_Macro.GetSelectedMacroIcon(macroId: luaIndex) → textureNum: fileID`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `UIMacrosDocumentation.lua`

### C_Macro.RunMacroText

`C_Macro.RunMacroText(text: cstring, button: cstring)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UIMacrosDocumentation.lua`

### C_Macro.SetMacroExecuteLineCallback

`C_Macro.SetMacroExecuteLineCallback(cb: MacroExecuteLineCallback)`

- Status: ⛔ in Blizzard's docs, not in game
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UIMacrosDocumentation.lua`

## Events

### UPDATE_MACROS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 34 times (0 in combat); argument kinds: ``

## Types

### MacroExecuteLineCallback

- CallbackType
