# LuaTableExtensions

Namespace: `table`

## Functions

| | Function | Out of combat | In combat |
|---|---|---|---|
| ❔ | [table.contains](#tablecontains) |  |  |
| ❔ | [table.count](#tablecount) |  |  |
| ❔ | [table.create](#tablecreate) |  |  |
| ❔ | [table.freeze](#tablefreeze) |  |  |
| ❔ | [table.getcountinfo](#tablegetcountinfo) |  |  |
| ❔ | [table.indexof](#tableindexof) |  |  |
| ❔ | [table.isempty](#tableisempty) |  |  |
| ❔ | [table.isfrozen](#tableisfrozen) |  |  |
| ❔ | [table.keys](#tablekeys) |  |  |
| ❔ | [table.removeunordered](#tableremoveunordered) |  |  |
| ❔ | [table.removevalue](#tableremovevalue) |  |  |
| ❔ | [table.values](#tablevalues) |  |  |

### table.contains

`table.contains(table: table, value: any?) → containsValue: bool`

- Status: ❔ unverified
- Blizzard: Returns true if any value in the table compares equal to the specified value.
- `table`: The table to search.
- `value`: The value for which to search.
- `containsValue`: True if any entry in the table has the specified value.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaTableExtensionsDocumentation.lua`

### table.count

`table.count(table: table) → count: number`

- Status: ❔ unverified
- Blizzard: Returns the number of entries in the table.
- `table`: The table whose entries will be counted.
- `count`: The number of entries in the table.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- SecretWhenLuaTableHasSecretKeys (Blizzard's docs; not checked in game)
- Source: client docs `LuaTableExtensionsDocumentation.lua`

### table.create

`table.create(arraySizeHint: number, nodeSizeHint: number = 0) → table: table`

- Status: ❔ unverified
- Blizzard: Creates an empty table with storage preallocated for the specified number of array and non-array entries.
- `arraySizeHint`: The number of array entries for which to preallocate storage.
- `nodeSizeHint`: The number of non-array entries for which to preallocate storage.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaTableExtensionsDocumentation.lua`

### table.freeze

`table.freeze(table: table) → frozen: table`

- Status: ❔ unverified
- Blizzard: Marks a supplied table as frozen, preventing any modifications to its contents, or replacement of its metatable. If the table has a pre-existing metatable with a '__newindex' table or function, assignments will pass through without raising errors. For tainted code, only tables created by the same addon making this function call are permitted to be frozen.
- `table`: The table to freeze.
- `frozen`: The supplied table, passed through.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaTableExtensionsDocumentation.lua`

### table.getcountinfo

`table.getcountinfo(table: table) → numEntries: number, numPositiveIntegerKeys: number, maxPositiveIntegerKey: number`

- Status: ❔ unverified
- Blizzard: Returns detailed information about the number and distribution of entries in the table.
- `table`: The table to inspect.
- `numEntries`: The total number of entries in the table.
- `numPositiveIntegerKeys`: The number of entries with positive integral keys.
- `maxPositiveIntegerKey`: The largest positive integral key in the table, or zero if no such keys were found.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- SecretWhenLuaTableHasSecretKeys (Blizzard's docs; not checked in game)
- Source: client docs `LuaTableExtensionsDocumentation.lua`

### table.indexof

`table.indexof(table: table, value: any?) → index: number?`

- Status: ❔ unverified
- Blizzard: Returns the first integer index whose value compares equal to the specified value, searching consecutively from index 1 until the first nil value.
- `table`: The table to search.
- `value`: The value for which to search.
- `index`: The first matching index, or nil if no match is found.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaTableExtensionsDocumentation.lua`

### table.isempty

`table.isempty(table: table) → empty: bool`

- Status: ❔ unverified
- Blizzard: Returns true if the table contains no entries.
- `empty`: True if the table contains no entries; otherwise false.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- SecretWhenLuaTableHasSecretKeys (Blizzard's docs; not checked in game)
- Source: client docs `LuaTableExtensionsDocumentation.lua`

### table.isfrozen

`table.isfrozen(table: table) → frozen: bool`

- Status: ❔ unverified
- Blizzard: Returns true if a table has been marked as frozen.
- `table`: The table to inspect.
- `frozen`: True if the table has been made read-only; otherwise false.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaTableExtensionsDocumentation.lua`

### table.keys

`table.keys(table: table) → keys: any`

- Status: ❔ unverified
- Blizzard: Returns an array containing the keys of the specified table.
- `table`: The table whose keys will be returned.
- `keys`: An array containing the table's keys. The order of the returned keys is unspecified.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaTableExtensionsDocumentation.lua`

### table.removeunordered

`table.removeunordered(table: table, index: number?) → value: any?`

- Status: ❔ unverified
- Blizzard: Removes the value at the specified integer index by replacing it with the last value in the array and shortening the array by one element. The order of values in the array is not preserved.
- `table`: The table from which to remove a value.
- `index`: The integer index of the value to remove. If omitted, the last value is removed.
- `value`: The removed value, or nil if the index is outside the array bounds.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaTableExtensionsDocumentation.lua`

### table.removevalue

`table.removevalue(table: table, value: any?) → removedCount: number`

- Status: ❔ unverified
- Blizzard: Removes all values equal to the specified value from the array portion of a table.
- `table`: The table from which to remove values.
- `value`: The value to remove.
- `removedCount`: The number of values removed.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaTableExtensionsDocumentation.lua`

### table.values

`table.values(table: table) → values: any`

- Status: ❔ unverified
- Blizzard: Returns an array containing the values of the specified table.
- `table`: The table whose values will be returned.
- `values`: An array containing the table's values. The order of the returned values is unspecified.
- secret arguments: AllowedWhenUntainted (Blizzard's docs; not checked in game)
- Source: client docs `LuaTableExtensionsDocumentation.lua`
