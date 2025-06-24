from src.modules.editor_app_main import TextEditor
from src.dist import ConfigSpreader
from threading import Lock


class TextEditorMain(TextEditor):
    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    lock = Lock()
    try:
        with lock:
            c = ConfigSpreader()
            filepaths_obj = c.copy_configs()
        app = TextEditorMain(filepaths_obj)
        app.run()
    except KeyboardInterrupt:
        exit(1)
