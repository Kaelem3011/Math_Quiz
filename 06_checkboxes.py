from tkinter import *
from functools import partial # To prevent unwanted windows
import random

class Start:
    def __init__(self):
        
        # GUI frame
        self.Main_GUI = Frame(padx=20, pady=10)
        self.Main_GUI.grid()

        # checkbox frame
        self.checkbox_frame = Frame(self.Main_GUI, padx=20, pady=5)
        self.checkbox_frame.grid(row=3)
  
        # checkbox input +
        self.checkbox_entry = Checkbutton(self.checkbox_frame, text="+", variable="+")
        self.checkbox_entry.grid(row=0)

        # checkbox input −
        self.checkbox_entry = Checkbutton(self.checkbox_frame, text="−", variable="−")
        self.checkbox_entry.grid(row=1)

        # checkbox input ×
        self.checkbox_entry = Checkbutton(self.checkbox_frame, text="×", variable="×")
        self.checkbox_entry.grid(row=2)

        # checkbox input ÷
        self.checkbox_entry = Checkbutton(self.checkbox_frame, text="÷", variable="÷")
        self.checkbox_entry.grid(row=3)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start()
    root.mainloop()

    ///// to do /////

    refinement for user_input - user enter button instead of checkbox
    create functioning stored variables for checkboxes
    
 