# UnitConstants

## Types

### AddPrivateAuraAnchorArgs

- Structure
  - `unitToken`: cstring
  - `auraIndex`: number
  - `parent`: SimpleFrame
  - `showCooldownFrame`: bool
  - `showCooldownEdge`: bool
  - `showCountdownNumbers`: bool
  - `showDispelIcon`: bool
  - `isContainer`: bool
  - `iconInfo`: PrivateAuraIconInfo?
  - `durationAnchor`: AnchorBinding?

### GroupBuffVisualAlertInfo

- Structure
  - `spellID`: number
  - `visualValue`: VisualAlertType

### PrivateAuraIconInfo

- Structure
  - `iconAnchor`: AnchorBinding
  - `iconWidth`: uiUnit
  - `iconHeight`: uiUnit
  - `borderScale`: uiUnit?

### UnitAuraSoundInfo

- Structure
  - `unitToken`: string
  - `spellID`: number
  - `soundFileName`: string?
  - `soundFileID`: number?
  - `outputChannel`: string?
  - `throttleSeconds`: number?

### UnitAuraUpdateInfo

- Structure
  - `isFullUpdate`: bool
  - `removedAuraInstanceIDs`: number[]?
  - `addedAuras`: AuraData[]?
  - `updatedAuraInstanceIDs`: number[]?

### UnitPrivateAuraAnchorInfo

- Structure
  - `anchorID`: number
  - `unitToken`: string
  - `auraIndex`: number
  - `showCooldownFrame`: bool
  - `showCooldownEdge`: bool
  - `showCountdownNumbers`: bool
  - `showDispelIcon`: bool
  - `iconWidth`: uiUnit?
  - `iconHeight`: uiUnit?
  - `borderScale`: uiUnit?
  - `isContainer`: bool?
  - `parent`: SimpleFrame
