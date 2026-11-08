# LimitedInput

Namespace: `C_LimitedInput`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_LimitedInput.LimitedInputAllowed](#c_limitedinputlimitedinputallowed) |  |  |

### C_LimitedInput.LimitedInputAllowed

`C_LimitedInput.LimitedInputAllowed(type: LimitedInputType) → allowed: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LimitedInputDocumentation.lua`

## Types

### LimitedInputType

- Enumeration — ✅ verified
  - `MouseMove` = 0
  - `MouseDown` = 1
  - `MouseUp` = 2
  - `MouseWheel` = 3
