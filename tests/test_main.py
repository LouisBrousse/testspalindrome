from src.main import Ohce
from datetime import datetime
import builtins

def test_nominal(monkeypatch, capfd):
    # ETANT DONNE une chainbe de caractères
    # On simule l'entrée de l'utilisateur
    monkeypatch.setattr(builtins, 'input', lambda _: "test")
    # QUAND on l'envoie au détecteur de palindrome
    result = Ohce.palindrome()
    # ALORS IL RENVOI la chaîne à l'envers
    out, _ = capfd.readouterr()
    assert "tset" in out

def test_palindrome(monkeypatch, capfd):
    # ETANT DONNE une chainbe de caractères
    # On simule l'entrée de l'utilisateur
    monkeypatch.setattr(builtins, 'input', lambda _: "kayak")
    # QUAND on l'envoie au détecteur de palindrome
    result = Ohce.palindrome()
    # ALORS IL RENVOI la chaîne à l'envers
    out, _ = capfd.readouterr()
    assert "Bien dit" in out

def test_bonjour(monkeypatch, capfd):
    # ETANT DONNE un démarage du programme avant 18h
    # Et on simule l'entrée de l'utilisateur
    fake_time = lambda: datetime(2025, 1, 1, 9, 0, 0)
    monkeypatch.setattr(builtins, "input", lambda _: "palindrome")
    # QUAND on l'envoie au détecteur de palindrome
    result = Ohce.palindrome(fake_time)
    # ALORS il renvoi "Bonjour!"
    out, _ = capfd.readouterr()
    assert "Bonjour!" in out

def test_bonjour2(monkeypatch, capfd):
    # ETANT DONNE un démarage du programme avant 18h
    # Et on simule l'entrée de l'utilisateur
    fake_time = lambda: datetime(2025, 1, 1, 9, 17, 59)
    monkeypatch.setattr(builtins, "input", lambda _: "palindrome")
    # QUAND on l'envoie au détecteur de palindrome
    result = Ohce.palindrome(fake_time)
    # ALORS il renvoi "Bonjour!"
    out, _ = capfd.readouterr()
    assert "Bonjour!" in out

def test_bonsoir(monkeypatch, capfd):
    # ETANT DONNE un démarage du programme à 18h
    # Et on simule l'entrée de l'utilisateur
    fake_time = lambda: datetime(2023, 10, 1, 18, 0)
    monkeypatch.setattr(builtins, "input", lambda _: "palindrome")
    # QUAND on l'envoie au détecteur de palindrome
    result = Ohce.palindrome(fake_time)
    # ALORS il renvoi "Bonsoir!"
    out, _ = capfd.readouterr()
    assert "Bonsoir!" in out

def test_bonsoir2(monkeypatch, capfd):
    # ETANT DONNE un démarage du programme à 18h
    # Et on simule l'entrée de l'utilisateur
    fake_time = lambda: datetime(2023, 10, 1, 23, 59)
    monkeypatch.setattr(builtins, "input", lambda _: "palindrome")
    # QUAND on l'envoie au détecteur de palindrome
    result = Ohce.palindrome(fake_time)
    # ALORS il renvoi "Bonsoir!"
    out, _ = capfd.readouterr()
    assert "Bonsoir!" in out

def test_biendit(monkeypatch, capfd):
    # ETANT DONNE une chainbe de caractères
    # On simule l'entrée de l'utilisateur
    monkeypatch.setattr(builtins, 'input', lambda _: "kayak")
    # QUAND on l'envoie au détecteur de palindrome
    result = Ohce.palindrome()
    # ALORS IL RENVOI la chaîne à l'envers
    out, _ = capfd.readouterr()
    assert "Bien dit!" in out

def test_bonjouren(monkeypatch, capfd):
    # ETANT DONNE un démarage du programme avant 18h
    # Et on simule l'entrée de l'utilisateur
    fake_time = lambda: datetime(2025, 1, 1, 9, 0, 0)
    monkeypatch.setattr(builtins, "input", lambda _: "palindrome")
    # QUAND on l'envoie au détecteur de palindrome
    result = Ohce.palindrome(fake_time, langue="en")
    # ALORS il renvoi "Bonjour!" en Anglais
    out, _ = capfd.readouterr()
    assert "Hello!" in out

def test_bonsoiren(monkeypatch, capfd):
    # ETANT DONNE un démarage du programme à 18h
    # Et on simule l'entrée de l'utilisateur
    fake_time = lambda: datetime(2023, 10, 1, 18, 0)
    monkeypatch.setattr(builtins, "input", lambda _: "palindrome")
    # QUAND on l'envoie au détecteur de palindrome
    result = Ohce.palindrome(fake_time, langue="en")
    # ALORS il renvoi "Bonsoir!" en Anglais
    out, _ = capfd.readouterr()
    assert "Good evening!" in out



    # assert trop laxe, lisibilité des tests, cas de tests sur bonjour aurevoir.