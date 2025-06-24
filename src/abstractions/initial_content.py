from abc import ABC


class InitialContent(ABC):
    """
    Abstract base class for initial content.
    """
    file_name: str
    content: dict | bytes
