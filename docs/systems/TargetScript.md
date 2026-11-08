# TargetScript

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [AssistUnit](#assistunit) |  |  |
| ❔ | [AttackTarget](#attacktarget) |  |  |
| ❔ | [ClearFocus](#clearfocus) |  |  |
| ❔ | [ClearTarget](#cleartarget) |  |  |
| ❔ | [FocusUnit](#focusunit) |  |  |
| ❔ | [IsTargetLoose](#istargetloose) |  |  |
| ❔ | [SetPreferredGamepadInteractTarget](#setpreferredgamepadinteracttarget) |  |  |
| ❔ | [TargetDirectionEnemy](#targetdirectionenemy) |  |  |
| ❔ | [TargetDirectionFinished](#targetdirectionfinished) |  |  |
| ❔ | [TargetDirectionFriend](#targetdirectionfriend) |  |  |
| ❔ | [TargetLastEnemy](#targetlastenemy) |  |  |
| ❔ | [TargetLastFriend](#targetlastfriend) |  |  |
| ❔ | [TargetLastTarget](#targetlasttarget) |  |  |
| ❔ | [TargetNearest](#targetnearest) |  |  |
| ❔ | [TargetNearestEnemy](#targetnearestenemy) |  |  |
| ❔ | [TargetNearestEnemyPlayer](#targetnearestenemyplayer) |  |  |
| ❔ | [TargetNearestFriend](#targetnearestfriend) |  |  |
| ❔ | [TargetNearestFriendPlayer](#targetnearestfriendplayer) |  |  |
| ❔ | [TargetNearestPartyMember](#targetnearestpartymember) |  |  |
| ❔ | [TargetNearestRaidMember](#targetnearestraidmember) |  |  |
| ❔ | [TargetPriorityHighlightEnd](#targetpriorityhighlightend) |  |  |
| ❔ | [TargetPriorityHighlightStart](#targetpriorityhighlightstart) |  |  |
| ❔ | [TargetToggle](#targettoggle) |  |  |
| ❔ | [TargetUnit](#targetunit) |  |  |

### AssistUnit

`AssistUnit(name: cstring = , exactMatch: bool = False)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TargetScriptDocumentation.lua`

### AttackTarget

`AttackTarget()`

- Status: ❔ unverified
- Source: client docs `TargetScriptDocumentation.lua`

### ClearFocus

`ClearFocus()`

- Status: ❔ unverified
- Source: client docs `TargetScriptDocumentation.lua`

### ClearTarget

`ClearTarget() → willMakeChange: bool`

- Status: ❔ unverified
- Source: client docs `TargetScriptDocumentation.lua`

### FocusUnit

`FocusUnit(name: cstring = )`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TargetScriptDocumentation.lua`

### IsTargetLoose

`IsTargetLoose() → isTargetLoose: bool`

- Status: ❔ unverified
- Source: client docs `TargetScriptDocumentation.lua`

### SetPreferredGamepadInteractTarget

`SetPreferredGamepadInteractTarget(unit: UnitToken?)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TargetScriptDocumentation.lua`

### TargetDirectionEnemy

`TargetDirectionEnemy(facing: number, coneAngle: number?)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TargetScriptDocumentation.lua`

### TargetDirectionFinished

`TargetDirectionFinished()`

- Status: ❔ unverified
- Source: client docs `TargetScriptDocumentation.lua`

### TargetDirectionFriend

`TargetDirectionFriend(facing: number, coneAngle: number?)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TargetScriptDocumentation.lua`

### TargetLastEnemy

`TargetLastEnemy()`

- Status: ❔ unverified
- Source: client docs `TargetScriptDocumentation.lua`

### TargetLastFriend

`TargetLastFriend()`

- Status: ❔ unverified
- Source: client docs `TargetScriptDocumentation.lua`

### TargetLastTarget

`TargetLastTarget()`

- Status: ❔ unverified
- Source: client docs `TargetScriptDocumentation.lua`

### TargetNearest

`TargetNearest(reverse: bool = False)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TargetScriptDocumentation.lua`

### TargetNearestEnemy

`TargetNearestEnemy(reverse: bool = False)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TargetScriptDocumentation.lua`

### TargetNearestEnemyPlayer

`TargetNearestEnemyPlayer(reverse: bool = False)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TargetScriptDocumentation.lua`

### TargetNearestFriend

`TargetNearestFriend(reverse: bool = False)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TargetScriptDocumentation.lua`

### TargetNearestFriendPlayer

`TargetNearestFriendPlayer(reverse: bool = False)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TargetScriptDocumentation.lua`

### TargetNearestPartyMember

`TargetNearestPartyMember(reverse: bool = False)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TargetScriptDocumentation.lua`

### TargetNearestRaidMember

`TargetNearestRaidMember(reverse: bool = False)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TargetScriptDocumentation.lua`

### TargetPriorityHighlightEnd

`TargetPriorityHighlightEnd()`

- Status: ❔ unverified
- Source: client docs `TargetScriptDocumentation.lua`

### TargetPriorityHighlightStart

`TargetPriorityHighlightStart(useStartDelay: bool = False)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TargetScriptDocumentation.lua`

### TargetToggle

`TargetToggle()`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `TargetScriptDocumentation.lua`

### TargetUnit

`TargetUnit(name: cstring = , exactMatch: bool = False)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TargetScriptDocumentation.lua`
