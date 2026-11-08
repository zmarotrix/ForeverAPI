# MajorFactionsUI

Namespace: `C_MajorFactions`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_MajorFactions.GetCurrentRenownLevel](#c_majorfactionsgetcurrentrenownlevel) |  |  |
| ✅ | [C_MajorFactions.GetMajorFactionData](#c_majorfactionsgetmajorfactiondata) |  |  |
| ✅ | [C_MajorFactions.GetMajorFactionIDs](#c_majorfactionsgetmajorfactionids) | 1 value |  |
| ✅ | [C_MajorFactions.GetMajorFactionProgressionInfo](#c_majorfactionsgetmajorfactionprogressioninfo) |  |  |
| ✅ | [C_MajorFactions.GetMajorFactionRenownInfo](#c_majorfactionsgetmajorfactionrenowninfo) |  |  |
| ✅ | [C_MajorFactions.GetRenownLevels](#c_majorfactionsgetrenownlevels) |  |  |
| ✅ | [C_MajorFactions.GetRenownNPCFactionID](#c_majorfactionsgetrenownnpcfactionid) | 1 value |  |
| ✅ | [C_MajorFactions.GetRenownRewardsForLevel](#c_majorfactionsgetrenownrewardsforlevel) |  |  |
| ✅ | [C_MajorFactions.GetTotalReputationForRenownLevel](#c_majorfactionsgettotalreputationforrenownlevel) |  |  |
| ✅ | [C_MajorFactions.HasMaximumRenown](#c_majorfactionshasmaximumrenown) |  |  |
| ✅ | [C_MajorFactions.IsMajorFactionHiddenFromExpansionPage](#c_majorfactionsismajorfactionhiddenfromexpansionpage) |  |  |
| ✅ | [C_MajorFactions.IsWeeklyRenownCapped](#c_majorfactionsisweeklyrenowncapped) |  |  |
| ✅ | [C_MajorFactions.ShouldDisplayMajorFactionAsJourney](#c_majorfactionsshoulddisplaymajorfactionasjourney) |  |  |
| ✅ | [C_MajorFactions.ShouldUseJourneyRewardTrack](#c_majorfactionsshouldusejourneyrewardtrack) |  |  |

### C_MajorFactions.GetCurrentRenownLevel

`C_MajorFactions.GetCurrentRenownLevel(majorFactionID: number) → level: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MajorFactionsDocumentation.lua`

### C_MajorFactions.GetMajorFactionData

`C_MajorFactions.GetMajorFactionData(majorFactionID: number) → data: MajorFactionData?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MajorFactionsDocumentation.lua`

### C_MajorFactions.GetMajorFactionIDs

`C_MajorFactions.GetMajorFactionIDs(expansionID: number?) → majorFactionIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `table{[number]=number,[number]=number}`
- Source: client docs `MajorFactionsDocumentation.lua`

### C_MajorFactions.GetMajorFactionProgressionInfo

`C_MajorFactions.GetMajorFactionProgressionInfo(majorFactionID: number) → data: MajorFactionProgressionInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MajorFactionsDocumentation.lua`

### C_MajorFactions.GetMajorFactionRenownInfo

`C_MajorFactions.GetMajorFactionRenownInfo(majorFactionID: number) → data: MajorFactionRenownInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MajorFactionsDocumentation.lua`

### C_MajorFactions.GetRenownLevels

`C_MajorFactions.GetRenownLevels(majorFactionID: number) → levels: MajorFactionRenownLevelInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MajorFactionsDocumentation.lua`

### C_MajorFactions.GetRenownNPCFactionID

`C_MajorFactions.GetRenownNPCFactionID() → renownNPCFactionID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `MajorFactionsDocumentation.lua`

### C_MajorFactions.GetRenownRewardsForLevel

`C_MajorFactions.GetRenownRewardsForLevel(majorFactionID: number, renownLevel: number) → rewards: MajorFactionRenownRewardInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MajorFactionsDocumentation.lua`

### C_MajorFactions.GetTotalReputationForRenownLevel

`C_MajorFactions.GetTotalReputationForRenownLevel(majorFactionID: number, renownLevel: number) → totalReputation: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MajorFactionsDocumentation.lua`

### C_MajorFactions.HasMaximumRenown

`C_MajorFactions.HasMaximumRenown(majorFactionID: number) → hasMaxRenown: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MajorFactionsDocumentation.lua`

### C_MajorFactions.IsMajorFactionHiddenFromExpansionPage

`C_MajorFactions.IsMajorFactionHiddenFromExpansionPage(majorFactionID: number) → isHidden: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MajorFactionsDocumentation.lua`

### C_MajorFactions.IsWeeklyRenownCapped

`C_MajorFactions.IsWeeklyRenownCapped(majorFactionID: number) → isWeeklyCapped: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MajorFactionsDocumentation.lua`

### C_MajorFactions.ShouldDisplayMajorFactionAsJourney

`C_MajorFactions.ShouldDisplayMajorFactionAsJourney(majorFactionID: number) → shouldDisplayMajorFactionAsJourney: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MajorFactionsDocumentation.lua`

### C_MajorFactions.ShouldUseJourneyRewardTrack

`C_MajorFactions.ShouldUseJourneyRewardTrack(majorFactionID: number) → shouldUseJourneyRewardTrack: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `MajorFactionsDocumentation.lua`

## Events

### MAJOR_FACTION_INTERACTION_ENDED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### MAJOR_FACTION_INTERACTION_STARTED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### MAJOR_FACTION_RENOWN_LEVEL_CHANGED

- Status: ✅ verified
- Payload: `majorFactionID: number`, `newRenownLevel: number`, `oldRenownLevel: number`
- fires synchronously (Blizzard's docs)

### MAJOR_FACTION_UNLOCKED

- Status: ✅ verified
- Payload: `majorFactionID: number`
- fires synchronously (Blizzard's docs)

## Types

### MajorFactionData

- Structure
  - `name`: cstring
  - `description`: cstring
  - `highlights`: RenownHighlightInfo[]
  - `factionID`: number
  - `expansionID`: number
  - `bountySetID`: number
  - `isUnlocked`: bool
  - `useJourneyUnlockToast`: bool
  - `hideRenownLevelUpToast`: bool
  - `unlockDescription`: cstring?
  - `uiPriority`: number
  - `renownLevel`: number
  - `maxLevel`: number
  - `renownReputationEarned`: number
  - `renownLevelThreshold`: number
  - `textureKit`: textureKit
  - `celebrationSoundKit`: number
  - `renownFanfareSoundKitID`: number
  - `factionFontColor`: DBColorExport?
  - `renownTrackLevelEffectID`: number?
  - `playerCompanionID`: number?

### MajorFactionProgressionInfo

- Structure
  - `renownLevel`: number
  - `previousWeekProgressiveMaxLevel`: number
  - `currentWeekProgressiveMaxLevel`: number
  - `maxLevel`: number
  - `renownReputationEarned`: number
  - `renownLevelThreshold`: number
  - `weekNumber`: number

### MajorFactionRenownInfo

- Structure
  - `renownLevel`: number
  - `renownReputationEarned`: number
  - `renownLevelThreshold`: number

### MajorFactionRenownLevelInfo

- Structure
  - `factionID`: number
  - `level`: number
  - `locked`: bool
  - `isMilestone`: bool
  - `isCapstone`: bool

### MajorFactionRenownRewardInfo

- Structure
  - `renownRewardID`: number
  - `uiOrder`: number
  - `isAccountUnlock`: bool
  - `itemID`: number?
  - `spellID`: number?
  - `mountID`: number?
  - `transmogID`: number?
  - `transmogSetID`: number?
  - `titleMaskID`: number?
  - `transmogIllusionSourceID`: number?
  - `icon`: fileID?
  - `name`: cstring?
  - `description`: cstring?
  - `toastDescription`: cstring?
  - `rewardType`: number?
  - `isCollected`: bool?

### RenownHighlightInfo

- Structure
  - `title`: cstring
  - `description`: cstring
  - `level`: number
