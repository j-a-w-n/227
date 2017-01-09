# My Quick Ref for PEP8

## Indentation
  - 4 ```spaces``` per indentation *level*I
  - Opt for spaces only, no "tabs". Never mix "tabs" & spaces
  - Limit all lines to 79 characters
  - Top-level functions and Class definitions separated with 2 blank lines
    - Methods defined within a Class separated by 1 bank line

## Imports
  - Placed top of file, after Module comments, Docstrings and before modual globals/constants.
  - On separate lines: 
    ```python import os
              import sys
    ```
    - In this order: Std lib imports, Third party, local app/lib specific.

## Whitespace in Expressions & Statements
  - Immediately inside (), [], {}
    ( x[1] ) [X] 
    (x[1]) [Y] 
  - Immediately before open parens that start an arg list of a function call
   ```python 
    n() [X] 
    y() [Y] 
    ```
  - Use 1 space on either side of Binary-operators

    ```python
    x+1 [X]
    y % 3 [Y]
    ```
    - Except on keyword args or default param values
    e.g. ```return magic(r=real, i=imag)```
  - Multi-clause statements should be broken up by statement. One statement, one line
    (indent a statement running beyond 79 chars)
    
## Comments

  - Block comments are indicated with a ```#``` and have a single space after them. 
  - In-line comments are also done using a ```#``` and should be *at least* two spaces from the statement the refer to.
  - Docstrings should be written for all public modules, functions, classes and methods.
    - Mutliline format and single line format:
      -Multiline: ```"""Return a foobang
                        
                      Optional plotz says to frobnicate the bizbaz first.

                     """
                  ```
      -Singleline: ```""" Return a fooband ... """
                   ```
