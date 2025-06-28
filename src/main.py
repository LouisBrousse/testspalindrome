from DetecteurPalindrome import DetecteurPalindrome
from langues.LangueFrancaise import LangueFrancaise

def main():

    while True:
       
            entree = input("> ")
            
            print(DetecteurPalindrome(LangueFrancaise()).miroir(entree))
         

if __name__ == "__main__":
    main()