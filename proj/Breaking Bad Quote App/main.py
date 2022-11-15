import tkinter as tk
import requests
import os

CWD = os.getcwd()
QUOTE_BUBBLE_IMG_PATH = f"{CWD}\\images\\QuoteBubble.png"
WALTER_IMG_PATH = f"{CWD}\\images\\Walter.png"
JESSE_IMG_PATH = f"{CWD}\\images\\Jesse.png"
SAUL_IMG_PATH = f"{CWD}\\images\\Saul.png"
HANK_IMG_PATH = f"{CWD}\\images\\Hank.png"
GUSTAVO_IMG_PATH = f"{CWD}\\images\\Gustavo.png"
MIKE_IMG_PATH = f"{CWD}\\images\\Mike.png"
SKYLER_IMG_PATH = f"{CWD}\\images\\Skyler.png"
WALTER_JR_IMG_PATH = f"{CWD}\\images\\WaltJr.png"
DEFAULT_IMG_PATH = f"{CWD}\\images\\Default.png"
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
SCREEN_LOCATIONS = {
    "top_left" : (0, 0),
    "top-mid" : (SCREEN_WIDTH/2, 0),
    "top_right" : (SCREEN_WIDTH, 0),
    "center-left" : (0,SCREEN_HEIGHT/2),
    "center" : (SCREEN_WIDTH/2, SCREEN_HEIGHT/2),
    "center-right" : (SCREEN_WIDTH,  SCREEN_HEIGHT/2),
    "bot_left" : (0, SCREEN_HEIGHT),
    "bot_mid" : (SCREEN_WIDTH/2, SCREEN_HEIGHT),
    "bot_right" : (SCREEN_WIDTH, SCREEN_HEIGHT)
}
URL = "https://api.breakingbadquotes.xyz/v1/quotes"
QUOTE_FONT = ("Calibri", 12, "italic")

class BreakingBadQuotes(tk.Tk):
    
    author_options = {
        "Jesse Pinkman" : JESSE_IMG_PATH,
        "Saul Goodman" : SAUL_IMG_PATH,
        "Walter White" : WALTER_IMG_PATH,
        "Mike Ehrmantraut" : MIKE_IMG_PATH,
        "Gustavo Fring" : GUSTAVO_IMG_PATH,
        "Hank Schrader" : HANK_IMG_PATH,
        "Skyler White" : SKYLER_IMG_PATH,
        "Walter White Jr" : WALTER_JR_IMG_PATH
    }
    
    def __init__(self):
        super().__init__()
        # Initialisation
        self.quote = ""
        self.author = ""
        # Setup
        self.setup_window()
        self.setup_canvas()
    
    def setup_window(self):
        """ Sets up and initialises the main window """
        self.title("Breaking Bad Quotes")
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

    def setup_canvas(self):
        """ Sets up and initialises the main canvas """    
        self.main_canvas = tk.Canvas(master=self, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg="white")
        
        self.quote_bubble_img = tk.PhotoImage(file=QUOTE_BUBBLE_IMG_PATH)
        self.main_canvas.create_image((150,200), image=self.quote_bubble_img)

        self.quote_text = self.main_canvas.create_text((150, 150), text='', font=QUOTE_FONT, justify=tk.CENTER, width=200)
        
        self.author_img = tk.PhotoImage(file='')
        self.quote_button = tk.Button(master=self.main_canvas, image=self.author_img, bg="white", border=0, command=self.updates_quotes)
        self.quote_window = self.main_canvas.create_window((150,500), window=self.quote_button)

        self.updates_quotes()
                
        self.main_canvas.grid(row=0, column=0)        
    
    def updates_quotes(self):
        """ Retrieves a new quote and changes the GUI accordingly """
        self.get_random_quote()
        self.change_quote_text()
        self.change_quote_button()
    
    def change_quote_button(self):
        """ Changes the quote button widget to the current quotes corresponding author """
        self.author_img.config(file=self.author_options.get(self.author, DEFAULT_IMG_PATH))
        self.main_canvas.itemconfig(self.quote_window, window=self.quote_button)
        
    def change_quote_text(self):
        """ Changes the quote text widget to the current stored quote """
        print(len(self.quote))

        if len(self.quote) > 300:
            new_font = ("Calibri", 6, "italic")
        elif len(self.quote) > 200:
            new_font = ("Calibri", 8, "italic")
        elif len(self.quote) > 100:
            new_font = ("Calibri", 10, "italic")
        else:
            new_font = QUOTE_FONT

        self.main_canvas.itemconfig(self.quote_text, font=new_font,text=self.quote)
    
    def get_random_quote(self):
        """ Requests and saved a random quote from the Breaking Bad API """
        response = requests.get(URL)
        data = response.json()[0]
        self.quote = data['quote']
        self.author = data['author']
        
if __name__ == "__main__":
    app = BreakingBadQuotes()
    app.mainloop()