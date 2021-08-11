from tkinter import *
from functools import partial  # To prevent unwanted windows
import random

class Start:
    def __init__(self, error=""):
        
        # Master frame
        self.master = Frame(padx=20, pady=10)
        self.master.grid()

        # Quiz heading
        self.heading_label = Label(self.master, font='arial 19 bold', text="Math Quiz")
        self.heading_label.grid(row=0)

        # Error label
        self.error_label = Label(self.master, text="", font='arial 12', fg='maroon', wraplength=150)
        self.error_label.grid()

        if error != "":
            self.error_label.config(text=error)

        # entry frame
        self.entry_frame = Frame(self.master)
        self.entry_frame.grid()

        # Min Entry 
        self.min_entry = Entry(self.entry_frame, width=8, font='arial 14')
        self.min_entry.grid(row=2, column=0)

        # Max Entry 
        self.max_entry = Entry(self.entry_frame, width=8, font='arial 14')
        self.max_entry.grid(row=2, column=1)

        # Buttons frame
        self.buttons_frame = Frame(self.master, padx=5, pady=5)
        self.buttons_frame.grid(row=3)

        # plus button
        self.plus_button = Button(self.buttons_frame, text="+", command=lambda:Start.error_checking(self, "+"), pady=5, padx=16)
        self.plus_button.grid(row=0, column=0)

        # minus button
        self.minus_button = Button(self.buttons_frame, text="−", command=lambda:Start.error_checking(self, "-"), pady=5, padx=16)
        self.minus_button.grid(row=0, column=1)

        # times button
        self.times_button = Button(self.buttons_frame, text="×", command=lambda:Start.error_checking(self, "*"), pady=5, padx=16)
        self.times_button.grid(row=1, column=0)

        # Quit Button
        self.quit_button = Button(self.buttons_frame, text="⏎", command=self.to_quit, pady=5, padx=14)
        self.quit_button.grid(row=1, column=1)

        # help frame
        self.help_frame = Frame(self.master)
        self.help_frame.grid()

        # Help Button
        self.help_button = Button(self.help_frame, text='help', command=lambda:Help(), padx=20, pady=5)
        self.help_button.grid(row=2, column=0)


    def error_checking(self, operation):
        try:
            # Sets the minimum value and maximum value
            min = self.min_entry.get()
            max = self.max_entry.get()

            print("You chose {}".format(operation))

            
            # Checks if the entry is blank. If it is, the user will get an error.
            if min == "" or max == "":
                self.error_label.config(text="Entry is blank")
                return

            min = int(min)
            max = int(max)
            # Checks if user has entered a min number higher than 0.
            if min <= 0:
                self.error_label.config(text="Enter a number higher than 0.")
                return
            # Checks if minimum number is higher than max number. If it is then print an error
            if min > max:
                self.error_label.config(text="Minimum is higher than max, please enter a lower number", fg='maroon')
                return
            # If there are no problems, the error label will hide itself
            else:
                self.error_label.config(text="Valid", fg='green')


        except ValueError:
            self.error_label.config(text="Please enter a valid number.")
        
    def to_quit(self):
        root.destroy()


class Help:
    def __init__(self):

        # Sets up child window (help box)
        self.help_box = Toplevel()

        # if users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help))

        # Setup GUI Frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        # Setup Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                    font="arial 14 bold")
        self.how_heading.grid(row=0)

        help_text = "Input One (left box) must be lower than or equal to Input Two (right box). " \
                    "Only input integers, no decimals, letters or special characters."

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text,
                                justify=LEFT, wrap=400, padx=10, pady=10)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_box, text="Dismiss", width=10,
                                    bg='dark red', fg='white', font="arial 10 bold",
                                    command=partial(self.close_help))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self):
        # Put help button back to normal..
        self.help_box.destroy()

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math")
    something = Start()
    root.mainloop()
