# NewItems

Namespace: `C_NewItems`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_NewItems.ClearAll](#c_newitemsclearall) |  |  |
| ✅ | [C_NewItems.IsNewItem](#c_newitemsisnewitem) |  |  |
| ✅ | [C_NewItems.RemoveNewItem](#c_newitemsremovenewitem) |  |  |

### C_NewItems.ClearAll

`C_NewItems.ClearAll()`

- Status: ✅ verified (function)
- Source: client docs `NewItemsDocumentation.lua`

### C_NewItems.IsNewItem

`C_NewItems.IsNewItem(containerIndex: BagIndex, slotIndex: luaIndex) → isNew: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `NewItemsDocumentation.lua`

### C_NewItems.RemoveNewItem

`C_NewItems.RemoveNewItem(containerIndex: BagIndex, slotIndex: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `NewItemsDocumentation.lua`
