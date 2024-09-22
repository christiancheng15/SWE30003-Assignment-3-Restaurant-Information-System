from classes.SystemUtils import SystemUtils
from classes.Validator import Validator 
from classes.Reports import Reports


class StaffInterface:
    """
    A class to represent the staff interface of the system.

    Methods
    -------
    display() -> None:
        Displays the staff dashboard and handles user input.
    """

    @staticmethod
    def display() -> None:
        """
        Displays the staff dashboard and handles user input.

        The method runs in a loop, showing the staff dashboard options and handling the 
        corresponding user inputs to export sales reports or manage reservations.
        """
        message = ""
        reports = Reports()
        while True:
            SystemUtils.clear_screen()
            SystemUtils.display_message(message)
            SystemUtils.heading("STAFF DASHBOARD")
            print("[1] Export Sales Report\n")
            print("[2] Export Menu Items Report\n")
            print("[3] Manage Reservations\n")
            print("[4] Shutdown the System\n")
            print("[E] Exit\n")
            user_input = input("Select an option: ").lower()

            if user_input == 'e': 
                return
            
            SystemUtils.clear_screen()

            if user_input in ['1', '2', '3']:
                if user_input == '1':
                    SystemUtils.heading("SALES REPORT")
                    temp = input("Date (DD/MM/YYYY) or [E] Exit: ")
                    if temp.lower() == 'e':
                        continue
                    if Validator.validate_date(temp):
                        reports.display_sales(temp)
                    else:
                        print("Please enter a valid date in DD/MM/YYYY format.") 
                elif user_input == '2':
                    SystemUtils.heading("MENU ITEM REPORT")
                    temp = input("Date (DD/MM/YYYY) or [E] Exit: ")
                    if temp.lower() == 'e':
                        continue
                    if Validator.validate_date(temp):
                        reports.display_menuitems(temp)
                    else:
                        print("Please enter a valid date in DD/MM/YYYY format.") 
                elif user_input == '3':
                    SystemUtils.heading("UPCOMING BOOKINGS")
                    reports.display_reservations()
                input("\nPress ENTER to continue")
            elif user_input == '4':
                SystemUtils.heading("SYSTEM SHUTDOWN CONFIRMATION")
                SystemUtils.shutdown()
            else:
                message = "Please select a valid option."
                continue