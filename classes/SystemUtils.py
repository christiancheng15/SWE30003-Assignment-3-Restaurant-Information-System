import os

class SystemUtils:
    """
    A utility class for system-related functions.

    Methods
    -------
    clear_screen() -> None:
        Clears the console screen.
    display_message(message: str) -> None:
        Displays a message if it is not empty.
    divider() -> None:
        Prints a divider line.
    """

    @staticmethod
    def clear_screen() -> None:
        """
        Clears the console screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def display_message(message: str) -> None:
        """
        Displays a message if it is not empty.

        Parameters
        ----------
        message : str
            The message to be displayed.
        """
        if message:
            print(f"{message}\n")

    @staticmethod
    def divider() -> None:
        """
        Prints a divider line.
        """
        print("--------------------------------------------------")

    @staticmethod
    def heading(string: str) -> None:
        """
        Prints a header
        """
        print("--------------------------------------------------")
        print(string.center(50))
        print("--------------------------------------------------\n")

    @staticmethod
    def shutdown() -> None:
        from classes.PinValidator import PinValidator
        message = ""
        while True:
            SystemUtils.clear_screen()
            SystemUtils.display_message(message)
            SystemUtils.heading("SYSTEM SHUTDOWN CONFIRMATION")
            print("You are about to shut down the system.")
            user_input = input("Are you sure you want to proceed? (y/n): ").lower()
            
            if user_input == 'y':
                if PinValidator.check_pin():
                    print
                    exit()
            elif user_input == 'n':
                return
            else:
                message = "[ERROR] Please select a valid option."

    @staticmethod
    def koala() -> None:
        """
        Prints an ascii koala
       ||༢ 
   ʕ•ᴥ•ʔ   The
  o(____⊃  Relaxing
      ୧||  Koala
        """
        print("""\
       ||༢ 
   ʕ•ᴥ•ʔ   The
  o(____⊃  Relaxing
      ୧||  Koala
            """)