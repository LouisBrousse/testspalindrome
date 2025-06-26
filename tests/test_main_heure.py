# from src.main import Ohce

# def test_jourdebut():
#     # ETANT DONNE une chainbe de caractères
#     chaine = "caracteres"
#     # QUAND on l'envoie au détecteur de palindrome en debut de journée
#     result = Ohce("00:00").palindrome(chaine)
#     # ALORS IL RENVOI bonjour au début
#     assert result.startswith("Bonjour \n")

# def test_jourfin():
#     # ETANT DONNE une chainbe de caractères
#     chaine = "caracteres"
#     # QUAND on l'envoie au détecteur de palindrome en fin de journée
#     result = Ohce("17:59").palindrome(chaine)
#     # ALORS IL RENVOI bonjour au début
#     assert result.startswith("Bonjour \n")

# def test_soirdebut():
#     # ETANT DONNE une chainbe de caractères
#     chaine = "caracteres"
#     # QUAND on l'envoie au détecteur de palindrome debut de soirée
#     result = Ohce("18:00").palindrome(chaine)
#     # ALORS IL RENVOI bonsoir au début
#     assert result.startswith("Bonsoir \n")

# def test_soirfin():
#     # ETANT DONNE une chainbe de caractères
#     chaine = "caracteres"
#     # QUAND on l'envoie au détecteur de palindrome en fin de soirée
#     result = Ohce("23:59").palindrome(chaine)
#     # ALORS IL RENVOI bonsoir au début
#     assert result.startswith("Bonsoir \n")