# WowEntitlementInfo

## Events

### ENTITLEMENT_DELIVERED

- Status: ✅ verified
- Payload: `entitlementType: WoWEntitlementType`, `textureID: number`, `name: string`, `payloadID: number?`, `showFancyToast: bool`
- fires synchronously (Blizzard's docs)

### RAF_ENTITLEMENT_DELIVERED

- Status: ✅ verified
- Payload: `entitlementType: WoWEntitlementType`, `textureID: number`, `name: string`, `payloadID: number?`, `showFancyToast: bool`, `rafVersion: RecruitAFriendRewardsVersion`
- fires synchronously (Blizzard's docs)

## Types

### WoWEntitlementType

- Enumeration — ✅ verified
  - `Item` = 0
  - `Mount` = 1
  - `Battlepet` = 2
  - `Toy` = 3
  - `Appearance` = 4
  - `AppearanceSet` = 5
  - `GameTime` = 6
  - `Title` = 7
  - `Illusion` = 8
  - `Invalid` = 9
