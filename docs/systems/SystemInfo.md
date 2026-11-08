# SystemInfo

Namespace: `C_System`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_System.GetFrameStack](#c_systemgetframestack) |  |  |

### C_System.GetFrameStack

`C_System.GetFrameStack() → objects: ScriptRegion[]`

- Status: ❔ unverified
- Source: client docs `SystemDocumentation.lua`

## Events

### CAPTUREFRAMES_FAILED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CAPTUREFRAMES_SUCCEEDED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### DISABLE_TAXI_BENCHMARK

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### ENABLE_TAXI_BENCHMARK

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### FIRST_FRAME_RENDERED

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

### GENERIC_ERROR

- Status: ❔ unverified
- Payload: `errorMessage: cstring`
- fires synchronously (Blizzard's docs)

### GLOBAL_MOUSE_DOWN

- Status: ❔ unverified
- Payload: `button: cstring`
- fires synchronously (Blizzard's docs)

### GLOBAL_MOUSE_UP

- Status: ❔ unverified
- Payload: `button: cstring`
- fires synchronously (Blizzard's docs)

### GLOBAL_REGION_MOUSE_DOWN

- Status: ❔ unverified
- Payload: `region: ScriptRegion`, `button: cstring`
- fires synchronously (Blizzard's docs)

### GLOBAL_REGION_MOUSE_UP

- Status: ❔ unverified
- Payload: `region: ScriptRegion`, `button: cstring`
- fires synchronously (Blizzard's docs)

### INITIAL_HOTFIXES_APPLIED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### LOC_RESULT

- Status: ❔ unverified
- Payload: `result: cstring`
- fires synchronously (Blizzard's docs)

### LOGOUT_CANCEL

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_CAMPING

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_ENTERING_WORLD

- Status: ❔ unverified
- Payload: `isInitialLogin: bool`, `isReloadingUi: bool`
- fires synchronously (Blizzard's docs)

### PLAYER_LEAVING_WORLD

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_LOGIN

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_LOGOUT

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_QUITING

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SEARCH_DB_LOADED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SHARD_TRANSFER

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SHARD_TRANSFER_CANCELLED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SHARD_TRANSFER_IMMINENT

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### STREAMING_ICON

- Status: ❔ unverified
- Payload: `streamingStatus: number`
- fires synchronously (Blizzard's docs)

### SYSMSG

- Status: ❔ unverified
- Payload: `string: cstring`, `r: number`, `g: number`, `b: number`
- fires synchronously (Blizzard's docs)

### TIME_PLAYED_MSG

- Status: ❔ unverified
- Payload: `totalTimePlayed: number`, `timePlayedThisLevel: number`
- fires synchronously (Blizzard's docs)

### UI_ERROR_MESSAGE

- Status: ❔ unverified
- Payload: `errorType: luaIndex`, `message: string`
- unique event (Blizzard's docs)

### UI_ERROR_POPUP

- Status: ❔ unverified
- Payload: `errorType: luaIndex`, `message: string`
- unique event (Blizzard's docs)

### UI_INFO_MESSAGE

- Status: ❔ unverified
- Payload: `errorType: luaIndex`, `message: string`
- unique event (Blizzard's docs)

### VARIABLES_LOADED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### WOW_MOUSE_NOT_FOUND

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)
