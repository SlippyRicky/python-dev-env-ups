import numpy as np
import matplotlib.pyplot as plt

# Fonction pour calculer la dérivée numérique en utilisant soit la méthode des différences finies avant, soit centrée
def compute_derivative(x, y, method="centered"):
    # Méthode des différences finies avant
    if method == "forward":
        # Initialiser un tableau pour stocker les valeurs de la dérivée
        yp = np.zeros(len(x) - 1)
        # Boucle sur chaque point (sauf le dernier)
        for i in range(len(x) - 1):
            # Approximer la dérivée en utilisant la formule des différences finies avant :
            # (y[i+1] - y[i]) / (x[i+1] - x[i])
            yp[i] = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
        # Les coordonnées x pour la dérivée sont les valeurs x originales (sauf la dernière)
        x_deriv = x[0:-1]

    # Méthode des différences finies centrées
    elif method == "centered":
        # Approximer la dérivée en utilisant la formule des différences finies centrées :
        # (y[1:] - y[:-1]) / (x[1:] - x[:-1])
        # Cela calcule la différence entre les valeurs y consécutives et divise par la différence des valeurs x
        yp = (y[1:] - y[:-1]) / (x[1:] - x[:-1])
        # Les coordonnées x pour la dérivée sont les points milieux entre les valeurs x originales
        x_deriv = (x[:-1] + x[1:]) / 2

    # Retourner les coordonnées x et les valeurs de la dérivée calculées
    return x_deriv, yp

# Définir le nombre de points
Nx = 101
# Créer un tableau de valeurs x de 0 à 10, équidistantes
x = np.linspace(0, 10, Nx)
# Calculer les valeurs y comme le cosinus des valeurs x
y = x**0.2+20*x+2

# Calculer la dérivée en utilisant la méthode des différences finies avant
x_forward, yp_forward = compute_derivative(x, y, method="forward")
# Calculer la dérivée en utilisant la méthode des différences finies centrées
x_centered, yp_centered = compute_derivative(x, y, method="centered")

# Commandes de traçage (non commentées comme demandé)
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="f(x) = cos(x)", linewidth=2)
plt.plot(x_forward, yp_forward, label="Différence avant", linestyle="--")
plt.plot(x_centered, yp_centered, label="Différence centrée", linestyle="--")
plt.legend()
plt.title("Dérivée numérique de cos(x)")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.grid(True)
plt.show()
