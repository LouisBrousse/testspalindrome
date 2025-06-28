from langues.Ilangue import Ilangue

class LangueParDefaut(Ilangue):
    
    def salutations(self, heure):
        return ""
    @property
    def felicitations(self):
        return ""
    @property
    def acquittance(self):
        return ""