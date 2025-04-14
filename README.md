# 📚 Quiz Bowl Application

This is a Python-based Quiz Bowl application developed for the DS-3850 Business Applications course. The project integrates a GUI with a SQLite database and allows for two distinct user roles: **Administrator** (password protected) and **Quiz Taker** (open access).

---

## 🚀 Features

### 👤 Admin Interface
- Password-protected login (`admin123`)
- Add new quiz questions
- View existing questions by category
- Edit or delete questions

### 🧠 Quiz Taker Interface
- Select a category (Accounting, Marketing, Finance, Management, Economics)
- Answer multiple-choice questions
- Get immediate feedback after each question
- Final score display at the end of the quiz

---

## 🗃️ Database Structure

The app uses **SQLite** and includes 5 tables (one for each course category):
- `accounting`
- `marketing`
- `finance`
- `management`
- `economics`

Each table includes:
- `id` (Primary Key)
- `question` (Text)
- `option_a`, `option_b`, `option_c`, `option_d` (Choices)
- `correct_option` (Correct answer as "A", "B", "C", or "D")

> The database auto-populates with 10 preloaded quiz questions per subject on first run.

---

## 🛠️ How to Run

### Requirements:
- Python 3.x
- `tkinter` (comes pre-installed with Python)

### Instructions:
1. **Clone this repo** or download the source code.
2. Open the project folder in **VSCode** or your preferred IDE.
3. Run the app:
    ```bash
    python main.py
    ```

---

## 🔑 Admin Password

To access the admin panel:
```text
admin123
