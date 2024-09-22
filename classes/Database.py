import json
from typing import Any


class Database:
    """
    A class to handle database operations using a JSON file.

    Attributes
    ----------
    file_path : str
        The path to the JSON file used for storing data.

    Methods
    -------
    read() -> Any:
        Reads and returns the data from the JSON file.
    write(data: Any) -> None:
        Writes the given data to the JSON file.
    append(item: Any) -> None:
        Appends an item to the data in the JSON file.
    """

    def __init__(self, file_path: str):
        """
        Constructs all the necessary attributes for the Database object.

        Parameters
        ----------
        file_path : str
            The path to the JSON file used for storing data.
        """
        self.file_path = file_path

    def read(self) -> Any:
        """
        Reads and returns the data from the JSON file.

        Returns
        -------
        Any
            The data read from the JSON file. Returns an empty list if the file
            does not exist or contains invalid JSON.
        """
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        return data

    def write(self, data: Any) -> None:
        """
        Writes the given data to the JSON file.

        Parameters
        ----------
        data : Any
            The data to be written to the JSON file.
        """
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def append(self, item: Any) -> None:
        """
        Appends an item to the data in the JSON file.

        Parameters
        ----------
        item : Any
            The item to be appended to the data in the JSON file.
        """
        data = self.read()
        data.append(item)
        self.write(data)