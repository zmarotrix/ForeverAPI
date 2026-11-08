# Os

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [CopyToClipboard](#copytoclipboard) |  |  |
| ✅ | [GetTimePreciseSec](#gettimeprecisesec) | 1 value | 1 value |

### CopyToClipboard

`CopyToClipboard(text: cstring, removeMarkup: bool = False) → length: number`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `OsDocumentation.lua`

### GetTimePreciseSec

`GetTimePreciseSec() → time: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `OsDocumentation.lua`
