import os
from src.langues.Ilangue import Ilangue
import datetime

class LangueAleatoire(Ilangue):
    def __init__(self, length=64):
        self._salutations = os.urandom(length).decode('latin1', errors='ignore')
        self._felicitations = os.urandom(length).decode('latin1', errors='ignore')
        self._acquittance = os.urandom(length).decode('latin1', errors='ignore')

    
    def salutations(self, heure=datetime.time):
        return self._salutations

    @property
    def felicitations(self):
        return self._felicitations

    @property
    def acquittance(self):
        return self._acquittance
