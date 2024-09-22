class LuhnAlgorithm:
    """
    A class to represent the Luhn Algorithm for validating credit card numbers.

    Methods
    -------
    checksum(card_number: str) -> bool:
        Validates the given credit card number using the Luhn Algorithm.
    """

    @staticmethod
    def checksum(card_number: str) -> bool:
        """
        Validates the given credit card number using the Luhn Algorithm.

        Parameters
        ----------
        card_number : str
            The credit card number to be validated.

        Returns
        -------
        bool
            True if the credit card number is valid, False otherwise.
        """
        def digits_of(n):
            """
            Converts a number into a list of its digits.

            Parameters
            ----------
            n : int
                The number to be converted into digits.

            Returns
            -------
            list
                A list of digits.
            """
            return [int(d) for d in str(n)]

        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10 == 0
