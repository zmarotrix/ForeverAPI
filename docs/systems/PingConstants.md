# PingConstants

## Types

### PingMode

- Enumeration — ✅ verified
  - `KeyDown` = 0
  - `ClickDrag` = 1

### PingResult

- Enumeration — ✅ verified
  - `Success` = 0
  - `FailedGeneric` = 1
  - `FailedSpamming` = 2
  - `FailedDisabledByLeader` = 3
  - `FailedDisabledBySettings` = 4
  - `FailedOutOfPingArea` = 5
  - `FailedSquelched` = 6
  - `FailedUnspecified` = 7
  - `FailedSilent` = 8

### PingSetTargetState

- Enumeration — ✅ verified
  - `Ok` = 0
  - `Failed` = 1
  - `FailedSilent` = 2

### PingSubjectType

- Enumeration — ✅ verified
  - `Attack` = 0
  - `Warning` = 1
  - `Assist` = 2
  - `OnMyWay` = 3
  - `AlertThreat` = 4
  - `AlertNotThreat` = 5
  - `ActionReady` = 6
  - `ActionOnCooldown` = 7
  - `ActionUnavailable` = 8
  - `ActionNotReady` = 9

### PingTargetOption

- Enumeration — ✅ verified
  - `All` = 0
  - `Environment` = 1
  - `Units` = 2

### PingTargetType

- Enumeration — ✅ verified
  - `Unit` = 0
  - `Point` = 1
  - `Action` = 2

### PingTypeFlags

- Enumeration — ✅ verified
  - `DefaultPing` = 1
