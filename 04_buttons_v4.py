from tkinter import *
from functools import partial # To prevent unwanted windows
import random
 
 
class Start:
    def __init__(self):
 
        # GUI frame
        self.Main_GUI = Frame(padx=20, pady=10)
        self.Main_GUI.grid()

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
        self.quit_button = Button(self.buttons_3_frame, text="Quit", command=self.to_quit, padx=9, pady=5)
        self.quit_button.grid(row=1, column=1, padx=5)

        # Help Button
        self.help_button = Button(self.buttons_3_frame, text='help', command=lambda:Help(), padx=11, pady=5)
        self.help_button.grid(row=1, column=0)


    # quit function
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
                    "Only input integers, no decimals, letters, special letters etc."

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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start()
    root.mainloop()