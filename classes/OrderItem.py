from classes.MenuItem import MenuItem


class OrderItem:
    """
    A class to represent an order item.

    Attributes
    ----------
    menu_item : MenuItem
        An instance of the MenuItem class representing the item in the menu.
    quantity : int
        The quantity of the menu item in the order.

    Methods
    -------
    calculate_total_price() -> float:
        Calculates and returns the total price for the order item.
    """

    def __init__(self, menu_item: MenuItem, quantity: int):
        """
        Constructs all the necessary attributes for the OrderItem object.

        Parameters
        ----------
        menu_item : MenuItem
            An instance of the MenuItem class representing the item in the menu.
        quantity : int
            The quantity of the menu item in the order.
        """
        self.menu_item = menu_item
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Calculates and returns the total price for the order item.

        Returns
        -------
        float
            The total price for the order item.
        """
        return round(self.menu_item.price * self.quantity, 2)