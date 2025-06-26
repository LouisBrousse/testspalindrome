from src.langues.Ilangue import Ilangue

class DetecteurPalindrome:

    def __init__(self, langue: Ilangue):
        self.langue = langue


    
    def miroir(self, chaine):
        if chaine == chaine[::-1]:
            return f"{self.langue.salutations}\n{chaine}\n{self.langue.felicitations}\n{self.langue.acquittance}"
        else:            
            return f"{self.langue.salutations}\n{chaine[::-1]}\n{self.langue.acquittance}"
