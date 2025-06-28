from src.langues.Ilangue import Ilangue

class LangueAnglaise(Ilangue):
    
    def salutations(self, heure):
        return "Hello!"
    @property
    def felicitations(self):
        return "Well done"
    @property
    def acquittance(self):
        return "Goodbye!"