# Glue

Namespace: `C_Glue`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Glue.IsFirstLoadThisSession](#c_glueisfirstloadthissession) | 1 value | 1 value |
| ✅ | [C_Glue.IsOnGlueScreen](#c_glueisongluescreen) | 1 value | 1 value |

### C_Glue.IsFirstLoadThisSession

`C_Glue.IsFirstLoadThisSession() → IsFirstLoadThisSession: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GlueDocumentation.lua`

### C_Glue.IsOnGlueScreen

`C_Glue.IsOnGlueScreen() → isOnGlueScreen: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GlueDocumentation.lua`

## Events

### ACCOUNT_CVARS_LOADED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
