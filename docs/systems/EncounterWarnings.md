# EncounterWarnings

Namespace: `C_EncounterWarnings`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_EncounterWarnings.GetColorForSeverity](#c_encounterwarningsgetcolorforseverity) |  |  |
| ❔ | [C_EncounterWarnings.GetEditModeWarningInfo](#c_encounterwarningsgeteditmodewarninginfo) |  |  |
| ❔ | [C_EncounterWarnings.GetPlayCustomSoundsWhenHidden](#c_encounterwarningsgetplaycustomsoundswhenhidden) |  |  |
| ❔ | [C_EncounterWarnings.GetSoundKitForSeverity](#c_encounterwarningsgetsoundkitforseverity) |  |  |
| ❔ | [C_EncounterWarnings.GetWarningsShown](#c_encounterwarningsgetwarningsshown) |  |  |
| ❔ | [C_EncounterWarnings.IsFeatureAvailable](#c_encounterwarningsisfeatureavailable) |  |  |
| ❔ | [C_EncounterWarnings.IsFeatureEnabled](#c_encounterwarningsisfeatureenabled) |  |  |
| ❔ | [C_EncounterWarnings.PlaySound](#c_encounterwarningsplaysound) |  |  |
| ❔ | [C_EncounterWarnings.SetPlayCustomSoundsWhenHidden](#c_encounterwarningssetplaycustomsoundswhenhidden) |  |  |
| ❔ | [C_EncounterWarnings.SetWarningsShown](#c_encounterwarningssetwarningsshown) |  |  |

### C_EncounterWarnings.GetColorForSeverity

`C_EncounterWarnings.GetColorForSeverity(severity: EncounterEventSeverity) → color: colorRGBA`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterWarningsDocumentation.lua`

### C_EncounterWarnings.GetEditModeWarningInfo

`C_EncounterWarnings.GetEditModeWarningInfo(severity: EncounterEventSeverity) → warningInfo: EncounterWarningInfo`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterWarningsDocumentation.lua`

### C_EncounterWarnings.GetPlayCustomSoundsWhenHidden

`C_EncounterWarnings.GetPlayCustomSoundsWhenHidden() → play: bool`

- Status: ❔ unverified
- Blizzard: Returns true if custom sound alerts are allowed to play for hidden warning messages.
- Source: client docs `EncounterWarningsDocumentation.lua`

### C_EncounterWarnings.GetSoundKitForSeverity

`C_EncounterWarnings.GetSoundKitForSeverity(severity: EncounterEventSeverity) → soundKitID: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterWarningsDocumentation.lua`

### C_EncounterWarnings.GetWarningsShown

`C_EncounterWarnings.GetWarningsShown() → shown: bool`

- Status: ❔ unverified
- Blizzard: Returns true if text messages for encounter events are allowed to be shown.
- Source: client docs `EncounterWarningsDocumentation.lua`

### C_EncounterWarnings.IsFeatureAvailable

`C_EncounterWarnings.IsFeatureAvailable() → isAvailable: bool`

- Status: ❔ unverified
- Source: client docs `EncounterWarningsDocumentation.lua`

### C_EncounterWarnings.IsFeatureEnabled

`C_EncounterWarnings.IsFeatureEnabled() → isAvailableAndEnabled: bool`

- Status: ❔ unverified
- Source: client docs `EncounterWarningsDocumentation.lua`

### C_EncounterWarnings.PlaySound

`C_EncounterWarnings.PlaySound(severity: EncounterEventSeverity) → soundHandle: number`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterWarningsDocumentation.lua`

### C_EncounterWarnings.SetPlayCustomSoundsWhenHidden

`C_EncounterWarnings.SetPlayCustomSoundsWhenHidden(play: bool)`

- Status: ❔ unverified
- Blizzard: Controls whether custom sound alerts for encounter events are allowed to play for warning messages that are hidden.
- `play`: If true, allow playing custom sound alerts. Note that sound alerts will not be played if the encounter warnings feature has been disabled.
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterWarningsDocumentation.lua`

### C_EncounterWarnings.SetWarningsShown

`C_EncounterWarnings.SetWarningsShown(shown: bool)`

- Status: ❔ unverified
- Blizzard: Controls whether text messages for encounter events are allowed to be shown.
- `shown`: If false, hides all warning messages in the default UI.
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterWarningsDocumentation.lua`

## Events

### ENCOUNTER_WARNING

- Status: ❔ unverified
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
