from person import Person

class Crew(Person):
    def __init__(self, name: str, occupation: str) -> None:
        super().__init__(name, __class__.__name__)
        self.__occupation = occupation

    def __str__(self) -> str:
        return f"Name: {self.name}\nOccupation: {self.__occupation}"

    @property
    def occupation(self) -> str:
        return self.__occupation

    @occupation.setter
    def occupation(self, value) -> None:
        self.__occupation = value