# TTSSettings

Namespace: `C_TTSSettings`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_TTSSettings.GetChannelEnabled](#c_ttssettingsgetchannelenabled) |  |  |
| ❔ | [C_TTSSettings.GetCharacterSettingsSaved](#c_ttssettingsgetcharactersettingssaved) |  |  |
| ❔ | [C_TTSSettings.GetChatTypeEnabled](#c_ttssettingsgetchattypeenabled) |  |  |
| ❔ | [C_TTSSettings.GetSetting](#c_ttssettingsgetsetting) |  |  |
| ❔ | [C_TTSSettings.GetSpeechRate](#c_ttssettingsgetspeechrate) |  |  |
| ❔ | [C_TTSSettings.GetSpeechVolume](#c_ttssettingsgetspeechvolume) |  |  |
| ❔ | [C_TTSSettings.GetVoiceOptionID](#c_ttssettingsgetvoiceoptionid) |  |  |
| ❔ | [C_TTSSettings.GetVoiceOptionName](#c_ttssettingsgetvoiceoptionname) |  |  |
| ❔ | [C_TTSSettings.MarkCharacterSettingsSaved](#c_ttssettingsmarkcharactersettingssaved) |  |  |
| ❔ | [C_TTSSettings.SetChannelEnabled](#c_ttssettingssetchannelenabled) |  |  |
| ❔ | [C_TTSSettings.SetChannelKeyEnabled](#c_ttssettingssetchannelkeyenabled) |  |  |
| ❔ | [C_TTSSettings.SetChatTypeEnabled](#c_ttssettingssetchattypeenabled) |  |  |
| ❔ | [C_TTSSettings.SetDefaultSettings](#c_ttssettingssetdefaultsettings) |  |  |
| ❔ | [C_TTSSettings.SetSetting](#c_ttssettingssetsetting) |  |  |
| ❔ | [C_TTSSettings.SetSpeechRate](#c_ttssettingssetspeechrate) |  |  |
| ❔ | [C_TTSSettings.SetSpeechVolume](#c_ttssettingssetspeechvolume) |  |  |
| ❔ | [C_TTSSettings.SetVoiceOption](#c_ttssettingssetvoiceoption) |  |  |
| ❔ | [C_TTSSettings.SetVoiceOptionName](#c_ttssettingssetvoiceoptionname) |  |  |
| ❔ | [C_TTSSettings.ShouldOverrideMessage](#c_ttssettingsshouldoverridemessage) |  |  |

### C_TTSSettings.GetChannelEnabled

`C_TTSSettings.GetChannelEnabled(channelInfo: ChatChannelInfo) → enabled: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TTSSettingsDocumentation.lua`

### C_TTSSettings.GetCharacterSettingsSaved

`C_TTSSettings.GetCharacterSettingsSaved() → settingsBeenSaved: bool`

- Status: ❔ unverified
- Source: client docs `TTSSettingsDocumentation.lua`

### C_TTSSettings.GetChatTypeEnabled

`C_TTSSettings.GetChatTypeEnabled(chatName: cstring) → enabled: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TTSSettingsDocumentation.lua`

### C_TTSSettings.GetSetting

`C_TTSSettings.GetSetting(setting: TtsBoolSetting) → enabled: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TTSSettingsDocumentation.lua`

### C_TTSSettings.GetSpeechRate

`C_TTSSettings.GetSpeechRate() → rate: number`

- Status: ❔ unverified
- Source: client docs `TTSSettingsDocumentation.lua`

### C_TTSSettings.GetSpeechVolume

`C_TTSSettings.GetSpeechVolume() → volume: number`

- Status: ❔ unverified
- Source: client docs `TTSSettingsDocumentation.lua`

### C_TTSSettings.GetVoiceOptionID

`C_TTSSettings.GetVoiceOptionID(voiceType: TtsVoiceType) → voiceID: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TTSSettingsDocumentation.lua`

### C_TTSSettings.GetVoiceOptionName

`C_TTSSettings.GetVoiceOptionName(voiceType: TtsVoiceType) → voiceName: cstring`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TTSSettingsDocumentation.lua`

### C_TTSSettings.MarkCharacterSettingsSaved

`C_TTSSettings.MarkCharacterSettingsSaved()`

- Status: ❔ unverified
- Source: client docs `TTSSettingsDocumentation.lua`

### C_TTSSettings.SetChannelEnabled

`C_TTSSettings.SetChannelEnabled(channelInfo: ChatChannelInfo, newVal: bool = False)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TTSSettingsDocumentation.lua`

### C_TTSSettings.SetChannelKeyEnabled

`C_TTSSettings.SetChannelKeyEnabled(channelKey: string, newVal: bool = False)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TTSSettingsDocumentation.lua`

### C_TTSSettings.SetChatTypeEnabled

`C_TTSSettings.SetChatTypeEnabled(chatName: cstring, newVal: bool = False)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TTSSettingsDocumentation.lua`

### C_TTSSettings.SetDefaultSettings

`C_TTSSettings.SetDefaultSettings()`

- Status: ❔ unverified
- Source: client docs `TTSSettingsDocumentation.lua`

### C_TTSSettings.SetSetting

`C_TTSSettings.SetSetting(setting: TtsBoolSetting, newVal: bool = False)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TTSSettingsDocumentation.lua`

### C_TTSSettings.SetSpeechRate

`C_TTSSettings.SetSpeechRate(newVal: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TTSSettingsDocumentation.lua`

### C_TTSSettings.SetSpeechVolume

`C_TTSSettings.SetSpeechVolume(newVal: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TTSSettingsDocumentation.lua`

### C_TTSSettings.SetVoiceOption

`C_TTSSettings.SetVoiceOption(voiceType: TtsVoiceType, voiceID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TTSSettingsDocumentation.lua`

### C_TTSSettings.SetVoiceOptionName

`C_TTSSettings.SetVoiceOptionName(voiceType: TtsVoiceType, voiceName: string)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TTSSettingsDocumentation.lua`

### C_TTSSettings.ShouldOverrideMessage

`C_TTSSettings.ShouldOverrideMessage(language: number, messageText: string) → overrideMessage: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TTSSettingsDocumentation.lua`
