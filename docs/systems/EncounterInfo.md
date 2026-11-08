# EncounterInfo

## Events

### BOSS_KILL

- Status: ❔ unverified
- Payload: `encounterID: number`, `encounterName: cstring`
- fires synchronously (Blizzard's docs)

### DISABLE_LOW_LEVEL_RAID

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### ENABLE_LOW_LEVEL_RAID

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### ENCOUNTER_END

- Status: ❔ unverified
- Payload: `encounterID: number`, `encounterName: cstring`, `difficultyID: number`, `groupSize: number`, `success: number`, `encounterUnitStatus: EncounterUnitStatus[]`
- fires synchronously (Blizzard's docs)

### ENCOUNTER_START

- Status: ❔ unverified
- Payload: `encounterID: number`, `encounterName: cstring`, `difficultyID: number`, `groupSize: number`
- fires synchronously (Blizzard's docs)

### INSTANCE_LOCK_START

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### INSTANCE_LOCK_STOP

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### INSTANCE_LOCK_WARNING

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### RAID_TARGET_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### UPDATE_INSTANCE_INFO

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### EncounterUnitStatus

- Structure
  - `creatureID`: number
  - `creatureName`: string
  - `remainingHealthPercent`: number
