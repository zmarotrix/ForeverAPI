# AnimaDiversionInfo

Namespace: `C_AnimaDiversion`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_AnimaDiversion.CloseUI](#c_animadiversioncloseui) |  |  |
| ✅ | [C_AnimaDiversion.GetAnimaDiversionNodes](#c_animadiversiongetanimadiversionnodes) | 0 values |  |
| ✅ | [C_AnimaDiversion.GetOriginPosition](#c_animadiversiongetoriginposition) | 1 value |  |
| ✅ | [C_AnimaDiversion.GetReinforceProgress](#c_animadiversiongetreinforceprogress) | 1 value |  |
| ✅ | [C_AnimaDiversion.GetTextureKit](#c_animadiversiongettexturekit) | 1 value |  |
| ✅ | [C_AnimaDiversion.OpenAnimaDiversionUI](#c_animadiversionopenanimadiversionui) |  |  |
| ✅ | [C_AnimaDiversion.SelectAnimaNode](#c_animadiversionselectanimanode) |  |  |

### C_AnimaDiversion.CloseUI

`C_AnimaDiversion.CloseUI()`

- Status: ✅ verified (function)
- Source: client docs `AnimaDiversionUIDocumentation.lua`

### C_AnimaDiversion.GetAnimaDiversionNodes

`C_AnimaDiversion.GetAnimaDiversionNodes() → animaNodes: AnimaDiversionNodeInfo[]`

- Status: ✅ verified (function)
- may return nothing (Blizzard's docs; not checked in game)
- Called out of combat: returned 0 values
- Source: client docs `AnimaDiversionUIDocumentation.lua`

### C_AnimaDiversion.GetOriginPosition

`C_AnimaDiversion.GetOriginPosition() → normalizedPosition: vector2?`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Source: client docs `AnimaDiversionUIDocumentation.lua`

### C_AnimaDiversion.GetReinforceProgress

`C_AnimaDiversion.GetReinforceProgress() → progress: number`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Source: client docs `AnimaDiversionUIDocumentation.lua`

### C_AnimaDiversion.GetTextureKit

`C_AnimaDiversion.GetTextureKit() → textureKit: textureKit`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `nil`
- Source: client docs `AnimaDiversionUIDocumentation.lua`

### C_AnimaDiversion.OpenAnimaDiversionUI

`C_AnimaDiversion.OpenAnimaDiversionUI()`

- Status: ✅ verified (function)
- Source: client docs `AnimaDiversionUIDocumentation.lua`

### C_AnimaDiversion.SelectAnimaNode

`C_AnimaDiversion.SelectAnimaNode(talentID: number, temporary: bool)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `AnimaDiversionUIDocumentation.lua`

## Events

### ANIMA_DIVERSION_CLOSE

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

### ANIMA_DIVERSION_OPEN

- Status: ✅ verified
- Payload: `info: AnimaDiversionFrameInfo`
- fires synchronously (Blizzard's docs)

### ANIMA_DIVERSION_TALENT_UPDATED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### AnimaDiversionCostInfo

- Structure
  - `currencyID`: number
  - `quantity`: number

### AnimaDiversionFrameInfo

- Structure
  - `textureKit`: textureKit
  - `title`: string
  - `mapID`: number

### AnimaDiversionNodeInfo

- Structure
  - `talentID`: number
  - `name`: string
  - `description`: string
  - `costs`: AnimaDiversionCostInfo[]
  - `currencyID`: number
  - `icon`: number
  - `normalizedPosition`: vector2
  - `state`: AnimaDiversionNodeState

### AnimaDiversionNodeState

- Enumeration — ✅ verified
  - `Unavailable` = 0
  - `Available` = 1
  - `SelectedTemporary` = 2
  - `SelectedPermanent` = 3
  - `Cooldown` = 4
