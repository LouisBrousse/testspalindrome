
from .utils.Langue_Stub import Langue_Stub
from .utils.LangueAleatoire import LangueAleatoire
from src.langues.LangueAnglaise import LangueAnglaise
import datetime
import random
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
    LangueAleatoire(),
    Langue_Stub(),
])

def test_bien_dit(langue):
    # ETANT DONNE une chaine de caractères palindrome
    chaine = "kayak"
    # QUAND on l'envoie au détecteur de palindrome quelque soit la langue
    dp = DetecteurPalindromeBuilder().avec_langue(langue).build()
    result = dp.miroir(chaine)
    # ALORS IL RENVOI la chaîne à l'envers avec félicitations
    attendu = chaine + "\n" + langue.felicitations
    assert attendu in result

@pytest.mark.parametrize("langue, mot", [
    (LangueAleatoire(), "hello"),
    (Langue_Stub(felicitations="test"), "hello"), #En python obliger de mettre un mot car "" True
])

def test_non_bien_dit(langue, mot):
    # ETANT DONNE une chaine de caractères non palindrome
    chaine = mot
    # QUAND on l'envoie au détecteur de palindrome
    dp = DetecteurPalindromeBuilder().avec_langue(langue).build()
    result = dp.miroir(chaine)
    # ALORS IL RENVOI la chaîne à l'envers sans félicitations
    assert  langue.felicitations not in result


def langues_chaînes_heures_possibles():
    heures_remarquables = [
        datetime.time(0, 0),
        datetime.time(
            random.randint(0, 23),
            random.randint(0, 59)
        ),
        datetime.time(6, 0),    # matin
        datetime.time(12, 0),   # après-midi
        datetime.time(18, 0),   # soirée
        datetime.time(21, 0),   # nuit
    ]
    for heure in heures_remarquables:
        for mot in ["test", "kayak"]:
            yield LangueAleatoire(), mot, heure
            yield Langue_Stub(salutations="stub"), mot, heure

@pytest.mark.parametrize("langue, mot, heureTestee", list(langues_chaînes_heures_possibles()))

def test_bonjour(langue, mot, heureTestee):
    # ETANT DONNE une chaine de caractères
    chaine = mot
    # ET un détecteure avec une langue une heure fixe
    heure = heureTestee 
    dp = DetecteurPalindromeBuilder().avec_langue(langue).avec_heure_fixe_a(heure).build()
    # QUAND on l'envoie au détecteur de palindrome
    result = dp.miroir(chaine)
    # ALORS IL DIT Bonjour avant de répondre
    assert result.startswith(langue.salutations(heureTestee))
    

@pytest.mark.parametrize("langue, mot", [
    (LangueAleatoire(), "hello"),
    (LangueAleatoire(), "kayak"),
    (Langue_Stub(acquittance="test3"), "hello"),
    (Langue_Stub(acquittance="test3"), "kayak"),
])

def test_aurevoir(langue, mot):
    # ETANT DONNE une chaine de caractères
    chaine = mot
    # QUAND on l'envoie au détecteur de palindrome
    dp = DetecteurPalindromeBuilder().avec_langue(langue).build()
    result = dp.miroir(chaine)
    # ALORS IL DIT Aurevoir après avoir répondu
    assert result.endswith(langue.acquittance)




def test_langue_anglaise_matin():
    assert LangueAnglaise().salutations(datetime.time(9, 0)) == "Hello!"