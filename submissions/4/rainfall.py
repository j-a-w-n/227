# rainfall.py
# Kyle:Connolly:A00371085:csc227107
# Submission 04
# Retrieving and Processing Rainfall Data
"""

I don't know how I managed, but I think I've got this assignment figured out,

I know this is two weeks late, but I would love it if you could point some-
things out from this code.
"""

from sys import argv, exit
from os import system


def clear():
    system("clear")


def ok():
    print("OK ... Program now terminating.")


def repeat():
    ask = input("\nDo it again for another year? [[y]/n] ")
    if ask == "n":
        print()
        ok()
        pause()
        exit()
    else:
        user_input()


def pause():
    input("Press Enter to continue ... ")


info = """\n \n \n \n \n
                  Kyle:Connolly:A00371085:csc227017
                  Submission 04
                  Retrieving and Processing Rainfall Data
          \n \n \n \n \n
       """

desc = """
This program opens a file of text containing rainfall data for any number of
years. The data for any year is contained on two lines of the file. The first
of those two lines contains just the year, while the second line contains 12
values, each representing the recorded rainfall for a month of the year given
on the preceding line. Thus the file data for two years might look like this:
2014
12 23.5 20 17.2 15 19 16 3 12 22 11.6 7
2015
10 18.2 10 11 7.5 1.9 5 3 9.6 13 6 5.4

Note that the rainfall amounts can be integers or real numbers and that the
values are separated by blank spaces. No units (centimetres or inches, say)
are given, since they are irrelevant for our purposes.

The name of the file containing the rainfall data must be entered as the only
command-line argument, and the file is assumed to exist and be located in the
current directory (the directory in which the program is running). If data for
the entered year exists, it is displayed along with the yearly total and the
monthly average rainfall amounts, as well as the months with the highest and
lowest rainfall amounts. If no data exists for the year entered, a message to
that effect is output. The data for any number of years may be processed on a
single run.
"""
month = ["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November",
         "December"]


def no_input():
    print(info)
    pause()
    print(desc)
    pause()


def title():
    print("\n===== Rainfall Summary for {}".format(year))


def month_stats():
    global rain_line
    rain_float = [float(n) for n in rain_line.split()]
    months = """\
January..... {0}  July........ {6}
February.... {1}  August...... {7}
March....... {2}  September... {8}
April....... {3}  October..... {9}
May......... {4}  November.... {10}
June........ {5}  December.... {11}\
    """.format(*rain_float)
    total = sum(rain_float)
    avg = total / 12
    high = month[rain_float.index(max(rain_float))]
    low = month[rain_float.index(min(rain_float))]
    calc = [total, avg, high, low]
    stats = """\
===== Total rainfall for the year... {:.1f}
===== Average monthly rainfall...... {:.1f}
===== Month with highest rainfall... {}
===== Month with lowest rainfall.... {}\
    """.format(*calc)
    print(months)
    print(stats)
    pause()
    repeat()


def user_input():
    clear()
    global infile
    infile = open(argv[1])
    global year
    year = input("\nEnter year for which you want rainfall data: ")
    while True:
        current_line = infile.readline().strip()
        if year == current_line:
            global rain_line
            rain_line = infile.readline().strip()
            title()
            month_stats()
            break
        if not current_line and current_line != year:
            print("\nNo rainfall data found for year {}.".format(year))
            pause()
            repeat()


def rainfall():
    if len(argv) == 1:
        no_input()
    elif len(argv) == 2:
        user_input()


rainfall()
