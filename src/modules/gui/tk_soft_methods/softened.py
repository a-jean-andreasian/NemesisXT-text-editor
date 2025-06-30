from tkinter import TclError, Text


def safe_undo(text: Text, event=None):
    try:
        text.edit_undo()
    except TclError:
        pass


def safe_redo(text: Text, event=None):
    try:
        text.edit_redo()
    except TclError:
        pass
