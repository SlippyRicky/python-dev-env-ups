import numpy as np

# Vecteurs
v1 = np.arange(1, 17)
v2 = np.arange(28, 10, -2)
v3 = 2 ** np.arange(0, 9)

# Tableau A
A = np.array([
    3 ** np.arange(0, 9),
    2 ** np.arange(0, 9),
    5 ** np.arange(0, 9)
])

# Affichage
print("v1 =", v1)
print("v2 =", v2)
print("v3 =", v3)
print("A =\n", A)
