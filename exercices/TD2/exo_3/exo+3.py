import pyfiglet

def conv_homme_chien(annees_humaines):
    if annees_humaines <= 18:
        return annees_humaines / 9
    else:
        return 2 + (annees_humaines - 18) / 6

def conv_chien_homme(annees_canines):
    if annees_canines <= 2:
        return annees_canines * 9
    else:
        return 18 + (annees_canines - 2) * 6

def main():
    print(pyfiglet.figlet_format("Conversion Humain Canin", font="slant"))



    print("Tapez 'quit' ou 'q' pour quitter.\n")

    while True:
        reponse = input("Que voulez-vous convertir ? (ex: 'humain vers chien', 'chien vers humain', '1', '2', 'quit') : ").strip().lower()

        if reponse in ('quit', 'q'):
            print("Au revoir ! 👋")
            break

        # Vérification des entrées verbeuses
        if any(mot in reponse for mot in ['humain vers chien', 'humain chien', 'humaines canines', '1']):
            try:
                annees_humaines = int(input("Entrez l'âge en années humaines : "))
                annees_canines = conv_homme_chien(annees_humaines)
                print(f"{annees_humaines} année(s) humaine(s) équivalent à {annees_canines:.1f} année(s) canine(s).\n")
            except ValueError:
                print("Erreur : Veuillez entrer un nombre valide.\n")

        elif any(mot in reponse for mot in ['chien vers humain', 'chien humain', 'canines humaines', '2']):
            try:
                annees_canines = int(input("Entrez l'âge du chien en années : "))
                annees_humaines = conv_chien_homme(annees_canines)
                print(f"{annees_canines} année(s) canine(s) équivalent à {annees_humaines} année(s) humaine(s).\n")
            except ValueError:
                print("Erreur : Veuillez entrer un nombre valide.\n")

        else:
            print("Réponse non comprise. Essayez par exemple : 'humain vers chien', 'chien vers humain', '1', ou '2'.\n")

if __name__ == "__main__":
    main()
