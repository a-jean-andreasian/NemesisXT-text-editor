"""A special window for custom titlebar"""

from __future__ import annotations

import pathlib
from ctypes import WINFUNCTYPE, c_uint64, windll
from platform import win32_ver
import tkinter as tk
from typing import Any, Dict, Literal, Mapping, Optional, Tuple

import darkdetect
from PIL import Image, ImageTk

from src.modules.gui.widgets.title_bar.data import *


class CustomTitleBar(tk.Frame):
    def __init__(self, master: tk.Tk, title: str, icon_path: str = "", height: int = 30, **kwargs):
        super().__init__(master, height=height, **kwargs)

        self.master = master
        self.hwnd = windll.user32.GetParent(self.master.winfo_id())

        self.bg = "#000000"
        self.fg = "#ffffff"
        self.hover_bg = "#222222"
        self.exit_hover = "#c42b1c"

        self.configure(bg=self.bg)

        # Drag behavior
        self.bind("<B1-Motion>", self._move_window)

        # Icon (optional)
        if icon_path:
            icon_img = Image.open(icon_path).resize((16, 16))
            self.icon = ImageTk.PhotoImage(icon_img)
            tk.Label(self, image=self.icon, bg=self.bg).pack(side="left", padx=5)

        # Title label
        self.title_label = tk.Label(self, text=title, fg=self.fg, bg=self.bg)
        self.title_label.pack(side="left", padx=5)
        self.title_label.bind("<B1-Motion>", self._move_window)

        # Buttons
        self.exit_btn = tk.Button(self, text="✕", fg=self.fg, bg=self.bg, activebackground=self.exit_hover,
                                  bd=0, command=self.master.destroy)
        self.exit_btn.pack(side="right", ipadx=10)

        self.min_btn = tk.Button(self, text="—", fg=self.fg, bg=self.bg, activebackground=self.hover_bg,
                                 bd=0, command=self.master.iconify)
        self.min_btn.pack(side="right", ipadx=10)

        self.max_btn = tk.Button(self, text="⬜", fg=self.fg, bg=self.bg, activebackground=self.hover_bg,
                                 bd=0, command=self._toggle_maximize)
        self.max_btn.pack(side="right", ipadx=10)

        self.master.bind("<FocusIn>", lambda e: self._set_focus_style(True))
        self.master.bind("<FocusOut>", lambda e: self._set_focus_style(False))

    def _move_window(self, event):
        windll.user32.ReleaseCapture()
        windll.user32.SendMessageA(self.hwnd, 0x112, 0xf012, 0)

    def _toggle_maximize(self):
        if self.master.state() == "zoomed":
            self.master.state("normal")
        else:
            self.master.state("zoomed")

    def _set_focus_style(self, focus: bool):
        color = self.fg if focus else "grey"
        self.title_label.config(fg=color)
