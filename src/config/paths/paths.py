import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
print('base dir:', BASE_DIR)


class AssetsFilePaths:
    THEMES_FILEPATH = os.path.join(BASE_DIR, "config", "app", "themes.json")
    ICO_LOGO_FILEPATH = os.path.join(BASE_DIR, "assets", "logos", "window_logo.ico")
    PNG_LOGO_FILEPATH = os.path.join(BASE_DIR, "assets", "logos", "window_logo.png")


class UserSettingsFilePaths:
    USER_CONFIG_FILEPATH = os.path.join(BASE_DIR, "config", "user", "user_config.json")
    USER_HOTKEYS_FILEPATH = os.path.join(BASE_DIR, "config", "user", "user_hotkeys.json")
