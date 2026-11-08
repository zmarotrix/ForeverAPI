# LoreText

Namespace: `C_LoreText`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_LoreText.RequestLoreTextForCampaignID](#c_loretextrequestloretextforcampaignid) |  |  |

### C_LoreText.RequestLoreTextForCampaignID

`C_LoreText.RequestLoreTextForCampaignID(campaignID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LoreTextDocumentation.lua`

## Events

### LORE_TEXT_UPDATED_CAMPAIGN

- Status: ✅ verified
- Payload: `campaignID: number`, `textEntries: LoreTextEntry[]`
- fires synchronously (Blizzard's docs)

## Types

### LoreTextEntry

- Structure
  - `text`: string
  - `isHeader`: bool
