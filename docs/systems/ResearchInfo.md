# ResearchInfo

Namespace: `C_ResearchInfo`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_ResearchInfo.GetDigSitesForMap](#c_researchinfogetdigsitesformap) |  |  |

### C_ResearchInfo.GetDigSitesForMap

`C_ResearchInfo.GetDigSitesForMap(uiMapID: number) → digSites: DigSiteMapInfo[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ResearchInfoDocumentation.lua`

## Events

### ARCHAEOLOGY_CLOSED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### ARCHAEOLOGY_FIND_COMPLETE

- Status: ❔ unverified
- Payload: `numFindsCompleted: number`, `totalFinds: number`, `researchBranchID: number`
- fires synchronously (Blizzard's docs)

### ARCHAEOLOGY_SURVEY_CAST

- Status: ❔ unverified
- Payload: `numFindsCompleted: number`, `totalFinds: number`, `researchBranchID: number`, `successfulFind: number`
- fires synchronously (Blizzard's docs)

### ARCHAEOLOGY_TOGGLE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### ARTIFACT_DIGSITE_COMPLETE

- Status: ❔ unverified
- Payload: `researchBranchID: number`
- fires synchronously (Blizzard's docs)

### RESEARCH_ARTIFACT_COMPLETE

- Status: ❔ unverified
- Payload: `name: cstring`
- fires synchronously (Blizzard's docs)

### RESEARCH_ARTIFACT_DIG_SITE_UPDATED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### RESEARCH_ARTIFACT_UPDATE

- Status: ❔ unverified
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
