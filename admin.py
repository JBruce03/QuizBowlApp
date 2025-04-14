import tkinter as tk
from tkinter import messagebox, ttk
from db_manager import DBManager

ADMIN_PASSWORD = 'admin123'  # You can change this password

class AdminInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Admin Login")
        self.db = DBManager()
        self.login_screen()

    def login_screen(self):
        self.clear_frame()
        tk.Label(self.master, text="Enter Admin Password:").pack(pady=10)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()
        tk.Button(self.master, text="Login", command=self.check_password).pack(pady=10)

    def check_password(self):
        if self.password_entry.get() == ADMIN_PASSWORD:
            self.open_admin_panel()
        else:
            messagebox.showerror("Error", "Incorrect password")

    def open_admin_panel(self):
        self.clear_frame()
        tk.Label(self.master, text="Admin Panel", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.master, text="Add Question", width=20, command=self.add_question_form).pack(pady=5)
        tk.Button(self.master, text="View/Edit/Delete Questions", width=20, command=self.view_questions).pack(pady=5)

    def add_question_form(self):
        self.clear_frame()
        tk.Label(self.master, text="Add New Question", font=("Arial", 14)).pack(pady=10)

        self.category_var = tk.StringVar()
        self.category_var.set("accounting")
        categories = ["accounting", "marketing", "finance", "management", "economics"]
        ttk.Combobox(self.master, values=categories, textvariable=self.category_var).pack(pady=5)

        self.q_entry = tk.Entry(self.master, width=60)
        tk.Label(self.master, text="Question:").pack()
        self.q_entry.pack()

        self.options = {}
        for opt in ['A', 'B', 'C', 'D']:
            tk.Label(self.master, text=f"Option {opt}:").pack()
            self.options[opt] = tk.Entry(self.master, width=60)
            self.options[opt].pack()

        tk.Label(self.master, text="Correct Option (A/B/C/D):").pack()
        self.correct_entry = tk.Entry(self.master)
        self.correct_entry.pack(pady=5)

        tk.Button(self.master, text="Submit", command=self.submit_question).pack(pady=10)
        tk.Button(self.master, text="Back", command=self.open_admin_panel).pack()

    def submit_question(self):
        course = self.category_var.get()
        q = self.q_entry.get()
        a, b, c, d = [self.options[o].get() for o in ['A', 'B', 'C', 'D']]
        correct = self.correct_entry.get().upper()

        if correct not in ['A', 'B', 'C', 'D']:
            messagebox.showerror("Error", "Correct answer must be A, B, C, or D.")
            return

        if not all([q, a, b, c, d, correct]):
            messagebox.showerror("Error", "All fields must be filled.")
            return

        self.db.add_question(course, (q, a, b, c, d, correct))
        messagebox.showinfo("Success", "Question added!")

        self.q_entry.delete(0, tk.END)
        self.correct_entry.delete(0, tk.END)
        for entry in self.options.values():
            entry.delete(0, tk.END)

    def view_questions(self):
        self.clear_frame()
        tk.Label(self.master, text="View/Edit/Delete Questions", font=("Arial", 14)).pack(pady=10)

        self.category_var = tk.StringVar()
        self.category_var.set("accounting")
        categories = ["accounting", "marketing", "finance", "management", "economics"]
        ttk.Combobox(self.master, values=categories, textvariable=self.category_var).pack()

        tk.Button(self.master, text="Load Questions", command=self.load_questions_list).pack(pady=10)
        tk.Button(self.master, text="Back", command=self.open_admin_panel).pack()

    def load_questions_list(self):
        self.clear_frame()
        tk.Label(self.master, text="Questions", font=("Arial", 14)).pack(pady=10)

        course = self.category_var.get()
        questions = self.db.get_questions(course)

        for q in questions:
            frame = tk.Frame(self.master, bd=1, relief="solid", padx=10, pady=5)
            frame.pack(fill="x", padx=10, pady=5)

            q_text = f"Q: {q[1]}"
            tk.Label(frame, text=q_text, wraplength=400, justify="left").pack(anchor="w")

            tk.Button(frame, text="Edit", command=lambda q=q: self.edit_question(course, q)).pack(side="left", padx=5)
            tk.Button(frame, text="Delete", command=lambda q=q: self.delete_question(course, q[0])).pack(side="left")

        tk.Button(self.master, text="Back", command=self.view_questions).pack(pady=10)

    def edit_question(self, course, question):
        self.clear_frame()
        tk.Label(self.master, text="Edit Question", font=("Arial", 14)).pack(pady=10)

        self.q_entry = tk.Entry(self.master, width=60)
        self.q_entry.insert(0, question[1])
        tk.Label(self.master, text="Question:").pack()
        self.q_entry.pack()

        self.options = {}
        labels = ['A', 'B', 'C', 'D']
        for i, opt in enumerate(labels, 2):
            tk.Label(self.master, text=f"Option {opt}:").pack()
            self.options[opt] = tk.Entry(self.master, width=60)
            self.options[opt].insert(0, question[i])
            self.options[opt].pack()

        self.correct_entry = tk.Entry(self.master)
        self.correct_entry.insert(0, question[6])
        tk.Label(self.master, text="Correct Option (A/B/C/D):").pack()
        self.correct_entry.pack()

        tk.Button(self.master, text="Save Changes",
                  command=lambda: self.save_edited_question(course, question[0])).pack(pady=10)
        tk.Button(self.master, text="Cancel", command=self.view_questions).pack()

    def save_edited_question(self, course, question_id):
        q = self.q_entry.get()
        a, b, c, d = [self.options[o].get() for o in ['A', 'B', 'C', 'D']]
        correct = self.correct_entry.get().upper()

        if correct not in ['A', 'B', 'C', 'D']:
            messagebox.showerror("Error", "Correct answer must be A, B, C, or D.")
            return

        if not all([q, a, b, c, d, correct]):
            messagebox.showerror("Error", "All fields must be filled.")
            return

        self.db.update_question(course, question_id, (q, a, b, c, d, correct))
        messagebox.showinfo("Success", "Question updated!")
        self.view_questions()

    def delete_question(self, course, question_id):
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this question?"):
            self.db.delete_question(course, question_id)
            messagebox.showinfo("Deleted", "Question deleted.")
            self.view_questions()

    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()


print(AdminInterface)