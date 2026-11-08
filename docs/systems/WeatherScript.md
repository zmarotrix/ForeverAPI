# WeatherScript

Namespace: `C_Weather`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_Weather.GetCurrentWeather](#c_weathergetcurrentweather) |  |  |

### C_Weather.GetCurrentWeather

`C_Weather.GetCurrentWeather() → info: WeatherInfo`

- Status: ❔ unverified
- Blizzard: C_Weather the outlook is favorable.
- Source: client docs `WeatherScriptDocumentation.lua`

## Events

### WEATHER_CHANGED

- Status: ❔ unverified
- Payload: none
- Blizzard: The weather has taken a turn.
- unique event (Blizzard's docs)

## Types

### WeatherInfo

- Structure
  - `type`: WeatherType
  - `intensity`: number
