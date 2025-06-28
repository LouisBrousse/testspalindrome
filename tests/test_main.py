
from src.langues.LangueAnglaise import LangueAnglaise
from src.langues.LangueFrancaise import LangueFrancaise
import pytest
from .utils.DetecteurPalindrome_builder import DetecteurPalindromeBuilder 

def test_nominal():
    # ETANT DONNE une chaine de caractères
    chaine = "caracteres"
    # QUAND on l'envoie au détecteur de palindrome
    dp = DetecteurPalindromeBuilder().build()
    result = dp.miroir(chaine)
    # ALORS IL RENVOI la chaîne à l'envers
    assert "seretcarac" in result

def test_palindrome():
    # ETANT DONNE une chaine de caractères palindrome
    chaine = "kayak"
    # QUAND on l'envoie au détecteur de palindrome
    dp = DetecteurPalindromeBuilder().build()
    result = dp.miroir(chaine)
    # ALORS IL RENVOI la chaîne à l'envers
    assert "kayak" in result


@pytest.mark.parametrize("langue", [
    LangueFrancaise(),
    LangueAnglaise(),
])


def test_bien_dit(langue):
    # ETANT DONNE une chaine de caractères palindrome
    chaine = "kayak"
    # QUAND on l'envoie au détecteur de palindrome quelque soit la langue
    fake_felicitations = "BRAVO"

    dp = DetecteurPalindromeBuilder().avec_langue(langue).build()
    result = dp.miroir(chaine)
    # ALORS IL RENVOI la chaîne à l'envers avec "Bien dit!"
    assert langue.felicitations in result

@pytest.mark.parametrize("langue", [
    LangueFrancaise(),
    LangueAnglaise(),
])

def test_non_bien_dit(langue):
    # ETANT DONNE une chaine de caractères non palindrome
    chaine = "hello"
    # QUAND on l'envoie au détecteur de palindrome
    fake_felicitations = "BRAVO"
    dp = DetecteurPalindromeBuilder().avec_langue(langue).build()
    result = dp.miroir(chaine)
    # ALORS IL RENVOI la chaîne à l'envers sans "Bien dit!"
    assert  langue.felicitations not in result
    assert "olleh" in result

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
    