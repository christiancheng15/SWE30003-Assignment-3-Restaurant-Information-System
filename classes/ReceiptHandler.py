from classes.SystemUtils import SystemUtils
from classes.Invoice import Invoice


class ReceiptHandler:
    """
    A class to handle receipt-related operations.

    Methods
    -------
    handle_receipt(invoice: Invoice) -> None:
        Prompts the user to print the receipt and displays it if requested.
    """

    @staticmethod
    def handle_receipt(invoice: Invoice) -> None:
        """
        Prompts the user to print the receipt and displays it if requested.

        Parameters
        ----------
        invoice : Invoice
            An instance of the Invoice class representing the current invoice.
        """
        while True:
            user_input = input("\nWould you like to print your receipt? (Y/N): ").lower()
            if user_input == 'y':
                SystemUtils.clear_screen()
                invoice.display_invoice()
                return
            elif user_input == 'n':
                break