from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        
        
        # Score Label:
        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        
        # True Image:
        true_img = PhotoImage(file='true.png')
        self.true = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true.grid(row=2, column=0)
        
        
        # False Image:
        false_img = PhotoImage(file='false.png')
        self.false = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false.grid(row=2, column=1)
        
        
        # Canvas:
        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=260,
            text='Something',
            fill=THEME_COLOR,
            font=('Ariel', 16, 'italic')
            )
        self.canvas.config(bg='white', highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        self.get_next_question()
        
        self.window.mainloop()
        
        
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label['text'] = f"Score: {self.quiz.score}"
            q_text =self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.true.config(state='disabled')
            self.false.config(state='disabled')
            self.canvas.itemconfig(self.question_text, text=f"Your Score is {self.quiz.score}")
        
    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)
    
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)