# TextureUtils

Namespace: `C_Texture`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Texture.ClearTitleIconTexture](#c_texturecleartitleicontexture) |  |  |
| ✅ | [C_Texture.GetAtlasElementID](#c_texturegetatlaselementid) |  |  |
| ✅ | [C_Texture.GetAtlasElements](#c_texturegetatlaselements) | 1 value | 1 value |
| ✅ | [C_Texture.GetAtlasExists](#c_texturegetatlasexists) |  |  |
| ✅ | [C_Texture.GetAtlasID](#c_texturegetatlasid) |  |  |
| ✅ | [C_Texture.GetAtlasInfo](#c_texturegetatlasinfo) |  |  |
| ✅ | [C_Texture.GetFilenameFromFileDataID](#c_texturegetfilenamefromfiledataid) |  |  |
| ✅ | [C_Texture.GetTitleIconTexture](#c_texturegettitleicontexture) |  |  |
| ✅ | [C_Texture.IsTitleIconTextureReady](#c_textureistitleicontextureready) |  |  |
| ✅ | [C_Texture.SetTitleIconTexture](#c_texturesettitleicontexture) |  |  |
| ✅ | [C_Texture.SetURLTexture](#c_textureseturltexture) |  |  |

### C_Texture.ClearTitleIconTexture

`C_Texture.ClearTitleIconTexture(texture: SimpleTexture)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TextureUtilsDocumentation.lua`

### C_Texture.GetAtlasElementID

`C_Texture.GetAtlasElementID(atlas: textureAtlas) → elementID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TextureUtilsDocumentation.lua`

### C_Texture.GetAtlasElements

`C_Texture.GetAtlasElements() → atlases: textureAtlas[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,...(16858)}`
- Called in combat: returned 1 value: `table{[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,[number]=string,...(16858)}`
- Source: client docs `TextureUtilsDocumentation.lua`

### C_Texture.GetAtlasExists

`C_Texture.GetAtlasExists(atlas: textureAtlas) → atlasExists: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TextureUtilsDocumentation.lua`

### C_Texture.GetAtlasID

`C_Texture.GetAtlasID(atlas: textureAtlas) → atlasID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TextureUtilsDocumentation.lua`

### C_Texture.GetAtlasInfo

`C_Texture.GetAtlasInfo(atlas: textureAtlas) → info: AtlasInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TextureUtilsDocumentation.lua`

### C_Texture.GetFilenameFromFileDataID

`C_Texture.GetFilenameFromFileDataID(fileDataID: number) → filename: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TextureUtilsDocumentation.lua`

### C_Texture.GetTitleIconTexture

`C_Texture.GetTitleIconTexture(titleID: string, version: TitleIconVersion, callback: GetTitleIconTextureCallback, subIcon: string?)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TextureUtilsDocumentation.lua`

### C_Texture.IsTitleIconTextureReady

`C_Texture.IsTitleIconTextureReady(titleID: string, version: TitleIconVersion, subIcon: string?) → ready: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TextureUtilsDocumentation.lua`

### C_Texture.SetTitleIconTexture

`C_Texture.SetTitleIconTexture(texture: SimpleTexture, titleID: string, version: TitleIconVersion, subIcon: string?)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TextureUtilsDocumentation.lua`

### C_Texture.SetURLTexture

`C_Texture.SetURLTexture(texture: SimpleTexture, url: cstring)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `TextureUtilsDocumentation.lua`

## Events

### URL_TEXTURE_REQUEST_RESULT

- Status: ✅ verified
- Payload: `texture: SimpleTexture`, `result: UrlTextureResult`
- fires synchronously (Blizzard's docs)

## Types

### AtlasInfo

- Structure
  - `elementName`: cstring
  - `width`: number
  - `height`: number
  - `rawSize`: vector2
  - `leftTexCoord`: number
  - `rightTexCoord`: number
  - `topTexCoord`: number
  - `bottomTexCoord`: number
  - `tilesHorizontally`: bool
  - `tilesVertically`: bool
  - `file`: fileID?
  - `filename`: string?
  - `sliceData`: UITextureSliceData?

### GetTitleIconTextureCallback

- CallbackType

### TitleIconVersion

- Enumeration — ✅ verified
  - `Small` = 0
  - `Medium` = 1
  - `Large` = 2

### UrlTextureResult

- Enumeration — ✅ verified
  - `Found` = 1
  - `NotFound` = 2
  - `Requested` = 3
  - `NotAllowed` = 4
