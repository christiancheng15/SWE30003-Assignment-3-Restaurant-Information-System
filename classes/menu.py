from classes.Database import Database
from classes.MenuItem import MenuItem


class Menu:
    """
    A class to represent the menu using the Singleton pattern.

    Attributes
    ----------
    _instance : Menu
        A single instance of the Menu class.
    menu_items : list
        A list of MenuItem objects representing the items in the menu.

    Methods
    -------
    __new__(cls) -> 'Menu':
        Creates and returns a single instance of the Menu class.
    load_menu() -> None:
        Loads the menu items from the database.
    __len__() -> int:
        Returns the number of items in the menu.
    __getitem__(index: int) -> MenuItem:
        Returns the menu item at the specified index.
    display_menu() -> None:
        Displays the menu items.
    """

    _instance = None

    def __new__(cls) -> 'Menu':
        """
        Creates and returns a single instance of the Menu class.

        Returns
        -------
        Menu
            A single instance of the Menu class.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.menu_items = []
            cls._instance.load_menu()
        return cls._instance

    def load_menu(self) -> None:
        """
        Loads the menu items from the database.
        """
        db = Database("./menu.json")
        menu_data = db.read()
        for item_data in menu_data:
            if item_data['availability'] and item_data['active']:
                item = MenuItem(
                    item_data['id'],
                    item_data['name'],
                    item_data['description'],
                    item_data['price'],
                    item_data['category'],
                    item_data['availability'],
                    item_data['active']
                )
                self.menu_items.append(item)

    def __len__(self) -> int:
        """
        Returns the number of items in the menu.

        Returns
        -------
        int
            The number of items in the menu.
        """
        return len(self.menu_items)

    def __getitem__(self, index: int) -> MenuItem:
        """
        Returns the menu item at the specified index.

        Parameters
        ----------
        index : int
            The index of the menu item to be retrieved.

        Returns
        -------
        MenuItem
            The menu item at the specified index.
        """
        return self.menu_items[index]

    def display_menu(self) -> None:
        """
        Displays the menu items.
        """
        for index, item in enumerate(self.menu_items, start=1):
            print(f"{index}. \033[1m{item.name}\033[0m - ${item.price:.2f}\n")
            print(f"      \x1B[3m{item.description}\x1B[0m\n")
