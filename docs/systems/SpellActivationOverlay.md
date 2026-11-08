# SpellActivationOverlay

Namespace: `C_SpellActivationOverlay`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_SpellActivationOverlay.IsSpellOverlayed](#c_spellactivationoverlayisspelloverlayed) |  |  |

### C_SpellActivationOverlay.IsSpellOverlayed

`C_SpellActivationOverlay.IsSpellOverlayed(spellID: number) → isSpellOverlayed: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SpellActivationOverlayDocumentation.lua`

## Events

### SPELL_ACTIVATION_OVERLAY_GLOW_HIDE

- Status: ❔ unverified
- Payload: `spellID: number`
- fires synchronously (Blizzard's docs)

### SPELL_ACTIVATION_OVERLAY_GLOW_SHOW

- Status: ❔ unverified
- Payload: `spellID: number`
- fires synchronously (Blizzard's docs)

### SPELL_ACTIVATION_OVERLAY_HIDE

- Status: ❔ unverified
- Payload: `spellID: number?`
- fires synchronously (Blizzard's docs)

### SPELL_ACTIVATION_OVERLAY_SHOW

- Status: ❔ unverified
- Payload: `spellID: number`, `overlayFileDataID: number`, `locationType: ScreenLocationType`, `scale: number`, `r: number`, `g: number`, `b: number`
- fires synchronously (Blizzard's docs)
