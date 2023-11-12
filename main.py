import tkinter as tk
from PIL import Image, ImageTk
import pygame

from question_set import question_multiplication_single_digit, question_addition_within_twenty

# Global counters
total_correct = 0
total_wrong = 0


def init_pygame():
    pygame.init()
    pygame.mixer.init()

def play_sound(filename):
    pygame.mixer.music.load(filename)  # Replace with the path to your sound file
    pygame.mixer.music.play()

def update_image(correct):
    global image_label
    if correct:
        image = Image.open('resource/duck_thumbup.png')
    else:
        image = Image.open('resource/duck_thumbdown.png')
    image = image.resize((600, 600), Image.ANTIALIAS)  # Resize image
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo  # Keep a reference


def check_answer(event=None):  # Added event=None to handle the keypress event
    global correct_answer, answer_entry, feedback_label, question_label
    global total_correct, total_wrong  # Global counters

    user_answer = answer_entry.get()

    if user_answer.isdigit() and int(user_answer) == correct_answer:
        feedback_text = "Correct!"
        total_correct += 1
        feedback_label.config(text=feedback_text, fg='green')
        correct_label.config(text=f"Total Correct: {total_correct}")
        update_image(correct=True)
        if total_correct % 5 == 0:
            play_sound('resource/guaguagua.wav')
        else:
            play_sound('resource/correct.wav')
    else:
        total_wrong += 1
        feedback_text = f"Incorrect. {question_label.cget('text')} = {correct_answer}."
        feedback_label.config(text=feedback_text, fg='red')
        wrong_label.config(text=f"Total Wrong: {total_wrong}")
        update_image(correct=False)
        play_sound('resource/wrong.wav')

    new_question()
    answer_entry.focus()  # Set focus back to the answer_entry widget


def new_question():
    global correct_answer, answer_entry, question_label
    question, correct_answer = generate_question()
    question_label.config(text=question)
    answer_entry.delete(0, tk.END)
    answer_entry.focus()  # Set focus to the answer_entry widget


def generate_question():
    # Call the current question set function
    return current_question_set_function()

def select_question_set(set_func):
    global current_question_set_function
    current_question_set_function = set_func
    new_question()

# Set up the main application window
root = tk.Tk()
root.title("Kids math practice")
root.geometry("600x768")  # Set the window size to 640x480

# Menu setup
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a submenu for question sets
question_set_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Question Sets", menu=question_set_menu)

# Add question sets to the submenu
question_set_menu.add_command(label="question_multiplication_single_digit", command=lambda: select_question_set(question_multiplication_single_digit))
question_set_menu.add_command(label="question_addition_within_twenty", command=lambda: select_question_set(question_addition_within_twenty))

# Default question set
current_question_set_function = question_addition_within_twenty

# Initialize the first question
initial_question, correct_answer = generate_question()

# Create a frame for the score labels and pack it to the top right
score_frame = tk.Frame(root)
score_frame.pack(side="top", anchor="ne")

question_label = tk.Label(root, text=initial_question, font=("Helvetica", 36))
question_label.pack(pady=20)

feedback_label = tk.Label(root, font=("Helvetica", 16))
feedback_label.pack(pady=5)


# Labels for correct and wrong answers inside the frame
correct_label = tk.Label(score_frame, text=f"Total Correct: {total_correct}", font=("Helvetica", 16))
correct_label.pack()

wrong_label = tk.Label(score_frame, text=f"Total Wrong: {total_wrong}", font=("Helvetica", 16))
wrong_label.pack()

answer_entry = tk.Entry(root, font=("Helvetica", 16))
answer_entry.pack(pady=10)
answer_entry.bind("<Return>", check_answer)  # Binding the Enter key to check_answer
answer_entry.bind("<KP_Enter>", check_answer)  # Binding the Numpad Enter key to check_answer
answer_entry.focus()  # Initially set focus to the answer_entry widget

image_label = tk.Label(root)
image_label.pack(pady=10)

check_button = tk.Button(root, text="Check Answer", command=check_answer, font=("Helvetica", 14))
check_button.pack(pady=10)

init_pygame()
# Start the GUI event loop
root.mainloop()