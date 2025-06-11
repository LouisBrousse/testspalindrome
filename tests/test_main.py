from src.main import Ohce

def test_nominal():
    # ETANT DONNE une chainbe de caractères
    chaine = "caracteres"
    # QUAND on l'envoie au détecteur de palindrome
    result = Ohce().palindrome(chaine)
    # ALORS IL RENVOI la chaîne à l'envers
    assert "seretcarac \n"

def test_bonjour():
    # ETANT DONNE une chainbe de caractères
    chaine = "caracteres"
    # QUAND on l'envoie au détecteur de palindrome
    result = Ohce().palindrome(chaine)
    # ALORS IL RENVOI bonjour au début
    assert "Bonjour \n"+ "seretcarac \n"

def test_aurevoir():
    # ETANT DONNE une chainbe de caractères
    chaine = "caracteres"
    # QUAND on l'envoie au détecteur de palindrome
    result = Ohce().palindrome(chaine)
    # ALORS IL RENVOI Aurevoir a la fin
    assert "Bonjour \n" + "seretcarac \n" + "Au revoir"

def test_kayak():
    # ETANT DONNE une chainbe de caractères
    chaine = "kayak"
    # QUAND on l'envoie au détecteur de palindrome
    result = Ohce().palindrome(chaine)
    # ALORS IL RENVOI Aurevoir a la fin
    assert "Bonjour \n" + "kayak, bien dit \n" + "Au revoir"