import tkinter as tk
from tkinter import messagebox
import random
import json

class PasswordManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.setup_canvas()
        self.setup_widgets()

    def setup_window(self):
        """ Initialises The Tkinter Window """
        self.title("Password Manager")
        self.config(padx=100, pady=75, bg="white")
    
    def setup_canvas(self):
        """ Sets up the main canvas """
        self.canvas = tk.Canvas(width=200, height=189, highlightthickness=0, bg="white")
        self.logo = tk.PhotoImage(master=self.canvas, file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo)
        self.canvas.grid(row=0,column=1, sticky=tk.NW)

    def setup_widgets(self):
        """ Calls all widget setups """
        self.setup_website_widget()
        self.setup_email_widget()
        self.setup_password_widget()
        self.setup_account_widgets()   
        
    def setup_website_widget(self):
        """ Sets up the website widget """
        self.website_label = tk.Label(text="Website: ", bg="white")
        self.website_entry = tk.Entry(width=50, bg="white")
        self.website_entry.focus()
        self.website_label.grid(row=1, column=0, sticky=tk.W, pady=2)
        self.website_entry.grid(row=1, column=1, sticky=tk.W, pady=2)

    def setup_email_widget(self):
        """ Sets up the email widget """
        self.user_label = tk.Label(text="Email/Username: ", bg="white")
        self.user_entry = tk.Entry(width=50, bg="white")
        self.user_label.grid(row=2, column=0, sticky=tk.W, pady=2)
        self.user_entry.grid(row=2, column=1, sticky=tk.W, pady=2)

    def setup_password_widget(self):
        """ Sets up the password widget"""
        self.password_label = tk.Label(text="Password: ", bg="white")
        self.password_entry = tk.Entry(width=30, bg="white") #, show("*")
        self.password_generate_button = tk.Button(text="Generate Password", bg="white", command=self.generate_randpass)
        self.password_label.grid(row=3, column=0, sticky=tk.W, pady=2)
        self.password_entry.grid(row=3, column=1, sticky=tk.W, pady=2)
        self.password_generate_button.grid(row=3, column=1, sticky=tk.E, pady=2)

    def setup_account_widgets(self):
        """ Sets up account widgets """
        self.add_account_button = tk.Button(text="Add Account", width=42, command=self.add_data)
        self.search_button = tk.Button(text="Search", bg="white", command=self.search_acc)
        self.add_account_button.grid(row=4, column=1, sticky=tk.W)
        self.search_button.grid(row=1, column=2, sticky=tk.W, padx=5)

    def add_data(self):
        """ Adds any data from the widgets to the data file. """
        website = self.website_entry.get()
        user = self.user_entry.get()
        password = self.password_entry.get()
        
        entry_values = {
            website : {
                "user" : user,
                "password" : self.ceasar_cipher_encode(password, len(password))
            }
        }

        if website == "" or user == "" or password == "":
            return messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {user}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            try: 
                with open("data.json", 'r') as data_file:
                    # Read old data
                    current_data = json.load(data_file)
                    # Update old data with new data
                    current_data.update(entry_values)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open("data.json", 'w') as data_file:
                    current_data = {}
                    current_data.update(entry_values)
                    json.dump(current_data, data_file, indent = 4)
            else:
                with open("data.json", 'w') as data_file:
                    # Saving updated data
                    json.dump(current_data, data_file, indent = 4)
            finally:
                self.website_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.user_entry.delete(0, tk.END)

    def search_acc(self):
        """ Search through the data file to find an account """
        website = self.website_entry.get()

        try:
            with open("data.json", 'r') as data_file:
                # Read old data
                current_data = json.load(data_file)
                account = current_data[website]
                return_message = f"Username: {account['user']}\nPassword: {self.ceasar_cipher_encode(account['password'], len(account['password']), dir=-1)}"
        except (KeyError, FileNotFoundError):
            return_message = "Account not found"
        finally:
            return messagebox.showinfo(title="Account", message=return_message)

    def generate_randpass(self):
        """ Generates a random password """
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_letters = "abcdefghijklmnopqrstuvwxyz"
        symbols = "!@#$%^&*()"
        numbers = "1234567890"
        random_length = random.randrange(12, 17)
        
        new_pass = ""
        for _ in range(random_length):
            new_pass += random.choice([random.choice(lower_letters), random.choice(letters), random.choice(numbers), random.choice(symbols)])
            
        self.password_entry.delete(0, len(self.password_entry.get()))
        self.password_entry.insert(0, new_pass)
        self.clipboard_clear()
        self.clipboard_append(new_pass)
    
    def ceasar_cipher_encode(self, message: str, key: int, dir: int=1):
        """ Encodes a given message using ceasars cipher method 

        Args:
            message (str): message to encode.
            key (int): encoding key.
            dir (int, optional): 1 = encode, -1 = decode, defaults to 1.

        Returns:
            _type_: _description_
        """
        ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        encoded_message = ""
        for letter in message:
            if letter in ALPHABET:
                letter_idx = ALPHABET.index(letter)+(key*dir)
                encoded_message += ALPHABET[letter_idx%len(ALPHABET)]
            else:
                encoded_message += letter
        return encoded_message

if __name__ == "__main__":
    app = PasswordManager()
    app.mainloop()