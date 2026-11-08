# EncounterEvents

Namespace: `C_EncounterEvents`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_EncounterEvents.GetEventColor](#c_encountereventsgeteventcolor) |  |  |
| ✅ | [C_EncounterEvents.GetEventInfo](#c_encountereventsgeteventinfo) |  |  |
| ✅ | [C_EncounterEvents.GetEventList](#c_encountereventsgeteventlist) |  |  |
| ✅ | [C_EncounterEvents.GetEventSound](#c_encountereventsgeteventsound) |  |  |
| ✅ | [C_EncounterEvents.HasEventInfo](#c_encountereventshaseventinfo) |  |  |
| ✅ | [C_EncounterEvents.PlayEventSound](#c_encountereventsplayeventsound) |  |  |
| ✅ | [C_EncounterEvents.SetEventColor](#c_encountereventsseteventcolor) |  |  |
| ✅ | [C_EncounterEvents.SetEventSound](#c_encountereventsseteventsound) |  |  |

### C_EncounterEvents.GetEventColor

`C_EncounterEvents.GetEventColor(encounterEventID: number, trigger: EncounterEventColorTrigger) → color: colorRGBA?`

- Status: ✅ verified (function)
- Blizzard: Returns any custom color override applied for an encounter event.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterEventsDocumentation.lua`

### C_EncounterEvents.GetEventInfo

`C_EncounterEvents.GetEventInfo(encounterEventID: number) → encounterEventInfo: EncounterEventInfo`

- Status: ✅ verified (function)
- Blizzard: Returns information about an encounter event.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterEventsDocumentation.lua`

### C_EncounterEvents.GetEventList

`C_EncounterEvents.GetEventList() → encounterEventIDs: number[]`

- Status: ✅ verified (function)
- Blizzard: Returns a list of all encounter event IDs.
- Source: client docs `EncounterEventsDocumentation.lua`

### C_EncounterEvents.GetEventSound

`C_EncounterEvents.GetEventSound(encounterEventID: number, trigger: EncounterEventSoundTrigger) → sound: EncounterEventSoundInfo`

- Status: ✅ verified (function)
- Blizzard: Returns information on a custom sound file to be played when an encounter event trigger occurs.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterEventsDocumentation.lua`

### C_EncounterEvents.HasEventInfo

`C_EncounterEvents.HasEventInfo(encounterEventID: number) → exists: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if an encounter event record with a specified ID exists.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterEventsDocumentation.lua`

### C_EncounterEvents.PlayEventSound

`C_EncounterEvents.PlayEventSound(encounterEventID: number, trigger: EncounterEventSoundTrigger) → handle: SoundHandle`

- Status: ✅ verified (function)
- Blizzard: Plays any registered custom sound file for a given encounter event trigger.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncounterEventsDocumentation.lua`

### C_EncounterEvents.SetEventColor

`C_EncounterEvents.SetEventColor(encounterEventID: number, trigger: EncounterEventColorTrigger, color: colorRGBA?)`

- Status: ✅ verified (function)
- Blizzard: Sets a custom color override for an encounter event. This can be used to colorize text or timer bars individually.
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterEventsDocumentation.lua`

### C_EncounterEvents.SetEventSound

`C_EncounterEvents.SetEventSound(encounterEventID: number, trigger: EncounterEventSoundTrigger, sound: EncounterEventSoundInfo?)`

- Status: ✅ verified (function)
- Blizzard: Sets a custom sound file to be played when an encounter event trigger occurs.
- secret arguments: NotAllowed (Blizzard's docs; not checked in game)
- Source: client docs `EncounterEventsDocumentation.lua`
