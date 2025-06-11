from datetime import datetime, time

class Ohce:
    
    def __parlefr__():
        bonjour = "Bonjour!"
        bonsoir = "Bonsoir!"
        aurevoir = "Au revoir"
        return(bonjour, bonsoir, aurevoir)
    
    def __parleen__():
        bonjour = "Hello!"
        bonsoir = "Good evening!"
        aurevoir = "Good by!"
        return(bonjour, bonsoir, aurevoir)
    
    
    def __quelheureestil__():
        return datetime.now()
    
    
    def __biendit__(chaine):
        if chaine == chaine[::-1]:
            print ("Bien dit!")
        else :
            print (chaine[::-1])

    def palindrome(heure_fn=None, langue=None):
        # Heure
        if heure_fn is None:
            heure_fn = Ohce.__quelheureestil__
        heure = heure_fn()

        # Langue
        if langue == "en":
            bonjour, bonsoir, aurevoir = Ohce.__parleen__()
        elif langue == None or "fr":
            bonjour, bonsoir, aurevoir = Ohce.__parlefr__()
        

        if heure.time() < time(18, 0):
            print(bonjour)
        else:
            print(bonsoir)
                
        chaine = input("> ")
        
        Ohce.__biendit__(chaine)
       
        print(aurevoir)
    
    
    
    def detecteur(chaine):
        if chaine == chaine[::-1]:
            return Ohce.biendit(chaine)
        else:
            return Ohce.palindrome(chaine)

if __name__ == "__main__":
    Ohce.palindrome()