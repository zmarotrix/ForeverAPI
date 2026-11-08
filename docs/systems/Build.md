# Build

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [GetBuildInfo](#getbuildinfo) |  |  |
| ❔ | [GetBuildOption](#getbuildoption) |  |  |
| ❔ | [Is64BitClient](#is64bitclient) |  |  |
| ❔ | [IsBetaBuild](#isbetabuild) |  |  |
| ❔ | [IsDebugBuild](#isdebugbuild) |  |  |
| ❔ | [IsLinuxClient](#islinuxclient) |  |  |
| ❔ | [IsMacClient](#ismacclient) |  |  |
| ❔ | [IsPublicBuild](#ispublicbuild) |  |  |
| ❔ | [IsPublicTestClient](#ispublictestclient) |  |  |
| ❔ | [IsTestBuild](#istestbuild) |  |  |
| ❔ | [IsWindowsClient](#iswindowsclient) |  |  |
| ❔ | [SupportsClipCursor](#supportsclipcursor) |  |  |

### GetBuildInfo

`GetBuildInfo() → buildVersion: cstring, buildNumber: cstring, buildDate: cstring, interfaceVersion: number, localizedVersion: cstring, buildInfo: string`

- Status: ❔ unverified
- Source: client docs `BuildDocumentation.lua`

### GetBuildOption

`GetBuildOption(name: cstring) → isSet: bool?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BuildDocumentation.lua`

### Is64BitClient

`Is64BitClient() → is64Bit: bool`

- Status: ❔ unverified
- Source: client docs `BuildDocumentation.lua`

### IsBetaBuild

`IsBetaBuild() → isBetaBuild: bool`

- Status: ❔ unverified
- Source: client docs `BuildDocumentation.lua`

### IsDebugBuild

`IsDebugBuild() → isDebugBuild: bool`

- Status: ❔ unverified
- Source: client docs `BuildDocumentation.lua`

### IsLinuxClient

`IsLinuxClient() → isLinux: bool`

- Status: ❔ unverified
- Source: client docs `BuildDocumentation.lua`

### IsMacClient

`IsMacClient() → isMac: bool`

- Status: ❔ unverified
- Source: client docs `BuildDocumentation.lua`

### IsPublicBuild

`IsPublicBuild() → isPublicBuild: bool`

- Status: ❔ unverified
- Source: client docs `BuildDocumentation.lua`

### IsPublicTestClient

`IsPublicTestClient() → isPublicTestClient: bool`

- Status: ❔ unverified
- Blizzard: Reflects the state of the OnlyBetaAndPTR TOC directive
- Source: client docs `BuildDocumentation.lua`

### IsTestBuild

`IsTestBuild() → isTestBuild: bool`

- Status: ❔ unverified
- Source: client docs `BuildDocumentation.lua`

### IsWindowsClient

`IsWindowsClient() → isWindows: bool`

- Status: ❔ unverified
- Source: client docs `BuildDocumentation.lua`

### SupportsClipCursor

`SupportsClipCursor() → supportsClipCursor: bool`

- Status: ❔ unverified
- Source: client docs `BuildDocumentation.lua`
