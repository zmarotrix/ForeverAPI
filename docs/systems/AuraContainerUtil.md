# AuraContainerUtil

Namespace: `C_AuraContainerUtil`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_AuraContainerUtil.ProcessAuraTooltipBackdropOptions](#c_auracontainerutilprocessauratooltipbackdropoptions) |  |  |
| ❔ | [C_AuraContainerUtil.ProcessAuraTooltipNineSliceOptions](#c_auracontainerutilprocessauratooltipninesliceoptions) |  |  |
| ❔ | [C_AuraContainerUtil.ProcessAuraTooltipTextureSliceOptions](#c_auracontainerutilprocessauratooltiptexturesliceoptions) |  |  |
| ❔ | [C_AuraContainerUtil.ProcessCustomAuraButtonApplicationBarOptions](#c_auracontainerutilprocesscustomaurabuttonapplicationbaroptions) |  |  |
| ❔ | [C_AuraContainerUtil.ProcessCustomAuraButtonApplicationCountOptions](#c_auracontainerutilprocesscustomaurabuttonapplicationcountoptions) |  |  |
| ❔ | [C_AuraContainerUtil.ProcessCustomAuraButtonCasterNameOptions](#c_auracontainerutilprocesscustomaurabuttoncasternameoptions) |  |  |
| ❔ | [C_AuraContainerUtil.ProcessCustomAuraButtonDispelTypeTextOptions](#c_auracontainerutilprocesscustomaurabuttondispeltypetextoptions) |  |  |
| ❔ | [C_AuraContainerUtil.ProcessCustomAuraButtonDispelTypeTextureOptions](#c_auracontainerutilprocesscustomaurabuttondispeltypetextureoptions) |  |  |
| ❔ | [C_AuraContainerUtil.ProcessCustomAuraButtonDurationBarOptions](#c_auracontainerutilprocesscustomaurabuttondurationbaroptions) |  |  |
| ❔ | [C_AuraContainerUtil.ProcessCustomAuraButtonDurationTextOptions](#c_auracontainerutilprocesscustomaurabuttondurationtextoptions) |  |  |

### C_AuraContainerUtil.ProcessAuraTooltipBackdropOptions

`C_AuraContainerUtil.ProcessAuraTooltipBackdropOptions(options: AuraContainerTooltipBackdropOptions) → result: AuraContainerTooltipBackdropOptions`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AuraContainerUtilDocumentation.lua`

### C_AuraContainerUtil.ProcessAuraTooltipNineSliceOptions

`C_AuraContainerUtil.ProcessAuraTooltipNineSliceOptions(options: AuraContainerTooltipNineSliceOptions) → result: AuraContainerTooltipNineSliceOptions`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AuraContainerUtilDocumentation.lua`

### C_AuraContainerUtil.ProcessAuraTooltipTextureSliceOptions

`C_AuraContainerUtil.ProcessAuraTooltipTextureSliceOptions(options: AuraContainerTooltipTextureSliceOptions) → result: AuraContainerTooltipTextureSliceOptions`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AuraContainerUtilDocumentation.lua`

### C_AuraContainerUtil.ProcessCustomAuraButtonApplicationBarOptions

`C_AuraContainerUtil.ProcessCustomAuraButtonApplicationBarOptions(options: CustomAuraButtonApplicationBarOptions) → result: CustomAuraButtonApplicationBarOptions`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AuraContainerUtilDocumentation.lua`

### C_AuraContainerUtil.ProcessCustomAuraButtonApplicationCountOptions

`C_AuraContainerUtil.ProcessCustomAuraButtonApplicationCountOptions(options: CustomAuraButtonApplicationCountOptions?) → result: CustomAuraButtonApplicationCountOptions`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AuraContainerUtilDocumentation.lua`

### C_AuraContainerUtil.ProcessCustomAuraButtonCasterNameOptions

`C_AuraContainerUtil.ProcessCustomAuraButtonCasterNameOptions(options: CustomAuraButtonCasterNameOptions?) → result: CustomAuraButtonCasterNameOptions`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AuraContainerUtilDocumentation.lua`

### C_AuraContainerUtil.ProcessCustomAuraButtonDispelTypeTextOptions

`C_AuraContainerUtil.ProcessCustomAuraButtonDispelTypeTextOptions(options: CustomAuraButtonDispelTypeTextOptions?) → result: CustomAuraButtonDispelTypeTextOptions`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AuraContainerUtilDocumentation.lua`

### C_AuraContainerUtil.ProcessCustomAuraButtonDispelTypeTextureOptions

`C_AuraContainerUtil.ProcessCustomAuraButtonDispelTypeTextureOptions(options: CustomAuraButtonDispelTypeTextureOptions?) → result: CustomAuraButtonDispelTypeTextureOptions`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AuraContainerUtilDocumentation.lua`

### C_AuraContainerUtil.ProcessCustomAuraButtonDurationBarOptions

`C_AuraContainerUtil.ProcessCustomAuraButtonDurationBarOptions(options: CustomAuraButtonDurationBarOptions?) → result: CustomAuraButtonDurationBarOptions`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AuraContainerUtilDocumentation.lua`

### C_AuraContainerUtil.ProcessCustomAuraButtonDurationTextOptions

`C_AuraContainerUtil.ProcessCustomAuraButtonDurationTextOptions(options: CustomAuraButtonDurationTextOptions?) → result: CustomAuraButtonDurationTextOptions`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AuraContainerUtilDocumentation.lua`

## Types

### AuraContainerTooltipAnchorOffsets

- Structure
  - `left`: number
  - `right`: number
  - `top`: number
  - `bottom`: number

### AuraContainerTooltipBackdropInfo

- Structure
  - `bgFile`: TextureAssetDisk?
  - `edgeFile`: TextureAssetDisk?
  - `edgeSize`: number?
  - `insets`: AuraContainerTooltipBackdropInsets?
  - `tile`: bool?
  - `tileEdge`: bool?
  - `tileSize`: number?

### AuraContainerTooltipBackdropInsets

- Structure
  - `left`: number
  - `right`: number
  - `top`: number
  - `bottom`: number

### AuraContainerTooltipBackdropOptions

- Structure
  - `backdropInfo`: AuraContainerTooltipBackdropInfo
  - `borderColor`: colorRGBA?
  - `centerColor`: colorRGBA?
  - `anchorOffsets`: AuraContainerTooltipAnchorOffsets?

### AuraContainerTooltipNineSliceOptions

- Structure
  - `layoutName`: cstring
  - `borderColor`: colorRGBA?
  - `centerColor`: colorRGBA?
  - `anchorOffsets`: AuraContainerTooltipAnchorOffsets?

### AuraContainerTooltipTextureSliceOptions

- Structure
  - `asset`: TextureAssetDisk
  - `sliceMargins`: UITextureSliceMargins?
  - `sliceMode`: UITextureSliceMode?
  - `color`: colorRGBA?
  - `anchorOffsets`: AuraContainerTooltipAnchorOffsets?
  - `drawLayer`: DrawLayer?
  - `drawLayerSublevel`: number

### CustomAuraButtonApplicationBarOptions

- Structure
  - `maxApplications`: number
  - `minApplications`: number
  - `interpolation`: StatusBarInterpolation?

### CustomAuraButtonApplicationCountOptions

- Structure
  - `formatter`: NumericFormatter?

### CustomAuraButtonCasterNameOptions

- Structure
  - `showRealmName`: bool
  - `useClassColors`: bool

### CustomAuraButtonDispelTypeTextOptions

- Structure
  - `showWhenHarmful`: bool
  - `showWhenHelpful`: bool
  - `showWithoutDispelType`: bool
  - `customDispelTextMap`: stringView[]?

### CustomAuraButtonDispelTypeTextureAsset

- Structure
  - `asset`: TextureAssetDisk
  - `useAtlasSize`: bool
  - `texCoords`: CustomAuraButtonDispelTypeTextureTexCoords?

### CustomAuraButtonDispelTypeTextureOptions

- Structure
  - `showAlways`: bool
  - `showWhenHarmful`: bool
  - `showWhenHelpful`: bool
  - `showWithoutDispelType`: bool
  - `stealableFilter`: CustomAuraButtonDispelTypeStealableFilter?
  - `style`: CustomAuraButtonDispelTypeTextureStyle
  - `customDispelAssetMap`: CustomAuraButtonDispelTypeTextureAsset[]?
  - `customDispelColorMap`: colorRGB[]?
  - `customDispelColorCurve`: LuaColorCurveObject?

### CustomAuraButtonDispelTypeTextureTexCoords

- Structure
  - `left`: number
  - `right`: number
  - `top`: number
  - `bottom`: number

### CustomAuraButtonDurationBarOptions

- Structure
  - `interpolation`: StatusBarInterpolation?
  - `direction`: StatusBarTimerDirection?

### CustomAuraButtonDurationTextOptions

- Structure
  - `binding`: DurationTextBinding?
  - `textFormatter`: NumericFormatter?
  - `textFormat`: DurationTextBindingFormatOptions?
  - `textColor`: DurationTextBindingColorOptions?
