

class Seat:
    def __init__(self, id: str, owner: str = 'Not owned', status: str = 'Available') -> None:
        self.__id = id
        self.__status = status
        self.__owner = owner
    
    def __str__(self) -> str:
        return f"SEAT [{self.__id}]: {self.__status}"

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
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, value: str) -> None:
        self.__owner = value