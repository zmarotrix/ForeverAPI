# Expansion

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [CanUpgradeToCurrentExpansion](#canupgradetocurrentexpansion) |  |  |
| ❔ | [DoesCurrentLocaleSellExpansionLevels](#doescurrentlocalesellexpansionlevels) |  |  |
| ❔ | [GetAccountExpansionLevel](#getaccountexpansionlevel) |  |  |
| ❔ | [GetClientDisplayExpansionLevel](#getclientdisplayexpansionlevel) |  |  |
| ❔ | [GetCreditsDisplayInfo](#getcreditsdisplayinfo) |  |  |
| ❔ | [GetCurrentRegionName](#getcurrentregionname) |  |  |
| ❔ | [GetExpansionDisplayInfo](#getexpansiondisplayinfo) |  |  |
| ❔ | [GetExpansionForLevel](#getexpansionforlevel) |  |  |
| ❔ | [GetExpansionLevel](#getexpansionlevel) |  |  |
| ❔ | [GetExpansionTrialInfo](#getexpansiontrialinfo) |  |  |
| ❔ | [GetMaxLevelForExpansionLevel](#getmaxlevelforexpansionlevel) |  |  |
| ❔ | [GetMaxLevelForLatestExpansion](#getmaxlevelforlatestexpansion) |  |  |
| ❔ | [GetMaxLevelForPlayerExpansion](#getmaxlevelforplayerexpansion) |  |  |
| ❔ | [GetMaximumExpansionLevel](#getmaximumexpansionlevel) |  |  |
| ❔ | [GetMinimumExpansionLevel](#getminimumexpansionlevel) |  |  |
| ❔ | [GetNumExpansions](#getnumexpansions) |  |  |
| ❔ | [GetServerExpansionLevel](#getserverexpansionlevel) |  |  |
| ❔ | [GetUpgradeExpansionLevel](#getupgradeexpansionlevel) |  |  |
| ❔ | [IsDemonHunterAvailable](#isdemonhunteravailable) |  |  |
| ❔ | [IsExpansionTrial](#isexpansiontrial) |  |  |
| ❔ | [IsTrialAccount](#istrialaccount) |  |  |
| ❔ | [IsVeteranTrialAccount](#isveterantrialaccount) |  |  |
| ❔ | [SendSubscriptionInterstitialResponse](#sendsubscriptioninterstitialresponse) |  |  |
| ❔ | [ShouldShowExpansionUpgradeBanner](#shouldshowexpansionupgradebanner) |  |  |

### CanUpgradeToCurrentExpansion

`CanUpgradeToCurrentExpansion() → canUpgradeExpansion: bool`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

### DoesCurrentLocaleSellExpansionLevels

`DoesCurrentLocaleSellExpansionLevels() → regionSellsExpansions: bool`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

### GetAccountExpansionLevel

`GetAccountExpansionLevel() → expansionLevel: number`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

### GetClientDisplayExpansionLevel

`GetClientDisplayExpansionLevel() → expansionLevel: number`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

### GetCreditsDisplayInfo

`GetCreditsDisplayInfo() → info: CreditsDisplayInfo[]`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

### GetCurrentRegionName

`GetCurrentRegionName() → regionName: cstring`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

### GetExpansionDisplayInfo

`GetExpansionDisplayInfo(expansionLevel: number, desiredReleaseType: ReleaseType?) → info: ExpansionDisplayInfo?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ExpansionDocumentation.lua`

### GetExpansionForLevel

`GetExpansionForLevel(playerLevel: number) → expansionLevel: number`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ExpansionDocumentation.lua`

### GetExpansionLevel

`GetExpansionLevel() → expansionLevel: number`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

### GetExpansionTrialInfo

`GetExpansionTrialInfo() → isExpansionTrialAccount: bool, expansionTrialRemainingSeconds: time_t?`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

### GetMaxLevelForExpansionLevel

`GetMaxLevelForExpansionLevel(expansionLevel: number) → maxLevel: number`

- Status: ❔ unverified
- Blizzard: Maps an expansion level to a maximum character level for that expansion.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ExpansionDocumentation.lua`

### GetMaxLevelForLatestExpansion

`GetMaxLevelForLatestExpansion() → maxLevel: number`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

### GetMaxLevelForPlayerExpansion

`GetMaxLevelForPlayerExpansion() → maxLevel: number`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

### GetMaximumExpansionLevel

`GetMaximumExpansionLevel() → expansionLevel: number`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

### GetMinimumExpansionLevel

`GetMinimumExpansionLevel() → expansionLevel: number`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

### GetNumExpansions

`GetNumExpansions() → numExpansions: number`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

### GetServerExpansionLevel

`GetServerExpansionLevel() → serverExpansionLevel: number`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

### GetUpgradeExpansionLevel

`GetUpgradeExpansionLevel() → upgradeExpansionLevel: number`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

### IsDemonHunterAvailable

`IsDemonHunterAvailable() → available: bool`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

### IsExpansionTrial

`IsExpansionTrial() → isExpansionTrialAccount: bool`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

### IsTrialAccount

`IsTrialAccount() → isTrialAccount: bool`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

### IsVeteranTrialAccount

`IsVeteranTrialAccount() → isVeteranTrialAccount: bool`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

### SendSubscriptionInterstitialResponse

`SendSubscriptionInterstitialResponse(response: SubscriptionInterstitialResponseType)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ExpansionDocumentation.lua`

### ShouldShowExpansionUpgradeBanner

`ShouldShowExpansionUpgradeBanner() → showUpgradeBanner: bool`

- Status: ❔ unverified
- Source: client docs `ExpansionDocumentation.lua`

## Events

### MAX_EXPANSION_LEVEL_UPDATED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### MIN_EXPANSION_LEVEL_UPDATED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### SHOW_SUBSCRIPTION_INTERSTITIAL

- Status: ❔ unverified
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

- Enumeration — ❔ unverified
  - `Clicked` = 0
  - `Closed` = 1
  - `WebRedirect` = 2

### SubscriptionInterstitialType

- Enumeration — ❔ unverified
  - `Standard` = 0
  - `LeftNpeArea` = 1
  - `MaxLevel` = 2
  - `SubscriptionPeriod` = 3
