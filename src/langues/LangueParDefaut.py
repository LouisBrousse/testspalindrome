from src.langues.Ilangue import Ilangue

class LangueParDefaut(Ilangue):
    @property
    def salutations(self):
        return ""
    @property
    def felicitations(self):
        return ""
    @property
    def acquittance(self):
        return ""