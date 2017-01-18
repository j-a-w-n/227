# Class 5
## Jan. 18, 2017
---------

- `len()` gives us length of a string
- `[x:y]` slices a string with x beginning at char @ position, y ending but not including position (within string's index)
- Page 73 has a table of string methods.
  `"some string with string value".strmethod()`
  The var, or literal string must be appended with the string method. 
  - For example 
```python
s = "text, text, text."
s.capitalize()

>>> 'Text, text, text.'
```
- there are a number of `isxyz()` string methods, which return a bool value
- `print(x, end=" ")` the print stmt has an implicit `end=` parameter, which is `\n` by default, by explicitly stating an alternative, we can print different results.
- `list` is a keyword - I used it as a var name is sub. 1. Refrain from using keywords as var names!! 
