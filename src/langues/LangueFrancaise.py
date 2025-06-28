from src.langues.Ilangue import Ilangue

class LangueFrancaise(Ilangue):
    @property
    def salutations(self):
        return "Bonjour"
    @property
    def felicitations(self):
        return "Bien dit"
    @property
    def acquittance(self):
        return "Au revoir"