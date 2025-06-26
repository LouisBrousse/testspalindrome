from src.DetecteurPalindrome import DetecteurPalindrome

def main():

    detecteur = DetecteurPalindrome()

    while True:
        try:
            entree = input("> ")
            if not entree:
                raise ValueError("Aucune saisie")
            print(entree + " => " + detecteur.miroir(entree))
        except (EOFError, KeyboardInterrupt):
            print("\n" + "Au revoir !")
            break
        except Exception as e:
            print(f"Erreur : {e}")

if __name__ == "__main__":
    main()