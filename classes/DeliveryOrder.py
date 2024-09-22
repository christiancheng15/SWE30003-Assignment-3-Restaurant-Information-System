from classes.Order import Order
from classes.Menu import Menu


class DeliveryOrder(Order):
    """
    A class to represent a delivery order.

    Attributes
    ----------
    menu : Menu
        An instance of the Menu class representing the menu.
    order_type : str
        The type of the order, which is "Delivery".
    name : str
        The name of the customer.
    mobile_number : str
        The mobile number of the customer.
    email : str
        The email address of the customer.
    address : str
        The delivery address of the customer.
    suburb : str
        The suburb of the delivery address.
    postal_code : str
        The postal code of the delivery address.
    delivery_fee : float
        The delivery fee for the order.

    Methods
    -------
    __init__(menu: Menu):
        Constructs all the necessary attributes for the DeliveryOrder object.
    """

    def __init__(self, menu: Menu):
        """
        Constructs all the necessary attributes for the DeliveryOrder object.

        Parameters
        ----------
        menu : Menu
            An instance of the Menu class representing the menu.
        """
        super().__init__(menu)
        self.order_type = "Delivery"
        self.name = ""
        self.mobile_number = ""
        self.email = ""
        self.address = ""
        self.suburb = ""
        self.postal_code = ""
        self.delivery_fee = 9.99
