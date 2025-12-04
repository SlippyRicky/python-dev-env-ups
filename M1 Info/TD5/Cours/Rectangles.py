import numpy as np
import matplotlib.pyplot as plt

# Définition de la fonction
def f(x):
    return 0.25 * x**2 + 1

# Paramètres d'intégration
a = 0       # Borne inférieure
b = 4       # Borne supérieure
N = 4       # Nombre d'intervalles (rectangles)

# Calculs pour la visualisation
dx = (b - a) / N                 # Largeur des intervalles
x_rect = np.linspace(a, b-dx, N) # Points à gauche (alpha = a)
y_rect = f(x_rect)               # Hauteurs correspondantes
aire_approx = np.sum(y_rect * dx) # Calcul de l'intégrale

# Affichage
x_smooth = np.linspace(a, b, 1000) # Pour tracer la courbe lisse
plt.figure(figsize=(8, 5))

# Tracer la fonction
plt.plot(x_smooth, f(x_smooth), 'r', linewidth=2, label='Fonction f(x)')

# Tracer les rectangles
# align='edge' permet de coller le rectangle à droite du point x
plt.bar(x_rect, y_rect, width=dx, align='edge', alpha=0.5, edgecolor='black', label='Rectangles (gauche)')

plt.title(f"Méthode des Rectangles (N={N})\nAire approchée ≈ {aire_approx:.4f}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
