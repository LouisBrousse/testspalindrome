from src.langues.Ilangue import Ilangue

class DetecteurPalindrome:

    def __init__(self, langue: Ilangue, heureActuelle):
        self.langue = langue
        self.heureActuelle = heureActuelle


    
    def miroir(self, chaine):
        if chaine == chaine[::-1]:
            return f"{self.langue.salutations(self.heureActuelle)}\n{chaine}\n{self.langue.felicitations}\n{self.langue.acquittance}"
        else:            
            return f"{self.langue.salutations(self.heureActuelle)}\n{chaine[::-1]}\n{self.langue.acquittance}"
