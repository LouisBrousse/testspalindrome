import datetime
from src.langues.LangueAnglaise import LangueAnglaise

def test_langue_anglaise_matin():
    assert LangueAnglaise().salutations(datetime.time(9, 0)) == "Good morning!"

def test_langue_anglaise_apres_midi():
    assert LangueAnglaise().salutations(datetime.time(13, 30)) == "Good afternoon!"

def test_langue_anglaise_soiree():
    assert LangueAnglaise().salutations(datetime.time(19, 0)) == "Good evening!"

def test_langue_anglaise_nuit_avant_minuit():
    assert LangueAnglaise().salutations(datetime.time(22, 0)) == "Good night!"

def test_langue_anglaise_nuit_apres_minuit():
    assert LangueAnglaise().salutations(datetime.time(2, 0)) == "Good night!"