import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


class FilePaths:
    ICON_ICON_FILEPATH = None
    ICON_PNG_FILEPATH = None
    THEMES_FILEPATH = None

    USER_CONFIG_FILEPATH = None
    USER_HOTKEYS_FILEPATH = None

    _bindings = {
        "icon.ico": "ICON_ICON_FILEPATH",
        "icon.png": "ICON_PNG_FILEPATH",
        "themes.json": "THEMES_FILEPATH",
        "user_config.json": "USER_CONFIG_FILEPATH",
        "user_hotkeys.json": "USER_HOTKEYS_FILEPATH",
    }

    @classmethod
    def update_config_path(cls, file_name: str, file_path: str) -> type["FilePaths"]:
        if file_name in cls._bindings:
            attr_name = cls._bindings[file_name]
            setattr(cls, attr_name, file_path)
        else:
            raise ValueError(f"File name '{file_name}' is not a valid attribute of FilePaths.")

        return cls
