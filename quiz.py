import tkinter as tk
from tkinter import messagebox, ttk
from db_manager import DBManager
from question import Question
import random

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Bowl")
        self.db = DBManager()
        self.score = 0
        self.current_index = 0
        self.start_screen()

    def start_screen(self):
        tk.Label(self.master, text="Welcome to the Quiz Bowl", font=("Arial", 16)).pack()
        self.category_var = tk.StringVar()
        self.category_var.set("accounting")
        categories = ["accounting", "marketing", "finance", "management", "economics"]
        ttk.Combobox(self.master, values=categories, textvariable=self.category_var).pack()

        tk.Button(self.master, text="Start Quiz", command=self.load_questions).pack()

    def load_questions(self):
        self.questions_raw = self.db.get_questions(self.category_var.get())
        random.shuffle(self.questions_raw)
        self.questions = [
            Question(q[1], {'A': q[2], 'B': q[3], 'C': q[4], 'D': q[5]}, q[6])
            for q in self.questions_raw
        ]
        self.score = 0
        self.current_index = 0
        self.show_question()

    def show_question(self):
        self.clear_frame()
        if self.current_index >= len(self.questions):
            self.display_score()
            return

        q = self.questions[self.current_index]
        tk.Label(self.master, text=q.question_text, wraplength=400).pack()

        self.answer_var = tk.StringVar()
        for key, val in q.options.items():
            tk.Radiobutton(self.master, text=f"{key}: {val}", variable=self.answer_var, value=key).pack(anchor='w')

        tk.Button(self.master, text="Submit", command=self.check_answer).pack()

    def check_answer(self):
        selected = self.answer_var.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an answer.")
            return

        if self.questions[self.current_index].is_correct(selected):
            self.score += 1
            messagebox.showinfo("Correct!", "Great job!")
        else:
            messagebox.showinfo("Incorrect", f"The correct answer was: {self.questions[self.current_index].correct_option}")

        self.current_index += 1
        self.show_question()

    def display_score(self):
        self.clear_frame()
        tk.Label(self.master, text=f"Quiz Completed!", font=("Arial", 16)).pack()
        tk.Label(self.master, text=f"Your score: {self.score} / {len(self.questions)}").pack()

    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()
