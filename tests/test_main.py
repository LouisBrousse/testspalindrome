from src.main import Ohce

def test_nominal():
    # ETANT DONNE une chainbe de caractères
    chaine = "caracteres"
    # QUAND on l'envoie au détecteur de palindrome
    result = Ohce().palindrome(chaine)
    # ALORS IL RENVOI la chaîne à l'envers
    assert "seretcarac \n" in result

def test_bonjour():
    # ETANT DONNE une chainbe de caractères
    chaine = "caracteres"
    # QUAND on l'envoie au détecteur de palindrome
    result = Ohce().palindrome(chaine)
    # ALORS IL RENVOI bonjour au début
    assert result.startswith("Bonjour \n")

def test_aurevoir():
    # ETANT DONNE une chainbe de caractères
    chaine = "caracteres"
    # QUAND on l'envoie au détecteur de palindrome
    result = Ohce().palindrome(chaine)
    # ALORS IL RENVOI Aurevoir a la fin
    assert result.endswith("Au revoir")

def test_kayak():
    # ETANT DONNE une chainbe de caractères qui est un palindrome
    chaine = "kayak"
    # QUAND on l'envoie au détecteur de palindrome
    result = Ohce().palindrome(chaine)
    # ALORS IL RENVOI Bien dit après la chaine
    assert "Bien dit \n" 


def test_pasbiendit():
    # ETANT DONNE une chainbe de caractères
    chaine = "caracteres"
    # QUAND on l'envoie au détecteur de palindrome
    result = Ohce().palindrome(chaine)
    # ALORS IL RENVOI la chaîne à l'envers
    assert "Bien dit \n" not in result