class Ohce:
    
    def ditbonjour(self):
        return"Bonjour \n"

    def au_revoir(self):
        return "Au revoir"
    
    def miroir(self, chaine):
        if chaine == chaine[::-1]:
            return chaine + ", bien dit \n"
        else :
            return chaine[::-1] + " \n"

    def palindrome(self, chaine):
        reponse=self.ditbonjour()  

        reponse += self.miroir(chaine)
        
        reponse += self.au_revoir()

        return reponse
    
