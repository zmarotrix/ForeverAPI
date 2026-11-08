# ProfessionConstants

## Types

### CraftingOrderDuration

- Enumeration — ✅ verified
  - `Short` = 0
  - `Medium` = 1
  - `Long` = 2

### CraftingOrderFlags

- Enumeration — ✅ verified
  - `None` = 0
  - `IsRecraft` = 1
  - `HasNoneReagents` = 2
  - `HasSomeReagents` = 4
  - `HasAllReagents` = 8
  - `IsFulfillable` = 16

### CraftingOrderItemFlags

- Enumeration — ✅ verified
  - `None` = 0
  - `NpcProvided` = 1
  - `HasEnchantmentData` = 2

### CraftingOrderItemType

- Enumeration — ✅ verified
  - `Item` = 0
  - `Recraft` = 1
  - `CraftedResult` = 2
  - `RemoveReagent` = 3
  - `Deprecated` = 4
  - `Currency` = 5

### CraftingOrderReagentSource

- Enumeration — ✅ verified
  - `Any` = 0
  - `Customer` = 1
  - `Crafter` = 2
  - `None` = 3

### CraftingOrderResult

- Enumeration — ✅ verified
  - `Ok` = 0
  - `Aborted` = 1
  - `AlreadyClaimed` = 2
  - `AlreadyCrafted` = 3
  - `CannotBeOrdered` = 4
  - `CannotCancel` = 5
  - `CannotClaim` = 6
  - `CannotClaimOwnOrder` = 7
  - `CannotCraft` = 8
  - `CannotCreate` = 9
  - `CannotFulfill` = 10
  - `CannotRecraft` = 11
  - `CannotReject` = 12
  - `CannotRelease` = 13
  - `CrafterIsIgnored` = 14
  - `DatabaseError` = 15
  - `Expired` = 16
  - `Locked` = 17
  - `InvalidDuration` = 18
  - `InvalidMinQuality` = 19
  - `InvalidNotes` = 20
  - `InvalidReagent` = 21
  - `InvalidRealm` = 22
  - `InvalidRecipe` = 23
  - `InvalidRecraftItem` = 24
  - `InvalidSort` = 25
  - `InvalidTarget` = 26
  - `InvalidType` = 27
  - `MaxOrdersReached` = 28
  - `MissingCraftingTable` = 29
  - `MissingCurrency` = 30
  - `MissingItem` = 31
  - `MissingNpc` = 32
  - `MissingOrder` = 33
  - `MissingRecraftItem` = 34
  - `NoAccountItems` = 35
  - `NotClaimed` = 36
  - `NotCrafted` = 37
  - `NotInGuild` = 38
  - `NotYetImplemented` = 39
  - `OutOfPublicOrderCapacity` = 40
  - `ServerIsNotAvailable` = 41
  - `ThrottleViolation` = 42
  - `TargetCannotCraft` = 43
  - `TargetLocked` = 44
  - `Timeout` = 45
  - `TooManyCurrencies` = 46
  - `TooManyItems` = 47
  - `WrongVersion` = 48

### CraftingOrderSortType

- Enumeration — ✅ verified
  - `ItemName` = 0
  - `AveTip` = 1
  - `MaxTip` = 2
  - `Quantity` = 3
  - `Reagents` = 4
  - `Tip` = 5
  - `TimeRemaining` = 6
  - `Status` = 7

### CraftingOrderState

- Enumeration — ✅ verified
  - `None` = 0
  - `Creating` = 1
  - `Created` = 2
  - `Claiming` = 3
  - `Claimed` = 4
  - `Rejecting` = 5
  - `Rejected` = 6
  - `Releasing` = 7
  - `Crafting` = 8
  - `Recrafting` = 9
  - `Fulfilling` = 10
  - `Fulfilled` = 11
  - `Canceling` = 12
  - `Canceled` = 13
  - `Expiring` = 14
  - `Expired` = 15

### CraftingOrderType

- Enumeration — ✅ verified
  - `Public` = 0
  - `Guild` = 1
  - `Personal` = 2
  - `Npc` = 3

### CraftingReagentType

- Enumeration — ✅ verified
  - `Modifying` = 0
  - `Basic` = 1
  - `Finishing` = 2
  - `Automatic` = 3

### ItemRecraftFlags

- Enumeration — ✅ verified
  - `Invalid` = 1

### NpcCraftingOrderSetFlags

- Enumeration — ✅ verified
  - `AllowMultiple` = 1
  - `AllowDuplicate` = 2

### Profession

- Enumeration — ✅ verified
  - `FirstAid` = 0
  - `Blacksmithing` = 1
  - `Leatherworking` = 2
  - `Alchemy` = 3
  - `Herbalism` = 4
  - `Cooking` = 5
  - `Mining` = 6
  - `Tailoring` = 7
  - `Engineering` = 8
  - `Enchanting` = 9
  - `Fishing` = 10
  - `Skinning` = 11
  - `Jewelcrafting` = 12
  - `Inscription` = 13
  - `Archaeology` = 14

### ProfessionActionType

- Enumeration — ✅ verified
  - `Craft` = 0
  - `Gather` = 1

### ProfessionConsts

- Constants — ✅ verified
  - `NUM_PRIMARY_PROFESSIONS` = 2
  - `CLASSIC_PROFESSION_PARENT_TIER_INDEX` = 4
  - `RUNEFORGING_SKILL_LINE_ID` = 960
  - `RUNEFORGING_ROOT_CATEGORY_ID` = 210
  - `MAX_CRAFTING_REAGENT_SLOTS` = 12
  - `CRAFTING_ORDER_CLAIM_DURATION` = 0
  - `PUBLIC_CRAFTING_ORDER_STALE_THRESHOLD` = 0
  - `CRAFTING_ORDER_ITEM_RETENTION` = 30
  - `CRAFTING_ORDER_CURRENCY_WALLET_ITEM_ID` = 262724
- ⚠️ `CRAFTING_ORDER_CLAIM_DURATION`: docs say 0, game has 1800
- ⚠️ `PUBLIC_CRAFTING_ORDER_STALE_THRESHOLD`: docs say 0, game has 14400

### ProfessionEffect

- Enumeration — ✅ verified
  - `Skill` = 0
  - `StatInspiration` = 1
  - `StatResourcefulness` = 2
  - `StatFinesse` = 3
  - `StatDeftness` = 4
  - `StatPerception` = 5
  - `StatCraftingSpeed` = 6
  - `StatMulticraft` = 7
  - `UnlockReagentSlot` = 8
  - `ModInspiration` = 9
  - `ModResourcefulness` = 10
  - `ModFinesse` = 11
  - `ModDeftness` = 12
  - `ModPerception` = 13
  - `ModCraftingSpeed` = 14
  - `ModMulticraft` = 15
  - `ModUnused_1` = 16
  - `ModUnused_2` = 17
  - `ModCraftExtraQuantity` = 18
  - `ModGatherExtraQuantity` = 19
  - `ModCraftCritSize` = 20
  - `ModCraftReductionQuantity` = 21
  - `DecreaseDifficulty` = 22
  - `IncreaseDifficulty` = 23
  - `ModSkillGain` = 24
  - `AccumulateRanksByLabel` = 25
  - `StatIngenuity` = 26
  - `ModConcentration` = 27
  - `Tokenizer` = 28
  - `ModIngenuity` = 29
  - `ConcentrationRefund` = 30

### ProfessionRating

- Enumeration — ✅ verified
  - `Inspiration` = 0
  - `Resourcefulness` = 1
  - `Finesse` = 2
  - `Deftness` = 3
  - `Perception` = 4
  - `CraftingSpeed` = 5
  - `Multicraft` = 6
  - `Ingenuity` = 7
  - `Unused_2` = 8

### ProfessionRatingType

- Enumeration — ✅ verified
  - `Craft` = 0
  - `Gather` = 1

### RcoCloseReason

- Enumeration — ✅ verified
  - `Fulfill` = 0
  - `Expire` = 1
  - `Cancel` = 2
  - `Reject` = 3
  - `GmCancel` = 4
  - `CrafterFulfill` = 5
  - `Invalid` = 6

### SkinningState

- Enumeration — ✅ verified
  - `None` = 0
  - `Reserved` = 1
  - `Skinning` = 2
  - `Looting` = 3
  - `Skinned` = 4
