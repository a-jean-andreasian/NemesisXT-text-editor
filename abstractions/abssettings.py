from abc import ABC


class AbsSettings(ABC):
    """
    Abstract base class for settings management.
    This class defines the interface for settings-related operations.
    """
    def load_settings(self) -> None:
        """
        Load settings from a persistent storage into the instance.
        This method should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def save_settings(self):
        """
        Save current settings from instance into a persistent storage.
        This method should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method.")
