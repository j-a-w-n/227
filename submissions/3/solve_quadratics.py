# solve_quadratics.py
# Kyle:Connolly:A00371085:csc227107
# Submission 03
# Solving Quadratic Equations

"""
Defined a pause() function because doing submission from personal linux
machine, took out some blank-lines as per feedback. Both assignemnt 1 &
2 lookedfine on my machine and a school computer - if this assignment
looks weird please ping me and e-mail at
kyle.connolly@smu.ca - as I don't want to make things difficult for you!
Also, this assignment is a little sloppy, I can't seem to format the strings
properly - tired and not seeing my mistakes.
Looking forward to your correction!
"""

from math import sqrt
from sys import argv


def pause():

    input("Press Enter to continue ... ")


info = """\n \n
                  Kyle:Connolly:A00371085:csc227017\n
                  Submission 03\n
                  Solving Quadratic Equations\n
          \n \n
       """

desc = """
This program solves quadratic equations, one equation per run, if the
equation is in fact solvable (has real roots).

If not, the program simply reports that the equation cannot be solved,
pauses, and then terminates when the user presses Enter.

The coefficients of the standard quadratic equation

ax**2 + bx + c = 0

are entered on the command line in the order a, b, c. If nothing is entered
on the command line, an opening identification screen is displayed first,
followed by a screen containing this information. Each screen has a pause at
the end to allow the user to read it.

If one or more values are entered, the program checks to make sure that
there are exactly three, and reports an error if that is not the case.
If there are three values, they are all assumed to be real numbers, and
no further error checking is performed. If the entered values do correspond
to a solvable quadratic equation, the two roots of the equation are computed
and displayed. Depending on the coefficients, the roots may, of course, be
identical. In any case, a pause again precedes program termination.
"""


def no_input():

    print(info)
    pause()
    print(desc)


def must_be_three():

    print("""
Error: Wrong number of command-line arguments (must be three).
Program now terminating.""")


def formula():

    a = float(argv[1])
    b = float(argv[2])
    c = float(argv[3])
    d = (b**2) - (4*a*c)
    if d < 0:
        no_roots = """
Warning: The quadratic equation {0:g}x**2+{0:g}x+{0:g} = 0 has no roots.
Program now terminating.\
""".format(a, b, c)
        print(no_roots)
    elif d >= 0:
        r1 = float((-b-sqrt(d))/(2*a))
        r2 = float((-b+sqrt(d))/(2*a))
        if r1 == r2:
            same_root = """
The quadratic equation {0:g}x**2{0:g}x+{0:g} = 0 has two identical roots\
equal to {0:00}.
Program now terminating.\
            """.format(a, b, c, r1)
            print(same_root)
        else:
            roots = """
The quadratic equation {0:g}x**2+{0:g}x+{0:g} = 0 has the two roots \
{0:0} and {0:0}.
Program now terminating.\
            """.format(a, b, c, r1, r2)
            print(roots)


def solve_quadratics():

    if len(argv) == 1:
        no_input()
    elif len(argv) != 4:
        must_be_three()
    elif len(argv) == 4:
        formula()


solve_quadratics()
pause()
