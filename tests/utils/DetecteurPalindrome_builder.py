from src.DetecteurPalindrome import DetecteurPalindrome
from tests.utils.Langue_Stub import Langue_Stub

class DetecteurPalindromeBuilder:
    def __init__(self):
        self._langue = Langue_Stub()
        self._heure = None

    def avec_langue(self, langue):
        self._langue = langue
        return self
    
    def avec_heure_fixe_a(self, heure):
        self._heure = heure
        return self
    
    def build(self):
        return DetecteurPalindrome(self._langue, self._heure)
    
    @staticmethod
    def default():
        return DetecteurPalindromeBuilder().build()
