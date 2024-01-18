import tkinter as tk
import random
import time

class SpeedTypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test Application")

        # Set up GUI elements
        self.root.geometry("800x600")  # Increase window size
        self.root.configure(bg='#3498db')  # Set background color

        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "A journey of a thousand miles begins with a single step.",
            "To be or not to be, that is the question.",
            "In the beginning God created the heavens and the earth.",
            "All that glitters is not gold.",
            "Where there is love, there is life."
        ]

        self.current_sentence = ""
        self.start_time = 0

        self.instruction_label = tk.Label(root, text="Type the sentence as fast as you can:", font=('Helvetica', 14), bg='#3498db', fg='#ffffff')
        self.instruction_label.pack(pady=20)

        self.sentence_label = tk.Label(root, text="", font=('Helvetica', 14), wraplength=500, justify='center', bg='#3498db', fg='#ffffff')
        self.sentence_label.pack(pady=20)

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.entry_var, font=('Helvetica', 14))
        self.entry.pack(pady=20)

        self.start_button = tk.Button(root, text="Start Typing Test", command=self.start_typing_test, font=('Helvetica', 12), bg='#2ecc71', fg='#ffffff')
        self.start_button.pack(pady=15)

        self.reset_button = tk.Button(root, text="Reset Test", command=self.restart_test, font=('Helvetica', 12), bg='#e74c3c', fg='#ffffff')
        self.reset_button.pack(pady=15)

        self.result_label = tk.Label(root, text="", font=('Helvetica', 14), bg='#3498db', fg='#ffffff')
        self.result_label.pack(pady=20)

    def start_typing_test(self):
        self.current_sentence = random.choice(self.sentences)
        self.sentence_label.config(text=self.current_sentence)
        self.start_time = time.time()
        self.entry_var.set("")
        self.entry.focus()

        self.root.bind('<Return>', self.check_typing)
        self.start_button.config(state=tk.DISABLED)

    def check_typing(self, event):
        user_input = self.entry_var.get().strip()

        correct_words = sum(a == b for a, b in zip(user_input.split(), self.current_sentence.split()))
        total_words = len(self.current_sentence.split())
        accuracy = (correct_words / total_words) * 100

        if user_input == self.current_sentence:
            elapsed_time = time.time() - self.start_time
            words_per_minute = int(total_words / (elapsed_time / 60))

            result_text = f"Good job! You typed the sentence correctly.\nWords per Minute: {words_per_minute}\nAccuracy: {accuracy:.2f}%"

            self.result_label.config(text=result_text)
            self.start_button.config(state=tk.NORMAL)
            self.root.unbind('<Return>')

        else:
            self.entry_var.set("")  # Clear the entry for the next attempt
            self.current_sentence = random.choice(self.sentences)
            self.sentence_label.config(text=self.current_sentence)

    def restart_test(self):
        self.start_button.config(state=tk.NORMAL)
        self.entry_var.set("")
        self.sentence_label.config(text="")
        self.instruction_label.config(text="Type the sentence as fast as you can:")
        self.result_label.config(text="")
        self.root.unbind('<Return>')
        self.start_button.config(state=tk.NORMAL)

# Create the main window
root = tk.Tk()
app = SpeedTypingTest(root)

# Run the main loop
root.mainloop()
