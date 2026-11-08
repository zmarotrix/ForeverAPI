# ToyBoxInfo

Namespace: `C_ToyBoxInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ToyBoxInfo.ClearFanfare](#c_toyboxinfoclearfanfare) |  |  |
| ✅ | [C_ToyBoxInfo.HasAnyToy](#c_toyboxinfohasanytoy) | 1 value |  |
| ✅ | [C_ToyBoxInfo.IsToySourceValid](#c_toyboxinfoistoysourcevalid) |  |  |
| ✅ | [C_ToyBoxInfo.IsUsingDefaultFilters](#c_toyboxinfoisusingdefaultfilters) | 1 value |  |
| ✅ | [C_ToyBoxInfo.NeedsFanfare](#c_toyboxinfoneedsfanfare) |  |  |
| ✅ | [C_ToyBoxInfo.SetDefaultFilters](#c_toyboxinfosetdefaultfilters) |  |  |

### C_ToyBoxInfo.ClearFanfare

`C_ToyBoxInfo.ClearFanfare(itemID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ToyBoxInfoDocumentation.lua`

### C_ToyBoxInfo.HasAnyToy

`C_ToyBoxInfo.HasAnyToy() → hasToy: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `ToyBoxInfoDocumentation.lua`

### C_ToyBoxInfo.IsToySourceValid

`C_ToyBoxInfo.IsToySourceValid(source: luaIndex) → isToySourceValid: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ToyBoxInfoDocumentation.lua`

### C_ToyBoxInfo.IsUsingDefaultFilters

`C_ToyBoxInfo.IsUsingDefaultFilters() → isUsingDefaultFilters: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `ToyBoxInfoDocumentation.lua`

### C_ToyBoxInfo.NeedsFanfare

`C_ToyBoxInfo.NeedsFanfare(itemID: number) → needsFanfare: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ToyBoxInfoDocumentation.lua`

### C_ToyBoxInfo.SetDefaultFilters

`C_ToyBoxInfo.SetDefaultFilters()`

- Status: ✅ verified (function)
- Source: client docs `ToyBoxInfoDocumentation.lua`

## Events

### NEW_TOY_ADDED

- Status: ✅ verified
- Payload: `itemID: number`
- fires synchronously (Blizzard's docs)

### TOYS_UPDATED

- Status: ✅ verified
- Payload: `itemID: number?`, `isNew: bool?`, `hasFanfare: bool?`
- fires synchronously (Blizzard's docs)
- unique event (Blizzard's docs)
- Seen firing 16 times (0 in combat); argument kinds: `-,-,-` / `n,b,b`
