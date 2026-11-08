# SwingTimer

Namespace: `C_SwingTimer`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_SwingTimer.EnableRangeCheck](#c_swingtimerenablerangecheck) |  |  |
| ✅ | [C_SwingTimer.IsTargetWithinSwingRange](#c_swingtimeristargetwithinswingrange) |  |  |

### C_SwingTimer.EnableRangeCheck

`C_SwingTimer.EnableRangeCheck(swingType: PlayerSwingType, enable: bool)`

- Status: ✅ verified (function)
- Blizzard: Used in conjunction with PlayerSwingRangeUpdate to inform the UI when the current target goes in or out of auto attack range.
- `enable`: True if changes in range for the swing type should dispatch PlayerSwingRangeUpdate. False if the swing type no longer needs the event.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SwingTimerDocumentation.lua`

### C_SwingTimer.IsTargetWithinSwingRange

`C_SwingTimer.IsTargetWithinSwingRange(swingType: PlayerSwingType) → isInRange: bool?`

- Status: ✅ verified (function)
- Blizzard: Whether the current target is within range of the player's auto attack for the given swing type. Auto attacks only ever apply to the current target, so no other unit can be queried.
- `isInRange`: Nil when no range check could be made, for example there is no target, the target cannot be attacked, or no weapon is equipped for the swing type. Nil must not be treated as out of range.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SwingTimerDocumentation.lua`

## Events

### PLAYER_SWING

- Status: ✅ verified
- Payload: `swingDuration: number`, `swingType: PlayerSwingType`
- fires synchronously (Blizzard's docs)
- Seen firing 147 times (147 in combat); argument kinds: `n,n`

### PLAYER_SWING_RANGE_UPDATE

- Status: ✅ verified
- Payload: `swingType: PlayerSwingType`, `isInRange: bool`, `checksRange: bool`
- Blizzard: Only signaled for swing types that have an active range check. See C_SwingTimer.EnableRangeCheck.
- fires synchronously (Blizzard's docs)

## Types

### PlayerSwingType

- Enumeration — ✅ verified
  - `MainHand` = 0
  - `OffHand` = 1
  - `Ranged` = 2
