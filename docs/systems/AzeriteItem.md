# AzeriteItem

Namespace: `C_AzeriteItem`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_AzeriteItem.FindActiveAzeriteItem](#c_azeriteitemfindactiveazeriteitem) |  |  |
| ✅ | [C_AzeriteItem.GetAzeriteItemXPInfo](#c_azeriteitemgetazeriteitemxpinfo) |  |  |
| ✅ | [C_AzeriteItem.GetPowerLevel](#c_azeriteitemgetpowerlevel) |  |  |
| ✅ | [C_AzeriteItem.GetUnlimitedPowerLevel](#c_azeriteitemgetunlimitedpowerlevel) |  |  |
| ✅ | [C_AzeriteItem.HasActiveAzeriteItem](#c_azeriteitemhasactiveazeriteitem) |  |  |
| ✅ | [C_AzeriteItem.IsAzeriteItem](#c_azeriteitemisazeriteitem) |  |  |
| ✅ | [C_AzeriteItem.IsAzeriteItemAtMaxLevel](#c_azeriteitemisazeriteitematmaxlevel) |  |  |
| ✅ | [C_AzeriteItem.IsAzeriteItemByID](#c_azeriteitemisazeriteitembyid) |  |  |
| ✅ | [C_AzeriteItem.IsAzeriteItemEnabled](#c_azeriteitemisazeriteitemenabled) |  |  |
| ✅ | [C_AzeriteItem.IsUnlimitedLevelingUnlocked](#c_azeriteitemisunlimitedlevelingunlocked) |  |  |

### C_AzeriteItem.FindActiveAzeriteItem

`C_AzeriteItem.FindActiveAzeriteItem() → activeAzeriteItemLocation: AzeriteItemLocation`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteItemDocumentation.lua`

### C_AzeriteItem.GetAzeriteItemXPInfo

`C_AzeriteItem.GetAzeriteItemXPInfo(azeriteItemLocation: AzeriteItemLocation) → xp: number, totalLevelXP: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteItemDocumentation.lua`

### C_AzeriteItem.GetPowerLevel

`C_AzeriteItem.GetPowerLevel(azeriteItemLocation: AzeriteItemLocation) → powerLevel: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteItemDocumentation.lua`

### C_AzeriteItem.GetUnlimitedPowerLevel

`C_AzeriteItem.GetUnlimitedPowerLevel(azeriteItemLocation: AzeriteItemLocation) → powerLevel: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteItemDocumentation.lua`

### C_AzeriteItem.HasActiveAzeriteItem

`C_AzeriteItem.HasActiveAzeriteItem() → hasActiveAzeriteItem: bool`

- Status: ✅ verified (function)
- Source: client docs `AzeriteItemDocumentation.lua`

### C_AzeriteItem.IsAzeriteItem

`C_AzeriteItem.IsAzeriteItem(itemLocation: ItemLocation) → isAzeriteItem: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteItemDocumentation.lua`

### C_AzeriteItem.IsAzeriteItemAtMaxLevel

`C_AzeriteItem.IsAzeriteItemAtMaxLevel() → isAtMax: bool`

- Status: ✅ verified (function)
- Source: client docs `AzeriteItemDocumentation.lua`

### C_AzeriteItem.IsAzeriteItemByID

`C_AzeriteItem.IsAzeriteItemByID(itemInfo: ItemInfo) → isAzeriteItem: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteItemDocumentation.lua`

### C_AzeriteItem.IsAzeriteItemEnabled

`C_AzeriteItem.IsAzeriteItemEnabled(azeriteItemLocation: AzeriteItemLocation) → isEnabled: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteItemDocumentation.lua`

### C_AzeriteItem.IsUnlimitedLevelingUnlocked

`C_AzeriteItem.IsUnlimitedLevelingUnlocked() → isUnlimitedLevelingUnlocked: bool`

- Status: ✅ verified (function)
- Source: client docs `AzeriteItemDocumentation.lua`

## Events

### AZERITE_ITEM_ENABLED_STATE_CHANGED

- Status: ✅ verified
- Payload: `enabled: bool`
- fires synchronously (Blizzard's docs)

### AZERITE_ITEM_EXPERIENCE_CHANGED

- Status: ✅ verified
- Payload: `azeriteItemLocation: AzeriteItemLocation`, `oldExperienceAmount: number`, `newExperienceAmount: number`
- fires synchronously (Blizzard's docs)

### AZERITE_ITEM_POWER_LEVEL_CHANGED

- Status: ✅ verified
- Payload: `azeriteItemLocation: AzeriteItemLocation`, `oldPowerLevel: number`, `newPowerLevel: number`, `unlockedEmpoweredItemsInfo: UnlockedAzeriteEmpoweredItems[]`, `azeriteItemID: number`
- fires synchronously (Blizzard's docs)

## Types

### UnlockedAzeriteEmpoweredItems

- Structure
  - `unlockedItem`: AzeriteEmpoweredItemLocation
  - `tierIndex`: luaIndex
