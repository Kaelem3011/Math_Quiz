from tkinter import *
from functools import partial # To prevent unwanted windows
import random


class Start:
    def __init__(self):

        # Heading frame
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Quiz Heading(row 0)
        self.math_box_label = Label(self.start_frame, text="Math Quiz",
                                       font="Arial 19 bold")
        self.math_box_label.grid(row=0)

        # User input (row 1)
        self.get_input_frame = Frame(self.start_frame)
        self.get_input_frame.grid(row=1)

        self.start_amount_entry = Entry(self.get_input_frame, font="Arial 19 bold", width=8)
        self.start_amount_entry.grid(row=0, column=0)

        self.enter_button = Button(self.get_input_frame, font="Arial 14 bold",
                                       text="✓", command=self.error_check)
        self.enter_button.grid(row=0, column=1)
        
        self.error_label = Label(self.start_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.error_label.grid(row=2)

    def error_check(self):
        
        input_answer = self.start_amount_entry.get()
        has_errors = "no"

        self.error_label.config(text="")

        try:
            input_1 = int(input_answer)
            valid_feedback = "Thanks, valid integer"

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please input an integer"

        if has_errors == "yes":
            self.start_amount_entry.config() 
            self.error_label.config(text=error_feedback)

        else:
            self.error_label.config(text=valid_feedback)
     
           
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start()
    root.mainloop()


