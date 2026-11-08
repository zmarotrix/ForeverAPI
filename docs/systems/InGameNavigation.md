# InGameNavigation

Namespace: `C_Navigation`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_Navigation.GetDistance](#c_navigationgetdistance) |  |  |
| ❔ | [C_Navigation.GetFrame](#c_navigationgetframe) |  |  |
| ❔ | [C_Navigation.GetNearestPartyMemberToken](#c_navigationgetnearestpartymembertoken) |  |  |
| ❔ | [C_Navigation.GetNextWaypointForMap](#c_navigationgetnextwaypointformap) |  |  |
| ❔ | [C_Navigation.GetTargetState](#c_navigationgettargetstate) |  |  |
| ❔ | [C_Navigation.HasValidScreenPosition](#c_navigationhasvalidscreenposition) |  |  |
| ❔ | [C_Navigation.WasClampedToScreen](#c_navigationwasclampedtoscreen) |  |  |

### C_Navigation.GetDistance

`C_Navigation.GetDistance() → distance: number`

- Status: ❔ unverified
- Source: client docs `InGameNavigationDocumentation.lua`

### C_Navigation.GetFrame

`C_Navigation.GetFrame() → frame: ScriptRegion?`

- Status: ❔ unverified
- Source: client docs `InGameNavigationDocumentation.lua`

### C_Navigation.GetNearestPartyMemberToken

`C_Navigation.GetNearestPartyMemberToken() → unitToken: cstring`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `InGameNavigationDocumentation.lua`

### C_Navigation.GetNextWaypointForMap

`C_Navigation.GetNextWaypointForMap(uiMapID: number) → x: number, y: number, waypointDescription: string`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `InGameNavigationDocumentation.lua`

### C_Navigation.GetTargetState

`C_Navigation.GetTargetState() → state: NavigationState`

- Status: ❔ unverified
- Source: client docs `InGameNavigationDocumentation.lua`

### C_Navigation.HasValidScreenPosition

`C_Navigation.HasValidScreenPosition() → hasValidScreenPosition: bool`

- Status: ❔ unverified
- Source: client docs `InGameNavigationDocumentation.lua`

### C_Navigation.WasClampedToScreen

`C_Navigation.WasClampedToScreen() → wasClamped: bool`

- Status: ❔ unverified
- Source: client docs `InGameNavigationDocumentation.lua`

## Events

### NAVIGATION_DESTINATION_REACHED

- Status: ❔ unverified
- Payload: `isWaypoint: bool`
- fires synchronously (Blizzard's docs)

### NAVIGATION_FRAME_CREATED

- Status: ❔ unverified
- Payload: `region: ScriptRegion`
- fires synchronously (Blizzard's docs)

### NAVIGATION_FRAME_DESTROYED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### NavigationState

- Enumeration — ❔ unverified
  - `Invalid` = 0
  - `Occluded` = 1
  - `InRange` = 2
  - `Disabled` = 3
