from tkinter import *
import pandas as pds
import random

# ---------------------------- Tool Kits ------------------------------- #
TITLE_FONT = "Daddy Rewind"
FONT = "Work sans"
COLOR = "white"
DARK = "grey15"
DURATION = 5
current_card = {}
card_flipped = False
# ---------------------------- Random Words ------------------------------- #
try:
    data = pds.read_csv("data\\learning_list\\words_to_learn_kannada.csv")
except FileNotFoundError:
    original_data = pds.read_csv("data\\kannada_words.csv")
    word_list = original_data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")


def kannada_word_gen():
    global current_card
    canvas.itemconfig(title_text, text="Kannada")
    canvas.itemconfig(card, image=front_card)
    current_card = random.choice(word_list)
    canvas.itemconfig(word, text=current_card["Kannada"])
    tick_button.grid_forget()
    cross_button.grid_forget()
    count_down()

# ---------------------------- Flip Cards ------------------------------- #


def flip_cards():
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(card, image=back_card)
    canvas.itemconfig(word, text=current_card["English"])
    tick_button.config(state="normal")
    tick_button.grid(row=2, column=2)
    cross_button.config(state="normal")
    cross_button.grid(row=2, column=1)


def remove_word():
    word_list.remove(current_card)
    save = pds.DataFrame(word_list)
    save.to_csv("data\\learning_list\\words_to_learn_kannada.csv", index=False)
    kannada_word_gen()
# ---------------------------- Counter ------------------------------- #


def count_down():
    window.after(3000, flip_cards)


# ---------------------------- Ui Setup ------------------------------- #
window = Tk()
window.config(bg=DARK, padx=25, pady=25)
window.resizable(width=False, height=False)
window.title("Flashy Cards")

count_down()

canvas = Canvas(width=400, height=400, bg=DARK, highlightthickness=0)

# ? Image path
logo = PhotoImage(file="images\\lingo.png")
back_card = PhotoImage(
    file="images\\back_card.png")
front_card = PhotoImage(
    file="images\\front_card.png")
wrong_button = PhotoImage(
    file="images\\nope.png")
tick_mark = PhotoImage(
    file="images\\yep.png")

# ? Front Card
card = canvas.create_image(200, 200, image=front_card)
canvas.grid(row=0, column=1, columnspan=2)

# ? Title Text
title_text = canvas.create_text(
    200, 70, text="Tittle", fill=COLOR, font=(TITLE_FONT, 45))
# ? Text
word = canvas.create_text(200, 215, text="word", fill=COLOR,
                          font=(FONT, 30, "italic"))

# ? Crossed Mark
cross_button = Button(image=wrong_button,
                      highlightthickness=0, width=284, height=60)
cross_button.config(border=0, background=DARK,
                    activebackground=DARK, command=kannada_word_gen)


# ? Tick Mark
tick_button = Button(image=tick_mark,
                     highlightthickness=0, width=284, height=60)
tick_button.config(border=0, background=DARK,
                   activebackground=DARK, command=remove_word)

# ? Initial boot
kannada_word_gen()

window.mainloop()
