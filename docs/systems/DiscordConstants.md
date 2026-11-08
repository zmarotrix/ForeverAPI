# DiscordConstants

## Types

### DiscordAccountType

- Enumeration — ❔ unverified
  - `Normal` = 0
  - `Provisional` = 1

### DiscordChannelID

- Enumeration — ❔ unverified
  - `InvalidDiscordID` = 0

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

- Enumeration — ❔ unverified
  - `Default` = 0
  - `LastOnline` = 1
  - `GlobalName` = 2

### DiscordGuildID

- Enumeration — ❔ unverified
  - `InvalidDiscordID` = 0

### DiscordGuildSettings

- Enumeration — ❔ unverified
  - `SeparateStream` = 1

### DiscordID

- Enumeration — ❔ unverified
  - `InvalidDiscordID` = 0

### DiscordLobbyID

- Enumeration — ❔ unverified
  - `InvalidDiscordID` = 0

### DiscordMemberID

- Enumeration — ❔ unverified
  - `InvalidDiscordID` = 0

### DiscordMessageID

- Enumeration — ❔ unverified
  - `InvalidDiscordID` = 0
