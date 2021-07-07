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
        self.entry_frame.grid(row=1)

        self.low_amount_entry = Entry(self.entry_frame, font="Arial 19 bold", width=8)
        self.low_amount_entry.grid(row=0, column=0)
  
        self.high_amount_entry = Entry(self.entry_frame, font="Arial 19 bold", width=8)
        self.high_amount_entry.grid(row=0, column=1)
 
        # error labels
        self.error_frame = Frame(self.Main_GUI, padx=10, pady=10)
        self.error_frame.grid(row=2)
 
        self.error_1_label = Label(self.error_frame, fg="maroon",
                                        text="", font="Arial 9 bold", wrap=275)
        self.error_1_label.grid(row=0, column=0)

        # buttons frame
        self.buttons_1_frame = Frame(self.Main_GUI, padx=20, pady=5)
        self.buttons_1_frame.grid()

        # bottom buttons frame
        self.buttons_2_frame = Frame(self.Main_GUI, padx=20, pady=5)
        self.buttons_2_frame.grid()

        # bottom buttons frame
        self.buttons_3_frame = Frame(self.Main_GUI, padx=20, pady=5)
        self.buttons_3_frame.grid()

        # plus button
        self.plus_button = Button(self.buttons_1_frame, text="+", pady=5, padx=16)
        self.plus_button.grid(row=0, column=0, padx=2)

        # minus button
        self.minus_button = Button(self.buttons_1_frame, text="−", pady=5, padx=16)
        self.minus_button.grid(row=0, column=1, padx=2)

        # times button
        self.times_button = Button(self.buttons_2_frame, text="×", pady=5, padx=16)
        self.times_button.grid(row=0, column=0, padx=2)

        # divide button
        self.divide_button = Button(self.buttons_2_frame, text="÷", pady=5, padx=16)
        self.divide_button.grid(row=0, column=1, padx=2)

        # Quit Button
        self.quit_button = Button(self.buttons_3_frame, text="Quit", padx=9, pady=5)
        self.quit_button.grid(row=1, column=1, padx=5)

        # Help Button
        self.help_button = Button(self.buttons_3_frame, text='help', padx=11, pady=5)
        self.help_button.grid(row=1, column=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start()
    root.mainloop()
 
 
 

