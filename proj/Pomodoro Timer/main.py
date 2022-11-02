from data.PomodoroAppSettings import PomodoroAppSettings
from tkinter import messagebox
import tkinter as tk
import datetime
import winsound
import math

class PomodoroApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # Variables
        self.repetition_number = 0
        self.timer_started = False
        # Configuration
        self.settings = PomodoroAppSettings()
        self.setup_screen()
        self.setup_canvas()
        self.bind("<KeyRelease>", self.on_space_release)

    def setup_screen(self):
        """ Initialises the GUI screen. """
        self.title("Minimalistic Pomodoro Timer")
        self.geometry(self.settings.SCREEN_DIMENSIONS)
        self.main_frame = tk.Frame(master=self, width=self.settings.SCREEN_WIDTH, height=self.settings.SCREEN_HEIGHT)
        self.main_frame.grid(row=0, column=0)
    
    def setup_canvas(self):
        """ Sets up the base canvas for the timer. """
        # Variables
        canvas_width = self.settings.SCREEN_WIDTH 
        canvas_height = self.settings.SCREEN_HEIGHT
        center = (canvas_width/2, canvas_height/2)
        lower_center = (canvas_width/2, canvas_height/2+40)
        top_right = (10, 10)
        # Canvas
        self.canvas = tk.Canvas(master=self.main_frame, width=canvas_width, height=canvas_height, bg=self.settings.BG_COLOUR_BLUE, highlightthickness=0) 
        
        self.halo_img = tk.PhotoImage(master=self.canvas, file=self.settings.BLUE_HALO_IMAGE_PATH)
        self.canvas.create_image(center, image=self.halo_img)
        
        self.cog_img = tk.PhotoImage(master=self.canvas, file=self.settings.SETTING_COG_IMAGE_PATH)
        self.cog_button = tk.Button(master=self.canvas, image=self.cog_img, bg=self.settings.BG_COLOUR_BLUE, activebackground=self.settings.BG_COLOUR_BLUE, border=0, command=self.open_settings)
        self.canvas.create_window(top_right, anchor=tk.NW, window=self.cog_button)
        
        self.timer_text = self.canvas.create_text(center, text=' '.join([i for i in "TIMER"]), fill=self.settings.TIMER_TEXT_COLOUR, font=self.settings.TIMER_TEXT_FONT)
        self.start_text = self.canvas.create_text(lower_center, text=' '.join([i for i in "PRESS SPACE TO START TIMER"]), fill=self.settings.START_TEXT_COLOUR, font=self.settings.START_TEXT_FONT)
        
        self.canvas.grid(row=0, column=0)
        
    def start_timer(self):
        self.repetition_number += 1
        work_sec = self.settings.get_times('work_min') * 60
        short_break_sec = self.settings.get_times('short_break_min') * 60
        long_break_sec = self.settings.get_times('long_break_min') * 60
        
        if self.repetition_number%8 == 0:
            # Long break
            self.alternate_gui_colours()
            winsound.Beep(5000, 1000)
            self.change_start_text("Break Time! ")
            self.after(3000, self.change_start_text, f"Press Space To Reset! ")
            self.count_down(long_break_sec)
        elif self.repetition_number%2 == 0:
            # Short break
            self.alternate_gui_colours()
            winsound.Beep(5000, 1000)
            self.change_start_text("Break Time! ")
            self.after(3000, self.change_start_text, f"Press Space To Reset! ")
            self.count_down(short_break_sec)
        else:
            # Work
            self.change_start_text("Work Time! ")
            winsound.Beep(2500, 500)
            self.after(3000, self.change_start_text, f"{math.ceil((8 - self.repetition_number)/2)} Pomodoros Left! ")
            self.after(6000, self.change_start_text, f"Press Space To Reset! ")
            self.alternate_gui_colours()
            self.count_down(work_sec)
    
    def reset_timer(self):
        self.repetition_number = 0
        self.timer_started = False
        self.after_cancel(self.timer)
        self.change_gui_colour(bg_colour = self.settings.BG_COLOUR_BLUE, halo_img_path = self.settings.BLUE_HALO_IMAGE_PATH)
        self.change_timer_text("TIMER")
        self.change_start_text("PRESS SPACE TO START TIMER")
         
    def count_down(self, count):
        new_time = str(datetime.timedelta(seconds=count))[2::]
        self.change_timer_text(new_time)
        if count >= 0:
            self.timer = self.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()

    def open_settings(self):
        newWindow = tk.Toplevel(master=self, bg=self.settings.BG_COLOUR_BLUE)
        newWindow.title("Pomodoro Timer Settings")
        tk.Label(master=newWindow, text="Work Minutes").grid(column=0, row=0, padx=5, pady=5)
        work_min_entry = tk.Entry(master=newWindow)
        work_min_entry.grid(column=0, row=1, padx=5, pady=5)
        tk.Label(master=newWindow, text="Short Break Minutes").grid(column=0, row=2, padx=5, pady=5)
        short_break_min_entry = tk.Entry(newWindow)
        short_break_min_entry.grid(column=0, row=3, padx=5, pady=5)
        tk.Label(master=newWindow, text="Long Break Minutes").grid(column=0, row=4, padx=5, pady=5)
        long_break_min_entry = tk.Entry(master=newWindow)
        long_break_min_entry.grid(column=0, row=5, padx=5, pady=5)
        
        def change_time_settings():
            try:
                self.settings.change_times('work_min', new_value=int(work_min_entry.get()))
                self.settings.change_times('short_break_min', new_value=int(short_break_min_entry.get()))
                self.settings.change_times('long_break_min', new_value=int(long_break_min_entry.get()))
            except ValueError:
                messagebox.showerror(title="VALUE ERROR!", message="Invalid Value")
        
        confirm_button = tk.Button(master=newWindow, text="Confirm", command=change_time_settings)
        confirm_button.grid(column=0, row=6, padx=5, pady=10)
        
    def change_timer_text(self, new_text):
        self.canvas.itemconfig(self.timer_text, text=' '.join([i for i in new_text]))
    
    def change_start_text(self, new_text):
        self.canvas.itemconfig(self.start_text, text=' '.join([i for i in new_text]))

    def change_gui_colour(self, bg_colour, halo_img_path):
        center = (self.settings.SCREEN_WIDTH /2, self.settings.SCREEN_HEIGHT/2)
        self.canvas['bg'] = bg_colour
        self.cog_button['bg'] = bg_colour
        self.halo_img = tk.PhotoImage(master=self.canvas, file=halo_img_path)
        self.canvas.create_image(center, image=self.halo_img)
        
    def alternate_gui_colours(self):
        bg_red = self.settings.BG_COLOUR_RED
        bg_green = self.settings.BG_COLOUR_GREEN
        
        if self.canvas['bg'] == bg_red:
            self.change_gui_colour(bg_colour=bg_green, halo_img_path=self.settings.GREEN_HALO_IMAGE_PATH)
        else:
            self.change_gui_colour(bg_colour=bg_red, halo_img_path=self.settings.RED_HALO_IMAGE_PATH)

    def on_space_release(self, e):
        """ Starts the timer on space key release. """
        space_key_code = '32'
        if str(e)[50:52] == space_key_code:
            if self.timer_started == False:
                self.timer_started = True
                self.start_timer()
            elif self.timer_started == True:
                self.reset_timer()

if __name__ == "__main__":
    app = PomodoroApp()
    app.mainloop()