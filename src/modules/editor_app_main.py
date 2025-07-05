import tkinter as tk
from src.modules.gui.themes.theme_manager import ThemeManager
from src.modules.gui.functional import StandAloneFunctions
from src.modules.file_managment.file_manager import FileManager
from src.modules.gui.keyboard.hotkeys import KeyboardBindings
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.config.paths import FilePaths


class TextEditor:
    """
    TextEditor is a simple text editor application built using the tkinter library.

    Attributes:
        root (tkinter.Tk): The main application window.
        menu (tkinter.Menu): The menu bar for the application.
        text (tkinter.Text): The text editing widget.

    Methods:
        __init__(self, filepath_=None): Initializes the TextEditor instance.
    """

    def __init__(self, filepaths_obj: "FilePaths"):
        # defining the settings
        self.root = tk.Tk()
        self.root.title("Nemesis-XT")
        # self.root.attributes('-transparentcolor', 'white')
        self.root.iconbitmap(default=filepaths_obj.ICON_PNG_FILEPATH)
        self.root.geometry("800x600")  # Set your preferred initial window size

        # main menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # editor widget
        self.text = tk.Text(self.root, undo=True, maxundo=-1, autoseparators=True)
        self.text.pack(fill="both", expand=True)  # full-size

        # initialization of subclasses
        theme_manager = ThemeManager(themes_filepath=filepaths_obj.THEMES_FILEPATH)
        file_manager = FileManager(text=self.text, root=self.root)
        text_settings = StandAloneFunctions(text=self.text)
        # font_settings = FontSettings(text=self.text)
        keyboard_bindings = KeyboardBindings(text=self.text, file_manager=file_manager).bindings

        # hotkeys
        for keyboard_binding in keyboard_bindings:
            self.text.bind(sequence=keyboard_binding.key_combination, func=keyboard_binding.action, add=None)

        # File tab
        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=file_manager.open_file)
        self.file_menu.add_command(label="Save", command=file_manager.save_file_as)
        self.file_menu.add_command(label="Exit", command=file_manager.on_closing)

        # Edit tab
        self.edit_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Clear", command=text_settings.clear_text)

        # Themes tab
        self.themes_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Themes", menu=self.themes_menu)
        self.themes_menu.add_command(label="Atom",
                                     command=lambda: theme_manager.set_theme(chosen_theme='atom', text=self.text))
        self.themes_menu.add_command(label="Sublime-Text",
                                     command=lambda: theme_manager.set_theme(chosen_theme='sublime-text',
                                                                             text=self.text))
        self.themes_menu.add_command(label="Black & White",
                                     command=lambda: theme_manager.set_theme(chosen_theme='black', text=self.text))
        self.themes_menu.add_command(label="Light",
                                     command=lambda: theme_manager.set_theme(chosen_theme='light', text=self.text))

        # Settings tab
        self.settings_menu = tk.Menu(self.menu, tearoff=False)
        self.settings_menu.add_cascade(label="Settings", menu=self.settings_menu)

        # exit
        self.root.protocol(name="WM_DELETE_WINDOW", func=file_manager.on_closing)
