from classes.Menu import Menu
from classes.DineInOrder import DineInOrder
from classes.TakeawayOrder import TakeawayOrder
from classes.DeliveryOrder import DeliveryOrder
from classes.Order import Order


class OrderFactory:
    """
    A factory class to create different types of orders.

    Methods
    -------
    create_order(order_type: str, menu: Menu) -> Order:
        Creates and returns an order based on the specified type.
    """

    @staticmethod
    def create_order(order_type: str, menu: Menu) -> Order:
        """
        Creates and returns an order based on the specified type.

        Parameters
        ----------
        order_type : str
            The type of order to be created. ('1' for Dine-In, '2' for Takeaway, '3' for Delivery)
        menu : Menu
            An instance of the Menu class representing the menu.

        Returns
        -------
        Order
            An instance of the appropriate Order subclass.

        Raises
        ------
        ValueError
            If an invalid order type is provided.
        """
        if order_type == '1':
            return DineInOrder(menu)
        elif order_type == '2':
            return TakeawayOrder(menu)
        elif order_type == '3':
            return DeliveryOrder(menu)
        else:
            raise ValueError("Invalid order type")
