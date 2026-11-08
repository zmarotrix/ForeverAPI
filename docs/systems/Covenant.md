# Covenant

Namespace: `C_Covenants`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_Covenants.GetActiveCovenantID](#c_covenantsgetactivecovenantid) |  |  |
| ❔ | [C_Covenants.GetCovenantData](#c_covenantsgetcovenantdata) |  |  |
| ❔ | [C_Covenants.GetCovenantIDs](#c_covenantsgetcovenantids) |  |  |

### C_Covenants.GetActiveCovenantID

`C_Covenants.GetActiveCovenantID() → covenantID: number`

- Status: ❔ unverified
- Source: client docs `CovenantsDocumentation.lua`

### C_Covenants.GetCovenantData

`C_Covenants.GetCovenantData(covenantID: number) → data: CovenantData?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CovenantsDocumentation.lua`

### C_Covenants.GetCovenantIDs

`C_Covenants.GetCovenantIDs() → covenantID: number[]`

- Status: ❔ unverified
- Source: client docs `CovenantsDocumentation.lua`

## Events

### COVENANT_CHOSEN

- Status: ❔ unverified
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
