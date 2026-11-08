# SpellActivationOverlay

Namespace: `C_SpellActivationOverlay`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_SpellActivationOverlay.IsSpellOverlayed](#c_spellactivationoverlayisspelloverlayed) | 1 value | 1 value |

### C_SpellActivationOverlay.IsSpellOverlayed

`C_SpellActivationOverlay.IsSpellOverlayed(spellID: number) → isSpellOverlayed: bool`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Called out of combat with `spell`: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `SpellActivationOverlayDocumentation.lua`

## Events

### SPELL_ACTIVATION_OVERLAY_GLOW_HIDE

- Status: ✅ verified
- Payload: `spellID: number`
- fires synchronously (Blizzard's docs)

### SPELL_ACTIVATION_OVERLAY_GLOW_SHOW

- Status: ✅ verified
- Payload: `spellID: number`
- fires synchronously (Blizzard's docs)

### SPELL_ACTIVATION_OVERLAY_HIDE

- Status: ✅ verified
- Payload: `spellID: number?`
- fires synchronously (Blizzard's docs)
- Seen firing 30442 times (1813 in combat); argument kinds: `-`

### SPELL_ACTIVATION_OVERLAY_SHOW

- Status: ✅ verified
- Payload: `spellID: number`, `overlayFileDataID: number`, `locationType: ScreenLocationType`, `scale: number`, `r: number`, `g: number`, `b: number`
- fires synchronously (Blizzard's docs)
