from abc import ABC, abstractmethod

class Ilangue(ABC):
    @property
    @abstractmethod
    def salutations(self):
        pass

    @property
    @abstractmethod
    def felicitations(self):
        pass

    @property
    @abstractmethod
    def acquittance(self):
        pass
