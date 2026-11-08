# WarCampaign

Namespace: `C_CampaignInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_CampaignInfo.GetAvailableCampaigns](#c_campaigninfogetavailablecampaigns) |  |  |
| ❔ | [C_CampaignInfo.GetCampaignChapterInfo](#c_campaigninfogetcampaignchapterinfo) |  |  |
| ❔ | [C_CampaignInfo.GetCampaignID](#c_campaigninfogetcampaignid) |  |  |
| ❔ | [C_CampaignInfo.GetCampaignInfo](#c_campaigninfogetcampaigninfo) |  |  |
| ❔ | [C_CampaignInfo.GetChapterIDs](#c_campaigninfogetchapterids) |  |  |
| ❔ | [C_CampaignInfo.GetCurrentChapterID](#c_campaigninfogetcurrentchapterid) |  |  |
| ❔ | [C_CampaignInfo.GetFailureReason](#c_campaigninfogetfailurereason) |  |  |
| ❔ | [C_CampaignInfo.GetState](#c_campaigninfogetstate) |  |  |
| ❔ | [C_CampaignInfo.IsCampaignQuest](#c_campaigninfoiscampaignquest) |  |  |
| ❔ | [C_CampaignInfo.SortAsNormalQuest](#c_campaigninfosortasnormalquest) |  |  |

### C_CampaignInfo.GetAvailableCampaigns

`C_CampaignInfo.GetAvailableCampaigns() → campaignIDs: number[]`

- Status: ❔ unverified
- Source: client docs `WarCampaignDocumentation.lua`

### C_CampaignInfo.GetCampaignChapterInfo

`C_CampaignInfo.GetCampaignChapterInfo(campaignChapterID: number) → campaignChapterInfo: CampaignChapterInfo?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WarCampaignDocumentation.lua`

### C_CampaignInfo.GetCampaignID

`C_CampaignInfo.GetCampaignID(questID: number) → campaignID: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WarCampaignDocumentation.lua`

### C_CampaignInfo.GetCampaignInfo

`C_CampaignInfo.GetCampaignInfo(campaignID: number) → campaignInfo: CampaignInfo?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WarCampaignDocumentation.lua`

### C_CampaignInfo.GetChapterIDs

`C_CampaignInfo.GetChapterIDs(campaignID: number) → chapterIDs: number[]?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WarCampaignDocumentation.lua`

### C_CampaignInfo.GetCurrentChapterID

`C_CampaignInfo.GetCurrentChapterID(campaignID: number) → currentChapterID: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WarCampaignDocumentation.lua`

### C_CampaignInfo.GetFailureReason

`C_CampaignInfo.GetFailureReason(campaignID: number) → failureReason: CampaignFailureReason?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WarCampaignDocumentation.lua`

### C_CampaignInfo.GetState

`C_CampaignInfo.GetState(campaignID: number) → state: CampaignState`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WarCampaignDocumentation.lua`

### C_CampaignInfo.IsCampaignQuest

`C_CampaignInfo.IsCampaignQuest(questID: number) → isCampaignQuest: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WarCampaignDocumentation.lua`

### C_CampaignInfo.SortAsNormalQuest

`C_CampaignInfo.SortAsNormalQuest(campaignID: number) → sortAsNormalQuest: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WarCampaignDocumentation.lua`

## Types

### CampaignChapterInfo

- Structure
  - `name`: cstring
  - `description`: cstring
  - `rewardQuestID`: number

### CampaignFailureReason

- Structure
  - `text`: string
  - `questID`: number?
  - `mapID`: number?

### CampaignInfo

- Structure
  - `name`: cstring
  - `description`: cstring
  - `uiTextureKit`: textureKit
  - `isWarCampaign`: bool
  - `usesNormalQuestIcons`: bool
  - `isContainerCampaign`: bool
  - `sortAsNormalQuest`: bool
  - `hideFutureChapters`: bool

### CampaignState

- Enumeration — ❔ unverified
  - `Invalid` = 0
  - `Complete` = 1
  - `InProgress` = 2
  - `Stalled` = 3
