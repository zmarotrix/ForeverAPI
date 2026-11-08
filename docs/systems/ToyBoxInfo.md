# ToyBoxInfo

Namespace: `C_ToyBoxInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_ToyBoxInfo.ClearFanfare](#c_toyboxinfoclearfanfare) |  |  |
| ❔ | [C_ToyBoxInfo.HasAnyToy](#c_toyboxinfohasanytoy) |  |  |
| ❔ | [C_ToyBoxInfo.IsToySourceValid](#c_toyboxinfoistoysourcevalid) |  |  |
| ❔ | [C_ToyBoxInfo.IsUsingDefaultFilters](#c_toyboxinfoisusingdefaultfilters) |  |  |
| ❔ | [C_ToyBoxInfo.NeedsFanfare](#c_toyboxinfoneedsfanfare) |  |  |
| ❔ | [C_ToyBoxInfo.SetDefaultFilters](#c_toyboxinfosetdefaultfilters) |  |  |

### C_ToyBoxInfo.ClearFanfare

`C_ToyBoxInfo.ClearFanfare(itemID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ToyBoxInfoDocumentation.lua`

### C_ToyBoxInfo.HasAnyToy

`C_ToyBoxInfo.HasAnyToy() → hasToy: bool`

- Status: ❔ unverified
- Source: client docs `ToyBoxInfoDocumentation.lua`

### C_ToyBoxInfo.IsToySourceValid

`C_ToyBoxInfo.IsToySourceValid(source: luaIndex) → isToySourceValid: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ToyBoxInfoDocumentation.lua`

### C_ToyBoxInfo.IsUsingDefaultFilters

`C_ToyBoxInfo.IsUsingDefaultFilters() → isUsingDefaultFilters: bool`

- Status: ❔ unverified
- Source: client docs `ToyBoxInfoDocumentation.lua`

### C_ToyBoxInfo.NeedsFanfare

`C_ToyBoxInfo.NeedsFanfare(itemID: number) → needsFanfare: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ToyBoxInfoDocumentation.lua`

### C_ToyBoxInfo.SetDefaultFilters

`C_ToyBoxInfo.SetDefaultFilters()`

- Status: ❔ unverified
- Source: client docs `ToyBoxInfoDocumentation.lua`

## Events

### NEW_TOY_ADDED

- Status: ❔ unverified
- Payload: `itemID: number`
- fires synchronously (Blizzard's docs)

### TOYS_UPDATED

- Status: ❔ unverified
- Payload: `itemID: number?`, `isNew: bool?`, `hasFanfare: bool?`
- fires synchronously (Blizzard's docs)
- unique event (Blizzard's docs)
