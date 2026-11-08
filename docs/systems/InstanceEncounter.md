# InstanceEncounter

Namespace: `C_InstanceEncounter`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_InstanceEncounter.IsEncounterInProgress](#c_instanceencounterisencounterinprogress) | 1 value | 1 value |
| ✅ | [C_InstanceEncounter.IsEncounterLimitingResurrections](#c_instanceencounterisencounterlimitingresurrections) | 1 value | 1 value |
| ✅ | [C_InstanceEncounter.IsEncounterSuppressingRelease](#c_instanceencounterisencountersuppressingrelease) | 1 value | 1 value |
| ✅ | [C_InstanceEncounter.ShouldShowTimelineForEncounter](#c_instanceencountershouldshowtimelineforencounter) | 1 value | 1 value |

### C_InstanceEncounter.IsEncounterInProgress

`C_InstanceEncounter.IsEncounterInProgress() → isInProgress: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `InstanceEncounterDocumentation.lua`

### C_InstanceEncounter.IsEncounterLimitingResurrections

`C_InstanceEncounter.IsEncounterLimitingResurrections() → isLimitingResurrections: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `InstanceEncounterDocumentation.lua`

### C_InstanceEncounter.IsEncounterSuppressingRelease

`C_InstanceEncounter.IsEncounterSuppressingRelease() → isSuppressingRelease: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `InstanceEncounterDocumentation.lua`

### C_InstanceEncounter.ShouldShowTimelineForEncounter

`C_InstanceEncounter.ShouldShowTimelineForEncounter() → shouldShow: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `InstanceEncounterDocumentation.lua`

## Events

### ENCOUNTER_STATE_CHANGED

- Status: ✅ verified
- Payload: `isInProgress: bool`
- Blizzard: Signaled when the in-progress state of an encounter changes.
- CallbackEvent (Blizzard's docs)
- fires synchronously (Blizzard's docs)
- Seen firing 26 times (18 in combat); argument kinds: `b`

### INSTANCE_ENCOUNTER_ADD_TIMER

- Status: ✅ verified
- Payload: `timeRemaining: number`
- fires synchronously (Blizzard's docs)

### INSTANCE_ENCOUNTER_ENGAGE_UNIT

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### INSTANCE_ENCOUNTER_OBJECTIVE_COMPLETE

- Status: ✅ verified
- Payload: `objectiveID: number`
- fires synchronously (Blizzard's docs)

### INSTANCE_ENCOUNTER_OBJECTIVE_START

- Status: ✅ verified
- Payload: `objectiveID: number`, `objectiveProgress: number`
- fires synchronously (Blizzard's docs)

### INSTANCE_ENCOUNTER_OBJECTIVE_UPDATE

- Status: ✅ verified
- Payload: `objectiveID: number`, `objectiveProgress: number`
- fires synchronously (Blizzard's docs)
