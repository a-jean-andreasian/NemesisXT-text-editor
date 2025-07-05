import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tkinter import Text


class ThemeManager:
    """
    ThemeManager is responsible for managing the color themes of the Text Editor.

    Args:
        themes_filepath (str): The file path to the JSON file containing theme definitions.

    Attributes:
        themes (dict): A dictionary containing theme definitions loaded from a JSON file.
    """

    def __init__(self, themes_filepath: str):
        with open(themes_filepath) as file:
            self.themes = json.load(file)

    def set_theme(self, chosen_theme: str, text: "Text"):
        """
        Set the color theme of the Text Editor.

        Args:
            :param chosen_theme: The name of the theme to apply.  A string specifying the theme name (e.g., 'light' or 'dark').
            :param text The Text widget to apply the theme to.

        :return: None
        """
        if chosen_theme in self.themes:
            current_theme = self.themes[chosen_theme]

            # [Fix-needed]
            # supposed to set dark theme for header and menus, but only menus are affected
            """
            self.root.configure(bg=current_theme["background"])

            self.menu.configure(bg=current_theme["menu_background"], fg=current_theme["menu_foreground"])
            self.file_menu.configure(bg=current_theme["menu_background"], fg=current_theme["menu_foreground"])
            self.edit_menu.configure(bg=current_theme["menu_background"], fg=current_theme["menu_foreground"])
            """

            text.configure(bg=current_theme["text_background"], fg=current_theme["text_foreground"])
            text.configure(insertbackground=current_theme["cursor"])  # Set cursor color to text color
