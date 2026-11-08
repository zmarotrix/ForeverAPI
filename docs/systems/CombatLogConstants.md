# CombatLogConstants

## Types

### CombatLogMessageLimits

- Constants — ✅ verified
  - `CombatLogDefaultMessageLimit` = 300
  - `CombatLogMaximumMessageLimit` = 1000

### CombatLogObject

- Enumeration — ✅ verified
  - `Empty` = 0
  - `AffiliationMine` = 1
  - `AffiliationParty` = 2
  - `AffiliationRaid` = 4
  - `AffiliationOutsider` = 8
  - `ReactionFriendly` = 16
  - `ReactionNeutral` = 32
  - `ReactionHostile` = 64
  - `ControlPlayer` = 256
  - `ControlNpc` = 512
  - `TypePlayer` = 1024
  - `TypeNpc` = 2048
  - `TypePet` = 4096
  - `TypeGuardian` = 8192
  - `TypeObject` = 16384
  - `Target` = 65536
  - `Focus` = 131072
  - `Maintank` = 262144
  - `Mainassist` = 524288
  - `None` = 2147483648

### CombatLogObjectMasks

- Constants — ✅ verified
  - `COMBATLOG_OBJECT_AFFILIATION_MASK` = 15
  - `COMBATLOG_OBJECT_REACTION_MASK` = 240
  - `COMBATLOG_OBJECT_CONTROL_MASK` = 768
  - `COMBATLOG_OBJECT_TYPE_MASK` = 64512
  - `COMBATLOG_OBJECT_SPECIAL_MASK` = 4294901760
- ⚠️ `COMBATLOG_OBJECT_SPECIAL_MASK`: docs say 4294901760, game has -65536

### CombatLogObjectTarget

- Enumeration — ✅ verified
  - `Raidtarget1` = 1
  - `Raidtarget2` = 2
  - `Raidtarget3` = 4
  - `Raidtarget4` = 8
  - `Raidtarget5` = 16
  - `Raidtarget6` = 32
  - `Raidtarget7` = 64
  - `Raidtarget8` = 128
  - `RaidNone` = 2147483648

### CombatLogObjectTargetMasks

- Constants — ✅ verified
  - `COMBATLOG_OBJECT_RAID_TARGET_MASK` = 255
  - `COMBATLOG_OBJECT_RAID_MASK` = 4294967295
- ⚠️ `COMBATLOG_OBJECT_RAID_MASK`: docs say 4294967295, game has -1
