from classes.SystemUtils import SystemUtils
from classes.OrderFactory import OrderFactory
from classes.Order import Order
from classes.PaymentHandler import PaymentHandler
from classes.Menu import Menu


class OrderHandler:
    """
    A class to handle order-related operations.

    Methods
    -------
    handle_order(menu: Menu) -> None:
        Handles the process of creating and managing an order.
    select_order_type() -> str:
        Displays the order type selection menu and returns the selected option.
    add_items_to_order(order: Order, menu: Menu) -> str:
        Adds items to the order from the menu.
    remove_items_from_order(order: Order) -> str:
        Removes items from the order.
    display_order(order: Order) -> str:
        Displays the order and handles user interaction for removing items, paying, or going back.
    """

    @staticmethod
    def handle_order(menu: Menu) -> None:
        """
        Handles the process of creating and managing an order.

        Parameters
        ----------
        menu : Menu
            An instance of the Menu class representing the menu.
        """
        order_type = OrderHandler.select_order_type()
        if not order_type:
            return
        
        order = OrderFactory.create_order(order_type, menu)
        while True:
            status = OrderHandler.add_items_to_order(order, menu)
            if status == 'v':
                status = OrderHandler.display_order(order)
                if status == 'p':
                    PaymentHandler.process_payment(order)
                    break
                elif status == 'b':
                    continue
                else:
                    break
            else:
                break

    @staticmethod
    def select_order_type() -> str:
        """
        Displays the order type selection menu and returns the selected option.

        Returns
        -------
        str
            The selected order type ('1' for Dine-In, '2' for Takeaway, '3' for Delivery) or None to exit.
        """
        message = ""
        while True:
            SystemUtils.clear_screen()
            SystemUtils.display_message(message)
            SystemUtils.heading("Ordering")
            print("Select an order type:\n")
            print("[1] Dine-In\n")
            print("[2] Takeaway\n")
            print("[3] Delivery\n")
            print("[E] Exit\n")
            temp = input("Select an option: ").lower()

            if temp == 'e':
                return None

            if temp in ['1', '2', '3']:
                return temp

            message = "[ERROR] Please enter a valid option."

    @staticmethod
    def add_items_to_order(order: Order, menu: Menu) -> str:
        """
        Adds items to the order from the menu.

        Parameters
        ----------
        order : Order
            An instance of the Order class representing the current order.
        menu : Menu
            An instance of the Menu class representing the menu.

        Returns
        -------
        str
            'v' to view cart, 'e' to exit, or 'b' to go back.
        """
        message = ""
        while True:
            SystemUtils.clear_screen()
            SystemUtils.display_message(message)
            SystemUtils.heading("ORDERING")
            menu.display_menu()
            print("[V] View Cart        [E] Exit\n")
            user_input = input("Select an option: ").lower()
            if user_input == 'v':
                return 'v'
            elif user_input == 'e':
                return 'e'
            elif user_input.isdigit() and 1 <= int(user_input) <= len(menu):
                quantity = input("Quantity: ")
                if quantity.isdigit() and int(quantity) > 0:
                    order.add_item(int(user_input), int(quantity))
                else:
                    message = "[ERROR] Please enter a valid quantity."
            else:
                message = "[ERROR] Please enter a valid menu item number."

    @staticmethod
    def remove_items_from_order(order: Order) -> str:
        """
        Removes items from the order.

        Parameters
        ----------
        order : Order
            An instance of the Order class representing the current order.

        Returns
        -------
        str
            A system message indicating the result of the removal operation.
        """
        user_input = input("\nEnter the item number to remove or [E] Exit: ").lower()
        if user_input == 'e':
            return
        elif user_input.isdigit() and 1 <= int(user_input) <= len(order.order_items):
            item_index = int(user_input) - 1
            item = order.order_items[item_index]
            quantity_to_remove = input(f"Enter the quantity to remove (max {item.quantity}): ")
            if quantity_to_remove.isdigit() and 1 <= int(quantity_to_remove) <= item.quantity:
                quantity_to_remove = int(quantity_to_remove)
                item.quantity -= quantity_to_remove
                if item.quantity == 0:
                    order.order_items.pop(item_index)
                return f"[SYSTEM] {item.menu_item.name} (x{quantity_to_remove}) Removed"
            else:
                return "[ERROR] Please enter a valid quantity."
        else:
            return "[ERROR] Please enter a valid item number."

    @staticmethod
    def display_order(order: Order) -> str:
        """
        Displays the order and handles user interaction for removing items, paying, or going back.

        Parameters
        ----------
        order : Order
            An instance of the Order class representing the current order.

        Returns
        -------
        str
            'r' to remove items, 'p' to pay, 'b' to go back, or 'e' to exit.
        """
        message = ""
        while True:
            SystemUtils.clear_screen()
            SystemUtils.display_message(message)
            SystemUtils.heading("ORDERING")
            order.display_order()
            print("\n[R] Remove Item        [P] Pay        [B] Back        [E] Exit\n")
            user_input = input("Select an option: ").lower()
            if user_input == 'r':
                if order.order_items:
                    message = OrderHandler.remove_items_from_order(order)
                else:
                    message = "[ERROR] Your order is empty."
            elif user_input == 'p':
                if order.order_items:
                    return 'p'
                message = "[ERROR] Your order is empty."
            elif user_input == 'b':
                return 'b'
            elif user_input == 'e':
                return 'e'
            else:
                message = "[ERROR] Please enter a valid option."