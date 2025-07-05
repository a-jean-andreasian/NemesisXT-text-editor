from src.modules.editor_app_main import TextEditor
from src.dist import ConfigSpreader
from threading import Lock
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.config.paths import FilePaths

if __name__ == '__main__':
    lock = Lock()

    try:
        with lock:
            c = ConfigSpreader()
            filepaths_obj: type["FilePaths"] = c.copy_configs()
        app = TextEditor(filepaths_obj)
        app.root.mainloop()
    except KeyboardInterrupt:
        exit(1)
