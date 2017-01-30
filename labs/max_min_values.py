# max_min_values.py
# Kyle Connolly:csc227017:A00371085

from sys import argv


def pause():
    input("Press Enter to continue ... ")


programmer = 'Programmed by Kyle Connolly'
no_arg = 'Warning: You must enter at least one number on the command line.'


def convert_float():
    for item in argv:
        li = float(item)
    large = li.max()
    small = li.min()
    print(large, small)

# def largest_input():
    # print()

# def smallest_input():
    # pass


if len(argv) == 1:
    print(programmer)
    print(no_arg)
    pause()
elif len(argv) > 1:
    convert_float()
    # largest_input()
    # smallest_input()
    pause()
