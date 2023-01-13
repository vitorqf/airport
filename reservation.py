from abc import ABC, abstractmethod
from flight import Flight
from person import Person
from seat import Seat

class Reservation(ABC):
    def __init__(self, flight: Flight) -> None:
        self.__flight = flight

    """
    Checks whether the 
    @param seat 
    is currently available in the flight, if ==true then reservation is possible.
    """
    def create(self, seat) -> None:
        if self.__flight.seats[seat].status == 'Busy':
            raise ValueError('Seat is busy!')

        self.__flight.seats[seat].status = 'Busy'

    """
    Checks whether the 
    @param seat 
    is currently busy in the flight, if ==true then cancelling is possible.
    """
    def cancel(self, seat) -> None:
        if self.__flight.seats[seat].status == 'Available':
            raise ValueError('Seat is already available!')

        self.__flight.seats[seat].status = 'Available'

    @property
    def flight(self) -> Flight:
        return self.__flight

    @flight.setter
    def flight(self, value: Flight) -> None:
        self.__flight = value

class Passenger(Person, Reservation):
    def __init__(self, name: str, flight: Flight, seat: Seat) -> None:
        super().__init__(name, __class__.__name__)
        self.__flight = flight