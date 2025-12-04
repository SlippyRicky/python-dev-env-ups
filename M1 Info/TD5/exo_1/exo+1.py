"""
Résumé du code :
Ce script compare la dérivée numérique (calculée par différence centrale)
et la dérivée analytique de la fonction f(x) = 1 + 0.5 * tanh(2x).
Il évalue l'erreur moyenne absolue pour différentes valeurs du pas h,
puis trace l'évolution de cette erreur en fonction de h sur une échelle logarithmique.
L'objectif est d'illustrer comment l'erreur numérique varie avec la taille du pas h.
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# Définition de la fonction f(x)
def f(x):
    return 1 + 0.5 * math.tanh(2 * x)

# Dérivée analytique de f(x)
def df_analytique(x):
    return 1 / (np.cosh(2 * x))**2

# Approximation de la dérivée par différence centrale
def df_centrale(f, x, h):
    return (f(x + h/2) - f(x - h/2)) / h

# Création d'un intervalle de valeurs pour x
x = np.linspace(-2, 2, 1000)

# Calcul de la dérivée analytique pour chaque point de x
df_ana = np.array([df_analytique(xi) for xi in x])

# Liste des valeurs de h à tester
hs = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10, 1e-11, 1e-12]
erreurs = []

# Pour chaque valeur de h, calculer la dérivée numérique et l'erreur associée
for h in hs:
    df_num = np.array([df_centrale(f, xi, h) for xi in x])
    erreur = np.mean(np.abs(df_num - df_ana))  # Erreur moyenne absolue
    erreurs.append(erreur)

# Affichage des erreurs pour chaque h
print(erreurs)

# Tracé de l'erreur en fonction de h (échelle log-log)
plt.figure(figsize=(10, 6))
plt.loglog(hs, erreurs, 'o-')
plt.xlabel('Pas \( h \)')
plt.ylabel('Erreur moyenne absolue')
plt.title('Erreur en fonction du pas \( h \)')
plt.grid(True)
plt.show()
