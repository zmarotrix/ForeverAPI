# TradeSkillUITypes

## Types

### CraftingCurrencyResultData

- Structure
  - `currencyID`: number
  - `quantity`: number
  - `operationID`: number
  - `firstCraftReward`: bool
  - `showCurrencyText`: bool

### CraftingItemResultData

- Structure
  - `resourcesReturned`: CraftingResourceReturnInfo[]?
  - `craftingQuality`: number?
  - `qualityProgress`: number
  - `itemID`: number
  - `itemGUID`: WOWGUID
  - `quantity`: number
  - `hyperlink`: string
  - `isCrit`: bool
  - `critBonusSkill`: number
  - `recraftable`: bool
  - `bonusCraft`: bool
  - `multicraft`: number
  - `operationID`: number
  - `firstCraftReward`: bool
  - `isEnchant`: bool
  - `hasIngenuityProc`: bool
  - `concentrationCurrencyID`: number
  - `concentrationSpent`: number
  - `ingenuityRefund`: number

### CraftingItemSlotModification

- Structure
  - `dataSlotIndex`: luaIndex
  - `reagent`: CraftingReagent

### CraftingOperationBonusStatInfo

- Structure
  - `bonusStatName`: string
  - `bonusStatValue`: number
  - `ratingDescription`: string
  - `ratingPct`: number
  - `bonusRatingPct`: number

### CraftingOperationInfo

- Structure
  - `recipeID`: number
  - `baseDifficulty`: number
  - `bonusDifficulty`: number
  - `baseSkill`: number
  - `bonusSkill`: number
  - `isQualityCraft`: bool
  - `quality`: number
  - `craftingQuality`: number
  - `craftingQualityID`: number
  - `craftingDataID`: number
  - `lowerSkillThreshold`: number
  - `upperSkillTreshold`: number
  - `guaranteedCraftingQualityID`: number
  - `bonusStats`: CraftingOperationBonusStatInfo[]
  - `concentrationCurrencyID`: number
  - `concentrationCost`: number
  - `ingenuityRefund`: number

### CraftingQualityInfo

- Structure
  - `quality`: number
  - `icon`: textureAtlas
  - `iconSmall`: textureAtlas
  - `iconInventory`: textureAtlas
  - `iconMixed`: textureAtlas
  - `iconAppear`: textureAtlas
  - `iconDissolve`: textureAtlas
  - `barFill`: textureAtlas
  - `barBackground`: textureAtlas
  - `barBackgroundCap`: textureAtlas
  - `barHighlight`: textureAtlas
  - `iconChat`: textureAtlas
  - `iconQuestObjective`: textureAtlas

### CraftingReagent

- Structure
  - `itemID`: number?
  - `currencyID`: number?

### CraftingReagentInfo

- Structure
  - `reagent`: CraftingReagent
  - `dataSlotIndex`: luaIndex
  - `quantity`: number

### CraftingReagentItemFlag

- Enumeration — ❔ unverified
  - `TooltipShowsAsStatModifications` = 1

### CraftingReagentSlotInfo

- Structure
  - `mcrSlotID`: number
  - `requiredSkillRank`: number
  - `slotText`: cstring?

### CraftingReagentSlotSchematic

- Structure
  - `reagents`: CraftingReagent[]
  - `reagentType`: CraftingReagentType
  - `variableQuantities`: CraftingVariableQuantities[]
  - `quantityRequired`: number
  - `slotInfo`: CraftingReagentSlotInfo?
  - `dataSlotType`: TradeskillSlotDataType
  - `dataSlotIndex`: luaIndex
  - `slotIndex`: luaIndex
  - `orderSource`: CraftingOrderReagentSource?
  - `required`: bool
  - `hiddenInCraftingForm`: bool

### CraftingRecipeOutputInfo

- Structure
  - `icon`: number
  - `hyperlink`: cstring?
  - `itemID`: number?

### CraftingRecipeRequirement

- Structure
  - `name`: cstring
  - `met`: bool
  - `type`: RecipeRequirementType

### CraftingRecipeSchematic

- Structure
  - `recipeID`: number
  - `icon`: number
  - `quantityMin`: number
  - `quantityMax`: number
  - `name`: cstring
  - `recipeType`: TradeskillRecipeType
  - `productQuality`: number?
  - `outputItemID`: number?
  - `reagentSlotSchematics`: CraftingReagentSlotSchematic[]
  - `isRecraft`: bool
  - `hasCraftingOperationInfo`: bool

### CraftingRecipeSkillLineInfo

- Structure
  - `professionSkillLineID`: number
  - `expansionSkillLineID`: number

### CraftingResourceReturnInfo

- Structure
  - `reagent`: CraftingReagent
  - `quantity`: number

### CraftingTargetItem

- Structure
  - `itemID`: number
  - `itemGUID`: WOWGUID
  - `hyperlink`: string?
  - `quantity`: number

### CraftingVariableQuantities

- Structure
  - `reagent`: CraftingReagent
  - `quantity`: number

### GatheringOperationBonusStatInfo

- Structure
  - `bonusStatName`: string
  - `bonusStatValue`: number
  - `ratingDescription`: string
  - `ratingPct`: number
  - `bonusRatingPct`: number

### GatheringOperationInfo

- Structure
  - `spellID`: number
  - `maxDifficulty`: number
  - `baseSkill`: number
  - `bonusSkill`: number
  - `bonusStats`: GatheringOperationBonusStatInfo[]

### ProfessionInfo

- Structure
  - `profession`: Profession?
  - `professionID`: number
  - `sourceCounter`: number
  - `professionName`: cstring
  - `expansionName`: cstring
  - `skillLevel`: number
  - `maxSkillLevel`: number
  - `skillModifier`: number
  - `isPrimaryProfession`: bool
  - `parentProfessionID`: number?
  - `parentProfessionName`: cstring?

### RecipeRequirementType

- Enumeration — ❔ unverified
  - `SpellFocus` = 0
  - `Totem` = 1
  - `Area` = 2

### RegularReagentInfo

- Structure
  - `reagent`: CraftingReagent
  - `quantity`: number

### TradeSkillRecipeInfo

- Structure
  - `categoryID`: number
  - `name`: cstring
  - `relativeDifficulty`: TradeskillRelativeDifficulty?
  - `maxTrivialLevel`: number
  - `itemLevel`: number
  - `alternateVerb`: cstring?
  - `numSkillUps`: number
  - `canSkillUp`: bool
  - `firstCraft`: bool
  - `sourceType`: number?
  - `learned`: bool
  - `disabled`: bool
  - `favorite`: bool
  - `supportsQualities`: bool
  - `craftable`: bool
  - `disabledReason`: cstring?
  - `recipeID`: number
  - `skillLineAbilityID`: number
  - `previousRecipeID`: number?
  - `nextRecipeID`: number?
  - `icon`: number?
  - `hyperlink`: cstring?
  - `currentRecipeExperience`: number?
  - `nextLevelRecipeExperience`: number?
  - `unlockedRecipeLevel`: number?
  - `earnedExperience`: number?
  - `supportsCraftingStats`: bool
  - `hasSingleItemOutput`: bool
  - `qualityItemIDs`: number[]?
  - `qualityIlvlBonuses`: number[]?
  - `alwaysUsesLowestQuality`: bool
  - `maxQuality`: number?
  - `qualityIDs`: number[]?
  - `canCreateMultiple`: bool
  - `abilityVerb`: cstring?
  - `abilityAllVerb`: cstring?
  - `isRecraft`: bool
  - `isDummyRecipe`: bool
  - `isGatheringRecipe`: bool
  - `isEnchantingRecipe`: bool
  - `isSalvageRecipe`: bool

### TradeskillOrderDuration

- Enumeration — ❔ unverified
  - `Short` = 1
  - `Medium` = 2
  - `Long` = 3

### TradeskillOrderRecipient

- Enumeration — ❔ unverified
  - `Public` = 1
  - `Guild` = 2
  - `Private` = 3

### TradeskillOrderStatus

- Enumeration — ❔ unverified
  - `Unclaimed` = 1
  - `Started` = 2
  - `Completed` = 3
  - `Expired` = 4

### TradeskillRecipeType

- Enumeration — ❔ unverified
  - `Item` = 1
  - `Salvage` = 2
  - `Enchant` = 3
  - `Gathering` = 4

### TradeskillRelativeDifficulty

- Enumeration — ❔ unverified
  - `Optimal` = 0
  - `Medium` = 1
  - `Easy` = 2
  - `Trivial` = 3

### TradeskillSlotDataType

- Enumeration — ❔ unverified
  - `Reagent` = 1
  - `ModifiedReagent` = 2
  - `Currency` = 3
