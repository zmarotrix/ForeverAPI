# BlizzCon2026Scripts

Namespace: `C_BlizzCon2026`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_BlizzCon2026.GetExperience](#c_blizzcon2026getexperience) |  |  |
| ✅ | [C_BlizzCon2026.IsActive](#c_blizzcon2026isactive) |  |  |
| ✅ | [C_BlizzCon2026.IsColdSwapFeatureEnabled](#c_blizzcon2026iscoldswapfeatureenabled) |  |  |
| ✅ | [C_BlizzCon2026.SetExperience](#c_blizzcon2026setexperience) |  |  |

### C_BlizzCon2026.GetExperience

`C_BlizzCon2026.GetExperience() → experience: Bc26Experience`

- Status: ✅ verified (function)
- Source: client docs `BlizzCon2026Documentation.lua`

### C_BlizzCon2026.IsActive

`C_BlizzCon2026.IsActive() → isActive: bool`

- Status: ✅ verified (function)
- Source: client docs `BlizzCon2026Documentation.lua`

### C_BlizzCon2026.IsColdSwapFeatureEnabled

`C_BlizzCon2026.IsColdSwapFeatureEnabled() → isEnabled: bool`

- Status: ✅ verified (function)
- Source: client docs `BlizzCon2026Documentation.lua`

### C_BlizzCon2026.SetExperience

`C_BlizzCon2026.SetExperience(experience: Bc26Experience)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BlizzCon2026Documentation.lua`

## Events

### BC_26_COLD_SWAP_FEATURE_ENABLED_CHANGED

- Status: ✅ verified
- Payload: `newEnabled: bool`, `oldEnabled: bool`
- unique event (Blizzard's docs)

### BC_26_EXPERIENCE_CHANGED

- Status: ✅ verified
- Payload: `newExperience: Bc26Experience`, `oldExperience: Bc26Experience`
- unique event (Blizzard's docs)

## Types

### Bc26Experience

- Enumeration — ✅ verified
  - `Skyborne` = 0
  - `Dungeon` = 1
