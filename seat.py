class Seat:
    def __init__(self, id: str, status: str = 'Available') -> None:
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
    def status(self) -> str:
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