import numpy as np
import matplotlib.pyplot as plt

# Génération des données bruitées
x = np.linspace(0, 2 * np.pi, 100)
y = np.array([np.sin(xi) + 0.1 * np.random.random(size=x.shape)]for xi in x)

# Fonction pour calculer la dérivée avec la forward approximation
def forward_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

# Fonction pour calculer la dérivée avec la formule centrée à 5 points
def centered_five_point_derivative(f, x, h=1e-5):
    return (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12 * h)

# Définition de la fonction f(x) = sin(x) + bruit
def f(x):
    return np.sin(x) + 0.1 * np.random.random(size=x.shape)

# Calcul des dérivées
h = 1e-6
dy_forward = np.zeros_like(x)
dy_centered = np.zeros_like(x)

# On évite les bords pour la méthode centrée
for i in range(2, len(x)-2):
    dy_forward[i] = forward_derivative(y, x[i], h)
    dy_centered[i] = centered_five_point_derivative(np.sin, x[i], h)

# Dérivée théorique (cosinus)
dy_theoretical = np.cos(x)

# Tracé des résultats
plt.figure(figsize=(18, 10))
plt.plot(x, y, 'b', label='Données bruitées')
plt.plot(x[2:-2], dy_forward[2:-2], 'r--', linewidth = 3, label="Dérivée (forward)")
plt.plot(x[2:-2], dy_centered[2:-2], 'g*', linewidth = 1, label="Dérivée (5 points)")
# plt.plot(x, dy_theoretical, 'k', label="Dérivée théorique (cos)")
plt.legend()
plt.title("Comparaison des méthodes de calcul de dérivée")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.grid(True)
plt.show()
