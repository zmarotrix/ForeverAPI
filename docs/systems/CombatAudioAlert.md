# CombatAudioAlert

Namespace: `C_CombatAudioAlert`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_CombatAudioAlert.AddToKnownTargetingList](#c_combataudioalertaddtoknowntargetinglist) |  |  |
| ✅ | [C_CombatAudioAlert.GetCategoryVoice](#c_combataudioalertgetcategoryvoice) | 1 value | 1 value |
| ✅ | [C_CombatAudioAlert.GetCategoryVolume](#c_combataudioalertgetcategoryvolume) | 1 value | 1 value |
| ✅ | [C_CombatAudioAlert.GetFormatSetting](#c_combataudioalertgetformatsetting) | 1 value | 1 value |
| ✅ | [C_CombatAudioAlert.GetSpeakerSpeed](#c_combataudioalertgetspeakerspeed) | 1 value | 1 value |
| ✅ | [C_CombatAudioAlert.GetSpecSetting](#c_combataudioalertgetspecsetting) | 1 value | 1 value |
| ✅ | [C_CombatAudioAlert.GetThrottle](#c_combataudioalertgetthrottle) | 1 value | 1 value |
| ✅ | [C_CombatAudioAlert.IsEnabled](#c_combataudioalertisenabled) | 1 value | 1 value |
| ✅ | [C_CombatAudioAlert.RemoveFromKnownTargetingList](#c_combataudioalertremovefromknowntargetinglist) |  |  |
| ✅ | [C_CombatAudioAlert.SetCategoryVoice](#c_combataudioalertsetcategoryvoice) |  |  |
| ✅ | [C_CombatAudioAlert.SetCategoryVolume](#c_combataudioalertsetcategoryvolume) |  |  |
| ✅ | [C_CombatAudioAlert.SetFormatSetting](#c_combataudioalertsetformatsetting) |  |  |
| ✅ | [C_CombatAudioAlert.SetSpeakerSpeed](#c_combataudioalertsetspeakerspeed) |  |  |
| ✅ | [C_CombatAudioAlert.SetSpecSetting](#c_combataudioalertsetspecsetting) |  |  |
| ✅ | [C_CombatAudioAlert.SetThrottle](#c_combataudioalertsetthrottle) |  |  |
| ✅ | [C_CombatAudioAlert.SpeakText](#c_combataudioalertspeaktext) |  |  |

### C_CombatAudioAlert.AddToKnownTargetingList

`C_CombatAudioAlert.AddToKnownTargetingList(unit: UnitToken) → added: bool`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.GetCategoryVoice

`C_CombatAudioAlert.GetCategoryVoice(category: CombatAudioAlertCategory) → voice: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.GetCategoryVolume

`C_CombatAudioAlert.GetCategoryVolume(category: CombatAudioAlertCategory) → volume: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.GetFormatSetting

`C_CombatAudioAlert.GetFormatSetting(unit: CombatAudioAlertUnit, alertType: CombatAudioAlertType) → formatVal: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `unit,n:0`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.GetSpeakerSpeed

`C_CombatAudioAlert.GetSpeakerSpeed() → speed: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.GetSpecSetting

`C_CombatAudioAlert.GetSpecSetting(setting: CombatAudioAlertSpecSetting) → value: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.GetThrottle

`C_CombatAudioAlert.GetThrottle(throttleType: CombatAudioAlertThrottle) → throttle: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.IsEnabled

`C_CombatAudioAlert.IsEnabled() → isEnabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.RemoveFromKnownTargetingList

`C_CombatAudioAlert.RemoveFromKnownTargetingList(unit: UnitToken) → removed: bool`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.SetCategoryVoice

`C_CombatAudioAlert.SetCategoryVoice(category: CombatAudioAlertCategory, newVal: number) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.SetCategoryVolume

`C_CombatAudioAlert.SetCategoryVolume(category: CombatAudioAlertCategory, newVal: number) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.SetFormatSetting

`C_CombatAudioAlert.SetFormatSetting(unit: CombatAudioAlertUnit, alertType: CombatAudioAlertType, newVal: number) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.SetSpeakerSpeed

`C_CombatAudioAlert.SetSpeakerSpeed(newVal: number) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.SetSpecSetting

`C_CombatAudioAlert.SetSpecSetting(setting: CombatAudioAlertSpecSetting, newVal: number) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.SetThrottle

`C_CombatAudioAlert.SetThrottle(throttleType: CombatAudioAlertThrottle, newVal: number) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`

### C_CombatAudioAlert.SpeakText

`C_CombatAudioAlert.SpeakText(text: string, category: CombatAudioAlertCategory, allowOverlap: bool = True) → utteranceID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CombatAudioAlertDocumentation.lua`
