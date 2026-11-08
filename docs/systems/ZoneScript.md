# ZoneScript

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [GetAreaText](#getareatext) | 1 value |  |
| ✅ | [GetMinimapZoneText](#getminimapzonetext) | 1 value |  |
| ✅ | [GetRealZoneText](#getrealzonetext) | 1 value |  |
| ✅ | [GetSubZoneText](#getsubzonetext) | 1 value |  |
| ✅ | [GetZoneText](#getzonetext) | 1 value |  |

### GetAreaText

`GetAreaText() → text: cstring`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `string`
- Source: client docs `ZoneScriptDocumentation.lua`

### GetMinimapZoneText

`GetMinimapZoneText() → text: cstring`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `string`
- Source: client docs `ZoneScriptDocumentation.lua`

### GetRealZoneText

`GetRealZoneText(mapID: number?) → text: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `string`
- Source: client docs `ZoneScriptDocumentation.lua`

### GetSubZoneText

`GetSubZoneText() → text: cstring`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `string`
- Source: client docs `ZoneScriptDocumentation.lua`

### GetZoneText

`GetZoneText() → text: cstring`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `string`
- Source: client docs `ZoneScriptDocumentation.lua`
