import tkinter as tk
from tkinter import filedialog, messagebox  # Frame, Button, X
from threading import Lock


class FileManager:
    def __init__(self, text: tk.Text, root: tk.Tk):
        self.text = text
        self.text_in_file: str = None
        self.root = root
        self.file_path = None
        self.lock = Lock()

    def __is_everything_saved(self) -> bool:
        """
        Checks if there are any unsaved changes in the text editor.
        """
        tk_text_str = self.text.get("1.0", "end-1c")
        if len(tk_text_str) > 0:
            if self.text_in_file != tk_text_str:
                return False
        return True

    def close_file(self, event=None):
        """
        Closes the current file in text editor.
        """
        with self.lock:
            if not self.__is_everything_saved():
                response: bool | None = messagebox.askyesnocancel("Save Changes",
                                                                  "Do you want to save the changes before closing?")
                if response:
                    self.save_file_as()
            self.text.delete('1.0', tk.END)
            self.file_path = None
            self.text_in_file = None

    def open_file(self, event=None):
        """
        Open a new file in text editor.
        """
        with self.lock:
            file_path = filedialog.askopenfilename()
            if file_path:
                self.file_path = file_path
                with open(file_path, 'r') as file:
                    self.text.delete('1.0', tk.END)
                    self.text_in_file = file.read()
                    self.text.insert('1.0', self.text_in_file)

    def save_file(self, event=None):
        """
        Saves the text to the current file.
        """
        try:
            if self.file_path:
                with self.lock:
                    with open(self.file_path, 'w') as file:
                        file.write(self.text.get('1.0', tk.END))
            else:
                return self.save_file_as()
        except Exception as e:
            # messagebox.showerror("Error", f"Failed to save file: {e}")
            return  # Handle the error gracefully

    def save_file_as(self, event=None):
        """
        Saves the text to a new file.
        """
        with self.lock:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt", filetypes=[("Text Files", "*.txt")], initialfile="NemesisXT-Note.txt")

            with open(file_path, 'w') as file:
                file.write(self.text.get('1.0', tk.END))
            self.file_path = file_path
            return

    def on_closing(self):
        """
        Asks the user if he wants to save the changes on closing.
        """
        if not self.__is_everything_saved():
            response: bool | None = messagebox.askyesnocancel("Save Changes",
                                                              "Do you want to save the changes before closing?")
            if response:
                self.save_file_as()
        self.root.destroy()
