# First Class after Break Week
## Tk

- `import tkinter`
- Python had tkinter, however, Arch was missing Tk... `pacman -S tk`
  - tk import now works
- This GUI work will really be all about learning an API
- `.pack()` is what enables up to visually include widgets into our windows
- GUIs are 'Event-Driven'

### Midterm Chat
- Know the `%` operator well
- `Slices[x:y]` from x : up to but *not* including y
- slices mimic `range()` 
- printing returns the value, **without** quotes
  - Understand `print()` kwargs: i.e. `end=''` & `sep=''`
- remember the `len()` function!
- `sorted(obj)` returns expression w/o changing obj value
  - `obj.sort()` mutates the underlying value of obj
- Python functions can return multiple values, stored within a `tuple`
- name == main idiom:
  ```python
  if __name__ == '__main__':
  #call function to run the program
  ```
