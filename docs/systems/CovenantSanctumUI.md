# CovenantSanctumUI

Namespace: `C_CovenantSanctumUI`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_CovenantSanctumUI.CanAccessReservoir](#c_covenantsanctumuicanaccessreservoir) | 1 value | 1 value |
| ✅ | [C_CovenantSanctumUI.CanDepositAnima](#c_covenantsanctumuicandepositanima) | 1 value | 1 value |
| ✅ | [C_CovenantSanctumUI.DepositAnima](#c_covenantsanctumuidepositanima) |  |  |
| ✅ | [C_CovenantSanctumUI.EndInteraction](#c_covenantsanctumuiendinteraction) |  |  |
| ✅ | [C_CovenantSanctumUI.GetAnimaInfo](#c_covenantsanctumuigetanimainfo) | 2 values | 2 values |
| ✅ | [C_CovenantSanctumUI.GetCurrentTalentTreeID](#c_covenantsanctumuigetcurrenttalenttreeid) | 1 value | 1 value |
| ✅ | [C_CovenantSanctumUI.GetFeatures](#c_covenantsanctumuigetfeatures) | 1 value | 1 value |
| ✅ | [C_CovenantSanctumUI.GetRenownLevel](#c_covenantsanctumuigetrenownlevel) | 1 value | 1 value |
| ✅ | [C_CovenantSanctumUI.GetRenownLevels](#c_covenantsanctumuigetrenownlevels) |  |  |
| ✅ | [C_CovenantSanctumUI.GetRenownRewardsForLevel](#c_covenantsanctumuigetrenownrewardsforlevel) |  |  |
| ✅ | [C_CovenantSanctumUI.GetSanctumType](#c_covenantsanctumuigetsanctumtype) | 1 value | 1 value |
| ✅ | [C_CovenantSanctumUI.GetSoulCurrencies](#c_covenantsanctumuigetsoulcurrencies) | 1 value | 1 value |
| ✅ | [C_CovenantSanctumUI.HasMaximumRenown](#c_covenantsanctumuihasmaximumrenown) | 1 value | 1 value |
| ✅ | [C_CovenantSanctumUI.IsPlayerInRenownCatchUpMode](#c_covenantsanctumuiisplayerinrenowncatchupmode) | 1 value | 1 value |
| ✅ | [C_CovenantSanctumUI.IsWeeklyRenownCapped](#c_covenantsanctumuiisweeklyrenowncapped) | 1 value | 1 value |
| ✅ | [C_CovenantSanctumUI.RequestCatchUpState](#c_covenantsanctumuirequestcatchupstate) |  |  |

### C_CovenantSanctumUI.CanAccessReservoir

`C_CovenantSanctumUI.CanAccessReservoir() → canAccess: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `CovenantSanctumDocumentation.lua`

### C_CovenantSanctumUI.CanDepositAnima

`C_CovenantSanctumUI.CanDepositAnima() → canDeposit: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `CovenantSanctumDocumentation.lua`

### C_CovenantSanctumUI.DepositAnima

`C_CovenantSanctumUI.DepositAnima()`

- Status: ✅ verified (function)
- Source: client docs `CovenantSanctumDocumentation.lua`

### C_CovenantSanctumUI.EndInteraction

`C_CovenantSanctumUI.EndInteraction()`

- Status: ✅ verified (function)
- Source: client docs `CovenantSanctumDocumentation.lua`

### C_CovenantSanctumUI.GetAnimaInfo

`C_CovenantSanctumUI.GetAnimaInfo() → currencyID: number, maxDisplayableValue: number`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `number`, `number`
- Called in combat: returned 2 values: `number`, `number`
- Source: client docs `CovenantSanctumDocumentation.lua`

### C_CovenantSanctumUI.GetCurrentTalentTreeID

`C_CovenantSanctumUI.GetCurrentTalentTreeID() → currentTalentTreeID: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `CovenantSanctumDocumentation.lua`

### C_CovenantSanctumUI.GetFeatures

`C_CovenantSanctumUI.GetFeatures() → features: CovenantSanctumFeatureInfo[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `CovenantSanctumDocumentation.lua`

### C_CovenantSanctumUI.GetRenownLevel

`C_CovenantSanctumUI.GetRenownLevel() → level: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `CovenantSanctumDocumentation.lua`

### C_CovenantSanctumUI.GetRenownLevels

`C_CovenantSanctumUI.GetRenownLevels(covenantID: number) → levels: CovenantSanctumRenownLevelInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CovenantSanctumDocumentation.lua`

### C_CovenantSanctumUI.GetRenownRewardsForLevel

`C_CovenantSanctumUI.GetRenownRewardsForLevel(covenantID: number, renownLevel: number) → rewards: CovenantSanctumRenownRewardInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CovenantSanctumDocumentation.lua`

### C_CovenantSanctumUI.GetSanctumType

`C_CovenantSanctumUI.GetSanctumType() → sanctumType: GarrTalentFeatureSubtype?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `CovenantSanctumDocumentation.lua`

### C_CovenantSanctumUI.GetSoulCurrencies

`C_CovenantSanctumUI.GetSoulCurrencies() → currencyIDs: number[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `CovenantSanctumDocumentation.lua`

### C_CovenantSanctumUI.HasMaximumRenown

`C_CovenantSanctumUI.HasMaximumRenown() → hasMaxRenown: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `CovenantSanctumDocumentation.lua`

### C_CovenantSanctumUI.IsPlayerInRenownCatchUpMode

`C_CovenantSanctumUI.IsPlayerInRenownCatchUpMode() → isInCatchUpMode: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `CovenantSanctumDocumentation.lua`

### C_CovenantSanctumUI.IsWeeklyRenownCapped

`C_CovenantSanctumUI.IsWeeklyRenownCapped() → isWeeklyCapped: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `CovenantSanctumDocumentation.lua`

### C_CovenantSanctumUI.RequestCatchUpState

`C_CovenantSanctumUI.RequestCatchUpState()`

- Status: ✅ verified (function)
- Source: client docs `CovenantSanctumDocumentation.lua`

## Events

### COVENANT_RENOWN_CATCH_UP_STATE_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### COVENANT_SANCTUM_RENOWN_LEVEL_CHANGED

- Status: ✅ verified
- Payload: `newRenownLevel: number`, `oldRenownLevel: number`
- fires synchronously (Blizzard's docs)

## Types

### CovenantSanctumFeatureInfo

- Structure
  - `garrTalentTreeID`: number
  - `featureType`: number
  - `uiOrder`: number

### CovenantSanctumRenownLevelInfo

- Structure
  - `level`: number
  - `locked`: bool
  - `isMilestone`: bool
  - `isCapstone`: bool

### CovenantSanctumRenownRewardInfo

- Structure
  - `uiOrder`: number
  - `itemID`: number?
  - `spellID`: number?
  - `mountID`: number?
  - `transmogID`: number?
  - `transmogSetID`: number?
  - `titleMaskID`: number?
  - `garrFollowerID`: number?
  - `transmogIllusionSourceID`: number?
  - `icon`: fileID?
  - `name`: cstring?
  - `description`: cstring?
  - `toastDescription`: cstring?
