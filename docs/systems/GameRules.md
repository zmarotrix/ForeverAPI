# GameRules

Namespace: `C_GameRules`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_GameRules.AccountHasSDEnabled](#c_gamerulesaccounthassdenabled) |  |  |
| ✅ | [C_GameRules.AutoConnectToGameModeRealm](#c_gamerulesautoconnecttogamemoderealm) |  |  |
| ✅ | [C_GameRules.DoesGameModeHavePromo](#c_gamerulesdoesgamemodehavepromo) |  |  |
| ✅ | [C_GameRules.GetActiveGameMode](#c_gamerulesgetactivegamemode) | 1 value | 1 value |
| ✅ | [C_GameRules.GetCurrentEventRealmQueues](#c_gamerulesgetcurrenteventrealmqueues) | 1 value | 1 value |
| ✅ | [C_GameRules.GetCurrentGameModeDisplayInfo](#c_gamerulesgetcurrentgamemodedisplayinfo) | 1 value | 1 value |
| ✅ | [C_GameRules.GetCurrentGameModeRecordID](#c_gamerulesgetcurrentgamemoderecordid) | 1 value | 1 value |
| ✅ | [C_GameRules.GetDisplayedGameModeRecordIDAtIndex](#c_gamerulesgetdisplayedgamemoderecordidatindex) | 1 value | 1 value |
| ✅ | [C_GameRules.GetForeverExperiencePreset](#c_gamerulesgetforeverexperiencepreset) | 1 value | 1 value |
| ✅ | [C_GameRules.GetGameModeDisplayInfoByRecordID](#c_gamerulesgetgamemodedisplayinfobyrecordid) |  |  |
| ✅ | [C_GameRules.GetGameModeGlueScreenName](#c_gamerulesgetgamemodegluescreenname) | 1 value | 1 value |
| ✅ | [C_GameRules.GetGameModePromoGlobalString](#c_gamerulesgetgamemodepromoglobalstring) |  |  |
| ✅ | [C_GameRules.GetGameRuleAsFloat](#c_gamerulesgetgameruleasfloat) |  |  |
| ✅ | [C_GameRules.GetGameRuleAsFrameStrata](#c_gamerulesgetgameruleasframestrata) |  |  |
| ✅ | [C_GameRules.GetNumDisplayedGameModes](#c_gamerulesgetnumdisplayedgamemodes) | 1 value | 1 value |
| ✅ | [C_GameRules.IsCharacterlessLoginActive](#c_gamerulesischaracterlessloginactive) | 1 value | 1 value |
| ✅ | [C_GameRules.IsClassAllowedForGameMode](#c_gamerulesisclassallowedforgamemode) | 1 value | 1 value |
| ✅ | [C_GameRules.IsGameModeEnabled](#c_gamerulesisgamemodeenabled) |  |  |
| ✅ | [C_GameRules.IsGameRuleActive](#c_gamerulesisgameruleactive) |  |  |
| ✅ | [C_GameRules.IsHardcoreActive](#c_gamerulesishardcoreactive) | 1 value | 1 value |
| ✅ | [C_GameRules.IsMultiActionBarVisibilityForced](#c_gamerulesismultiactionbarvisibilityforced) | 1 value | 1 value |
| ✅ | [C_GameRules.IsPersonalResourceDisplayEnabled](#c_gamerulesispersonalresourcedisplayenabled) | 1 value | 1 value |
| ✅ | [C_GameRules.IsPlunderstorm](#c_gamerulesisplunderstorm) | 1 value | 1 value |
| ✅ | [C_GameRules.IsSDHDToggleEnabled](#c_gamerulesissdhdtoggleenabled) | 1 value | 1 value |
| ✅ | [C_GameRules.IsSelfFoundAllowed](#c_gamerulesisselffoundallowed) | 1 value | 1 value |
| ✅ | [C_GameRules.IsStandard](#c_gamerulesisstandard) | 1 value | 1 value |
| ✅ | [C_GameRules.IsWoWHack](#c_gamerulesiswowhack) | 1 value | 1 value |
| ✅ | [C_GameRules.SetForeverExperiencePresetPostLogin](#c_gamerulessetforeverexperiencepresetpostlogin) |  |  |
| ✅ | [C_GameRules.SetForeverExperiencePresetPreLogin](#c_gamerulessetforeverexperiencepresetprelogin) |  |  |
| ✅ | [C_GameRules.SetSDHDToggleValue](#c_gamerulessetsdhdtogglevalue) |  |  |

### C_GameRules.AccountHasSDEnabled

`C_GameRules.AccountHasSDEnabled() → isSDEnabled: bool`

- Status: ✅ verified (function)
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.AutoConnectToGameModeRealm

`C_GameRules.AutoConnectToGameModeRealm(gameModeRecordID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.DoesGameModeHavePromo

`C_GameRules.DoesGameModeHavePromo(gameModeRecordID: number) → hasPromo: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.GetActiveGameMode

`C_GameRules.GetActiveGameMode() → gameMode: GameMode`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.GetCurrentEventRealmQueues

`C_GameRules.GetCurrentEventRealmQueues() → eventRealmQueues: EventRealmQueues`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.GetCurrentGameModeDisplayInfo

`C_GameRules.GetCurrentGameModeDisplayInfo() → info: GameModeDisplayInfo?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{characterCreateExtraHeight=number,logoHeight=number,logoShrunkenHeight=number,logoUsesDarkBackdrop=boolean,logoVerticalOffset=number}`
- Called in combat: returned 1 value: `table{characterCreateExtraHeight=number,logoHeight=number,logoShrunkenHeight=number,logoUsesDarkBackdrop=boolean,logoVerticalOffset=number}`
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.GetCurrentGameModeRecordID

`C_GameRules.GetCurrentGameModeRecordID() → gameModeRecordID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.GetDisplayedGameModeRecordIDAtIndex

`C_GameRules.GetDisplayedGameModeRecordIDAtIndex(displayIndex: luaIndex) → gameModeRecordID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.GetForeverExperiencePreset

`C_GameRules.GetForeverExperiencePreset() → preset: ForeverExperiencePreset?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.GetGameModeDisplayInfoByRecordID

`C_GameRules.GetGameModeDisplayInfoByRecordID(gameModeRecordID: number) → info: GameModeDisplayInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.GetGameModeGlueScreenName

`C_GameRules.GetGameModeGlueScreenName() → screenName: cstring`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.GetGameModePromoGlobalString

`C_GameRules.GetGameModePromoGlobalString(gameModeRecordID: number) → promoGlobalString: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.GetGameRuleAsFloat

`C_GameRules.GetGameRuleAsFloat(gameRule: GameRule, decimalPlaces: number = 0) → value: number`

- Status: ✅ verified (function)
- Blizzard: Returns the numeric value specified in the Game Rule, multiplied by 0.1 for every decimal place requested
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.GetGameRuleAsFrameStrata

`C_GameRules.GetGameRuleAsFrameStrata(gameRule: GameRule) → frameStrata: cstring`

- Status: ✅ verified (function)
- Blizzard: Returns the value specified in the Game Rule converted to a frame strata
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.GetNumDisplayedGameModes

`C_GameRules.GetNumDisplayedGameModes() → numDisplayedGameModes: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.IsCharacterlessLoginActive

`C_GameRules.IsCharacterlessLoginActive() → active: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.IsClassAllowedForGameMode

`C_GameRules.IsClassAllowedForGameMode(classID: number) → valid: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `class`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.IsGameModeEnabled

`C_GameRules.IsGameModeEnabled(gameModeRecordID: number) → enabled: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.IsGameRuleActive

`C_GameRules.IsGameRuleActive(gameRule: GameRule) → isActive: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.IsHardcoreActive

`C_GameRules.IsHardcoreActive() → active: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.IsMultiActionBarVisibilityForced

`C_GameRules.IsMultiActionBarVisibilityForced() → valid: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.IsPersonalResourceDisplayEnabled

`C_GameRules.IsPersonalResourceDisplayEnabled() → isPersonalResourceDisplayEnabled: bool`

- Status: ✅ verified (function)
- Blizzard: Checks the game rule as well as nameplateShowSelf
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.IsPlunderstorm

`C_GameRules.IsPlunderstorm() → active: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.IsSDHDToggleEnabled

`C_GameRules.IsSDHDToggleEnabled() → isEnabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.IsSelfFoundAllowed

`C_GameRules.IsSelfFoundAllowed() → active: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.IsStandard

`C_GameRules.IsStandard() → active: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.IsWoWHack

`C_GameRules.IsWoWHack() → active: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.SetForeverExperiencePresetPostLogin

`C_GameRules.SetForeverExperiencePresetPostLogin(preset: ForeverExperiencePreset)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.SetForeverExperiencePresetPreLogin

`C_GameRules.SetForeverExperiencePresetPreLogin(preset: ForeverExperiencePreset)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GameRulesDocumentation.lua`

### C_GameRules.SetSDHDToggleValue

`C_GameRules.SetSDHDToggleValue(setToSD: bool, usageLocation: SdToggleUsageLocationUI)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `GameRulesDocumentation.lua`

## Events

### ACTIVE_GAME_MODE_UPDATED

- Status: ✅ verified
- Payload: `gameMode: GameMode`
- fires synchronously (Blizzard's docs)

### AVAILABLE_GAME_MODES_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### EVENT_REALM_QUEUES_UPDATED

- Status: ✅ verified
- Payload: `eventRealmQueues: EventRealmQueues`
- fires synchronously (Blizzard's docs)

### GAME_MODE_DISPLAY_INFO_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 2 times (0 in combat); argument kinds: ``

### GAME_MODE_DISPLAY_MODE_TOGGLE_DISABLED

- Status: ✅ verified
- Payload: `gameModeRecordID: number`, `disabled: bool`
- fires synchronously (Blizzard's docs)

### GAME_RULES_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 2 times (0 in combat); argument kinds: ``

### SETTINGS_HEADER_TEXT_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### ForeverExperiencePreset

- Enumeration — ✅ verified
  - `Classic` = 0
  - `Enhanced` = 1

### GameModeDisplayInfo

- Structure
  - `logo`: fileID
  - `logoHeight`: number
  - `logoVerticalOffset`: number
  - `logoShrunkenHeight`: number
  - `logoUsesDarkBackdrop`: bool
  - `characterCreateExtraHeight`: number
  - `characterCreateOuterBorder`: fileID

### SdToggleUsageLocationUI

- Enumeration — ✅ verified
  - `BeforeLogin` = 0
  - `CharacterCreation` = 1
  - `BarberShop` = 2
  - `OptionsMenu` = 3
