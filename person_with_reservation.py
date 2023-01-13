from abc import ABC, abstractmethod
from flight import Flight
from person import Person

class PersonWithReservation(Person, ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def cancel(self):
        pass


class Passenger(PersonWithReservation):
    def __init__(self, name) -> None:
        super().__init__(name, __class__.__name__)
        self.__seatRequest = None

    def create(self, flight, seat):
        if flight.seats[seat].owner != 'Not owned':
            raise Exception('Sorry! Seat is owned by another person.')

        self.__seatRequest = {
            'flight': flight,
            'name': super().name,
            'seat': seat,
        }

        return self.__seatRequest

    def cancel(self):
        if self.__seatRequest == None:
            raise Exception("Sorry! You don't own any seat.")

        self.__seatRequest = None
        
    def __str__(self) -> str:
        return f"Name: {self.__name}"

class Operator(PersonWithReservation):
    def __init__(self, name, flight: Flight) -> None:
        super().__init__(name, __class__.__name__)
        self.__flight = flight

    """
    Checa se
    @param seat 
    no momento não possui um ocupante, se ==true então a reserva é possível de ser criada.
    """
    def create(self, request: dict['flight': Flight, 'name': str, 'seat': str]) -> None:
        if request == None:
            raise Exception("You're trying to confirm an empty request.")

        if request['flight'].id != self.__flight.id:
            raise Exception("You're trying to confirm a request for a different flight.")

        self.__flight.seats[request['seat']].owner = request['name']
        self.__flight.seats[request['seat']].status = 'Busy'

        return True

    """
    Checa se
    @param seat 
    no momento possui um ocupante, se ==true então é possível o cancelamento da reserva.
    """
    def cancel(self, seat, reservation) -> None:
        if self.__flight.seats[seat].owner == 'Not owned':
            raise ValueError('Seat is already available!')

        self.__flight.seats[seat].owner = 'Not owned'
        self.__flight.seats[seat].status = 'Available'
        reservation.delete()

    @property
    def flight(self) -> Flight:
        return self.__flight

    @flight.setter
    def flight(self, value: Flight) -> None:
        self.__flight = value

PersonWithReservation.register(Passenger)
PersonWithReservation.register(Operator)