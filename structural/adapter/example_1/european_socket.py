from abc import ABC, abstractmethod

class IEuropeanSocket(ABC):

    @abstractmethod
    def voltage(self):
        pass

    @abstractmethod
    def live(self):
        pass

    @abstractmethod
    def neutral(self):
        pass

    @abstractmethod
    def earth(self):
        pass