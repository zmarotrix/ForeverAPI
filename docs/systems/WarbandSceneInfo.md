# WarbandSceneInfo

Namespace: `C_WarbandScene`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_WarbandScene.GetRandomEntryID](#c_warbandscenegetrandomentryid) |  |  |
| ✅ | [C_WarbandScene.GetWarbandSceneEntry](#c_warbandscenegetwarbandsceneentry) |  |  |
| ✅ | [C_WarbandScene.HasWarbandScene](#c_warbandscenehaswarbandscene) |  |  |
| ✅ | [C_WarbandScene.IsFavorite](#c_warbandsceneisfavorite) |  |  |
| ✅ | [C_WarbandScene.SearchWarbandSceneEntries](#c_warbandscenesearchwarbandsceneentries) |  |  |
| ✅ | [C_WarbandScene.SetFavorite](#c_warbandscenesetfavorite) |  |  |
| ✅ | [C_WarbandScene.WarbandScenesAvailable](#c_warbandscenewarbandscenesavailable) |  |  |

### C_WarbandScene.GetRandomEntryID

`C_WarbandScene.GetRandomEntryID() → warbandSceneID: number`

- Status: ✅ verified (function)
- Source: client docs `WarbandSceneInfoDocumentation.lua`

### C_WarbandScene.GetWarbandSceneEntry

`C_WarbandScene.GetWarbandSceneEntry(warbandSceneID: number) → warbandSceneEntry: WarbandSceneEntry`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WarbandSceneInfoDocumentation.lua`

### C_WarbandScene.HasWarbandScene

`C_WarbandScene.HasWarbandScene(warbandSceneID: number) → owned: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WarbandSceneInfoDocumentation.lua`

### C_WarbandScene.IsFavorite

`C_WarbandScene.IsFavorite(warbandSceneID: number) → favorite: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WarbandSceneInfoDocumentation.lua`

### C_WarbandScene.SearchWarbandSceneEntries

`C_WarbandScene.SearchWarbandSceneEntries(searchParams: WarbandSceneSearchInfo) → matchingEntryIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WarbandSceneInfoDocumentation.lua`

### C_WarbandScene.SetFavorite

`C_WarbandScene.SetFavorite(warbandSceneID: number, favorite: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WarbandSceneInfoDocumentation.lua`

### C_WarbandScene.WarbandScenesAvailable

`C_WarbandScene.WarbandScenesAvailable() → areWarbandScenesAvailable: bool`

- Status: ✅ verified (function)
- Source: client docs `WarbandSceneInfoDocumentation.lua`

## Events

### NEW_WARBAND_SCENE_ADDED

- Status: ✅ verified
- Payload: `warbandScenID: number`
- fires synchronously (Blizzard's docs)

### WARBAND_SCENE_FAVORITES_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### WarbandSceneEntry

- Structure
  - `warbandSceneID`: number
  - `name`: cstring
  - `description`: cstring
  - `source`: cstring
  - `quality`: number
  - `textureKit`: textureKit
  - `isFavorite`: bool
  - `hasFanfare`: bool
  - `sourceType`: number

### WarbandSceneSearchInfo

- Structure
  - `ownedOnly`: bool
  - `favoritesOnly`: bool
