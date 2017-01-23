# converter.py
# Kyle:Connolly:A00371085:csc227107
# Submission 02
# Converting Time or Temperature

"""
Defined a pause() function because doing submission from personal linux
machine, did my best to re-write the .bat file as it was a bash file
originally
"""

from sys import argv
from datetime import timedelta


def pause():

    input("Press Enter to continue ... ")


info = """\n \n \n \n
                  Kyle:Connolly:A00371085:csc227017\n
                  Submission 02\n
                  Converting Time or Temperature\n
          \n \n \n \n
       """

desc = """
This program allows the user to convert either a temperature value (either
Fahrenheit to Celsius or vice versa) or a time value given as a total number
of seconds to the corresponding equivalent hours, minutes and seconds.

Input for the program is entered on the command line, and must be entered in
the following way:

The first input parameter must be one of the following:
time - to indicate that the next input will be a number of seconds
ftemp - to indicate that the next input will be a Fahrenheit temperature
ctemp - to indicate that the next input will be a Celsius temperature

The number of seconds entered must be a positive integer, but a temperature
of either kind can be a real number. The program performs the appropriate
conversion, depending on the input data, and outputs the value entered as
well as the converted equivalent.

For any conversion to take place there must be exactly two input values, the
first of which must be one of the three given above. If the number of inputs
is not two, or if the first is not one of the required ones, an appropriate
message is output and the program terminates. No error checking is performed
on the second input value, which must be an appropriate numerical value.
"""

incorrect = """
Error: Incorrect number of input values (must be exactly 2).
Program now terminating.\
"""

badArg = """
Error: Bad first parameter.
Program now terminating.\
"""


def no_arg():

    print(info)
    pause()
    print(desc)
    pause()


def wrong_arg():

    print(incorrect)
    pause()


def arg_given():

    if argv[1] == 'time':
        convert_time()
    elif argv[1] == 'ctemp':
        convert_celsius()
    elif argv[1] == 'ftemp':
        convert_fahrenheit()
    else:
        print(badArg)
    pause()


def convert_time():

    cast = float(argv[2])
    t = str(timedelta(seconds=cast))
    print("\n{} seconds in hh:mm:ss format is 0{}".format(argv[2], t))


def convert_celsius():

    cast = float(argv[2])
    fahrenheit = (cast * 9) / 5 + 32
    print("""
{:.2f} degrees Celsius is equivalent to {:.2f} degrees Fahrenheit.\
""".format(cast, fahrenheit))


def convert_fahrenheit():

    cast = float(argv[2])
    celsius = (cast - 32) * 5 / 9
    print("""
{:.2f} degrees Fahrenheit is equivalent to {:.2f} degrees Celsius.\
""".format(cast, celsius))


def convertion():

    if len(argv) == 1:
        no_arg()
    elif len(argv) > 3:
        wrong_arg()
    elif len(argv) == 2:
        wrong_arg()
    elif len(argv) == 3:
        arg_given()


convertion()
