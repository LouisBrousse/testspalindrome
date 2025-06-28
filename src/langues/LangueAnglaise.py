from src.langues.Ilangue import Ilangue

class LangueAnglaise(Ilangue):
    @property
    def salutations(self):
        return "Hello!"
    @property
    def felicitations(self):
        return "Well done"
    @property
    def acquittance(self):
        return "Goodbye!"