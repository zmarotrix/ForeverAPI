# UIFileAssetAPI

Namespace: `C_UIFileAsset`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_UIFileAsset.GetFileID](#c_uifileassetgetfileid) |  |  |
| ✅ | [C_UIFileAsset.IsKnownFile](#c_uifileassetisknownfile) |  |  |
| ✅ | [C_UIFileAsset.IsLooseFile](#c_uifileassetisloosefile) |  |  |

### C_UIFileAsset.GetFileID

`C_UIFileAsset.GetFileID(asset: FileAsset) → assetFileID: fileID?`

- Status: ✅ verified (function)
- Blizzard: Returns the numeric file ID associated with a file asset.
- `assetFileID`: The file ID corresponding to the given asset. If the asset is already a file ID, it is returned unchanged; otherwise returns nil if the file path is not known to the client.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UIFileAssetAPIDocumentation.lua`

### C_UIFileAsset.IsKnownFile

`C_UIFileAsset.IsKnownFile(asset: FileAsset) → isValid: bool`

- Status: ✅ verified (function)
- Blizzard: Determines whether a file asset is known to the client, either as a shipped asset or a locally existing loose file.
- `isValid`: True if the asset is shipped with the client or refers to a known loose file. Existence or openability of loose files is not verified.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UIFileAssetAPIDocumentation.lua`

### C_UIFileAsset.IsLooseFile

`C_UIFileAsset.IsLooseFile(asset: FileAsset) → isLooseFile: bool`

- Status: ✅ verified (function)
- Blizzard: Determines whether a file asset refers to a known loose (local) file.
- `isLooseFile`: True if the asset refers to a loose file known to the client.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `UIFileAssetAPIDocumentation.lua`
