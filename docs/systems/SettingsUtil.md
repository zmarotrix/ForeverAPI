# SettingsUtil

Namespace: `C_SettingsUtil`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_SettingsUtil.NotifySettingsLoaded](#c_settingsutilnotifysettingsloaded) |  |  |
| ❔ | [C_SettingsUtil.OpenSettingsPanel](#c_settingsutilopensettingspanel) |  |  |

### C_SettingsUtil.NotifySettingsLoaded

`C_SettingsUtil.NotifySettingsLoaded()`

- Status: ❔ unverified
- Source: client docs `SettingsUtilDocumentation.lua`

### C_SettingsUtil.OpenSettingsPanel

`C_SettingsUtil.OpenSettingsPanel(openToCategoryID: number?, scrollToElementName: stringView?)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SettingsUtilDocumentation.lua`

## Events

### SETTINGS_LOADED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SETTINGS_PANEL_OPEN

- Status: ❔ unverified
- Payload: `openToCategoryID: number?`, `scrollToElementName: stringView?`
- fires synchronously (Blizzard's docs)
