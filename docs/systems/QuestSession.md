# QuestSession

Namespace: `C_QuestSession`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_QuestSession.CanStart](#c_questsessioncanstart) |  |  |
| ❔ | [C_QuestSession.CanStop](#c_questsessioncanstop) |  |  |
| ❔ | [C_QuestSession.Exists](#c_questsessionexists) |  |  |
| ❔ | [C_QuestSession.GetAvailableSessionCommand](#c_questsessiongetavailablesessioncommand) |  |  |
| ❔ | [C_QuestSession.GetPendingCommand](#c_questsessiongetpendingcommand) |  |  |
| ❔ | [C_QuestSession.GetProposedMaxLevelForSession](#c_questsessiongetproposedmaxlevelforsession) |  |  |
| ❔ | [C_QuestSession.GetSessionBeginDetails](#c_questsessiongetsessionbegindetails) |  |  |
| ❔ | [C_QuestSession.GetSuperTrackedQuest](#c_questsessiongetsupertrackedquest) |  |  |
| ❔ | [C_QuestSession.HasJoined](#c_questsessionhasjoined) |  |  |
| ❔ | [C_QuestSession.HasPendingCommand](#c_questsessionhaspendingcommand) |  |  |
| ❔ | [C_QuestSession.RequestSessionStart](#c_questsessionrequestsessionstart) |  |  |
| ❔ | [C_QuestSession.RequestSessionStop](#c_questsessionrequestsessionstop) |  |  |
| ❔ | [C_QuestSession.SendSessionBeginResponse](#c_questsessionsendsessionbeginresponse) |  |  |
| ❔ | [C_QuestSession.SetQuestIsSuperTracked](#c_questsessionsetquestissupertracked) |  |  |

### C_QuestSession.CanStart

`C_QuestSession.CanStart() → allowed: bool`

- Status: ❔ unverified
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.CanStop

`C_QuestSession.CanStop() → allowed: bool`

- Status: ❔ unverified
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.Exists

`C_QuestSession.Exists() → exists: bool`

- Status: ❔ unverified
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.GetAvailableSessionCommand

`C_QuestSession.GetAvailableSessionCommand() → command: QuestSessionCommand`

- Status: ❔ unverified
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.GetPendingCommand

`C_QuestSession.GetPendingCommand() → command: QuestSessionCommand`

- Status: ❔ unverified
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.GetProposedMaxLevelForSession

`C_QuestSession.GetProposedMaxLevelForSession() → proposedMaxLevel: number`

- Status: ❔ unverified
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.GetSessionBeginDetails

`C_QuestSession.GetSessionBeginDetails() → details: QuestSessionPlayerDetails?`

- Status: ❔ unverified
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.GetSuperTrackedQuest

`C_QuestSession.GetSuperTrackedQuest() → questID: number?`

- Status: ❔ unverified
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.HasJoined

`C_QuestSession.HasJoined() → hasJoined: bool`

- Status: ❔ unverified
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.HasPendingCommand

`C_QuestSession.HasPendingCommand() → hasPendingCommand: bool`

- Status: ❔ unverified
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.RequestSessionStart

`C_QuestSession.RequestSessionStart()`

- Status: ❔ unverified
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.RequestSessionStop

`C_QuestSession.RequestSessionStop()`

- Status: ❔ unverified
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.SendSessionBeginResponse

`C_QuestSession.SendSessionBeginResponse(beginSession: bool)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.SetQuestIsSuperTracked

`C_QuestSession.SetQuestIsSuperTracked(questID: number, superTrack: bool)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `QuestSessionDocumentation.lua`

## Events

### QUEST_SESSION_CREATED

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

### QUEST_SESSION_DESTROYED

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

### QUEST_SESSION_ENABLED_STATE_CHANGED

- Status: ❔ unverified
- Payload: `enabled: bool`
- fires synchronously (Blizzard's docs)

### QUEST_SESSION_JOINED

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

### QUEST_SESSION_LEFT

- Status: ❔ unverified
- Payload: none
- unique event (Blizzard's docs)

### QUEST_SESSION_MEMBER_CONFIRM

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### QUEST_SESSION_MEMBER_START_RESPONSE

- Status: ❔ unverified
- Payload: `guid: WOWGUID`, `response: bool`
- fires synchronously (Blizzard's docs)

### QUEST_SESSION_NOTIFICATION

- Status: ❔ unverified
- Payload: `result: QuestSessionResult`, `guid: WOWGUID`
- fires synchronously (Blizzard's docs)

## Types

### QuestSessionPlayerDetails

- Structure
  - `name`: string
  - `guid`: WOWGUID
