from src.modules.editor_app_main import TextEditor
from src.dist import ConfigSpreader
from threading import Lock

lock = Lock()

if __name__ == '__main__':
    try:
        with lock:
            c = ConfigSpreader()
            filepaths_obj = c.copy_configs()
        app = TextEditor(filepaths_obj)
        app.root.mainloop()
    except KeyboardInterrupt:
        exit(1)
