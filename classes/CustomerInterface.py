from classes.Menu import Menu
from classes.SystemUtils import SystemUtils
from classes.ReservationHandler import ReservationHandler
from classes.OrderHandler import OrderHandler
from classes.MenuHandler import MenuHandler


class CustomerInterface:
    """
    A class to represent the customer interface of the system.

    Attributes
    ----------
    menu : Menu
        An instance of the Menu class representing the menu.

    Methods
    -------
    display():
        Displays the main menu and handles user input.
    """

    def __init__(self, menu: Menu):
        """
        Constructs all the necessary attributes for the CustomerInterface object.

        Parameters
        ----------
        menu : Menu
            An instance of the Menu class representing the menu.
        """
        self.menu = menu
        self.message = ""

    def display(self) -> None:
        """
        Displays the main menu and handles user input.

        The method runs in a loop, showing the main menu options and handling the 
        corresponding user inputs to make a reservation, view the menu, place an 
        order, or exit the system.
        """
        while True:
            SystemUtils.clear_screen()
            SystemUtils.display_message(self.message)
            SystemUtils.heading("MAIN MENU")
            print("[1] Make Reservation\n")
            print("[2] View Menu\n")
            print("[3] Place Order\n")
            print("[E] Exit\n")
            user_input = input("Select an option: ").lower()

            if user_input == '1':
                ReservationHandler.handle_reservation()
            elif user_input == '2':
                if MenuHandler.view_menu(self.menu):
                    OrderHandler.handle_order(self.menu)
            elif user_input == '3':
                OrderHandler.handle_order(self.menu)
            elif user_input == 'e':
                return
            else:
                self.message = "[ERROR] Invalid Option. Please select a valid option."