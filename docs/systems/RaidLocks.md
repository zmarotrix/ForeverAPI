# RaidLocks

Namespace: `C_RaidLocks`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_RaidLocks.GetRedirectedDifficultyID](#c_raidlocksgetredirecteddifficultyid) |  |  |
| ✅ | [C_RaidLocks.IsEncounterComplete](#c_raidlocksisencountercomplete) |  |  |
| ✅ | [C_RaidLocks.IsRaidLockExtendFeatureEnabled](#c_raidlocksisraidlockextendfeatureenabled) | 1 value |  |
| ✅ | [C_RaidLocks.IsRaidLockExtendFeatureSupported](#c_raidlocksisraidlockextendfeaturesupported) | 1 value |  |

### C_RaidLocks.GetRedirectedDifficultyID

`C_RaidLocks.GetRedirectedDifficultyID(mapID: number, difficultyID: number) → redirectedDifficultyID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RaidLocksDocumentation.lua`

### C_RaidLocks.IsEncounterComplete

`C_RaidLocks.IsEncounterComplete(mapID: number, encounterID: number, difficultyID: number?) → encounterIsComplete: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RaidLocksDocumentation.lua`

### C_RaidLocks.IsRaidLockExtendFeatureEnabled

`C_RaidLocks.IsRaidLockExtendFeatureEnabled() → raidLockExtendFeatureEnabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `RaidLocksDocumentation.lua`

### C_RaidLocks.IsRaidLockExtendFeatureSupported

`C_RaidLocks.IsRaidLockExtendFeatureSupported() → raidLockExtendFeatureSupported: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `RaidLocksDocumentation.lua`
