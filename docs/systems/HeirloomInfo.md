# HeirloomInfo

Namespace: `C_HeirloomInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_HeirloomInfo.AreAllCollectionFiltersChecked](#c_heirloominfoareallcollectionfilterschecked) |  |  |
| ❔ | [C_HeirloomInfo.AreAllSourceFiltersChecked](#c_heirloominfoareallsourcefilterschecked) |  |  |
| ❔ | [C_HeirloomInfo.HeirloomsAvailable](#c_heirloominfoheirloomsavailable) |  |  |
| ❔ | [C_HeirloomInfo.IsHeirloomSourceValid](#c_heirloominfoisheirloomsourcevalid) |  |  |
| ❔ | [C_HeirloomInfo.IsUsingDefaultFilters](#c_heirloominfoisusingdefaultfilters) |  |  |
| ❔ | [C_HeirloomInfo.SetAllCollectionFilters](#c_heirloominfosetallcollectionfilters) |  |  |
| ❔ | [C_HeirloomInfo.SetAllSourceFilters](#c_heirloominfosetallsourcefilters) |  |  |
| ❔ | [C_HeirloomInfo.SetDefaultFilters](#c_heirloominfosetdefaultfilters) |  |  |

### C_HeirloomInfo.AreAllCollectionFiltersChecked

`C_HeirloomInfo.AreAllCollectionFiltersChecked() → areAllCollectionFiltersChecked: bool`

- Status: ❔ unverified
- Source: client docs `HeirloomInfoDocumentation.lua`

### C_HeirloomInfo.AreAllSourceFiltersChecked

`C_HeirloomInfo.AreAllSourceFiltersChecked() → areAllSourceFiltersChecked: bool`

- Status: ❔ unverified
- Source: client docs `HeirloomInfoDocumentation.lua`

### C_HeirloomInfo.HeirloomsAvailable

`C_HeirloomInfo.HeirloomsAvailable() → areHeirloomsAvailable: bool`

- Status: ❔ unverified
- Source: client docs `HeirloomInfoDocumentation.lua`

### C_HeirloomInfo.IsHeirloomSourceValid

`C_HeirloomInfo.IsHeirloomSourceValid(source: luaIndex) → isHeirloomSourceValid: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HeirloomInfoDocumentation.lua`

### C_HeirloomInfo.IsUsingDefaultFilters

`C_HeirloomInfo.IsUsingDefaultFilters() → isUsingDefaultFilters: bool`

- Status: ❔ unverified
- Source: client docs `HeirloomInfoDocumentation.lua`

### C_HeirloomInfo.SetAllCollectionFilters

`C_HeirloomInfo.SetAllCollectionFilters(checked: bool)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HeirloomInfoDocumentation.lua`

### C_HeirloomInfo.SetAllSourceFilters

`C_HeirloomInfo.SetAllSourceFilters(checked: bool)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `HeirloomInfoDocumentation.lua`

### C_HeirloomInfo.SetDefaultFilters

`C_HeirloomInfo.SetDefaultFilters()`

- Status: ❔ unverified
- Source: client docs `HeirloomInfoDocumentation.lua`

## Events

### HEIRLOOMS_UPDATED

- Status: ❔ unverified
- Payload: `itemID: number?`, `updateReason: cstring?`, `hideUntilLearned: bool?`
- fires synchronously (Blizzard's docs)
- unique event (Blizzard's docs)

### HEIRLOOM_UPGRADE_TARGETING_CHANGED

- Status: ❔ unverified
- Payload: `pendingHeirloomUpgradeSpellcast: bool`
- fires synchronously (Blizzard's docs)
