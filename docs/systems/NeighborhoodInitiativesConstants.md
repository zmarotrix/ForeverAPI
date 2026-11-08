# NeighborhoodInitiativesConstants

## Types

### InitiativeMilestoneFlags

- Enumeration — ✅ verified
  - `FinalMilestone` = 1

### InitiativeRewardFlags

- Enumeration — ✅ verified
  - `PermanentWorldState` = 1

### NeighborhoodInitiativeChestResult

- Enumeration — ✅ verified
  - `NiSuccess` = 0
  - `NiUnspecifiedFailure` = 1
  - `NiNoHouseFound` = 2
  - `NiNoRewards` = 3
  - `NiThrottled` = 4
  - `NiServiceDisabled` = 5

### NeighborhoodInitiativeFlags

- Enumeration — ✅ verified
  - `Disabled` = 1
  - `NoAbandon` = 2
  - `NoRepeat` = 4

### NeighborhoodInitiativeNeighborhoodTypes

- Enumeration — ✅ verified
  - `NiNeighborhoodTypeSingleton` = 0
  - `NiNeighborhoodTypePool` = 1

### NeighborhoodInitiativeTaskType

- Enumeration — ✅ verified
  - `Single` = 0
  - `RepeatableFinite` = 1
  - `RepeatableInfinite` = 2

### NeighborhoodInitiativeUpdateStatus

- Enumeration — ✅ verified
  - `Started` = 0
  - `MilestoneCompleted` = 1
  - `Completed` = 2
  - `Failed` = 3

### NeighborhoodInitiativesCompletionStates

- Enumeration — ✅ verified
  - `NiCompletionStateNotCompleted` = 0
  - `NiCompletionStatePlayerCompleted` = 1
  - `NiCompletionStateSystemAbandoned` = 2
