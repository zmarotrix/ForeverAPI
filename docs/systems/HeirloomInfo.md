# HeirloomInfo

Namespace: `C_HeirloomInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_HeirloomInfo.AreAllCollectionFiltersChecked](#c_heirloominfoareallcollectionfilterschecked) | 1 value | 1 value |
| ✅ | [C_HeirloomInfo.AreAllSourceFiltersChecked](#c_heirloominfoareallsourcefilterschecked) | 1 value | 1 value |
| ✅ | [C_HeirloomInfo.HeirloomsAvailable](#c_heirloominfoheirloomsavailable) |  |  |
| ✅ | [C_HeirloomInfo.IsHeirloomSourceValid](#c_heirloominfoisheirloomsourcevalid) | 1 value | 1 value |
| ✅ | [C_HeirloomInfo.IsUsingDefaultFilters](#c_heirloominfoisusingdefaultfilters) | 1 value | 1 value |
| ✅ | [C_HeirloomInfo.SetAllCollectionFilters](#c_heirloominfosetallcollectionfilters) |  |  |
| ✅ | [C_HeirloomInfo.SetAllSourceFilters](#c_heirloominfosetallsourcefilters) |  |  |
| ✅ | [C_HeirloomInfo.SetDefaultFilters](#c_heirloominfosetdefaultfilters) |  |  |

### C_HeirloomInfo.AreAllCollectionFiltersChecked

`C_HeirloomInfo.AreAllCollectionFiltersChecked() → areAllCollectionFiltersChecked: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HeirloomInfoDocumentation.lua`

### C_HeirloomInfo.AreAllSourceFiltersChecked

`C_HeirloomInfo.AreAllSourceFiltersChecked() → areAllSourceFiltersChecked: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HeirloomInfoDocumentation.lua`

### C_HeirloomInfo.HeirloomsAvailable

`C_HeirloomInfo.HeirloomsAvailable() → areHeirloomsAvailable: bool`

- Status: ✅ verified (function)
- Source: client docs `HeirloomInfoDocumentation.lua`

### C_HeirloomInfo.IsHeirloomSourceValid

`C_HeirloomInfo.IsHeirloomSourceValid(source: luaIndex) → isHeirloomSourceValid: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:1`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HeirloomInfoDocumentation.lua`

### C_HeirloomInfo.IsUsingDefaultFilters

`C_HeirloomInfo.IsUsingDefaultFilters() → isUsingDefaultFilters: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `HeirloomInfoDocumentation.lua`

### C_HeirloomInfo.SetAllCollectionFilters

`C_HeirloomInfo.SetAllCollectionFilters(checked: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HeirloomInfoDocumentation.lua`

### C_HeirloomInfo.SetAllSourceFilters

`C_HeirloomInfo.SetAllSourceFilters(checked: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HeirloomInfoDocumentation.lua`

### C_HeirloomInfo.SetDefaultFilters

`C_HeirloomInfo.SetDefaultFilters()`

- Status: ✅ verified (function)
- Source: client docs `HeirloomInfoDocumentation.lua`

## Events

### HEIRLOOMS_UPDATED

- Status: ✅ verified
- Payload: `itemID: number?`, `updateReason: cstring?`, `hideUntilLearned: bool?`
- fires synchronously (Blizzard's docs)
- unique event (Blizzard's docs)

### HEIRLOOM_UPGRADE_TARGETING_CHANGED

- Status: ✅ verified
- Payload: `pendingHeirloomUpgradeSpellcast: bool`
- fires synchronously (Blizzard's docs)
