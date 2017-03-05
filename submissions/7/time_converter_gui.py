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


desc = "Time Converter for Seconds to hh:mm:ss"


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
