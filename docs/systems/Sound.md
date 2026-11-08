# Sound

Namespace: `C_Sound`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_Sound.GetSoundScaledVolume](#c_soundgetsoundscaledvolume) |  |  |
| ❔ | [C_Sound.IsPlaying](#c_soundisplaying) |  |  |
| ❔ | [C_Sound.PlayItemSound](#c_soundplayitemsound) |  |  |
| ❔ | [C_Sound.PlaySound](#c_soundplaysound) |  |  |
| ❔ | [C_Sound.PlaySoundWithOptions](#c_soundplaysoundwithoptions) |  |  |
| ❔ | [C_Sound.PlayVocalErrorSound](#c_soundplayvocalerrorsound) |  |  |

### C_Sound.GetSoundScaledVolume

`C_Sound.GetSoundScaledVolume(soundHandle: number) → scaledVolume: number`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoundDocumentation.lua`

### C_Sound.IsPlaying

`C_Sound.IsPlaying(soundHandle: number) → isPlaying: bool`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoundDocumentation.lua`

### C_Sound.PlayItemSound

`C_Sound.PlayItemSound(soundType: ItemSoundType, itemLocation: ItemLocation)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoundDocumentation.lua`

### C_Sound.PlaySound

`C_Sound.PlaySound(soundKitID: number, uiSoundSubType: UISoundSubType = g_defaultSI3UISoundSubTypeForLua, forceNoDuplicates: bool = False, runFinishCallback: bool = False, overridePriority: number?, volumeOverride: number?) → success: bool, soundHandle: SoundHandle`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoundDocumentation.lua`

### C_Sound.PlaySoundWithOptions

`C_Sound.PlaySoundWithOptions(params: PlaySoundParams) → success: bool, soundHandle: SoundHandle`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoundDocumentation.lua`

### C_Sound.PlayVocalErrorSound

`C_Sound.PlayVocalErrorSound(vocalErrorSoundID: Vocalerrorsounds)`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `SoundDocumentation.lua`

## Events

### SOUNDKIT_FINISHED

- Status: ❔ unverified
- Payload: `soundHandle: number`
- fires synchronously (Blizzard's docs)

### SOUND_DEVICE_UPDATE

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

## Types

### PlaySoundParams

- Structure
  - `soundKitID`: number
  - `uiSoundSubType`: UISoundSubType
  - `forceNoDuplicates`: bool
  - `runFinishCallback`: bool
  - `overridePriority`: number?
  - `volumeOverride`: number?

### PlaySoundResult

- Structure
  - `success`: bool
  - `soundHandle`: SoundHandle
