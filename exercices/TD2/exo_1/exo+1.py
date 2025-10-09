import pyfiglet
import random

# Liste de fun facts locaux (tu peux en ajouter autant que tu veux !)
FUN_FACTS = {
    2024: "Les Jeux Olympiques de Paris auront lieu en 2024 ! 🏅",
    2000: "L'an 2000 a marqué le passage au 3e millénaire. 🎆",
    1969: "Premier pas sur la Lune en 1969 ! 🌕",
    1989: "Chute du mur de Berlin en 1989. 🧱",
    1945: "Fin de la Seconde Guerre mondiale en 1945. ✌️",
    1789: "Révolution française en 1789. 🇫🇷",
    1492: "Christophe Colomb découvre l'Amérique en 1492. ⛵",
    1999: "Sortie de la Matrix en 1999. 🕶️",
    2020: "Début de la pandémie de COVID-19 en 2020. 😷",
    2023: "Lancement de Threads par Meta en 2023. 🧵",
}

def est_bisextile(annee):
    if annee % 400 == 0:
        return True, "🎉"
    elif annee % 100 == 0:
        return False, "❌"
    elif annee % 4 == 0:
        return True, "🎉"
    else:
        return False, "❌"

def obtenir_fun_fact(annee):
    return FUN_FACTS.get(annee, f"Aucun fun fact prédéfini pour {annee}. Tu peux en ajouter un !")

def main():
    print(pyfiglet.figlet_format("Bisextile ?", font="digital"))
    print("Tape 'quit' ou 'q' pour quitter.\n")

    while True:
        annee_input = input("Entrez une année : ").strip().lower()
        if annee_input in ('quit', 'q'):
            print("Au revoir ! 👋")
            break

        try:
            annee = int(annee_input)
            est_bis, emoji = est_bisextile(annee)
            print(pyfiglet.figlet_format(f"{annee} {emoji}", font="standard"))

            if est_bis:
                print(f"{annee} est bisextile ! {emoji}")
            else:
                print(f"{annee} n'est pas bisextile. {emoji}")

            fun_fact = obtenir_fun_fact(annee)
            print(f"\nFun fact : {fun_fact}\n")

        except ValueError:
            print("⚠️ Erreur : entrez un nombre valide (ex: 2024).\n")
        except KeyboardInterrupt:
            print("\nAu revoir ! 👋")
            break
        except Exception as e:
            print(f"⚠️ Erreur inattendue : {e}\n")

if __name__ == "__main__":
    main()
