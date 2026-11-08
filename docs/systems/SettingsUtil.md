# SettingsUtil

Namespace: `C_SettingsUtil`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_SettingsUtil.NotifySettingsLoaded](#c_settingsutilnotifysettingsloaded) |  |  |
| ✅ | [C_SettingsUtil.OpenSettingsPanel](#c_settingsutilopensettingspanel) |  |  |

### C_SettingsUtil.NotifySettingsLoaded

`C_SettingsUtil.NotifySettingsLoaded()`

- Status: ✅ verified (function)
- Source: client docs `SettingsUtilDocumentation.lua`

### C_SettingsUtil.OpenSettingsPanel

`C_SettingsUtil.OpenSettingsPanel(openToCategoryID: number?, scrollToElementName: stringView?)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SettingsUtilDocumentation.lua`

## Events

### SETTINGS_LOADED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: ``

### SETTINGS_PANEL_OPEN

- Status: ✅ verified
- Payload: `openToCategoryID: number?`, `scrollToElementName: stringView?`
- fires synchronously (Blizzard's docs)
