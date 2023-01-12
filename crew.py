from person import Person

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