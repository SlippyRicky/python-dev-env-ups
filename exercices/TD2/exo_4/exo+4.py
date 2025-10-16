import string

def valider_nom_utilisateur(usr):
    erreurs = []
    # 1. Longueur du nom d'utilisateur
    if len(usr) > 16:
        erreurs.append("Le nom d'utilisateur doit faire moins de 16 caractères.")
    # 2. Pas d'espaces
    if ' ' in usr:
        erreurs.append("Le nom d'utilisateur ne doit pas contenir d'espaces.")
    # 3. Pas de caractères spéciaux
    caracteres_autorises_usr = string.ascii_letters + string.digits
    for char in usr:
        if char not in caracteres_autorises_usr:
            erreurs.append(f"Le nom d'utilisateur ne doit contenir que des lettres et des chiffres (le caractère '{char}' n'est pas autorisé).")
            break
    return erreurs

def valider_mot_de_passe(mdp):
    erreurs = []
    minuscules = string.ascii_lowercase
    majuscules = string.ascii_uppercase
    numeros = [str(i) for i in range(10)]̦
    caracteres_speciaux_acceptes = [
        '~', '`', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=',
        '[', '{', ']', '}', '\\', '|', ';', ':', '"', '\'', ',', '<', '.', '>',
        '/', '?', '!', '§', '°', 'µ', '£'
    ]
    caracteres_speciaux_non_acceptes = [
        '¨', '²', '¹', '³', '€', '¤', '¬', '¦', '¥', '©', '®', '«', '»', '±', '×', '÷', '¶', '·', '°', '½', '¼', '¾'
    ]

    # 1. Vérification de la longueur
    if not (6 <= len(mdp) <= 16):
        erreurs.append("Le mot de passe doit contenir entre 6 et 16 caractères.")
    # 2. Vérification des chiffres
    if not any(n in mdp for n in numeros):
        erreurs.append("Le mot de passe doit contenir au moins un chiffre (0-9).")
    # 3. Vérification des majuscules
    if not any(char in mdp for char in majuscules):
        erreurs.append("Le mot de passe doit contenir au moins une majuscule.")
    # 4. Vérification des minuscules
    if not any(char in mdp for char in minuscules):
        erreurs.append("Le mot de passe doit contenir au moins une minuscule.")
    # 5. Vérification des caractères spéciaux acceptés
    if not any(char in mdp for char in caracteres_speciaux_acceptes):
        erreurs.append("Le mot de passe doit contenir au moins un caractère spécial parmi : " + " ".join(caracteres_speciaux_acceptes))
    # 6. Vérification des caractères spéciaux NON acceptés
    if any(char in mdp for char in caracteres_speciaux_non_acceptes):
        erreurs.append("Le mot de passe contient un caractère spécial non autorisé.")
    return erreurs

def demander_entree(prompt):
    while True:
        entree = input(prompt)
        if entree.upper() in ('C', 'Y'):
            print("\nOpération annulée. Au revoir !")
            exit()
        return entree

def main():
    print("Bienvenue ! Tapez 'C' ou 'Y' à tout moment pour quitter.")

    while True:
        usr = demander_entree("Quel est votre nom d'utilisateur ? : ")
        erreurs_usr = valider_nom_utilisateur(usr)
        if erreurs_usr:
            print("\nNom d'utilisateur INVALIDE. Voici les erreurs :")
            for erreur in erreurs_usr:
                print(f"— {erreur}")
            continue  # Redemande le nom d'utilisateur

        mdp = demander_entree("Quel est votre mot de passe ? : ")
        erreurs_mdp = valider_mot_de_passe(mdp)
        if erreurs_mdp:
            print("\nMot de passe INVALIDE. Voici les erreurs :")
            for erreur in erreurs_mdp:
                print(f"— {erreur}")
            continue  # Redemande le mot de passe

        # Si tout est valide
        print("\nNom d'utilisateur et mot de passe VALIDES !")
        break

if __name__ == "__main__":
    main()
