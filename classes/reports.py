from classes.Database import Database
from datetime import datetime
from tabulate import tabulate
from collections import Counter

class Reports:
    """
    A class to generate and display reports for sales and reservations.

    Attributes
    ----------
    order_history_file : str
        The file path for the order history data.
    reservations_file : str
        The file path for the reservations data.

    Methods
    -------
    display_sales() -> None:
        Displays the sales report from specified date.
    display_menuitems() -> None:
        Displays the sold menu item report from specified date.
    display_reservations() -> None:
        Displays the reservations report.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the Reports object.
        """
        self.order_history_file = "./order_history.json"
        self.reservations_file = "./reservations.json"

    def display_sales(self, on_date: str) -> None:
        """
        Displays the sales report on specified date.
        """
        db = Database(self.order_history_file)
        sales = db.read()

        if not sales:
            print("No sales found.")
            return

        for sale in sales:
            sale['datetime'] = datetime.strptime(sale['date_time'], "%Y-%m-%d %H:%M:%S")

        sorted_sales = sorted(sales, key=lambda x: x['datetime'])

        on_date_dt = datetime.strptime(on_date, "%d/%m/%Y").date()

        # logic to show data only if it equals to input date
        filtered_sales = []
        for sale in sales:
            sale_datetime = datetime.strptime(sale['date_time'], "%Y-%m-%d %H:%M:%S")
            sale_date = sale_datetime.date()
            if sale_date == on_date_dt:
                sale['datetime'] = sale_datetime
                filtered_sales.append(sale)

        if not filtered_sales:
            print(f"No sales found on {on_date}.")
            return

        sorted_sales = sorted(filtered_sales, key=lambda x: x['datetime'])

        table_data = []
        for sale in sorted_sales:
            items_str = "\n".join([
                f"{item['name']} (x{item['quantity']}) - ${item['total_price']:.2f}"
                for item in sale['items']
            ])
            if sale.get('delivery_fee', 0) > 0:
                items_str += f"\nDelivery Fee - ${sale['delivery_fee']:.2f}"
            table_data.append([
                sale['date_time'],
                sale['order_id'],
                sale['order_type'],
                items_str,
                f"${sale['order_total']:.2f}"
            ])

        headers = ["Date Time", "Order ID", "Order Type", "Items", "Order Total"]

        print(tabulate(table_data, headers, tablefmt="grid"))

    def display_menuitems(self, on_date: str) -> None:
        """
        Displays the total sold quantity of each menu item ordered from specific date
        """
        db = Database(self.order_history_file)
        sales = db.read()

        if not sales:
            print("No sales found.")
            return

        item_counter = Counter()
        on_date_dt = datetime.strptime(on_date, "%d/%m/%Y").date()
        
        for sale in sales:
            sale_date = datetime.strptime(sale['date_time'], "%Y-%m-%d %H:%M:%S").date()
            if sale_date == on_date_dt:
                for item in sale['items']:
                    item_counter[item['name']] += item['quantity']

        if not item_counter:
            print("No menu items sold on " + on_date)
            return

        table_data = [
            [item_name, quantity]
            for item_name, quantity in item_counter.items()
        ]

        headers = ["Item Name", "Quantity Ordered"]

        print(tabulate(table_data, headers, tablefmt="grid"))

    def display_reservations(self) -> None:
        """
        Displays the reservations report.
        """
        db = Database(self.reservations_file)
        reservations = db.read()

        if not reservations:
            print("No reservations found.")
            return

        current_datetime = datetime.now()

        for reservation in reservations:
            reservation['datetime'] = datetime.strptime(
                f"{reservation['date']} {reservation['time']}", "%d/%m/%Y %H:%M"
            )

        future_reservations = [r for r in reservations if r['datetime'] >= current_datetime]

        sorted_reservations = sorted(future_reservations, key=lambda x: x['datetime'])

        table_data = []
        for reservation in sorted_reservations:
            table_data.append([
                reservation['date'],
                reservation['time'],
                reservation['name'],
                reservation['mobile_number'],
                reservation['email'],
                reservation['party_size'],
                reservation['accommodations'] if reservation['accommodations'] else "None"
            ])

        headers = ["Date", "Time", "Name", "Mobile Number", "Email", "Party Size", "Accommodations"]

        print(tabulate(table_data, headers, tablefmt="grid"))