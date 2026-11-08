# WowSurvey

Namespace: `C_WowSurvey`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_WowSurvey.OpenSurvey](#c_wowsurveyopensurvey) |  |  |
| ✅ | [C_WowSurvey.TriggerSurveyServe](#c_wowsurveytriggersurveyserve) |  |  |

### C_WowSurvey.OpenSurvey

`C_WowSurvey.OpenSurvey()`

- Status: ✅ verified (function)
- restricted in some situations (Blizzard's docs; not checked in game)
- Source: client docs `WowSurveyDocumentation.lua`

### C_WowSurvey.TriggerSurveyServe

`C_WowSurvey.TriggerSurveyServe(deliveryMoment: SurveyDeliveryMoment)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `WowSurveyDocumentation.lua`

## Events

### SURVEY_DELIVERED

- Status: ✅ verified
- Payload: none
- fires synchronously (Blizzard's docs)
