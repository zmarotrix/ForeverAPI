# InstanceEncounter

Namespace: `C_InstanceEncounter`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_InstanceEncounter.IsEncounterInProgress](#c_instanceencounterisencounterinprogress) |  |  |
| ❔ | [C_InstanceEncounter.IsEncounterLimitingResurrections](#c_instanceencounterisencounterlimitingresurrections) |  |  |
| ❔ | [C_InstanceEncounter.IsEncounterSuppressingRelease](#c_instanceencounterisencountersuppressingrelease) |  |  |
| ❔ | [C_InstanceEncounter.ShouldShowTimelineForEncounter](#c_instanceencountershouldshowtimelineforencounter) |  |  |

### C_InstanceEncounter.IsEncounterInProgress

`C_InstanceEncounter.IsEncounterInProgress() → isInProgress: bool`

- Status: ❔ unverified
- Source: client docs `InstanceEncounterDocumentation.lua`

### C_InstanceEncounter.IsEncounterLimitingResurrections

`C_InstanceEncounter.IsEncounterLimitingResurrections() → isLimitingResurrections: bool`

- Status: ❔ unverified
- Source: client docs `InstanceEncounterDocumentation.lua`

### C_InstanceEncounter.IsEncounterSuppressingRelease

`C_InstanceEncounter.IsEncounterSuppressingRelease() → isSuppressingRelease: bool`

- Status: ❔ unverified
- Source: client docs `InstanceEncounterDocumentation.lua`

### C_InstanceEncounter.ShouldShowTimelineForEncounter

`C_InstanceEncounter.ShouldShowTimelineForEncounter() → shouldShow: bool`

- Status: ❔ unverified
- Source: client docs `InstanceEncounterDocumentation.lua`

## Events

### ENCOUNTER_STATE_CHANGED

- Status: ❔ unverified
- Payload: `isInProgress: bool`
- Blizzard: Signaled when the in-progress state of an encounter changes.
- CallbackEvent (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### INSTANCE_ENCOUNTER_ADD_TIMER

- Status: ❔ unverified
- Payload: `timeRemaining: number`
- fires synchronously (Blizzard's docs)

### INSTANCE_ENCOUNTER_ENGAGE_UNIT

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### INSTANCE_ENCOUNTER_OBJECTIVE_COMPLETE

- Status: ❔ unverified
- Payload: `objectiveID: number`
- fires synchronously (Blizzard's docs)

### INSTANCE_ENCOUNTER_OBJECTIVE_START

- Status: ❔ unverified
- Payload: `objectiveID: number`, `objectiveProgress: number`
- fires synchronously (Blizzard's docs)

### INSTANCE_ENCOUNTER_OBJECTIVE_UPDATE

- Status: ❔ unverified
- Payload: `objectiveID: number`, `objectiveProgress: number`
- fires synchronously (Blizzard's docs)
