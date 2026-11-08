# SuperTrackManager

Namespace: `C_SuperTrack`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_SuperTrack.ClearAllSuperTracked](#c_supertrackclearallsupertracked) |  |  |
| ❔ | [C_SuperTrack.ClearSuperTrackedContent](#c_supertrackclearsupertrackedcontent) |  |  |
| ❔ | [C_SuperTrack.ClearSuperTrackedMapPin](#c_supertrackclearsupertrackedmappin) |  |  |
| ❔ | [C_SuperTrack.GetHighestPrioritySuperTrackingType](#c_supertrackgethighestprioritysupertrackingtype) |  |  |
| ❔ | [C_SuperTrack.GetSuperTrackedContent](#c_supertrackgetsupertrackedcontent) |  |  |
| ❔ | [C_SuperTrack.GetSuperTrackedItemName](#c_supertrackgetsupertrackeditemname) |  |  |
| ❔ | [C_SuperTrack.GetSuperTrackedMapPin](#c_supertrackgetsupertrackedmappin) |  |  |
| ❔ | [C_SuperTrack.GetSuperTrackedQuestID](#c_supertrackgetsupertrackedquestid) |  |  |
| ❔ | [C_SuperTrack.GetSuperTrackedVignette](#c_supertrackgetsupertrackedvignette) |  |  |
| ❔ | [C_SuperTrack.IsSuperTrackingAnything](#c_supertrackissupertrackinganything) |  |  |
| ❔ | [C_SuperTrack.IsSuperTrackingContent](#c_supertrackissupertrackingcontent) |  |  |
| ❔ | [C_SuperTrack.IsSuperTrackingCorpse](#c_supertrackissupertrackingcorpse) |  |  |
| ❔ | [C_SuperTrack.IsSuperTrackingMapPin](#c_supertrackissupertrackingmappin) |  |  |
| ❔ | [C_SuperTrack.IsSuperTrackingQuest](#c_supertrackissupertrackingquest) |  |  |
| ❔ | [C_SuperTrack.IsSuperTrackingUserWaypoint](#c_supertrackissupertrackinguserwaypoint) |  |  |
| ❔ | [C_SuperTrack.SetSuperTrackedContent](#c_supertracksetsupertrackedcontent) |  |  |
| ❔ | [C_SuperTrack.SetSuperTrackedMapPin](#c_supertracksetsupertrackedmappin) |  |  |
| ❔ | [C_SuperTrack.SetSuperTrackedQuestID](#c_supertracksetsupertrackedquestid) |  |  |
| ❔ | [C_SuperTrack.SetSuperTrackedUserWaypoint](#c_supertracksetsupertrackeduserwaypoint) |  |  |
| ❔ | [C_SuperTrack.SetSuperTrackedVignette](#c_supertracksetsupertrackedvignette) |  |  |

### C_SuperTrack.ClearAllSuperTracked

`C_SuperTrack.ClearAllSuperTracked()`

- Status: ❔ unverified
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.ClearSuperTrackedContent

`C_SuperTrack.ClearSuperTrackedContent()`

- Status: ❔ unverified
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.ClearSuperTrackedMapPin

`C_SuperTrack.ClearSuperTrackedMapPin()`

- Status: ❔ unverified
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.GetHighestPrioritySuperTrackingType

`C_SuperTrack.GetHighestPrioritySuperTrackingType() → type: SuperTrackingType?`

- Status: ❔ unverified
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.GetSuperTrackedContent

`C_SuperTrack.GetSuperTrackedContent() → trackableType: ContentTrackingType, trackableID: number`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.GetSuperTrackedItemName

`C_SuperTrack.GetSuperTrackedItemName() → name: string, description: string`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.GetSuperTrackedMapPin

`C_SuperTrack.GetSuperTrackedMapPin() → type: SuperTrackingMapPinType, typeID: number`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.GetSuperTrackedQuestID

`C_SuperTrack.GetSuperTrackedQuestID() → questID: number?`

- Status: ❔ unverified
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.GetSuperTrackedVignette

`C_SuperTrack.GetSuperTrackedVignette() → vignetteGUID: WOWGUID?`

- Status: ❔ unverified
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.IsSuperTrackingAnything

`C_SuperTrack.IsSuperTrackingAnything() → isSuperTracking: bool`

- Status: ❔ unverified
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.IsSuperTrackingContent

`C_SuperTrack.IsSuperTrackingContent() → isSuperTracking: bool`

- Status: ❔ unverified
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.IsSuperTrackingCorpse

`C_SuperTrack.IsSuperTrackingCorpse() → isSuperTracking: bool`

- Status: ❔ unverified
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.IsSuperTrackingMapPin

`C_SuperTrack.IsSuperTrackingMapPin() → isSuperTracking: bool`

- Status: ❔ unverified
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.IsSuperTrackingQuest

`C_SuperTrack.IsSuperTrackingQuest() → isSuperTracking: bool`

- Status: ❔ unverified
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.IsSuperTrackingUserWaypoint

`C_SuperTrack.IsSuperTrackingUserWaypoint() → isSuperTracking: bool`

- Status: ❔ unverified
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.SetSuperTrackedContent

`C_SuperTrack.SetSuperTrackedContent(trackableType: ContentTrackingType, trackableID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.SetSuperTrackedMapPin

`C_SuperTrack.SetSuperTrackedMapPin(type: SuperTrackingMapPinType, typeID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.SetSuperTrackedQuestID

`C_SuperTrack.SetSuperTrackedQuestID(questID: number)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.SetSuperTrackedUserWaypoint

`C_SuperTrack.SetSuperTrackedUserWaypoint(superTracked: bool)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SuperTrackManagerDocumentation.lua`

### C_SuperTrack.SetSuperTrackedVignette

`C_SuperTrack.SetSuperTrackedVignette(vignetteGUID: WOWGUID)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SuperTrackManagerDocumentation.lua`

## Events

### SUPER_TRACKING_CHANGED

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

### SUPER_TRACKING_PATH_UPDATED

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)
