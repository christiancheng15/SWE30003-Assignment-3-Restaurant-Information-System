from classes.Payment import Payment
from classes.Invoice import Invoice
from classes.ReceiptHandler import ReceiptHandler
from classes.Order import Order


class PaymentHandler:
    """
    A class to handle the payment process for an order.

    Methods
    -------
    process_payment(order: Order) -> None:
        Processes the payment for the given order.
    """

    @staticmethod
    def process_payment(order: Order) -> None:
        """
        Processes the payment for the given order.

        Parameters
        ----------
        order : Order
            An instance of the Order class representing the current order.
        """
        payment = Payment(order)
        if payment.enter_payment_details():
            if payment.finalize_payment():
                invoice = Invoice(payment)
                ReceiptHandler.handle_receipt(invoice)
            else:
                print("Payment Cancelled.")
        else:
            print("Payment Cancelled.")
