from tkinter import *
from functools import partial # To prevent unwanted windows
import random
 
 
class Start:
    def __init__(self):
 
        # GUI frame
        self.Main_GUI = Frame(padx=20, pady=10)
        self.Main_GUI.grid()

        # buttons frame
        self.buttons_frame = Frame(padx=20, pady=10)
        self.buttons_frame.grid()

        # Enter button
        self.enter_button = Button(self.buttons_frame, text="Enter", pady=5, padx=5)
        self.enter_button.grid(row=0, column=0, padx=5)

        # Quit Button
        self.quit_button = Button(self.buttons_frame, text="Quit", command=self.to_quit, padx=5, pady=5)
        self.quit_button.grid(row=0, column=1, padx=5)

        # Help Button
        self.help_button = Button(self.Main_GUI, text='help', padx=15, pady=5)
        self.help_button.grid(row=1, column=0)


    # quit function
    def to_quit(self):
        root.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start()
    root.mainloop()