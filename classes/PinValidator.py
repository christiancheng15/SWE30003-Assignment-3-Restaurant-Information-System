class PinValidator:
    """
    A class to validate a PIN.

    Methods
    -------
    check_pin(correct_pin: str) -> bool:
        Checks if the entered PIN matches the correct PIN.
    """

    @staticmethod
    def check_pin() -> bool:
        """
        Checks if the entered PIN matches the correct PIN.

        Parameters
        ----------
        correct_pin : str
            The correct PIN to be validated against.

        Returns
        -------
        bool
            True if the entered PIN is correct, False otherwise.
        """
        PIN_CODE = "1234"
        user_input = input("PIN: ")
        if user_input == PIN_CODE:
            return True
        else:
            print("Invalid PIN.")
            return False
