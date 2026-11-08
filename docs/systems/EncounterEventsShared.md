# EncounterEventsShared

## Types

### EncounterEventColorTrigger

- Enumeration — ❔ unverified
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

- Enumeration — ❔ unverified
  - `OnTextWarningShown` = 0
  - `OnTimelineEventFinished` = 1
  - `OnTimelineEventHighlight` = 2
