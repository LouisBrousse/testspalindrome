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
# def test_bonjour():
#     # ETANT DONNE une chaine de caractères
#     chaine = "test"
#     # QUAND on l'envoie au détecteur de palindrome
#     result = DetecteurPalindrome.miroir(chaine)
#     # ALORS IL DIT Bonjour avant de répondre
#     assert result.startswith("Bonjour")
#     assert "tset" in result

# def test_aurevoir():
#     # ETANT DONNE une chaine de caractères
#     chaine = "test"
#     # QUAND on l'envoie au détecteur de palindrome
#     result = DetecteurPalindrome.miroir(chaine)
#     # ALORS IL DIT Aurevoir après avoir répondu
#     assert result.endswith("Aurevoir")
#     assert "tset" in result