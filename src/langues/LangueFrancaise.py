from src.langues.Ilangue import Ilangue

class LangueFrancaise(Ilangue):
    @property
    def salutations(self):
        return "Bonjour"
    @property
    def felicitations(self):
        return "Félicitations"
    @property
    def acquittance(self):
        return "Au revoir"