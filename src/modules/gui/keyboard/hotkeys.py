import tkinter as tk
from .tabulation import Tabulation


class KeyboardHotkeys:
    def __init__(self, text: tk.Text):
        self.text = text
        tabulation = Tabulation(self.text)
        # Assigning tabulation methods to instance
        self.tab_forward = tabulation.tab_forward
        self.tab_backward = tabulation.tab_backward
