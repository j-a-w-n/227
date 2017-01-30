#Class 7
##Jan. 25, 2017

##Containers
- `list` e.g. `list = [1, 2, 3, 4]`  `list = [1, "two", True, function()]`
- `tuple` e.g. `tuple = (1, 2, 3, 4)`  `tuple = (9, "five", False, invoke())`
- `dictionary` or `map` or `associative array` e.g. `dict = {"Joe":23, "Al":47,}`
  - Collection of key:value pairs, similar to JSON / Object literals in JS
- `set` e.g. `set = {1, 2, 3}` does not store duplicates

###We can manipulate lists with similar methods as string objects
  - `list`s are mutable, we can change their values and indexes
  - `tuple`s are immutable, their values and indexes remain the same
  - Both `set` and `list` are non-sequential, they are hashed and therefore *cannot* be accessed by `[]` + an index value 
