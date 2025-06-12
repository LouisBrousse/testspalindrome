from src.main import Ohce

def test_nominal():
    # ETANT DONNE une chainbe de caractères
    chaine = "caracteres"
    # QUAND on l'envoie au détecteur de palindrome
    result = Ohce.decterpalindrome(chaine)
    # ALORS IL RENVOI la chaîne à l'envers
    assert "seretcarac \n" in result
