from classes.SystemUtils import SystemUtils
from classes.Database import Database
from classes.Validator import Validator


class Reservation:
    """
    A class to handle reservations.

    Attributes
    ----------
    message : str
        A message to display to the user.
    date : str
        The date of the reservation.
    time : str
        The time of the reservation.
    name : str
        The name of the person making the reservation.
    mobile_number : str
        The mobile number of the person making the reservation.
    email : str
        The email address of the person making the reservation.
    party_size : str
        The size of the party for the reservation.
    accommodations : str
        Any additional accommodations for the reservation.

    Methods
    -------
    enter_reservation_details() -> bool:
        Prompts the user to enter reservation details.
    confirm_reservation() -> str:
        Confirms the reservation details with the user.
    make_reservation() -> None:
        Saves the reservation details to the database.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the Reservation object.
        """
        self.message = ""
        self.date = ""
        self.time = ""
        self.name = ""
        self.mobile_number = ""
        self.email = ""
        self.party_size = ""
        self.accommodations = ""

    def enter_reservation_details(self) -> bool:
        """
        Prompts the user to enter reservation details.

        Returns
        -------
        bool
            True if reservation details are successfully entered, False if the process is exited.
        """
        while not (self.date and self.time and self.name and self.mobile_number and self.email and self.party_size):
            SystemUtils.clear_screen()
            SystemUtils.heading("RESERVATION")
            print("Make a Reservation. Enter [E] to Exit Anytime.\n")
            self.message = SystemUtils.display_message(self.message)

            if not self.date:
                temp = input("Date (DD/MM/YYYY): ")
                if temp.lower() == 'e':
                    return False
                if Validator.validate_future_date(temp):
                    self.date = temp
                else:
                    self.message = "Please enter a valid date in the future in DD/MM/YYYY format."
                continue
            else:
                print(f"Date (DD/MM/YYYY): {self.date}")

            if not self.time:
                temp = input("Time (HH:MM): ")
                if temp.lower() == 'e':
                    return False
                if Validator.validate_time(temp):
                    self.time = temp
                else:
                    self.message = "Please enter a time between opening hours (09:00 - 21:00)."
                continue
            else:
                print(f"Time (HH:MM): {self.time}")

            if not self.name:
                temp = input("Name: ")
                if temp.lower() == 'e':
                    return False
                if Validator.validate_name(temp):
                    self.name = ' '.join(temp.title().split())
                else:
                    self.message = "Please enter a valid name."
                continue
            else:
                print(f"Name: {self.name}")

            if not self.mobile_number:
                temp = input("Mobile Number: ")
                if temp.lower() == 'e':
                    return False
                if Validator.validate_mobile_number(temp):
                    self.mobile_number = temp
                else:
                    self.message = "Please enter a valid mobile number starting with 04."
                continue
            else:
                print(f"Mobile Number: {self.mobile_number}")

            if not self.email:
                temp = input("Email: ")
                if temp.lower() == 'e':
                    return False
                if Validator.validate_email(temp):
                    self.email = temp
                else:
                    self.message = "Please enter a valid email address."
                continue
            else:
                print(f"Email: {self.email}")

            if not self.party_size:
                temp = input("Party Size (1-20): ")
                if temp.lower() == 'e':
                    return False
                if Validator.validate_party_size(temp):
                    self.party_size = int(temp)
                else:
                    self.message = "Please enter a valid party size (1-20)."
                continue
            else:
                print(f"Party Size (1-20): {self.party_size}")

        self.accommodations = input("Accommodations (optional): ")
        return True

    def confirm_reservation(self) -> str:
        """
        Confirms the reservation details with the user.

        Returns
        -------
        str
            A confirmation message indicating the result of the confirmation process.
        """
        while True:
            SystemUtils.clear_screen()
            SystemUtils.heading("RESERVATION")
            self.message = SystemUtils.display_message(self.message)
            print("Reservation Confirmation. Please ensure that all details are correct.\n")
            print(f"Date (DD/MM/YYYY): {self.date}")
            print(f"Time (HH:MM): {self.time}")
            print(f"Name: {self.name}")
            print(f"Mobile Number: {self.mobile_number}")
            print(f"Email: {self.email}")
            print(f"Party Size (1-20): {self.party_size}")
            print(f"Accommodations (optional): {self.accommodations}")
            user_input = input("\nSelect [C] Confirm Reservation or [E] Exit: ").lower()
            if user_input == 'c':
                self.make_reservation()
                return "Reservation Created."
            elif user_input == 'e':
                return "Reservation Cancelled."
            else:
                self.message = "Invalid Input. Please try again."

    def make_reservation(self) -> None:
        """
        Saves the reservation details to the database.
        """
        db = Database("./reservations.json")

        new_reservation = {
            "date": self.date,
            "time": self.time,
            "name": self.name,
            "mobile_number": self.mobile_number,
            "email": self.email,
            "party_size": self.party_size,
            "accommodations": self.accommodations
        }

        db.append(new_reservation)