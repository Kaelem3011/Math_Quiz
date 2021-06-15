from tkinter import *
from functools import partial # To prevent unwanted windows
import random


class Start:
    def __init__(self):

        # Heading frame
        self.all_input_frame = Frame(padx=10, pady=10)
        self.all_input_frame.grid()

 



        # Quiz Heading(row 0)
        self.math_box_label = Label(self.all_input_frame, text="Math Quiz", font="Arial 19 bold")
        self.math_box_label.grid(row=0)

        # User input 2 (row 1)

       # entry frame
        self.entry_frame = Frame(self.all_input_frame, padx=10, pady=10)
        self.entry_frame.grid(row = 1)

        self.low_amount_entry = Entry(self.entry_frame, font="Arial 19 bold", width=8)
        self.low_amount_entry.grid(row=0, column=0)

        self.high_amount_entry = Entry(self.entry_frame, font="Arial 19 bold", width=8)
        self.high_amount_entry.grid(row=0, column=1)

       # error labels
        self.error_frame = Frame(self.all_input_frame, padx=10, pady=10)
        self.error_frame.grid(row = 2)

        self.error_1_label = Label(self.error_frame, fg="maroon",
                                        text="error 1", font="Arial 10 bold", wrap=275)
        self.error_1_label.grid(row=0, column=0)

        self.error_2_label = Label(self.error_frame, fg="maroon",
                                        text="error 2", font="Arial 10 bold", wrap=275)
        self.error_2_label.grid(row=0, column=1)

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
            self.error_1_label.config(text=error_feedback, fg='maroon')

        else:
            self.error_1_label.config(text=valid_feedback, fg='green')


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start()
    root.mainloop()


