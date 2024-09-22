class MenuItem:
    """
    A class to represent a menu item.

    Attributes
    ----------
    id : int
        The unique identifier for the menu item.
    name : str
        The name of the menu item.
    description : str
        The description of the menu item.
    price : float
        The price of the menu item.
    category : str
        The category of the menu item.
    availability : bool
        The availability status of the menu item.
    active : bool
        The active status of the menu item.

    Methods
    -------
    __init__(id: int, name: str, description: str, price: float, category: str, availability: bool, active: bool):
        Constructs all the necessary attributes for the MenuItem object.
    """

    def __init__(self, id: int, name: str, description: str, price: float, category: str, availability: bool, active: bool):
        """
        Constructs all the necessary attributes for the MenuItem object.

        Parameters
        ----------
        id : int
            The unique identifier for the menu item.
        name : str
            The name of the menu item.
        description : str
            The description of the menu item.
        price : float
            The price of the menu item.
        category : str
            The category of the menu item.
        availability : bool
            The availability status of the menu item.
        active : bool
            The active status of the menu item.
        """
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.availability = availability
        self.active = active
