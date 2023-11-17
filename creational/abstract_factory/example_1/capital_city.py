from abc import ABC, abstractmethod

class CapitalCity(ABC):

    @abstractmethod
    def get_popullation(self) -> int:
        pass

    @abstractmethod
    def list_top_attractions(self) -> []:
        pass