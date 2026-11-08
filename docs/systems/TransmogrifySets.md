# TransmogrifySets

Namespace: `C_TransmogSets`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_TransmogSets.ClearLatestSource](#c_transmogsetsclearlatestsource) |  |  |
| ❔ | [C_TransmogSets.ClearNewSource](#c_transmogsetsclearnewsource) |  |  |
| ❔ | [C_TransmogSets.ClearSetNewSourcesForSlot](#c_transmogsetsclearsetnewsourcesforslot) |  |  |
| ❔ | [C_TransmogSets.GetAllSets](#c_transmogsetsgetallsets) |  |  |
| ❔ | [C_TransmogSets.GetAllSourceIDs](#c_transmogsetsgetallsourceids) |  |  |
| ❔ | [C_TransmogSets.GetAvailableSets](#c_transmogsetsgetavailablesets) |  |  |
| ❔ | [C_TransmogSets.GetBaseSetID](#c_transmogsetsgetbasesetid) |  |  |
| ❔ | [C_TransmogSets.GetBaseSets](#c_transmogsetsgetbasesets) |  |  |
| ❔ | [C_TransmogSets.GetBaseSetsFilter](#c_transmogsetsgetbasesetsfilter) |  |  |
| ❔ | [C_TransmogSets.GetCameraIDs](#c_transmogsetsgetcameraids) |  |  |
| ❔ | [C_TransmogSets.GetFilteredBaseSetsCounts](#c_transmogsetsgetfilteredbasesetscounts) |  |  |
| ❔ | [C_TransmogSets.GetFullBaseSetsCounts](#c_transmogsetsgetfullbasesetscounts) |  |  |
| ❔ | [C_TransmogSets.GetIsFavorite](#c_transmogsetsgetisfavorite) |  |  |
| ❔ | [C_TransmogSets.GetLatestSource](#c_transmogsetsgetlatestsource) |  |  |
| ❔ | [C_TransmogSets.GetSetInfo](#c_transmogsetsgetsetinfo) |  |  |
| ❔ | [C_TransmogSets.GetSetNewSources](#c_transmogsetsgetsetnewsources) |  |  |
| ❔ | [C_TransmogSets.GetSetPrimaryAppearances](#c_transmogsetsgetsetprimaryappearances) |  |  |
| ❔ | [C_TransmogSets.GetSetsContainingSourceID](#c_transmogsetsgetsetscontainingsourceid) |  |  |
| ❔ | [C_TransmogSets.GetSetsFilter](#c_transmogsetsgetsetsfilter) |  |  |
| ❔ | [C_TransmogSets.GetSourceIDsForSlot](#c_transmogsetsgetsourceidsforslot) |  |  |
| ❔ | [C_TransmogSets.GetSourcesForSlot](#c_transmogsetsgetsourcesforslot) |  |  |
| ❔ | [C_TransmogSets.GetTransmogSetsClassFilter](#c_transmogsetsgettransmogsetsclassfilter) |  |  |
| ❔ | [C_TransmogSets.GetUsableSets](#c_transmogsetsgetusablesets) |  |  |
| ❔ | [C_TransmogSets.GetValidBaseSetsCountsForCharacter](#c_transmogsetsgetvalidbasesetscountsforcharacter) |  |  |
| ❔ | [C_TransmogSets.GetValidClassForSet](#c_transmogsetsgetvalidclassforset) |  |  |
| ❔ | [C_TransmogSets.GetVariantSets](#c_transmogsetsgetvariantsets) |  |  |
| ❔ | [C_TransmogSets.HasAnyValidSets](#c_transmogsetshasanyvalidsets) |  |  |
| ❔ | [C_TransmogSets.HasAvailableSets](#c_transmogsetshasavailablesets) |  |  |
| ❔ | [C_TransmogSets.HasUsableSets](#c_transmogsetshasusablesets) |  |  |
| ❔ | [C_TransmogSets.IsBaseSetCollected](#c_transmogsetsisbasesetcollected) |  |  |
| ❔ | [C_TransmogSets.IsNewSource](#c_transmogsetsisnewsource) |  |  |
| ❔ | [C_TransmogSets.IsSetVisible](#c_transmogsetsissetvisible) |  |  |
| ❔ | [C_TransmogSets.IsUsingDefaultBaseSetsFilters](#c_transmogsetsisusingdefaultbasesetsfilters) |  |  |
| ❔ | [C_TransmogSets.IsUsingDefaultSetsFilters](#c_transmogsetsisusingdefaultsetsfilters) |  |  |
| ❔ | [C_TransmogSets.SetBaseSetsFilter](#c_transmogsetssetbasesetsfilter) |  |  |
| ❔ | [C_TransmogSets.SetDefaultBaseSetsFilters](#c_transmogsetssetdefaultbasesetsfilters) |  |  |
| ❔ | [C_TransmogSets.SetDefaultSetsFilters](#c_transmogsetssetdefaultsetsfilters) |  |  |
| ❔ | [C_TransmogSets.SetHasNewSources](#c_transmogsetssethasnewsources) |  |  |
| ❔ | [C_TransmogSets.SetHasNewSourcesForSlot](#c_transmogsetssethasnewsourcesforslot) |  |  |
| ❔ | [C_TransmogSets.SetIsFavorite](#c_transmogsetssetisfavorite) |  |  |
| ❔ | [C_TransmogSets.SetSetsFilter](#c_transmogsetssetsetsfilter) |  |  |
| ❔ | [C_TransmogSets.SetTransmogSetsClassFilter](#c_transmogsetssettransmogsetsclassfilter) |  |  |

### C_TransmogSets.ClearLatestSource

`C_TransmogSets.ClearLatestSource()`

- Status: ❔ unverified
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.ClearNewSource

`C_TransmogSets.ClearNewSource(sourceID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.ClearSetNewSourcesForSlot

`C_TransmogSets.ClearSetNewSourcesForSlot(transmogSetID: number, slot: luaIndex)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetAllSets

`C_TransmogSets.GetAllSets() → sets: TransmogSetInfo[]`

- Status: ❔ unverified
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetAllSourceIDs

`C_TransmogSets.GetAllSourceIDs(transmogSetID: number) → sources: number[]`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetAvailableSets

`C_TransmogSets.GetAvailableSets() → sets: TransmogSetInfo[]`

- Status: ❔ unverified
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetBaseSetID

`C_TransmogSets.GetBaseSetID(transmogSetID: number) → baseTransmogSetID: number`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetBaseSets

`C_TransmogSets.GetBaseSets() → sets: TransmogSetInfo[]`

- Status: ❔ unverified
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetBaseSetsFilter

`C_TransmogSets.GetBaseSetsFilter(index: luaIndex) → isChecked: bool`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetCameraIDs

`C_TransmogSets.GetCameraIDs() → detailsCameraID: number?, vendorCameraID: number?`

- Status: ❔ unverified
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetFilteredBaseSetsCounts

`C_TransmogSets.GetFilteredBaseSetsCounts() → numCollected: number, numTotal: number`

- Status: ❔ unverified
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetFullBaseSetsCounts

`C_TransmogSets.GetFullBaseSetsCounts() → numCollected: number, numTotal: number`

- Status: ❔ unverified
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetIsFavorite

`C_TransmogSets.GetIsFavorite(transmogSetID: number) → isFavorite: bool, isGroupFavorite: bool`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetLatestSource

`C_TransmogSets.GetLatestSource() → sourceID: number`

- Status: ❔ unverified
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetSetInfo

`C_TransmogSets.GetSetInfo(transmogSetID: number) → set: TransmogSetInfo`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetSetNewSources

`C_TransmogSets.GetSetNewSources(transmogSetID: number) → sourceIDs: number[]`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetSetPrimaryAppearances

`C_TransmogSets.GetSetPrimaryAppearances(transmogSetID: number) → apppearances: TransmogSetPrimaryAppearanceInfo[]`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetSetsContainingSourceID

`C_TransmogSets.GetSetsContainingSourceID(sourceID: number) → setIDs: number[]`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetSetsFilter

`C_TransmogSets.GetSetsFilter(index: luaIndex) → isChecked: bool`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetSourceIDsForSlot

`C_TransmogSets.GetSourceIDsForSlot(transmogSetID: number, slot: luaIndex) → sources: number[]`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetSourcesForSlot

`C_TransmogSets.GetSourcesForSlot(transmogSetID: number, slot: luaIndex) → sources: AppearanceSourceInfo[]`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetTransmogSetsClassFilter

`C_TransmogSets.GetTransmogSetsClassFilter() → classID: number`

- Status: ❔ unverified
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetUsableSets

`C_TransmogSets.GetUsableSets() → sets: TransmogSetInfo[]`

- Status: ❔ unverified
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetValidBaseSetsCountsForCharacter

`C_TransmogSets.GetValidBaseSetsCountsForCharacter() → numCollected: number, numTotal: number`

- Status: ❔ unverified
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetValidClassForSet

`C_TransmogSets.GetValidClassForSet(transmogSetID: number) → classID: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.GetVariantSets

`C_TransmogSets.GetVariantSets(transmogSetID: number) → sets: TransmogSetInfo[]`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.HasAnyValidSets

`C_TransmogSets.HasAnyValidSets() → hasAnyValidSets: bool`

- Status: ❔ unverified
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.HasAvailableSets

`C_TransmogSets.HasAvailableSets() → hasAvailableSets: bool`

- Status: ❔ unverified
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.HasUsableSets

`C_TransmogSets.HasUsableSets() → hasUsableSets: bool`

- Status: ❔ unverified
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.IsBaseSetCollected

`C_TransmogSets.IsBaseSetCollected(transmogSetID: number) → isCollected: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.IsNewSource

`C_TransmogSets.IsNewSource(sourceID: number) → isNew: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.IsSetVisible

`C_TransmogSets.IsSetVisible(transmogSetID: number) → isVisible: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.IsUsingDefaultBaseSetsFilters

`C_TransmogSets.IsUsingDefaultBaseSetsFilters() → isUsingDefaultBaseSetsFilters: bool`

- Status: ❔ unverified
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.IsUsingDefaultSetsFilters

`C_TransmogSets.IsUsingDefaultSetsFilters() → isUsingDefaultSetsFilters: bool`

- Status: ❔ unverified
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.SetBaseSetsFilter

`C_TransmogSets.SetBaseSetsFilter(index: luaIndex, isChecked: bool)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.SetDefaultBaseSetsFilters

`C_TransmogSets.SetDefaultBaseSetsFilters()`

- Status: ❔ unverified
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.SetDefaultSetsFilters

`C_TransmogSets.SetDefaultSetsFilters()`

- Status: ❔ unverified
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.SetHasNewSources

`C_TransmogSets.SetHasNewSources(transmogSetID: number) → hasNewSources: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.SetHasNewSourcesForSlot

`C_TransmogSets.SetHasNewSourcesForSlot(transmogSetID: number, slot: luaIndex) → hasNewSources: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.SetIsFavorite

`C_TransmogSets.SetIsFavorite(transmogSetID: number, isFavorite: bool)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.SetSetsFilter

`C_TransmogSets.SetSetsFilter(index: luaIndex, isChecked: bool)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

### C_TransmogSets.SetTransmogSetsClassFilter

`C_TransmogSets.SetTransmogSetsClassFilter(classID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TransmogSetsDocumentation.lua`

## Types

### TransmogSetInfo

- Structure
  - `setID`: number
  - `name`: string
  - `baseSetID`: number?
  - `description`: cstring?
  - `label`: cstring?
  - `expansionID`: number
  - `patchID`: number
  - `uiOrder`: number
  - `classMask`: number
  - `hiddenUntilCollected`: bool
  - `requiredFaction`: cstring?
  - `collected`: bool
  - `favorite`: bool
  - `limitedTimeSet`: bool
  - `validForCharacter`: bool
  - `grantAsPrecedingVariant`: bool

### TransmogSetPrimaryAppearanceInfo

- Structure
  - `appearanceID`: number
  - `collected`: bool
