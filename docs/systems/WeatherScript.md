# WeatherScript

Namespace: `C_Weather`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_Weather.GetCurrentWeather](#c_weathergetcurrentweather) | 1 value | 1 value |

### C_Weather.GetCurrentWeather

`C_Weather.GetCurrentWeather() → info: WeatherInfo`

- Status: ✅ verified (function)
- Blizzard: C_Weather the outlook is favorable.
- Called out of combat: returned 1 value: `table{intensity=number,type=number}`
- Called in combat: returned 1 value: `table{intensity=number,type=number}`
- Source: client docs `WeatherScriptDocumentation.lua`

## Events

### WEATHER_CHANGED

- Status: ✅ verified
- Payload: none
- Blizzard: The weather has taken a turn.
- unique event (Blizzard's docs)
- Seen firing 116 times (0 in combat); argument kinds: ``

## Types

### WeatherInfo

- Structure
  - `type`: WeatherType
  - `intensity`: number
