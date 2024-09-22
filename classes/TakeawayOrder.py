from classes.Order import Order
from classes.Menu import Menu


class TakeawayOrder(Order):
    """
    A class to represent a takeaway order.

    Attributes
    ----------
    order_type : str
        The type of the order, which is "Takeaway".
    name : str
        The name of the customer.
    mobile_number : str
        The mobile number of the customer.
    email : str
        The email address of the customer.

    Methods
    -------
    __init__(menu: Menu):
        Constructs all the necessary attributes for the TakeawayOrder object.
    """

    def __init__(self, menu: Menu):
        """
        Constructs all the necessary attributes for the TakeawayOrder object.

        Parameters
        ----------
        menu : Menu
            An instance of the Menu class representing the menu.
        """
        super().__init__(menu)
        self.order_type = "Takeaway"
        self.name = ""
        self.mobile_number = ""
        self.email = ""
