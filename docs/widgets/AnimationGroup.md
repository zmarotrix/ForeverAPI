# AnimationGroup

Object type reported: `AnimationGroup`

Script handlers: `OnLoad`, `OnUpdate`, `OnPlay`, `OnPause`, `OnStop`, `OnFinished`, `OnLoop`

## Methods

- ✅ `AddAccessRestrictions(restrictions: ScriptObjectAccessRestriction)` — Adds access restrictions to a script object, preventing it from being used in API calls when enforced. (restricted in some situations; secret arguments: NotAllowed)
- ✅ `AddForbiddenAspects(aspects: ForbiddenAspect)` — Adds forbidden aspects to a script object, restricting access to various functionalities such as script bindings. (restricted in some situations; secret arguments: NotAllowed)
- ✅ `AddSecretAspect(aspect: SecretAspect)` (restricted in some situations; secret arguments: AllowedWhenUntainted)
- ✅ `CanBeAccessedInContext() → canAccess: bool` — Returns whether the current Lua execution context has permission to access this object. (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `ClearParentKey()`
- ✅ `CreateAnimation(animationType: cstring?, name: cstring?, templateName: cstring?) → anim: SimpleAnim` (ChecksForbiddenAspects: [{'Argument': 'self', 'Aspect': 'Enum.ForbiddenAspect.AddAnimations'}]; secret arguments: NotAllowed)
- ✅ `Finish()`
- ✅ `GetAccessRestrictions() → restrictions: ScriptObjectAccessRestriction` — Returns the mask of all access restrictions applied to this object. (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `GetAnimationSpeedMultiplier() → animationSpeedMultiplier: number`
- ✅ `GetAnimations() → anims: SimpleAnim`
- ✅ `GetDebugName(preferParentKey: bool = False) → debugName: string` (ConstSecretAccessor; secret arguments: AllowedWhenUntainted)
- ✅ `GetDuration() → durationSec: number`
- ✅ `GetElapsed() → elapsedSec: number` (ChecksForbiddenAspects: [{'Argument': 'self', 'Aspect': 'Enum.ForbiddenAspect.QueryAnimationProgress'}])
- ✅ `GetForbiddenAspects() → aspects: ForbiddenAspect` — Returns the mask of all forbidden aspects applied to this object. (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `GetInheritableForbiddenAspects(path: ScriptObjectPropagationPath) → aspects: ForbiddenAspect` — Returns the mask of all forbidden aspects applied to this object that can propagate to others. (secret arguments: NotAllowed; SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `GetLoopState() → loopState: cstring` (ChecksForbiddenAspects: [{'Argument': 'self', 'Aspect': 'Enum.ForbiddenAspect.QueryAnimationProgress'}])
- ✅ `GetLooping() → loopType: LoopType`
- ✅ `GetName() → name: cstring` (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectName'])
- ✅ `GetObjectTable() → objectTable: FrameScriptObject`
- ✅ `GetObjectType() → objectType: cstring` (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectType'])
- ✅ `GetParent() → parent: CScriptObject` (SecretReturnsForAspect: ['Enum.SecretAspect.Hierarchy'])
- ✅ `GetParentKey() → parentKey: cstring`
- ✅ `GetProgress() → progress: number` (ChecksForbiddenAspects: [{'Argument': 'self', 'Aspect': 'Enum.ForbiddenAspect.QueryAnimationProgress'}])
- ✅ `GetScript(scriptTypeName: ScriptTypeName, bindingType: ScriptBindingType = Extrinsic) → script: LuaFunctionReference` (ChecksForbiddenAspects: [{'Argument': 'self', 'Aspect': 'Enum.ForbiddenAspect.ScriptBindings'}]; ConstSecretAccessor; RequiresSupportedScript; secret arguments: AllowedWhenUntainted)
- ✅ `HasAccessConstraints() → hasAccessConstraints: bool` — Returns whether this object has any access constraints that may limit access from some Lua execution contexts. (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `HasAnyAccessRestrictions(restrictions: ScriptObjectAccessRestriction?) → hasAnyAccessRestriction: bool` — Returns true if this object has any of the supplied access restrictions applied. (secret arguments: AllowedWhenUntainted; SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `HasAnyForbiddenAspects(aspects: ForbiddenAspect?) → hasAnyForbiddenAspect: bool` — Returns true if this object has any of the supplied forbidden aspects added. (secret arguments: AllowedWhenUntainted; SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `HasAnySecretAspect() → hasSecretAspect: bool` (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecrets'])
- ✅ `HasScript(scriptName: cstring) → hasScript: bool` (ConstSecretAccessor; secret arguments: AllowedWhenUntainted; SecretReturnsForAspect: ['Enum.SecretAspect.ObjectType'])
- ✅ `HasSecretAspect(aspect: SecretAspect) → hasSecretAspect: bool` (ConstSecretAccessor; secret arguments: AllowedWhenUntainted; SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecrets'])
- ✅ `HasSecretValues() → hasSecretValues: bool` (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecrets'])
- ✅ `HookScript(scriptTypeName: ScriptTypeName, script: LuaFunctionReference, bindingType: ScriptBindingType = Extrinsic) → success: bool` (ChecksForbiddenAspects: [{'Argument': 'self', 'Aspect': 'Enum.ForbiddenAspect.ScriptBindings'}]; RequiresAssignableScript; secret arguments: AllowedWhenUntainted)
- ✅ `IsDone() → isDone: bool` (ChecksForbiddenAspects: [{'Argument': 'self', 'Aspect': 'Enum.ForbiddenAspect.QueryAnimationProgress'}])
- ✅ `IsForbidden() → isForbidden: bool` — Returns whether this object has been explicitly marked as forbidden. (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `IsObjectType(objectType: cstring) → isType: bool` (ConstSecretAccessor; secret arguments: AllowedWhenUntainted; SecretReturnsForAspect: ['Enum.SecretAspect.ObjectType'])
- ✅ `IsPaused() → isPaused: bool` (ChecksForbiddenAspects: [{'Argument': 'self', 'Aspect': 'Enum.ForbiddenAspect.QueryAnimationProgress'}])
- ✅ `IsPendingFinish() → isPendingFinish: bool` (ChecksForbiddenAspects: [{'Argument': 'self', 'Aspect': 'Enum.ForbiddenAspect.QueryAnimationProgress'}])
- ✅ `IsPlaying() → isPlaying: bool` (ChecksForbiddenAspects: [{'Argument': 'self', 'Aspect': 'Enum.ForbiddenAspect.QueryAnimationProgress'}])
- ✅ `IsPreventingSecretValues() → isPreventingSecretValues: bool` (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecrets'])
- ✅ `IsReverse() → isReverse: bool` (ChecksForbiddenAspects: [{'Argument': 'self', 'Aspect': 'Enum.ForbiddenAspect.QueryAnimationProgress'}])
- ✅ `IsSetToFinalAlpha() → isSetToFinalAlpha: bool`
- ✅ `Pause()`
- ✅ `Play(reverse: bool = False, offset: number = 0)` (secret arguments: AllowedWhenUntainted)
- ✅ `RemoveAnimations()`
- ✅ `Restart(reverse: bool = False, offset: number = 0)` (secret arguments: AllowedWhenUntainted)
- ✅ `SetAnimationSpeedMultiplier(animationSpeedMultiplier: number)` (secret arguments: AllowedWhenUntainted)
- ✅ `SetForbidden()` (restricted in some situations)
- ✅ `SetLooping(loopType: LoopType)` (secret arguments: NotAllowed)
- ✅ `SetParentKey(parentKey: cstring, clearOtherKeys: bool = False)` (secret arguments: AllowedWhenUntainted)
- ✅ `SetPlaying(play: bool)` (secret arguments: AllowedWhenUntainted)
- ✅ `SetScript(scriptTypeName: ScriptTypeName, script: LuaFunctionReference?)` (ChecksForbiddenAspects: [{'Argument': 'self', 'Aspect': 'Enum.ForbiddenAspect.ScriptBindings'}]; RequiresAssignableScript; secret arguments: AllowedWhenUntainted)
- ✅ `SetToDefaults()` — Reset all script accessible values to their default values. If possible, clears secret states. (ChecksForbiddenAspects: [{'Argument': 'self', 'Aspect': 'Enum.ForbiddenAspect.SetToDefaults'}, {'Argument': 'self', 'Aspect': 'Enum.ForbiddenAspect.RemoveSecretAspects'}]; protected: only Blizzard's secure code may call it)
- ✅ `SetToFinalAlpha(setToFinalAlpha: bool)` (secret arguments: AllowedWhenUntainted)
- ✅ `Stop()`
