# EncodingUtil

Namespace: `C_EncodingUtil`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_EncodingUtil.CompressString](#c_encodingutilcompressstring) |  |  |
| ✅ | [C_EncodingUtil.DecodeBase64](#c_encodingutildecodebase64) |  |  |
| ✅ | [C_EncodingUtil.DecodeHex](#c_encodingutildecodehex) |  |  |
| ✅ | [C_EncodingUtil.DecompressString](#c_encodingutildecompressstring) |  |  |
| ✅ | [C_EncodingUtil.DeserializeCBOR](#c_encodingutildeserializecbor) |  |  |
| ✅ | [C_EncodingUtil.DeserializeJSON](#c_encodingutildeserializejson) |  |  |
| ✅ | [C_EncodingUtil.EncodeBase64](#c_encodingutilencodebase64) |  |  |
| ✅ | [C_EncodingUtil.EncodeHex](#c_encodingutilencodehex) |  |  |
| ✅ | [C_EncodingUtil.SerializeCBOR](#c_encodingutilserializecbor) |  |  |
| ✅ | [C_EncodingUtil.SerializeJSON](#c_encodingutilserializejson) |  |  |

### C_EncodingUtil.CompressString

`C_EncodingUtil.CompressString(source: stringView, method: CompressionMethod = Deflate, level: CompressionLevel = Default) → output: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncodingUtilDocumentation.lua`

### C_EncodingUtil.DecodeBase64

`C_EncodingUtil.DecodeBase64(source: stringView, variant: Base64Variant = Standard) → output: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncodingUtilDocumentation.lua`

### C_EncodingUtil.DecodeHex

`C_EncodingUtil.DecodeHex(source: string) → output: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncodingUtilDocumentation.lua`

### C_EncodingUtil.DecompressString

`C_EncodingUtil.DecompressString(source: stringView, method: CompressionMethod = Deflate) → output: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncodingUtilDocumentation.lua`

### C_EncodingUtil.DeserializeCBOR

`C_EncodingUtil.DeserializeCBOR(source: stringView) → value: LuaValueVariant?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncodingUtilDocumentation.lua`

### C_EncodingUtil.DeserializeJSON

`C_EncodingUtil.DeserializeJSON(source: string) → value: LuaValueVariant?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncodingUtilDocumentation.lua`

### C_EncodingUtil.EncodeBase64

`C_EncodingUtil.EncodeBase64(source: stringView, variant: Base64Variant = Standard) → output: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncodingUtilDocumentation.lua`

### C_EncodingUtil.EncodeHex

`C_EncodingUtil.EncodeHex(source: stringView) → output: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncodingUtilDocumentation.lua`

### C_EncodingUtil.SerializeCBOR

`C_EncodingUtil.SerializeCBOR(value: LuaValueVariant?, options: CBORSerializationOptions?) → output: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncodingUtilDocumentation.lua`

### C_EncodingUtil.SerializeJSON

`C_EncodingUtil.SerializeJSON(value: LuaValueVariant?, options: JSONSerializationOptions?) → output: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `EncodingUtilDocumentation.lua`

## Types

### Base64Variant

- Enumeration — ✅ verified
  - `Standard` = 0
  - `StandardUrlSafe` = 1

### CBORSerializationOptions

- Structure
  - `ignoreSerializationErrors`: bool

### CompressionLevel

- Enumeration — ✅ verified
  - `Default` = 0
  - `OptimizeForSpeed` = 1
  - `OptimizeForSize` = 2

### CompressionMethod

- Enumeration — ✅ verified
  - `Deflate` = 0
  - `Zlib` = 1
  - `Gzip` = 2

### JSONSerializationOptions

- Structure
  - `ignoreSerializationErrors`: bool
