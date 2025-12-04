import numpy as np

def demontrer_commandes_numpy():
    print("=== Démonstration des commandes NumPy ===\n")

    # 1. np.ones((3, 1)) : Matrice colonne
    matrice_colonne = np.ones((3, 1))
    print("1. np.ones((3, 1)) : Matrice colonne de 1")
    print(matrice_colonne)
    print("Forme :", matrice_colonne.shape, "\n")

    # 2. np.ones((1, 3)) : Matrice ligne
    matrice_ligne = np.ones((1, 3))
    print("2. np.ones((1, 3)) : Matrice ligne de 1")
    print(matrice_ligne)
    print("Forme :", matrice_ligne.shape, "\n")

    # 3. np.ones(3) : Vecteur 3D de
    vecteur = np.ones(3)
    print("3. np.ones(3) : Vecteur 3D de 1")
    print(vecteur)
    print("Forme :", vecteur.shape, "\n")

    # 4. np.eye(3) : Matrice identité 3x3
    matrice_identite = np.eye(3)
    print("4. np.eye(3) : Matrice identité 3x3")
    print(matrice_identite)
    print("Forme :", matrice_identite.shape, "\n")
    # 5. np.eye(3, 2) : Matrice diagonale 3x2
    matrice_diagonale = np.eye(3, 2)
    print("5. np.eye(3, 2) : Matrice diagonale 3x2")
    print(matrice_diagonale)
    print("Forme :", matrice_diagonale.shape, "\n")

    # Exemple d'utilisation : Multiplication matricielle
    print("=== Exemple d'utilisation : Multiplication matricielle ===")
    A = np.array([[1, 2], [3, 4], [5, 6]])
    print("Matrice A :\n", A)

    # Multiplication par l'identité
    resultat_identite = A @ np.eye(3)[:2, :2]  # On ajuste pour que les dimensions correspondent
    print("\nA multiplié par une sous-matrice identité (2x2) :\n", resultat_identite)

    # Utilisation de np.eye pour extraire des lignes
    print("\nUtilisation de np.eye(2, 3) pour extraire des lignes de A :")
    transformation = np.eye(2, 3)
    resultat_transformation = transformation @ A
    print("Résultat (2 premières lignes de A) :\n", resultat_transformation)

    # Exemple avec np.ones : Addition à un vecteur
    print("\n=== Exemple avec np.ones : Addition à un vecteur ===")
    vecteur_exemple = np.array([10, 20, 30])
    print("Vecteur d'exemple :", vecteur_exemple)
    print("Ajout de np.ones(3) :", vecteur_exemple + np.ones(3))

    # Sélection de colonnes avec slicing
    print("\n=== Sélection des 2 premières colonnes de B ===")
    B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    print("Matrice B (4x3) :\n", B)
    colonnes_selectionnees = B[:, :2]  # Sélectionne les 2 premières colonnes
    print("Sélection des 2 premières colonnes de B :\n", colonnes_selectionnees)

if __name__ == "__main__":
    demontrer_commandes_numpy()
