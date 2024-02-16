from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"


class QuizInterface():

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score = Label(text="Score: 0 / 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, width=280, font=(FONT_NAME, 16, "italic"))
        self.canvas.grid(row=1, column=0, pady=20, columnspan=2)

        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_clicked)
        self.true_button.grid(row=2, column=0)
        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_clicked)
        self.false_button.grid(row=2, column=1)

        # Initialize with first question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score} / {self.quiz.question_number}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="That's the end of the quiz...")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, correct: bool):
        self.canvas.config(bg="green") if correct else self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)