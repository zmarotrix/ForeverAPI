# ClientScene

Namespace: `C_ClientScene`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ClientScene.IsSceneTypeActive](#c_clientsceneisscenetypeactive) | 1 value |  |

### C_ClientScene.IsSceneTypeActive

`C_ClientScene.IsSceneTypeActive(desiredSceneType: ClientSceneType?) → isPlaying: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `ClientSceneDocumentation.lua`

## Events

### CLIENT_SCENE_CLOSED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CLIENT_SCENE_OPENED

- Status: ✅ verified
- Payload: `sceneType: ClientSceneType`
- fires synchronously (Blizzard's docs)

## Types

### ClientSceneType

- Enumeration — ✅ verified
  - `DefaultSceneType` = 0
  - `MinigameSceneType` = 1
