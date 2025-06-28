from src.langues.Ilangue import Ilangue
import datetime

class LangueAnglaise(Ilangue):
    
    def salutations(self, heure: datetime.time) -> str:
        if heure >= datetime.time(6, 0) and heure < datetime.time(12, 0):
            return "Good morning!"
        elif heure >= datetime.time(12, 0) and heure < datetime.time(18, 0):
            return "Good afternoon!"
        elif heure >= datetime.time(18, 0) and heure < datetime.time(21, 0):
            return "Good evening!"
        else:
            return "Good night!"
    @property
    def felicitations(self):
        return "Well done"
    @property
    def acquittance(self):
        return "Goodbye!"