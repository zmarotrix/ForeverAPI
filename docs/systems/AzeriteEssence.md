# AzeriteEssence

Namespace: `C_AzeriteEssence`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_AzeriteEssence.ActivateEssence](#c_azeriteessenceactivateessence) |  |  |
| ✅ | [C_AzeriteEssence.CanActivateEssence](#c_azeriteessencecanactivateessence) |  |  |
| ✅ | [C_AzeriteEssence.CanDeactivateEssence](#c_azeriteessencecandeactivateessence) |  |  |
| ✅ | [C_AzeriteEssence.CanOpenUI](#c_azeriteessencecanopenui) | 1 value |  |
| ✅ | [C_AzeriteEssence.ClearPendingActivationEssence](#c_azeriteessenceclearpendingactivationessence) |  |  |
| ✅ | [C_AzeriteEssence.CloseForge](#c_azeriteessencecloseforge) |  |  |
| ✅ | [C_AzeriteEssence.GetEssenceHyperlink](#c_azeriteessencegetessencehyperlink) |  |  |
| ✅ | [C_AzeriteEssence.GetEssenceInfo](#c_azeriteessencegetessenceinfo) |  |  |
| ✅ | [C_AzeriteEssence.GetEssences](#c_azeriteessencegetessences) | 0 values |  |
| ✅ | [C_AzeriteEssence.GetMilestoneEssence](#c_azeriteessencegetmilestoneessence) |  |  |
| ✅ | [C_AzeriteEssence.GetMilestoneInfo](#c_azeriteessencegetmilestoneinfo) |  |  |
| ✅ | [C_AzeriteEssence.GetMilestoneSpell](#c_azeriteessencegetmilestonespell) |  |  |
| ✅ | [C_AzeriteEssence.GetMilestones](#c_azeriteessencegetmilestones) | 0 values |  |
| ✅ | [C_AzeriteEssence.GetNumUnlockedEssences](#c_azeriteessencegetnumunlockedessences) | 1 value |  |
| ✅ | [C_AzeriteEssence.GetNumUsableEssences](#c_azeriteessencegetnumusableessences) | 1 value |  |
| ✅ | [C_AzeriteEssence.GetPendingActivationEssence](#c_azeriteessencegetpendingactivationessence) | 1 value |  |
| ✅ | [C_AzeriteEssence.HasNeverActivatedAnyEssences](#c_azeriteessencehasneveractivatedanyessences) | 1 value |  |
| ✅ | [C_AzeriteEssence.HasPendingActivationEssence](#c_azeriteessencehaspendingactivationessence) | 1 value |  |
| ✅ | [C_AzeriteEssence.IsAtForge](#c_azeriteessenceisatforge) | 1 value |  |
| ✅ | [C_AzeriteEssence.SetPendingActivationEssence](#c_azeriteessencesetpendingactivationessence) |  |  |
| ✅ | [C_AzeriteEssence.UnlockMilestone](#c_azeriteessenceunlockmilestone) |  |  |

### C_AzeriteEssence.ActivateEssence

`C_AzeriteEssence.ActivateEssence(essenceID: number, milestoneID: number)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.CanActivateEssence

`C_AzeriteEssence.CanActivateEssence(essenceID: number, milestoneID: number) → canActivate: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.CanDeactivateEssence

`C_AzeriteEssence.CanDeactivateEssence(milestoneID: number) → canDeactivate: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.CanOpenUI

`C_AzeriteEssence.CanOpenUI() → canOpen: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.ClearPendingActivationEssence

`C_AzeriteEssence.ClearPendingActivationEssence()`

- Status: ✅ verified (function)
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.CloseForge

`C_AzeriteEssence.CloseForge()`

- Status: ✅ verified (function)
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.GetEssenceHyperlink

`C_AzeriteEssence.GetEssenceHyperlink(essenceID: number, rank: number) → link: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.GetEssenceInfo

`C_AzeriteEssence.GetEssenceInfo(essenceID: number) → info: AzeriteEssenceInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.GetEssences

`C_AzeriteEssence.GetEssences() → essences: AzeriteEssenceInfo[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.GetMilestoneEssence

`C_AzeriteEssence.GetMilestoneEssence(milestoneID: number) → essenceID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.GetMilestoneInfo

`C_AzeriteEssence.GetMilestoneInfo(milestoneID: number) → info: AzeriteMilestoneInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.GetMilestoneSpell

`C_AzeriteEssence.GetMilestoneSpell(milestoneID: number) → spellID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.GetMilestones

`C_AzeriteEssence.GetMilestones() → milestones: AzeriteMilestoneInfo[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.GetNumUnlockedEssences

`C_AzeriteEssence.GetNumUnlockedEssences() → numUnlockedEssences: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.GetNumUsableEssences

`C_AzeriteEssence.GetNumUsableEssences() → numUsableEssences: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.GetPendingActivationEssence

`C_AzeriteEssence.GetPendingActivationEssence() → essenceID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.HasNeverActivatedAnyEssences

`C_AzeriteEssence.HasNeverActivatedAnyEssences() → hasNeverActivatedAnyEssences: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.HasPendingActivationEssence

`C_AzeriteEssence.HasPendingActivationEssence() → hasEssence: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.IsAtForge

`C_AzeriteEssence.IsAtForge() → isAtForge: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.SetPendingActivationEssence

`C_AzeriteEssence.SetPendingActivationEssence(essenceID: number)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEssenceDocumentation.lua`

### C_AzeriteEssence.UnlockMilestone

`C_AzeriteEssence.UnlockMilestone(milestoneID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AzeriteEssenceDocumentation.lua`

## Events

### AZERITE_ESSENCE_ACTIVATED

- Status: ✅ verified
- Payload: `slot: AzeriteEssenceSlot`, `essenceID: number`
- fires synchronously (Blizzard's docs)

### AZERITE_ESSENCE_ACTIVATION_FAILED

- Status: ✅ verified
- Payload: `slot: AzeriteEssenceSlot`, `essenceID: number`
- fires synchronously (Blizzard's docs)

### AZERITE_ESSENCE_CHANGED

- Status: ✅ verified
- Payload: `essenceID: number`, `newRank: number`
- fires synchronously (Blizzard's docs)

### AZERITE_ESSENCE_FORGE_CLOSE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### AZERITE_ESSENCE_FORGE_OPEN

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### AZERITE_ESSENCE_MILESTONE_UNLOCKED

- Status: ✅ verified
- Payload: `milestoneID: number`
- fires synchronously (Blizzard's docs)

### AZERITE_ESSENCE_UPDATE

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### PENDING_AZERITE_ESSENCE_CHANGED

- Status: ✅ verified
- Payload: `essenceID: number?`
- fires synchronously (Blizzard's docs)

## Types

### AzeriteEssenceInfo

- Structure
  - `ID`: number
  - `name`: cstring
  - `rank`: number
  - `unlocked`: bool
  - `valid`: bool
  - `icon`: fileID

### AzeriteMilestoneInfo

- Structure
  - `ID`: number
  - `requiredLevel`: number
  - `canUnlock`: bool
  - `unlocked`: bool
  - `rank`: number?
  - `slot`: AzeriteEssenceSlot?
