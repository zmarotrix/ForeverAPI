# Title

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [GetCurrentTitle](#getcurrenttitle) | 1 value | 1 value |
| ✅ | [GetNumTitles](#getnumtitles) | 1 value | 1 value |
| ✅ | [GetTitleName](#gettitlename) |  |  |
| ✅ | [IsTitleKnown](#istitleknown) |  |  |
| ✅ | [SetCurrentTitle](#setcurrenttitle) |  |  |

### GetCurrentTitle

`GetCurrentTitle() → result: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `TitleDocumentation.lua`

### GetNumTitles

`GetNumTitles() → result: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `TitleDocumentation.lua`

### GetTitleName

`GetTitleName(titleMaskID: number) → titleString: string, playerTitle: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TitleDocumentation.lua`

### IsTitleKnown

`IsTitleKnown(titleMaskID: number) → result: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TitleDocumentation.lua`

### SetCurrentTitle

`SetCurrentTitle(titleMaskID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TitleDocumentation.lua`
