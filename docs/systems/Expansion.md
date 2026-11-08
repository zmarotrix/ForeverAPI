# Expansion

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [CanUpgradeToCurrentExpansion](#canupgradetocurrentexpansion) | 1 value |  |
| ✅ | [DoesCurrentLocaleSellExpansionLevels](#doescurrentlocalesellexpansionlevels) | 1 value |  |
| ✅ | [GetAccountExpansionLevel](#getaccountexpansionlevel) | 1 value |  |
| ✅ | [GetClientDisplayExpansionLevel](#getclientdisplayexpansionlevel) | 1 value |  |
| ✅ | [GetCreditsDisplayInfo](#getcreditsdisplayinfo) | 1 value |  |
| ✅ | [GetCurrentRegionName](#getcurrentregionname) | 1 value |  |
| ✅ | [GetExpansionDisplayInfo](#getexpansiondisplayinfo) |  |  |
| ✅ | [GetExpansionForLevel](#getexpansionforlevel) |  |  |
| ✅ | [GetExpansionLevel](#getexpansionlevel) | 1 value |  |
| ✅ | [GetExpansionTrialInfo](#getexpansiontrialinfo) | 2 values |  |
| ✅ | [GetMaxLevelForExpansionLevel](#getmaxlevelforexpansionlevel) |  |  |
| ✅ | [GetMaxLevelForLatestExpansion](#getmaxlevelforlatestexpansion) | 1 value |  |
| ✅ | [GetMaxLevelForPlayerExpansion](#getmaxlevelforplayerexpansion) | 1 value |  |
| ✅ | [GetMaximumExpansionLevel](#getmaximumexpansionlevel) | 1 value |  |
| ✅ | [GetMinimumExpansionLevel](#getminimumexpansionlevel) | 1 value |  |
| ✅ | [GetNumExpansions](#getnumexpansions) | 1 value |  |
| ✅ | [GetServerExpansionLevel](#getserverexpansionlevel) | 1 value |  |
| ✅ | [GetUpgradeExpansionLevel](#getupgradeexpansionlevel) | 1 value |  |
| ✅ | [IsDemonHunterAvailable](#isdemonhunteravailable) | 1 value |  |
| ✅ | [IsExpansionTrial](#isexpansiontrial) | 1 value |  |
| ✅ | [IsTrialAccount](#istrialaccount) | 1 value |  |
| ✅ | [IsVeteranTrialAccount](#isveterantrialaccount) | 1 value |  |
| ✅ | [SendSubscriptionInterstitialResponse](#sendsubscriptioninterstitialresponse) |  |  |
| ✅ | [ShouldShowExpansionUpgradeBanner](#shouldshowexpansionupgradebanner) | 1 value |  |

### CanUpgradeToCurrentExpansion

`CanUpgradeToCurrentExpansion() → canUpgradeExpansion: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `ExpansionDocumentation.lua`

### DoesCurrentLocaleSellExpansionLevels

`DoesCurrentLocaleSellExpansionLevels() → regionSellsExpansions: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `ExpansionDocumentation.lua`

### GetAccountExpansionLevel

`GetAccountExpansionLevel() → expansionLevel: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `ExpansionDocumentation.lua`

### GetClientDisplayExpansionLevel

`GetClientDisplayExpansionLevel() → expansionLevel: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `ExpansionDocumentation.lua`

### GetCreditsDisplayInfo

`GetCreditsDisplayInfo() → info: CreditsDisplayInfo[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{[number]=table,[number]=table}`
- Source: client docs `ExpansionDocumentation.lua`

### GetCurrentRegionName

`GetCurrentRegionName() → regionName: cstring`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `string`
- Source: client docs `ExpansionDocumentation.lua`

### GetExpansionDisplayInfo

`GetExpansionDisplayInfo(expansionLevel: number, desiredReleaseType: ReleaseType?) → info: ExpansionDisplayInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ExpansionDocumentation.lua`

### GetExpansionForLevel

`GetExpansionForLevel(playerLevel: number) → expansionLevel: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ExpansionDocumentation.lua`

### GetExpansionLevel

`GetExpansionLevel() → expansionLevel: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `ExpansionDocumentation.lua`

### GetExpansionTrialInfo

`GetExpansionTrialInfo() → isExpansionTrialAccount: bool, expansionTrialRemainingSeconds: time_t?`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `nil`
- Source: client docs `ExpansionDocumentation.lua`

### GetMaxLevelForExpansionLevel

`GetMaxLevelForExpansionLevel(expansionLevel: number) → maxLevel: number`

- Status: ✅ verified (function)
- Blizzard: Maps an expansion level to a maximum character level for that expansion.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ExpansionDocumentation.lua`

### GetMaxLevelForLatestExpansion

`GetMaxLevelForLatestExpansion() → maxLevel: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `ExpansionDocumentation.lua`

### GetMaxLevelForPlayerExpansion

`GetMaxLevelForPlayerExpansion() → maxLevel: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `ExpansionDocumentation.lua`

### GetMaximumExpansionLevel

`GetMaximumExpansionLevel() → expansionLevel: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `ExpansionDocumentation.lua`

### GetMinimumExpansionLevel

`GetMinimumExpansionLevel() → expansionLevel: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `ExpansionDocumentation.lua`

### GetNumExpansions

`GetNumExpansions() → numExpansions: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `ExpansionDocumentation.lua`

### GetServerExpansionLevel

`GetServerExpansionLevel() → serverExpansionLevel: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `ExpansionDocumentation.lua`

### GetUpgradeExpansionLevel

`GetUpgradeExpansionLevel() → upgradeExpansionLevel: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `ExpansionDocumentation.lua`

### IsDemonHunterAvailable

`IsDemonHunterAvailable() → available: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `ExpansionDocumentation.lua`

### IsExpansionTrial

`IsExpansionTrial() → isExpansionTrialAccount: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `ExpansionDocumentation.lua`

### IsTrialAccount

`IsTrialAccount() → isTrialAccount: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `ExpansionDocumentation.lua`

### IsVeteranTrialAccount

`IsVeteranTrialAccount() → isVeteranTrialAccount: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `ExpansionDocumentation.lua`

### SendSubscriptionInterstitialResponse

`SendSubscriptionInterstitialResponse(response: SubscriptionInterstitialResponseType)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ExpansionDocumentation.lua`

### ShouldShowExpansionUpgradeBanner

`ShouldShowExpansionUpgradeBanner() → showUpgradeBanner: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `ExpansionDocumentation.lua`

## Events

### MAX_EXPANSION_LEVEL_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### MIN_EXPANSION_LEVEL_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SHOW_SUBSCRIPTION_INTERSTITIAL

- Status: ✅ verified
- Payload: `type: SubscriptionInterstitialType`
- fires synchronously (Blizzard's docs)

## Types

### CreditsDisplayInfo

- Structure
  - `isDefault`: bool
  - `creditsFileID`: number
  - `keyArt`: string
  - `background`: string
  - `name`: string
  - `logo`: fileID
  - `soundKit`: number?

### ExpansionDisplayInfo

- Structure
  - `logo`: fileID
  - `banner`: textureAtlas
  - `features`: ExpansionDisplayInfoFeature[]
  - `highResBackgroundID`: fileID
  - `lowResBackgroundID`: fileID
  - `textureKit`: textureKit
  - `glueAmbianceSoundKit`: number?
  - `glueMusicSoundKit`: number?
  - `glueCreditsSoundKit`: number?

### ExpansionDisplayInfoFeature

- Structure
  - `icon`: fileID
  - `text`: cstring

### SubscriptionInterstitialResponseType

- Enumeration — ✅ verified
  - `Clicked` = 0
  - `Closed` = 1
  - `WebRedirect` = 2

### SubscriptionInterstitialType

- Enumeration — ✅ verified
  - `Standard` = 0
  - `LeftNpeArea` = 1
  - `MaxLevel` = 2
  - `SubscriptionPeriod` = 3
