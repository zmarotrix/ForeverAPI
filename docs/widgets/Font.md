# Font

Object type reported: `Font`

Script handlers: none found

## Methods

- ✅ `AddAccessRestrictions(restrictions: ScriptObjectAccessRestriction)` — Adds access restrictions to a script object, preventing it from being used in API calls when enforced. (restricted in some situations; secret arguments: NotAllowed)
- ✅ `AddForbiddenAspects(aspects: ForbiddenAspect)` — Adds forbidden aspects to a script object, restricting access to various functionalities such as script bindings. (restricted in some situations; secret arguments: NotAllowed)
- ✅ `AddSecretAspect(aspect: SecretAspect)` (restricted in some situations; secret arguments: AllowedWhenUntainted)
- ✅ `CanBeAccessedInContext() → canAccess: bool` — Returns whether the current Lua execution context has permission to access this object. (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `CopyFontObject(sourceFont: SimpleFont)` (secret arguments: AllowedWhenUntainted)
- ✅ `GetAccessRestrictions() → restrictions: ScriptObjectAccessRestriction` — Returns the mask of all access restrictions applied to this object. (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `GetAlpha() → alpha: SingleColorValue`
- ✅ `GetFont() → fontFile: cstring, height: uiFontHeight, flags: TBFFlags`
- ✅ `GetFontHeight() → height: number` — Return is either in uiUnits or internal height due to fixedHeight.
- ✅ `GetFontObject() → font: SimpleFont`
- ✅ `GetFontObjectForAlphabet(alphabet: FontAlphabet) → font: SimpleFont` (ConstSecretAccessor; secret arguments: AllowedWhenUntainted)
- ✅ `GetForbiddenAspects() → aspects: ForbiddenAspect` — Returns the mask of all forbidden aspects applied to this object. (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `GetIndentedWordWrap() → wordWrap: bool`
- ✅ `GetInheritableForbiddenAspects(path: ScriptObjectPropagationPath) → aspects: ForbiddenAspect` — Returns the mask of all forbidden aspects applied to this object that can propagate to others. (secret arguments: NotAllowed; SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `GetJustifyH() → justifyH: JustifyHorizontal`
- ✅ `GetJustifyV() → justifyV: JustifyVertical`
- ✅ `GetName() → name: cstring` (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectName'])
- ✅ `GetObjectTable() → objectTable: FrameScriptObject`
- ✅ `GetObjectType() → objectType: cstring` (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectType'])
- ✅ `GetShadowColor() → colorR: number, colorG: number, colorB: number, colorA: number`
- ✅ `GetShadowOffset() → offsetX: number, offsetY: number`
- ✅ `GetSpacing() → spacing: uiUnit`
- ✅ `GetTextColor() → colorR: number, colorG: number, colorB: number, colorA: number`
- ✅ `HasAccessConstraints() → hasAccessConstraints: bool` — Returns whether this object has any access constraints that may limit access from some Lua execution contexts. (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `HasAnyAccessRestrictions(restrictions: ScriptObjectAccessRestriction?) → hasAnyAccessRestriction: bool` — Returns true if this object has any of the supplied access restrictions applied. (secret arguments: AllowedWhenUntainted; SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `HasAnyForbiddenAspects(aspects: ForbiddenAspect?) → hasAnyForbiddenAspect: bool` — Returns true if this object has any of the supplied forbidden aspects added. (secret arguments: AllowedWhenUntainted; SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `HasAnySecretAspect() → hasSecretAspect: bool` (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecrets'])
- ✅ `HasSecretAspect(aspect: SecretAspect) → hasSecretAspect: bool` (ConstSecretAccessor; secret arguments: AllowedWhenUntainted; SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecrets'])
- ✅ `HasSecretValues() → hasSecretValues: bool` (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecrets'])
- ✅ `IsForbidden() → isForbidden: bool` — Returns whether this object has been explicitly marked as forbidden. (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecurity'])
- ✅ `IsObjectType(objectType: cstring) → isType: bool` (ConstSecretAccessor; secret arguments: AllowedWhenUntainted; SecretReturnsForAspect: ['Enum.SecretAspect.ObjectType'])
- ✅ `IsPreventingSecretValues() → isPreventingSecretValues: bool` (SecretReturnsForAspect: ['Enum.SecretAspect.ObjectSecrets'])
- ✅ `SetAlpha(alpha: SingleColorValue)` (secret arguments: AllowedWhenUntainted)
- ✅ `SetFont(fontFile: cstring, height: uiFontHeight, flags: TBFFlags)` (RequiresValidFontAsset; RequiresValidFontHeight; secret arguments: AllowedWhenUntainted)
- ✅ `SetFontHeight(height: number)` — Preserves all flags, does correct height conversion due to fixedHeight. (secret arguments: AllowedWhenUntainted)
- ✅ `SetFontObject(font: SimpleFont)` (secret arguments: AllowedWhenUntainted)
- ✅ `SetForbidden()` (restricted in some situations)
- ✅ `SetIndentedWordWrap(wordWrap: bool)` (secret arguments: AllowedWhenUntainted)
- ✅ `SetJustifyH(justifyH: JustifyHorizontal)` (secret arguments: AllowedWhenUntainted)
- ✅ `SetJustifyV(justifyV: JustifyVertical)` (secret arguments: AllowedWhenUntainted)
- ✅ `SetShadowColor(colorR: number, colorG: number, colorB: number, a: SingleColorValue?)` (secret arguments: AllowedWhenUntainted)
- ✅ `SetShadowOffset(offsetX: number, offsetY: number)` (secret arguments: AllowedWhenUntainted)
- ✅ `SetSpacing(spacing: uiUnit)` (secret arguments: AllowedWhenUntainted)
- ✅ `SetTextColor(colorR: number, colorG: number, colorB: number, a: SingleColorValue?)` (secret arguments: AllowedWhenUntainted)
- ✅ `SetToDefaults()` — Reset all script accessible values to their default values. If possible, clears secret states. (ChecksForbiddenAspects: [{'Argument': 'self', 'Aspect': 'Enum.ForbiddenAspect.SetToDefaults'}, {'Argument': 'self', 'Aspect': 'Enum.ForbiddenAspect.RemoveSecretAspects'}]; protected: only Blizzard's secure code may call it)
