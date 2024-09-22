from classes.Menu import Menu
from classes.SystemUtils import SystemUtils

class MenuHandler:
    """
    A class to handle menu-related operations.

    Methods
    -------
    view_menu(menu: Menu) -> str:
        Displays the menu and handles user interaction for ordering or exiting.
    """

    @staticmethod
    def view_menu(menu: Menu) -> bool:
        """
        Displays the menu and handles user interaction for ordering or exiting.

        Parameters
        ----------
        menu : Menu
            An instance of the Menu class representing the menu.

        Returns
        -------
        bool
            True if the user chooses to order, False if the user chooses to exit.
        """
        message = ""
        while True:
            SystemUtils.clear_screen()
            SystemUtils.display_message(message)
            SystemUtils.heading("MENU")
            menu.display_menu()
            print("\n[O] Order        [E] Exit")
            user_input = input("\nSelect an option: ").lower()
            if user_input == 'o':
                return True
            elif user_input == 'e':
                return False
            else:
                message = "[ERROR] Invalid Option. Please select a valid option."
