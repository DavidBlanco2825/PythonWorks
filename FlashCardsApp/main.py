from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ---------------------------- DATA ------------------------------- #
try:
    data = pandas.read_csv(r".\data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(r".\data\french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ---------------------------- CARD CHANGE ------------------------------- #


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(language_text, text="French", fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(language_text, text="English", fill="white")


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(r".\data\words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file=r".\images\card_back.png")
card_front_img = PhotoImage(file=r".\images\card_front.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))  # put
language_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canvas.grid(column=0, row=0, columnspan=2)

right_button_image = PhotoImage(file=r".\images\right.png")
right_button = Button(image=right_button_image, command=is_known, highlightthickness=0, bd=0)
right_button.grid(column=1, row=1)

wrong_button_image = PhotoImage(file=r".\images\wrong.png")
wrong_button = Button(image=wrong_button_image, command=next_card, highlightthickness=0, bd=0)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()