# BehavioralMessaging

Namespace: `C_BehavioralMessaging`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ✅ | [C_BehavioralMessaging.SendNotificationReceipt](#c_behavioralmessagingsendnotificationreceipt) |  |  |

### C_BehavioralMessaging.SendNotificationReceipt

`C_BehavioralMessaging.SendNotificationReceipt(dbId: NotificationDbId, openTimeSeconds: number, readTimeSeconds: number)`

- Status: ✅ verified (function)
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `BehavioralMessagingDocumentation.lua`

## Events

### BEHAVIORAL_NOTIFICATION

- Status: ✅ verified
- Payload: `notificationType: string`, `dbId: NotificationDbId`
- fires synchronously (Blizzard's docs)
