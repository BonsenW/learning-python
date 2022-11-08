import json
import os

class PomodoroAppSettings():
    
    MAIN_PATH = f"{os.getcwd()}"
    
    # General
    TIME_DATA_PATH = f"{MAIN_PATH}\\data\\time.json"
    SETTING_COG_IMAGE_PATH = f"{MAIN_PATH}\\images\\Settings Cog.png"
    BG_COLOUR_BLUE = "#00111e"
    BG_COLOUR_GREEN = "#001e0b"
    BG_COLOUR_RED = "#1e0005"
    FONT_NAME = "Screaming Neon"

    # Screen Dimension
    SCREEN_DIMENSIONS = '500x500'
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    
    # Halo Images
    GREEN_HALO_IMAGE_PATH = f"{MAIN_PATH}\\images\\Halo Border Green.png"
    BLUE_HALO_IMAGE_PATH = f"{MAIN_PATH}\\images\\Halo Border Blue.png"
    RED_HALO_IMAGE_PATH = f"{MAIN_PATH}\\images\\Halo Border Red.png"
    HALO_WIDTH = 250
    HALO_HEIGHT = 250
    
    # Labels
    TIMER_TEXT_FONT = (FONT_NAME, 35, 'bold')
    TIMER_TEXT_COLOUR = "#ffffff"
    START_TEXT_FONT = (FONT_NAME, 10, 'italic')
    START_TEXT_COLOUR = "#ffffff"
    
    def get_times(self, time_name: str):
        """ Returns the time for the given time name (work, short_break, long_break) """
        with open(self.TIME_DATA_PATH, 'r') as data:
            current_data: dict = json.load(data)
            assert time_name in current_data.keys(), f"Given key {time_name} is not in dictionary, keys avaliable are: {current_data.keys()}"
            return current_data[time_name]
    
    def change_times(self, time_name: str, new_value: int):
        with open(self.TIME_DATA_PATH, 'r') as data:
            current_data: dict = json.load(data)
            assert time_name in current_data.keys(), f"Given key {time_name} is not in dictionary, keys avaliable are: {current_data.keys()}"
        with open(self.TIME_DATA_PATH, 'w') as data:
            current_data[time_name] = new_value
            json.dump(current_data, data, indent=4)