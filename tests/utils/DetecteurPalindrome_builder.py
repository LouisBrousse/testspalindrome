from src.DetecteurPalindrome import DetecteurPalindrome
from tests.utils.Langue_Stub import Langue_Stub

class DetecteurPalindromeBuilder:
    def __init__(self):
        self._langue = Langue_Stub()
    def avec_langue(self, langue):
        self._langue = langue
        return self
    def build(self):
        return DetecteurPalindrome(self._langue)
    @staticmethod
    def default():
        return DetecteurPalindromeBuilder().build()
