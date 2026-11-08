# ProfessionSpecUI

Namespace: `C_ProfSpecs`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ProfSpecs.CanRefundPath](#c_profspecscanrefundpath) |  |  |
| ✅ | [C_ProfSpecs.CanUnlockTab](#c_profspecscanunlocktab) |  |  |
| ✅ | [C_ProfSpecs.GetChildrenForPath](#c_profspecsgetchildrenforpath) |  |  |
| ✅ | [C_ProfSpecs.GetConfigIDForSkillLine](#c_profspecsgetconfigidforskillline) |  |  |
| ✅ | [C_ProfSpecs.GetCurrencyInfoForSkillLine](#c_profspecsgetcurrencyinfoforskillline) |  |  |
| ✅ | [C_ProfSpecs.GetDefaultSpecSkillLine](#c_profspecsgetdefaultspecskillline) | 1 value | 1 value |
| ✅ | [C_ProfSpecs.GetDescriptionForPath](#c_profspecsgetdescriptionforpath) |  |  |
| ✅ | [C_ProfSpecs.GetDescriptionForPerk](#c_profspecsgetdescriptionforperk) |  |  |
| ✅ | [C_ProfSpecs.GetEntryIDForPerk](#c_profspecsgetentryidforperk) |  |  |
| ✅ | [C_ProfSpecs.GetNewSpecReminderProfName](#c_profspecsgetnewspecreminderprofname) | 1 value | 1 value |
| ✅ | [C_ProfSpecs.GetPerksForPath](#c_profspecsgetperksforpath) |  |  |
| ✅ | [C_ProfSpecs.GetRootPathForTab](#c_profspecsgetrootpathfortab) |  |  |
| ✅ | [C_ProfSpecs.GetSourceTextForPath](#c_profspecsgetsourcetextforpath) |  |  |
| ✅ | [C_ProfSpecs.GetSpecTabIDsForSkillLine](#c_profspecsgetspectabidsforskillline) |  |  |
| ✅ | [C_ProfSpecs.GetSpecTabInfo](#c_profspecsgetspectabinfo) | 1 value | 1 value |
| ✅ | [C_ProfSpecs.GetSpendCurrencyForPath](#c_profspecsgetspendcurrencyforpath) |  |  |
| ✅ | [C_ProfSpecs.GetSpendEntryForPath](#c_profspecsgetspendentryforpath) |  |  |
| ✅ | [C_ProfSpecs.GetStateForPath](#c_profspecsgetstateforpath) |  |  |
| ✅ | [C_ProfSpecs.GetStateForPerk](#c_profspecsgetstateforperk) |  |  |
| ✅ | [C_ProfSpecs.GetStateForTab](#c_profspecsgetstatefortab) |  |  |
| ✅ | [C_ProfSpecs.GetTabInfo](#c_profspecsgettabinfo) |  |  |
| ✅ | [C_ProfSpecs.GetUnlockEntryForPath](#c_profspecsgetunlockentryforpath) |  |  |
| ✅ | [C_ProfSpecs.GetUnlockRankForPerk](#c_profspecsgetunlockrankforperk) |  |  |
| ✅ | [C_ProfSpecs.ShouldShowPointsReminder](#c_profspecsshouldshowpointsreminder) | 1 value | 1 value |
| ✅ | [C_ProfSpecs.ShouldShowPointsReminderForSkillLine](#c_profspecsshouldshowpointsreminderforskillline) |  |  |
| ✅ | [C_ProfSpecs.ShouldShowSpecTab](#c_profspecsshouldshowspectab) | 1 value | 1 value |
| ✅ | [C_ProfSpecs.SkillLineHasSpecialization](#c_profspecsskilllinehasspecialization) |  |  |

### C_ProfSpecs.CanRefundPath

`C_ProfSpecs.CanRefundPath(pathID: number, configID: number) → canRefund: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.CanUnlockTab

`C_ProfSpecs.CanUnlockTab(tabTreeID: number, configID: number) → canUnlock: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetChildrenForPath

`C_ProfSpecs.GetChildrenForPath(pathID: number) → childIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetConfigIDForSkillLine

`C_ProfSpecs.GetConfigIDForSkillLine(skillLineID: number) → configID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetCurrencyInfoForSkillLine

`C_ProfSpecs.GetCurrencyInfoForSkillLine(skillLineID: number) → info: SpecializationCurrencyInfo`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetDefaultSpecSkillLine

`C_ProfSpecs.GetDefaultSpecSkillLine() → defaultSpecSkillLine: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetDescriptionForPath

`C_ProfSpecs.GetDescriptionForPath(pathID: number) → description: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetDescriptionForPerk

`C_ProfSpecs.GetDescriptionForPerk(perkID: number) → description: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetEntryIDForPerk

`C_ProfSpecs.GetEntryIDForPerk(perkID: number) → entryID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetNewSpecReminderProfName

`C_ProfSpecs.GetNewSpecReminderProfName() → profName: cstring?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetPerksForPath

`C_ProfSpecs.GetPerksForPath(pathID: number) → perkInfos: SpecPerkInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetRootPathForTab

`C_ProfSpecs.GetRootPathForTab(tabTreeID: number) → rootPathID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetSourceTextForPath

`C_ProfSpecs.GetSourceTextForPath(pathID: number, configID: number) → sourceText: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetSpecTabIDsForSkillLine

`C_ProfSpecs.GetSpecTabIDsForSkillLine(skillLineID: number) → specTabIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetSpecTabInfo

`C_ProfSpecs.GetSpecTabInfo() → specTabInfo: SpecializationTabInfo`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{enabled=boolean}`
- Called in combat: returned 1 value: `table{enabled=boolean}`
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetSpendCurrencyForPath

`C_ProfSpecs.GetSpendCurrencyForPath(pathID: number) → currencyID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetSpendEntryForPath

`C_ProfSpecs.GetSpendEntryForPath(pathID: number) → entryID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetStateForPath

`C_ProfSpecs.GetStateForPath(pathID: number, configID: number) → state: ProfessionsSpecPathState`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetStateForPerk

`C_ProfSpecs.GetStateForPerk(perkID: number, configID: number) → state: ProfessionsSpecPerkState`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetStateForTab

`C_ProfSpecs.GetStateForTab(tabTreeID: number, configID: number) → tabInfo: ProfessionsSpecTabState`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetTabInfo

`C_ProfSpecs.GetTabInfo(tabTreeID: number) → tabInfo: ProfTabInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetUnlockEntryForPath

`C_ProfSpecs.GetUnlockEntryForPath(pathID: number) → entryID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.GetUnlockRankForPerk

`C_ProfSpecs.GetUnlockRankForPerk(perkID: number) → unlockRank: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.ShouldShowPointsReminder

`C_ProfSpecs.ShouldShowPointsReminder() → showReminder: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.ShouldShowPointsReminderForSkillLine

`C_ProfSpecs.ShouldShowPointsReminderForSkillLine(skillLineID: number) → showReminder: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.ShouldShowSpecTab

`C_ProfSpecs.ShouldShowSpecTab() → showSpecTab: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `ProfessionSpecUIDocumentation.lua`

### C_ProfSpecs.SkillLineHasSpecialization

`C_ProfSpecs.SkillLineHasSpecialization(skillLineID: number) → hasSpecialization: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ProfessionSpecUIDocumentation.lua`

## Events

### SKILL_LINE_SPECS_RANKS_CHANGED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### SKILL_LINE_SPECS_UNLOCKED

- Status: ✅ verified
- Payload: `skillLineID: number`, `tradeSkillID: number`
- unique event (Blizzard's docs)
