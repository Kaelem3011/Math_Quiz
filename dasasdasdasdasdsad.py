from tkinter import *
from functools import partial  # To prevent unwanted windows
import random

class Start:
    def __init__(self, error=""):
        # Heading frame
        self.start_frame = Frame(padx=40, pady=15)
        self.start_frame.grid()

        # Heading label
        self.heading_label = Label(self.start_frame, font='arial 15', text="Math game")
        self.heading_label.grid(row=0)

        # Hidden error label
        self.error_label = Label(self.start_frame, text="", font='arial 12', fg='red', wraplength=150)
        self.error_label.grid()

        if error != "":
            self.error_label.config(text=error)

        # Menu frame
        self.menu_frame = Frame(padx=10)
        self.menu_frame.grid()

        # Instruction Label
        self.instruction_label = Label(self.menu_frame, font='arial 12', text="Enter a minimum (left) and maximum (right) number", wraplength=140)
        self.instruction_label.grid(row=1, column=0)

        # Min Entry 
        self.min_entry = Entry(self.menu_frame, width=4, font='arial 14')
        self.min_entry.grid(row=2, column=0)

        # Max Entry 
        self.max_entry = Entry(self.menu_frame, font='arial 14', width=4)
        self.max_entry.grid(row=2, column=1)

        # Buttons frame
        self.buttons_frame = Frame(padx=5, pady=5)
        self.buttons_frame.grid()

        # Play button 
        self.play_button = Button(self.buttons_frame, font='arial 12 bold', text="Play", padx=10, command=lambda:Start.error_checking(self))
        self.play_button.grid(row=4, pady=5, sticky="ew")

        # Help button 
        self.help_button = Button(self.buttons_frame, font='arial 12 bold', text="Help", padx=5)
        self.help_button.grid(row=6, pady=20)


    def error_checking(self):
        try:
            # Sets the minimum value and maximum value
            min = self.min_entry.get()
            max = self.max_entry.get()
            # Checks if the entry is blank. If it is, the user will get an error.
            if min == "" or max == "":
                self.error_label.config(text="Entry is blank")
                return

            min = int(min)
            max = int(max)
            # Checks if user has entered a min number higher than 0.
            if min <= 0:
                self.error_label.config(text="Enter a number higher than 0.")
                return
            # Checks if minimum number is higher than max number. If it is then print an error
            if min > max:
                self.error_label.config(text="Minimum is higher than max, please enter a lower number")
                return
            # If there are no problems, the error label will hide itself
            else:
                self.error_label.config(text="")
            Game(int(self.min_entry.get()), int(self.max_entry.get()))

        except ValueError:
            self.error_label.config(text="Please enter a valid number.")
        
        
class Game:
    def __init__(self, min, max):
        # Creates new window
        self.Game_box = Toplevel()

        self.eqn_ans = IntVar()

        # Top frame
        self.Modes_frame = Frame(self.Game_box)
        self.Modes_frame.grid(padx=30, pady=20)

        # Heading label 
        self.heading_label = Label(self.Modes_frame, text="Math quiz", font='arial 24')
        self.heading_label.grid(row=0)

        
        # Error label 
        self.error_label = Label(self.Modes_frame, text="", font='arial 13', fg="red", wraplength=150)
        self.error_label.grid(row=1)

        # Question label
        self.question_label = Label(self.Modes_frame, text="Question here", font='arial 15')
        self.question_label.grid(row=2)

        # Answer label
        self.answer_label = Label(self.Modes_frame, text="", font='arial 12 bold')
        self.answer_label.grid(row=3)

        # Answer entry 
        self.answer_entry = Entry(self.Modes_frame, width=13)
        self.answer_entry.grid(row=4)

        # Buttons frame
        self.buttons_frame = Frame(self.Game_box)
        self.buttons_frame.grid(padx=5, pady=5)
    
        # Enter button
        self.enter_button = Button(self.buttons_frame, text="Enter", font='arial 12', command=lambda:Game.error_checking(self, self.answer_entry.get(), self.eqn_ans.get()))
        self.enter_button.grid(row=0, column=0, padx=5)

        # Next button
        self.next_button = Button(self.buttons_frame, text="Next", font='arial 12', padx=10, command=lambda:Game.generate(self, min, max))
        self.next_button.config(state=DISABLED)
        self.next_button.grid(row=0, column=1)
        
        Game.generate(self, min, max)


    def change(self, question):
        self.question_label.config(text=question)
        self.answer_label.config(text="")

    def generate(self, min, max):
        # Generate two numbers within range.
        a = random.randint(min, max)
        b = random.randint(min, max)
        question = "{} {} {} =".format(a, "+", b)
        answer = question[:-1]
        
        answer = eval(answer)
        self.eqn_ans.set(answer)
        self.answer_entry.config(state=NORMAL)
        self.answer_entry.delete(0, 'end')
        self.next_button.config(state=DISABLED)
        Game.change(self, question)
            

    # Check if users response to question is valid, then checks if it is correct or incorrect.
    def error_checking(self, response, answer):
        try:
            # Checks if response is blank.
            if str(response) == "":
                self.error_label.config(text="Please enter a number.")
                return

            self.error_label.config(text="")
            # Checks if users response(answer) is equal to the program answer.
            if int(response) == self.eqn_ans.get():
                # If it is, answer label will change to -
                self.answer_label.config(text="Correct", fg='green')
            else:
                self.answer_label.config(text="Incorrect", fg='red')
            self.next_button.config(state=NORMAL)
        except ValueError:
            self.error_label.config(text="Please enter a valid number.")
            raise
        

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math")
    something = Start()
    root.mainloop()