# TraitConstants

## Types

### NodeOpFailureReason

- Enumeration — ✅ verified
  - `None` = 0
  - `MissingEdgeConnection` = 1
  - `RequiredForEdge` = 2
  - `MissingRequiredEdge` = 3
  - `HasMutuallyExclusiveEdge` = 4
  - `NotEnoughSourcedCurrencySpent` = 5
  - `NotEnoughCurrencySpent` = 6
  - `NotEnoughGoldSpent` = 7
  - `MissingAchievement` = 8
  - `MissingQuest` = 9
  - `WrongSpec` = 10
  - `WrongSelection` = 11
  - `MaxRank` = 12
  - `DataError` = 13
  - `NotEnoughSourcedCurrency` = 14
  - `NotEnoughCurrency` = 15
  - `NotEnoughGold` = 16
  - `SameSelection` = 17
  - `NodeNotFound` = 18
  - `EntryNotFound` = 19
  - `RequiredForCondition` = 20
  - `WrongTreeID` = 21
  - `LevelTooLow` = 22
  - `TreeFlaggedNoRefund` = 23
  - `NodeNeverPurchasable` = 24
  - `AccountDataNoMatch` = 25
  - `NotEnoughRanksInEntry` = 26

### RespecType

- Enumeration — ✅ verified
  - `Talents` = 0
  - `Glyphs` = 1
  - `SetPrimarySpecialization` = 2
  - `PetTalents` = 3
  - `Legacy` = 4
  - `Specialization` = 5

### SharedStringFlag

- Enumeration — ✅ verified
  - `InternalOnly` = 1

### TraitCombatConfigFlags

- Enumeration — ✅ verified
  - `ActiveForSpec` = 1
  - `StarterBuild` = 2
  - `SharedActionBars` = 4
  - `SecondarySpec` = 8

### TraitCondFlag

- Enumeration — ✅ verified
  - `IsGate` = 1
  - `IsAlwaysMet` = 2
  - `IsSufficient` = 4

### TraitConditionType

- Enumeration — ✅ verified
  - `Available` = 0
  - `Visible` = 1
  - `Granted` = 2
  - `Increased` = 3
  - `DisplayError` = 4
  - `RanksAllowed` = 5

### TraitConfigDbState

- Enumeration — ✅ verified
  - `Ready` = 0
  - `Created` = 1
  - `Removed` = 2
  - `Deleted` = 3

### TraitConfigType

- Enumeration — ✅ verified
  - `Invalid` = 0
  - `Combat` = 1
  - `Profession` = 2
  - `Generic` = 3
  - `CamelotCombat` = 4

### TraitConsts

- Constants — ✅ verified
  - `MAX_COMBAT_TRAIT_CONFIGS` = 40
  - `COMMIT_COMBAT_TRAIT_CONFIG_CHANGES_SPELL_ID` = 384255
  - `INSPECT_TRAIT_CONFIG_ID` = -1
  - `STARTER_BUILD_TRAIT_CONFIG_ID` = -2
  - `VIEW_TRAIT_CONFIG_ID` = -3

### TraitCurrencyFlag

- Enumeration — ✅ verified
  - `ShowQuantityAsSpent` = 1
  - `TraitSourcedShowMax` = 2
  - `UseClassIcon` = 4
  - `UseSpecIcon` = 8

### TraitCurrencyType

- Enumeration — ✅ verified
  - `Gold` = 0
  - `CurrencyTypesBased` = 1
  - `TraitSourced` = 2
  - `TraitSourcedPlayerDataElement` = 3

### TraitDefinitionSubType

- Enumeration — ✅ verified
  - `DragonflightRed` = 0
  - `DragonflightBlue` = 1
  - `DragonflightGreen` = 2
  - `DragonflightBronze` = 3
  - `DragonflightBlack` = 4

### TraitEdgeType

- Enumeration — ✅ verified
  - `VisualOnly` = 0
  - `DeprecatedRankConnection` = 1
  - `SufficientForAvailability` = 2
  - `RequiredForAvailability` = 3
  - `MutuallyExclusive` = 4
  - `DeprecatedSelectionOption` = 5

### TraitEdgeVisualStyle

- Enumeration — ✅ verified
  - `None` = 0
  - `Straight` = 1

### TraitNodeEntryType

- Enumeration — ✅ verified
  - `SpendHex` = 0
  - `SpendSquare` = 1
  - `SpendCircle` = 2
  - `SpendSmallCircle` = 3
  - `DeprecatedSelect` = 4
  - `DragAndDrop` = 5
  - `SpendDiamond` = 6
  - `ProfPath` = 7
  - `ProfPerk` = 8
  - `ProfPathUnlock` = 9
  - `RedButton` = 10
  - `ArmorSet` = 11
  - `SpendInfinite` = 12
  - `SpendCapstoneCircle` = 13
  - `SpendCapstoneSquare` = 14

### TraitNodeFlag

- Enumeration — ✅ verified
  - `ShowMultipleIcons` = 1
  - `NeverPurchasable` = 2
  - `TestPositionLocked` = 4
  - `TestGridPositioned` = 8
  - `ActiveAtFirstRank` = 16
  - `ShowExpandedSelection` = 32
  - `HideMaxRank` = 64
  - `HighestChosenRank` = 128
  - `ShowTierTrack` = 256

### TraitNodeGroupFlag

- Enumeration — ✅ verified
  - `AvailableByDefault` = 1

### TraitNodeType

- Enumeration — ✅ verified
  - `Single` = 0
  - `Tiered` = 1
  - `Selection` = 2
  - `SubTreeSelection` = 3

### TraitPointsOperationType

- Enumeration — ✅ verified
  - `None` = -1
  - `Set` = 0
  - `Multiply` = 1

### TraitSystemFlag

- Enumeration — ✅ verified
  - `AllowMultipleLoadoutsPerTree` = 1
  - `ShowSpendConfirmation` = 2
  - `AllowEditInCombat` = 4
  - `AllowEditInChallengeMode` = 8

### TraitSystemVariationType

- Enumeration — ✅ verified
  - `None` = 0
  - `Spec` = 1

### TraitTreeFlag

- Enumeration — ✅ verified
  - `CannotRefund` = 1
  - `HideSingleRankNumbers` = 2

### TraitVendorResetFailureReason

- Enumeration — ✅ verified
  - `None` = 0
  - `DataError` = 1
  - `ClassPointDeficit` = 2
