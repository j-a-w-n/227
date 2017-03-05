# converter.py
# Kyle:Connolly:A00371085:csc227107
# Submission 07
# Converting Time GUI

"""
I believe things are working & formatted properly, my flake8 shows me no PEP8
errors.
The trickiest part of this submission was adapting the pre-existing code from
sub. 2 to work properly with the tk API, figuring out where and how I could
print text variables and I had initiallybeen packing widgets as I created
them.. e.g. seconds = tkinter.Entry(...).pack().This alters the behaviour of
the widget and caused an error in trying to `.get` the value inmy convertion
function. Turns out when a widget is packed it returns a None object.
Lesson learned.
"""


import tkinter
import tkinter.messagebox
from datetime import timedelta


desc = "Time Converter for Seconds to hh:mm:ss"


def info():
    """Populates a message box with programmer info and
    brief description of the convertion."""
    tkinter.messagebox.showinfo(
            'Program Information',
            'Kyle:Connolly:A00371085:csc227017' + '\n'
            'Submission 07' + '\n'
            'Converting Time with a GUI' + '\n' + '\n'
            'This program allows the user to convert either a time value ' +
            'value given as a total number of seconds to the corresponding' +
            ' equivalent hours, minutes and seconds.'
            )


def convert():
    """Converts the user's input from the `entry` widget
    and prints the value in a dialogue box in proper format."""
    time = float(entry.get())
    t = timedelta(seconds=time)
    tkinter.messagebox.showinfo(
            'Conversion Result',
            str(int(time)) + ' seconds in hh:mm:ss format is 0' + str(t) + '.'
            )


parent = tkinter.Tk()
field = tkinter.Frame()
buttons = tkinter.Frame()

desc_label = tkinter.Label(text=desc)
prompt_label = tkinter.Label(field, text='Enter a number of inches: ')
entry = tkinter.Entry(field, width=10)

desc_label.pack()
prompt_label.pack(side='left')
entry.pack(side='left')

info_button = tkinter.Button(
        buttons,
        text='Get Information',
        command=info)

convert_button = tkinter.Button(
        buttons,
        text='Convert Seconds',
        command=convert
        )

quit_button = tkinter.Button(
        buttons,
        text='Quit',
        command=parent.destroy
        )
info_button.pack(side='left')
convert_button.pack(side='left')
quit_button.pack(side='left')

field.pack()
buttons.pack()

tkinter.mainloop()
