from DetecteurPalindrome import DetecteurPalindrome
from langues.LangueFrancaise import LangueFrancaise
import datetime

def main():

    while True:
       
            entree = input("> ")
            heure = datetime.datetime.now().time()
            langue= LangueFrancaise()
            print(DetecteurPalindrome(langue, heureActuelle=heure).miroir(entree))
         

if __name__ == "__main__":
    main()