# InGameNavigation

Namespace: `C_Navigation`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Navigation.GetDistance](#c_navigationgetdistance) | 1 value | 1 value |
| ✅ | [C_Navigation.GetFrame](#c_navigationgetframe) | 1 value | 1 value |
| ✅ | [C_Navigation.GetNearestPartyMemberToken](#c_navigationgetnearestpartymembertoken) | 💥 forbidden | 💥 forbidden |
| ✅ | [C_Navigation.GetNextWaypointForMap](#c_navigationgetnextwaypointformap) | 💥 no sample for map | 💥 no sample for map |
| ✅ | [C_Navigation.GetTargetState](#c_navigationgettargetstate) | 1 value | 1 value |
| ✅ | [C_Navigation.HasValidScreenPosition](#c_navigationhasvalidscreenposition) | 1 value | 1 value |
| ✅ | [C_Navigation.WasClampedToScreen](#c_navigationwasclampedtoscreen) |  |  |

### C_Navigation.GetDistance

`C_Navigation.GetDistance() → distance: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `InGameNavigationDocumentation.lua`

### C_Navigation.GetFrame

`C_Navigation.GetFrame() → frame: ScriptRegion?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `InGameNavigationDocumentation.lua`

### C_Navigation.GetNearestPartyMemberToken

`C_Navigation.GetNearestPartyMemberToken() → unitToken: cstring`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Called out of combat: not called: forbidden
- Called in combat: not called: forbidden
- Source: client docs `InGameNavigationDocumentation.lua`

### C_Navigation.GetNextWaypointForMap

`C_Navigation.GetNextWaypointForMap(uiMapID: number) → x: number, y: number, waypointDescription: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `map`: not called: no sample for map
- Called in combat: not called: no sample for map
- Source: client docs `InGameNavigationDocumentation.lua`

### C_Navigation.GetTargetState

`C_Navigation.GetTargetState() → state: NavigationState`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `InGameNavigationDocumentation.lua`

### C_Navigation.HasValidScreenPosition

`C_Navigation.HasValidScreenPosition() → hasValidScreenPosition: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `InGameNavigationDocumentation.lua`

### C_Navigation.WasClampedToScreen

`C_Navigation.WasClampedToScreen() → wasClamped: bool`

- Status: ✅ verified (function)
- Source: client docs `InGameNavigationDocumentation.lua`

## Events

### NAVIGATION_DESTINATION_REACHED

- Status: ✅ verified
- Payload: `isWaypoint: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 3 times (0 in combat); argument kinds: `b`

### NAVIGATION_FRAME_CREATED

- Status: ✅ verified
- Payload: `region: ScriptRegion`
- fires synchronously (Blizzard's docs)
- Seen firing 31 times (2 in combat); argument kinds: `t`

### NAVIGATION_FRAME_DESTROYED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 61 times (0 in combat); argument kinds: ``

## Types

### NavigationState

- Enumeration — ✅ verified
  - `Invalid` = 0
  - `Occluded` = 1
  - `InRange` = 2
  - `Disabled` = 3
