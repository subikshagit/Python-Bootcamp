BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random
current_card = {}
#__ main code __#
data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
def known_card_func():
    to_learn.remove(current_card)
    random_word_func()
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    

def random_word_func():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="white")
    canvas.itemconfig(card_background, image=card_front_img)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)




# Placeholder text for the flashcard
current_card = random.choice(to_learn)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text=current_card["French"], font=("Ariel", 60, "bold"))

window.after(3000, func=flip_card)


# Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=random_word_func)
unknown_button.grid(row=1, column=0)
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=known_card_func)
known_button.grid(row=1, column=1)
window.mainloop()
# Note: The functionality to flip the card and load words is not yet implemented
# You can add that functionality later as needed