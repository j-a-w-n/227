# RainfallProcessor.py
# Kyle:Connolly:A00371085:csc227107
# Submission 06
# Retrieving and Processing Rainfall Data Classes
"""
An event I hadn't planned for was if user input no year at all, in this
assignment I have the program terminate. I have also tried to open the data
file via `with - as` operators, which has saved me a bit of code. Also,
I've changed the list of month to a tuple of MONTHS; becuase those values
remain constant.

From sys, I'm using `platform` to try and test the general OS the programm
is running on and que the proper shell cmd based on the result. It's worked
for me on my Linux machine, please let me know if you've had trouble with it.

"""


class RainfallProcessor(object):
    """Sets up an instance with a text file associated."""
    def __init__(self, rainfall_file):
        self.rainfall_file = rainfall_file

    from sys import exit as exit
    from sys import platform as platform
    from os import system as system

    MONTHS = ("January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November",
              "December")

    def process_rainfall_file(self):
        """This function is called from the driver to run the program and
        populate data, if any.

        Handles context of the class instance's text file object, taking
        care of setup and teardown logic. Creates global obj `YEAR` and
        `RAIN_LINE` used in helper method title() and month_stats().
        """

        self.clear()
        global YEAR
        YEAR = input("\nEnter year for which you want rainfall data: ")
        with open(self.rainfall_file) as infile:
            while YEAR:
                current_line = infile.readline().strip()
                if YEAR == current_line:
                    global RAIN_LINE
                    RAIN_LINE = infile.readline().split()
                    self.title()
                    self.month_stats()
                    break
                if not current_line and current_line != YEAR:
                    print("\nNo rainfall data found for year {}.".format(YEAR))
                    self.pause()
                    self.repeat()

    def month_stats(self):
        """Responsible for outputting rainfall data, if available for the
        user's supplied year.
        """

        rain_float = [float(n) for n in RAIN_LINE]
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
        high = self.MONTHS[rain_float.index(max(rain_float))]
        low = self.MONTHS[rain_float.index(min(rain_float))]
        calc = [total, avg, high, low]
        stats = """\
===== Total rainfall for the year... {:.1f}
===== Average monthly rainfall...... {:.1f}
===== Month with highest rainfall... {}
===== Month with lowest rainfall.... {}\
        """.format(*calc)
        print(months)
        print(stats)
        self.pause()
        self.repeat()

    def title(self):
        """Prints the heading for rainfall data of user's supplied year."""

        print("\n===== Rainfall Summary for {}".format(YEAR))

    def clear(self):
        """Calls appropriate shell command, depending on user's
        operating system.
        """

        if self.platform.lower() is 'linux' or 'darwin':
            self.system("clear")
        elif self.platform.lower() is 'windows':
            self.system("cls")

    def ok(self):
        "Outputs message to user program will terminate."

        print("OK ... Program now terminating.")

    def repeat(self):
        """Prompts user whether or not they'd like to find data for another
        year, either calls process_rainfall_file() again or
        terminates program."""

        ask = input("\nDo it again for another year? [[y]/n] ")
        if ask == "n":
            print()
            self.ok()
            self.pause()
            self.exit()
        else:
            self.process_rainfall_file()

    def pause(self):
        "Halts program untill user provides stdin from keyboard."

        input("Press Enter to continue ... ")

