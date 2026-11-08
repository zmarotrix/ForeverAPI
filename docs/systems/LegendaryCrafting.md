# LegendaryCrafting

Namespace: `C_LegendaryCrafting`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_LegendaryCrafting.CloseRuneforgeInteraction](#c_legendarycraftingcloseruneforgeinteraction) |  |  |
| ✅ | [C_LegendaryCrafting.CraftRuneforgeLegendary](#c_legendarycraftingcraftruneforgelegendary) |  |  |
| ✅ | [C_LegendaryCrafting.GetRuneforgeItemPreviewInfo](#c_legendarycraftinggetruneforgeitempreviewinfo) | 1 value | 1 value |
| ✅ | [C_LegendaryCrafting.GetRuneforgeLegendaryComponentInfo](#c_legendarycraftinggetruneforgelegendarycomponentinfo) | 1 value | 1 value |
| ✅ | [C_LegendaryCrafting.GetRuneforgeLegendaryCost](#c_legendarycraftinggetruneforgelegendarycost) | 1 value | 1 value |
| ✅ | [C_LegendaryCrafting.GetRuneforgeLegendaryCraftSpellID](#c_legendarycraftinggetruneforgelegendarycraftspellid) | 1 value | 1 value |
| ✅ | [C_LegendaryCrafting.GetRuneforgeLegendaryCurrencies](#c_legendarycraftinggetruneforgelegendarycurrencies) | 1 value | 1 value |
| ✅ | [C_LegendaryCrafting.GetRuneforgeLegendaryUpgradeCost](#c_legendarycraftinggetruneforgelegendaryupgradecost) | 1 value | 1 value |
| ✅ | [C_LegendaryCrafting.GetRuneforgeModifierInfo](#c_legendarycraftinggetruneforgemodifierinfo) |  |  |
| ✅ | [C_LegendaryCrafting.GetRuneforgeModifiers](#c_legendarycraftinggetruneforgemodifiers) | 1 value | 1 value |
| ✅ | [C_LegendaryCrafting.GetRuneforgePowerInfo](#c_legendarycraftinggetruneforgepowerinfo) |  |  |
| ✅ | [C_LegendaryCrafting.GetRuneforgePowerSlots](#c_legendarycraftinggetruneforgepowerslots) |  |  |
| ✅ | [C_LegendaryCrafting.GetRuneforgePowers](#c_legendarycraftinggetruneforgepowers) | 2 values | 2 values |
| ✅ | [C_LegendaryCrafting.GetRuneforgePowersByClassSpecAndCovenant](#c_legendarycraftinggetruneforgepowersbyclassspecandcovenant) | 1 value | 1 value |
| ✅ | [C_LegendaryCrafting.IsRuneforgeLegendary](#c_legendarycraftingisruneforgelegendary) | 1 value | 1 value |
| ✅ | [C_LegendaryCrafting.IsRuneforgeLegendaryMaxLevel](#c_legendarycraftingisruneforgelegendarymaxlevel) | 1 value | 1 value |
| ✅ | [C_LegendaryCrafting.IsUpgradeItemValidForRuneforgeLegendary](#c_legendarycraftingisupgradeitemvalidforruneforgelegendary) | 1 value | 1 value |
| ✅ | [C_LegendaryCrafting.IsValidRuneforgeBaseItem](#c_legendarycraftingisvalidruneforgebaseitem) | 1 value | 1 value |
| ✅ | [C_LegendaryCrafting.MakeRuneforgeCraftDescription](#c_legendarycraftingmakeruneforgecraftdescription) |  |  |
| ✅ | [C_LegendaryCrafting.UpgradeRuneforgeLegendary](#c_legendarycraftingupgraderuneforgelegendary) |  |  |

### C_LegendaryCrafting.CloseRuneforgeInteraction

`C_LegendaryCrafting.CloseRuneforgeInteraction()`

- Status: ✅ verified (function)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.CraftRuneforgeLegendary

`C_LegendaryCrafting.CraftRuneforgeLegendary(description: RuneforgeLegendaryCraftDescription)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgeItemPreviewInfo

`C_LegendaryCrafting.GetRuneforgeItemPreviewInfo(baseItem: ItemLocation, runeforgePowerID: number?, modifiers: number[]?) → info: RuneforgeItemPreviewInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `itemloc`: returned 1 value: `table{itemGUID=string,itemLevel=number,itemName=string}`
- Called in combat: returned 1 value: `table{itemGUID=string,itemLevel=number,itemName=string}`
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgeLegendaryComponentInfo

`C_LegendaryCrafting.GetRuneforgeLegendaryComponentInfo(runeforgeLegendary: ItemLocation) → componentInfo: RuneforgeLegendaryComponentInfo`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `itemloc`: returned 1 value: `table{modifiers=table,powerID=number}`
- Called in combat: returned 1 value: `table{modifiers=table,powerID=number}`
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgeLegendaryCost

`C_LegendaryCrafting.GetRuneforgeLegendaryCost(baseItem: ItemLocation) → cost: CurrencyCost[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `itemloc`: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgeLegendaryCraftSpellID

`C_LegendaryCrafting.GetRuneforgeLegendaryCraftSpellID() → spellID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgeLegendaryCurrencies

`C_LegendaryCrafting.GetRuneforgeLegendaryCurrencies() → currencies: number[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgeLegendaryUpgradeCost

`C_LegendaryCrafting.GetRuneforgeLegendaryUpgradeCost(runeforgeLegendary: ItemLocation, upgradeItem: ItemLocation) → cost: CurrencyCost[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `itemloc,itemloc`: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgeModifierInfo

`C_LegendaryCrafting.GetRuneforgeModifierInfo(baseItem: ItemLocation, powerID: number?, addedModifierIndex: luaIndex, modifiers: number[]) → name: string, description: string[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgeModifiers

`C_LegendaryCrafting.GetRuneforgeModifiers() → modifiedReagentItemIDs: number[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgePowerInfo

`C_LegendaryCrafting.GetRuneforgePowerInfo(runeforgePowerID: number) → power: RuneforgePower`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgePowerSlots

`C_LegendaryCrafting.GetRuneforgePowerSlots(runeforgePowerID: number) → slotNames: cstring[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgePowers

`C_LegendaryCrafting.GetRuneforgePowers(baseItem: ItemLocation?, filter: RuneforgePowerFilter?) → primaryRuneforgePowerIDs: number[], otherRuneforgePowerIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 2 values: `table{}`, `table{}`
- Called in combat: returned 2 values: `table{}`, `table{}`
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgePowersByClassSpecAndCovenant

`C_LegendaryCrafting.GetRuneforgePowersByClassSpecAndCovenant(classID: number?, specID: number?, covenantID: number?, filter: RuneforgePowerFilter?) → runeforgePowerIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.IsRuneforgeLegendary

`C_LegendaryCrafting.IsRuneforgeLegendary(item: ItemLocation) → isRuneforgeLegendary: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `itemloc`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.IsRuneforgeLegendaryMaxLevel

`C_LegendaryCrafting.IsRuneforgeLegendaryMaxLevel(runeforgeLegendary: ItemLocation) → isMaxLevel: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `itemloc`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.IsUpgradeItemValidForRuneforgeLegendary

`C_LegendaryCrafting.IsUpgradeItemValidForRuneforgeLegendary(runeforgeLegendary: ItemLocation, upgradeItem: ItemLocation) → isValid: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `itemloc,itemloc`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.IsValidRuneforgeBaseItem

`C_LegendaryCrafting.IsValidRuneforgeBaseItem(baseItem: ItemLocation) → isValid: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `itemloc`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.MakeRuneforgeCraftDescription

`C_LegendaryCrafting.MakeRuneforgeCraftDescription(baseItem: ItemLocation, runeforgePowerID: number, modifiers: number[]) → description: RuneforgeLegendaryCraftDescription`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.UpgradeRuneforgeLegendary

`C_LegendaryCrafting.UpgradeRuneforgeLegendary(runeforgeLegendary: ItemLocation, upgradeItem: ItemLocation)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

## Events

### NEW_RUNEFORGE_POWER_ADDED

- Status: ✅ verified
- Payload: `powerID: number`
- fires synchronously (Blizzard's docs)

### RUNEFORGE_LEGENDARY_CRAFTING_CLOSED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### RUNEFORGE_LEGENDARY_CRAFTING_OPENED

- Status: ✅ verified
- Payload: `isUpgrade: bool`
- fires synchronously (Blizzard's docs)

### RUNEFORGE_POWER_INFO_UPDATED

- Status: ✅ verified
- Payload: `powerID: number`
- fires synchronously (Blizzard's docs)
