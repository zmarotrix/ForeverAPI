# ModelInfo

Namespace: `C_ModelInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ModelInfo.AddActiveModelScene](#c_modelinfoaddactivemodelscene) |  |  |
| ✅ | [C_ModelInfo.AddActiveModelSceneActor](#c_modelinfoaddactivemodelsceneactor) |  |  |
| ✅ | [C_ModelInfo.ClearActiveModelScene](#c_modelinfoclearactivemodelscene) |  |  |
| ✅ | [C_ModelInfo.ClearActiveModelSceneActor](#c_modelinfoclearactivemodelsceneactor) |  |  |
| ✅ | [C_ModelInfo.GetModelSceneActorDisplayInfoByID](#c_modelinfogetmodelsceneactordisplayinfobyid) |  |  |
| ✅ | [C_ModelInfo.GetModelSceneActorInfoByID](#c_modelinfogetmodelsceneactorinfobyid) |  |  |
| ✅ | [C_ModelInfo.GetModelSceneCameraInfoByID](#c_modelinfogetmodelscenecamerainfobyid) |  |  |
| ✅ | [C_ModelInfo.GetModelSceneInfoByID](#c_modelinfogetmodelsceneinfobyid) |  |  |

### C_ModelInfo.AddActiveModelScene

`C_ModelInfo.AddActiveModelScene(modelSceneFrame: ModelSceneFrame, modelSceneID: number)`

- Status: ✅ verified (function)
- Blizzard: This function does nothing in public clients
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UIModelInfoDocumentation.lua`

### C_ModelInfo.AddActiveModelSceneActor

`C_ModelInfo.AddActiveModelSceneActor(modelSceneFrameActor: ModelSceneFrameActor, modelSceneActorID: number)`

- Status: ✅ verified (function)
- Blizzard: This function does nothing in public clients
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UIModelInfoDocumentation.lua`

### C_ModelInfo.ClearActiveModelScene

`C_ModelInfo.ClearActiveModelScene(modelSceneFrame: ModelSceneFrame)`

- Status: ✅ verified (function)
- Blizzard: This function does nothing in public clients
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UIModelInfoDocumentation.lua`

### C_ModelInfo.ClearActiveModelSceneActor

`C_ModelInfo.ClearActiveModelSceneActor(modelSceneFrameActor: ModelSceneFrameActor)`

- Status: ✅ verified (function)
- Blizzard: This function does nothing in public clients
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UIModelInfoDocumentation.lua`

### C_ModelInfo.GetModelSceneActorDisplayInfoByID

`C_ModelInfo.GetModelSceneActorDisplayInfoByID(modelActorDisplayID: number) → actorDisplayInfo: UIModelSceneActorDisplayInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UIModelInfoDocumentation.lua`

### C_ModelInfo.GetModelSceneActorInfoByID

`C_ModelInfo.GetModelSceneActorInfoByID(modelActorID: number) → actorInfo: UIModelSceneActorInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UIModelInfoDocumentation.lua`

### C_ModelInfo.GetModelSceneCameraInfoByID

`C_ModelInfo.GetModelSceneCameraInfoByID(modelSceneCameraID: number) → modelSceneCameraInfo: UIModelSceneCameraInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UIModelInfoDocumentation.lua`

### C_ModelInfo.GetModelSceneInfoByID

`C_ModelInfo.GetModelSceneInfoByID(modelSceneID: number) → modelSceneType: ModelSceneType, modelCameraIDs: number[], modelActorsIDs: number[], flags: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UIModelInfoDocumentation.lua`

## Events

### UI_MODEL_SCENE_INFO_UPDATED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

## Types

### UIModelSceneActorDisplayInfo

- Structure
  - `animation`: number
  - `animationVariation`: number
  - `animSpeed`: number
  - `animationKitID`: number?
  - `spellVisualKitID`: number?
  - `alpha`: number
  - `scale`: number

### UIModelSceneActorInfo

- Structure
  - `modelActorID`: number
  - `scriptTag`: cstring
  - `position`: vector3
  - `yaw`: number
  - `pitch`: number
  - `roll`: number
  - `normalizeScaleAggressiveness`: number?
  - `useCenterForOriginX`: bool
  - `useCenterForOriginY`: bool
  - `useCenterForOriginZ`: bool
  - `modelActorDisplayID`: number?

### UIModelSceneCameraInfo

- Structure
  - `modelSceneCameraID`: number
  - `scriptTag`: cstring
  - `cameraType`: cstring
  - `target`: vector3
  - `yaw`: number
  - `pitch`: number
  - `roll`: number
  - `zoomDistance`: number
  - `minZoomDistance`: number
  - `maxZoomDistance`: number
  - `zoomedTargetOffset`: vector3
  - `zoomedYawOffset`: number
  - `zoomedPitchOffset`: number
  - `zoomedRollOffset`: number
  - `flags`: ModelSceneSetting
