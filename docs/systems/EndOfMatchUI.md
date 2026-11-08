# EndOfMatchUI

Namespace: `C_EndOfMatchUI`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_EndOfMatchUI.GetEndOfMatchDetails](#c_endofmatchuigetendofmatchdetails) |  |  |

### C_EndOfMatchUI.GetEndOfMatchDetails

`C_EndOfMatchUI.GetEndOfMatchDetails() → matchDetails: MatchDetails?`

- Status: ❔ unverified
- Source: client docs `EndOfMatchUIDocumentation.lua`

## Events

### SHOW_END_OF_MATCH_UI

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### EndOfMatchType

- Enumeration — ❔ unverified
  - `None` = 0
  - `Plunderstorm` = 1

### MatchDetail

- Structure
  - `type`: MatchDetailType
  - `value`: number

### MatchDetailType

- Enumeration — ❔ unverified
  - `Placement` = 0
  - `Kills` = 1
  - `PlunderAcquired` = 2

### MatchDetails

- Structure
  - `matchType`: EndOfMatchType
  - `matchEnded`: bool
  - `detailsList`: MatchDetail[]
