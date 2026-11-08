# QuestSession

Namespace: `C_QuestSession`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_QuestSession.CanStart](#c_questsessioncanstart) | 1 value | 1 value |
| ✅ | [C_QuestSession.CanStop](#c_questsessioncanstop) | 1 value | 1 value |
| ✅ | [C_QuestSession.Exists](#c_questsessionexists) |  |  |
| ✅ | [C_QuestSession.GetAvailableSessionCommand](#c_questsessiongetavailablesessioncommand) | 1 value | 1 value |
| ✅ | [C_QuestSession.GetPendingCommand](#c_questsessiongetpendingcommand) | 1 value | 1 value |
| ✅ | [C_QuestSession.GetProposedMaxLevelForSession](#c_questsessiongetproposedmaxlevelforsession) | 1 value | 1 value |
| ✅ | [C_QuestSession.GetSessionBeginDetails](#c_questsessiongetsessionbegindetails) | 1 value | 1 value |
| ✅ | [C_QuestSession.GetSuperTrackedQuest](#c_questsessiongetsupertrackedquest) | 1 value | 1 value |
| ✅ | [C_QuestSession.HasJoined](#c_questsessionhasjoined) | 1 value | 1 value |
| ✅ | [C_QuestSession.HasPendingCommand](#c_questsessionhaspendingcommand) | 1 value | 1 value |
| ✅ | [C_QuestSession.RequestSessionStart](#c_questsessionrequestsessionstart) |  |  |
| ✅ | [C_QuestSession.RequestSessionStop](#c_questsessionrequestsessionstop) |  |  |
| ✅ | [C_QuestSession.SendSessionBeginResponse](#c_questsessionsendsessionbeginresponse) |  |  |
| ✅ | [C_QuestSession.SetQuestIsSuperTracked](#c_questsessionsetquestissupertracked) |  |  |

### C_QuestSession.CanStart

`C_QuestSession.CanStart() → allowed: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.CanStop

`C_QuestSession.CanStop() → allowed: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.Exists

`C_QuestSession.Exists() → exists: bool`

- Status: ✅ verified (function)
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.GetAvailableSessionCommand

`C_QuestSession.GetAvailableSessionCommand() → command: QuestSessionCommand`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.GetPendingCommand

`C_QuestSession.GetPendingCommand() → command: QuestSessionCommand`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.GetProposedMaxLevelForSession

`C_QuestSession.GetProposedMaxLevelForSession() → proposedMaxLevel: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.GetSessionBeginDetails

`C_QuestSession.GetSessionBeginDetails() → details: QuestSessionPlayerDetails?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.GetSuperTrackedQuest

`C_QuestSession.GetSuperTrackedQuest() → questID: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.HasJoined

`C_QuestSession.HasJoined() → hasJoined: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.HasPendingCommand

`C_QuestSession.HasPendingCommand() → hasPendingCommand: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.RequestSessionStart

`C_QuestSession.RequestSessionStart()`

- Status: ✅ verified (function)
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.RequestSessionStop

`C_QuestSession.RequestSessionStop()`

- Status: ✅ verified (function)
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.SendSessionBeginResponse

`C_QuestSession.SendSessionBeginResponse(beginSession: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `QuestSessionDocumentation.lua`

### C_QuestSession.SetQuestIsSuperTracked

`C_QuestSession.SetQuestIsSuperTracked(questID: number, superTrack: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `QuestSessionDocumentation.lua`

## Events

### QUEST_SESSION_CREATED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### QUEST_SESSION_DESTROYED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### QUEST_SESSION_ENABLED_STATE_CHANGED

- Status: ✅ verified
- Payload: `enabled: bool`
- fires synchronously (Blizzard's docs)
- Seen firing 2 times (0 in combat); argument kinds: `b`

### QUEST_SESSION_JOINED

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### QUEST_SESSION_LEFT

- Status: ✅ verified
- Payload: none
- unique event (Blizzard's docs)

### QUEST_SESSION_MEMBER_CONFIRM

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### QUEST_SESSION_MEMBER_START_RESPONSE

- Status: ✅ verified
- Payload: `guid: WOWGUID`, `response: bool`
- fires synchronously (Blizzard's docs)

### QUEST_SESSION_NOTIFICATION

- Status: ✅ verified
- Payload: `result: QuestSessionResult`, `guid: WOWGUID`
- fires synchronously (Blizzard's docs)

## Types

### QuestSessionPlayerDetails

- Structure
  - `name`: string
  - `guid`: WOWGUID
