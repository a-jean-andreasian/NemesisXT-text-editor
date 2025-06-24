import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

"""
Module for managing file paths used in the application.

Path are defined relative to the base directory of the application.
Based on the environment variables, the paths can be overridden.
- This we need to pack the application with PyInstaller. `config_spreader.py` will copy json files to the correct location based on the OS.
- Then it will set the environment variables to point to the correct paths.
"""


class FilePaths:
    ICO_LOGO_FILEPATH = None

    USER_CONFIG_FILEPATH = None  # config_spreader.py will set this path
    USER_HOTKEYS_FILEPATH = None  # TODO: implement this
    THEMES_FILEPATH = None  # config_spreader.py will set this path
