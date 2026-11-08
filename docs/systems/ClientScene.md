# ClientScene

Namespace: `C_ClientScene`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_ClientScene.IsSceneTypeActive](#c_clientsceneisscenetypeactive) |  |  |

### C_ClientScene.IsSceneTypeActive

`C_ClientScene.IsSceneTypeActive(desiredSceneType: ClientSceneType?) → isPlaying: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClientSceneDocumentation.lua`

## Events

### CLIENT_SCENE_CLOSED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CLIENT_SCENE_OPENED

- Status: ❔ unverified
- Payload: `sceneType: ClientSceneType`
- fires synchronously (Blizzard's docs)

## Types

### ClientSceneType

- Enumeration — ❔ unverified
  - `DefaultSceneType` = 0
  - `MinigameSceneType` = 1
