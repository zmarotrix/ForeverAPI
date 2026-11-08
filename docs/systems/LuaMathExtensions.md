# LuaMathExtensions

Namespace: `math`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [math.clamp](#mathclamp) |  |  |
| ❔ | [math.isfinite](#mathisfinite) |  |  |
| ❔ | [math.isinf](#mathisinf) |  |  |
| ❔ | [math.isnan](#mathisnan) |  |  |
| ❔ | [math.lerp](#mathlerp) |  |  |
| ❔ | [math.normalize](#mathnormalize) |  |  |
| ❔ | [math.remap](#mathremap) |  |  |
| ❔ | [math.round](#mathround) |  |  |
| ❔ | [math.saturate](#mathsaturate) |  |  |
| ❔ | [math.sign](#mathsign) |  |  |
| ❔ | [math.wrap](#mathwrap) |  |  |

### math.clamp

`math.clamp(value: number, minimum: number, maximum: number) → clampedValue: number`

- Status: ❔ unverified
- Blizzard: Clamps a value to the inclusive range defined by the minimum and maximum values.
- `value`: The value to clamp.
- `minimum`: The inclusive lower bound.
- `maximum`: The inclusive upper bound.
- `clampedValue`: The clamped value.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaMathExtensionsDocumentation.lua`

### math.isfinite

`math.isfinite(value: number) → finite: bool`

- Status: ❔ unverified
- Blizzard: Returns whether a value is finite.
- `value`: The value to inspect.
- `finite`: True if the value is neither infinite nor NaN; otherwise false.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaMathExtensionsDocumentation.lua`

### math.isinf

`math.isinf(value: number) → infinite: bool`

- Status: ❔ unverified
- Blizzard: Returns whether a value is positive or negative infinity.
- `value`: The value to inspect.
- `infinite`: True if the value is positive or negative infinity; otherwise false.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaMathExtensionsDocumentation.lua`

### math.isnan

`math.isnan(value: number) → nan: bool`

- Status: ❔ unverified
- Blizzard: Returns whether a value is NaN.
- `value`: The value to inspect.
- `nan`: True if the value is NaN; otherwise false.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaMathExtensionsDocumentation.lua`

### math.lerp

`math.lerp(startValue: number, endValue: number, amount: number) → interpolatedValue: number`

- Status: ❔ unverified
- Blizzard: Linearly interpolates between two values.
- `startValue`: The value returned when the interpolation amount is 0.
- `endValue`: The value returned when the interpolation amount is 1.
- `amount`: The interpolation amount. Values outside [0, 1] extrapolate beyond the two values.
- `interpolatedValue`: The interpolated value.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaMathExtensionsDocumentation.lua`

### math.normalize

`math.normalize(value: number, minimum: number, maximum: number) → normalizedValue: number`

- Status: ❔ unverified
- Blizzard: Returns the relative position of a value within a range, where the minimum maps to 0 and the maximum maps to 1.
- `value`: The value to normalize.
- `minimum`: The value that maps to 0.
- `maximum`: The value that maps to 1.
- `normalizedValue`: The normalized value. Values outside the input range produce results outside [0, 1].
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaMathExtensionsDocumentation.lua`

### math.remap

`math.remap(value: number, sourceMinimum: number, sourceMaximum: number, destinationMinimum: number, destinationMaximum: number) → remappedValue: number`

- Status: ❔ unverified
- Blizzard: Maps a value from one range to the corresponding position in another range.
- `value`: The value to map.
- `sourceMinimum`: The lower endpoint of the source range.
- `sourceMaximum`: The upper endpoint of the source range.
- `destinationMinimum`: The lower endpoint of the destination range.
- `destinationMaximum`: The upper endpoint of the destination range.
- `remappedValue`: The mapped value. Values outside the source range are extrapolated beyond the destination range.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaMathExtensionsDocumentation.lua`

### math.round

`math.round(value: number, decimalPlaces: number = 0) → roundedValue: number`

- Status: ❔ unverified
- Blizzard: Rounds a value to the specified number of decimal places, with halfway values rounded away from zero.
- `value`: The value to round.
- `decimalPlaces`: The number of decimal places to preserve. Negative values round to positions left of the decimal point.
- `roundedValue`: The rounded value.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaMathExtensionsDocumentation.lua`

### math.saturate

`math.saturate(value: number) → saturatedValue: number`

- Status: ❔ unverified
- Blizzard: Clamps a value to the inclusive range [0, 1].
- `value`: The value to clamp.
- `saturatedValue`: The value clamped to the inclusive range [0, 1].
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaMathExtensionsDocumentation.lua`

### math.sign

`math.sign(value: number) → sign: number`

- Status: ❔ unverified
- Blizzard: Returns -1 for negative values, 0 for zero, and 1 for positive values.
- `value`: The value whose sign will be returned.
- `sign`: The sign of the value.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaMathExtensionsDocumentation.lua`

### math.wrap

`math.wrap(value: number, minimum: number, maximum: number) → wrapped: number`

- Status: ❔ unverified
- Blizzard: Wraps a value into the half-open range [minimum, maximum).
- `value`: The value to wrap.
- `minimum`: The inclusive lower bound of the range.
- `maximum`: The exclusive upper bound of the range.
- `wrapped`: The wrapped value, greater than or equal to minimum and less than maximum. If minimum equals maximum, returns minimum.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaMathExtensionsDocumentation.lua`
