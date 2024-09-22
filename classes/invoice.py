from classes.Payment import Payment
from classes.Database import Database
from datetime import datetime


class Invoice:
    """
    A class to represent an invoice.

    Attributes
    ----------
    order_data : dict
        A dictionary containing the order details.

    Methods
    -------
    __init__(payment: Payment):
        Constructs all the necessary attributes for the Invoice object and initializes the order data.
    display_invoice() -> None:
        Displays the invoice details.
    send_to_kds() -> None:
        Sends the order data to the kitchen display system (KDS).
    update_order_history() -> None:
        Updates the order history in the database.
    """

    def __init__(self, payment: Payment):
        """
        Constructs all the necessary attributes for the Invoice object and initializes the order data.

        Parameters
        ----------
        payment : Payment
            An instance of the Payment class containing the payment details.
        """
        self.order_data = {
            "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "order_id": payment.order.order_id,
            "order_type": payment.order.order_type,
            "items": [
                {
                    "id": order_item.menu_item.id,
                    "name": order_item.menu_item.name,
                    "quantity": order_item.quantity,
                    "price": order_item.menu_item.price,
                    "total_price": order_item.calculate_total_price()
                } for order_item in payment.order.order_items
            ],
            "subtotal": payment.order.subtotal,
            "delivery_fee": getattr(payment.order, 'delivery_fee', 0),
            "order_total": payment.order.order_total,
            "payment_info": {
                "card_number": payment.card_number[-4:].rjust(len(payment.card_number), '*'),
                "expiration_date": payment.expiration_date,
                "cvv": payment.cvv,
                "cardholder_name": payment.cardholder_name,
                "note": payment.note
            }
        }

        if payment.order.order_type in ["Takeaway", "Delivery"]:
            self.order_data["contact_information"] = {
                "name": payment.order.name,
                "mobile_number": payment.order.mobile_number,
                "email": payment.order.email
            }
            if payment.order.order_type == "Delivery":
                self.order_data["delivery_address"] = {
                    "address": payment.order.address,
                    "suburb": payment.order.suburb,
                    "postal_code": payment.order.postal_code
                }
        elif payment.order.order_type == "Dine-In":
            self.order_data["table_number"] = payment.order.table_number

        self.send_to_kds()
        self.update_order_history()

    def display_invoice(self) -> None:
        """
        Displays the invoice details.
        """
        print(f"Date Time: {self.order_data['date_time']}")
        print(f"Order ID: {self.order_data['order_id']}")
        print(f"Order Type: {self.order_data['order_type']}\n")
        print("Items:")
        for i, item in enumerate(self.order_data["items"], start=1):
            print(f"\n{i}. {item['name']} - {item['quantity']} x ${item['price']:.2f} = ${item['total_price']:.2f}")
        if self.order_data["delivery_fee"] > 0:
            print(f"\nDelivery Fee: ${self.order_data['delivery_fee']:.2f}")
        print(f"\nSubtotal: ${self.order_data['subtotal']:.2f}")
        print(f"\nOrder Total: ${self.order_data['order_total']:.2f}")
        if self.order_data.get("contact_information"):
            print("\nContact Information:")
            print(f"Name: {self.order_data['contact_information']['name']}")
            print(f"Mobile Number: {self.order_data['contact_information']['mobile_number']}")
            print(f"Email: {self.order_data['contact_information']['email']}")
        if self.order_data.get("delivery_address"):
            print("\nDelivery Address:")
            print(f"Address: {self.order_data['delivery_address']['address']}")
            print(f"Suburb: {self.order_data['delivery_address']['suburb']}")
            print(f"Postal Code: {self.order_data['delivery_address']['postal_code']}")
        if self.order_data.get("table_number"):
            print(f"\nTable Number: {self.order_data['table_number']}")
        print(f"\nNote: {self.order_data['payment_info']['note']}")
        print(f"\n[SYSTEM] A copy of your receipt has been sent to your email")
        input("\nPress ENTER to continue")

    def send_to_kds(self) -> None:
        """
        Sends the order data to the kitchen display system (KDS).
        """
        db = Database(f"./invoices/{self.order_data['order_id']}.txt")
        db.write(self.order_data)

    def update_order_history(self) -> None:
        """
        Updates the order history in the database.
        """
        db = Database("./order_history.json")
        db.append(self.order_data)