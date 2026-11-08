# CooldownViewer

Namespace: `C_CooldownViewer`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_CooldownViewer.GetCooldownViewerCategorySet](#c_cooldownviewergetcooldownviewercategoryset) |  |  |
| ❔ | [C_CooldownViewer.GetCooldownViewerCooldownInfo](#c_cooldownviewergetcooldownviewercooldowninfo) |  |  |
| ❔ | [C_CooldownViewer.GetGroupBuffItems](#c_cooldownviewergetgroupbuffitems) |  |  |
| ❔ | [C_CooldownViewer.GetLayoutData](#c_cooldownviewergetlayoutdata) |  |  |
| ❔ | [C_CooldownViewer.GetValidAlertTypes](#c_cooldownviewergetvalidalerttypes) |  |  |
| ❔ | [C_CooldownViewer.IsCooldownViewerAvailable](#c_cooldownvieweriscooldownvieweravailable) |  |  |
| ❔ | [C_CooldownViewer.SetLayoutData](#c_cooldownviewersetlayoutdata) |  |  |

### C_CooldownViewer.GetCooldownViewerCategorySet

`C_CooldownViewer.GetCooldownViewerCategorySet(category: CooldownViewerCategory, allowUnlearned: bool = False) → cooldownIDs: number[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CooldownViewerDocumentation.lua`

### C_CooldownViewer.GetCooldownViewerCooldownInfo

`C_CooldownViewer.GetCooldownViewerCooldownInfo(cooldownID: number) → cooldownInfo: CooldownViewerCooldown`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CooldownViewerDocumentation.lua`

### C_CooldownViewer.GetGroupBuffItems

`C_CooldownViewer.GetGroupBuffItems() → groupBuffItems: GroupBuffItem[]`

- Status: ❔ unverified
- Source: client docs `CooldownViewerDocumentation.lua`

### C_CooldownViewer.GetLayoutData

`C_CooldownViewer.GetLayoutData() → data: cstring`

- Status: ❔ unverified
- Source: client docs `CooldownViewerDocumentation.lua`

### C_CooldownViewer.GetValidAlertTypes

`C_CooldownViewer.GetValidAlertTypes(cooldownID: number) → validAlertTypes: CooldownViewerAlertEventType[]`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CooldownViewerDocumentation.lua`

### C_CooldownViewer.IsCooldownViewerAvailable

`C_CooldownViewer.IsCooldownViewerAvailable() → isAvailable: bool, failureReason: string`

- Status: ❔ unverified
- Source: client docs `CooldownViewerDocumentation.lua`

### C_CooldownViewer.SetLayoutData

`C_CooldownViewer.SetLayoutData(data: cstring)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `CooldownViewerDocumentation.lua`

## Events

### COOLDOWN_VIEWER_DATA_LOADED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### COOLDOWN_VIEWER_SPELL_OVERRIDE_UPDATED

- Status: ❔ unverified
- Payload: `baseSpellID: number`, `overrideSpellID: number?`
- fires synchronously (Blizzard's docs)

### COOLDOWN_VIEWER_TABLE_HOTFIXED

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### CooldownViewerCooldown

- Structure
  - `cooldownID`: number
  - `spellID`: number?
  - `spellCategoryID`: number?
  - `overrideSpellID`: number?
  - `overrideTooltipSpellID`: number?
  - `equipSlot`: luaIndex?
  - `buffSlot`: luaIndex?
  - `linkedSpellIDs`: number[]
  - `selfAura`: bool
  - `hasAura`: bool
  - `charges`: bool
  - `isKnown`: bool
  - `isInvisible`: bool
  - `flags`: CooldownSetSpellFlags
  - `category`: CooldownViewerCategory

### GroupBuffItem

- Structure
  - `spellID`: number
  - `displaySpellID`: number
  - `name`: cstring
  - `iconID`: fileID
  - `flags`: GroupBuffItemFlags
  - `isKnown`: bool
