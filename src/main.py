import datetime

class Ohce:
    def __init__(self, heure=None, langue="fr"):
        if heure is None:
            self.heure = datetime.datetime.now().time()
        else:
            self.heure = datetime.datetime.strptime(heure, "%H:%M").time()
        self.langue = langue
    
    def ditbonjour(self):
        limite = datetime.time(18, 0)

        if self.heure >= limite:
            return "Bonsoir \n"
        else:
            return "Bonjour \n"

    def au_revoir(self):
        return "Au revoir"
    
    def miroir(self, chaine):
        if chaine == chaine[::-1]:
            return chaine + "\n"+ "Bien dit \n"
        else :
            return chaine[::-1] + " \n"
    
    def palindrome(self, chaine):
        reponse=self.ditbonjour()  

        reponse += self.miroir(chaine)
        
        reponse += self.au_revoir()

        return reponse
    
