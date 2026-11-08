# EncounterEventsShared

## Types

### EncounterEventColorTrigger

- Enumeration — ✅ verified
  - `TextWarning` = 0
  - `TimelineEvent` = 1
  - `TimelineEventHighlight` = 2

### EncounterEventInfo

- Structure
  - `encounterEventID`: number
  - `enabled`: bool
  - `spellID`: number
  - `iconFileID`: number
  - `severity`: EncounterEventSeverity
  - `icons`: EncounterEventIconmask

### EncounterEventSoundInfo

- Structure
  - `file`: FileAsset
  - `channel`: UISoundSubType
  - `volume`: number

### EncounterEventSoundTrigger

- Enumeration — ✅ verified
  - `OnTextWarningShown` = 0
  - `OnTimelineEventFinished` = 1
  - `OnTimelineEventHighlight` = 2
