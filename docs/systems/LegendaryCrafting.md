# LegendaryCrafting

Namespace: `C_LegendaryCrafting`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_LegendaryCrafting.CloseRuneforgeInteraction](#c_legendarycraftingcloseruneforgeinteraction) |  |  |
| ❔ | [C_LegendaryCrafting.CraftRuneforgeLegendary](#c_legendarycraftingcraftruneforgelegendary) |  |  |
| ❔ | [C_LegendaryCrafting.GetRuneforgeItemPreviewInfo](#c_legendarycraftinggetruneforgeitempreviewinfo) |  |  |
| ❔ | [C_LegendaryCrafting.GetRuneforgeLegendaryComponentInfo](#c_legendarycraftinggetruneforgelegendarycomponentinfo) |  |  |
| ❔ | [C_LegendaryCrafting.GetRuneforgeLegendaryCost](#c_legendarycraftinggetruneforgelegendarycost) |  |  |
| ❔ | [C_LegendaryCrafting.GetRuneforgeLegendaryCraftSpellID](#c_legendarycraftinggetruneforgelegendarycraftspellid) |  |  |
| ❔ | [C_LegendaryCrafting.GetRuneforgeLegendaryCurrencies](#c_legendarycraftinggetruneforgelegendarycurrencies) |  |  |
| ❔ | [C_LegendaryCrafting.GetRuneforgeLegendaryUpgradeCost](#c_legendarycraftinggetruneforgelegendaryupgradecost) |  |  |
| ❔ | [C_LegendaryCrafting.GetRuneforgeModifierInfo](#c_legendarycraftinggetruneforgemodifierinfo) |  |  |
| ❔ | [C_LegendaryCrafting.GetRuneforgeModifiers](#c_legendarycraftinggetruneforgemodifiers) |  |  |
| ❔ | [C_LegendaryCrafting.GetRuneforgePowerInfo](#c_legendarycraftinggetruneforgepowerinfo) |  |  |
| ❔ | [C_LegendaryCrafting.GetRuneforgePowerSlots](#c_legendarycraftinggetruneforgepowerslots) |  |  |
| ❔ | [C_LegendaryCrafting.GetRuneforgePowers](#c_legendarycraftinggetruneforgepowers) |  |  |
| ❔ | [C_LegendaryCrafting.GetRuneforgePowersByClassSpecAndCovenant](#c_legendarycraftinggetruneforgepowersbyclassspecandcovenant) |  |  |
| ❔ | [C_LegendaryCrafting.IsRuneforgeLegendary](#c_legendarycraftingisruneforgelegendary) |  |  |
| ❔ | [C_LegendaryCrafting.IsRuneforgeLegendaryMaxLevel](#c_legendarycraftingisruneforgelegendarymaxlevel) |  |  |
| ❔ | [C_LegendaryCrafting.IsUpgradeItemValidForRuneforgeLegendary](#c_legendarycraftingisupgradeitemvalidforruneforgelegendary) |  |  |
| ❔ | [C_LegendaryCrafting.IsValidRuneforgeBaseItem](#c_legendarycraftingisvalidruneforgebaseitem) |  |  |
| ❔ | [C_LegendaryCrafting.MakeRuneforgeCraftDescription](#c_legendarycraftingmakeruneforgecraftdescription) |  |  |
| ❔ | [C_LegendaryCrafting.UpgradeRuneforgeLegendary](#c_legendarycraftingupgraderuneforgelegendary) |  |  |

### C_LegendaryCrafting.CloseRuneforgeInteraction

`C_LegendaryCrafting.CloseRuneforgeInteraction()`

- Status: ❔ unverified
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.CraftRuneforgeLegendary

`C_LegendaryCrafting.CraftRuneforgeLegendary(description: RuneforgeLegendaryCraftDescription)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgeItemPreviewInfo

`C_LegendaryCrafting.GetRuneforgeItemPreviewInfo(baseItem: ItemLocation, runeforgePowerID: number?, modifiers: number[]?) → info: RuneforgeItemPreviewInfo?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgeLegendaryComponentInfo

`C_LegendaryCrafting.GetRuneforgeLegendaryComponentInfo(runeforgeLegendary: ItemLocation) → componentInfo: RuneforgeLegendaryComponentInfo`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgeLegendaryCost

`C_LegendaryCrafting.GetRuneforgeLegendaryCost(baseItem: ItemLocation) → cost: CurrencyCost[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgeLegendaryCraftSpellID

`C_LegendaryCrafting.GetRuneforgeLegendaryCraftSpellID() → spellID: number`

- Status: ❔ unverified
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgeLegendaryCurrencies

`C_LegendaryCrafting.GetRuneforgeLegendaryCurrencies() → currencies: number[]`

- Status: ❔ unverified
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgeLegendaryUpgradeCost

`C_LegendaryCrafting.GetRuneforgeLegendaryUpgradeCost(runeforgeLegendary: ItemLocation, upgradeItem: ItemLocation) → cost: CurrencyCost[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgeModifierInfo

`C_LegendaryCrafting.GetRuneforgeModifierInfo(baseItem: ItemLocation, powerID: number?, addedModifierIndex: luaIndex, modifiers: number[]) → name: string, description: string[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgeModifiers

`C_LegendaryCrafting.GetRuneforgeModifiers() → modifiedReagentItemIDs: number[]`

- Status: ❔ unverified
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgePowerInfo

`C_LegendaryCrafting.GetRuneforgePowerInfo(runeforgePowerID: number) → power: RuneforgePower`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgePowerSlots

`C_LegendaryCrafting.GetRuneforgePowerSlots(runeforgePowerID: number) → slotNames: cstring[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgePowers

`C_LegendaryCrafting.GetRuneforgePowers(baseItem: ItemLocation?, filter: RuneforgePowerFilter?) → primaryRuneforgePowerIDs: number[], otherRuneforgePowerIDs: number[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.GetRuneforgePowersByClassSpecAndCovenant

`C_LegendaryCrafting.GetRuneforgePowersByClassSpecAndCovenant(classID: number?, specID: number?, covenantID: number?, filter: RuneforgePowerFilter?) → runeforgePowerIDs: number[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.IsRuneforgeLegendary

`C_LegendaryCrafting.IsRuneforgeLegendary(item: ItemLocation) → isRuneforgeLegendary: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.IsRuneforgeLegendaryMaxLevel

`C_LegendaryCrafting.IsRuneforgeLegendaryMaxLevel(runeforgeLegendary: ItemLocation) → isMaxLevel: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.IsUpgradeItemValidForRuneforgeLegendary

`C_LegendaryCrafting.IsUpgradeItemValidForRuneforgeLegendary(runeforgeLegendary: ItemLocation, upgradeItem: ItemLocation) → isValid: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.IsValidRuneforgeBaseItem

`C_LegendaryCrafting.IsValidRuneforgeBaseItem(baseItem: ItemLocation) → isValid: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.MakeRuneforgeCraftDescription

`C_LegendaryCrafting.MakeRuneforgeCraftDescription(baseItem: ItemLocation, runeforgePowerID: number, modifiers: number[]) → description: RuneforgeLegendaryCraftDescription`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

### C_LegendaryCrafting.UpgradeRuneforgeLegendary

`C_LegendaryCrafting.UpgradeRuneforgeLegendary(runeforgeLegendary: ItemLocation, upgradeItem: ItemLocation)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LegendaryCraftingDocumentation.lua`

## Events

### NEW_RUNEFORGE_POWER_ADDED

- Status: ❔ unverified
- Payload: `powerID: number`
- fires synchronously (Blizzard's docs)

### RUNEFORGE_LEGENDARY_CRAFTING_CLOSED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### RUNEFORGE_LEGENDARY_CRAFTING_OPENED

- Status: ❔ unverified
- Payload: `isUpgrade: bool`
- fires synchronously (Blizzard's docs)

### RUNEFORGE_POWER_INFO_UPDATED

- Status: ❔ unverified
- Payload: `powerID: number`
- fires synchronously (Blizzard's docs)
