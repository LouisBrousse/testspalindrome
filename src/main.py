from DetecteurPalindrome import DetecteurPalindrome
from src.langues.LangueFrancaise import LangueFrancaise

def main():

    while True:
       
            entree = input("> ")
            
            print(DetecteurPalindrome(LangueFrancaise()).miroir(entree))
         

if __name__ == "__main__":
    main()