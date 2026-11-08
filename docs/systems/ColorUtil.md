# ColorUtil

Namespace: `C_ColorUtil`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ColorUtil.ConvertHSLToHSV](#c_colorutilconverthsltohsv) |  |  |
| ✅ | [C_ColorUtil.ConvertHSVToHSL](#c_colorutilconverthsvtohsl) |  |  |
| ✅ | [C_ColorUtil.ConvertHSVToRGB](#c_colorutilconverthsvtorgb) |  |  |
| ✅ | [C_ColorUtil.ConvertRGBToHSV](#c_colorutilconvertrgbtohsv) |  |  |
| ✅ | [C_ColorUtil.GenerateTextColorCode](#c_colorutilgeneratetextcolorcode) |  |  |
| ✅ | [C_ColorUtil.WrapTextInColor](#c_colorutilwraptextincolor) |  |  |
| ✅ | [C_ColorUtil.WrapTextInColorCode](#c_colorutilwraptextincolorcode) |  |  |

### C_ColorUtil.ConvertHSLToHSV

`C_ColorUtil.ConvertHSLToHSV(hslH: number, hslS: number, hslL: number) → hsvH: number, hsvS: number, hsvV: number`

- Status: ✅ verified (function)
- Blizzard: Converts an unpacked HSL color to HSV.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ColorUtilDocumentation.lua`

### C_ColorUtil.ConvertHSVToHSL

`C_ColorUtil.ConvertHSVToHSL(hsvH: number, hsvS: number, hsvV: number) → hslH: number, hslS: number, hslL: number`

- Status: ✅ verified (function)
- Blizzard: Converts an unpacked HSV color to HSL.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ColorUtilDocumentation.lua`

### C_ColorUtil.ConvertHSVToRGB

`C_ColorUtil.ConvertHSVToRGB(hsvH: number, hsvS: number, hsvV: number) → rgbR: number, rgbG: number, rgbB: number`

- Status: ✅ verified (function)
- Blizzard: Converts an unpacked HSV color to RGB.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ColorUtilDocumentation.lua`

### C_ColorUtil.ConvertRGBToHSV

`C_ColorUtil.ConvertRGBToHSV(rgbR: number, rgbG: number, rgbB: number) → hsvH: number, hsvS: number, hsvV: number`

- Status: ✅ verified (function)
- Blizzard: Converts an unpacked RGB color to HSV. For achromatic inputs, the returned hue will be -1.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ColorUtilDocumentation.lua`

### C_ColorUtil.GenerateTextColorCode

`C_ColorUtil.GenerateTextColorCode(color: colorRGB) → textColorCode: string`

- Status: ✅ verified (function)
- Blizzard: Generates a hex color code suitable for use in text color code markup.
- `color`: Color to generate a hex color code from.
- `textColorCode`: Hex representation of the color formatted as an 8-byte ARGB string, with alpha forced to 255.
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `ColorUtilDocumentation.lua`

### C_ColorUtil.WrapTextInColor

`C_ColorUtil.WrapTextInColor(text: cstring, color: colorRGB) → coloredText: string`

- Status: ✅ verified (function)
- Blizzard: Wraps a given string with color code markup.
- `text`: Text to be wrapped in color markup.
- `color`: Color to apply to the text.
- `coloredText`: The input text wrapped in '|c' and '|r' quoted code sequences for the supplied color.
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `ColorUtilDocumentation.lua`

### C_ColorUtil.WrapTextInColorCode

`C_ColorUtil.WrapTextInColorCode(text: cstring, textColorCode: cstring) → coloredText: string`

- Status: ✅ verified (function)
- Blizzard: Wraps a given string with color code markup.
- `text`: Text to be wrapped in color markup.
- `textColorCode`: Color to apply to the text, formatted as an 8-byte ARGB string as returned by GenerateTextColorCode.
- `coloredText`: The input text wrapped in '|c' and '|r' quoted code sequences for the supplied color.
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `ColorUtilDocumentation.lua`
