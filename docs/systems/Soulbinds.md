# Soulbinds

Namespace: `C_Soulbinds`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Soulbinds.ActivateSoulbind](#c_soulbindsactivatesoulbind) |  |  |
| ✅ | [C_Soulbinds.CanActivateSoulbind](#c_soulbindscanactivatesoulbind) |  |  |
| ✅ | [C_Soulbinds.CanModifySoulbind](#c_soulbindscanmodifysoulbind) | 1 value |  |
| ✅ | [C_Soulbinds.CanResetConduitsInSoulbind](#c_soulbindscanresetconduitsinsoulbind) |  |  |
| ✅ | [C_Soulbinds.CanSwitchActiveSoulbindTreeBranch](#c_soulbindscanswitchactivesoulbindtreebranch) | 1 value |  |
| ✅ | [C_Soulbinds.CloseUI](#c_soulbindscloseui) |  |  |
| ✅ | [C_Soulbinds.CommitPendingConduitsInSoulbind](#c_soulbindscommitpendingconduitsinsoulbind) |  |  |
| ✅ | [C_Soulbinds.FindNodeIDActuallyInstalled](#c_soulbindsfindnodeidactuallyinstalled) |  |  |
| ✅ | [C_Soulbinds.FindNodeIDAppearingInstalled](#c_soulbindsfindnodeidappearinginstalled) |  |  |
| ✅ | [C_Soulbinds.FindNodeIDPendingInstall](#c_soulbindsfindnodeidpendinginstall) |  |  |
| ✅ | [C_Soulbinds.FindNodeIDPendingUninstall](#c_soulbindsfindnodeidpendinguninstall) |  |  |
| ✅ | [C_Soulbinds.GetActiveSoulbindID](#c_soulbindsgetactivesoulbindid) | 1 value |  |
| ✅ | [C_Soulbinds.GetConduitCollection](#c_soulbindsgetconduitcollection) |  |  |
| ✅ | [C_Soulbinds.GetConduitCollectionCount](#c_soulbindsgetconduitcollectioncount) | 1 value |  |
| ✅ | [C_Soulbinds.GetConduitCollectionData](#c_soulbindsgetconduitcollectiondata) |  |  |
| ✅ | [C_Soulbinds.GetConduitCollectionDataAtCursor](#c_soulbindsgetconduitcollectiondataatcursor) | 1 value |  |
| ✅ | [C_Soulbinds.GetConduitCollectionDataByVirtualID](#c_soulbindsgetconduitcollectiondatabyvirtualid) |  |  |
| ✅ | [C_Soulbinds.GetConduitDisplayed](#c_soulbindsgetconduitdisplayed) |  |  |
| ✅ | [C_Soulbinds.GetConduitHyperlink](#c_soulbindsgetconduithyperlink) |  |  |
| ✅ | [C_Soulbinds.GetConduitIDPendingInstall](#c_soulbindsgetconduitidpendinginstall) |  |  |
| ✅ | [C_Soulbinds.GetConduitQuality](#c_soulbindsgetconduitquality) |  |  |
| ✅ | [C_Soulbinds.GetConduitRank](#c_soulbindsgetconduitrank) |  |  |
| ✅ | [C_Soulbinds.GetConduitSpellID](#c_soulbindsgetconduitspellid) |  |  |
| ✅ | [C_Soulbinds.GetInstalledConduitID](#c_soulbindsgetinstalledconduitid) |  |  |
| ✅ | [C_Soulbinds.GetNode](#c_soulbindsgetnode) |  |  |
| ✅ | [C_Soulbinds.GetSoulbindData](#c_soulbindsgetsoulbinddata) |  |  |
| ✅ | [C_Soulbinds.GetSpecsAssignedToSoulbind](#c_soulbindsgetspecsassignedtosoulbind) |  |  |
| ✅ | [C_Soulbinds.GetTree](#c_soulbindsgettree) |  |  |
| ✅ | [C_Soulbinds.HasAnyInstalledConduitInSoulbind](#c_soulbindshasanyinstalledconduitinsoulbind) |  |  |
| ✅ | [C_Soulbinds.HasAnyPendingConduits](#c_soulbindshasanypendingconduits) | 1 value |  |
| ✅ | [C_Soulbinds.HasPendingConduitsInSoulbind](#c_soulbindshaspendingconduitsinsoulbind) |  |  |
| ✅ | [C_Soulbinds.IsConduitInstalled](#c_soulbindsisconduitinstalled) |  |  |
| ✅ | [C_Soulbinds.IsConduitInstalledInSoulbind](#c_soulbindsisconduitinstalledinsoulbind) |  |  |
| ✅ | [C_Soulbinds.IsItemConduitByItemInfo](#c_soulbindsisitemconduitbyiteminfo) |  |  |
| ✅ | [C_Soulbinds.IsNodePendingModify](#c_soulbindsisnodependingmodify) |  |  |
| ✅ | [C_Soulbinds.IsUnselectedConduitPendingInSoulbind](#c_soulbindsisunselectedconduitpendinginsoulbind) |  |  |
| ✅ | [C_Soulbinds.ModifyNode](#c_soulbindsmodifynode) |  |  |
| ✅ | [C_Soulbinds.SelectNode](#c_soulbindsselectnode) |  |  |
| ✅ | [C_Soulbinds.UnmodifyNode](#c_soulbindsunmodifynode) |  |  |

### C_Soulbinds.ActivateSoulbind

`C_Soulbinds.ActivateSoulbind(soulbindID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.CanActivateSoulbind

`C_Soulbinds.CanActivateSoulbind(soulbindID: number) → result: bool, errorDescription: cstring?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.CanModifySoulbind

`C_Soulbinds.CanModifySoulbind() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.CanResetConduitsInSoulbind

`C_Soulbinds.CanResetConduitsInSoulbind(soulbindID: number) → result: bool, errorDescription: cstring?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.CanSwitchActiveSoulbindTreeBranch

`C_Soulbinds.CanSwitchActiveSoulbindTreeBranch() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.CloseUI

`C_Soulbinds.CloseUI()`

- Status: ✅ verified (function)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.CommitPendingConduitsInSoulbind

`C_Soulbinds.CommitPendingConduitsInSoulbind(soulbindID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.FindNodeIDActuallyInstalled

`C_Soulbinds.FindNodeIDActuallyInstalled(soulbindID: number, conduitID: number) → nodeID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.FindNodeIDAppearingInstalled

`C_Soulbinds.FindNodeIDAppearingInstalled(soulbindID: number, conduitID: number) → nodeID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.FindNodeIDPendingInstall

`C_Soulbinds.FindNodeIDPendingInstall(soulbindID: number, conduitID: number) → nodeID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.FindNodeIDPendingUninstall

`C_Soulbinds.FindNodeIDPendingUninstall(soulbindID: number, conduitID: number) → nodeID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.GetActiveSoulbindID

`C_Soulbinds.GetActiveSoulbindID() → soulbindID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.GetConduitCollection

`C_Soulbinds.GetConduitCollection(conduitType: SoulbindConduitType) → collectionData: ConduitCollectionData[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.GetConduitCollectionCount

`C_Soulbinds.GetConduitCollectionCount() → count: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.GetConduitCollectionData

`C_Soulbinds.GetConduitCollectionData(conduitID: number) → collectionData: ConduitCollectionData?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.GetConduitCollectionDataAtCursor

`C_Soulbinds.GetConduitCollectionDataAtCursor() → collectionData: ConduitCollectionData?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.GetConduitCollectionDataByVirtualID

`C_Soulbinds.GetConduitCollectionDataByVirtualID(virtualID: number) → collectionData: ConduitCollectionData?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.GetConduitDisplayed

`C_Soulbinds.GetConduitDisplayed(nodeID: number) → conduitID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.GetConduitHyperlink

`C_Soulbinds.GetConduitHyperlink(conduitID: number, rank: number) → link: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.GetConduitIDPendingInstall

`C_Soulbinds.GetConduitIDPendingInstall(nodeID: number) → conduitID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.GetConduitQuality

`C_Soulbinds.GetConduitQuality(conduitID: number, rank: number) → quality: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.GetConduitRank

`C_Soulbinds.GetConduitRank(conduitID: number) → conduitRank: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.GetConduitSpellID

`C_Soulbinds.GetConduitSpellID(conduitID: number, conduitRank: number) → spellID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.GetInstalledConduitID

`C_Soulbinds.GetInstalledConduitID(nodeID: number) → conduitID: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.GetNode

`C_Soulbinds.GetNode(nodeID: number) → node: SoulbindNode`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.GetSoulbindData

`C_Soulbinds.GetSoulbindData(soulbindID: number) → data: SoulbindData`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.GetSpecsAssignedToSoulbind

`C_Soulbinds.GetSpecsAssignedToSoulbind(soulbindID: number) → specIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.GetTree

`C_Soulbinds.GetTree(treeID: number) → tree: SoulbindTree`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.HasAnyInstalledConduitInSoulbind

`C_Soulbinds.HasAnyInstalledConduitInSoulbind(soulbindID: number) → result: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.HasAnyPendingConduits

`C_Soulbinds.HasAnyPendingConduits() → result: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.HasPendingConduitsInSoulbind

`C_Soulbinds.HasPendingConduitsInSoulbind(soulbindID: number) → result: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.IsConduitInstalled

`C_Soulbinds.IsConduitInstalled(nodeID: number) → result: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.IsConduitInstalledInSoulbind

`C_Soulbinds.IsConduitInstalledInSoulbind(soulbindID: number, conduitID: number) → result: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.IsItemConduitByItemInfo

`C_Soulbinds.IsItemConduitByItemInfo(itemInfo: ItemInfo) → result: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.IsNodePendingModify

`C_Soulbinds.IsNodePendingModify(nodeID: number) → result: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.IsUnselectedConduitPendingInSoulbind

`C_Soulbinds.IsUnselectedConduitPendingInSoulbind(soulbindID: number) → result: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.ModifyNode

`C_Soulbinds.ModifyNode(nodeID: number, conduitID: number, type: SoulbindConduitTransactionType)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.SelectNode

`C_Soulbinds.SelectNode(nodeID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

### C_Soulbinds.UnmodifyNode

`C_Soulbinds.UnmodifyNode(nodeID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoulbindsDocumentation.lua`

## Events

### SOULBIND_ACTIVATED

- Status: ✅ verified
- Payload: `soulbindID: number`
- fires synchronously (Blizzard's docs)

### SOULBIND_CONDUIT_COLLECTION_CLEARED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SOULBIND_CONDUIT_COLLECTION_REMOVED

- Status: ✅ verified
- Payload: `conduitID: number`
- fires synchronously (Blizzard's docs)

### SOULBIND_CONDUIT_COLLECTION_UPDATED

- Status: ✅ verified
- Payload: `collectionData: ConduitCollectionData`
- fires synchronously (Blizzard's docs)

### SOULBIND_CONDUIT_INSTALLED

- Status: ✅ verified
- Payload: `nodeID: number`, `data: SoulbindConduitData`
- fires synchronously (Blizzard's docs)

### SOULBIND_CONDUIT_UNINSTALLED

- Status: ✅ verified
- Payload: `nodeID: number`, `data: SoulbindConduitData`
- fires synchronously (Blizzard's docs)

### SOULBIND_FORGE_INTERACTION_ENDED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SOULBIND_FORGE_INTERACTION_STARTED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SOULBIND_NODE_LEARNED

- Status: ✅ verified
- Payload: `nodeID: number`
- fires synchronously (Blizzard's docs)

### SOULBIND_NODE_UNLEARNED

- Status: ✅ verified
- Payload: `nodeID: number`
- fires synchronously (Blizzard's docs)

### SOULBIND_NODE_UPDATED

- Status: ✅ verified
- Payload: `nodeID: number`
- fires synchronously (Blizzard's docs)

### SOULBIND_PATH_CHANGED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### SOULBIND_PENDING_CONDUIT_CHANGED

- Status: ✅ verified
- Payload: `nodeID: number`, `conduitID: number`
- fires synchronously (Blizzard's docs)

## Types

### ConduitCollectionData

- Structure
  - `conduitID`: number
  - `conduitRank`: number
  - `conduitItemLevel`: number
  - `conduitType`: SoulbindConduitType
  - `conduitSpecSetID`: number
  - `conduitSpecIDs`: number[]
  - `conduitSpecName`: cstring?
  - `covenantID`: number?
  - `conduitItemID`: number

### SoulbindConduitData

- Structure
  - `conduitID`: number
  - `conduitRank`: number

### SoulbindData

- Structure
  - `ID`: number
  - `covenantID`: number
  - `name`: cstring
  - `description`: cstring
  - `textureKit`: textureKit
  - `unlocked`: bool
  - `cvarIndex`: luaIndex
  - `tree`: SoulbindTree
  - `modelSceneData`: SoulbindModelSceneData
  - `activationSoundKitID`: number
  - `playerConditionReason`: cstring?

### SoulbindModelSceneData

- Structure
  - `creatureDisplayInfoID`: number
  - `modelSceneActorID`: number

### SoulbindNode

- Structure
  - `ID`: number
  - `row`: number
  - `column`: number
  - `icon`: fileID
  - `spellID`: number
  - `playerConditionReason`: cstring?
  - `conduitID`: number
  - `conduitRank`: number
  - `state`: SoulbindNodeState
  - `conduitType`: SoulbindConduitType?
  - `parentNodeIDs`: number[]
  - `failureRenownRequirement`: number?
  - `socketEnhanced`: bool?

### SoulbindTree

- Structure
  - `editable`: bool
  - `nodes`: SoulbindNode[]
