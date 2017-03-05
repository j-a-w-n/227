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


desc = """
 or a time value given as a total number
of seconds to the corresponding equivalent hours, minutes and seconds.
"""


def info():

    tkinter.messagebox.showinfo(
            'Program Information',
            'Kyle:Connolly:A00371085:csc227017' + '\n'
            'Submission 07' + '\n'
            'Converting Time with a GUI' + '\n' + '\n'
            'This program allows the user to convert either a temperature' +
            ' value (eitherFahrenheit to Celsius or vice versa) or a time' +
            ' value given as a total number of seconds to the corresponding' +
            ' equivalent hours, minutes and seconds.'
            )


def convert():

    time = float(entry.get())
    t = timedelta(seconds=time)
    tkinter.messagebox.showinfo(
            'Conversion Result',
            str(int(time)) + ' seconds in hh:mm:ss format is 0' + str(t)
            )


parent = tkinter.Tk()

desc_label = tkinter.Label(textvariable="desc")
prompt_label = tkinter.Label(text='Enter a number of inches: ')
entry = tkinter.Entry(parent, width=10)

info_button = tkinter.Button(
        text='Get Information',
        command=info)

convert_button = tkinter.Button(
        text='Convert Seconds',
        command=convert
        )

quit_button = tkinter.Button(
        text='quit',
        command=parent.destroy
        )
desc_label.pack()
prompt_label.pack()
entry.pack()
info_button.pack()
convert_button.pack()
quit_button.pack()
tkinter.mainloop()
