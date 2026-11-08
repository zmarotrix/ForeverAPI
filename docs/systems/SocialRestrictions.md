# SocialRestrictions

Namespace: `C_SocialRestrictions`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_SocialRestrictions.AcknowledgeAgeVerificationRestriction](#c_socialrestrictionsacknowledgeageverificationrestriction) |  |  |
| ✅ | [C_SocialRestrictions.AcknowledgeRegionalChatDisabled](#c_socialrestrictionsacknowledgeregionalchatdisabled) |  |  |
| ✅ | [C_SocialRestrictions.CanReceiveChat](#c_socialrestrictionscanreceivechat) |  |  |
| ✅ | [C_SocialRestrictions.CanSendChat](#c_socialrestrictionscansendchat) |  |  |
| ✅ | [C_SocialRestrictions.IsAgeVerificationRestricted](#c_socialrestrictionsisageverificationrestricted) |  |  |
| ✅ | [C_SocialRestrictions.IsAgeVerificationRestrictedMinor](#c_socialrestrictionsisageverificationrestrictedminor) |  |  |
| ✅ | [C_SocialRestrictions.IsChatDisabled](#c_socialrestrictionsischatdisabled) |  |  |
| ✅ | [C_SocialRestrictions.IsFriendsDisabled](#c_socialrestrictionsisfriendsdisabled) |  |  |
| ✅ | [C_SocialRestrictions.IsMuted](#c_socialrestrictionsismuted) |  |  |
| ✅ | [C_SocialRestrictions.IsSilenced](#c_socialrestrictionsissilenced) |  |  |
| ✅ | [C_SocialRestrictions.IsSquelched](#c_socialrestrictionsissquelched) |  |  |
| ✅ | [C_SocialRestrictions.SetChatDisabled](#c_socialrestrictionssetchatdisabled) |  |  |

### C_SocialRestrictions.AcknowledgeAgeVerificationRestriction

`C_SocialRestrictions.AcknowledgeAgeVerificationRestriction()`

- Status: ✅ verified (function)
- Source: client docs `SocialRestrictionsDocumentation.lua`

### C_SocialRestrictions.AcknowledgeRegionalChatDisabled

`C_SocialRestrictions.AcknowledgeRegionalChatDisabled()`

- Status: ✅ verified (function)
- Source: client docs `SocialRestrictionsDocumentation.lua`

### C_SocialRestrictions.CanReceiveChat

`C_SocialRestrictions.CanReceiveChat() → canReceiveChat: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the player meets all conditions that allow them to receive chat messages.
- Source: client docs `SocialRestrictionsDocumentation.lua`

### C_SocialRestrictions.CanSendChat

`C_SocialRestrictions.CanSendChat() → canSendChat: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the player meets all conditions that allow them to send chat messages.
- Source: client docs `SocialRestrictionsDocumentation.lua`

### C_SocialRestrictions.IsAgeVerificationRestricted

`C_SocialRestrictions.IsAgeVerificationRestricted() → restricted: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the account is restricted by the Age Verification feature.
- Source: client docs `SocialRestrictionsDocumentation.lua`

### C_SocialRestrictions.IsAgeVerificationRestrictedMinor

`C_SocialRestrictions.IsAgeVerificationRestrictedMinor() → isMinor: bool`

- Status: ✅ verified (function)
- Blizzard: Returns true if the Age Verification restriction is because the account belongs to a minor, as opposed to an adult who has not yet verified their age.
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `SocialRestrictionsDocumentation.lua`

### C_SocialRestrictions.IsChatDisabled

`C_SocialRestrictions.IsChatDisabled() → disabled: bool`

- Status: ✅ verified (function)
- Source: client docs `SocialRestrictionsDocumentation.lua`

### C_SocialRestrictions.IsFriendsDisabled

`C_SocialRestrictions.IsFriendsDisabled() → disabled: bool`

- Status: ✅ verified (function)
- Source: client docs `SocialRestrictionsDocumentation.lua`

### C_SocialRestrictions.IsMuted

`C_SocialRestrictions.IsMuted() → isMuted: bool`

- Status: ✅ verified (function)
- Source: client docs `SocialRestrictionsDocumentation.lua`

### C_SocialRestrictions.IsSilenced

`C_SocialRestrictions.IsSilenced() → isSilenced: bool`

- Status: ✅ verified (function)
- Source: client docs `SocialRestrictionsDocumentation.lua`

### C_SocialRestrictions.IsSquelched

`C_SocialRestrictions.IsSquelched() → isSquelched: bool`

- Status: ✅ verified (function)
- Source: client docs `SocialRestrictionsDocumentation.lua`

### C_SocialRestrictions.SetChatDisabled

`C_SocialRestrictions.SetChatDisabled(disabled: bool)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SocialRestrictionsDocumentation.lua`

## Events

### ALERT_AGE_VERIFICATION_RESTRICTED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### ALERT_REGIONAL_CHAT_DISABLED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### CHAT_DISABLED_CHANGED

- Status: ✅ verified
- Payload: `disabled: bool`
- fires synchronously (Blizzard's docs)

### CHAT_DISABLED_CHANGE_FAILED

- Status: ✅ verified
- Payload: `disabled: bool`
- fires synchronously (Blizzard's docs)
