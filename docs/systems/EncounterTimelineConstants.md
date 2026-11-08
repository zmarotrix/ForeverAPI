# EncounterTimelineConstants

## Types

### EncounterTimelineEventConstants

- Constants — ❔ unverified
  - `ENCOUNTER_TIMELINE_INVALID_EVENT` = 0
  - `ENCOUNTER_TIMELINE_RESERVED_EVENT_COUNT` = 40

### EncounterTimelineEventSortDirection

- Enumeration — ❔ unverified
  - `Descending` = 0
  - `Ascending` = 1

### EncounterTimelineEventSource

- Enumeration — ❔ unverified
- Blizzard: Enumeration of all encounter timeline event sources.
  - `Encounter` = 0
  - `Script` = 1
  - `EditMode` = 2

### EncounterTimelineEventState

- Enumeration — ❔ unverified
- Blizzard: Enumeration of all encounter timeline event states.
  - `Active` = 0
  - `Paused` = 1
  - `Finished` = 2
  - `Canceled` = 3

### EncounterTimelineIconMasks

- Constants — ❔ unverified
  - `EncounterTimelineTankAlertIcons` = TankRole
  - `EncounterTimelineHealerAlertIcons` = HealerRole
  - `EncounterTimelineDamageAlertIcons` = DpsRole
  - `EncounterTimelineDeadlyIcons` = DeadlyEffect
  - `EncounterTimelineDispelIcons` = 124
  - `EncounterTimelineEnrageIcons` = EnrageEffect
  - `EncounterTimelineAllIcons` = 1023
  - `EncounterTimelineRoleIcons` = 896
  - `EncounterTimelineOtherIcons` = 127
  - `EncounterTimelineNoIcons` = 0

### EncounterTimelineIconSet

- Enumeration — ❔ unverified
  - `TankAlert` = 1
  - `HealerAlert` = 2
  - `DamageAlert` = 3
  - `Deadly` = 4
  - `Dispel` = 5
  - `Enrage` = 6

### EncounterTimelineTrack

- Enumeration — ❔ unverified
- Blizzard: Enumeration of all encounter timeline tracks., Tracks are not permitted to overlap (but may have a zero duration span), and are contiguously ordered from shortest maximum duration to longest.
  - `Queued` = 0
  - `Short` = 1
  - `Medium` = 2
  - `Long` = 3
  - `Indeterminate` = 4

### EncounterTimelineTrackType

- Enumeration — ❔ unverified
- Blizzard: Enumeration of all encounter timeline track types. Track types infer behavioral aspects of the track, for example whether or not we associate sort orders to events in the track.
  - `Hidden` = 0
  - `Sorted` = 1
  - `Linear` = 2

### EncounterTimelineViewType

- Enumeration — ❔ unverified
- Blizzard: Enumeration of view types for the timeline., View types control layout parameters for the timeline such as maximum track durations and event counts, and optimize event processing for expected display behaviors.
  - `None` = 0
  - `Timeline` = 1
  - `Bars` = 2
