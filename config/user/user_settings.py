from os import PathLike
from utils import JsonUtils
from threading import Lock
from abstractions.abssettings import AbsSettings
from typing import Any, Union
from dataclasses import dataclass, asdict, field


@dataclass
class UserSettingsData:
    """
    Data class to hold user settings.
    """
    font_size: int = field(default=12)  # Default font size


class UserSettings(AbsSettings):
    """
    Class to manage user settings.
    """

    def __init__(self, settings_file: PathLike):
        self.settings: UserSettingsData = None
        self.settings_file = settings_file

        self.lock = Lock()
        self.load_settings()

    def load_settings(self) -> None:
        if self.settings is None:
            with self.lock:
                settings_from_file: dict = JsonUtils.load_json(self.settings_file)

                if not settings_from_file:
                    self.settings = UserSettingsData()
                    self.save_settings()

                else:
                    self.settings = UserSettingsData(**settings_from_file)
        return

    def update_settings(self, key: str, value: Union[str, int, bool]) -> None:
        """
        Update a specific setting by key.
        Does not save the settings to file immediately.
        Call `save_settings` to persist changes.

        :param key: The key of the setting to update.
        :param value: The new value for the setting.
        """
        if hasattr(self.settings, key):
            setattr(self.settings, key, value)
        else:
            raise KeyError(f"Setting '{key}' does not exist.")
        return

    def save_settings(self):
        """
        Save the current settings to a file.
        """
        with self.lock:
            JsonUtils.save_json(filepath=self.settings_file, data=asdict(self.settings))
        return
