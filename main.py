from time import time
from datetime import datetime
from uuid import uuid4

class City:
    def __init__(self, name: str, country: str, state: str) -> None:
        self.__name = name
        self.__country = country
        self.__state = state

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def country(self) -> str:
        return self.__country
    
    @country.setter
    def country(self, value: str) -> None:
        self.__country = value

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, value: str) -> None:
        self.__state = value

class Airport:
    def __init__(self, city: City, max_departures: int, name: str) -> None:
        self.__city = city
        self.__max_departures = max_departures
        self.__name = name

    @property
    def city(self) -> City:
        return self.__city
    
    @city.setter
    def city(self, value: City) -> None:

    @property
    def max_departures(self) -> int:
        return self.__max_departures

    @max_departures.setter
    def max_departures(self, value: int) -> None:
        self.__max_departures = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

class Person:
    def __init__(self, name: str, func: str) -> None:
        self.__name = name
        self.__func = func

class Crew(Person):
    def __init__(self, name: str, occupation: str) -> None:
        super().__init__(name, __class__.__name__)
        self.__occupation = occupation

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def occupation(self) -> str:
        return self.__occupation

    @occupation.setter
    def occupation(self, value) -> None:
        self.__occupation = value

class Seat:
    def __init__(self, id: str, status: 'Busy' | 'Available' = 'Available') -> None:
        self.__id = id
        self.__status = status
        self.__seats_list = list()

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, value: str) -> None:
        self.__id = value

    @property
    def status(self) -> 'Busy' | 'Available':
        return self.__status

    @status.setter
    def status(self, value) -> None:
        self.__status = value

    @property
    def seats_list(self) -> list[str]:
        return self.__seats_list

    @seats_list.setter
    def seats_list(self, value: list[str]) -> None:
        self.__seats_list = value

class Flight:
    def __init__(self, type: 'International' | 'National', departure: Airport.city, destination: Airport.city, departure_time: time, departure_date: datetime.date, seats: list[Seat], crew: list[Crew]) -> None:
        self.__type = type
        self.__id = uuid4()
        self.__departure = departure
        self.__destination = destination
        self.__departure_time = departure_time
        self.__departure_date = departure_date
        self.__seats = seats
        self.__crew = crew


    @property
    def type(self) -> 'International' | 'National':
        return self.__type

    @type.setter
    def type(self, value) -> None:
        self.__type = value

    @property
    def id(self) -> string:
        return self.__id

    @id.setter
    def id(self, value: string) -> None:
        self.__id = value

    @property
    def departure(self) -> Airport.city:
        return self.__departure

    @departure.setter
    def departure(self, value: Airport.city) -> None:
        self.__departure = value

    @property
    def destination(self) -> Airport.city:
        return self.__destination

    @destination.setter
    def destination(self, value: Airport.city) -> None:
        self.__destination = value

    @property
    def departure_time(self) -> time:
        return self.__departure_time

    @departure_time.setter
    def departure_time(self, value: time) -> None:
        self.__departure_time = value

    @property
    def departure_date(self) -> datetime.date:
        return self.__departure_date

    @departure_date.setter
    def departure_date(self, value: datetime.date) -> None:
        self.__departure_date = value

    @property
    def seats(self) -> list[Seat]:
        return self.__seats

    @seats.setter
    def seats(self, value: list[Seat]) -> None:
        self.__seats = value

class Reservation(ABC):
    def __init__(self, flight: Flight) -> None:
        self.__flight = flight

    """
    Checks whether the 
    @param seat 
    is currently available in the flight, if ==true then reservation is possible.
    """
    @abstractmethod
    def create(self, seat) -> None:
        if self.__flight.seats[seat].status == 'Busy':
            raise ValueError('Seat is busy!')

        self.__flight.seats[seat].status = 'Busy'

    """
    Checks whether the 
    @param seat 
    is currently busy in the flight, if ==true then cancelling is possible.
    """
    @abstractmethod
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