# Build

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [GetBuildInfo](#getbuildinfo) | 6 values |  |
| ✅ | [GetBuildOption](#getbuildoption) |  |  |
| ✅ | [Is64BitClient](#is64bitclient) | 1 value |  |
| ✅ | [IsBetaBuild](#isbetabuild) | 1 value |  |
| ✅ | [IsDebugBuild](#isdebugbuild) | 1 value |  |
| ✅ | [IsLinuxClient](#islinuxclient) | 1 value |  |
| ✅ | [IsMacClient](#ismacclient) | 1 value |  |
| ✅ | [IsPublicBuild](#ispublicbuild) | 1 value |  |
| ✅ | [IsPublicTestClient](#ispublictestclient) | 1 value |  |
| ✅ | [IsTestBuild](#istestbuild) | 1 value |  |
| ✅ | [IsWindowsClient](#iswindowsclient) | 1 value |  |
| ✅ | [SupportsClipCursor](#supportsclipcursor) |  |  |

### GetBuildInfo

`GetBuildInfo() → buildVersion: cstring, buildNumber: cstring, buildDate: cstring, interfaceVersion: number, localizedVersion: cstring, buildInfo: string`

- Status: ✅ verified (function)
- Called out of combat: returned 6 values: `string`, `string`, `string`, `number`, `string`, `string`
- Source: client docs `BuildDocumentation.lua`

### GetBuildOption

`GetBuildOption(name: cstring) → isSet: bool?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BuildDocumentation.lua`

### Is64BitClient

`Is64BitClient() → is64Bit: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `BuildDocumentation.lua`

### IsBetaBuild

`IsBetaBuild() → isBetaBuild: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `BuildDocumentation.lua`

### IsDebugBuild

`IsDebugBuild() → isDebugBuild: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `BuildDocumentation.lua`

### IsLinuxClient

`IsLinuxClient() → isLinux: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `BuildDocumentation.lua`

### IsMacClient

`IsMacClient() → isMac: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `BuildDocumentation.lua`

### IsPublicBuild

`IsPublicBuild() → isPublicBuild: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `BuildDocumentation.lua`

### IsPublicTestClient

`IsPublicTestClient() → isPublicTestClient: bool`

- Status: ✅ verified (function)
- Blizzard: Reflects the state of the OnlyBetaAndPTR TOC directive
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `BuildDocumentation.lua`

### IsTestBuild

`IsTestBuild() → isTestBuild: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `BuildDocumentation.lua`

### IsWindowsClient

`IsWindowsClient() → isWindows: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `BuildDocumentation.lua`

### SupportsClipCursor

`SupportsClipCursor() → supportsClipCursor: bool`

- Status: ✅ verified (function)
- Source: client docs `BuildDocumentation.lua`
