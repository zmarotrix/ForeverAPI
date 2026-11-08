# ResearchInfo

Namespace: `C_ResearchInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ResearchInfo.GetDigSitesForMap](#c_researchinfogetdigsitesformap) |  |  |

### C_ResearchInfo.GetDigSitesForMap

`C_ResearchInfo.GetDigSitesForMap(uiMapID: number) → digSites: DigSiteMapInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ResearchInfoDocumentation.lua`

## Events

### ARCHAEOLOGY_CLOSED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### ARCHAEOLOGY_FIND_COMPLETE

- Status: ✅ verified
- Payload: `numFindsCompleted: number`, `totalFinds: number`, `researchBranchID: number`
- fires synchronously (Blizzard's docs)

### ARCHAEOLOGY_SURVEY_CAST

- Status: ✅ verified
- Payload: `numFindsCompleted: number`, `totalFinds: number`, `researchBranchID: number`, `successfulFind: number`
- fires synchronously (Blizzard's docs)

### ARCHAEOLOGY_TOGGLE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### ARTIFACT_DIGSITE_COMPLETE

- Status: ✅ verified
- Payload: `researchBranchID: number`
- fires synchronously (Blizzard's docs)

### RESEARCH_ARTIFACT_COMPLETE

- Status: ✅ verified
- Payload: `name: cstring`
- fires synchronously (Blizzard's docs)

### RESEARCH_ARTIFACT_DIG_SITE_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### RESEARCH_ARTIFACT_UPDATE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### DigSiteMapInfo

- Structure
  - `researchSiteID`: number
  - `position`: vector2
  - `name`: cstring
  - `poiBlobID`: number
  - `textureIndex`: number
