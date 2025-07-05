class FilePaths:
    """
    Module for managing file paths used in the application.
    File paths are defined relative to the base directory of the application.

    Initially all paths are set to ``None``, and updated dynamically during runtime via ``.update_config_path(...)`` class method after copying files to their respective locations depending on the operating system.

    Available paths:
        - ``ICON_ICON_FILEPATH (str | None)``: Path to the `.ico` file (for window icon).
        - ``ICON_PNG_FILEPATH (str | None)``: Path to the `.png` file (alternative icon format).
        - ``THEMES_FILEPATH (str | None)``: Path to the themes JSON file.
        - ``USER_CONFIG_FILEPATH (str | None)``: Path to the user configuration JSON file.
        - ``USER_HOTKEYS_FILEPATH (str | None)``: Path to the user hotkeys JSON file.

    Internal:
        - ``_bindings (dict[str, str])``: Maps actual filenames to their corresponding attribute names
                                    on this class, for dynamic updates.

    Usage:
        Set a path then call the ``.update_config_path(...)`` method to update the class attributes in a loop.
    """
    ICON_ICON_FILEPATH = str | None
    ICON_PNG_FILEPATH = str | None
    THEMES_FILEPATH = str | None

    USER_CONFIG_FILEPATH = str | None
    USER_HOTKEYS_FILEPATH = str | None

    _bindings = dict

    @classmethod
    def update_config_path(cls, file_name: str, file_path: str) -> type["FilePaths"]:
        """
        Updates the appropriate class attribute for a given configuration or resource file.

        Args:
            file_name (str): The known filename (e.g. "themes.json"). Needed to fetch the corresponding class attribute name.
            file_path (str): The absolute path to assign to its corresponding class attribute.

        Raises:
            ValueError: If the file name is not a recognized configuration/resource file.

        Returns:
            type[FilePaths]: The class itself (with updated attribute).
        """
        ...
