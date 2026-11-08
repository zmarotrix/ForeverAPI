# CombatAudioAlertShared

## Types

### CombatAudioAlertCastState

- Enumeration — ❔ unverified
  - `Off` = 0
  - `OnCastStart` = 1
  - `OnCastEnd` = 2

### CombatAudioAlertCategory

- Enumeration — ❔ unverified
  - `General` = 0
  - `PlayerHealth` = 1
  - `TargetHealth` = 2
  - `PlayerCast` = 3
  - `TargetCast` = 4
  - `PlayerResource1` = 5
  - `PlayerResource2` = 6
  - `PartyHealth` = 7
  - `PlayerDebuffs` = 8
  - `PlayerHealthPulse` = 9

### CombatAudioAlertDebuffSelfAlertValues

- Enumeration — ❔ unverified
  - `Off` = 0
  - `DispelType` = 1

### CombatAudioAlertPartyPercentValues

- Enumeration — ❔ unverified
  - `Off` = 0
  - `Under100Percent` = 1
  - `Under90Percent` = 2
  - `Under80Percent` = 3
  - `Under70Percent` = 4
  - `Under60Percent` = 5
  - `Under50Percent` = 6
  - `Under40Percent` = 7
  - `Under30Percent` = 8
  - `Under20Percent` = 9
  - `Under10Percent` = 10

### CombatAudioAlertPercentValues

- Enumeration — ❔ unverified
  - `Off` = 0
  - `Every10Percent` = 1
  - `Every20Percent` = 2
  - `Every30Percent` = 3
  - `Every40Percent` = 4
  - `Every50Percent` = 5

### CombatAudioAlertPlayerCastFormatValues

- Enumeration — ❔ unverified
  - `CastingSpellname` = 0
  - `CastSpellname` = 1
  - `Casting` = 2
  - `Cast` = 3
  - `Spellname` = 4

### CombatAudioAlertPlayerDebuffFormatValues

- Enumeration — ❔ unverified
  - `Full` = 0
  - `NoSpellname` = 1

### CombatAudioAlertPlayerHealthFormatValues

- Enumeration — ❔ unverified
  - `HealthFull` = 0
  - `HealthNoPercent` = 1
  - `HealthNoPercentDiv10` = 2
  - `NoHealthFull` = 3
  - `NoHealthNoPercent` = 4
  - `NoHealthNoPercentDiv10` = 5

### CombatAudioAlertPlayerResourceFormatValues

- Enumeration — ❔ unverified
  - `ResourceFull` = 0
  - `ResourceNoPercent` = 1
  - `ResourceNoPercentDiv10` = 2
  - `NoResourceFull` = 3
  - `NoResourceNoPercent` = 4
  - `NoResourceNoPercentDiv10` = 5

### CombatAudioAlertPulsePercentValues

- Enumeration — ❔ unverified
  - `Off` = 0
  - `Under90Percent` = 1
  - `Under80Percent` = 2
  - `Under70Percent` = 3
  - `Under60Percent` = 4
  - `Under50Percent` = 5
  - `Under40Percent` = 6
  - `Under30Percent` = 7
  - `Under20Percent` = 8
  - `Under10Percent` = 9

### CombatAudioAlertSayIfTargetedType

- Enumeration — ❔ unverified
  - `None` = 0
  - `Aggro` = 1
  - `Targeted` = 2
  - `TargetedBy` = 3

### CombatAudioAlertSpecSetting

- Enumeration — ❔ unverified
  - `Resource1Percent` = 0
  - `Resource1Format` = 1
  - `Resource1Voice` = 2
  - `Resource1Volume` = 3
  - `Resource2Percent` = 4
  - `Resource2Format` = 5
  - `Resource2Voice` = 6
  - `Resource2Volume` = 7
  - `SayIfTargeted` = 8

### CombatAudioAlertTargetCastFormatValues

- Enumeration — ❔ unverified
  - `TargetCastingSpellname` = 0
  - `TargetCastSpellname` = 1
  - `CastingSpellname` = 2
  - `CastSpellname` = 3
  - `Casting` = 4
  - `Cast` = 5
  - `Spellname` = 6

### CombatAudioAlertTargetDeathBehavior

- Enumeration — ❔ unverified
  - `Default` = 0
  - `SayTargetDead` = 1

### CombatAudioAlertTargetHealthFormatValues

- Enumeration — ❔ unverified
  - `NoHealthFull` = 0
  - `NoHealthNoPercent` = 1
  - `NoHealthNoPercentDiv10` = 2
  - `HealthFull` = 3
  - `HealthNoPercent` = 4
  - `HealthNoPercentDiv10` = 5
  - `TargetFull` = 6
  - `TargetNoPercent` = 7
  - `TargetNoPercentDiv10` = 8

### CombatAudioAlertThrottle

- Enumeration — ❔ unverified
  - `Sample` = 0
  - `PlayerHealth` = 1
  - `TargetHealth` = 2
  - `PlayerCast` = 3
  - `TargetCast` = 4
  - `PlayerResource1` = 5
  - `PlayerResource2` = 6
  - `PlayerHealthSamePercent` = 7
  - `TargetHealthSamePercent` = 8
  - `PlayerResource1SamePercent` = 9
  - `PlayerResource2SamePercent` = 10

### CombatAudioAlertType

- Enumeration — ❔ unverified
  - `Health` = 0
  - `Cast` = 1

### CombatAudioAlertUnit

- Enumeration — ❔ unverified
  - `Player` = 0
  - `Target` = 1
