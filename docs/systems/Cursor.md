# Cursor

Namespace: `C_Cursor`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [C_Cursor.GetCursorItem](#c_cursorgetcursoritem) |  |  |

### C_Cursor.GetCursorItem

`C_Cursor.GetCursorItem() → item: ItemLocation`

- Status: ❔ unverified
- may return nothing (Blizzard's docs; not checked in game)
- Source: client docs `CursorDocumentation.lua`

## Events

### BATTLE_PET_CURSOR_CLEAR

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### CURSOR_CHANGED

- Status: ❔ unverified
- Payload: `isDefault: bool`, `newCursorType: UICursorType`, `oldCursorType: UICursorType`, `oldCursorVirtualID: number`
- fires synchronously (Blizzard's docs)

### MOUNT_CURSOR_CLEAR

- Status: ❔ unverified
- Payload: none
- fires synchronously (Blizzard's docs)

### WORLD_CURSOR_TOOLTIP_UPDATE

- Status: ❔ unverified
- Payload: `anchorType: WorldCursorAnchorType`
- Blizzard: Sends an update when the mouse enters or leaves something in-world (object, unit, etc) that should display a tooltip
- fires synchronously (Blizzard's docs)
