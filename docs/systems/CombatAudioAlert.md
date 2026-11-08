# CombatAudioAlert

Namespace: `C_CombatAudioAlert`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_CombatAudioAlert.AddToKnownTargetingList](#c_combataudioalertaddtoknowntargetinglist) |  |  |
| ❔ | [C_CombatAudioAlert.GetCategoryVoice](#c_combataudioalertgetcategoryvoice) |  |  |
| ❔ | [C_CombatAudioAlert.GetCategoryVolume](#c_combataudioalertgetcategoryvolume) |  |  |
| ❔ | [C_CombatAudioAlert.GetFormatSetting](#c_combataudioalertgetformatsetting) |  |  |
| ❔ | [C_CombatAudioAlert.GetSpeakerSpeed](#c_combataudioalertgetspeakerspeed) |  |  |
| ❔ | [C_CombatAudioAlert.GetSpecSetting](#c_combataudioalertgetspecsetting) |  |  |
| ❔ | [C_CombatAudioAlert.GetThrottle](#c_combataudioalertgetthrottle) |  |  |
| ❔ | [C_CombatAudioAlert.IsEnabled](#c_combataudioalertisenabled) |  |  |
| ❔ | [C_CombatAudioAlert.RemoveFromKnownTargetingList](#c_combataudioalertremovefromknowntargetinglist) |  |  |
| ❔ | [C_CombatAudioAlert.SetCategoryVoice](#c_combataudioalertsetcategoryvoice) |  |  |
| ❔ | [C_CombatAudioAlert.SetCategoryVolume](#c_combataudioalertsetcategoryvolume) |  |  |
| ❔ | [C_CombatAudioAlert.SetFormatSetting](#c_combataudioalertsetformatsetting) |  |  |
| ❔ | [C_CombatAudioAlert.SetSpeakerSpeed](#c_combataudioalertsetspeakerspeed) |  |  |
| ❔ | [C_CombatAudioAlert.SetSpecSetting](#c_combataudioalertsetspecsetting) |  |  |
| ❔ | [C_CombatAudioAlert.SetThrottle](#c_combataudioalertsetthrottle) |  |  |
| ❔ | [C_CombatAudioAlert.SpeakText](#c_combataudioalertspeaktext) |  |  |

### C_CombatAudioAlert.AddToKnownTargetingList

`C_CombatAudioAlert.AddToKnownTargetingList(unit: UnitToken) → added: bool`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.GetCategoryVoice

`C_CombatAudioAlert.GetCategoryVoice(category: CombatAudioAlertCategory) → voice: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.GetCategoryVolume

`C_CombatAudioAlert.GetCategoryVolume(category: CombatAudioAlertCategory) → volume: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.GetFormatSetting

`C_CombatAudioAlert.GetFormatSetting(unit: CombatAudioAlertUnit, alertType: CombatAudioAlertType) → formatVal: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.GetSpeakerSpeed

`C_CombatAudioAlert.GetSpeakerSpeed() → speed: number`

- Status: ❔ unverified
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.GetSpecSetting

`C_CombatAudioAlert.GetSpecSetting(setting: CombatAudioAlertSpecSetting) → value: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.GetThrottle

`C_CombatAudioAlert.GetThrottle(throttleType: CombatAudioAlertThrottle) → throttle: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.IsEnabled

`C_CombatAudioAlert.IsEnabled() → isEnabled: bool`

- Status: ❔ unverified
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.RemoveFromKnownTargetingList

`C_CombatAudioAlert.RemoveFromKnownTargetingList(unit: UnitToken) → removed: bool`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.SetCategoryVoice

`C_CombatAudioAlert.SetCategoryVoice(category: CombatAudioAlertCategory, newVal: number) → success: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.SetCategoryVolume

`C_CombatAudioAlert.SetCategoryVolume(category: CombatAudioAlertCategory, newVal: number) → success: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.SetFormatSetting

`C_CombatAudioAlert.SetFormatSetting(unit: CombatAudioAlertUnit, alertType: CombatAudioAlertType, newVal: number) → success: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.SetSpeakerSpeed

`C_CombatAudioAlert.SetSpeakerSpeed(newVal: number) → success: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.SetSpecSetting

`C_CombatAudioAlert.SetSpecSetting(setting: CombatAudioAlertSpecSetting, newVal: number) → success: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.SetThrottle

`C_CombatAudioAlert.SetThrottle(throttleType: CombatAudioAlertThrottle, newVal: number) → success: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.SpeakText

`C_CombatAudioAlert.SpeakText(text: string, category: CombatAudioAlertCategory, allowOverlap: bool = True) → utteranceID: number`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`
