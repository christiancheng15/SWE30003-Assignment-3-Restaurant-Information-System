from classes.Menu import Menu
from classes.OrderItem import OrderItem
from uuid import uuid4


class Order:
    """
    A class to represent an order.

    Attributes
    ----------
    menu : Menu
        An instance of the Menu class representing the menu.
    order_id : str
        The unique identifier for the order.
    order_items : list
        A list of OrderItem objects representing the items in the order.
    subtotal : float
        The subtotal amount of the order.
    order_total : float
        The total amount of the order, including any additional fees.

    Methods
    -------
    __init__(menu: Menu):
        Constructs all the necessary attributes for the Order object.
    add_item(item_index: int, quantity: int) -> None:
        Adds an item to the order.
    calculate_totals() -> None:
        Calculates the subtotal and total amounts for the order.
    display_order() -> str:
        Displays the order details.
    """

    def __init__(self, menu: Menu):
        """
        Constructs all the necessary attributes for the Order object.

        Parameters
        ----------
        menu : Menu
            An instance of the Menu class representing the menu.
        """
        self.menu = menu
        self.order_id = str(uuid4())
        self.order_items = []
        self.subtotal = 0
        self.order_total = 0

    def add_item(self, item_index: int, quantity: int) -> None:
        """
        Adds an item to the order.

        Parameters
        ----------
        item_index : int
            The index of the item in the menu to be added to the order.
        quantity : int
            The quantity of the item to be added.
        """
        menu_item = self.menu[item_index - 1]
        order_item = next((item for item in self.order_items if item.menu_item == menu_item), None)
        if order_item:
            order_item.quantity += quantity
        else:
            self.order_items.append(OrderItem(menu_item, quantity))

    def calculate_totals(self) -> None:
        """
        Calculates the subtotal and total amounts for the order.
        """
        self.subtotal = sum(item.calculate_total_price() for item in self.order_items)
        self.order_total = self.subtotal
        if hasattr(self, 'order_type') and self.order_type == "Delivery":
            self.order_total += self.delivery_fee

        self.subtotal = round(self.subtotal, 2)
        self.order_total = round(self.order_total, 2)

    def display_order(self) -> str:
        """
        Displays the order details.

        Returns
        -------
        str
            The string representation of the order details.
        """
        print(f"Order Type: {self.order_type}\n")
        print(f"Order ID: {self.order_id}\n")
        
        if self.order_items:
            print("Your Order:")
            for i, order_item in enumerate(self.order_items, start=1):
                item_total = order_item.calculate_total_price()
                print(f"\n{i}. {order_item.menu_item.name} - {order_item.quantity} x ${order_item.menu_item.price:.2f} = ${item_total:.2f}")
        else:
            print("Your order is empty.")

        self.calculate_totals()

        if hasattr(self, 'order_type') and self.order_type == "Delivery":
            print(f"\nDelivery Fee: ${self.delivery_fee:.2f}")

        print(f"\nSubtotal: ${self.subtotal:.2f}")
        print(f"Order Total: ${self.order_total:.2f}")
