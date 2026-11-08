# ClassTalents

Namespace: `C_ClassTalents`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ClassTalents.CanChangeTalents](#c_classtalentscanchangetalents) | 3 values |  |
| ✅ | [C_ClassTalents.CanCreateNewConfig](#c_classtalentscancreatenewconfig) | 1 value |  |
| ✅ | [C_ClassTalents.CanEditTalents](#c_classtalentscanedittalents) | 2 values |  |
| ✅ | [C_ClassTalents.CommitConfig](#c_classtalentscommitconfig) |  |  |
| ✅ | [C_ClassTalents.DeleteConfig](#c_classtalentsdeleteconfig) |  |  |
| ✅ | [C_ClassTalents.GetActiveConfigID](#c_classtalentsgetactiveconfigid) | 1 value |  |
| ✅ | [C_ClassTalents.GetActiveHeroTalentSpec](#c_classtalentsgetactiveherotalentspec) | 1 value |  |
| ✅ | [C_ClassTalents.GetConfigIDsBySpecID](#c_classtalentsgetconfigidsbyspecid) | 1 value |  |
| ✅ | [C_ClassTalents.GetHasStarterBuild](#c_classtalentsgethasstarterbuild) | 1 value |  |
| ✅ | [C_ClassTalents.GetHeroTalentSpecsForClassSpec](#c_classtalentsgetherotalentspecsforclassspec) | 0 values |  |
| ✅ | [C_ClassTalents.GetLastSelectedSavedConfigID](#c_classtalentsgetlastselectedsavedconfigid) |  |  |
| ✅ | [C_ClassTalents.GetNextStarterBuildPurchase](#c_classtalentsgetnextstarterbuildpurchase) | 2 values |  |
| ✅ | [C_ClassTalents.GetStarterBuildActive](#c_classtalentsgetstarterbuildactive) | 1 value |  |
| ✅ | [C_ClassTalents.GetTraitTreeForSpec](#c_classtalentsgettraittreeforspec) |  |  |
| ✅ | [C_ClassTalents.HasUnspentHeroTalentPoints](#c_classtalentshasunspentherotalentpoints) | 2 values |  |
| ✅ | [C_ClassTalents.HasUnspentTalentPoints](#c_classtalentshasunspenttalentpoints) | 3 values |  |
| ✅ | [C_ClassTalents.ImportLoadout](#c_classtalentsimportloadout) |  |  |
| ✅ | [C_ClassTalents.InitializeViewLoadout](#c_classtalentsinitializeviewloadout) |  |  |
| ✅ | [C_ClassTalents.IsConfigPopulated](#c_classtalentsisconfigpopulated) |  |  |
| ✅ | [C_ClassTalents.LoadConfig](#c_classtalentsloadconfig) |  |  |
| ✅ | [C_ClassTalents.RenameConfig](#c_classtalentsrenameconfig) |  |  |
| ✅ | [C_ClassTalents.RequestNewConfig](#c_classtalentsrequestnewconfig) |  |  |
| ✅ | [C_ClassTalents.SaveConfig](#c_classtalentssaveconfig) |  |  |
| ✅ | [C_ClassTalents.SetStarterBuildActive](#c_classtalentssetstarterbuildactive) |  |  |
| ✅ | [C_ClassTalents.SetUsesSharedActionBars](#c_classtalentssetusessharedactionbars) |  |  |
| ✅ | [C_ClassTalents.SwitchToLoadoutByIndex](#c_classtalentsswitchtoloadoutbyindex) |  |  |
| ✅ | [C_ClassTalents.SwitchToLoadoutByName](#c_classtalentsswitchtoloadoutbyname) |  |  |
| ✅ | [C_ClassTalents.SwitchToSpecializationByIndex](#c_classtalentsswitchtospecializationbyindex) |  |  |
| ✅ | [C_ClassTalents.SwitchToSpecializationByName](#c_classtalentsswitchtospecializationbyname) |  |  |
| ✅ | [C_ClassTalents.UpdateLastSelectedSavedConfigID](#c_classtalentsupdatelastselectedsavedconfigid) |  |  |
| ✅ | [C_ClassTalents.ViewLoadout](#c_classtalentsviewloadout) |  |  |

### C_ClassTalents.CanChangeTalents

`C_ClassTalents.CanChangeTalents() → canChange: bool, canAdd: bool, changeError: string?`

- Status: ✅ verified (function)
- Blizzard: Returns true only if the player has staged changes and can commit their talents in their current state.
- Called out of combat: returned 3 values: `boolean`, `boolean`, `nil`
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.CanCreateNewConfig

`C_ClassTalents.CanCreateNewConfig() → canCreate: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.CanEditTalents

`C_ClassTalents.CanEditTalents() → canEdit: bool, changeError: cstring`

- Status: ✅ verified (function)
- Blizzard: Returns true if the player could switch talents if they staged a proper loadout.
- Called out of combat: returned 2 values: `boolean`, `string`
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.CommitConfig

`C_ClassTalents.CommitConfig(savedConfigID: number?) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.DeleteConfig

`C_ClassTalents.DeleteConfig(configID: number) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.GetActiveConfigID

`C_ClassTalents.GetActiveConfigID() → activeConfigID: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.GetActiveHeroTalentSpec

`C_ClassTalents.GetActiveHeroTalentSpec() → heroSpecID: number?`

- Status: ✅ verified (function)
- Blizzard: Returns the SubTreeID of the player's active Hero Talent Specialization SubTree.
- `heroSpecID`: SubTreeID of the player's active Hero Talent Specialization or nil if no Specialization is active.
- Called out of combat: returned 1 value: `nil`
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.GetConfigIDsBySpecID

`C_ClassTalents.GetConfigIDsBySpecID(specID: number?) → configIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `table{}`
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.GetHasStarterBuild

`C_ClassTalents.GetHasStarterBuild() → hasStarterBuild: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.GetHeroTalentSpecsForClassSpec

`C_ClassTalents.GetHeroTalentSpecsForClassSpec(configID: number?, classSpecID: number?) → subTreeIDs: number[]?, requiredPlayerLevel: number?`

- Status: ✅ verified (function)
- Blizzard: Returns the SubTreeIDs of the Hero Talent Specializations available to a Class Specialization and config; Returns nothing if none available
- `configID`: If not supplied, defaults to the player's active config
- `classSpecID`: If not supplied, defaults to the player's active spec
- `subTreeIDs`: SubTreeIDs of each Hero Talent Specialization
- `requiredPlayerLevel`: The player level at which one of the Hero Talent Specializations can be activated
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.GetLastSelectedSavedConfigID

`C_ClassTalents.GetLastSelectedSavedConfigID(specID: number) → configID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.GetNextStarterBuildPurchase

`C_ClassTalents.GetNextStarterBuildPurchase() → nodeID: number?, entryID: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 2 values: `nil`, `nil`
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.GetStarterBuildActive

`C_ClassTalents.GetStarterBuildActive() → isActive: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.GetTraitTreeForSpec

`C_ClassTalents.GetTraitTreeForSpec(specID: number) → treeID: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.HasUnspentHeroTalentPoints

`C_ClassTalents.HasUnspentHeroTalentPoints() → hasUnspentPoints: bool, numHeroPoints: number`

- Status: ✅ verified (function)
- Blizzard: Returns whether the player has any unspent talent points in their active hero talent tree. If hasUnspentPoints is true, numHeroPoints will be greater than zero.
- Called out of combat: returned 2 values: `boolean`, `number`
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.HasUnspentTalentPoints

`C_ClassTalents.HasUnspentTalentPoints() → hasUnspentPoints: bool, numClassPoints: number, numSpecPoints: number`

- Status: ✅ verified (function)
- Blizzard: Returns whether the player has any unspent talent points in their class or spec talent trees. If hasUnspentPoints is true, the number of unspent points for at least one of the trees will be greater than zero. Hero talent points are not included by this function.
- Called out of combat: returned 3 values: `boolean`, `number`, `number`
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.ImportLoadout

`C_ClassTalents.ImportLoadout(configID: number, entries: ImportLoadoutEntryInfo[], name: string, importString: string?) → success: bool, importError: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.InitializeViewLoadout

`C_ClassTalents.InitializeViewLoadout(specID: number, level: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.IsConfigPopulated

`C_ClassTalents.IsConfigPopulated(configID: number) → isPopulated: bool`

- Status: ✅ verified (function)
- Blizzard: New configs may or may not be populated and ready to load immediately after creation. Avoid calling for configs intentionally created empty.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.LoadConfig

`C_ClassTalents.LoadConfig(configID: number, autoApply: bool) → result: LoadConfigResult, changeError: string?, newLearnedNodeIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.RenameConfig

`C_ClassTalents.RenameConfig(configID: number, name: string) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.RequestNewConfig

`C_ClassTalents.RequestNewConfig(name: string) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.SaveConfig

`C_ClassTalents.SaveConfig(configID: number) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.SetStarterBuildActive

`C_ClassTalents.SetStarterBuildActive(active: bool) → result: LoadConfigResult`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.SetUsesSharedActionBars

`C_ClassTalents.SetUsesSharedActionBars(configID: number, usesShared: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.SwitchToLoadoutByIndex

`C_ClassTalents.SwitchToLoadoutByIndex(loadoutIndex: number)`

- Status: ✅ verified (function)
- Blizzard: Loads loadout for the current specialization by dropdown index. Indices start at 1.
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.SwitchToLoadoutByName

`C_ClassTalents.SwitchToLoadoutByName(loadoutName: cstring)`

- Status: ✅ verified (function)
- Blizzard: Loads loadout for the current specialization by name. Loads the first one found in the case of duplicate names.
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.SwitchToSpecializationByIndex

`C_ClassTalents.SwitchToSpecializationByIndex(specIndex: number)`

- Status: ✅ verified (function)
- Blizzard: Activates specialization for the current class by index in the order within the Specializations tab. Indices start at 1.
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.SwitchToSpecializationByName

`C_ClassTalents.SwitchToSpecializationByName(specName: cstring)`

- Status: ✅ verified (function)
- Blizzard: Activates specialization for the current class by spec name.
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.UpdateLastSelectedSavedConfigID

`C_ClassTalents.UpdateLastSelectedSavedConfigID(specID: number, configID: number?)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClassTalentsDocumentation.lua`

### C_ClassTalents.ViewLoadout

`C_ClassTalents.ViewLoadout(entries: ImportLoadoutEntryInfo[], importString: string?) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClassTalentsDocumentation.lua`

## Events

### ACTIVE_COMBAT_CONFIG_CHANGED

- Status: ✅ verified
- Payload: `configID: number`
- fires synchronously (Blizzard's docs)

### CLASS_TALENTS_SWITCH_TO_LOADOUT_BY_INDEX

- Status: ⛔ in Blizzard's docs, not in game
- Payload: `loadoutIndex: number`
- CallbackEvent (Blizzard's docs)

### CLASS_TALENTS_SWITCH_TO_LOADOUT_BY_NAME

- Status: ⛔ in Blizzard's docs, not in game
- Payload: `loadoutName: cstring`
- CallbackEvent (Blizzard's docs)

### CLASS_TALENTS_SWITCH_TO_SPECIALIZATION_BY_INDEX

- Status: ⛔ in Blizzard's docs, not in game
- Payload: `specIndex: number`
- CallbackEvent (Blizzard's docs)

### CLASS_TALENTS_SWITCH_TO_SPECIALIZATION_BY_NAME

- Status: ⛔ in Blizzard's docs, not in game
- Payload: `specName: cstring`
- CallbackEvent (Blizzard's docs)

### SELECTED_LOADOUT_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SPECIALIZATION_CHANGE_CAST_FAILED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### STARTER_BUILD_ACTIVATION_FAILED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### ImportLoadoutEntryInfo

- Structure
  - `nodeID`: number
  - `ranksGranted`: number
  - `ranksPurchased`: number
  - `selectionEntryID`: number

### LoadConfigResult

- Enumeration — ✅ verified
  - `Error` = 0
  - `NoChangesNecessary` = 1
  - `LoadInProgress` = 2
  - `Ready` = 3
