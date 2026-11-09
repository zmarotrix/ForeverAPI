# SpecializationInfo

Namespace: `C_SpecializationInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_SpecializationInfo.CanPlayerUsePVPTalentUI](#c_specializationinfocanplayerusepvptalentui) | 2 values | 2 values |
| ✅ | [C_SpecializationInfo.CanPlayerUseTalentSpecUI](#c_specializationinfocanplayerusetalentspecui) | 2 values | 2 values |
| ✅ | [C_SpecializationInfo.CanPlayerUseTalentUI](#c_specializationinfocanplayerusetalentui) | 2 values | 2 values |
| ✅ | [C_SpecializationInfo.GetActiveSpecGroup](#c_specializationinfogetactivespecgroup) | 1 value | 1 value |
| ✅ | [C_SpecializationInfo.GetAllClassIDs](#c_specializationinfogetallclassids) | 1 value | 1 value |
| ✅ | [C_SpecializationInfo.GetAllSelectedPvpTalentIDs](#c_specializationinfogetallselectedpvptalentids) | 1 value | 1 value |
| ✅ | [C_SpecializationInfo.GetClassIDFromSpecID](#c_specializationinfogetclassidfromspecid) |  |  |
| ✅ | [C_SpecializationInfo.GetCombatConfigIDForSpecGroup](#c_specializationinfogetcombatconfigidforspecgroup) | 1 value | 1 value |
| ✅ | [C_SpecializationInfo.GetInspectSelectedPvpTalent](#c_specializationinfogetinspectselectedpvptalent) |  |  |
| ✅ | [C_SpecializationInfo.GetInspectSpecialization](#c_specializationinfogetinspectspecialization) | 1 value | 1 value |
| ✅ | [C_SpecializationInfo.GetNumSpecializationsForClassID](#c_specializationinfogetnumspecializationsforclassid) | 1 value | 1 value |
| ✅ | [C_SpecializationInfo.GetPvpTalentAlertStatus](#c_specializationinfogetpvptalentalertstatus) | 2 values | 2 values |
| ✅ | [C_SpecializationInfo.GetPvpTalentInfo](#c_specializationinfogetpvptalentinfo) |  |  |
| ✅ | [C_SpecializationInfo.GetPvpTalentSlotInfo](#c_specializationinfogetpvptalentslotinfo) |  |  |
| ✅ | [C_SpecializationInfo.GetPvpTalentSlotUnlockLevel](#c_specializationinfogetpvptalentslotunlocklevel) |  |  |
| ✅ | [C_SpecializationInfo.GetPvpTalentUnlockLevel](#c_specializationinfogetpvptalentunlocklevel) |  |  |
| ✅ | [C_SpecializationInfo.GetSpecIDs](#c_specializationinfogetspecids) |  |  |
| ✅ | [C_SpecializationInfo.GetSpecialization](#c_specializationinfogetspecialization) | 1 value | 1 value |
| ✅ | [C_SpecializationInfo.GetSpecializationInfo](#c_specializationinfogetspecializationinfo) | 10 values | 10 values |
| ✅ | [C_SpecializationInfo.GetSpecializationMasterySpells](#c_specializationinfogetspecializationmasteryspells) | 1 value | 1 value |
| ✅ | [C_SpecializationInfo.GetSpellsDisplay](#c_specializationinfogetspellsdisplay) |  |  |
| ✅ | [C_SpecializationInfo.GetTalentInfo](#c_specializationinfogettalentinfo) |  |  |
| ✅ | [C_SpecializationInfo.HasPlayerEarnedATalentPoint](#c_specializationinfohasplayerearnedatalentpoint) | 1 value | 1 value |
| ✅ | [C_SpecializationInfo.IsInitialized](#c_specializationinfoisinitialized) | 1 value | 1 value |
| ✅ | [C_SpecializationInfo.IsPvpTalentLocked](#c_specializationinfoispvptalentlocked) |  |  |
| ✅ | [C_SpecializationInfo.IsSpecSelectionEnabled](#c_specializationinfoisspecselectionenabled) | 1 value | 1 value |
| ✅ | [C_SpecializationInfo.MatchesCurrentSpecSet](#c_specializationinfomatchescurrentspecset) |  |  |
| ✅ | [C_SpecializationInfo.SetActiveSpecGroup](#c_specializationinfosetactivespecgroup) |  |  |
| ✅ | [C_SpecializationInfo.SetPetSpecialization](#c_specializationinfosetpetspecialization) |  |  |
| ✅ | [C_SpecializationInfo.SetPvpTalentLocked](#c_specializationinfosetpvptalentlocked) |  |  |
| ✅ | [C_SpecializationInfo.SetSpecialization](#c_specializationinfosetspecialization) |  |  |

### C_SpecializationInfo.CanPlayerUsePVPTalentUI

`C_SpecializationInfo.CanPlayerUsePVPTalentUI() → canUse: bool, failureReason: string`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `string`
- Called in combat: returned 2 values: `boolean`, `string`
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.CanPlayerUseTalentSpecUI

`C_SpecializationInfo.CanPlayerUseTalentSpecUI() → canUse: bool, failureReason: string`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `string`
- Called in combat: returned 2 values: `boolean`, `string`
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.CanPlayerUseTalentUI

`C_SpecializationInfo.CanPlayerUseTalentUI() → canUse: bool, failureReason: string`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `string`
- Called in combat: returned 2 values: `boolean`, `string`
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.GetActiveSpecGroup

`C_SpecializationInfo.GetActiveSpecGroup(isInspect: bool?, isPet: bool?) → groupIndex: luaIndex`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.GetAllClassIDs

`C_SpecializationInfo.GetAllClassIDs() → allClassIDs: number[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number}`
- Called in combat: returned 1 value: `table{[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number,[number]=number}`
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.GetAllSelectedPvpTalentIDs

`C_SpecializationInfo.GetAllSelectedPvpTalentIDs() → selectedPvpTalentIDs: number[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.GetClassIDFromSpecID

`C_SpecializationInfo.GetClassIDFromSpecID(specID: number) → classID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.GetCombatConfigIDForSpecGroup

`C_SpecializationInfo.GetCombatConfigIDForSpecGroup(groupIndex: luaIndex) → configID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.GetInspectSelectedPvpTalent

`C_SpecializationInfo.GetInspectSelectedPvpTalent(inspectedUnit: UnitToken, talentIndex: number) → selectedTalentID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.GetInspectSpecialization

`C_SpecializationInfo.GetInspectSpecialization(unit: UnitToken) → specializationID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret while unit identity is restricted (Blizzard's docs; not checked in game)
- Called out of combat with `player`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.GetNumSpecializationsForClassID

`C_SpecializationInfo.GetNumSpecializationsForClassID(classID: number) → specCount: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `class`: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.GetPvpTalentAlertStatus

`C_SpecializationInfo.GetPvpTalentAlertStatus() → hasUnspentSlot: bool, hasNewTalent: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `boolean`, `boolean`
- Called in combat: returned 2 values: `boolean`, `boolean`
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.GetPvpTalentInfo

`C_SpecializationInfo.GetPvpTalentInfo(talentID: number) → talentInfo: PvpTalentInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.GetPvpTalentSlotInfo

`C_SpecializationInfo.GetPvpTalentSlotInfo(talentIndex: number) → slotInfo: PvpTalentSlotInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.GetPvpTalentSlotUnlockLevel

`C_SpecializationInfo.GetPvpTalentSlotUnlockLevel(talentIndex: number) → requiredLevel: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.GetPvpTalentUnlockLevel

`C_SpecializationInfo.GetPvpTalentUnlockLevel(talentID: number) → requiredLevel: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.GetSpecIDs

`C_SpecializationInfo.GetSpecIDs(specSetID: number) → specIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.GetSpecialization

`C_SpecializationInfo.GetSpecialization(isInspect: bool?, isPet: bool?, specGroupIndex: luaIndex?) → specializationIndex: luaIndex`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.GetSpecializationInfo

`C_SpecializationInfo.GetSpecializationInfo(specializationIndex: luaIndex, isInspect: bool = False, isPet: bool = False, inspectTarget: string?, sex: number?, groupIndex: luaIndex?, classID: number?) → specId: number, name: string?, description: string?, icon: fileID?, role: string?, primaryStat: luaIndex?, pointsSpent: number, background: string?, previewPointsSpent: number, isUnlocked: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 10 values: `number`, `string`, `string`, `number`, `string`, `number`, `number`, `nil`, `number`, `boolean`
- Called in combat: returned 10 values: `number`, `string`, `string`, `number`, `string`, `number`, `number`, `nil`, `number`, `boolean`
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.GetSpecializationMasterySpells

`C_SpecializationInfo.GetSpecializationMasterySpells(specializationIndex: luaIndex, isInspect: bool?, isPet: bool?) → spellIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.GetSpellsDisplay

`C_SpecializationInfo.GetSpellsDisplay(specializationID: number) → spellID: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.GetTalentInfo

`C_SpecializationInfo.GetTalentInfo(query: TalentInfoQuery) → result: TalentInfoResult?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.HasPlayerEarnedATalentPoint

`C_SpecializationInfo.HasPlayerEarnedATalentPoint() → hasEarned: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.IsInitialized

`C_SpecializationInfo.IsInitialized() → isSpecializationDataInitialized: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.IsPvpTalentLocked

`C_SpecializationInfo.IsPvpTalentLocked(talentID: number) → locked: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.IsSpecSelectionEnabled

`C_SpecializationInfo.IsSpecSelectionEnabled(classID: number) → enabled: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `class`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.MatchesCurrentSpecSet

`C_SpecializationInfo.MatchesCurrentSpecSet(specSetID: number) → matches: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.SetActiveSpecGroup

`C_SpecializationInfo.SetActiveSpecGroup(groupIndex: luaIndex)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.SetPetSpecialization

`C_SpecializationInfo.SetPetSpecialization(specIndex: luaIndex, petNumber: number?)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.SetPvpTalentLocked

`C_SpecializationInfo.SetPvpTalentLocked(talentID: number, locked: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpecializationInfoDocumentation.lua`

### C_SpecializationInfo.SetSpecialization

`C_SpecializationInfo.SetSpecialization(specIndex: luaIndex) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpecializationInfoDocumentation.lua`

## Events

### ACTIVE_TALENT_GROUP_CHANGED

- Status: ✅ verified
- Payload: `curr: number`, `prev: number`
- fires synchronously (Blizzard's docs)
- Seen firing 8 times (1 in combat); argument kinds: `n,n`

### CONFIRM_PET_UNLEARN

- Status: ✅ verified
- Payload: `cost: number`
- fires synchronously (Blizzard's docs)

### CONFIRM_TALENT_WIPE

- Status: ✅ verified
- Payload: `cost: number`, `respecType: number`
- fires synchronously (Blizzard's docs)

### PET_SPECIALIZATION_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_LEARN_PVP_TALENT_FAILED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_LEARN_TALENT_FAILED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### PLAYER_PVP_TALENT_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 110 times (2 in combat); argument kinds: ``

### PLAYER_TALENT_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 110 times (1 in combat); argument kinds: ``

### SPEC_INVOLUNTARILY_CHANGED

- Status: ✅ verified
- Payload: `isPet: bool`
- fires synchronously (Blizzard's docs)

### TALENTS_INVOLUNTARILY_RESET

- Status: ✅ verified
- Payload: `isPetTalents: bool`
- fires synchronously (Blizzard's docs)

## Types

### PvpTalentInfo

- Structure
  - `talentID`: number
  - `name`: string
  - `icon`: number
  - `selected`: bool
  - `available`: bool
  - `spellID`: number
  - `unlocked`: bool
  - `known`: bool
  - `grantedByAura`: bool
  - `dependenciesUnmet`: bool
  - `dependenciesUnmetReason`: string?

### PvpTalentSlotInfo

- Structure
  - `enabled`: bool
  - `level`: number
  - `selectedTalentID`: number?
  - `availableTalentIDs`: number[]

### SpecializationInfoOutput

- Structure
  - `specId`: number
  - `name`: string?
  - `description`: string?
  - `icon`: fileID?
  - `role`: string?
  - `primaryStat`: luaIndex?
  - `pointsSpent`: number
  - `background`: string?
  - `previewPointsSpent`: number
  - `isUnlocked`: bool

### SpecializationInfoQuery

- Structure
  - `specializationIndex`: luaIndex
  - `isInspect`: bool
  - `isPet`: bool
  - `inspectTarget`: string?
  - `sex`: number?
  - `groupIndex`: luaIndex?
  - `classID`: number?

### TalentInfoQuery

- Structure
  - `groupIndex`: luaIndex?
  - `isInspect`: bool
  - `tier`: luaIndex?
  - `column`: luaIndex?
  - `target`: UnitToken?
  - `specializationIndex`: luaIndex?
  - `talentIndex`: luaIndex?
  - `isPet`: bool

### TalentInfoResult

- Structure
  - `talentID`: number
  - `name`: string
  - `icon`: fileID
  - `tier`: luaIndex
  - `column`: luaIndex
  - `selected`: bool
  - `available`: bool
  - `spellID`: number
  - `isPVPTalentUnlocked`: bool
  - `known`: bool
  - `grantedByAura`: bool
  - `rank`: luaIndex
  - `maxRank`: luaIndex
  - `meetsPrereq`: bool
  - `previewRank`: luaIndex
  - `meetsPreviewPrereq`: bool
  - `isExceptional`: bool
  - `hasGoldBorder`: bool
