import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Responsive Quiz App")
        self.root.configure(bg="#f0f8ff")

        # Minimum window size
        self.root.minsize(600, 400)

        # Expand main frame with window resize
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        # Quiz questions (10 Aptitude MCQs)
        self.questions = [
            {
                "question": "What is the value of (144 ÷ 12) × (15 ÷ 5)?",
                "options": ["A) 12", "B) 24", "C) 18", "D) 36"],
                "answer": "D"
            },
            {
                "question": "A student scored 480 marks out of 600. What is the percentage?",
                "options": ["A) 75%", "B) 80%", "C) 85%", "D) 90%"],
                "answer": "B"
            },
            {
                "question": "The ratio of ages of A and B is 3:5. If A is 15 years old, what is the age of B?",
                "options": ["A) 20", "B) 22", "C) 25", "D) 30"],
                "answer": "C"
            },
            {
                "question": "A dice is rolled once. What is the probability of getting an even number?",
                "options": ["A) 1/2", "B) 1/3", "C) 1/6", "D) 2/3"],
                "answer": "A"
            },
            {
                "question": "A can complete a piece of work in 10 days and B in 15 days. If both work together, how many days will they take?",
                "options": ["A) 5 days", "B) 6 days", "C) 7 days", "D) 8 days"],
                "answer": "B"
            },
            {
                "question": "A car covers 180 km in 3 hours. What is its average speed?",
                "options": ["A) 40 km/h", "B) 50 km/h", "C) 60 km/h", "D) 70 km/h"],
                "answer": "C"
            },
            {
                "question": "The simple interest on ₹5000 for 2 years at 10% per annum is:",
                "options": ["A) ₹500", "B) ₹750", "C) ₹1000", "D) ₹1200"],
                "answer": "C"
            },
            {
                "question": "A shopkeeper buys an item for ₹800 and sells it for ₹1000. What is the profit percentage?",
                "options": ["A) 20%", "B) 22.5%", "C) 25%", "D) 30%"],
                "answer": "C"
            },
            {
                "question": "Find the next number: 2, 6, 12, 20, 30, ?",
                "options": ["A) 36", "B) 40", "C) 42", "D) 44"],
                "answer": "C"
            },
            {
                "question": "If ALL = 38, THEN = 58, what will BALL equal?",
                "options": ["A) 50", "B) 52", "C) 54", "D) 56"],
                "answer": "B"
            }
        ]

        self.current_question = 0
        self.score = 0
        self.user_answers = []

        self.setup_ui()
        self.show_question()

        # Bind resize event
        self.root.bind("<Configure>", self.on_resize)

    def setup_ui(self):
        # Main frame
        self.main_frame = tk.Frame(self.root, bg="#f0f8ff", padx=20, pady=20)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        self.main_frame.rowconfigure(1, weight=1)
        self.main_frame.columnconfigure(0, weight=1)

        # Question Label
        self.question_label = tk.Label(
            self.main_frame, 
            text="", 
            font=("Arial", 18, "bold"), 
            bg="#f0f8ff", 
            wraplength=700, 
            justify="left"
        )
        self.question_label.grid(row=0, column=0, pady=(0, 20), sticky="w")

        self.selected_option = tk.StringVar()

        # Options Frame
        self.options_frame = tk.Frame(self.main_frame, bg="#f0f8ff")
        self.options_frame.grid(row=1, column=0, sticky="nsew")

        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(
                self.options_frame,
                text="", 
                variable=self.selected_option, 
                value=chr(65 + i), 
                font=("Arial", 14), 
                bg="#f0f8ff", 
                anchor="w", 
                justify="left", 
                padx=10, 
                pady=5
            )
            rb.pack(fill="x", pady=5)
            self.option_buttons.append(rb)

        # Navigation Button
        self.next_button = tk.Button(
            self.main_frame, 
            text="Next →", 
            font=("Arial", 16), 
            bg="#4682B4", 
            fg="white", 
            activebackground="#5a9bd3",
            relief="raised",
            padx=10, 
            pady=5,
            command=self.next_question
        )
        self.next_button.grid(row=2, column=0, pady=20, sticky="e")

    def show_question(self):
        q_data = self.questions[self.current_question]
        self.question_label.config(
            text=f"Q{self.current_question+1}: {q_data['question']}"
        )
        for i, option_text in enumerate(q_data["options"]):
            self.option_buttons[i].config(text=option_text)
        self.selected_option.set("")  # Reset radio buttons

    def next_question(self):
        selected = self.selected_option.get()
        if not selected:
            messagebox.showwarning("No selection", "Please select an option before proceeding.")
            return

        correct_answer = self.questions[self.current_question]["answer"]
        if selected == correct_answer:
            self.score += 1

        self.user_answers.append(selected)
        self.current_question += 1

        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_result_page()

    def show_result_page(self):
        # Clear frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        total_qs = len(self.questions)
        percentage = (self.score / total_qs) * 100

        # Performance message
        if percentage >= 80:
            performance = "🌟 Excellent Work!"
            color = "green"
        elif percentage >= 50:
            performance = "👍 Good Job!"
            color = "blue"
        else:
            performance = "😅 Needs Improvement"
            color = "red"

        # Title
        result_label = tk.Label(
            self.main_frame,
            text=f"🎉 Quiz Completed!\nYour Score: {self.score}/{total_qs} ({percentage:.1f}%)",
            font=("Arial", 20, "bold"),
            bg="#f0f8ff",
            fg="#2e8b57"
        )
        result_label.pack(pady=20)

        perf_label = tk.Label(
            self.main_frame,
            text=performance,
            font=("Arial", 18, "bold"),
            bg="#f0f8ff",
            fg=color
        )
        perf_label.pack(pady=(0, 20))

        # Results list
        result_frame = tk.Frame(self.main_frame, bg="#f0f8ff")
        result_frame.pack(fill="both", expand=True)

        for i, q in enumerate(self.questions):
            user_ans = self.user_answers[i]
            correct_ans = q["answer"]

            if user_ans == correct_ans:
                text = f"Q{i+1}: Correct ✅ ({user_ans})"
                fg = "green"
            else:
                text = f"Q{i+1}: Wrong ❌ (Your: {user_ans}, Correct: {correct_ans})"
                fg = "red"

            lbl = tk.Label(
                result_frame,
                text=text,
                font=("Arial", 14),
                bg="#f0f8ff",
                fg=fg,
                anchor="w",
                justify="left"
            )
            lbl.pack(fill="x", padx=10, pady=2)

        # Restart Button
        restart_btn = tk.Button(
            self.main_frame,
            text="🔄 Restart Quiz",
            font=("Arial", 16),
            bg="#4682B4",
            fg="white",
            activebackground="#5a9bd3",
            relief="raised",
            padx=10,
            pady=5,
            command=self.restart_quiz
        )
        restart_btn.pack(pady=20)

    def restart_quiz(self):
        self.current_question = 0
        self.score = 0
        self.user_answers.clear()
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.setup_ui()
        self.show_question()

    def on_resize(self, event):
        new_width = max(event.width - 80, 300)
        self.question_label.config(wraplength=new_width)


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
