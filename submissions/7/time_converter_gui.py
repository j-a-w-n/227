# converter.py
# Kyle:Connolly:A00371085:csc227107
# Submission 02
# Converting Time or Temperature

"""
Self-Eval.........
"""


import tkinter
import tkinter.messagebox
from datetime import timedelta


info = """\n \n \n \n
                  Kyle:Connolly:A00371085:csc227017\n
                  Submission 07\n
                  Converting Time with a GUI\n
          \n \n \n \n
       """

desc = """
This program allows the user to convert either a temperature value (either
Fahrenheit to Celsius or vice versa) or a time value given as a total number
of seconds to the corresponding equivalent hours, minutes and seconds.
"""


def info():
    tkinter.messagebox.showinfo(
            'Program Information',
            textvariable=info
            )


def convert():

    time = float(entry.get())
    t = timedelta(seconds=time)
    t = format(t, "1.2f")
    tkinter.messagebox.showinfo(
            'Conversion Result',
            str(time) + 'seconds in hh:mm:ss format is 0' + str(t)
            )


parent = tkinter.Tk()

desc_label = tkinter.Label(textvariable="desc").pack()
prompt_label = tkinter.Label(text='Enter a number of inches: ').pack()
entry = tkinter.Entry(parent, textvariable="StringVar", width=10).pack()

info_button = tkinter.Button(
        text='Get Information',
        command=info).pack()

convert_button = tkinter.Button(
        text='Convert Seconds',
        command=convert
        ).pack()

quit_button = tkinter.Button(
        text='quit',
        command=parent.destroy
        ).pack()

tkinter.mainloop()
