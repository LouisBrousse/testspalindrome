from src.DetecteurPalindrome import DetecteurPalindrome 
def test_nominal():
    # ETANT DONNE une chaine de caractères
    chaine = "caracteres"
    # QUAND on l'envoie au détecteur de palindrome
    result = DetecteurPalindrome.miroir(chaine)
    # ALORS IL RENVOI la chaîne à l'envers
    assert "seretcarac" in result

def test_palindrome():
    # ETANT DONNE une chaine de caractères palindrome
    chaine = "kayak"
    # QUAND on l'envoie au détecteur de palindrome
    result = DetecteurPalindrome.miroir(chaine)
    # ALORS IL RENVOI la chaîne à l'envers avec un message
    assert "kayak Bien dit!" in result