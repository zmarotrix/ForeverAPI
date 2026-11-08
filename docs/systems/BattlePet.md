# BattlePet

## Events

### PET_BATTLE_ABILITY_CHANGED

- Status: ✅ verified
- Payload: `owner: number`, `petIndex: number`, `abilityID: number`
- fires synchronously (Blizzard's docs)

### PET_BATTLE_ACTION_SELECTED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_BATTLE_AURA_APPLIED

- Status: ✅ verified
- Payload: `owner: number`, `petIndex: number`, `auraInstanceID: number`
- fires synchronously (Blizzard's docs)

### PET_BATTLE_AURA_CANCELED

- Status: ✅ verified
- Payload: `owner: number`, `petIndex: number`, `auraInstanceID: number`
- fires synchronously (Blizzard's docs)

### PET_BATTLE_AURA_CHANGED

- Status: ✅ verified
- Payload: `owner: number`, `petIndex: number`, `auraInstanceID: number`
- fires synchronously (Blizzard's docs)

### PET_BATTLE_CAPTURED

- Status: ✅ verified
- Payload: `owner: number`, `petIndex: number`
- fires synchronously (Blizzard's docs)

### PET_BATTLE_CLOSE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_BATTLE_FINAL_ROUND

- Status: ✅ verified
- Payload: `owner: number`
- fires synchronously (Blizzard's docs)

### PET_BATTLE_HEALTH_CHANGED

- Status: ✅ verified
- Payload: `owner: number`, `petIndex: number`, `healthChange: number`
- fires synchronously (Blizzard's docs)

### PET_BATTLE_LEVEL_CHANGED

- Status: ✅ verified
- Payload: `owner: number`, `petIndex: number`, `newLevel: number`
- fires synchronously (Blizzard's docs)

### PET_BATTLE_MAX_HEALTH_CHANGED

- Status: ✅ verified
- Payload: `owner: number`, `petIndex: number`, `healthChange: number`
- fires synchronously (Blizzard's docs)

### PET_BATTLE_OPENING_DONE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_BATTLE_OPENING_START

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_BATTLE_OVER

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_BATTLE_OVERRIDE_ABILITY

- Status: ✅ verified
- Payload: `abilityIndex: number`
- fires synchronously (Blizzard's docs)

### PET_BATTLE_PET_CHANGED

- Status: ✅ verified
- Payload: `owner: number`
- fires synchronously (Blizzard's docs)

### PET_BATTLE_PET_ROUND_PLAYBACK_COMPLETE

- Status: ✅ verified
- Payload: `roundNumber: number`
- fires synchronously (Blizzard's docs)

### PET_BATTLE_PET_ROUND_RESULTS

- Status: ✅ verified
- Payload: `roundNumber: number`
- fires synchronously (Blizzard's docs)

### PET_BATTLE_PET_TYPE_CHANGED

- Status: ✅ verified
- Payload: `owner: number`, `petIndex: number`, `stateValue: number`
- fires synchronously (Blizzard's docs)

### PET_BATTLE_PVP_DUEL_REQUESTED

- Status: ✅ verified
- Payload: `fullName: cstring`
- fires synchronously (Blizzard's docs)

### PET_BATTLE_PVP_DUEL_REQUEST_CANCEL

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_BATTLE_QUEUE_PROPOSAL_ACCEPTED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_BATTLE_QUEUE_PROPOSAL_DECLINED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_BATTLE_QUEUE_PROPOSE_MATCH

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_BATTLE_QUEUE_STATUS

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PET_BATTLE_XP_CHANGED

- Status: ✅ verified
- Payload: `owner: number`, `petIndex: number`, `xpChange: number`
- fires synchronously (Blizzard's docs)
