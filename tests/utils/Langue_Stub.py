from src.langues.Ilangue import Ilangue

class Langue_Stub(Ilangue):
    def __init__(self, salutations="", felicitations="", acquittance=""):
        self._salutations = salutations
        self._felicitations = felicitations
        self._acquittance = acquittance

    @property
    def salutations(self):
        return self._salutations

    @property
    def felicitations(self):
        return self._felicitations

    @property
    def acquittance(self):
        return self._acquittance
