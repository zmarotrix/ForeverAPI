# ConfigurationWarnings

Namespace: `C_ConfigurationWarnings`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ⛔ | [C_ConfigurationWarnings.GetConfigurationWarningSeen](#c_configurationwarningsgetconfigurationwarningseen) |  |  |
| ⛔ | [C_ConfigurationWarnings.GetConfigurationWarningString](#c_configurationwarningsgetconfigurationwarningstring) |  |  |
| ⛔ | [C_ConfigurationWarnings.GetConfigurationWarnings](#c_configurationwarningsgetconfigurationwarnings) | missing | missing |
| ⛔ | [C_ConfigurationWarnings.SetConfigurationWarningSeen](#c_configurationwarningssetconfigurationwarningseen) |  |  |

### C_ConfigurationWarnings.GetConfigurationWarningSeen

`C_ConfigurationWarnings.GetConfigurationWarningSeen(configurationWarning: ConfigurationWarning) → hasSeenConfigurationWarning: bool`

- Status: ⛔ in Blizzard's docs, not in game
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ConfigurationWarningsDocumentation.lua`

### C_ConfigurationWarnings.GetConfigurationWarningString

`C_ConfigurationWarnings.GetConfigurationWarningString(configurationWarning: ConfigurationWarning) → configurationWarningString: string`

- Status: ⛔ in Blizzard's docs, not in game
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ConfigurationWarningsDocumentation.lua`

### C_ConfigurationWarnings.GetConfigurationWarnings

`C_ConfigurationWarnings.GetConfigurationWarnings(includeSeenWarnings: bool = False) → configurationWarnings: ConfigurationWarning[]`

- Status: ⛔ in Blizzard's docs, not in game
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: missing at call time
- Called in combat: missing at call time
- Source: client docs `ConfigurationWarningsDocumentation.lua`

### C_ConfigurationWarnings.SetConfigurationWarningSeen

`C_ConfigurationWarnings.SetConfigurationWarningSeen(configurationWarning: ConfigurationWarning)`

- Status: ⛔ in Blizzard's docs, not in game
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ConfigurationWarningsDocumentation.lua`
