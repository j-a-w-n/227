# RainfallInfo.py
# Kyle:Connolly:A00371085:csc227107
# Submission 06
# Retrieving and Processing Rainfall Data Classes
"""
A more thorough self-assesment is in RainfallProcessor.py
"""


class RainfallInfo():

    opening = """\n \n \n \n \n
                  Kyle:Connolly:A00371085:csc227017
                  Submission 05
                  Retrieving and Processing Rainfall Data
          \n \n \n \n \n
    """

    info = """
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

    def pause(self):
        "Wait for user to enter std.input before continuing"

        input("Press Enter to continue ... ")

    def display_opening_screen(self):

        """Prints the title screen: who's programmed it and their creds and
        pauses for user-input."""
        print(self.opening)
        self.pause()

    def display_program_info(self):

        "Prints the program info / description and pauses for user-input."
        print(self.info)
        self.pause()

