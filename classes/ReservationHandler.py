from classes.Reservation import Reservation


class ReservationHandler:
    """
    A class to handle reservation-related operations.

    Methods
    -------
    handle_reservation() -> None:
        Handles the process of creating a reservation.
    """

    @staticmethod
    def handle_reservation() -> None:
        """
        Handles the process of creating a reservation.
        """
        reservation = Reservation()
        if reservation.enter_reservation_details():
            reservation.confirm_reservation()
        else:
            print("Reservation Cancelled.")
