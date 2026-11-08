# Font

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [CreateFontFamily](#createfontfamily) |  |  |
| ✅ | [GetFontInfo](#getfontinfo) |  |  |
| ✅ | [GetFonts](#getfonts) |  |  |

### CreateFontFamily

`CreateFontFamily(name: cstring, members: CreateFontFamilyMemberInfo[]) → fontFamily: SimpleFont`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FontDocumentation.lua`

### GetFontInfo

`GetFontInfo(fontObject: SimpleFont) → info: FontScriptInfo?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `FontDocumentation.lua`

### GetFonts

`GetFonts() → fontNames: cstring[]`

- Status: ✅ verified (function)
- Source: client docs `FontDocumentation.lua`

## Types

### CreateFontFamilyMemberInfo

- Structure
  - `alphabet`: FontAlphabet
  - `file`: cstring
  - `height`: uiFontHeight
  - `flags`: TBFFlags

### FontScriptInfo

- Structure
  - `color`: colorRGBA
  - `height`: number
  - `outline`: string
  - `shadow`: FontScriptShadowInfo?
  - `fontObject`: SimpleFont
  - `canBeUserScaled`: bool

### FontScriptShadowInfo

- Structure
  - `color`: colorRGBA
  - `x`: number
  - `y`: number
