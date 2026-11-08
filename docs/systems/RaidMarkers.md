# RaidMarkers

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [CanBeRaidTarget](#canberaidtarget) |  |  |
| ❔ | [ClearRaidMarker](#clearraidmarker) |  |  |
| ❔ | [GetNextAvailableRaidTargetMarkerIndex](#getnextavailableraidtargetmarkerindex) |  |  |
| ❔ | [GetRaidTargetIndex](#getraidtargetindex) |  |  |
| ❔ | [IsRaidMarkerActive](#israidmarkeractive) |  |  |
| ❔ | [IsRaidMarkerSystemEnabled](#israidmarkersystemenabled) |  |  |
| ❔ | [PlaceRaidMarker](#placeraidmarker) |  |  |
| ❔ | [RemoveRaidTargets](#removeraidtargets) |  |  |
| ❔ | [SetRaidTarget](#setraidtarget) |  |  |

### CanBeRaidTarget

`CanBeRaidTarget(target: UnitToken) → result: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RaidMarkersDocumentation.lua`

### ClearRaidMarker

`ClearRaidMarker(raidMarkerIndex: luaIndex = MAX_RAID_MARKERS)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RaidMarkersDocumentation.lua`

### GetNextAvailableRaidTargetMarkerIndex

`GetNextAvailableRaidTargetMarkerIndex(startIndex: luaIndex, reverseSearch: bool = False, wrapSearch: bool = False, treatDeadNonFriendlyAsAvailable: bool = False) → nextAvailableRaidTargetMarkerIndex: luaIndex`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret during chat lockdown (Blizzard's docs; not checked in game)
- Source: client docs `RaidMarkersDocumentation.lua`

### GetRaidTargetIndex

`GetRaidTargetIndex(target: UnitToken) → result: luaIndex?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- always returns secret values (Blizzard's docs; not checked in game)
- Source: client docs `RaidMarkersDocumentation.lua`

### IsRaidMarkerActive

`IsRaidMarkerActive(index: luaIndex) → result: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret during chat lockdown (Blizzard's docs; not checked in game)
- Source: client docs `RaidMarkersDocumentation.lua`

### IsRaidMarkerSystemEnabled

`IsRaidMarkerSystemEnabled() → enabled: bool`

- Status: ❔ unverified
- Source: client docs `RaidMarkersDocumentation.lua`

### PlaceRaidMarker

`PlaceRaidMarker(index: luaIndex, token: cstring?)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RaidMarkersDocumentation.lua`

### RemoveRaidTargets

`RemoveRaidTargets()`

- Status: ❔ unverified
- Blizzard: Removes all assigned raid target markers.
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `RaidMarkersDocumentation.lua`

### SetRaidTarget

`SetRaidTarget(target: UnitToken, userIndex: luaIndex)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RaidMarkersDocumentation.lua`
