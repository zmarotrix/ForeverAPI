# IntlSharedTypes

## Types

### BreakType

- Enumeration — ✅ verified
  - `Character` = 0
  - `Word` = 1
  - `Sentence` = 2
  - `Line` = 3

### CharacterProperties

- Structure
- Blizzard: Unicode property values for the first code point in a string.
  - `codePoint`: number
  - `isAlphabetic`: bool
  - `isDigit`: bool
  - `isWhitespace`: bool
  - `generalCategory`: string
  - `scriptCode`: string
  - `blockCode`: string

### CollationStrength

- Enumeration — ✅ verified
  - `Primary` = 0
  - `Secondary` = 1
  - `Tertiary` = 2
  - `Quaternary` = 3
  - `Identical` = 4

### CurrencyNameStyle

- Enumeration — ✅ verified
  - `Symbol` = 0
  - `NarrowSymbol` = 1
  - `Long` = 2
  - `FormalSymbol` = 3
  - `VariantSymbol` = 4

### CurrencyParseResult

- Structure
- Blizzard: A parsed numeric amount and currency from a localized currency string.
  - `amount`: number
  - `currencyCode`: string

### DateTimeStyle

- Enumeration — ✅ verified
  - `None` = 0
  - `Short` = 1
  - `Medium` = 2
  - `Long` = 3
  - `Full` = 4

### LocaleTransform

- Enumeration — ✅ verified
  - `Canonicalize` = 0
  - `AddLikelySubtags` = 1
  - `RemoveLikelySubtags` = 2
  - `Language` = 3
  - `Script` = 4
  - `Region` = 5
  - `Variant` = 6
  - `ParentLocale` = 7

### NormalizationForm

- Enumeration — ✅ verified
  - `Nfc` = 0
  - `Nfd` = 1
  - `Nfkc` = 2
  - `Nfkd` = 3

### NumberStyle

- Enumeration — ✅ verified
  - `Decimal` = 0
  - `Integer` = 1
  - `Percent` = 2
  - `Currency` = 3

### PluralType

- Enumeration — ✅ verified
  - `Cardinal` = 0
  - `Ordinal` = 1
