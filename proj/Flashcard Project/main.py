import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
BACK_CARD_COLOR = "#91c2af"

class App(tk.Tk):
    
    current_rand_word = ""
    is_flipped = False
        
    def __init__(self):
        super().__init__()
        self.import_data()
        
        self.title("Flashy")
        self.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        # Canvas
        self.canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.card_back_img = tk.PhotoImage(master=self.canvas, file="images/card_back.png")
        self.card_front_img = tk.PhotoImage(master=self.canvas, file="images/card_front.png")
        self.card_image = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.card_title = self.canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
        self.card_text = self.canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

        # Buttons
        self.cross_image = tk.PhotoImage(file="images/wrong.png")
        self.review_button = tk.Button(image=self.cross_image, highlightthickness=0, borderwidth=0, command=self.next_card)

        self.tick_image = tk.PhotoImage(file="images/right.png")
        self.correct_button = tk.Button(image=self.tick_image, highlightthickness=0, borderwidth=0, command=self.remove_card)

        self.arrow_image = tk.PhotoImage(file="images/black_arrow.png")
        self.flip_button = tk.Button(image=self.arrow_image, highlightthickness=0, borderwidth=0, bg="white", command=self.flip_card)

        self.layout_ui()

        self.next_card()
        
    def layout_ui(self):
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.review_button.grid(row=1, column=0)
        self.correct_button.grid(row=1, column=1)
        self.flip_button.grid(row=0, column=1, sticky=tk.S, pady=40)

    def import_data(self):
        try:
            word_data = pd.read_csv("data/words_to_review.csv")
        except FileNotFoundError:
            word_data = pd.read_csv("data/french_words.csv")
        self.word_list = [item for item in zip(word_data['French'], word_data['English'])]

        if len(self.word_list) <= 1:
            word_data = pd.read_csv("data/french_words.csv")
            self.word_list = [item for item in zip(word_data['French'], word_data['English'])]

    def remove_card(self):
        self.word_list.remove(self.current_rand_word)        
        
        data = pd.DataFrame(self.word_list, columns = ['French', 'English'])
        data.to_csv("data/words_to_review.csv")
        
        self.next_card()

    def next_card(self):
        self.current_rand_word = random.choice(self.word_list)

        self.canvas.itemconfigure(self.card_title, text="French")
        self.canvas.itemconfigure(self.card_text, text=self.current_rand_word[0])
        
        self.is_flipped = False
        self.flip_card()

    def flip_card(self):
        if self.is_flipped == True:
            self.canvas.itemconfigure(self.card_title, text="English", fill="white")
            self.canvas.itemconfigure(self.card_text, text=self.current_rand_word[1], fill="white")
            
            self.canvas.itemconfig(self.card_image, image=self.card_back_img)
            self.flip_button.config(bg=BACK_CARD_COLOR)
            self.is_flipped = False
        else:
            self.canvas.itemconfigure(self.card_title, text="French", fill="black")
            self.canvas.itemconfigure(self.card_text, text=self.current_rand_word[0], fill="black")
            
            self.canvas.itemconfig(self.card_image, image=self.card_front_img)
            self.flip_button.config(bg="white")
            self.is_flipped = True
    
if __name__ == "__main__":
    app = App()
    app.mainloop()