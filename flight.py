from airport import Airport, City
from crew import Crew
from seat import Seat
from time import time
from datetime import datetime
from uuid import uuid4


class Flight:
    def __init__(self, type: str, departure: Airport, destination: Airport, departure_time, departure_date, seats: dict[Seat], crew: list[Crew]) -> None:
        self.__id = uuid4()
        self.__type = type
        self.__departure = departure
        self.__destination = destination
        self.__departure_time = departure_time
        self.__departure_date = departure_date
        self.__seats = seats
        self.__crew = crew

    def freeSeats(self) -> dict[Seat]:
        return {key: value for key, value in self.__seats.items() if value.owner == 'Not owned'}

    def showCrew(self):
        pass

    def __str__(self):
        return f"ID: {self.__id}\
               \nTYPE: {self.__type}\
               \nTRAVEL: {self.__destination.name} -> {self.__departure.name}\
               \nDEPARTURE DATE: {self.__departure_date.strftime('%d/%m/%Y')}\
               \nDEPARTURE AT: {self.__departure_time}"
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: str) -> None:
        self.__id = value

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, value) -> None:
        self.__type = value


    @property
    def departure(self) -> Airport:
        return self.__departure

    @departure.setter
    def departure(self, value: Airport) -> None:
        self.__departure = value

    @property
    def destination(self) -> Airport:
        return self.__destination

    @destination.setter
    def destination(self, value: Airport) -> None:
        self.__destination = value

    @property
    def departure_time(self):
        return self.__departure_time

    @departure_time.setter
    def departure_time(self, value) -> None:
        self.__departure_time = value

    @property
    def departure_date(self):
        return self.__departure_date

    @departure_date.setter
    def departure_date(self, value) -> None:
        self.__departure_date = value

    @property
    def seats(self) -> list[Seat]:
        return self.__seats

    @seats.setter
    def seats(self, value: list[Seat]) -> None:
        self.__seats = value