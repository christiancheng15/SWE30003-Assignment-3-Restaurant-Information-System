from classes.Order import Order
from classes.Menu import Menu


class DineInOrder(Order):
    """
    A class to represent a dine-in order.

    Attributes
    ----------
    menu : Menu
        An instance of the Menu class representing the menu.
    order_type : str
        The type of the order, which is "Dine-In".
    table_number : str
        The table number for the dine-in order.

    Methods
    -------
    __init__(menu: Menu):
        Constructs all the necessary attributes for the DineInOrder object.
    """

    def __init__(self, menu: Menu):
        """
        Constructs all the necessary attributes for the DineInOrder object.

        Parameters
        ----------
        menu : Menu
            An instance of the Menu class representing the menu.
        """
        super().__init__(menu)
        self.order_type = "Dine-In"
        self.table_number = ""
