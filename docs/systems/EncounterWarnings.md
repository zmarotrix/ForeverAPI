# EncounterWarnings

Namespace: `C_EncounterWarnings`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_EncounterWarnings.GetColorForSeverity](#c_encounterwarningsgetcolorforseverity) | 1 value | 1 value |
| ✅ | [C_EncounterWarnings.GetEditModeWarningInfo](#c_encounterwarningsgeteditmodewarninginfo) | 1 value | 1 value |
| ✅ | [C_EncounterWarnings.GetPlayCustomSoundsWhenHidden](#c_encounterwarningsgetplaycustomsoundswhenhidden) | 1 value | 1 value |
| ✅ | [C_EncounterWarnings.GetSoundKitForSeverity](#c_encounterwarningsgetsoundkitforseverity) | 1 value | 1 value |
| ✅ | [C_EncounterWarnings.GetWarningsShown](#c_encounterwarningsgetwarningsshown) | 1 value | 1 value |
| ✅ | [C_EncounterWarnings.IsFeatureAvailable](#c_encounterwarningsisfeatureavailable) | 1 value | 1 value |
| ✅ | [C_EncounterWarnings.IsFeatureEnabled](#c_encounterwarningsisfeatureenabled) | 1 value | 1 value |
| ✅ | [C_EncounterWarnings.PlaySound](#c_encounterwarningsplaysound) |  |  |
| ✅ | [C_EncounterWarnings.SetPlayCustomSoundsWhenHidden](#c_encounterwarningssetplaycustomsoundswhenhidden) |  |  |
| ✅ | [C_EncounterWarnings.SetWarningsShown](#c_encounterwarningssetwarningsshown) |  |  |

### C_EncounterWarnings.GetColorForSeverity

`C_EncounterWarnings.GetColorForSeverity(severity: EncounterEventSeverity) → color: colorRGBA`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `table{GenerateHexColor=function,GenerateHexColorMarkup=function,GenerateHexColorNoAlpha=function,GetHSL=function,GetRGB=function,GetRGBA=function,GetRGBAAsBytes=function,GetRGBAsBytes=function,IsEqualTo=function,IsRGBEqualTo=function,OnLoad=function,SetRGB=function,SetRGBA=function,WrapTextInColorCode=function,a=number,b=number,g=number,r=number}`
- Called in combat: returned 1 value: `table{GenerateHexColor=function,GenerateHexColorMarkup=function,GenerateHexColorNoAlpha=function,GetHSL=function,GetRGB=function,GetRGBA=function,GetRGBAAsBytes=function,GetRGBAsBytes=function,IsEqualTo=function,IsRGBEqualTo=function,OnLoad=function,SetRGB=function,SetRGBA=function,WrapTextInColorCode=function,a=number,b=number,g=number,r=number}`
- Source: client docs `EncounterWarningsDocumentation.lua`

### C_EncounterWarnings.GetEditModeWarningInfo

`C_EncounterWarnings.GetEditModeWarningInfo(severity: EncounterEventSeverity) → warningInfo: EncounterWarningInfo`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `table{casterName=secret,color=table,duration=number,iconFileID=secret,isDeadly=secret,severity=number,shouldPlaySound=boolean,shouldShowChatMessage=boolean,shouldShowWarning=boolean,targetName=secret,text=secret,tooltipSpellID=secret}`
- Called in combat: returned 1 value: `table{casterName=secret,color=table,duration=number,iconFileID=secret,isDeadly=secret,severity=number,shouldPlaySound=boolean,shouldShowChatMessage=boolean,shouldShowWarning=boolean,targetName=secret,text=secret,tooltipSpellID=secret}`
- Source: client docs `EncounterWarningsDocumentation.lua`

### C_EncounterWarnings.GetPlayCustomSoundsWhenHidden

`C_EncounterWarnings.GetPlayCustomSoundsWhenHidden() → play: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if custom sound alerts are allowed to play for hidden warning messages.
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `EncounterWarningsDocumentation.lua`

### C_EncounterWarnings.GetSoundKitForSeverity

`C_EncounterWarnings.GetSoundKitForSeverity(severity: EncounterEventSeverity) → soundKitID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `EncounterWarningsDocumentation.lua`

### C_EncounterWarnings.GetWarningsShown

`C_EncounterWarnings.GetWarningsShown() → shown: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if text messages for encounter events are allowed to be shown.
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `EncounterWarningsDocumentation.lua`

### C_EncounterWarnings.IsFeatureAvailable

`C_EncounterWarnings.IsFeatureAvailable() → isAvailable: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `EncounterWarningsDocumentation.lua`

### C_EncounterWarnings.IsFeatureEnabled

`C_EncounterWarnings.IsFeatureEnabled() → isAvailableAndEnabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `EncounterWarningsDocumentation.lua`

### C_EncounterWarnings.PlaySound

`C_EncounterWarnings.PlaySound(severity: EncounterEventSeverity) → soundHandle: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterWarningsDocumentation.lua`

### C_EncounterWarnings.SetPlayCustomSoundsWhenHidden

`C_EncounterWarnings.SetPlayCustomSoundsWhenHidden(play: bool)`

- Status: ✅ verified (function)
- Blizzard: Controls whether custom sound alerts for encounter events are allowed to play for warning messages that are hidden.
- `play`: If true, allow playing custom sound alerts. Note that sound alerts will not be played if the encounter warnings feature has been disabled.
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterWarningsDocumentation.lua`

### C_EncounterWarnings.SetWarningsShown

`C_EncounterWarnings.SetWarningsShown(shown: bool)`

- Status: ✅ verified (function)
- Blizzard: Controls whether text messages for encounter events are allowed to be shown.
- `shown`: If false, hides all warning messages in the default UI.
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterWarningsDocumentation.lua`

## Events

### ENCOUNTER_WARNING

- Status: ✅ verified
- Payload: `encounterWarningInfo: EncounterWarningInfo`
- fires synchronously (Blizzard's docs)

## Types

### EncounterWarningInfo

- Structure
  - `text`: cstring
  - `casterGUID`: WOWGUID
  - `casterName`: cstring
  - `targetGUID`: WOWGUID
  - `targetName`: cstring
  - `iconFileID`: number
  - `tooltipSpellID`: number
  - `isDeadly`: bool
  - `color`: colorRGBA
  - `duration`: Seconds
  - `severity`: EncounterEventSeverity
  - `shouldPlaySound`: bool
  - `shouldShowChatMessage`: bool
  - `shouldShowWarning`: bool
