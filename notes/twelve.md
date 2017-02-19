#Class 12, Feb. 15
##Classes and `Self`


- `self` is the assignment that is commonly `this` in other languages
  - It's used everywhere in class method defs so that in use an object instance of the class is always acting upon itself / its attributes.
- `self` refers to the object belonging to the *class* we're dealing with
- `self` is a strong *convention* rather than a specifically reserved keyword.
- `_var = x` the "_" before a variable is a convention indicating the var should be kept **private**

```python
def __init__(self, arg1, arg2 = x):
    self._arg1 = arg1
    self._arg2 = arg2
```
  - `__init__` is actually a keyword & object attributeused to define the default construction of an object within a given class. 
  - `__str__` follows the same as above, but creates the definition of what's to be printed when calling `print(created_object)`

- Classes are named as: `My_Class_Name`
- Constants are named as: `A_CONTINUOUS_VALUE`
