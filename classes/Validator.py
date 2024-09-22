import re
from datetime import datetime
from classes.LuhnAlgorithm import LuhnAlgorithm


class Validator:
    """
    A class to provide various validation methods.

    Methods
    -------
    validate_name(name: str) -> bool:
        Validates that the name contains only letters and spaces.
    validate_date(date_str: str, date_format: str = "%d/%m/%Y") -> bool:
        Validates that is in the specified format.
    validate_future_date(date_str: str, date_format: str = "%d/%m/%Y") -> bool:
        Validates that the date is in the future and in the specified format.
    validate_time(time_str: str, start_time: str = "09:00", end_time: str = "21:00") -> bool:
        Validates that the time is within the specified range.
    validate_mobile_number(mobile_number: str) -> bool:
        Validates that the mobile number starts with 04 and has 10 digits.
    validate_email(email: str) -> bool:
        Validates that the email is in the correct format.
    validate_card_number(card_number: str) -> bool:
        Validates that the card number is valid using the Luhn Algorithm.
    validate_expiration_date(date_str: str, date_format: str = "%m/%y") -> bool:
        Validates that the expiration date is in the future.
    validate_cvv(cvv: str) -> bool:
        Validates that the CVV has 3 or 4 digits.
    validate_postal_code(postal_code: str) -> bool:
        Validates that the postal code has 4 digits.
    validate_table_number(table_number: str) -> bool:
        Validates that the table number is between 1 and 100.
    validate_party_size(party_size: str) -> bool:
        Validates that the party size is between 1 and 20.
    """

    @staticmethod
    def validate_name(name: str) -> bool:
        """
        Validates that the name contains only letters and spaces.

        Parameters
        ----------
        name : str
            The name to be validated.

        Returns
        -------
        bool
            True if the name is valid, False otherwise.
        """
        return bool(re.match(r"^[A-Za-z\s]+$", name))

    @staticmethod
    def validate_date(date_str: str, date_format: str = "%d/%m/%Y") -> bool:
        """
        Validates that the date is in the future and in the specified format.

        Parameters
        ----------
        date_str : str
            The date string to be validated.
        date_format : str, optional
            The format of the date string (default is "%d/%m/%Y").

        Returns
        -------
        bool
            True if the date is valid, False otherwise.
        """
        try:
            datetime.strptime(date_str, date_format).date()
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_future_date(date_str: str, date_format: str = "%d/%m/%Y") -> bool:
        """
        Validates that the date is in the future and in the specified format.

        Parameters
        ----------
        date_str : str
            The date string to be validated.
        date_format : str, optional
            The format of the date string (default is "%d/%m/%Y").

        Returns
        -------
        bool
            True if the date is valid and in the future, False otherwise.
        """
        try:
            date_obj = datetime.strptime(date_str, date_format).date()
            return date_obj > datetime.today().date()
        except ValueError:
            return False

    @staticmethod
    def validate_time(time_str: str, start_time: str = "09:00", end_time: str = "21:00") -> bool:
        """
        Validates that the time is within the specified range.

        Parameters
        ----------
        time_str : str
            The time string to be validated.
        start_time : str, optional
            The start of the valid time range (default is "09:00").
        end_time : str, optional
            The end of the valid time range (default is "21:00").

        Returns
        -------
        bool
            True if the time is within the range, False otherwise.
        """
        try:
            time_obj = datetime.strptime(time_str, '%H:%M').time()
            start = datetime.strptime(start_time, '%H:%M').time()
            end = datetime.strptime(end_time, '%H:%M').time()
            return start <= time_obj <= end and time_obj
        except ValueError:
            return False

    @staticmethod
    def validate_mobile_number(mobile_number: str) -> bool:
        """
        Validates that the mobile number starts with 04 and has 10 digits.

        Parameters
        ----------
        mobile_number : str
            The mobile number to be validated.

        Returns
        -------
        bool
            True if the mobile number is valid, False otherwise.
        """
        return bool(re.match(r"^04\d{8}$", mobile_number))

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validates that the email is in the correct format.

        Parameters
        ----------
        email : str
            The email to be validated.

        Returns
        -------
        bool
            True if the email is valid, False otherwise.
        """
        return bool(re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email))

    @staticmethod
    def validate_card_number(card_number: str) -> bool:
        """
        Validates that the card number is valid using the Luhn Algorithm.

        Parameters
        ----------
        card_number : str
            The card number to be validated.

        Returns
        -------
        bool
            True if the card number is valid, False otherwise.
        """
        return LuhnAlgorithm.checksum(card_number)

    @staticmethod
    def validate_expiration_date(date_str: str, date_format: str = "%m/%y") -> bool:
        """
        Validates that the expiration date is in the future.

        Parameters
        ----------
        date_str : str
            The expiration date string to be validated.
        date_format : str, optional
            The format of the expiration date string (default is "%m/%y").

        Returns
        -------
        bool
            True if the expiration date is valid and in the future, False otherwise.
        """
        try:
            exp_date = datetime.strptime(date_str, date_format)
            return exp_date > datetime.now()
        except ValueError:
            return False

    @staticmethod
    def validate_cvv(cvv: str) -> bool:
        """
        Validates that the CVV has 3 or 4 digits.

        Parameters
        ----------
        cvv : str
            The CVV to be validated.

        Returns
        -------
        bool
            True if the CVV is valid, False otherwise.
        """
        return bool(re.match(r"^\d{3,4}$", cvv))

    @staticmethod
    def validate_postal_code(postal_code: str) -> bool:
        """
        Validates that the postal code has 4 digits.

        Parameters
        ----------
        postal_code : str
            The postal code to be validated.

        Returns
        -------
        bool
            True if the postal code is valid, False otherwise.
        """
        return bool(re.match(r"^\d{4}$", postal_code))

    @staticmethod
    def validate_table_number(table_number: str) -> bool:
        """
        Validates that the table number is between 1 and 100.

        Parameters
        ----------
        table_number : str
            The table number to be validated.

        Returns
        -------
        bool
            True if the table number is valid, False otherwise.
        """
        return table_number.isdigit() and 1 <= int(table_number) <= 100

    @staticmethod
    def validate_party_size(party_size: str) -> bool:
        """
        Validates that the party size is between 1 and 20.

        Parameters
        ----------
        party_size : str
            The party size to be validated.

        Returns
        -------
        bool
            True if the party size is valid, False otherwise.
        """
        return party_size.isnumeric() and 1 <= int(party_size) <= 20