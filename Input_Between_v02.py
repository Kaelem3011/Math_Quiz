from tkinter import *
from functools import partial # To prevent unwanted windows
import random
 
 
class Start:
    def __init__(self):
 
        # GUI frame
        self.Main_GUI = Frame(padx=20, pady=10)
        self.Main_GUI.grid()
 
 
        # Quiz Heading(row 0)
        self.math_box_label = Label(self.Main_GUI, text="Math Quiz", font="Arial 19 bold")
        self.math_box_label.grid(row=0)
 
        # entry frame
        self.entry_frame = Frame(self.Main_GUI, padx=10, pady=10)
        self.entry_frame.grid()
 
        self.low_amount_entry = Entry(self.entry_frame, font="Arial 19 bold", width=8)
        self.low_amount_entry.grid(row=0, column=0)
 
        self.high_amount_entry = Entry(self.entry_frame, font="Arial 19 bold", width=8)
        self.high_amount_entry.grid(row=0, column=1)
 
        # Enter button
        self.enter_button = Button(self.Main_GUI, text="Enter", command=lambda: self.in_between("lol"), pady=5, padx=5)
        self.enter_button.grid(row=3, column=0, padx=5)
 
        # error labels
        self.error_frame = Frame(self.Main_GUI, padx=10, pady=10)
        self.error_frame.grid(row=2)
 
        self.error_1_label = Label(self.error_frame, fg="maroon",
                                        text="", font="Arial 9 bold", wrap=275)
        self.error_1_label.grid(row=0, column=0)
 
    # function detects if user input has min and max
    def in_between (self, operation):
 
        error_back = "red"
        error_feedback = "no errors"
 
        try:
            min = int(self.low_amount_entry.get())
            max = int(self.high_amount_entry.get())
 
            if min > max:
                self.error_1_label.config(text="Error: Min value > Max value")
            
            if max > min:
                self.error_1_label.config(text="Valid: Min value = {} | Max value = {}".format(min, max))
 
        except ValueError:
            has_errors = "yes"
            self.error_1_label.config(text="Enter an integer for Max and min value\nMin < Max")
            
 
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start()
    root.mainloop()
 
 
 

