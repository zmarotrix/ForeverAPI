# ExternalEventURL

Namespace: `C_ExternalEventURL`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ExternalEventURL.CanShow](#c_externaleventurlcanshow) |  |  |
| ✅ | [C_ExternalEventURL.HasURL](#c_externaleventurlhasurl) |  |  |
| ✅ | [C_ExternalEventURL.IsNew](#c_externaleventurlisnew) |  |  |
| ✅ | [C_ExternalEventURL.LaunchURL](#c_externaleventurllaunchurl) |  |  |

### C_ExternalEventURL.CanShow

`C_ExternalEventURL.CanShow() → canShow: bool`

- Status: ✅ verified (function)
- Source: client docs `ExternalEventURLDocumentation.lua`

### C_ExternalEventURL.HasURL

`C_ExternalEventURL.HasURL() → hasURL: bool`

- Status: ✅ verified (function)
- Source: client docs `ExternalEventURLDocumentation.lua`

### C_ExternalEventURL.IsNew

`C_ExternalEventURL.IsNew() → isNew: bool`

- Status: ✅ verified (function)
- Source: client docs `ExternalEventURLDocumentation.lua`

### C_ExternalEventURL.LaunchURL

`C_ExternalEventURL.LaunchURL()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `ExternalEventURLDocumentation.lua`

## Events

### EXTERNAL_EVENT_LAUNCH_URL_RESULT

- Status: ✅ verified
- Payload: `result: bool`
- fires synchronously (Blizzard's docs)

### EXTERNAL_EVENT_URL_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
