# RaidMarkers

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [CanBeRaidTarget](#canberaidtarget) | 1 value |  |
| ✅ | [ClearRaidMarker](#clearraidmarker) |  |  |
| ✅ | [GetNextAvailableRaidTargetMarkerIndex](#getnextavailableraidtargetmarkerindex) |  |  |
| ✅ | [GetRaidTargetIndex](#getraidtargetindex) | 1 value |  |
| ✅ | [IsRaidMarkerActive](#israidmarkeractive) |  |  |
| ✅ | [IsRaidMarkerSystemEnabled](#israidmarkersystemenabled) | 1 value |  |
| ✅ | [PlaceRaidMarker](#placeraidmarker) |  |  |
| ✅ | [RemoveRaidTargets](#removeraidtargets) |  |  |
| ✅ | [SetRaidTarget](#setraidtarget) |  |  |

### CanBeRaidTarget

`CanBeRaidTarget(target: UnitToken) → result: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with "player": returned 1 value: `boolean`
- Source: client docs `RaidMarkersDocumentation.lua`

### ClearRaidMarker

`ClearRaidMarker(raidMarkerIndex: luaIndex = MAX_RAID_MARKERS)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RaidMarkersDocumentation.lua`

### GetNextAvailableRaidTargetMarkerIndex

`GetNextAvailableRaidTargetMarkerIndex(startIndex: luaIndex, reverseSearch: bool = False, wrapSearch: bool = False, treatDeadNonFriendlyAsAvailable: bool = False) → nextAvailableRaidTargetMarkerIndex: luaIndex`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret during chat lockdown (Blizzard's docs; not checked in game)
- Source: client docs `RaidMarkersDocumentation.lua`

### GetRaidTargetIndex

`GetRaidTargetIndex(target: UnitToken) → result: luaIndex?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- always returns secret values (Blizzard's docs; not checked in game)
- Called out of combat with "player": returned 1 value: `nil`
- Source: client docs `RaidMarkersDocumentation.lua`

### IsRaidMarkerActive

`IsRaidMarkerActive(index: luaIndex) → result: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- secret during chat lockdown (Blizzard's docs; not checked in game)
- Source: client docs `RaidMarkersDocumentation.lua`

### IsRaidMarkerSystemEnabled

`IsRaidMarkerSystemEnabled() → enabled: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `RaidMarkersDocumentation.lua`

### PlaceRaidMarker

`PlaceRaidMarker(index: luaIndex, token: cstring?)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RaidMarkersDocumentation.lua`

### RemoveRaidTargets

`RemoveRaidTargets()`

- Status: ✅ verified (function)
- Blizzard: Removes all assigned raid target markers.
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `RaidMarkersDocumentation.lua`

### SetRaidTarget

`SetRaidTarget(target: UnitToken, userIndex: luaIndex)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RaidMarkersDocumentation.lua`
