from src.DetecteurPalindrome import DetecteurPalindrome 
from .Langue_Stub import Langue_Stub
from src.langues.Ilangue import Ilangue

class DetecteurPalindromeBuilder:
    def __init__(self):
        self._langue = Langue_Stub()

    def avec_langue(self, langue: Ilangue):
        self._langue = langue
        return self

    def build(self):
        return DetecteurPalindrome(self._langue)

    @staticmethod
    def default():
        return DetecteurPalindromeBuilder().build()