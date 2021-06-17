from tkinter import *
from functools import partial # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # Heading frame
        self.start_frame = Frame(padx=5, pady=5)
        self.start_frame.grid()

        # Quiz Heading(row 0)
        self.math_box_label = Label(self.start_frame, text="Math Quiz",
                                       font="Arial 19 bold")
        self.math_box_label.grid(row=0)

        # User input (row 1)
        self.entry_error_frame = Frame(self.start_frame, width=200)
        self.entry_error_frame.grid(row=2)

        self.start_amount_entry = Entry(self.entry_error_frame, font="Arial 19 bold", width=4)
        self.start_amount_entry.grid(row=0, column=0)

        self.add_funds_button = Button(self.entry_error_frame, font="Arial 14 bold",
                                       text="✓")
        self.add_funds_button.grid(row=0, column=1)

        Checkbutton(root, text="+").grid(row=3)
        Checkbutton(root, text="−").grid(row=4)
        Checkbutton(root, text="×").grid(row=5)
        Checkbutton(root, text="÷").grid(row=6) 

        # Button frame
        self.button_frame = Frame()
        self.button_frame.grid(pady=8)
        
        # Play button (row 3)
        self.play_button = Button(self.button_frame, text="Play", pady=5, padx=5)
        self.play_button.grid(row=0, column=0, padx=5)        

        # Quit button (row 3)
        self.quit_button = Button(self.button_frame, text="Quit", pady=5, padx=5)
        self.quit_button.grid(row=0, column=1, padx=5)

        # Help frame
        self.help_frame = Frame()
        self.help_frame.grid(pady=8)

        # Help button (row 2)
        self.help_button = Button(self.help_frame, text="Help", pady=5, padx=30)
        self.help_button.grid(row=0, column=0, pady=0)
        

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start(root)
    root.mainloop()
