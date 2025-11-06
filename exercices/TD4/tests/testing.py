import numpy as np

# --- Création d’un tableau ---
# a = np.eye(5, 5)
# print("Matrice identité 5x5 :\n", a)
#
# x = np.arange(0, 10, 1)
# print("Tableau x :", x)  # Affiche [0 1 2 3 4 5 6 7 8 9]
#
# y = np.arange(1, 8, 2)
# print("Tableau y :", y)  # Affiche [1 3 5 7]
#
# z = np.array([0, 1, 2, 5])
# print("Tableau z :", z)  # Affiche [0 1 2 5]
#
# v = np.array([[1, 2], [2, 3], [3, 4]])
# print("Tableau 2D v :\n", v)
# print("Type de v :", type(v))  # Affiche <class 'numpy.ndarray'>

# --- Opérations sur les vecteurs ---
x = np.arange(0, 11, 1)
y = 2 * x
print("x: ", x)
print("y: ", y)
# print("Taille de x :", np.size(x))  # 11
# print("Forme de x :", np.shape(x))  # (11,)
# print("Premier élément de x :", x[0])  # 0
# print("x au carré :", np.power(x, 2))  # [0, 1, 4, ..., 100]
# print("x à partir de l'indice 1 :", x[1:])  # [1, 2, ..., 10]
# print("x de l'indice 2 à 4 :", x[2:5])  # [2, 3, 4]
# print("x[2:2:6] :", x[2:2:6])  # Vide (début > fin)
x = x[2:-1]  # x devient [2, 3, ..., 9]
y = y[1:-2]  # y devient [2, 4, 6, 8, 10][1:-2] = [4, 6, 8]
# print("x: ", x)
# print("y: ", y)
# print("x + y :", x + y)  # Addition élément par élément

z = x < 5
print("x < 5 :", z)  # [True, True, True, False, False]
print("z en float :", z.astype(float))  # [1., 1., 1., 0., 0.]

# --- Éléments non nuls d’un vecteur ---
nz = np.nonzero([1, 2, 0, 0, 4, 0])  # Indices des éléments non nuls
print("Indices non nuls :", nz)  # (array([0, 1, 4]),)

# --- Opérations logiques ---
x = np.arange(0, 11, 1)
z2 = x > 3
z3 = x < 6
# print("z2 and z3 :", z2 and z3)  # ERREUR : utilise & pour les tableaux
print("z2 & z3 :", z2 & z3)  # [False False False True True True False ...]
