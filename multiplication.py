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

        # buttons frame
        self.buttons_frame = Frame(self.Main_GUI)
        self.buttons_frame.grid(row=3)

        # plus button
        self.plus_button = Button(self.buttons_frame, text="+", command=lambda: Game(), pady=5, padx=16)
        self.plus_button.grid(row=0, column=0, padx=0)

        # minus button
        self.minus_button = Button(self.buttons_frame, text="−", command=lambda: self.in_between("'"), pady=5, padx=16)
        self.minus_button.grid(row=0, column=1, padx=0)

        # times button
        self.times_button = Button(self.buttons_frame, text="×", command=lambda: self.in_between("'"), pady=5, padx=16)
        self.times_button.grid(row=1, column=0, padx=0)

        # divide button
        self.divide_button = Button(self.buttons_frame, text="÷", command=lambda: self.in_between("'"), pady=5, padx=16)
        self.divide_button.grid(row=1, column=1, padx=0)

        # Help Button
        self.help_button = Button(self.buttons_frame, text='help', command=lambda:Help(), padx=8, pady=5)
        self.help_button.grid(row=2, column=0, pady=5)
        
        # Quit Button
        self.quit_button = Button(self.buttons_frame, text="Quit", command=self.to_quit, padx=8, pady=5)
        self.quit_button.grid(row=2, column=1, pady=5)
        
        # error labels
        self.error_frame = Frame(self.Main_GUI, padx=10, pady=10,)
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
                self.error_1_label.config(fg='maroon', text="Error: Min value > Max value")
            
            if max > min:
                self.error_1_label.config(fg='green', text="Valid: Min value = {} | Max value = {}".format(min, max))
 
        except ValueError:
            has_errors = "yes"
            self.error_1_label.config(fg='maroon', text="Enter an integer for Max and min value\nMin < Max")
            
    
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


class Game:
    def __init__(self):

        self.game_box = Toplevel()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start()
    root.mainloop()
 
 
 

