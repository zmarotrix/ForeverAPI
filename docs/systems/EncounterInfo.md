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
- Seen firing 18 times (18 in combat); argument kinds: `n,s,n,n,n,t`

### ENCOUNTER_START

- Status: ✅ verified
- Payload: `encounterID: number`, `encounterName: cstring`, `difficultyID: number`, `groupSize: number`
- fires synchronously (Blizzard's docs)
- Seen firing 18 times (8 in combat); argument kinds: `n,s,n,n`

### INSTANCE_LOCK_START

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### INSTANCE_LOCK_STOP

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 64 times (0 in combat); argument kinds: ``

### INSTANCE_LOCK_WARNING

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### RAID_TARGET_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 37 times (11 in combat); argument kinds: ``

### UPDATE_INSTANCE_INFO

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 170 times (12 in combat); argument kinds: ``

## Types

### EncounterUnitStatus

- Structure
  - `creatureID`: number
  - `creatureName`: string
  - `remainingHealthPercent`: number
