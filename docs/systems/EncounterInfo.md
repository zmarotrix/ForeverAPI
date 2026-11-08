# EncounterInfo

## Events

### BOSS_KILL

- Status: ✅ verified
- Payload: `encounterID: number`, `encounterName: cstring`
- fires synchronously (Blizzard's docs)

### DISABLE_LOW_LEVEL_RAID

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### ENABLE_LOW_LEVEL_RAID

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### ENCOUNTER_END

- Status: ✅ verified
- Payload: `encounterID: number`, `encounterName: cstring`, `difficultyID: number`, `groupSize: number`, `success: number`, `encounterUnitStatus: EncounterUnitStatus[]`
- fires synchronously (Blizzard's docs)
- Seen firing 4 times (4 in combat); argument kinds: `n,s,n,n,n,t`

### ENCOUNTER_START

- Status: ✅ verified
- Payload: `encounterID: number`, `encounterName: cstring`, `difficultyID: number`, `groupSize: number`
- fires synchronously (Blizzard's docs)
- Seen firing 4 times (0 in combat); argument kinds: `n,s,n,n`

### INSTANCE_LOCK_START

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### INSTANCE_LOCK_STOP

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 27 times (0 in combat); argument kinds: ``

### INSTANCE_LOCK_WARNING

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### RAID_TARGET_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 22 times (2 in combat); argument kinds: ``

### UPDATE_INSTANCE_INFO

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 71 times (0 in combat); argument kinds: ``

## Types

### EncounterUnitStatus

- Structure
  - `creatureID`: number
  - `creatureName`: string
  - `remainingHealthPercent`: number
