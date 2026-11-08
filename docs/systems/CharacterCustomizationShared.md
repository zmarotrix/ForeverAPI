# CharacterCustomizationShared

## Types

### CharCustomizationCategory

- Structure
  - `id`: number
  - `orderIndex`: number
  - `name`: cstring
  - `icon`: textureAtlas
  - `selectedIcon`: textureAtlas
  - `undressModel`: bool
  - `subcategory`: bool
  - `cameraZoomLevel`: number
  - `cameraDistanceOffset`: number
  - `spellShapeshiftFormID`: number?
  - `chrModelID`: number?
  - `options`: CharCustomizationOption[]
  - `hasNewChoices`: bool
  - `needsNativeFormCategory`: bool

### CharCustomizationChoice

- Structure
  - `id`: number
  - `name`: cstring
  - `ineligibleChoice`: bool
  - `isNew`: bool
  - `swatchColor1`: colorRGB?
  - `swatchColor2`: colorRGB?
  - `soundKit`: number?
  - `isLocked`: bool
  - `lockedText`: string?

### CharCustomizationConstants

- Constants — ❔ unverified
  - `CHAR_CUSTOMIZE_CUSTOM_DISPLAY_OPTION_FIRST` = CustomOptionTattoo
  - `CHAR_CUSTOMIZE_CUSTOM_DISPLAY_OPTION_LAST` = CustomOptionTattooColor
  - `NUM_CUSTOM_DISPLAY` = Constants.CharCustomizationConstants.CHAR_CUSTOMIZE_CUSTOM_DISPLAY_OPTION_LAST - Constants.CharCustomizationConstants.CHAR_CUSTOMIZE_CUSTOM_DISPLAY_OPTION_FIRST + 1
  - `NAME_RESERVATION_DAYS` = 30

### CharCustomizationOption

- Structure
  - `id`: number
  - `name`: cstring
  - `orderIndex`: number
  - `optionType`: ChrCustomizationOptionType
  - `choices`: CharCustomizationChoice[]
  - `currentChoiceIndex`: luaIndex?
  - `hasNewChoices`: bool
  - `isSound`: bool

### CharCustomizationType

- Enumeration — ❔ unverified
  - `Skin` = 0
  - `Face` = 1
  - `Hair` = 2
  - `HairColor` = 3
  - `FacialHair` = 4
  - `CustomOptionTattoo` = 5
  - `CustomOptionHorn` = 6
  - `CustomOptionFacewear` = 7
  - `CustomOptionTattooColor` = 8

### ChrCustomizationCategoryFlag

- Enumeration — ❔ unverified
  - `UndressModel` = 1
  - `Subcategory` = 2

### ChrCustomizationOptionType

- Enumeration — ❔ unverified
  - `Dropdown` = 0
  - `Checkbox` = 1
  - `Slider` = 2

### ChrModelFeatureFlags

- Enumeration — ❔ unverified
  - `None` = 0
  - `Summons` = 1
  - `Forms` = 2
  - `Identity` = 4
  - `Deprecated0` = 8
  - `Mounts` = 16
  - `HunterPets` = 32
  - `Players` = 64

### NewCharGear

- Enumeration — ❔ unverified
  - `Start` = 0
  - `Preview` = 1
