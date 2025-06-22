import tkinter as tk
from tkinter import font
from src.config.paths import UserSettingsFilePaths
from src.config.user import UserSettings


class FontSettings:
    def __init__(self, text: tk.Text):
        self.text = text
        self.user_settings: UserSettings = UserSettings(settings_file=UserSettingsFilePaths.USER_CONFIG_FILEPATH)

        self.font_size = self.user_settings.settings.font_size

        # Add a binding to change the font size with Ctrl + Mouse Wheel
        self.text.bind("<Control-MouseWheel>", self.change_font_size)

        # Get the initial font information
        font_info = font.nametofont(text.cget("font"))

        # Create a separate font configuration to control the size
        self.font_size = font_info.actual()["size"]
        self.text_font = font.nametofont(text.cget("font"))
        self.user_config = UserSettingsFilePaths.USER_CONFIG_FILEPATH

    def change_font_size(self, event):
        if event.delta > 0:
            self.font_size += 1
        else:
            self.font_size -= 1

        # Create a new font with the updated size
        font_name = self.text.cget("font")
        font_name = font.nametofont(font_name)
        font_name.configure(size=self.font_size)

        # Update the text widget's font
        self.text.configure(font=font_name)
        # Saving user's choice
        self.save_user_font()

    def save_user_font(self):
        self.user_settings.update_settings('font_size', self.font_size)
