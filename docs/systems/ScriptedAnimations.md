# ScriptedAnimations

Namespace: `C_ScriptedAnimations`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ScriptedAnimations.GetAllScriptedAnimationEffects](#c_scriptedanimationsgetallscriptedanimationeffects) |  |  |

### C_ScriptedAnimations.GetAllScriptedAnimationEffects

`C_ScriptedAnimations.GetAllScriptedAnimationEffects() → scriptedAnimationEffects: ScriptedAnimationEffect[]`

- Status: ✅ verified (function)
- Source: client docs `ScriptedAnimationsDocumentation.lua`

## Events

### SCRIPTED_ANIMATIONS_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### ScriptedAnimationBehavior

- Enumeration — ✅ verified
  - `None` = 0
  - `TargetShake` = 1
  - `TargetKnockBack` = 2
  - `SourceRecoil` = 3
  - `SourceCollideWithTarget` = 4
  - `UIParentShake` = 5

### ScriptedAnimationEffect

- Structure
  - `id`: number
  - `visual`: fileID
  - `visualScale`: number
  - `duration`: number
  - `trajectory`: ScriptedAnimationTrajectory
  - `yawRadians`: number
  - `pitchRadians`: number
  - `rollRadians`: number
  - `offsetX`: number
  - `offsetY`: number
  - `offsetZ`: number
  - `animation`: number
  - `animationSpeed`: number
  - `alpha`: number
  - `useTargetAsSource`: bool
  - `startBehavior`: ScriptedAnimationBehavior?
  - `startSoundKitID`: number?
  - `finishEffectID`: number?
  - `finishBehavior`: ScriptedAnimationBehavior?
  - `finishSoundKitID`: number?
  - `startAlphaFade`: number?
  - `startAlphaFadeDuration`: number?
  - `endAlphaFade`: number?
  - `endAlphaFadeDuration`: number?
  - `animationStartOffset`: number?
  - `loopingSoundKitID`: number?
  - `particleOverrideScale`: number?

### ScriptedAnimationFlags

- Enumeration — ✅ verified
  - `UseTargetAsSource` = 1

### ScriptedAnimationTrajectory

- Enumeration — ✅ verified
  - `AtSource` = 0
  - `AtTarget` = 1
  - `Straight` = 2
  - `CurveLeft` = 3
  - `CurveRight` = 4
  - `CurveRandom` = 5
  - `HalfwayBetween` = 6
