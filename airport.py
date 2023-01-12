class City:
    def __init__(self, name: str, country: str, state: str) -> None:
        self.__name = name
        self.__country = country
        self.__state = state

    def __str__(self):
        return f"{self.__name}, {self.__country}, {self.__state}"

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

    def __str__(self):
        return f"{self.__name}\nMax departures per hour: {self.__max_departures}\n{self.__city}\n"

    @property
    def city(self) -> City:
        return self.__city
    
    @city.setter
    def city(self, value: City) -> None:
        self.__city = value

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
