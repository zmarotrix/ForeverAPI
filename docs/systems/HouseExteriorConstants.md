# HouseExteriorConstants

## Types

### HouseExteriorSizeOption

- Structure
  - `size`: HousingFixtureSize
  - `name`: cstring
  - `isLocked`: bool

### HouseExteriorSizeOptionsInfo

- Structure
  - `selectedSize`: HousingFixtureSize
  - `options`: HouseExteriorSizeOption[]

### HouseExteriorTypeOption

- Structure
  - `houseExteriorTypeID`: number
  - `name`: cstring
  - `isLocked`: bool
  - `isInvalid`: bool
  - `reasonString`: cstring

### HouseExteriorTypeOptionsInfo

- Structure
  - `selectedExteriorType`: number
  - `options`: HouseExteriorTypeOption[]

### HousingCoreFixtureInfo

- Structure
  - `selectedVariantFixtureID`: number
  - `selectedStyleFixtureID`: number
  - `currentStyleVariantOptions`: HousingFixtureOption[]
  - `styleOptions`: HousingFixtureOption[]

### HousingFixtureOption

- Structure
  - `fixtureID`: number
  - `name`: cstring
  - `typeID`: number
  - `typeName`: cstring
  - `isLocked`: bool
  - `isInvalid`: bool
  - `reasonString`: cstring
  - `colorID`: number

### HousingFixturePointInfo

- Structure
  - `ownerHash`: number
  - `selectedFixtureID`: number?
  - `fixtureOptions`: HousingFixtureOption[]
  - `canSelectionBeRemoved`: bool
