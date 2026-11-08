# ClickBindings

Namespace: `C_ClickBindings`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_ClickBindings.CanSpellBeClickBound](#c_clickbindingscanspellbeclickbound) |  |  |
| ❔ | [C_ClickBindings.ExecuteBinding](#c_clickbindingsexecutebinding) |  |  |
| ❔ | [C_ClickBindings.GetBindingType](#c_clickbindingsgetbindingtype) |  |  |
| ❔ | [C_ClickBindings.GetEffectiveInteractionButton](#c_clickbindingsgeteffectiveinteractionbutton) |  |  |
| ❔ | [C_ClickBindings.GetProfileInfo](#c_clickbindingsgetprofileinfo) |  |  |
| ❔ | [C_ClickBindings.GetTutorialShown](#c_clickbindingsgettutorialshown) |  |  |
| ❔ | [C_ClickBindings.ResetCurrentProfile](#c_clickbindingsresetcurrentprofile) |  |  |
| ❔ | [C_ClickBindings.SetProfileByInfo](#c_clickbindingssetprofilebyinfo) |  |  |
| ❔ | [C_ClickBindings.SetTutorialShown](#c_clickbindingssettutorialshown) |  |  |

### C_ClickBindings.CanSpellBeClickBound

`C_ClickBindings.CanSpellBeClickBound(spellID: SpellIdentifier) → canBeBound: bool`

- Status: ❔ unverified
- `spellID`: Base spellID for spell, spellID for PetAction
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `ClickBindingsDocumentation.lua`

### C_ClickBindings.ExecuteBinding

`C_ClickBindings.ExecuteBinding(targetToken: cstring, button: cstring, modifiers: number)`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClickBindingsDocumentation.lua`

### C_ClickBindings.GetBindingType

`C_ClickBindings.GetBindingType(button: cstring, modifiers: number) → type: ClickBindingType`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClickBindingsDocumentation.lua`

### C_ClickBindings.GetEffectiveInteractionButton

`C_ClickBindings.GetEffectiveInteractionButton(button: cstring, modifiers: number) → effectiveButton: cstring`

- Status: ❔ unverified
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClickBindingsDocumentation.lua`

### C_ClickBindings.GetProfileInfo

`C_ClickBindings.GetProfileInfo() → infoVec: ClickBindingInfo[]`

- Status: ❔ unverified
- Source: client docs `ClickBindingsDocumentation.lua`

### C_ClickBindings.GetTutorialShown

`C_ClickBindings.GetTutorialShown() → tutorialShown: bool`

- Status: ❔ unverified
- Source: client docs `ClickBindingsDocumentation.lua`

### C_ClickBindings.ResetCurrentProfile

`C_ClickBindings.ResetCurrentProfile()`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `ClickBindingsDocumentation.lua`

### C_ClickBindings.SetProfileByInfo

`C_ClickBindings.SetProfileByInfo(infoVec: ClickBindingInfo[])`

- Status: ❔ unverified
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClickBindingsDocumentation.lua`

### C_ClickBindings.SetTutorialShown

`C_ClickBindings.SetTutorialShown()`

- Status: ❔ unverified
- Source: client docs `ClickBindingsDocumentation.lua`

## Events

### CLICKBINDINGS_SET_HIGHLIGHTS_SHOWN

- Status: ❔ unverified
- Payload: `showHighlights: bool`
- fires synchronously (Blizzard's docs)
