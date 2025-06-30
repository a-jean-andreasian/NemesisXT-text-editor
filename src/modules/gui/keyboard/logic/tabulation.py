import tkinter as tk


# Tabulation functionality for the text editor
class TabLogic:
    def __init__(self, text: tk.Text):
        self.text = text

    def tab_forward(self, _):
        try:
            # Capture selection range
            sel_start = self.text.index("sel.first linestart")
            sel_end = self.text.index("sel.last lineend")
            content = self.text.get(sel_start, sel_end)

            lines = content.split('\n')
            indented = ['    ' + line for line in lines]

            self.text.delete(sel_start, sel_end)
            self.text.insert(sel_start, '\n'.join(indented))

            # Re-select the modified text properly
            new_end = self.text.index(f"{sel_start} + {len(indented) - 1} lines linestart + {len(indented[-1])}c")
            self.text.tag_add("sel", sel_start, new_end)

        except tk.TclError:
            # No selection
            self.text.insert(tk.INSERT, "    ")

        return 'break'


    def tab_backward(self, _):
        try:
            sel_start = self.text.index("sel.first linestart")
            sel_end = self.text.index("sel.last lineend")
            content = self.text.get(sel_start, sel_end)

            lines = content.split('\n')

            def unindent(line):
                if line.startswith("    "):
                    return line[4:]
                elif line.startswith("\t"):
                    return line[1:]
                else:
                    return line

            unindented = [unindent(line) for line in lines]

            self.text.delete(sel_start, sel_end)
            self.text.insert(sel_start, '\n'.join(unindented))

            new_end = self.text.index(f"{sel_start} + {len(unindented) - 1} lines linestart + {len(unindented[-1])}c")
            self.text.tag_add("sel", sel_start, new_end)

        except tk.TclError:
            # No selection
            current_position = self.text.index(tk.INSERT)
            if current_position.endswith(".0"):
                return 'break'
            prev_char_index = self.text.index(f"{current_position} - 4 chars")
            if self.text.get(prev_char_index, current_position) == "    ":
                self.text.delete(prev_char_index, current_position)
                self.text.mark_set(tk.INSERT, prev_char_index)

        return 'break'
