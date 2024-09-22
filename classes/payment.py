from classes.SystemUtils import SystemUtils
from classes.Order import Order
from classes.Validator import Validator


class Payment:
    """
    A class to handle payment processing for an order.

    Attributes
    ----------
    order : Order
        An instance of the Order class representing the current order.
    message : str
        A message to display to the user.
    card_number : str
        The credit card number for payment.
    expiration_date : str
        The expiration date of the credit card.
    cvv : str
        The CVV of the credit card.
    cardholder_name : str
        The name of the cardholder.
    note : str
        Any additional notes for the order.

    Methods
    -------
    enter_payment_details() -> None:
        Prompts the user to enter payment details.
    finalize_payment() -> bool:
        Finalizes the payment process.
    is_payment_info_complete() -> bool:
        Checks if the payment information is complete.
    """

    def __init__(self, order: Order):
        """
        Constructs all the necessary attributes for the Payment object.

        Parameters
        ----------
        order : Order
            An instance of the Order class representing the current order.
        """
        self.order = order
        self.message = ""
        self.card_number = ""
        self.expiration_date = ""
        self.cvv = ""
        self.cardholder_name = ""
        self.note = ""

    def enter_payment_details(self) -> bool:
        """
        Prompts the user to enter payment details.

        Returns
        -------
        bool
            True if payment details are successfully entered, False if the process is exited.
        """
        while not self.is_payment_info_complete():
            SystemUtils.clear_screen()
            SystemUtils.heading("PAYMENT PROCESSING")
            print("Complete your order. Enter [E] to Exit Anytime.:\n")
            self.message = SystemUtils.display_message(self.message)

            print("Payment Method:")

            if not self.card_number:
                temp = input("Card Number: ")
                if temp.lower() == 'e':
                    return False
                if Validator.validate_card_number(temp):
                    self.card_number = temp
                else:
                    self.message = "Invalid Input. Card number invalid."
                continue
            else:
                print(f"Card Number: {self.card_number}")

            if not self.expiration_date:
                temp = input("Expiration Date (MM/YY): ")
                if temp.lower() == 'e':
                    return False
                if Validator.validate_expiration_date(temp):
                    self.expiration_date = temp
                else:
                    self.message = "Invalid Input. Date invalid."
                continue
            else:
                print(f"Expiration Date: {self.expiration_date}")

            if not self.cvv:
                temp = input("CVV: ")
                if temp.lower() == 'e':
                    return False
                if Validator.validate_cvv(temp):
                    self.cvv = temp
                else:
                    self.message = "Invalid Input. CVV invalid."
                continue
            else:
                print(f"CVV: {self.cvv}")

            if not self.cardholder_name:
                temp = input("Cardholder Name: ")
                if temp.lower() == 'e':
                    return False
                if Validator.validate_name(temp):
                    self.cardholder_name = ' '.join(temp.title().split())
                else:
                    self.message = "Invalid Input. Name must contain only letters and spaces."
                continue
            else:
                print(f"Cardholder Name: {self.cardholder_name}")

            if self.order.order_type in ['Takeaway', 'Delivery']:
                print("\nContact Information")
                if not self.order.name:
                    temp = input("Name: ")
                    if temp.lower() == 'e':
                        return False
                    if Validator.validate_name(temp):
                        self.order.name = ' '.join(temp.title().split())
                    else:
                        self.message = "Invalid Input. Name must contain only letters and spaces."
                    continue
                else:
                    print(f"Name: {self.order.name}")

                if not self.order.mobile_number:
                    temp = input("Mobile Number: ")
                    if temp.lower() == 'e':
                        return False
                    if Validator.validate_mobile_number(temp):
                        self.order.mobile_number = temp
                    else:
                        self.message = "Invalid Input. Mobile number must start with 04 and only contain 10 digits."
                    continue
                else:
                    print(f"Mobile Number: {self.order.mobile_number}")

                if not self.order.email:
                    temp = input("Email: ")
                    if temp.lower() == 'e':
                        return False
                    if Validator.validate_email(temp):
                        self.order.email = temp
                    else:
                        self.message = "Invalid Input. Email must be valid."
                    continue
                else:
                    print(f"Email: {self.order.email}")

                if self.order.order_type == "Delivery":
                    if not self.order.address:
                        temp = input("Address: ")
                        if temp.lower() == 'e':
                            return False
                        if temp.strip():
                            self.order.address = temp.strip().title()
                        else:
                            self.message = "Invalid Input. Address cannot be empty."
                        continue
                    else:
                        print(f"Address: {self.order.address}")

                    if not self.order.suburb:
                        temp = input("Suburb: ")
                        if temp.lower() == 'e':
                            return False
                        if temp.strip():
                            self.order.suburb = temp.strip().title()
                        else:
                            self.message = "Invalid Input. Suburb cannot be empty."
                        continue
                    else:
                        print(f"Suburb: {self.order.suburb}")

                    if not self.order.postal_code:
                        temp = input("Postal Code: ")
                        if temp.lower() == 'e':
                            return False
                        if Validator.validate_postal_code(temp):
                            self.order.postal_code = temp
                        else:
                            self.message = "Invalid Input. Postal code must be 4 digits."
                        continue
                    else:
                        print(f"Postal Code: {self.order.postal_code}")
            else:
                print("\nTable Information:")
                if not self.order.table_number:
                    temp = input("Table Number: ")
                    if temp.lower() == 'e':
                        return False
                    if Validator.validate_table_number(temp):
                        self.order.table_number = temp
                    else:
                        self.message = "Invalid Input. Please enter a valid table number (1-100)."
                    continue
                else:
                    print(f"Table Number: {self.order.table_number}")

        self.note = input("Note (if any): ")
        return True

    def finalize_payment(self) -> bool:
        """
        Finalizes the payment process.

        Returns
        -------
        bool
            True if payment is successful, False if the process is exited.
        """
        while True:
            SystemUtils.clear_screen()
            self.message = SystemUtils.display_message(self.message)

            SystemUtils.heading("PAYMENT PROCESSING")

            self.order.display_order()

            print("Complete your order:")
            print(f"\nPayment Method (Credit Card)")
            print(f"Card Number: {self.card_number[-4:].rjust(len(self.card_number), '*')}")
            print(f"Expiration Date: {self.expiration_date}")
            print(f"CVV: {self.cvv}")
            print(f"Cardholder Name: {self.cardholder_name}")

            if self.order.order_type in ['Takeaway', 'Delivery']:
                print("\nContact Information")
                print(f"Name: {self.order.name}")
                print(f"Mobile Number: {self.order.mobile_number}")
                print(f"Email: {self.order.email}")
                if self.order.order_type == "Delivery":
                    print(f"Address: {self.order.address}")
                    print(f"Suburb: {self.order.suburb}")
                    print(f"Postal Code: {self.order.postal_code}")
            else:
                print(f"Table Number: {self.order.table_number}")

            print(f"Note: {self.note}")
            print(f"\nPayment Policy")
            print("All sales are final. No refunds will be issued after payment.\n")
            user_input = input("Enter [P] to Pay or [E] to Exit: ").lower()
            if user_input == 'p':
                print("\nPayment Success.")
                return True
            elif user_input == 'e':
                print("\nPayment Aborted.")
                return False
            else:
                self.message = "Invalid Input. Please try again."

    def is_payment_info_complete(self) -> bool:
        """
        Checks if the payment information is complete.

        Returns
        -------
        bool
            True if payment information is complete, False otherwise.
        """
        if self.order.order_type == "Delivery":
            return all([
                self.card_number, self.expiration_date, self.cvv, self.cardholder_name,
                self.order.name, self.order.mobile_number, self.order.email,
                self.order.address, self.order.suburb, self.order.postal_code
            ])
        elif self.order.order_type == "Takeaway":
            return all([
                self.card_number, self.expiration_date, self.cvv, self.cardholder_name,
                self.order.name, self.order.mobile_number, self.order.email
            ])
        else:
            return all([
                self.card_number, self.expiration_date, self.cvv, self.cardholder_name,
                self.order.table_number
            ])