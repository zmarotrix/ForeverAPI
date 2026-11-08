# Covenant

Namespace: `C_Covenants`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Covenants.GetActiveCovenantID](#c_covenantsgetactivecovenantid) | 1 value | 1 value |
| ✅ | [C_Covenants.GetCovenantData](#c_covenantsgetcovenantdata) |  |  |
| ✅ | [C_Covenants.GetCovenantIDs](#c_covenantsgetcovenantids) | 1 value | 1 value |

### C_Covenants.GetActiveCovenantID

`C_Covenants.GetActiveCovenantID() → covenantID: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `CovenantsDocumentation.lua`

### C_Covenants.GetCovenantData

`C_Covenants.GetCovenantData(covenantID: number) → data: CovenantData?`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CovenantsDocumentation.lua`

### C_Covenants.GetCovenantIDs

`C_Covenants.GetCovenantIDs() → covenantID: number[]`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{[number]=number,[number]=number}`
- Called in combat: returned 1 value: `table{[number]=number,[number]=number}`
- Source: client docs `CovenantsDocumentation.lua`

## Events

### COVENANT_CHOSEN

- Status: ✅ verified
- Payload: `covenantID: number`
- fires synchronously (Blizzard's docs)

## Types

### CovenantData

- Structure
  - `ID`: number
  - `textureKit`: textureKit
  - `celebrationSoundKit`: number
  - `animaChannelSelectSoundKit`: number
  - `animaChannelActiveSoundKit`: number
  - `animaGemsFullSoundKit`: number
  - `animaNewGemSoundKit`: number
  - `animaReinforceSelectSoundKit`: number
  - `upgradeTabSelectSoundKitID`: number
  - `reservoirFullSoundKitID`: number
  - `beginResearchSoundKitID`: number
  - `renownFanfareSoundKitID`: number
  - `factionID`: number
  - `name`: cstring
  - `soulbindIDs`: number[]
