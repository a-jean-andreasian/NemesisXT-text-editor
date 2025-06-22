import json


class JsonUtils:
    @staticmethod
    def load_json(filepath: str) -> dict:
        """
        Load a JSON file and return its content as a dictionary.

        :param filepath: Path to the JSON file.
        :return: Dictionary containing the JSON data.
        """
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def save_json(filepath: str, data: dict):
        """
        Save a dictionary to a JSON file.

        :param filepath: Path to the JSON file.
        :param data: Dictionary to save.
        """
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
