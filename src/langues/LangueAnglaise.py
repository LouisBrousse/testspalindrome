from src.langues.Ilangue import Ilangue

class LangueAnglaise(Ilangue):
    @property
    def salutations(self):
        return "Hello!"
    @property
    def felicitations(self):
        return "Congratulations"
    @property
    def acquittance(self):
        return "Goodbye!"