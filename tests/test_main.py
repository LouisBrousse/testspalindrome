from src.main import Ohce
def test_nominal():
    # ETANT DONNE une chainbe de caractères
    chaine = "caracteres"
    # QUAND on l'envoie au détecteur de palindrome
    chaine_inverse = Ohce.palindrome(chaine)
    # ALORS IL RENVOI la chaîne à l'envers
    assert chaine_inverse == "seretcarac"

def test_bonjour():
    # ETANT DONNE une chainbe de caractères
    # QUAND on l'envoie au détecteur de palindrome
    # ALORS IL PRINT "Bonjour"
    # ET il renvoi la chaîne à l'envers