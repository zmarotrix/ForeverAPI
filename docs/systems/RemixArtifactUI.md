# RemixArtifactUI

Namespace: `C_RemixArtifactUI`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_RemixArtifactUI.ClearRemixArtifactItem](#c_remixartifactuiclearremixartifactitem) |  |  |
| ✅ | [C_RemixArtifactUI.GetAppearanceInfoByID](#c_remixartifactuigetappearanceinfobyid) |  |  |
| ✅ | [C_RemixArtifactUI.GetArtifactArtInfo](#c_remixartifactuigetartifactartinfo) | 0 values | 0 values |
| ✅ | [C_RemixArtifactUI.GetArtifactItemInfo](#c_remixartifactuigetartifactiteminfo) | 0 values | 0 values |
| ✅ | [C_RemixArtifactUI.GetCurrArtifactItemID](#c_remixartifactuigetcurrartifactitemid) | 1 value | 1 value |
| ✅ | [C_RemixArtifactUI.GetCurrItemSpecIndex](#c_remixartifactuigetcurritemspecindex) | 1 value | 1 value |
| ✅ | [C_RemixArtifactUI.GetCurrTraitTreeID](#c_remixartifactuigetcurrtraittreeid) | 1 value | 1 value |
| ✅ | [C_RemixArtifactUI.ItemInSlotIsRemixArtifact](#c_remixartifactuiiteminslotisremixartifact) |  |  |

### C_RemixArtifactUI.ClearRemixArtifactItem

`C_RemixArtifactUI.ClearRemixArtifactItem()`

- Status: ✅ verified (function)
- Source: client docs `RemixArtifactUIDocumentation.lua`

### C_RemixArtifactUI.GetAppearanceInfoByID

`C_RemixArtifactUI.GetAppearanceInfoByID(artifactAppearanceID: number) → uiCameraID: number, altHandUICameraID: number?`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RemixArtifactUIDocumentation.lua`

### C_RemixArtifactUI.GetArtifactArtInfo

`C_RemixArtifactUI.GetArtifactArtInfo() → artifactArtInfo: RemixArtifactArtInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `RemixArtifactUIDocumentation.lua`

### C_RemixArtifactUI.GetArtifactItemInfo

`C_RemixArtifactUI.GetArtifactItemInfo() → itemID: number, altItemID: number?, artifactAppearanceID: number, appearanceModID: number, itemAppearanceID: number?, altItemAppearanceID: number?, altOnTop: bool`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Called in combat: returned 0 values
- Source: client docs `RemixArtifactUIDocumentation.lua`

### C_RemixArtifactUI.GetCurrArtifactItemID

`C_RemixArtifactUI.GetCurrArtifactItemID() → reqitemID: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `RemixArtifactUIDocumentation.lua`

### C_RemixArtifactUI.GetCurrItemSpecIndex

`C_RemixArtifactUI.GetCurrItemSpecIndex() → specIndex: luaIndex?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `RemixArtifactUIDocumentation.lua`

### C_RemixArtifactUI.GetCurrTraitTreeID

`C_RemixArtifactUI.GetCurrTraitTreeID() → traitTreeID: number?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Called in combat: returned 1 value: `nil`
- Source: client docs `RemixArtifactUIDocumentation.lua`

### C_RemixArtifactUI.ItemInSlotIsRemixArtifact

`C_RemixArtifactUI.ItemInSlotIsRemixArtifact(invSlot: luaIndex) → isRemixArtifact: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `RemixArtifactUIDocumentation.lua`

## Events

### REMIX_ARTIFACT_ITEM_SPECS_LOADED

- Status: ✅ verified
- Payload: `success: bool`
- fires synchronously (Blizzard's docs)

### REMIX_ARTIFACT_UPDATE

- Status: ✅ verified
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
