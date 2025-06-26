class DetecteurPalindrome:
    

    @staticmethod
    def miroir(chaine):
        if chaine == chaine[::-1]:
            return chaine + " Bien dit!"
        else:            
            return chaine[::-1]

    
