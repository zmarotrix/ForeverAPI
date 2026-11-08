# ClickBindings

Namespace: `C_ClickBindings`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_ClickBindings.CanSpellBeClickBound](#c_clickbindingscanspellbeclickbound) |  |  |
| ✅ | [C_ClickBindings.ExecuteBinding](#c_clickbindingsexecutebinding) |  |  |
| ✅ | [C_ClickBindings.GetBindingType](#c_clickbindingsgetbindingtype) |  |  |
| ✅ | [C_ClickBindings.GetEffectiveInteractionButton](#c_clickbindingsgeteffectiveinteractionbutton) |  |  |
| ✅ | [C_ClickBindings.GetProfileInfo](#c_clickbindingsgetprofileinfo) |  |  |
| 🆕 | [C_ClickBindings.GetStringFromModifiers](#c_clickbindingsgetstringfrommodifiers) |  |  |
| ✅ | [C_ClickBindings.GetTutorialShown](#c_clickbindingsgettutorialshown) |  |  |
| 🆕 | [C_ClickBindings.MakeModifiers](#c_clickbindingsmakemodifiers) |  |  |
| ✅ | [C_ClickBindings.ResetCurrentProfile](#c_clickbindingsresetcurrentprofile) |  |  |
| ✅ | [C_ClickBindings.SetProfileByInfo](#c_clickbindingssetprofilebyinfo) |  |  |
| ✅ | [C_ClickBindings.SetTutorialShown](#c_clickbindingssettutorialshown) |  |  |

### C_ClickBindings.CanSpellBeClickBound

`C_ClickBindings.CanSpellBeClickBound(spellID: SpellIdentifier) → canBeBound: bool`

- Status: ✅ verified (function)
- `spellID`: Base spellID for spell, spellID for PetAction
- secret arguments: AllowedWhenTainted (Blizzard's docs; not checked in game)
- Source: client docs `ClickBindingsDocumentation.lua`

### C_ClickBindings.ExecuteBinding

`C_ClickBindings.ExecuteBinding(targetToken: cstring, button: cstring, modifiers: number)`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClickBindingsDocumentation.lua`

### C_ClickBindings.GetBindingType

`C_ClickBindings.GetBindingType(button: cstring, modifiers: number) → type: ClickBindingType`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClickBindingsDocumentation.lua`

### C_ClickBindings.GetEffectiveInteractionButton

`C_ClickBindings.GetEffectiveInteractionButton(button: cstring, modifiers: number) → effectiveButton: cstring`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClickBindingsDocumentation.lua`

### C_ClickBindings.GetProfileInfo

`C_ClickBindings.GetProfileInfo() → infoVec: ClickBindingInfo[]`

- Status: ✅ verified (function)
- Source: client docs `ClickBindingsDocumentation.lua`

### C_ClickBindings.GetStringFromModifiers

`C_ClickBindings.GetStringFromModifiers(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_ClickBindings.GetTutorialShown

`C_ClickBindings.GetTutorialShown() → tutorialShown: bool`

- Status: ✅ verified (function)
- Source: client docs `ClickBindingsDocumentation.lua`

### C_ClickBindings.MakeModifiers

`C_ClickBindings.MakeModifiers(...)`

- Status: 🆕 in game, not in Blizzard's docs (function)

### C_ClickBindings.ResetCurrentProfile

`C_ClickBindings.ResetCurrentProfile()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `ClickBindingsDocumentation.lua`

### C_ClickBindings.SetProfileByInfo

`C_ClickBindings.SetProfileByInfo(infoVec: ClickBindingInfo[])`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `ClickBindingsDocumentation.lua`

### C_ClickBindings.SetTutorialShown

`C_ClickBindings.SetTutorialShown()`

- Status: ✅ verified (function)
- Source: client docs `ClickBindingsDocumentation.lua`

## Events

### CLICKBINDINGS_SET_HIGHLIGHTS_SHOWN

- Status: ✅ verified
- Payload: `showHighlights: bool`
- fires synchronously (Blizzard's docs)
