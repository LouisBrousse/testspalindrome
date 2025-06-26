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
    # ALORS IL RENVOI la chaîne à l'envers
    assert "kayak" in result

def test_bien_dit():
    # ETANT DONNE une chaine de caractères palindrome
    chaine = "kayak"
    # QUAND on l'envoie au détecteur de palindrome
    result = DetecteurPalindrome.miroir(chaine)
    # ALORS IL RENVOI la chaîne à l'envers avec "Bien dit!"
    assert "Bien dit!" in result

def test_non_bien_dit():
    # ETANT DONNE une chaine de caractères non palindrome
    chaine = "hello"
    # QUAND on l'envoie au détecteur de palindrome
    result = DetecteurPalindrome.miroir(chaine)
    # ALORS IL RENVOI la chaîne à l'envers sans "Bien dit!"
    assert "Bien dit!" not in result
    assert "olleh" in result

def test_bonjour():
    # ETANT DONNE une chaine de caractères
    chaine = "test"
    # QUAND on l'envoie au détecteur de palindrome
    result = DetecteurPalindrome.miroir(chaine)
    # ALORS IL DIT Bonjour avant de répondre
    assert result.startswith("Bonjour")
    