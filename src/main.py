from DetecteurPalindrome import DetecteurPalindrome

def main():

    while True:
       
            entree = input("> ")
            
            print( DetecteurPalindrome.miroir(entree))
         

if __name__ == "__main__":
    main()