from src.modules.gui.keyboard.logic import TabLogic
from src.modules.gui.fonts.gui_font_settings import FontSettings
from src.modules.gui.tk_soft_methods import safe_undo, safe_redo
from dataclasses import dataclass
from typing import TYPE_CHECKING
import platform

if TYPE_CHECKING:
    import tkinter as tk
    from src.modules.file_managment.file_manager import FileManager

MOD = "<Command" if platform.system() == "Darwin" else "<Control"


@dataclass
class KeyboardBinding:
    key_combination: str
    description: str
    action: callable


class KeyboardBindings:
    def __init__(self, text: "tk.Text", file_manager: "FileManager"):
        tab_logic = TabLogic(text=text)
        font_settings = FontSettings(text=text)

        self.bindings: list[KeyboardBinding] = [
            KeyboardBinding("<Tab>", "Forward tabulation.", tab_logic.tab_forward),
            KeyboardBinding("<Shift-Tab>", "Backward tabulation.", tab_logic.tab_backward),
            KeyboardBinding(MOD + "-MouseWheel>", "Font size adjustment.", font_settings.change_font_size),
            KeyboardBinding(MOD + "-s>", "Save current changes.", file_manager.save_file),
            KeyboardBinding(MOD + "-r>", "Save file as.", file_manager.save_file_as),
            KeyboardBinding(MOD + "-o>", "Open file.", file_manager.open_file),
            KeyboardBinding(MOD + "-w>", "Close current file.", file_manager.close_file),
            KeyboardBinding(MOD + "-z>", "Undo last change.", safe_undo(text)),
            KeyboardBinding(MOD + "-y>", "Redo last undone change.", safe_redo(text)),
        ]
