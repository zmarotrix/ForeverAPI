# FrameScript

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [AddSourceLocationExclude](#addsourcelocationexclude) |  |  |
| ❔ | [CreateFrameWithOptions](#createframewithoptions) |  |  |
| ❔ | [CreateFromMixins](#createfrommixins) |  |  |
| ❔ | [CreateSecureDelegate](#createsecuredelegate) |  |  |
| ❔ | [CreateWindow](#createwindow) |  |  |
| ❔ | [GetCallstackHeight](#getcallstackheight) |  |  |
| ❔ | [GetCurrentEventID](#getcurrenteventid) |  |  |
| ❔ | [GetErrorCallstackHeight](#geterrorcallstackheight) |  |  |
| ❔ | [GetEventTime](#geteventtime) |  |  |
| ❔ | [GetForbiddenObjectTable](#getforbiddenobjecttable) |  |  |
| ❔ | [GetScriptBucketThrottleLimits](#getscriptbucketthrottlelimits) |  |  |
| ❔ | [GetSourceLocation](#getsourcelocation) |  |  |
| ❔ | [Mixin](#mixin) |  |  |
| ❔ | [RegisterEventCallback](#registereventcallback) |  |  |
| ❔ | [RegisterUnitEventCallback](#registeruniteventcallback) |  |  |
| ❔ | [RunScript](#runscript) |  |  |
| ❔ | [SetErrorCallstackHeight](#seterrorcallstackheight) |  |  |
| ❔ | [UnregisterEventCallback](#unregistereventcallback) |  |  |
| ❔ | [UnregisterUnitEventCallback](#unregisteruniteventcallback) |  |  |
| ❔ | [canaccessallvalues](#canaccessallvalues) |  |  |
| ❔ | [canaccesssecrets](#canaccesssecrets) |  |  |
| ❔ | [canaccesstable](#canaccesstable) |  |  |
| ❔ | [canaccessvalue](#canaccessvalue) |  |  |
| ❔ | [debugprofilestart](#debugprofilestart) |  |  |
| ❔ | [debugprofilestop](#debugprofilestop) |  |  |
| ❔ | [dropsecretaccess](#dropsecretaccess) |  |  |
| ❔ | [dumpobject](#dumpobject) |  |  |
| ❔ | [hasanysecretvalues](#hasanysecretvalues) |  |  |
| ❔ | [issecrettable](#issecrettable) |  |  |
| ❔ | [issecretvalue](#issecretvalue) |  |  |
| ❔ | [mapvalues](#mapvalues) |  |  |
| ❔ | [scrub](#scrub) |  |  |
| ❔ | [scrubsecretvalues](#scrubsecretvalues) |  |  |
| ❔ | [secretunwrap](#secretunwrap) |  |  |
| ❔ | [secretwrap](#secretwrap) |  |  |
| ❔ | [securecallmethod](#securecallmethod) |  |  |
| ❔ | [securecopy](#securecopy) |  |  |
| ❔ | [settablesecurity](#settablesecurity) |  |  |

### AddSourceLocationExclude

`AddSourceLocationExclude(fileName: cstring)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### CreateFrameWithOptions

`CreateFrameWithOptions(options: CreateFrameOptions) → frame: SimpleFrame`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### CreateFromMixins

`CreateFromMixins(mixins: LuaValueVariant) → object: LuaValueVariant`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### CreateSecureDelegate

`CreateSecureDelegate(luaFunction: LuaValueReference, options: SecureDelegateOptions?) → secureDelegateFunction: LuaValueReference`

- Status: ❔ unverified
- Blizzard: Creates a secure delegate closure for a Lua function. The delegate invokes the original function in a protected call context with secure execution taint, and supports passing and returning values directly.
- `luaFunction`: The Lua function to invoke through the secure delegate.
- `options`: Optional settings controlling secure delegate behavior. If omitted, default options are used.
- `secureDelegateFunction`: A secure delegate function that calls through to the original Lua function.
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### CreateWindow

`CreateWindow(popupStyle: bool = True, topMost: bool = False) → window: SimpleWindow?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### GetCallstackHeight

`GetCallstackHeight() → height: number`

- Status: ❔ unverified
- Source: client docs `FrameScriptDocumentation.lua`

### GetCurrentEventID

`GetCurrentEventID() → eventID: number?`

- Status: ❔ unverified
- Source: client docs `FrameScriptDocumentation.lua`

### GetErrorCallstackHeight

`GetErrorCallstackHeight() → height: number?`

- Status: ❔ unverified
- Source: client docs `FrameScriptDocumentation.lua`

### GetEventTime

`GetEventTime(eventProfileIndex: number) → totalElapsedTime: number, numExecutedHandlers: number, slowestHandlerName: cstring, slowestHandlerTime: number`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### GetForbiddenObjectTable

`GetForbiddenObjectTable(object: FrameScriptObject) → forbiddenTable: FrameScriptObject`

- Status: ❔ unverified
- Environment: SecureOnly (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### GetScriptBucketThrottleLimits

`GetScriptBucketThrottleLimits() → limits: ScriptBucketThrottleLimits`

- Status: ❔ unverified
- Source: client docs `FrameScriptDocumentation.lua`

### GetSourceLocation

`GetSourceLocation() → location: string`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### Mixin

`Mixin(object: LuaValueVariant, mixins: LuaValueVariant) → outObject: LuaValueVariant`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### RegisterEventCallback

`RegisterEventCallback(eventName: cstring, callback: EventCallbackType)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### RegisterUnitEventCallback

`RegisterUnitEventCallback(eventName: cstring, callback: EventCallbackType, unit: UnitToken)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### RunScript

`RunScript(text: cstring)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### SetErrorCallstackHeight

`SetErrorCallstackHeight(height: number?)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### UnregisterEventCallback

`UnregisterEventCallback(eventName: cstring, callback: EventCallbackType)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### UnregisterUnitEventCallback

`UnregisterUnitEventCallback(eventName: cstring, callback: EventCallbackType, unit: UnitToken)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### canaccessallvalues

`canaccessallvalues(values: LuaValueReference) → canAccessAllValues: bool`

- Status: ❔ unverified
- Blizzard: Returns true if the immediate calling function has appropriate permissions to access and operate on all supplied values.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### canaccesssecrets

`canaccesssecrets() → canAccessSecrets: bool`

- Status: ❔ unverified
- Blizzard: Returns true if the immediate calling function has appropriate permissions to access or operate on secret values.
- Source: client docs `FrameScriptDocumentation.lua`

### canaccesstable

`canaccesstable(table: LuaValueReference) → canAccessTable: bool`

- Status: ❔ unverified
- Blizzard: Returns true if the immediate calling function has appropriate permissions to index secret tables. This will return false if the caller cannot access the table value itself, or if access to the table contents is disallowed by taint.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### canaccessvalue

`canaccessvalue(value: LuaValueReference) → canAccessValue: bool`

- Status: ❔ unverified
- Blizzard: Returns true if the immediate calling function has appropriate permissions to access and operate on a specific value.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### debugprofilestart

`debugprofilestart()`

- Status: ❔ unverified
- Blizzard: Starts a timer for profiling. The final time can be obtained by calling debugprofilestop.
- Source: client docs `FrameScriptDocumentation.lua`

### debugprofilestop

`debugprofilestop() → elapsedMilliseconds: number`

- Status: ❔ unverified
- Blizzard: Returns the time in milliseconds since the last debugprofilestart call.
- Source: client docs `FrameScriptDocumentation.lua`

### dropsecretaccess

`dropsecretaccess()`

- Status: ❔ unverified
- Blizzard: Removes the ability for the immediate calling function to access secret values.
- Source: client docs `FrameScriptDocumentation.lua`

### dumpobject

`dumpobject(value: LuaValueReference?) → result: LuaValueReference?`

- Status: ❔ unverified
- Blizzard: Invokes the '__dump' metamethod on any value (if present), returning its result.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### hasanysecretvalues

`hasanysecretvalues(values: LuaValueReference) → isAnyValueSecret: bool`

- Status: ❔ unverified
- Blizzard: Returns true if a supplied value is a secret value.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### issecrettable

`issecrettable(table: LuaValueReference) → isSecretOrContentsSecret: bool`

- Status: ❔ unverified
- Blizzard: Returns true if a supplied value is a secret table. This function will return true if the table value itself is secret, or if flags on the table are set such that accesses of the table would produce secrets.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### issecretvalue

`issecretvalue(value: LuaValueReference) → isSecret: bool`

- Status: ❔ unverified
- Blizzard: Returns true if a supplied value is a secret value.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### mapvalues

`mapvalues(func: LuaValueReference, values: LuaValueReference) → mapped: LuaValueReference`

- Status: ❔ unverified
- Blizzard: Applies a given function over all supplied values individually, replacing the value with the result of the call.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### scrub

`scrub(values: LuaValueReference) → scrubbed: LuaValueReference`

- Status: ❔ unverified
- Blizzard: Returns a transformed list of values with inputs that are either secret or are not string, number, or boolean type replaced by nil values.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### scrubsecretvalues

`scrubsecretvalues(values: LuaValueReference) → scrubbed: LuaValueReference`

- Status: ❔ unverified
- Blizzard: Returns a transformed list of values with inputs that are secret values replaced by nil values.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### secretunwrap

`secretunwrap(values: LuaValueReference) → unwrapped: LuaValueReference`

- Status: ❔ unverified
- Blizzard: Unwraps all supplied secrets, converting them back to regular values.
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### secretwrap

`secretwrap(values: LuaValueReference) → wrapped: LuaValueReference`

- Status: ❔ unverified
- Blizzard: Converts all supplied values to secret values, preventing most operations on them from occurring on tainted code paths.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### securecallmethod

`securecallmethod(object: LuaValueReference, method: cstring, arguments: LuaValueReference) → results: LuaValueReference`

- Status: ❔ unverified
- Blizzard: Invokes a named method on an object with a secure call barrier that prevents errors or taint from function lookup and execution from propagating to the caller.
- `object`: The table on which to look up the named method from. Lookup of the method uses raw access and ignores any associated metatable.
- `method`: The name of a method to retrieve.
- `arguments`: Arguments to supply to the method. The initial 'object' parameter is always supplied as the first argument, followed by these values.
- `results`: Results from the executed function. If an error occurred, this result list will be empty.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### securecopy

`securecopy(value: LuaValueReference?, options: SecureCopyOptions?) → copy: LuaValueReference`

- Status: ❔ unverified
- Blizzard: Securely copies a Lua value. Tables are deep-copied with recursive and shared references preserved. Copied values receive the current execution taint.
- `value`: The Lua value to copy.
- `options`: Optional settings controlling value copying behavior. If omitted, default secure copy options are used.
- `copy`: The copied value. For tables, recursive and shared references within the copied graph are preserved.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

### settablesecurity

`settablesecurity(table: LuaValueVariant, option: TableSecurityOption)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FrameScriptDocumentation.lua`

## Types

### CreateFrameOptions

- Structure
  - `frameType`: cstring
  - `name`: cstring?
  - `parent`: SimpleFrame?
  - `inherits`: cstring[]?
  - `id`: number?
  - `forbidden`: bool
  - `hidden`: bool

### EventCallbackType

- CallbackType

### ScriptBucketThrottleLimits

- Structure
  - `luaScriptBucketThrottleMaxMsPerSecondNormal`: number
  - `luaScriptBucketThrottleMaxMsPerSecondRestricted`: number
  - `luaScriptBucketThrottleMaxMsBurstNormal`: number
  - `luaScriptBucketThrottleMaxMsBurstRestricted`: number

### SecureCopyOptions

- Structure
  - `maxTraversalDepth`: number
  - `wrapUntrustedFunctions`: bool
  - `permitScriptObjects`: bool

### SecureDelegateOptions

- Structure
  - `wrapUntrustedFunctions`: bool

### TableSecurityOption

- Enumeration — ❔ unverified
  - `DisallowTaintedAccess` = 0
  - `DisallowSecretKeys` = 1
  - `SecretWrapContents` = 2
