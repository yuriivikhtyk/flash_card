from tkinter import * 
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    words_data = pd.read_csv('data/words_to_learn.csv')
    start_dict = pd.DataFrame.to_dict(words_data)
    french_words = words_data.French.to_list()
    english_words = words_data.English.to_list()
    words_dict = {}
    words_to_learn = {'French':{},'English':{}}
    for i in range(len(french_words)):
        words_dict[french_words[i]] = english_words[i]

except FileNotFoundError:
    words_data = pd.read_csv('data/french_words.csv')
    start_dict = pd.DataFrame.to_dict(words_data)
    french_words = words_data.French.to_list()
    english_words = words_data.English.to_list()
    words_dict = {}
    words_to_learn = {'French':{},'English':{}}
    for i in range(len(french_words)):
        words_dict[french_words[i]] = english_words[i]

except pd.errors.EmptyDataError:
    words_data = pd.read_csv('data/french_words.csv')
    start_dict = pd.DataFrame.to_dict(words_data)
    french_words = words_data.French.to_list()
    english_words = words_data.English.to_list()
    words_dict = {}
    words_to_learn = {'French':{},'English':{}}
    for i in range(len(french_words)):
        words_dict[french_words[i]] = english_words[i]

#print(words_dict)

DISPLAY_WORD = random.choice(french_words)

def right():
    global french_words, words_dict
    del words_dict[DISPLAY_WORD]
    french_words.remove(DISPLAY_WORD)
    count = 1
    for k,v in words_dict.items():
        words_to_learn["French"][count] = k
        words_to_learn["English"][count] = v
        count = count + 1
    df = pd.DataFrame.from_dict(words_to_learn)
    df.to_csv('data/words_to_learn.csv', index=False)
    back_flip()


def wrong():
    back_flip()
    



canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
language = canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 253, text=DISPLAY_WORD, fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=1,row=1, columnspan=2)


right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_btn = Button(image=right_img, highlightthickness=0, command=right)
right_btn.grid(column=2, row=2)
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=wrong)
wrong_btn.grid(column=1, row=2)


def flip():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(word, text=words_dict[DISPLAY_WORD], fill="white")
    canvas.itemconfig(language, text="English", fill="white")


def back_flip():
    global DISPLAY_WORD, flip_time
    DISPLAY_WORD = random.choice(french_words)
    window.after_cancel(flip_time)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(word, text=DISPLAY_WORD, fill="black")
    canvas.itemconfig(language, text="French", fill="black")
    flip_time = window.after(3000, flip)


flip_time = window.after(3000, flip)


window.mainloop()


