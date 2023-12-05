from abc import ABC, abstractmethod

class IUkPlugConnector(ABC):

    @abstractmethod
    def power(self):
        pass