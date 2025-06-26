from .Paroles import Paroles

class DetecteurPalindrome:

    @staticmethod
    def miroir(chaine):
        if chaine == chaine[::-1]:
            return Paroles.bonjour() + " " + chaine + " Bien dit!"
        else:            
            return Paroles.bonjour() + " " + chaine[::-1]
