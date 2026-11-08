# WorldStateInfo

## Events

### CANCEL_PLAYER_COUNTDOWN

- Status: ❔ unverified
- Payload: `initiatedBy: WOWGUID`, `informChat: bool`, `initiatedByName: string?`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### START_PLAYER_COUNTDOWN

- Status: ❔ unverified
- Payload: `initiatedBy: WOWGUID`, `timeRemaining: time_t`, `totalTime: time_t`, `informChat: bool`, `initiatedByName: string?`
- secret during chat lockdown (Blizzard's docs)
- fires synchronously (Blizzard's docs)

### START_TIMER

- Status: ❔ unverified
- Payload: `timerType: StartTimerType`, `timeRemaining: time_t`, `totalTime: time_t`
- fires synchronously (Blizzard's docs)

### STOP_TIMER_OF_TYPE

- Status: ❔ unverified
- Payload: `timerType: StartTimerType`
- fires synchronously (Blizzard's docs)

### WORLD_STATE_TIMER_START

- Status: ❔ unverified
- Payload: `timerID: number`
- fires synchronously (Blizzard's docs)

### WORLD_STATE_TIMER_STOP

- Status: ❔ unverified
- Payload: `timerID: number`
- fires synchronously (Blizzard's docs)
