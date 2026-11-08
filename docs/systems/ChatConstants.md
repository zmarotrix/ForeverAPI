# ChatConstants

## Types

### ChannelPlayerFlags

- Enumeration — ✅ verified
  - `ChannelPlayerNone` = 0
  - `ChannelPlayerOwner` = 1
  - `ChannelPlayerModerator` = 2
  - `ChannelPlayerTextAllow` = 4
  - `ChannelPlayerHidden` = 8

### ChatChannelInfo

- Structure
  - `name`: cstring
  - `shortcut`: cstring
  - `localID`: number
  - `instanceID`: number
  - `zoneChannelID`: number
  - `channelType`: PermanentChatChannelType

### ChatChannelRuleset

- Enumeration — ✅ verified
  - `None` = 0
  - `Mentor` = 1
  - `Disabled` = 2
  - `ChromieTimeCataclysm` = 3
  - `ChromieTimeBuringCrusade` = 4
  - `ChromieTimeWrath` = 5
  - `ChromieTimeMists` = 6
  - `ChromieTimeWoD` = 7
  - `ChromieTimeLegion` = 8

### ChatChannelType

- Enumeration — ✅ verified
  - `None` = 0
  - `Custom` = 1
  - `PrivateParty` = 2
  - `PublicParty` = 3
  - `Communities` = 4
  - `DiscordParty` = 5
  - `DiscordGuild` = 6
  - `DiscordSolo` = 7

### ChatFrameConstants

- Constants — ✅ verified
  - `MaxChatWindows` = 10
  - `MaxChatChannels` = 20
  - `MaxCharacterNameBytes` = FULLNAME_MAX_CHAR

### ChatToxityFilterOptOut

- Enumeration — ✅ verified
  - `FilterAll` = 0
  - `ExcludeFilterFriend` = 1
  - `ExcludeFilterGuild` = 2
  - `ExcludeFilterAll` = 4294967295

### ChatWhisperTargetStatus

- Enumeration — ✅ verified
  - `CanWhisper` = 0
  - `CanWhisperGuild` = 1
  - `Offline` = 2
  - `WrongFaction` = 3

### ExcludedCensorSources

- Enumeration — ✅ verified
  - `None` = 0
  - `Friends` = 1
  - `Guild` = 2
  - `Reserve1` = 4
  - `Reserve2` = 8
  - `Reserve3` = 16
  - `Reserve4` = 32
  - `Reserve5` = 64
  - `Reserve6` = 128
  - `All` = 255

### LanguageFlag

- Enumeration — ✅ verified
  - `IsExotic` = 1
  - `HiddenFromPlayer` = 2
  - `HideLanguageNameInChat` = 4

### PermanentChatChannelType

- Enumeration — ✅ verified
  - `None` = 0
  - `Zone` = 1
  - `Communities` = 2
  - `Custom` = 3

### RegisterAddonMessagePrefixResult

- Enumeration — ✅ verified
  - `Success` = 0
  - `DuplicatePrefix` = 1
  - `InvalidPrefix` = 2
  - `MaxPrefixes` = 3

### SendAddonMessageResult

- Enumeration — ✅ verified
  - `Success` = 0
  - `InvalidPrefix` = 1
  - `InvalidMessage` = 2
  - `AddonMessageThrottle` = 3
  - `InvalidChatType` = 4
  - `NotInGroup` = 5
  - `TargetRequired` = 6
  - `InvalidChannel` = 7
  - `ChannelThrottle` = 8
  - `GeneralError` = 9
  - `NotInGuild` = 10
  - `AddOnMessageLockdown` = 11
  - `TargetOffline` = 12

### TTSConstants

- Constants — ✅ verified
  - `TTSRateMin` = -10
  - `TTSRateMax` = 10
  - `TTSRateDefault` = 0
  - `TTSVolumeMin` = 0
  - `TTSVolumeMax` = 100
  - `TTSVolumeDefault` = 100

### TtsBoolSetting

- Enumeration — ✅ verified
  - `PlaySoundSeparatingChatLineBreaks` = 0
  - `AddCharacterNameToSpeech` = 1
  - `PlayActivitySoundWhenNotFocused` = 2
  - `AlternateSystemVoice` = 3
  - `NarrateMyMessages` = 4

### TtsVoiceType

- Enumeration — ✅ verified
  - `Standard` = 0
  - `Alternate` = 1
