# SharedTraits

Namespace: `C_Traits`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Traits.CanEditConfig](#c_traitscaneditconfig) |  |  |
| ✅ | [C_Traits.CanPurchaseRank](#c_traitscanpurchaserank) |  |  |
| ✅ | [C_Traits.CanRefundRank](#c_traitscanrefundrank) |  |  |
| ✅ | [C_Traits.CascadeRepurchaseRanks](#c_traitscascaderepurchaseranks) |  |  |
| ✅ | [C_Traits.ClearCascadeRepurchaseHistory](#c_traitsclearcascaderepurchasehistory) |  |  |
| ✅ | [C_Traits.CloseTraitSystemInteraction](#c_traitsclosetraitsysteminteraction) |  |  |
| ✅ | [C_Traits.CommitConfig](#c_traitscommitconfig) |  |  |
| ✅ | [C_Traits.ConfigHasStagedChanges](#c_traitsconfighasstagedchanges) |  |  |
| ✅ | [C_Traits.GenerateImportString](#c_traitsgenerateimportstring) |  |  |
| ✅ | [C_Traits.GenerateInspectImportString](#c_traitsgenerateinspectimportstring) |  |  |
| ✅ | [C_Traits.GetConditionInfo](#c_traitsgetconditioninfo) |  |  |
| ✅ | [C_Traits.GetConfigIDBySystemID](#c_traitsgetconfigidbysystemid) |  |  |
| ✅ | [C_Traits.GetConfigIDByTreeID](#c_traitsgetconfigidbytreeid) |  |  |
| ✅ | [C_Traits.GetConfigInfo](#c_traitsgetconfiginfo) |  |  |
| ✅ | [C_Traits.GetConfigVariationID](#c_traitsgetconfigvariationid) |  |  |
| ✅ | [C_Traits.GetConfigsByType](#c_traitsgetconfigsbytype) | 1 value | 1 value |
| ✅ | [C_Traits.GetDefinitionInfo](#c_traitsgetdefinitioninfo) |  |  |
| ✅ | [C_Traits.GetEntryInfo](#c_traitsgetentryinfo) |  |  |
| ✅ | [C_Traits.GetGroupCurrencyInfo](#c_traitsgetgroupcurrencyinfo) |  |  |
| ✅ | [C_Traits.GetGroupDisplayInfoByTreeID](#c_traitsgetgroupdisplayinfobytreeid) |  |  |
| ✅ | [C_Traits.GetIncreasedTraitData](#c_traitsgetincreasedtraitdata) |  |  |
| ✅ | [C_Traits.GetLoadoutSerializationVersion](#c_traitsgetloadoutserializationversion) | 1 value | 1 value |
| ✅ | [C_Traits.GetMaxAvailableTraitCurrency](#c_traitsgetmaxavailabletraitcurrency) |  |  |
| ✅ | [C_Traits.GetNodeCost](#c_traitsgetnodecost) |  |  |
| ✅ | [C_Traits.GetNodeInfo](#c_traitsgetnodeinfo) |  |  |
| ✅ | [C_Traits.GetStagedChanges](#c_traitsgetstagedchanges) |  |  |
| ✅ | [C_Traits.GetStagedChangesCost](#c_traitsgetstagedchangescost) |  |  |
| ✅ | [C_Traits.GetSubTreeInfo](#c_traitsgetsubtreeinfo) |  |  |
| ✅ | [C_Traits.GetSystemIDByTreeID](#c_traitsgetsystemidbytreeid) |  |  |
| ✅ | [C_Traits.GetTraitCurrencyForAchievement](#c_traitsgettraitcurrencyforachievement) |  |  |
| ✅ | [C_Traits.GetTraitCurrencyInfo](#c_traitsgettraitcurrencyinfo) |  |  |
| ✅ | [C_Traits.GetTraitDescription](#c_traitsgettraitdescription) |  |  |
| ✅ | [C_Traits.GetTraitSystemFlags](#c_traitsgettraitsystemflags) |  |  |
| ✅ | [C_Traits.GetTraitSystemWidgetSetID](#c_traitsgettraitsystemwidgetsetid) |  |  |
| ✅ | [C_Traits.GetTreeCurrencyInfo](#c_traitsgettreecurrencyinfo) |  |  |
| ✅ | [C_Traits.GetTreeHash](#c_traitsgettreehash) |  |  |
| ✅ | [C_Traits.GetTreeInfo](#c_traitsgettreeinfo) |  |  |
| ✅ | [C_Traits.GetTreeNodes](#c_traitsgettreenodes) |  |  |
| ✅ | [C_Traits.HasValidInspectData](#c_traitshasvalidinspectdata) | 1 value | 1 value |
| ✅ | [C_Traits.IsReadyForCommit](#c_traitsisreadyforcommit) | 1 value | 1 value |
| ✅ | [C_Traits.PurchaseAllRanks](#c_traitspurchaseallranks) |  |  |
| ✅ | [C_Traits.PurchaseRank](#c_traitspurchaserank) |  |  |
| ✅ | [C_Traits.RefundAllRanks](#c_traitsrefundallranks) |  |  |
| ✅ | [C_Traits.RefundRank](#c_traitsrefundrank) |  |  |
| ✅ | [C_Traits.ResetTree](#c_traitsresettree) |  |  |
| ✅ | [C_Traits.ResetTreeByCurrency](#c_traitsresettreebycurrency) |  |  |
| ✅ | [C_Traits.RollbackConfig](#c_traitsrollbackconfig) |  |  |
| ✅ | [C_Traits.SetSelection](#c_traitssetselection) |  |  |
| ✅ | [C_Traits.StageConfig](#c_traitsstageconfig) |  |  |
| ✅ | [C_Traits.TalentTestUnlearnSpells](#c_traitstalenttestunlearnspells) |  |  |
| ✅ | [C_Traits.TryPurchaseAllRanks](#c_traitstrypurchaseallranks) |  |  |
| ✅ | [C_Traits.TryPurchaseToNode](#c_traitstrypurchasetonode) |  |  |
| ✅ | [C_Traits.TryRefundToNode](#c_traitstryrefundtonode) |  |  |

### C_Traits.CanEditConfig

`C_Traits.CanEditConfig(configID: number) → canEdit: bool, errorMessage: cstring`

- Status: ✅ verified (function)
- Blizzard: Returns whether the player can make changes to the specified talent config.
- `errorMessage`: If canEdit is false, this will be filled out with text explaining why the player can not make changes.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.CanPurchaseRank

`C_Traits.CanPurchaseRank(configID: number, nodeID: number, nodeEntryID: number) → canPurchase: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.CanRefundRank

`C_Traits.CanRefundRank(configID: number, nodeID: number) → canRefund: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.CascadeRepurchaseRanks

`C_Traits.CascadeRepurchaseRanks(configID: number, nodeID: number, entryID: number?) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.ClearCascadeRepurchaseHistory

`C_Traits.ClearCascadeRepurchaseHistory(configID: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.CloseTraitSystemInteraction

`C_Traits.CloseTraitSystemInteraction()`

- Status: ✅ verified (function)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.CommitConfig

`C_Traits.CommitConfig(configID: number) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.ConfigHasStagedChanges

`C_Traits.ConfigHasStagedChanges(configID: number) → hasChanges: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GenerateImportString

`C_Traits.GenerateImportString(configID: number) → importString: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GenerateInspectImportString

`C_Traits.GenerateInspectImportString(target: cstring) → importString: string`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetConditionInfo

`C_Traits.GetConditionInfo(configID: number, condID: number) → condInfo: TraitCondInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetConfigIDBySystemID

`C_Traits.GetConfigIDBySystemID(systemID: number) → configID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetConfigIDByTreeID

`C_Traits.GetConfigIDByTreeID(treeID: number) → configID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetConfigInfo

`C_Traits.GetConfigInfo(configID: number) → configInfo: TraitConfigInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetConfigVariationID

`C_Traits.GetConfigVariationID(systemID: number) → variationID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetConfigsByType

`C_Traits.GetConfigsByType(configType: TraitConfigType) → configIDs: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `n:0`: returned 1 value: `table{}`
- Called in combat: returned 1 value: `table{}`
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetDefinitionInfo

`C_Traits.GetDefinitionInfo(definitionID: number) → definitionInfo: TraitDefinitionInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetEntryInfo

`C_Traits.GetEntryInfo(configID: number, entryID: number) → entryInfo: TraitEntryInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetGroupCurrencyInfo

`C_Traits.GetGroupCurrencyInfo(configID: number, groupIDs: number[]) → groupCurrencyInfos: GroupCurrencyInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetGroupDisplayInfoByTreeID

`C_Traits.GetGroupDisplayInfoByTreeID(treeID: number) → displayInfos: TraitGroupDisplayInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetIncreasedTraitData

`C_Traits.GetIncreasedTraitData(nodeID: number, entryID: number) → itemName: IncreasedTraitData[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetLoadoutSerializationVersion

`C_Traits.GetLoadoutSerializationVersion() → serializationVersion: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetMaxAvailableTraitCurrency

`C_Traits.GetMaxAvailableTraitCurrency(traitCurrencyID: number, limitBySourcedMax: bool) → maxAvailable: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetNodeCost

`C_Traits.GetNodeCost(configID: number, nodeID: number) → costs: TraitCurrencyCost[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetNodeInfo

`C_Traits.GetNodeInfo(configID: number, nodeID: number) → nodeInfo: TraitNodeInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetStagedChanges

`C_Traits.GetStagedChanges(configID: number) → nodeIDsWithPurchases: number[], nodeIDsWithRefunds: number[], nodeIDsWithSelectionSwaps: number[]`

- Status: ✅ verified (function)
- Blizzard: Returns IDs of Trait Nodes with pending changes, grouped by the type of change; Returns nothing if there are no pending changes
- `nodeIDsWithSelectionSwaps`: Selection nodes that had a previously committed selected entry, and now have a different selected entry pending
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetStagedChangesCost

`C_Traits.GetStagedChangesCost(configID: number) → costs: TraitCurrencyCost[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetSubTreeInfo

`C_Traits.GetSubTreeInfo(configID: number, subTreeID: number) → subTreeInfo: TraitSubTreeInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetSystemIDByTreeID

`C_Traits.GetSystemIDByTreeID(treeID: number) → systemID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetTraitCurrencyForAchievement

`C_Traits.GetTraitCurrencyForAchievement(traitCurrencyID: number, achievementID: number) → amount: number`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetTraitCurrencyInfo

`C_Traits.GetTraitCurrencyInfo(traitCurrencyID: number) → flags: number, type: number, currencyTypesID: number?, icon: number?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetTraitDescription

`C_Traits.GetTraitDescription(entryID: number, rank: number) → description: string`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetTraitSystemFlags

`C_Traits.GetTraitSystemFlags(configID: number) → flags: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetTraitSystemWidgetSetID

`C_Traits.GetTraitSystemWidgetSetID(configID: number) → uiWidgetSetID: number`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetTreeCurrencyInfo

`C_Traits.GetTreeCurrencyInfo(configID: number, treeID: number, excludeStagedChanges: bool) → treeCurrencyInfo: TreeCurrencyInfo[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetTreeHash

`C_Traits.GetTreeHash(treeID: number) → result: number[]`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetTreeInfo

`C_Traits.GetTreeInfo(configID: number, treeID: number) → treeInfo: TraitTreeInfo`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.GetTreeNodes

`C_Traits.GetTreeNodes(treeID: number) → nodeIDs: number[]`

- Status: ✅ verified (function)
- Blizzard: Returns a list of nodeIDs, sorted ascending, for a given treeID. Contains nodes for all class specializations.
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.HasValidInspectData

`C_Traits.HasValidInspectData() → hasValidInspectData: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.IsReadyForCommit

`C_Traits.IsReadyForCommit() → isReadyForCommit: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.PurchaseAllRanks

`C_Traits.PurchaseAllRanks(configID: number, nodeID: number, ignoreCost: bool) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.PurchaseRank

`C_Traits.PurchaseRank(configID: number, nodeID: number) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.RefundAllRanks

`C_Traits.RefundAllRanks(configID: number, nodeID: number) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.RefundRank

`C_Traits.RefundRank(configID: number, nodeID: number, clearEdges: bool?) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.ResetTree

`C_Traits.ResetTree(configID: number, treeID: number) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.ResetTreeByCurrency

`C_Traits.ResetTreeByCurrency(configID: number, treeID: number, traitCurrencyID: number) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.RollbackConfig

`C_Traits.RollbackConfig(configID: number) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.SetSelection

`C_Traits.SetSelection(configID: number, nodeID: number, nodeEntryID: number?, clearEdges: bool?) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.StageConfig

`C_Traits.StageConfig(configID: number) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.TalentTestUnlearnSpells

`C_Traits.TalentTestUnlearnSpells()`

- Status: ✅ verified (function)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.TryPurchaseAllRanks

`C_Traits.TryPurchaseAllRanks(configID: number, nodeID: number) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.TryPurchaseToNode

`C_Traits.TryPurchaseToNode(configID: number, nodeID: number) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

### C_Traits.TryRefundToNode

`C_Traits.TryRefundToNode(configID: number, nodeID: number, entryID: number) → success: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SharedTraitsDocumentation.lua`

## Events

### CONFIG_COMMIT_FAILED

- Status: ✅ verified
- Payload: `configID: number`
- fires synchronously (Blizzard's docs)

### TRAIT_COND_INFO_CHANGED

- Status: ✅ verified
- Payload: `condID: number`
- fires synchronously (Blizzard's docs)

### TRAIT_CONFIG_CREATED

- Status: ✅ verified
- Payload: `configInfo: TraitConfigInfo`
- fires synchronously (Blizzard's docs)

### TRAIT_CONFIG_DELETED

- Status: ✅ verified
- Payload: `configID: number`
- fires synchronously (Blizzard's docs)

### TRAIT_CONFIG_LIST_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
- Seen firing 64 times (0 in combat); argument kinds: ``

### TRAIT_CONFIG_UPDATED

- Status: ✅ verified
- Payload: `configID: number`
- fires synchronously (Blizzard's docs)
- Seen firing 1 times (0 in combat); argument kinds: `n`

### TRAIT_NODE_CHANGED

- Status: ✅ verified
- Payload: `nodeID: number`
- fires synchronously (Blizzard's docs)
- Seen firing 3 times (0 in combat); argument kinds: `n`

### TRAIT_NODE_CHANGED_PARTIAL

- Status: ✅ verified
- Payload: `ID: number`, `info: TraitNodeInfoPartial`
- fires synchronously (Blizzard's docs)

### TRAIT_NODE_ENTRY_UPDATED

- Status: ✅ verified
- Payload: `nodeEntryID: number`
- fires synchronously (Blizzard's docs)

### TRAIT_SUB_TREE_CHANGED

- Status: ✅ verified
- Payload: `subTreeID: number`
- fires synchronously (Blizzard's docs)

### TRAIT_SYSTEM_INTERACTION_STARTED

- Status: ✅ verified
- Payload: `treeID: number`
- fires synchronously (Blizzard's docs)

### TRAIT_SYSTEM_NPC_CLOSED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### TRAIT_TREE_CHANGED

- Status: ✅ verified
- Payload: `treeID: number`
- fires synchronously (Blizzard's docs)

### TRAIT_TREE_CURRENCY_INFO_UPDATED

- Status: ✅ verified
- Payload: `treeID: number`
- fires synchronously (Blizzard's docs)
- Seen firing 21 times (10 in combat); argument kinds: `n`

### TRY_PURCHASE_TO_NODE_PARTIAL_SUCCESS

- Status: ✅ verified
- Payload: `nodeFinishedOn: number`
- fires synchronously (Blizzard's docs)

## Types

### GroupCurrencyInfo

- Structure
  - `traitNodeGroupID`: number
  - `currencyInfos`: TreeCurrencyInfo[]

### IncreasedTraitData

- Structure
  - `itemNameIncreasing`: string
  - `itemQualityIncreasing`: ItemQuality
  - `numPointsIncreased`: number

### TraitCondInfo

- Structure
  - `condID`: number
  - `ranksGranted`: number?
  - `isAlwaysMet`: bool
  - `isMet`: bool
  - `isGate`: bool
  - `isSufficient`: bool
  - `type`: number
  - `questID`: number?
  - `achievementID`: number?
  - `specSetID`: number?
  - `playerLevel`: number?
  - `traitCurrencyID`: number?
  - `spentAmountRequired`: number?
  - `tooltipFormat`: string?
  - `traitCondAccountElementID`: number?

### TraitConfigInfo

- Structure
  - `ID`: number
  - `type`: TraitConfigType
  - `name`: string
  - `treeIDs`: number[]
  - `usesSharedActionBars`: bool

### TraitCurrencyCost

- Structure
  - `ID`: number
  - `amount`: number

### TraitDefinitionInfo

- Structure
  - `spellID`: number?
  - `overrideName`: string?
  - `overrideSubtext`: string?
  - `overrideDescription`: string?
  - `overrideIcon`: number?
  - `overriddenSpellID`: number?
  - `subType`: TraitDefinitionSubType?

### TraitEntryInfo

- Structure
  - `definitionID`: number?
  - `subTreeID`: number?
  - `type`: TraitNodeEntryType
  - `maxRanks`: number
  - `isAvailable`: bool
  - `isDisplayError`: bool
  - `conditionIDs`: number[]

### TraitEntryRankInfo

- Structure
  - `entryID`: number
  - `rank`: number

### TraitGateInfo

- Structure
  - `topLeftNodeID`: number
  - `conditionID`: number

### TraitGroupDisplayInfo

- Structure
  - `groupID`: number
  - `treeID`: number
  - `skillLineID`: number
  - `orderIndex`: number
  - `displayName`: cstring
  - `icon`: number

### TraitNodeInfo

- Structure
  - `ID`: number
  - `posX`: number
  - `posY`: number
  - `flags`: number
  - `entryIDs`: number[]
  - `entryIDsWithCommittedRanks`: number[]
  - `canPurchaseRank`: bool
  - `canRefundRank`: bool
  - `isAvailable`: bool
  - `isVisible`: bool
  - `isDisplayError`: bool
  - `ranksPurchased`: number
  - `ranksIncreased`: number
  - `entryIDToRanksIncreased`: LuaValueVariant
  - `activeRank`: number
  - `currentRank`: number
  - `activeEntry`: TraitEntryRankInfo?
  - `nextEntry`: TraitEntryRankInfo?
  - `maxRanks`: number
  - `totalMaxRanks`: number
  - `type`: TraitNodeType
  - `visibleEdges`: TraitOutEdgeInfo[]
  - `meetsEdgeRequirements`: bool
  - `groupIDs`: number[]
  - `conditionIDs`: number[]
  - `isCascadeRepurchasable`: bool
  - `cascadeRepurchaseEntryID`: number?
  - `subTreeID`: number?
  - `subTreeActive`: bool?

### TraitNodeInfoPartial

- Structure
  - `canPurchaseRank`: bool?
  - `canRefundRank`: bool?
  - `isAvailable`: bool?
  - `isVisible`: bool?
  - `ranksPurchased`: number?
  - `activeRank`: number?
  - `currentRank`: number?
  - `meetsEdgeRequirements`: bool?
  - `isCascadeRepurchasable`: bool?
  - `activeEntryID`: number?
  - `subTreeActive`: bool?

### TraitOutEdgeInfo

- Structure
  - `targetNode`: number
  - `type`: number
  - `visualStyle`: number
  - `isActive`: bool

### TraitSubTreeInfo

- Structure
  - `ID`: number
  - `name`: string?
  - `description`: string?
  - `iconElementID`: textureAtlas?
  - `traitCurrencyID`: number?
  - `isActive`: bool
  - `subTreeSelectionNodeIDs`: number[]
  - `posX`: number
  - `posY`: number

### TraitTreeInfo

- Structure
  - `ID`: number
  - `gates`: TraitGateInfo[]
  - `hideSingleRankNumbers`: bool
  - `cannotRefund`: bool
  - `rootNodeID`: number?
  - `uiTextureKit`: textureKit
  - `titleText`: string?

### TreeCurrencyInfo

- Structure
  - `traitCurrencyID`: number
  - `quantity`: number
  - `maxQuantity`: number?
  - `spent`: number
  - `spentInTree`: number?
