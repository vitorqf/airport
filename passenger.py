from flight import Flight
from person import Person


class Passenger(Person):
    def __init__(self, name, flight: Flight) -> None:
        super().__init__(name, __class__.__name__)
        self.__flight = flight

    @property
    def flight(self) -> Flight:
        return self.__flight

    @flight.setter
    def flight(self, value: Flight) -> None:
        self.__flight = value

    def __str__(self) -> str:
        return f"Name: {self.__name}"

class Operator(Person):
    def __init__(self, name, flight: Flight) -> None:
        super().__init__(name, __class__.__name__)
        self.__flight = flight

    """
    Checks whether the 
    @param seat 
    is currently available in the flight, if ==true then reservation is possible.
    """
    def create(self, passenger, seat) -> None:
        if self.__flight.seats[seat].owner != 'Not owned':
            raise ValueError('Seat is busy!')

        self.__flight.seats[seat].owner = passenger.name
        self.__flight.seats[seat].status = 'Busy'

    """
    Checks whether the 
    @param seat 
    is currently busy in the flight, if ==true then cancelling is possible.
    """
    def cancel(self, seat) -> None:
        if self.__flight.seats[seat].owner is 'Not owned':
            raise ValueError('Seat is already available!')

        self.__flight.seats[seat].owner = 'Not owned'
        self.__flight.seats[seat].status = 'Available'

    @property
    def flight(self) -> Flight:
        return self.__flight

    @flight.setter
    def flight(self, value: Flight) -> None:
        self.__flight = value