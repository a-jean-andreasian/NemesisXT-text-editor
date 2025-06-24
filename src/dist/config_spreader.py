import os
import platform
import json
from pathlib import Path
from src.config.app.config import APP_NAME, APP_VERSION
import copy
from typing import TYPE_CHECKING

from src.dist.initial_content import InitialThemes, InitialUserConfig, Icon
from src.config.paths import FilePaths

if TYPE_CHECKING:
    from src.abstractions.initial_content import InitialContent


class MetaProgrammer:
    def __init__(self):
        self.object = FilePaths


    def update_content_class(self, file_name: str, file_path: str):
        """
        Updates the file name and content of the initial content class.
        """
        if file_name == "user_config.json":
            self.object.USER_CONFIG_FILEPATH = file_path
        elif file_name == "user_hotkeys.json":
            self.object.USER_HOTKEYS_FILEPATH = file_path
        elif file_name == "themes.json":
            self.object.THEMES_FILEPATH = file_path
        elif file_name == "icon.png":
            self.object.ICO_LOGO_FILEPATH = file_path
        return

    @property
    def obj(self):
        return self.object



class ConfigSpreader:
    def __init__(self):
        self.app_name = copy.copy(APP_NAME).replace(" ", "_").lower() + APP_VERSION
        self.entities_to_copy: list["InitialContent"] = [
            InitialThemes,
            InitialUserConfig,
            Icon
        ]
        self.meta_programmer = MetaProgrammer()



    def get_base_directory(self, app_name) -> str:
        system = platform.system()
        if system == "Windows":
            base = os.getenv("APPDATA", os.path.expanduser(f"~\\AppData\\Roaming\\{app_name}"))
        elif system == "Darwin":  # macOS
            base = os.path.expanduser(f"~/Library/Application Support/{app_name}")
        else:  # Linux or others
            base = os.getenv("XDG_CONFIG_HOME", os.path.expanduser(f"~/.config/{app_name}"))
        return base

    def create_base_directory(self, config_dir: Path) -> bool:
        """
        Creates the base directory for the application.
        """
        if not config_dir.exists():
            try:
                config_dir.mkdir(parents=True, exist_ok=True)
                print(f"Configuration directory created: {config_dir}")
            except PermissionError:
                print(f"Permission denied: Unable to create directory {config_dir}.")
                return False
            except Exception as e:
                print(f"An error occurred while creating the directory: {e}")
                return False
        else:
            print(f"Configuration directory already exists: {config_dir}")
        return True

    def copy_configs(self) -> FilePaths:
        """
        Copies the configuration files to the appropriate directory based on the operating system.
        """

        base_dir = self.get_base_directory(self.app_name)
        config_dir = Path(base_dir) / self.app_name
        if not self.create_base_directory(config_dir):
            raise RuntimeError(f"Failed to create configuration directory: {config_dir}")

        for entity in self.entities_to_copy:
            file_path = os.path.join(config_dir, entity.file_name)

            if not os.path.exists(file_path):
                print(f"Copying {entity.file_name} to {file_path}")

                # If the content is a dictionary, write it directly to the file
                if isinstance(entity.content, dict):
                    with open(file_path, 'w', encoding='utf-8') as file:
                        json.dump(entity.content, file, indent=4, ensure_ascii=False)

                    # If content is a binary file
                elif isinstance(entity.content, bytes):
                    with open(file_path, 'wb') as file:
                        file.write(entity.content)

            # Updating the FilePaths module with the new paths
            print(f"Updating content class for FilePaths {entity.file_name} at {file_path}")
            self.meta_programmer.update_content_class(file_name=entity.file_name, file_path=file_path)

        print(f"Configuration files copied to: {config_dir}")
        return self.meta_programmer.obj

