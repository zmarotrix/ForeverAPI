# SystemInfo

Namespace: `C_System`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_System.GetFrameStack](#c_systemgetframestack) | 1 value | 1 value |

### C_System.GetFrameStack

`C_System.GetFrameStack() → objects: ScriptRegion[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table}`
- Called in combat: returned 1 value: `table{[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table,[number]=table}`
- Source: client docs `SystemDocumentation.lua`

## Events

### CAPTUREFRAMES_FAILED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CAPTUREFRAMES_SUCCEEDED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### DISABLE_TAXI_BENCHMARK

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### ENABLE_TAXI_BENCHMARK

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### FIRST_FRAME_RENDERED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)
- Seen firing 17 times (0 in combat); argument kinds: ``

### GENERIC_ERROR

- Status: ✅ verified
- Payload: `errorMessage: cstring`
- fires synchronously (Blizzard's docs)

### GLOBAL_MOUSE_DOWN

- Status: ✅ verified
- Payload: `button: cstring`
- fires synchronously (Blizzard's docs)
- Seen firing 3584 times (1447 in combat); argument kinds: `s`

### GLOBAL_MOUSE_UP

- Status: ✅ verified
- Payload: `button: cstring`
- fires synchronously (Blizzard's docs)
- Seen firing 3584 times (1460 in combat); argument kinds: `s`

### GLOBAL_REGION_MOUSE_DOWN

- Status: ✅ verified
- Payload: `region: ScriptRegion`, `button: cstring`
- fires synchronously (Blizzard's docs)
- Seen firing 2790 times (1233 in combat); argument kinds: `-,s` / `t,s`

### GLOBAL_REGION_MOUSE_UP

- Status: ✅ verified
- Payload: `region: ScriptRegion`, `button: cstring`
- fires synchronously (Blizzard's docs)
- Seen firing 3587 times (1460 in combat); argument kinds: `-,s` / `t,s`

### INITIAL_HOTFIXES_APPLIED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### LOC_RESULT

- Status: ✅ verified
- Payload: `result: cstring`
- fires synchronously (Blizzard's docs)

### LOGOUT_CANCEL

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_CAMPING

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_ENTERING_WORLD

- Status: ✅ verified
- Payload: `isInitialLogin: bool`, `isReloadingUi: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 27 times (0 in combat); argument kinds: `b,b`

### PLAYER_LEAVING_WORLD

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 27 times (0 in combat); argument kinds: ``

### PLAYER_LOGIN

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 17 times (0 in combat); argument kinds: ``

### PLAYER_LOGOUT

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 17 times (0 in combat); argument kinds: ``

### PLAYER_QUITING

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SEARCH_DB_LOADED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SHARD_TRANSFER

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 6 times (0 in combat); argument kinds: ``

### SHARD_TRANSFER_CANCELLED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SHARD_TRANSFER_IMMINENT

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### STREAMING_ICON

- Status: ✅ verified
- Payload: `streamingStatus: number`
- fires synchronously (Blizzard's docs)

### SYSMSG

- Status: ✅ verified
- Payload: `string: cstring`, `r: number`, `g: number`, `b: number`
- fires synchronously (Blizzard's docs)

### TIME_PLAYED_MSG

- Status: ✅ verified
- Payload: `totalTimePlayed: number`, `timePlayedThisLevel: number`
- fires synchronously (Blizzard's docs)
- Seen firing 17 times (2 in combat); argument kinds: `n,n`

### UI_ERROR_MESSAGE

- Status: ✅ verified
- Payload: `errorType: luaIndex`, `message: string`
- unique event (Blizzard's docs)
- Seen firing 4029 times (3893 in combat); argument kinds: `n,s`

### UI_ERROR_POPUP

- Status: ✅ verified
- Payload: `errorType: luaIndex`, `message: string`
- unique event (Blizzard's docs)

### UI_INFO_MESSAGE

- Status: ✅ verified
- Payload: `errorType: luaIndex`, `message: string`
- unique event (Blizzard's docs)
- Seen firing 16 times (3 in combat); argument kinds: `n,s`

### VARIABLES_LOADED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 17 times (0 in combat); argument kinds: ``

### WOW_MOUSE_NOT_FOUND

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
