import tkinter as tk
from admin import AdminInterface
from quiz import QuizApp

STYLES = {
    "bg": "#f0f4f8",
    "title_font": ("Arial", 20, "bold"),
    "button_font": ("Arial", 12),
    "label_font": ("Arial", 14)
}

def return_to_main(root):
    for widget in root.winfo_children():
        widget.destroy()
    main_menu(root)

def main_menu(root):
    root.configure(bg=STYLES["bg"])
    for widget in root.winfo_children():
        widget.destroy()

    frame = tk.Frame(root, bg=STYLES["bg"], padx=20, pady=40)
    frame.pack(expand=True)

    tk.Label(frame, text="🎓 Quiz Bowl", font=STYLES["title_font"], bg=STYLES["bg"]).pack(pady=30)

    tk.Button(frame, text="Admin Login", font=STYLES["button_font"], width=20,
              command=lambda: open_admin(root)).pack(pady=10)

    tk.Button(frame, text="Take a Quiz", font=STYLES["button_font"], width=20,
              command=lambda: open_quiz(root)).pack(pady=10)

def open_admin(root):
    for widget in root.winfo_children():
        widget.destroy()
    AdminInterface(root)

def open_quiz(root):
    for widget in root.winfo_children():
        widget.destroy()
    QuizApp(root)

def main():
    root = tk.Tk()
    root.title("Quiz Bowl")
    root.geometry("550x500")
    main_menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
