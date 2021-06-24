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

       # checkbox frame
        self.checkbox_frame = Frame(self.Main_GUI, padx=20, pady=5)
        self.checkbox_frame.grid(row=3)
  
        # checkbox inputs
        self.checkbox_entry = Checkbutton(self.checkbox_frame, text="+", variable="+")
        self.checkbox_entry.grid(row=0)

        self.checkbox_entry = Checkbutton(self.checkbox_frame, text="−", variable="−")
        self.checkbox_entry.grid(row=1)

        self.checkbox_entry = Checkbutton(self.checkbox_frame, text="×", variable="×")
        self.checkbox_entry.grid(row=2)

        self.checkbox_entry = Checkbutton(self.checkbox_frame, text="÷", variable="÷")
        self.checkbox_entry.grid(row=3)

        # buttons frame
        self.buttons_frame = Frame(self.Main_GUI, padx=20, pady=5)
        self.buttons_frame.grid(row=4)

        # Enter button
        self.enter_button = Button(self.buttons_frame, text="Enter", pady=5, padx=5)
        self.enter_button.grid(row=0, column=0, padx=5)

        # Quit Button
        self.quit_button = Button(self.buttons_frame, text="Quit", padx=5, pady=5)
        self.quit_button.grid(row=0, column=1, padx=5)

        # help frame
        self.help_frame = Frame(padx=20, pady=5)
        self.help_frame.grid(row=4)

        # Help Button
        self.help_button = Button(self.help_frame, text='help', padx=32, pady=5)
        self.help_button.grid(row=1, column=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start()
    root.mainloop()
 
 
 

