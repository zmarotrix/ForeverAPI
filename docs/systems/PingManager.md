# PingManager

Namespace: `C_Ping`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_Ping.GetCooldownInfo](#c_pinggetcooldowninfo) |  |  |
| ❔ | [C_Ping.GetDefaultPingOptions](#c_pinggetdefaultpingoptions) |  |  |
| ❔ | [C_Ping.GetTextureKitForType](#c_pinggettexturekitfortype) |  |  |
| ❔ | [C_Ping.IsPingSystemEnabled](#c_pingispingsystemenabled) |  |  |
| ❔ | [C_Ping.SendMacroPing](#c_pingsendmacroping) |  |  |
| ❔ | [C_Ping.TogglePingListener](#c_pingtogglepinglistener) |  |  |

### C_Ping.GetCooldownInfo

`C_Ping.GetCooldownInfo() → cooldownInfo: PingCooldownInfo`

- Status: ❔ unverified
- Source: client docs `PingManagerDocumentation.lua`

### C_Ping.GetDefaultPingOptions

`C_Ping.GetDefaultPingOptions() → pingTypes: PingTypeInfo[]`

- Status: ❔ unverified
- Source: client docs `PingManagerDocumentation.lua`

### C_Ping.GetTextureKitForType

`C_Ping.GetTextureKitForType(type: PingSubjectType) → uiTextureKitID: textureKit`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerDocumentation.lua`

### C_Ping.IsPingSystemEnabled

`C_Ping.IsPingSystemEnabled() → isEnabled: bool`

- Status: ❔ unverified
- Source: client docs `PingManagerDocumentation.lua`

### C_Ping.SendMacroPing

`C_Ping.SendMacroPing(macroInfo: PingMacroInfo)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerDocumentation.lua`

### C_Ping.TogglePingListener

`C_Ping.TogglePingListener(down: bool)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PingManagerDocumentation.lua`

## Events

### PING_SYSTEM_ERROR

- Status: ❔ unverified
- Payload: `error: cstring`
- fires synchronously (Blizzard's docs)

## Types

### PingTypeInfo

- Structure
  - `orderIndex`: number
  - `type`: PingSubjectType
  - `uiTextureKitID`: textureKit
