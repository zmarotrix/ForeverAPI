# Build

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [GetBuildInfo](#getbuildinfo) |  |  |
| ✅ | [GetBuildOption](#getbuildoption) |  |  |
| ✅ | [Is64BitClient](#is64bitclient) |  |  |
| ✅ | [IsBetaBuild](#isbetabuild) |  |  |
| ✅ | [IsDebugBuild](#isdebugbuild) |  |  |
| ✅ | [IsLinuxClient](#islinuxclient) |  |  |
| ✅ | [IsMacClient](#ismacclient) |  |  |
| ✅ | [IsPublicBuild](#ispublicbuild) |  |  |
| ✅ | [IsPublicTestClient](#ispublictestclient) |  |  |
| ✅ | [IsTestBuild](#istestbuild) |  |  |
| ✅ | [IsWindowsClient](#iswindowsclient) |  |  |
| ✅ | [SupportsClipCursor](#supportsclipcursor) |  |  |

### GetBuildInfo

`GetBuildInfo() → buildVersion: cstring, buildNumber: cstring, buildDate: cstring, interfaceVersion: number, localizedVersion: cstring, buildInfo: string`

- Status: ✅ verified (function)
- Source: client docs `BuildDocumentation.lua`

### GetBuildOption

`GetBuildOption(name: cstring) → isSet: bool?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BuildDocumentation.lua`

### Is64BitClient

`Is64BitClient() → is64Bit: bool`

- Status: ✅ verified (function)
- Source: client docs `BuildDocumentation.lua`

### IsBetaBuild

`IsBetaBuild() → isBetaBuild: bool`

- Status: ✅ verified (function)
- Source: client docs `BuildDocumentation.lua`

### IsDebugBuild

`IsDebugBuild() → isDebugBuild: bool`

- Status: ✅ verified (function)
- Source: client docs `BuildDocumentation.lua`

### IsLinuxClient

`IsLinuxClient() → isLinux: bool`

- Status: ✅ verified (function)
- Source: client docs `BuildDocumentation.lua`

### IsMacClient

`IsMacClient() → isMac: bool`

- Status: ✅ verified (function)
- Source: client docs `BuildDocumentation.lua`

### IsPublicBuild

`IsPublicBuild() → isPublicBuild: bool`

- Status: ✅ verified (function)
- Source: client docs `BuildDocumentation.lua`

### IsPublicTestClient

`IsPublicTestClient() → isPublicTestClient: bool`

- Status: ✅ verified (function)
- Blizzard: Reflects the state of the OnlyBetaAndPTR TOC directive
- Source: client docs `BuildDocumentation.lua`

### IsTestBuild

`IsTestBuild() → isTestBuild: bool`

- Status: ✅ verified (function)
- Source: client docs `BuildDocumentation.lua`

### IsWindowsClient

`IsWindowsClient() → isWindows: bool`

- Status: ✅ verified (function)
- Source: client docs `BuildDocumentation.lua`

### SupportsClipCursor

`SupportsClipCursor() → supportsClipCursor: bool`

- Status: ✅ verified (function)
- Source: client docs `BuildDocumentation.lua`
