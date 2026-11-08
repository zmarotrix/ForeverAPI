# DiscordConstants

## Types

### DiscordAccountType

- Enumeration — ✅ verified
  - `Normal` = 0
  - `Provisional` = 1

### DiscordChannelID

- Enumeration — ✅ verified
  - `InvalidDiscordID` = 0
- ⚠️ `InvalidDiscordID`: docs say 0, game has 0x0000000000000000

### DiscordChatInfo

- Structure
  - `userID`: DiscordMemberOpaqueID
  - `globalName`: string
  - `type`: DiscordDisplayNameType
  - `lastOnlineGUID`: WOWGUID
  - `lastOnlineName`: string
  - `hasAttachment`: bool
  - `hasPoll`: bool
  - `hasEmbed`: bool
  - `hasSticker`: bool
  - `hasEmoji`: bool
  - `hasError`: bool
  - `hasForwardedMessage`: bool
  - `forwardedMessage`: string
  - `fromDiscord`: bool

### DiscordDisplayNameType

- Enumeration — ✅ verified
  - `Default` = 0
  - `LastOnline` = 1
  - `GlobalName` = 2

### DiscordGuildID

- Enumeration — ✅ verified
  - `InvalidDiscordID` = 0
- ⚠️ `InvalidDiscordID`: docs say 0, game has 0x0000000000000000

### DiscordGuildSettings

- Enumeration — ✅ verified
  - `SeparateStream` = 1

### DiscordID

- Enumeration — ✅ verified
  - `InvalidDiscordID` = 0
- ⚠️ `InvalidDiscordID`: docs say 0, game has 0x0000000000000000

### DiscordLobbyID

- Enumeration — ✅ verified
  - `InvalidDiscordID` = 0
- ⚠️ `InvalidDiscordID`: docs say 0, game has 0x0000000000000000

### DiscordMemberID

- Enumeration — ✅ verified
  - `InvalidDiscordID` = 0
- ⚠️ `InvalidDiscordID`: docs say 0, game has 0x0000000000000000

### DiscordMessageID

- Enumeration — ✅ verified
  - `InvalidDiscordID` = 0
- ⚠️ `InvalidDiscordID`: docs say 0, game has 0x0000000000000000
