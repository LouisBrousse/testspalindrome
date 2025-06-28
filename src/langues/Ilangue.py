from abc import ABC, abstractmethod
import datetime

class Ilangue(ABC):
    
    @abstractmethod
    def salutations(self, heure: datetime.time):
        pass

    @property
    @abstractmethod
    def felicitations(self):
        pass

    @property
    @abstractmethod
    def acquittance(self):
        pass
