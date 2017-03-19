import tkinter
import tkinter.messagebox as popup


class Oscars():
    """
    Creates gui and works with txt file
    """
    def __init__(self):
        # Window & three frames
        self.window = tkinter.Tk()
        self.top = tkinter.Frame()
        self.mid = tkinter.Frame()
        self.title_frame = tkinter.Frame()
        self.genre_frame = tkinter.Frame()
        self.window.title("Academy Awards")
        # Widgets for top frame
        self.enter_year = tkinter.Label(
                self.top,
                text='Enter Year (1928-2016): '
                )
        self.entry = tkinter.Entry(
                self.top,
                width=4
                )
        # Pack
        self.enter_year.pack(side='left')
        self.entry.pack(side='left')
        # Widgets for mid frame
        self.button = tkinter.Button(
                self.mid,
                text="Show That Year's Best Picture'",
                command=self.get_info
                )
        # Pack
        self.button.pack(side='right')
        # Widgets for title frame
        self.title = tkinter.StringVar()
        self.title_label = tkinter.Label(
                self.title_frame,
                text='Film Title: ',
                )
        self.title_value = tkinter.Label(
                self.title_frame,
                width=30,
                textvariable=self.title
                )
        # Widgets for genre frame
        self.genre = tkinter.StringVar()
        self.genre_label = tkinter.Label(
                self.genre_frame,
                text='Film Genre: ',
                )
        self.genre_value = tkinter.Label(
                self.genre_frame,
                width=30,
                textvariable=self.genre
                )
        # Pack
        self.title_label.pack(side='left')
        self.title_value.pack(side='right')
        # Pack
        self.genre_label.pack(side='left')
        self.genre_value.pack(side='right')
        # Pack the four frames
        self.top.pack()
        self.mid.pack()
        self.title_frame.pack()
        self.genre_frame.pack()
        # Enter window's mainloop
        self.window.mainloop()

    def get_info(self):
        """Callback for self.button - gets user's year input and returns
           the correlated title & genre
        """
        try:
            user_input = int(self.entry.get())
        except ValueError:
            popup.showinfo("Error",
                           "Input value for year cannot be converted to " +
                           "an integer year.")

        with open('Oscars.txt', 'r') as data:
            for i, line in enumerate(data):
                if (user_input-1928) == i:
                    line_info = line.split(',')
                    self.title.set(line_info[0])
                    self.genre.set(line_info[1])
            if user_input > 2016 or user_input < 1928:
                popup.showinfo("Error",
                               "Requested year is out of range. \n" +
                               "It must lie in the interval 1928 to 2016.")


app = Oscars()
