# CVarScripts

Namespace: `C_CVar`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_CVar.AreCVarsLoaded](#c_cvararecvarsloaded) |  |  |
| ✅ | [C_CVar.GetCVar](#c_cvargetcvar) |  |  |
| ✅ | [C_CVar.GetCVarBitfield](#c_cvargetcvarbitfield) |  |  |
| ✅ | [C_CVar.GetCVarBool](#c_cvargetcvarbool) |  |  |
| ✅ | [C_CVar.GetCVarDefault](#c_cvargetcvardefault) |  |  |
| ✅ | [C_CVar.GetCVarInfo](#c_cvargetcvarinfo) |  |  |
| ✅ | [C_CVar.RegisterCVar](#c_cvarregistercvar) |  |  |
| ✅ | [C_CVar.RemoveTempCVar](#c_cvarremovetempcvar) |  |  |
| ✅ | [C_CVar.ResetTestCVars](#c_cvarresettestcvars) |  |  |
| ✅ | [C_CVar.SetCVar](#c_cvarsetcvar) |  |  |
| ✅ | [C_CVar.SetCVarBitfield](#c_cvarsetcvarbitfield) |  |  |
| ✅ | [C_CVar.SetTempCVar](#c_cvarsettempcvar) |  |  |

### C_CVar.AreCVarsLoaded

`C_CVar.AreCVarsLoaded() → loaded: bool`

- Status: ✅ verified (function)
- Source: client docs `CVarDocumentation.lua`

### C_CVar.GetCVar

`C_CVar.GetCVar(name: cstring) → value: string?`

- Status: ✅ verified (function)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `CVarDocumentation.lua`

### C_CVar.GetCVarBitfield

`C_CVar.GetCVarBitfield(name: cstring, index: luaIndex) → value: bool?`

- Status: ✅ verified (function)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `CVarDocumentation.lua`

### C_CVar.GetCVarBool

`C_CVar.GetCVarBool(name: cstring) → value: bool?`

- Status: ✅ verified (function)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `CVarDocumentation.lua`

### C_CVar.GetCVarDefault

`C_CVar.GetCVarDefault(name: cstring) → defaultValue: string?`

- Status: ✅ verified (function)
- RequiresValidAndPublicCVar (Blizzard's docs; not checked in game)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `CVarDocumentation.lua`

### C_CVar.GetCVarInfo

`C_CVar.GetCVarInfo(name: cstring) → value: cstring, defaultValue: cstring, isStoredServerAccount: bool, isStoredServerCharacter: bool, isLockedFromUser: bool, isSecure: bool, isReadOnly: bool`

- Status: ✅ verified (function)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `CVarDocumentation.lua`

### C_CVar.RegisterCVar

`C_CVar.RegisterCVar(name: cstring, value: cstring?)`

- Status: ✅ verified (function)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `CVarDocumentation.lua`

### C_CVar.RemoveTempCVar

`C_CVar.RemoveTempCVar(name: cstring)`

- Status: ✅ verified (function)
- RequiresNonReadOnlyCVar (Blizzard's docs; not checked in game)
- RequiresNonSecureCVar (Blizzard's docs; not checked in game)
- RequiresValidAndPublicCVar (Blizzard's docs; not checked in game)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `CVarDocumentation.lua`

### C_CVar.ResetTestCVars

`C_CVar.ResetTestCVars()`

- Status: ✅ verified (function)
- Source: client docs `CVarDocumentation.lua`

### C_CVar.SetCVar

`C_CVar.SetCVar(name: cstring, value: cstring?) → success: bool`

- Status: ✅ verified (function)
- RequiresNonReadOnlyCVar (Blizzard's docs; not checked in game)
- RequiresNonSecureCVar (Blizzard's docs; not checked in game)
- RequiresValidAndPublicCVar (Blizzard's docs; not checked in game)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `CVarDocumentation.lua`

### C_CVar.SetCVarBitfield

`C_CVar.SetCVarBitfield(name: cstring, index: luaIndex, value: bool) → success: bool`

- Status: ✅ verified (function)
- RequiresIndexInRange (Blizzard's docs; not checked in game)
- RequiresNonReadOnlyCVar (Blizzard's docs; not checked in game)
- RequiresNonSecureCVar (Blizzard's docs; not checked in game)
- RequiresValidAndPublicCVar (Blizzard's docs; not checked in game)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `CVarDocumentation.lua`

### C_CVar.SetTempCVar

`C_CVar.SetTempCVar(name: cstring, value: cstring?)`

- Status: ✅ verified (function)
- RequiresNonReadOnlyCVar (Blizzard's docs; not checked in game)
- RequiresNonSecureCVar (Blizzard's docs; not checked in game)
- RequiresValidAndPublicCVar (Blizzard's docs; not checked in game)
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `CVarDocumentation.lua`

## Types

### CVarInfo

- Structure
  - `value`: cstring
  - `defaultValue`: cstring
  - `isStoredServerAccount`: bool
  - `isStoredServerCharacter`: bool
  - `isLockedFromUser`: bool
  - `isSecure`: bool
  - `isReadOnly`: bool
