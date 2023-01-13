from datetime import datetime
from flight import Flight
from passenger import Operator, Passenger
from seat import Seat


class Reservation:
    def __init__(self, passenger: Passenger, operator: Operator, flight: Flight, seat: Seat) -> None:
        self.__passenger = passenger
        self.__operator = operator
        self.__flight = flight
        self.__seat = seat
        self.__id = f"{self.__flight.departure_date.strftime('%d%m%Y%')}{self.__seat.id}"
        self.__createdAt = datetime.now()

    def __str__(self):
        if self.__id is None:
            raise ValueError("Reservation yet to be created")

        return f"Created at: {self.__createdAt.strftime('%d/%m/%Y')}\nID: {self.__id}\nCreated by {self.__operator.name} for {self.__passenger.name}"
        
