# ControlPoint

Object type reported: `ControlPoint`

Script handlers: none found

## Methods

- ✅ `AddAccessRestrictions(restrictions: ScriptObjectAccessRestriction)` — Adds access restrictions to a script object, preventing it from being used in API calls when enforced. (restricted in some situations; secret arguments: NotAllowed)
- ✅ `AddForbiddenAspects(aspects: ForbiddenAspect)` — Adds forbidden aspects to a script object, restricting access to various functionalities such as script bindings. (restricted in some situations; secret arguments: NotAllowed)
- ✅ `AddSecretAspect(aspect: SecretAspect)` (restricted in some situations; secret arguments: AllowedWhenUntainted)
- ✅ `CanBeAccessedInContext() → canAccess: bool` — Returns whether the current Lua execution context has permission to access this object. (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `ClearParentKey()`
- ✅ `GetAccessRestrictions() → restrictions: ScriptObjectAccessRestriction` — Returns the mask of all access restrictions applied to this object. (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `GetDebugName(preferParentKey: bool = False) → debugName: string` (ConstSecretAccessor; secret arguments: AllowedWhenUntainted)
- ✅ `GetForbiddenAspects() → aspects: ForbiddenAspect` — Returns the mask of all forbidden aspects applied to this object. (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `GetInheritableForbiddenAspects(path: ScriptObjectPropagationPath) → aspects: ForbiddenAspect` — Returns the mask of all forbidden aspects applied to this object that can propagate to others. (secret arguments: NotAllowed; SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `GetName() → name: cstring` (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectName'])
- ✅ `GetObjectTable() → objectTable: FrameScriptObject`
- ✅ `GetObjectType() → objectType: cstring` (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectType'])
- ✅ `GetOffset() → offsetU: number, offsetV: number`
- ✅ `GetOrder() → order: number`
- ✅ `GetParent() → parent: CScriptObject` (SecretReturnsForAspect: ['Enum.SecretAspect.Hierarchy'])
- ✅ `GetParentKey() → parentKey: cstring`
- ✅ `HasAccessConstraints() → hasAccessConstraints: bool` — Returns whether this object has any access constraints that may limit access from some Lua execution contexts. (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `HasAnyAccessRestrictions(restrictions: ScriptObjectAccessRestriction?) → hasAnyAccessRestriction: bool` — Returns true if this object has any of the supplied access restrictions applied. (secret arguments: AllowedWhenUntainted; SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `HasAnyForbiddenAspects(aspects: ForbiddenAspect?) → hasAnyForbiddenAspect: bool` — Returns true if this object has any of the supplied forbidden aspects added. (secret arguments: AllowedWhenUntainted; SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `HasAnySecretAspect() → hasSecretAspect: bool` (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecrets'])
- ✅ `HasSecretAspect(aspect: SecretAspect) → hasSecretAspect: bool` (ConstSecretAccessor; secret arguments: AllowedWhenUntainted; SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecrets'])
- ✅ `HasSecretValues() → hasSecretValues: bool` (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecrets'])
- ✅ `IsForbidden() → isForbidden: bool` — Returns whether this object has been explicitly marked as forbidden. (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `IsObjectType(objectType: cstring) → isType: bool` (ConstSecretAccessor; secret arguments: AllowedWhenUntainted; SecretReturnsForAspect: ['Enum.SecretAspect.ObjectType'])
- ✅ `IsPreventingSecretValues() → isPreventingSecretValues: bool` (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecrets'])
- ✅ `SetForbidden()` (restricted in some situations)
- ✅ `SetOffset(offsetU: number, offsetV: number)` (secret arguments: AllowedWhenUntainted)
- ✅ `SetOrder(order: number)` (secret arguments: AllowedWhenUntainted)
- ✅ `SetParent(parent: SimplePathAnim, order: number?)` (CheckAllowChangeParent; secret arguments: AllowedWhenUntainted)
- ✅ `SetParentKey(parentKey: cstring, clearOtherKeys: bool = False)` (secret arguments: AllowedWhenUntainted)
- ✅ `SetToDefaults()` — Reset all script accessible values to their default values. If possible, clears secret states. (ChecksForbiddenAspects: [{'Argument': 'self', 'Aspect': 'Enum.ForbiddenAspect.SetToDefaults'}, {'Argument': 'self', 'Aspect': 'Enum.ForbiddenAspect.RemoveSecretAspects'}]; protected: only Blizzard's secure code may call it)
