# DelvesConstants

## Types

### CompanionConfigSlotTypes

- Enumeration — ❔ unverified
  - `Role` = 0
  - `Utility` = 1
  - `Combat` = 2
  - `Flavor` = 3

### CurioRarity

- Enumeration — ❔ unverified
  - `Common` = 1
  - `Uncommon` = 2
  - `Rare` = 3
  - `Epic` = 4
  - `EpicTier2` = 5

### DelveAssistActionData

- Structure
  - `assistedPlayer`: string
  - `mapName`: cstring?
  - `creatureName`: cstring?
  - `receivedSpellID`: number?
  - `assistAction`: AssistActionType

### DelvesConsts

- Constants — ❔ unverified
  - `DELVES_MIN_PLAYER_LEVEL_CONTENT_TUNING_ID` = 2677
  - `DELVES_NORMAL_KEY_CURRENCY_ID` = 3028
  - `DELVES_COMPANION_INFO_SELECTION_CHARACTER_DATA_ELEMENT_ID` = 13
  - `DELVES_COMPANION_TOOLTIP_WIDGET_SET_ID` = 1331
  - `DELVES_COMPANION_BRANN_CREATURE_ID` = 210759
  - `DELVES_COMPANION_VALEERA_CREATURE_ID` = 248567

### PlayerCompanionInfoFlags

- Enumeration — ❔ unverified
  - `IgnoreSeasonInScenarios` = 1

### TieredEntranceConsts

- Constants — ❔ unverified
  - `TIERED_ENTRANCE_TIER_SCORE_VALUE_TIER_LEVEL` = 1
  - `TIERED_ENTRANCE_TIER_SCORE_VALUE_MAP_ID` = 3
  - `TIERED_ENTRANCE_TIER_SCORE_VALUE_PLAYER_CONDITION_ID` = 6
  - `TIERED_ENTRANCE_INFO_WORLD_TIER_DIFFICULTY_CHARACTER_ELEMENT_ID` = 522

### TieredEntranceTierFlag

- Enumeration — ❔ unverified
  - `None` = 0
  - `IsLFG` = 1
  - `DisableTraitSystem` = 2

### TieredEntranceType

- Enumeration — ❔ unverified
  - `Invalid` = 0
  - `Delve` = 1
  - `Sites` = 2
  - `WorldTier` = 3
  - `Lairs` = 4
  - `Placeholder_5` = 5
  - `Placeholder_6` = 6

### WorldTierDifficulty

- Enumeration — ❔ unverified
  - `Normal` = 1
  - `Heroic` = 2
  - `Mythic` = 3
