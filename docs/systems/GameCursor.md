# GameCursor

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [ClearCursor](#clearcursor) |  |  |
| ✅ | [ClearCursorHoveredItem](#clearcursorhovereditem) |  |  |
| ✅ | [CursorHasItem](#cursorhasitem) |  |  |
| ✅ | [CursorHasMacro](#cursorhasmacro) |  |  |
| ✅ | [CursorHasMoney](#cursorhasmoney) |  |  |
| ✅ | [CursorHasSpell](#cursorhasspell) |  |  |
| ✅ | [DeleteCursorItem](#deletecursoritem) |  |  |
| ✅ | [DropCursorMoney](#dropcursormoney) |  |  |
| ✅ | [EquipCursorItem](#equipcursoritem) |  |  |
| ✅ | [GetCursorInfo](#getcursorinfo) | 0 values |  |
| ✅ | [GetCursorMoney](#getcursormoney) | 1 value |  |
| ✅ | [PickupPlayerMoney](#pickupplayermoney) |  |  |
| ✅ | [ResetCursor](#resetcursor) |  |  |
| ✅ | [SellCursorItem](#sellcursoritem) |  |  |
| ✅ | [SetCursor](#setcursor) |  |  |
| ✅ | [SetCursorByMode](#setcursorbymode) |  |  |
| ✅ | [SetCursorHoveredItem](#setcursorhovereditem) |  |  |
| ✅ | [SetCursorHoveredItemTradeItem](#setcursorhovereditemtradeitem) |  |  |
| ✅ | [SetCursorVirtualItem](#setcursorvirtualitem) |  |  |

### ClearCursor

`ClearCursor()`

- Status: ✅ verified (function)
- Source: client docs `GameCursorDocumentation.lua`

### ClearCursorHoveredItem

`ClearCursorHoveredItem()`

- Status: ✅ verified (function)
- Source: client docs `GameCursorDocumentation.lua`

### CursorHasItem

`CursorHasItem() → result: bool`

- Status: ✅ verified (function)
- Source: client docs `GameCursorDocumentation.lua`

### CursorHasMacro

`CursorHasMacro() → result: bool`

- Status: ✅ verified (function)
- Source: client docs `GameCursorDocumentation.lua`

### CursorHasMoney

`CursorHasMoney() → result: bool`

- Status: ✅ verified (function)
- Source: client docs `GameCursorDocumentation.lua`

### CursorHasSpell

`CursorHasSpell() → result: bool`

- Status: ✅ verified (function)
- Source: client docs `GameCursorDocumentation.lua`

### DeleteCursorItem

`DeleteCursorItem()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `GameCursorDocumentation.lua`

### DropCursorMoney

`DropCursorMoney()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `GameCursorDocumentation.lua`

### EquipCursorItem

`EquipCursorItem(slot: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GameCursorDocumentation.lua`

### GetCursorInfo

`GetCursorInfo()`

- Status: ✅ verified (function)
- Called out of combat: returned 0 values
- Source: client docs `GameCursorDocumentation.lua`

### GetCursorMoney

`GetCursorMoney() → amount: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `GameCursorDocumentation.lua`

### PickupPlayerMoney

`PickupPlayerMoney(amount: WOWMONEY)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GameCursorDocumentation.lua`

### ResetCursor

`ResetCursor()`

- Status: ✅ verified (function)
- Source: client docs `GameCursorDocumentation.lua`

### SellCursorItem

`SellCursorItem()`

- Status: ✅ verified (function)
- Source: client docs `GameCursorDocumentation.lua`

### SetCursor

`SetCursor(name: cstring?) → result: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GameCursorDocumentation.lua`

### SetCursorByMode

`SetCursorByMode(mode: Cursormode) → result: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GameCursorDocumentation.lua`

### SetCursorHoveredItem

`SetCursorHoveredItem(item: ItemLocation)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GameCursorDocumentation.lua`

### SetCursorHoveredItemTradeItem

`SetCursorHoveredItemTradeItem(enabled: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GameCursorDocumentation.lua`

### SetCursorVirtualItem

`SetCursorVirtualItem(itemInfo: ItemInfo, cursorType: UICursorType)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GameCursorDocumentation.lua`
