# SuperTrackManager

Namespace: `C_SuperTrack`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_SuperTrack.ClearAllSuperTracked](#c_supertrackclearallsupertracked) |  |  |
| ✅ | [C_SuperTrack.ClearSuperTrackedContent](#c_supertrackclearsupertrackedcontent) |  |  |
| ✅ | [C_SuperTrack.ClearSuperTrackedMapPin](#c_supertrackclearsupertrackedmappin) |  |  |
| ✅ | [C_SuperTrack.GetHighestPrioritySuperTrackingType](#c_supertrackgethighestprioritysupertrackingtype) | 1 value | 1 value |
| 🆕 | [C_SuperTrack.GetNextWaypointForMap](#c_supertrackgetnextwaypointformap) |  |  |
| ✅ | [C_SuperTrack.GetSuperTrackedContent](#c_supertrackgetsupertrackedcontent) | 0 values | 0 values |
| ✅ | [C_SuperTrack.GetSuperTrackedItemName](#c_supertrackgetsupertrackeditemname) | 0 values | 0 values |
| ✅ | [C_SuperTrack.GetSuperTrackedMapPin](#c_supertrackgetsupertrackedmappin) | 0 values | 0 values |
| ✅ | [C_SuperTrack.GetSuperTrackedQuestID](#c_supertrackgetsupertrackedquestid) | 1 value | 1 value |
| ✅ | [C_SuperTrack.GetSuperTrackedVignette](#c_supertrackgetsupertrackedvignette) | 1 value | 1 value |
| ✅ | [C_SuperTrack.IsSuperTrackingAnything](#c_supertrackissupertrackinganything) | 1 value | 1 value |
| ✅ | [C_SuperTrack.IsSuperTrackingContent](#c_supertrackissupertrackingcontent) | 1 value | 1 value |
| ✅ | [C_SuperTrack.IsSuperTrackingCorpse](#c_supertrackissupertrackingcorpse) | 1 value | 1 value |
| ✅ | [C_SuperTrack.IsSuperTrackingMapPin](#c_supertrackissupertrackingmappin) | 1 value | 1 value |
| ✅ | [C_SuperTrack.IsSuperTrackingQuest](#c_supertrackissupertrackingquest) | 1 value | 1 value |
| ✅ | [C_SuperTrack.IsSuperTrackingUserWaypoint](#c_supertrackissupertrackinguserwaypoint) | 1 value | 1 value |
| ✅ | [C_SuperTrack.SetSuperTrackedContent](#c_supertracksetsupertrackedcontent) |  |  |
| ✅ | [C_SuperTrack.SetSuperTrackedMapPin](#c_supertracksetsupertrackedmappin) |  |  |
| ✅ | [C_SuperTrack.SetSuperTrackedQuestID](#c_supertracksetsupertrackedquestid) |  |  |
| ✅ | [C_SuperTrack.SetSuperTrackedUserWaypoint](#c_supertracksetsupertrackeduserwaypoint) |  |  |
| ✅ | [C_SuperTrack.SetSuperTrackedVignette](#c_supertracksetsupertrackedvignette) |  |  |

### C_SuperTrack.ClearAllSuperTracked

`C_SuperTrack.ClearAllSuperTracked()`

- Status: ✅ verified (function)
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.ClearSuperTrackedContent

`C_SuperTrack.ClearSuperTrackedContent()`

- Status: ✅ verified (function)
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.ClearSuperTrackedMapPin

`C_SuperTrack.ClearSuperTrackedMapPin()`

- Status: ✅ verified (function)
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.GetHighestPrioritySuperTrackingType

`C_SuperTrack.GetHighestPrioritySuperTrackingType() → type: SuperTrackingType?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.GetNextWaypointForMap

`C_SuperTrack.GetNextWaypointForMap(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_SuperTrack.GetSuperTrackedContent

`C_SuperTrack.GetSuperTrackedContent() → trackableType: ContentTrackingType, trackableID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.GetSuperTrackedItemName

`C_SuperTrack.GetSuperTrackedItemName() → name: string, description: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.GetSuperTrackedMapPin

`C_SuperTrack.GetSuperTrackedMapPin() → type: SuperTrackingMapPinType, typeID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.GetSuperTrackedQuestID

`C_SuperTrack.GetSuperTrackedQuestID() → questID: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.GetSuperTrackedVignette

`C_SuperTrack.GetSuperTrackedVignette() → vignetteGUID: WOWGUID?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.IsSuperTrackingAnything

`C_SuperTrack.IsSuperTrackingAnything() → isSuperTracking: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.IsSuperTrackingContent

`C_SuperTrack.IsSuperTrackingContent() → isSuperTracking: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.IsSuperTrackingCorpse

`C_SuperTrack.IsSuperTrackingCorpse() → isSuperTracking: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.IsSuperTrackingMapPin

`C_SuperTrack.IsSuperTrackingMapPin() → isSuperTracking: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.IsSuperTrackingQuest

`C_SuperTrack.IsSuperTrackingQuest() → isSuperTracking: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.IsSuperTrackingUserWaypoint

`C_SuperTrack.IsSuperTrackingUserWaypoint() → isSuperTracking: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.SetSuperTrackedContent

`C_SuperTrack.SetSuperTrackedContent(trackableType: ContentTrackingType, trackableID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.SetSuperTrackedMapPin

`C_SuperTrack.SetSuperTrackedMapPin(type: SuperTrackingMapPinType, typeID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.SetSuperTrackedQuestID

`C_SuperTrack.SetSuperTrackedQuestID(questID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.SetSuperTrackedUserWaypoint

`C_SuperTrack.SetSuperTrackedUserWaypoint(superTracked: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.SetSuperTrackedVignette

`C_SuperTrack.SetSuperTrackedVignette(vignetteGUID: WOWGUID)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SuperTrackManagerDocumentation.lua`

## Events

### SUPER_TRACKING_CHANGED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### SUPER_TRACKING_PATH_UPDATED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)
