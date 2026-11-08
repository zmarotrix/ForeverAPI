# CurrencyConstants

## Types

### AccountCurrencyTransferResult

- Enumeration — ❔ unverified
  - `Success` = 0
  - `InvalidCharacter` = 1
  - `CharacterLoggedIn` = 2
  - `InsufficientCurrency` = 3
  - `MaxQuantity` = 4
  - `InvalidCurrency` = 5
  - `NoValidSourceCharacter` = 6
  - `ServerError` = 7
  - `CannotUseCurrency` = 8
  - `TransactionInProgress` = 9
  - `CurrencyTransferDisabled` = 10

### CurrencyConsts

- Constants — ❔ unverified
  - `PLAYER_CURRENCY_CLIENT_FLAGS` = Enum.PlayerCurrencyFlagsDbFlags.InBackpack + Enum.PlayerCurrencyFlagsDbFlags.UnusedInUI
  - `MAX_CURRENCY_QUANTITY` = 100000000
  - `CONQUEST_ARENA_AND_BG_META_CURRENCY_ID` = 483
  - `CONQUEST_RATED_BG_META_CURRENCY_ID` = 484
  - `CONQUEST_ASHRAN_META_CURRENCY_ID` = 692
  - `ACCOUNT_WIDE_HONOR_CURRENCY_ID` = 1585
  - `ACCOUNT_WIDE_HONOR_LEVEL_CURRENCY_ID` = 1586
  - `CONQUEST_CURRENCY_ID` = 1602
  - `CONQUEST_POINTS_CURRENCY_ID` = 390
  - `CONQUEST_ARENA_META_CURRENCY_ID` = 483
  - `CONQUEST_BG_META_CURRENCY_ID` = 484
  - `HONOR_CURRENCY_ID` = 1792
  - `CLASSIC_HONOR_CURRENCY_ID` = 1901
  - `ARTIFACT_KNOWLEDGE_CURRENCY_ID` = 1171
  - `WAR_RESOURCES_CURRENCY_ID` = 1560
  - `ECHOES_OF_NYALOTHA_CURRENCY_ID` = 1803
  - `DRAGON_ISLES_SUPPLIES_CURRENCY_ID` = 2003
  - `QUESTIONMARK_INV_ICON` = 134400
  - `PVP_CURRENCY_CONQUEST_ALLIANCE_INV_ICON` = 463448
  - `PVP_CURRENCY_CONQUEST_HORDE_INV_ICON` = 463449
  - `PVP_CURRENCY_HONOR_ALLIANCE_INV_ICON` = 463450
  - `PVP_CURRENCY_HONOR_HORDE_INV_ICON` = 463451
  - `CURRENCY_ID_RENOWN` = 1822
  - `CURRENCY_ID_RENOWN_KYRIAN` = 1829
  - `CURRENCY_ID_RENOWN_VENTHYR` = 1830
  - `CURRENCY_ID_RENOWN_NIGHT_FAE` = 1831
  - `CURRENCY_ID_RENOWN_NECROLORD` = 1832
  - `CURRENCY_ID_WILLING_SOUL` = 1810
  - `CURRENCY_ID_RESERVOIR_ANIMA` = 1813
  - `CURRENCY_ID_PERKS_PROGRAM_DISPLAY_INFO` = 2032
  - `CURRENCY_ID_RENOWN_PVP_RANK` = 3473
  - `CURRENCY_ID_RENOWN_LEGACY` = 3485
  - `IMMEDIATE_CURRENCY_WALLET_ITEM_ID` = 276637
  - `CURRENCY_WALLET_TYPE_WOWMONEY` = 0

### CurrencyConversionResult

- Enumeration — ❔ unverified
  - `NoConversion` = 0
  - `Conversion` = 1
  - `SkippedAccountCurrency` = 2

### CurrencyFilterType

- Enumeration — ❔ unverified
  - `None` = 0
  - `DiscoveredOnly` = 1
  - `DiscoveredAndAllAccountTransferable` = 2

### CurrencyFlags

- Enumeration — ❔ unverified
  - `CurrencyTradable` = 1
  - `CurrencyAppearsInLootWindow` = 2
  - `CurrencyComputedWeeklyMaximum` = 4
  - `Currency_100_Scaler` = 8
  - `CurrencyNoLowLevelDrop` = 16
  - `CurrencyIgnoreMaxQtyOnLoad` = 32
  - `CurrencyLogOnWorldChange` = 64
  - `CurrencyTrackQuantity` = 128
  - `CurrencyResetTrackedQuantity` = 256
  - `CurrencyUpdateVersionIgnoreMax` = 512
  - `CurrencySuppressChatMessageOnVersionChange` = 1024
  - `CurrencySingleDropInLoot` = 2048
  - `CurrencyHasWeeklyCatchup` = 4096
  - `CurrencyDoNotCompressChat` = 8192
  - `CurrencyDoNotLogAcquisitionToBi` = 16384
  - `CurrencyNoRaidDrop` = 32768
  - `CurrencyNotPersistent` = 65536
  - `CurrencyDeprecated` = 131072
  - `CurrencyDynamicMaximum` = 262144
  - `CurrencySuppressChatMessages` = 524288
  - `CurrencyDoNotToast` = 1048576
  - `CurrencyDestroyExtraOnLoot` = 2097152
  - `CurrencyDontShowTotalInTooltip` = 4194304
  - `CurrencyDontCoalesceInLootWindow` = 8388608
  - `CurrencyAccountWide` = 16777216
  - `CurrencyAllowOverflowMailer` = 33554432
  - `CurrencyHideAsReward` = 67108864
  - `CurrencyHasWarmodeBonus` = 134217728
  - `CurrencyIsAllianceOnly` = 268435456
  - `CurrencyIsHordeOnly` = 536870912
  - `CurrencyLimitWarmodeBonusOncePerTooltip` = 1073741824
  - `CurrencyUsesLedgerBalance` = 2147483648

### CurrencyFlagsB

- Enumeration — ❔ unverified
  - `CurrencyBUseTotalEarnedForEarned` = 1
  - `CurrencyBShowQuestXPGainInTooltip` = 2
  - `CurrencyBNoNotificationMailOnOfflineProgress` = 4
  - `CurrencyBBattlenetVirtualCurrency` = 8
  - `FutureCurrencyFlag` = 16
  - `CurrencyBDontDisplayIfZero` = 32
  - `CurrencyBScaleMaxQuantityBySeasonWeeks` = 64
  - `CurrencyBScaleMaxQuantityByWeeksSinceStart` = 128
  - `CurrencyBForceMaxQuantityOnConversion` = 256
  - `CurrencyBUnearnableBeforeMaxQuantityStart` = 512
  - `CurrencyBAllowReductionByResourcefulness` = 1024
  - `CurrencyBNoBonusXP` = 2048

### CurrencyGainFlags

- Enumeration — ❔ unverified
  - `None` = 0
  - `BonusAward` = 1
  - `DroppedFromDeath` = 2
  - `FromAccountServer` = 4
  - `Autotracking` = 8

### CurrencyTokenCategoryFlags

- Enumeration — ❔ unverified
  - `FlagSortLast` = 1
  - `FlagPlayerItemAssignment` = 2
  - `Hidden` = 4
  - `Virtual` = 8
  - `StartsCollapsed` = 16

### CurrencyWeeksFromStartOption

- Enumeration — ❔ unverified
  - `DebugLogging` = 1
  - `IgnoreTimeBeforeStart` = 2

### LinkedCurrencyFlags

- Enumeration — ❔ unverified
  - `IgnoreAdd` = 1
  - `IgnoreSubtract` = 2
  - `SuppressChatLog` = 4
  - `AddIgnoresMax` = 8

### PlayerCurrencyFlags

- Enumeration — ❔ unverified
  - `Incremented` = 1
  - `Loading` = 2

### PlayerCurrencyFlagsDbFlags

- Enumeration — ❔ unverified
  - `IgnoreMaxQtyOnload` = 1
  - `Reuse1` = 2
  - `InBackpack` = 4
  - `UnusedInUI` = 8
  - `Reuse2` = 16
