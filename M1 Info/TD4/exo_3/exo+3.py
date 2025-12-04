import numpy as np

# Définir les dimensions de la matrice
m = 3  # nombre de lignes
n = 4  
A = np.array([[i * j for j in range(1, n + 1)] for i in range(1, m + 1)])

print("Matrice A :")
print(A)

v = A[:, 0]
w = A[:, -1]

print("\nVecteur v (première colonne) :", v)
print("Vecteur w (dernière colonne) :", w)

produit_scalaire = np.dot(v, w)

print("\nProduit scalaire entre v et w :", produit_scalaire)
