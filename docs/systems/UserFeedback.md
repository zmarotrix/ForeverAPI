# UserFeedback

Namespace: `C_UserFeedback`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_UserFeedback.SubmitBug](#c_userfeedbacksubmitbug) |  |  |
| ✅ | [C_UserFeedback.SubmitSuggestion](#c_userfeedbacksubmitsuggestion) |  |  |

### C_UserFeedback.SubmitBug

`C_UserFeedback.SubmitBug(bugInfo: cstring, suppressNotification: bool = False) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UserFeedbackDocumentation.lua`

### C_UserFeedback.SubmitSuggestion

`C_UserFeedback.SubmitSuggestion(suggestion: cstring) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UserFeedbackDocumentation.lua`
