# ChromieTimeInfo

Namespace: `C_ChromieTime`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_ChromieTime.CloseUI](#c_chromietimecloseui) |  |  |
| ❔ | [C_ChromieTime.GetChromieTimeExpansionOption](#c_chromietimegetchromietimeexpansionoption) |  |  |
| ❔ | [C_ChromieTime.GetChromieTimeExpansionOptions](#c_chromietimegetchromietimeexpansionoptions) |  |  |
| ❔ | [C_ChromieTime.SelectChromieTimeOption](#c_chromietimeselectchromietimeoption) |  |  |

### C_ChromieTime.CloseUI

`C_ChromieTime.CloseUI()`

- Status: ❔ unverified
- Source: client docs `ChromieTimeUIDocumentation.lua`

### C_ChromieTime.GetChromieTimeExpansionOption

`C_ChromieTime.GetChromieTimeExpansionOption(expansionRecID: number) → info: ChromieTimeExpansionInfo?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ChromieTimeUIDocumentation.lua`

### C_ChromieTime.GetChromieTimeExpansionOptions

`C_ChromieTime.GetChromieTimeExpansionOptions() → expansionOptions: ChromieTimeExpansionInfo[]`

- Status: ❔ unverified
- Source: client docs `ChromieTimeUIDocumentation.lua`

### C_ChromieTime.SelectChromieTimeOption

`C_ChromieTime.SelectChromieTimeOption(chromieTimeExpansionInfoId: number)`

- Status: ❔ unverified
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
