# AddOns

Namespace: `C_AddOns`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_AddOns.DisableAddOn](#c_addonsdisableaddon) |  |  |
| ✅ | [C_AddOns.DisableAllAddOns](#c_addonsdisablealladdons) |  |  |
| ✅ | [C_AddOns.DoesAddOnExist](#c_addonsdoesaddonexist) |  |  |
| ✅ | [C_AddOns.DoesAddOnHaveLoadError](#c_addonsdoesaddonhaveloaderror) |  |  |
| ✅ | [C_AddOns.EnableAddOn](#c_addonsenableaddon) |  |  |
| ✅ | [C_AddOns.EnableAllAddOns](#c_addonsenablealladdons) |  |  |
| ✅ | [C_AddOns.GetAddOnDependencies](#c_addonsgetaddondependencies) |  |  |
| ✅ | [C_AddOns.GetAddOnEnableState](#c_addonsgetaddonenablestate) |  |  |
| ✅ | [C_AddOns.GetAddOnInfo](#c_addonsgetaddoninfo) |  |  |
| ✅ | [C_AddOns.GetAddOnInterfaceVersion](#c_addonsgetaddoninterfaceversion) |  |  |
| ✅ | [C_AddOns.GetAddOnLocalTable](#c_addonsgetaddonlocaltable) |  |  |
| ✅ | [C_AddOns.GetAddOnMetadata](#c_addonsgetaddonmetadata) |  |  |
| ✅ | [C_AddOns.GetAddOnName](#c_addonsgetaddonname) |  |  |
| ✅ | [C_AddOns.GetAddOnNotes](#c_addonsgetaddonnotes) |  |  |
| ✅ | [C_AddOns.GetAddOnOptionalDependencies](#c_addonsgetaddonoptionaldependencies) |  |  |
| ✅ | [C_AddOns.GetAddOnSecurity](#c_addonsgetaddonsecurity) |  |  |
| ✅ | [C_AddOns.GetAddOnTitle](#c_addonsgetaddontitle) |  |  |
| ✅ | [C_AddOns.GetNumAddOns](#c_addonsgetnumaddons) |  |  |
| ✅ | [C_AddOns.GetScriptsDisallowedForBeta](#c_addonsgetscriptsdisallowedforbeta) |  |  |
| ✅ | [C_AddOns.IsAddOnDefaultEnabled](#c_addonsisaddondefaultenabled) |  |  |
| ✅ | [C_AddOns.IsAddOnLoadOnDemand](#c_addonsisaddonloadondemand) |  |  |
| ✅ | [C_AddOns.IsAddOnLoadable](#c_addonsisaddonloadable) |  |  |
| ✅ | [C_AddOns.IsAddOnLoaded](#c_addonsisaddonloaded) |  |  |
| ✅ | [C_AddOns.IsAddonVersionCheckEnabled](#c_addonsisaddonversioncheckenabled) |  |  |
| ✅ | [C_AddOns.LoadAddOn](#c_addonsloadaddon) |  |  |
| ✅ | [C_AddOns.ResetAddOns](#c_addonsresetaddons) |  |  |
| ✅ | [C_AddOns.ResetDisabledAddOns](#c_addonsresetdisabledaddons) |  |  |
| ✅ | [C_AddOns.SaveAddOns](#c_addonssaveaddons) |  |  |
| ✅ | [C_AddOns.SetAddonVersionCheck](#c_addonssetaddonversioncheck) |  |  |

### C_AddOns.DisableAddOn

`C_AddOns.DisableAddOn(name: uiAddon, character: cstring = 0)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.DisableAllAddOns

`C_AddOns.DisableAllAddOns(character: cstring?)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.DoesAddOnExist

`C_AddOns.DoesAddOnExist(name: uiAddon) → exists: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.DoesAddOnHaveLoadError

`C_AddOns.DoesAddOnHaveLoadError(name: uiAddon) → hadError: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.EnableAddOn

`C_AddOns.EnableAddOn(name: uiAddon, character: cstring = 0)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.EnableAllAddOns

`C_AddOns.EnableAllAddOns(character: cstring?)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.GetAddOnDependencies

`C_AddOns.GetAddOnDependencies(name: uiAddon) → deps: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.GetAddOnEnableState

`C_AddOns.GetAddOnEnableState(name: uiAddon, character: cstring = 0) → state: AddOnEnableState`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.GetAddOnInfo

`C_AddOns.GetAddOnInfo(name: uiAddon) → name: cstring, title: cstring, notes: cstring, loadable: bool, reason: cstring, security: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.GetAddOnInterfaceVersion

`C_AddOns.GetAddOnInterfaceVersion(name: uiAddon) → interfaceVersion: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.GetAddOnLocalTable

`C_AddOns.GetAddOnLocalTable(name: uiAddon) → table: LuaValueVariant`

- Status: ✅ verified (function)
- Blizzard: Returns the addon table (passed as the second argument of ... to files) for any addon that opts in through setting AllowAddOnTableAccess: 1 in the toc file. Insecure code cannot query addon tables from Blizzard addons.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.GetAddOnMetadata

`C_AddOns.GetAddOnMetadata(name: uiAddon, variable: cstring) → value: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.GetAddOnName

`C_AddOns.GetAddOnName(index: uiAddon) → name: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.GetAddOnNotes

`C_AddOns.GetAddOnNotes(name: uiAddon) → notes: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.GetAddOnOptionalDependencies

`C_AddOns.GetAddOnOptionalDependencies(name: uiAddon) → deps: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.GetAddOnSecurity

`C_AddOns.GetAddOnSecurity(name: uiAddon) → security: AddOnSecurityStatus`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.GetAddOnTitle

`C_AddOns.GetAddOnTitle(name: uiAddon) → title: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.GetNumAddOns

`C_AddOns.GetNumAddOns() → numAddOns: number`

- Status: ✅ verified (function)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.GetScriptsDisallowedForBeta

`C_AddOns.GetScriptsDisallowedForBeta() → disallowed: bool`

- Status: ✅ verified (function)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.IsAddOnDefaultEnabled

`C_AddOns.IsAddOnDefaultEnabled(name: uiAddon) → defaultEnabled: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.IsAddOnLoadOnDemand

`C_AddOns.IsAddOnLoadOnDemand(name: uiAddon) → loadOnDemand: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.IsAddOnLoadable

`C_AddOns.IsAddOnLoadable(name: uiAddon, character: cstring = 0, demandLoaded: bool = False) → loadable: bool, reason: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.IsAddOnLoaded

`C_AddOns.IsAddOnLoaded(name: uiAddon) → loadedOrLoading: bool, loaded: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.IsAddonVersionCheckEnabled

`C_AddOns.IsAddonVersionCheckEnabled() → isEnabled: bool`

- Status: ✅ verified (function)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.LoadAddOn

`C_AddOns.LoadAddOn(name: uiAddon) → loaded: bool?, value: string?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.ResetAddOns

`C_AddOns.ResetAddOns()`

- Status: ✅ verified (function)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.ResetDisabledAddOns

`C_AddOns.ResetDisabledAddOns()`

- Status: ✅ verified (function)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.SaveAddOns

`C_AddOns.SaveAddOns()`

- Status: ✅ verified (function)
- Source: client docs `AddOnsDocumentation.lua`

### C_AddOns.SetAddonVersionCheck

`C_AddOns.SetAddonVersionCheck(enabled: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AddOnsDocumentation.lua`

## Events

### ADDONS_UNLOADING

- Status: ✅ verified
- Payload: `closingClient: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: `b`

### ADDON_LOADED

- Status: ✅ verified
- Payload: `addOnName: cstring`, `containsBindings: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 33 times (0 in combat); argument kinds: `s,b`

### SAVED_VARIABLES_TOO_LARGE

- Status: ✅ verified
- Payload: `addOnName: cstring`
- fires synchronously (Blizzard's docs)

## Types

### AddOnInfo

- Structure
  - `name`: cstring
  - `title`: cstring
  - `notes`: cstring
  - `loadable`: bool
  - `reason`: cstring
  - `security`: cstring

### AddOnLoadableInfo

- Structure
  - `loadable`: bool
  - `reason`: cstring
