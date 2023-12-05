from abc import ABC, abstractmethod


class IUSPlugConnector(ABC):
    @abstractmethod
    def power(self):
        pass
