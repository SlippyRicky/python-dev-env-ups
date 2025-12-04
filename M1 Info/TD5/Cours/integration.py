import math
import matplotlib.pyplot as plt
import numpy as np

def integrer_sin(a, b, n, methode="rectangles_gauche"):
    """
    Calcule l'intégrale de sin(x) entre a et b en utilisant n rectangles ou trapèzes.

    Paramètres :
    - a : borne inférieure
    - b : borne supérieure
    - n : nombre de rectangles/trapèzes
    - methode : "rectangles_gauche", "rectangles_droit", "rectangles_milieu" ou "trapezes"
    """
    delta_x = (b - a) / n  # Largeur de chaque rectangle/trapèze
    somme = 0.0  # Initialiser la somme
    x_vals = np.linspace(a, b, n+1)  # Discrétisation de l'intervalle
    y_vals = np.sin(x_vals)  # Valeurs de la fonction sin(x)

    if methode == "rectangles_gauche":
        for i in range(n):
            somme += y_vals[i] * delta_x  # Aire du rectangle à gauche

    elif methode == "rectangles_droit":
        for i in range(n):
            somme += y_vals[i+1] * delta_x  # Aire du rectangle à droite

    elif methode == "rectangles_milieu":
        for i in range(n):
            x_mid = (x_vals[i] + x_vals[i+1]) / 2
            somme += math.sin(x_mid) * delta_x  # Aire du rectangle au milieu

    elif methode == "trapezes":
        for i in range(n):
            somme += (y_vals[i] + y_vals[i+1]) * delta_x / 2  # Aire du trapèze

    return somme, x_vals, y_vals

def plot_integration(a, b, n, methode):
    # Calculer l'intégrale et obtenir les points pour le graphique
    integrale, x_vals, y_vals = integrer_sin(a, b, n, methode)
    delta_x = (b - a) / n

    # Créer le graphique
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='f(x) = sin(x)', color='blue', linewidth=2)

    # Dessiner les rectangles ou trapèzes
    for i in range(n):
        if methode == "rectangles_gauche":
            x_rect = [x_vals[i], x_vals[i], x_vals[i+1], x_vals[i+1]]
            y_rect = [0, y_vals[i], y_vals[i], 0]
            plt.fill_between(x_rect, y_rect, color='red', alpha=0.3)
        elif methode == "rectangles_droit":
            x_rect = [x_vals[i], x_vals[i], x_vals[i+1], x_vals[i+1]]
            y_rect = [0, y_vals[i+1], y_vals[i+1], 0]
            plt.fill_between(x_rect, y_rect, color='green', alpha=0.3)
        elif methode == "rectangles_milieu":
            x_mid = (x_vals[i] + x_vals[i+1]) / 2
            y_mid = math.sin(x_mid)
            x_rect = [x_vals[i], x_vals[i], x_vals[i+1], x_vals[i+1]]
            y_rect = [0, y_mid, y_mid, 0]
            plt.fill_between(x_rect, y_rect, color='purple', alpha=0.3)
        elif methode == "trapezes":
            x_trap = [x_vals[i], x_vals[i+1], x_vals[i+1], x_vals[i]]
            y_trap = [0, 0, y_vals[i+1], y_vals[i]]
            plt.fill_between(x_trap, y_trap, color='orange', alpha=0.3)

    plt.title(f'Intégration de sin(x) par la méthode des {methode}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    return integrale

# Paramètres
a = 0.0  # Borne inférieure
b = math.pi  # Borne supérieure (π radians)
n = 20  # Nombre de rectangles/trapèzes (réduit pour une meilleure visualisation)

# Calculer l'intégrale avec chaque méthode et afficher le graphique
methodes = ["rectangles_gauche", "rectangles_droit", "rectangles_milieu", "trapezes"]
integrale_exacte = 2.0  # Valeur exacte de l'intégrale de sin(x) entre 0 et π

for methode in methodes:
    integrale = plot_integration(a, b, n, methode)
    erreur = abs(integrale_exacte - integrale)
    print(f"Méthode {methode}: {integrale:.6f} (erreur: {erreur:.6f})")
