import numpy as np

# Définir les dimensions de la matrice
m = 3  # nombre de lignes
n = 4  # nombre de colonnes

# Créer la matrice A où chaque élément a_ij = i * j
A = np.array([[i * j for j in range(1, n + 1)] for i in range(1, m + 1)])

# Afficher la matrice A
print("Matrice A :")
print(A)

# Extraire les vecteurs v et w correspondant à la première et dernière colonne
v = A[:, 0]  # Première colonne
w = A[:, -1]  # Dernière colonne

# Afficher les vecteurs v et w
print("\nVecteur v (première colonne) :", v)
print("Vecteur w (dernière colonne) :", w)

# Calculer le produit scalaire entre v et w
produit_scalaire = np.dot(v, w)

# Afficher le produit scalaire
print("\nProduit scalaire entre v et w :", produit_scalaire)
