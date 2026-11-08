# PetBattles

Namespace: `C_PetBattles`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_PetBattles.GetBreedQuality](#c_petbattlesgetbreedquality) |  |  |
| ❔ | [C_PetBattles.GetIcon](#c_petbattlesgeticon) |  |  |
| ❔ | [C_PetBattles.GetName](#c_petbattlesgetname) |  |  |
| ❔ | [C_PetBattles.IsPlayerNPC](#c_petbattlesisplayernpc) |  |  |
| ❔ | [C_PetBattles.IsWildBattle](#c_petbattlesiswildbattle) |  |  |

### C_PetBattles.GetBreedQuality

`C_PetBattles.GetBreedQuality(petOwner: BattlePetOwner, slot: number) → quality: BattlePetBreedQuality`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetBattlesDocumentation.lua`

### C_PetBattles.GetIcon

`C_PetBattles.GetIcon(petOwner: BattlePetOwner, slot: number) → iconFileID: fileID`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetBattlesDocumentation.lua`

### C_PetBattles.GetName

`C_PetBattles.GetName(petOwner: BattlePetOwner, slot: number) → customName: string, speciesName: string`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `PetBattlesDocumentation.lua`

### C_PetBattles.IsPlayerNPC

`C_PetBattles.IsPlayerNPC() → isPlayerNPC: bool`

- Status: ❔ unverified
- Source: client docs `PetBattlesDocumentation.lua`

### C_PetBattles.IsWildBattle

`C_PetBattles.IsWildBattle() → isWildBattle: bool`

- Status: ❔ unverified
- Source: client docs `PetBattlesDocumentation.lua`
