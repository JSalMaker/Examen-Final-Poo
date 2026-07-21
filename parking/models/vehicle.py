from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, license_plate: str, owner_name: str, is_member: bool):
        self.license_plate = license_plate
        self.__owner_name = owner_name
        self._is_member = is_member
        self.ticket : 'Ticket' | None = None

    @abstractmethod
    def get_type(self):
        raise NotImplementedError("Las clases hijas deben redefinir este método de forma obligatoria.")
    
    def get_name(self):
        return self.__owner_name

    def __str__(self) -> str:
        raise NotImplementedError("Las clases hijas deben implementarlo.")


