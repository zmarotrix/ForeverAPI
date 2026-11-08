# LootConstants_Mainline

## Types

### LootConsts_Camelot

- Constants — ⛔ in Blizzard's docs, not in game
  - `MasterLootQualityThreshold` = 4

### LootRollDisabledReason

- Enumeration — ✅ verified
  - `None` = 0
  - `NotAllowed` = 1
  - `UniqueRestriction` = 2
  - `NotDisenchantable` = 3
  - `InsufficientEnchantSkill` = 4
  - `GreedOnly` = 5
  - `HasBetterExactItem` = 6
  - `MissingProfession` = 7

### LootRollType

- Enumeration — ✅ verified
  - `Pass` = 0
  - `Need` = 1
  - `Greed` = 2
  - `Disenchant` = 3
  - `Transmog` = 4
