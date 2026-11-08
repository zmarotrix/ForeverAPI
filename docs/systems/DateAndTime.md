# DateAndTime

Namespace: `C_DateAndTime`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_DateAndTime.AdjustTimeByDays](#c_dateandtimeadjusttimebydays) |  |  |
| ✅ | [C_DateAndTime.AdjustTimeByMinutes](#c_dateandtimeadjusttimebyminutes) |  |  |
| ✅ | [C_DateAndTime.AdjustTimeByMonths](#c_dateandtimeadjusttimebymonths) |  |  |
| ✅ | [C_DateAndTime.CompareCalendarTime](#c_dateandtimecomparecalendartime) |  |  |
| ✅ | [C_DateAndTime.GetCalendarTimeFromEpoch](#c_dateandtimegetcalendartimefromepoch) |  |  |
| ✅ | [C_DateAndTime.GetCurrentCalendarTime](#c_dateandtimegetcurrentcalendartime) | 1 value | 1 value |
| ✅ | [C_DateAndTime.GetSecondsUntilDailyReset](#c_dateandtimegetsecondsuntildailyreset) | 1 value | 1 value |
| ✅ | [C_DateAndTime.GetSecondsUntilWeeklyReset](#c_dateandtimegetsecondsuntilweeklyreset) | 1 value | 1 value |
| ✅ | [C_DateAndTime.GetServerTimeLocal](#c_dateandtimegetservertimelocal) | 1 value | 1 value |
| ✅ | [C_DateAndTime.GetWeeklyResetStartTime](#c_dateandtimegetweeklyresetstarttime) | 1 value | 1 value |
| ✅ | [C_DateAndTime.IsDayTime](#c_dateandtimeisdaytime) | 1 value | 1 value |

### C_DateAndTime.AdjustTimeByDays

`C_DateAndTime.AdjustTimeByDays(date: CalendarTime, days: number) → newDate: CalendarTime`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DateAndTimeDocumentation.lua`

### C_DateAndTime.AdjustTimeByMinutes

`C_DateAndTime.AdjustTimeByMinutes(date: CalendarTime, minutes: number) → newDate: CalendarTime`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DateAndTimeDocumentation.lua`

### C_DateAndTime.AdjustTimeByMonths

`C_DateAndTime.AdjustTimeByMonths(date: CalendarTime, months: number) → newDate: CalendarTime`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DateAndTimeDocumentation.lua`

### C_DateAndTime.CompareCalendarTime

`C_DateAndTime.CompareCalendarTime(lhsCalendarTime: CalendarTime, rhsCalendarTime: CalendarTime) → comparison: number`

- Status: ✅ verified (function)
- `comparison`: -1 if rhsCalendarTime < lhsCalendarTime, 0 if rhsCalendarTime == lhsCalendarTime, 1 if rhsCalendarTime > lhsCalendarTime
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DateAndTimeDocumentation.lua`

### C_DateAndTime.GetCalendarTimeFromEpoch

`C_DateAndTime.GetCalendarTimeFromEpoch(epoch: BigUInteger) → date: CalendarTime`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `DateAndTimeDocumentation.lua`

### C_DateAndTime.GetCurrentCalendarTime

`C_DateAndTime.GetCurrentCalendarTime() → date: CalendarTime`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `table{hour=number,minute=number,month=number,monthDay=number,weekday=number,year=number}`
- Called in combat: returned 1 value: `table{hour=number,minute=number,month=number,monthDay=number,weekday=number,year=number}`
- Source: client docs `DateAndTimeDocumentation.lua`

### C_DateAndTime.GetSecondsUntilDailyReset

`C_DateAndTime.GetSecondsUntilDailyReset() → seconds: time_t`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `DateAndTimeDocumentation.lua`

### C_DateAndTime.GetSecondsUntilWeeklyReset

`C_DateAndTime.GetSecondsUntilWeeklyReset() → seconds: time_t`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `DateAndTimeDocumentation.lua`

### C_DateAndTime.GetServerTimeLocal

`C_DateAndTime.GetServerTimeLocal() → serverTimeLocal: time_t`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `DateAndTimeDocumentation.lua`

### C_DateAndTime.GetWeeklyResetStartTime

`C_DateAndTime.GetWeeklyResetStartTime() → seconds: time_t`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `number`
- Called in combat: returned 1 value: `number`
- Source: client docs `DateAndTimeDocumentation.lua`

### C_DateAndTime.IsDayTime

`C_DateAndTime.IsDayTime() → isDayTime: bool`

- Status: ✅ verified (function)
- Called out of combat: returned 1 value: `boolean`
- Called in combat: returned 1 value: `boolean`
- Source: client docs `DateAndTimeDocumentation.lua`

## Events

### DIEL_CYCLE_CHANGED

- Status: ✅ verified
- Payload: `isDayTime: bool`
- Blizzard: Signaled when the game time transitions between day and night.
- fires synchronously (Blizzard's docs)
- Seen firing 3 times (0 in combat); argument kinds: `b`

## Types

### TimeEventFlag

- Enumeration — ✅ verified
  - `GlueScreenShortcut` = 1
  - `WeeklyReset` = 2
  - `GlobalLaunch` = 4
