import tkinter as tk
import random
import time
from tkinter import messagebox

class TypingSpeedTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")
        self.root.geometry("400x200")

        self.sentences = [
            "The quick brown fox jumps over the lazy dog",
            "Python is a versatile programming language",
            "Practice makes perfect",
            "Coding is fun and rewarding",
            "Keep calm and code on",
            "Programming is like solving puzzles",
            "Technology changes the world",
            "Innovation drives progress"
        ]
        self.current_sentence = ""
        self.user_input = ""

        self.typing_sentence_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.typing_sentence_label.pack(pady=10)

        self.user_input_entry = tk.Entry(self.root, font=("Arial", 12))
        self.user_input_entry.pack(pady=5)

        self.start_button = tk.Button(self.root, text="Start Typing Test", command=self.start_typing_test)
        self.start_button.pack(pady=5)

    def start_typing_test(self):
        self.current_sentence = random.choice(self.sentences)
        self.typing_sentence_label.config(text=self.current_sentence)

        self.user_input_entry.delete(0, tk.END)
        self.user_input_entry.focus()

        self.root.bind("<Return>", self.check_input)

        self.start_time = time.time()

    def check_input(self, event):
        self.user_input = self.user_input_entry.get()
        self.end_time = time.time()
        time_taken = self.end_time - self.start_time
        words_per_minute = len(self.user_input.split()) / (time_taken / 60)

        if self.user_input == self.current_sentence:
            result_message = f"Correct! Your typing speed: {words_per_minute:.2f} words per minute."
        else:
            result_message = "Incorrect! Please try again."

        tk.messagebox.showinfo("Typing Test Result", result_message)

        self.root.unbind("<Return>")
        self.typing_sentence_label.config(text="")
        self.user_input_entry.delete(0, tk.END)


root = tk.Tk()
app = TypingSpeedTester(root)
root.mainloop()
