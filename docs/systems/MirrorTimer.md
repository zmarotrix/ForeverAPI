# MirrorTimer

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [GetMirrorTimerInfo](#getmirrortimerinfo) |  |  |
| ❔ | [GetMirrorTimerProgress](#getmirrortimerprogress) |  |  |

### GetMirrorTimerInfo

`GetMirrorTimerInfo(timerIndex: luaIndex) → name: cstring, startValue: number, maxValue: number, scale: number, paused: number, label: cstring, spellID: number`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MirrorTimerDocumentation.lua`

### GetMirrorTimerProgress

`GetMirrorTimerProgress(timerName: cstring) → progress: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MirrorTimerDocumentation.lua`

## Types

### MirrorTimerInfo

- Structure
  - `name`: cstring
  - `startValue`: number
  - `maxValue`: number
  - `scale`: number
  - `paused`: number
  - `label`: cstring
  - `spellID`: number
