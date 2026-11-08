# CovenantPreview

Namespace: `C_CovenantPreview`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_CovenantPreview.CloseFromUI](#c_covenantpreviewclosefromui) |  |  |
| ❔ | [C_CovenantPreview.GetCovenantInfoForPlayerChoiceResponseID](#c_covenantpreviewgetcovenantinfoforplayerchoiceresponseid) |  |  |

### C_CovenantPreview.CloseFromUI

`C_CovenantPreview.CloseFromUI()`

- Status: ❔ unverified
- Source: client docs `CovenantPreviewDocumentation.lua`

### C_CovenantPreview.GetCovenantInfoForPlayerChoiceResponseID

`C_CovenantPreview.GetCovenantInfoForPlayerChoiceResponseID(playerChoiceResponseID: number) → previewInfo: CovenantPreviewInfo`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CovenantPreviewDocumentation.lua`

## Events

### COVENANT_PREVIEW_CLOSE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### COVENANT_PREVIEW_OPEN

- Status: ❔ unverified
- Payload: `previewInfo: CovenantPreviewInfo`
- fires synchronously (Blizzard's docs)

## Types

### CovenantAbilityInfo

- Structure
  - `spellID`: number
  - `type`: CovenantAbilityType

### CovenantFeatureInfo

- Structure
  - `name`: cstring
  - `description`: cstring
  - `texture`: number

### CovenantPreviewInfo

- Structure
  - `textureKit`: textureKit
  - `transmogSetID`: number
  - `mountID`: number
  - `covenantName`: string
  - `covenantZone`: string
  - `description`: string
  - `covenantCrest`: textureAtlas
  - `covenantAbilities`: CovenantAbilityInfo[]
  - `fromPlayerChoice`: bool
  - `covenantSoulbinds`: CovenantSoulbindInfo[]
  - `featureInfo`: CovenantFeatureInfo

### CovenantSoulbindInfo

- Structure
  - `spellID`: number
  - `uiTextureKit`: textureKit
  - `name`: cstring
  - `description`: cstring
  - `sortOrder`: number
