# converter.py

"""
Defined a pause() function because doing submission from personal computer,
all should be working fine.
"""

# from sys import argv

info = """\n \n \n \n
                  Kyle:Connolly:A00371085:csc227017\n
                  Submission 02\n
                  Converting Times or Temperatures\n
          \n \n \n \n
       """

desc = """
This program just accesses any and all command-line arguments (up to
a maximum of ten) and simply prints them out, one per line. A command-
line argument is something entered on the command line when a program
is run at the command prompt (interactively) in a "command window".

When a Python program runs, all command-line arguments are placed into
a list (which for the moment you can think of as an "array", though Python
does not have arrays in the sense that many other programming languages do).
The array (or list) that receives the command-line parameters is called
sys.argv, and it is only available to a program if the sys module has been
imported into that program.

The name of the running program itself is always the argument at index 0,
which means that the the items actually typed in are conveniently numbered
1, 2, 3, ... and so on, but in fact we usually ignore the program name as
a command-line parameter, and just deal with those entered on the line after
the program name.

Note that if any command-line argument contains one or more bank spaces,
that argument must be enclosed in double quotes (not single quotes).

       """
