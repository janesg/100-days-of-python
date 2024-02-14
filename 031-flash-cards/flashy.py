from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

# Use the 'words to learn' list if it exists
try:
    words_dict_list = pandas.read_csv("./data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    words_dict_list = pandas.read_csv("./data/spanish_words.csv").to_dict(orient="records")

print(f"Number of words to learn: {len(words_dict_list)}")
current_card = None
flip_timer = None

def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(language, text=list(current_card.keys())[1], fill="white")
    canvas.itemconfig(word, text=list(current_card.values())[1], fill="white")


def next_card():
    global current_card, flip_timer
    if flip_timer is not None:
        win.after_cancel(flip_timer)
    flip_timer = win.after(3000, func=flip_card)
    current_card = words_dict_list[random.randint(0, len(words_dict_list) - 1)]
    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(language, text=list(current_card.keys())[0], fill="black")
    canvas.itemconfig(word, text=list(current_card.values())[0], fill="black")


def correct_clicked():
    # Remove current_card from list & save the updated list to 'words_to_learn' file
    words_dict_list.remove(current_card)
    to_learn_df = pandas.DataFrame(words_dict_list)
    to_learn_df.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


win = Tk()
win.title("Flashy McFlash")
win.config(padx=50, pady=50, background=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
# canvas.create_image(400, 263, image=card_front_img)
card_image = canvas.create_image(400, 263)
# Note: x & y are positional arguments; *args
language = canvas.create_text(400, 150, text="Language", font=(FONT_NAME, 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
wrong_img = PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong.grid(row=1, column=0)
right_img = PhotoImage(file="./images/right.png")
correct = Button(image=right_img, highlightthickness=0, command=correct_clicked)
correct.grid(row=1, column=1)

next_card()

win.mainloop()
