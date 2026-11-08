# TimerunningUI

Namespace: `C_TimerunningUI`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_TimerunningUI.GetActiveTimerunningSeasonID](#c_timerunninguigetactivetimerunningseasonid) | 1 value | 1 value |

### C_TimerunningUI.GetActiveTimerunningSeasonID

`C_TimerunningUI.GetActiveTimerunningSeasonID() → activeTimerunningSeasonID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `TimerunningUIDocumentation.lua`

## Events

### REMIX_END_OF_EVENT

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
