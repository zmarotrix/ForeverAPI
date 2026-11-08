# RemixArtifactUI

Namespace: `C_RemixArtifactUI`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_RemixArtifactUI.ClearRemixArtifactItem](#c_remixartifactuiclearremixartifactitem) |  |  |
| ❔ | [C_RemixArtifactUI.GetAppearanceInfoByID](#c_remixartifactuigetappearanceinfobyid) |  |  |
| ❔ | [C_RemixArtifactUI.GetArtifactArtInfo](#c_remixartifactuigetartifactartinfo) |  |  |
| ❔ | [C_RemixArtifactUI.GetArtifactItemInfo](#c_remixartifactuigetartifactiteminfo) |  |  |
| ❔ | [C_RemixArtifactUI.GetCurrArtifactItemID](#c_remixartifactuigetcurrartifactitemid) |  |  |
| ❔ | [C_RemixArtifactUI.GetCurrItemSpecIndex](#c_remixartifactuigetcurritemspecindex) |  |  |
| ❔ | [C_RemixArtifactUI.GetCurrTraitTreeID](#c_remixartifactuigetcurrtraittreeid) |  |  |
| ❔ | [C_RemixArtifactUI.ItemInSlotIsRemixArtifact](#c_remixartifactuiiteminslotisremixartifact) |  |  |

### C_RemixArtifactUI.ClearRemixArtifactItem

`C_RemixArtifactUI.ClearRemixArtifactItem()`

- Status: ❔ unverified
- Source: client docs `RemixArtifactUIDocumentation.lua`

### C_RemixArtifactUI.GetAppearanceInfoByID

`C_RemixArtifactUI.GetAppearanceInfoByID(artifactAppearanceID: number) → uiCameraID: number, altHandUICameraID: number?`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RemixArtifactUIDocumentation.lua`

### C_RemixArtifactUI.GetArtifactArtInfo

`C_RemixArtifactUI.GetArtifactArtInfo() → artifactArtInfo: RemixArtifactArtInfo`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `RemixArtifactUIDocumentation.lua`

### C_RemixArtifactUI.GetArtifactItemInfo

`C_RemixArtifactUI.GetArtifactItemInfo() → itemID: number, altItemID: number?, artifactAppearanceID: number, appearanceModID: number, itemAppearanceID: number?, altItemAppearanceID: number?, altOnTop: bool`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `RemixArtifactUIDocumentation.lua`

### C_RemixArtifactUI.GetCurrArtifactItemID

`C_RemixArtifactUI.GetCurrArtifactItemID() → reqitemID: number?`

- Status: ❔ unverified
- Source: client docs `RemixArtifactUIDocumentation.lua`

### C_RemixArtifactUI.GetCurrItemSpecIndex

`C_RemixArtifactUI.GetCurrItemSpecIndex() → specIndex: luaIndex?`

- Status: ❔ unverified
- Source: client docs `RemixArtifactUIDocumentation.lua`

### C_RemixArtifactUI.GetCurrTraitTreeID

`C_RemixArtifactUI.GetCurrTraitTreeID() → traitTreeID: number?`

- Status: ❔ unverified
- Source: client docs `RemixArtifactUIDocumentation.lua`

### C_RemixArtifactUI.ItemInSlotIsRemixArtifact

`C_RemixArtifactUI.ItemInSlotIsRemixArtifact(invSlot: luaIndex) → isRemixArtifact: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RemixArtifactUIDocumentation.lua`

## Events

### REMIX_ARTIFACT_ITEM_SPECS_LOADED

- Status: ❔ unverified
- Payload: `success: bool`
- fires synchronously (Blizzard's docs)

### REMIX_ARTIFACT_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### RemixArtifactAppearanceInfo

- Structure
  - `uiCameraID`: number
  - `altHandUICameraID`: number?

### RemixArtifactArtInfo

- Structure
  - `textureKit`: textureKit
  - `titleName`: string
  - `uiModelSceneID`: number
  - `spellVisualKitID`: number

### RemixArtifactInfo

- Structure
  - `itemID`: number
  - `altItemID`: number?
  - `artifactAppearanceID`: number
  - `appearanceModID`: number
  - `itemAppearanceID`: number?
  - `altItemAppearanceID`: number?
  - `altOnTop`: bool
