THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR,fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="#FFFFFF")
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.question_text = self.canvas.create_text(150,125, width=280,text="question_text", font=("Arial",20,"italic"))
        self.right_img = PhotoImage(file="images/false.png")
        self.wrong_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_img, highlightthickness=0, command= self.right_pressed)
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, command= self.wrong_pressed)
        self.right_button.grid(row=2,column=0)
        self.wrong_button.grid(row=2,column=1)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text=f"Total Score: {self.quiz.score}")
    def right_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)
