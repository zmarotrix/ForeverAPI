# ChromieTimeInfo

Namespace: `C_ChromieTime`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ChromieTime.CloseUI](#c_chromietimecloseui) |  |  |
| ✅ | [C_ChromieTime.GetChromieTimeExpansionOption](#c_chromietimegetchromietimeexpansionoption) |  |  |
| ✅ | [C_ChromieTime.GetChromieTimeExpansionOptions](#c_chromietimegetchromietimeexpansionoptions) | 1 value |  |
| ✅ | [C_ChromieTime.SelectChromieTimeOption](#c_chromietimeselectchromietimeoption) |  |  |

### C_ChromieTime.CloseUI

`C_ChromieTime.CloseUI()`

- Status: ✅ verified (function)
- Source: client docs `ChromieTimeUIDocumentation.lua`

### C_ChromieTime.GetChromieTimeExpansionOption

`C_ChromieTime.GetChromieTimeExpansionOption(expansionRecID: number) → info: ChromieTimeExpansionInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChromieTimeUIDocumentation.lua`

### C_ChromieTime.GetChromieTimeExpansionOptions

`C_ChromieTime.GetChromieTimeExpansionOptions() → expansionOptions: ChromieTimeExpansionInfo[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Source: client docs `ChromieTimeUIDocumentation.lua`

### C_ChromieTime.SelectChromieTimeOption

`C_ChromieTime.SelectChromieTimeOption(chromieTimeExpansionInfoId: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChromieTimeUIDocumentation.lua`

## Types

### ChromieTimeExpansionInfo

- Structure
  - `id`: number
  - `name`: cstring
  - `description`: cstring
  - `mapAtlas`: textureAtlas
  - `previewAtlas`: textureAtlas
  - `completed`: bool
  - `alreadyOn`: bool
  - `recommended`: bool
  - `sortPriority`: number
