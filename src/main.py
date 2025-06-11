class Ohce:
    
    def ditbonjour(self):
        return"Bonjour \n"

    def au_revoir(self):
        return 
    
    
    def biendit(self, chaine):
        if chaine == chaine[::-1]:
            return chaine + "Bien dit \n"
        else :
            return chaine[::-1]

    def palindrome(self, chaine):
        reponse=self.ditbonjour()    # def demandechaine():

        # Inverser la chaîne de caractères
        
        # if chaine == chaine_inverse:
            # return chaine_inverse + self.biendit
        reponse += self.biendit(chaine)
        
        reponse += self.au_revoir()

        return reponse
    



    
    def detecteur(chaine):
        if chaine == chaine[::-1]:
            return Ohce.biendit(chaine)
        else:
            return Ohce.palindrome(chaine)