from .Paroles import Paroles

class DetecteurPalindrome:

    @staticmethod
    def miroir(chaine):
        if chaine == chaine[::-1]:
            return Paroles.bonjour() + " " + chaine + Paroles.felicitation() + " " + Paroles.aurevoir()
        else:            
            return Paroles.bonjour() + " " + chaine[::-1] + " " + Paroles.aurevoir()
