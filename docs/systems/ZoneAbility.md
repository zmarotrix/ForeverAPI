# ZoneAbility

Namespace: `C_ZoneAbility`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_ZoneAbility.GetActiveAbilities](#c_zoneabilitygetactiveabilities) |  |  |
| ❔ | [C_ZoneAbility.GetZoneAbilityIcon](#c_zoneabilitygetzoneabilityicon) |  |  |

### C_ZoneAbility.GetActiveAbilities

`C_ZoneAbility.GetActiveAbilities() → zoneAbilities: ZoneAbilityInfo[]`

- Status: ❔ unverified
- Source: client docs `ZoneAbilityDocumentation.lua`

### C_ZoneAbility.GetZoneAbilityIcon

`C_ZoneAbility.GetZoneAbilityIcon(zoneAbilitySpellID: number) → zoneAbilityIconID: number?`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ZoneAbilityDocumentation.lua`

## Types

### ZoneAbilityInfo

- Structure
  - `zoneAbilityID`: number
  - `uiPriority`: number
  - `spellID`: number
  - `textureKit`: textureKit
  - `tutorialText`: cstring?
