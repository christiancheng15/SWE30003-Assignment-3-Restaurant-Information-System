from classes.Menu import Menu
from classes.SystemUtils import SystemUtils
from classes.CustomerInterface import CustomerInterface
from classes.StaffInterface import StaffInterface
from classes.PinValidator import PinValidator


class MainInterface:
    """
    A class to represent the main interface of the system.

    Attributes
    ----------
    PIN_CODE : str
        The PIN code required for employee access.
    menu : Menu
        An instance of the Menu class representing the menu.
    message : str
        A message to be displayed on the screen.

    Methods
    -------
    display() -> None:
        Displays the main menu and handles user input.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the MainInterface object.
        """
        self.menu = Menu()
        self.message = ""

    def display(self) -> None:
        """
        Displays the main menu and handles user input.

        The method runs in a loop, showing the main menu options and handling the
        corresponding user inputs to access the customer interface or the employee
        interface after PIN validation.
        """
        while True:
            SystemUtils.clear_screen()
            SystemUtils.display_message(self.message)
            SystemUtils.heading("MAIN MENU")
            SystemUtils.koala()
            print("[1] Customer\n")
            print("[2] Employee\n")
            user_input = input("Select an option: ").lower()

            if user_input == '1':
                customer_interface = CustomerInterface(self.menu)
                customer_interface.display()
            elif user_input == '2':
                SystemUtils.clear_screen()
                SystemUtils.heading("STAFF LOGIN")
                if PinValidator.check_pin():
                    StaffInterface.display()
            else:
                self.message = "[ERROR] Invalid Option. Please select a valid option."