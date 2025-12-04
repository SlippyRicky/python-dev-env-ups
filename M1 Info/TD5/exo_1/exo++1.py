# Importer les bibliothèques nécessaires
import matplotlib.pyplot as plt
import numpy as np
from math import tanh

# Définir la taille du pas pour la différentiation numérique
h = np.float64(1e-7)

# Définir la plage des valeurs de x pour le tracé
x = np.linspace(-2, 2, 1000)

# Définir la fonction à différencier : f(x) = 0.5 * tanh(2x)
def f(x):
    return 1/2 * (tanh(x * 2))

# Approximation de la dérivée par différence avant : (f(x+h) - f(x))/h
def df_A(f, x, h):
    return (f(x + h) - f(x)) / h

# Approximation de la dérivée par différence centrée : (f(x+h/2) - f(x-h/2))/h
def df_C(f, x, h):
    return (f(x + h/2) - f(x - h/2)) / h

# Évaluer la fonction et ses approximations sur la plage de x
f_x = np.array([f(xi) for xi in x])  # Valeurs de la fonction
Dfx_A = np.array([df_A(f, xi, h) for xi in x])  # Valeurs de la différence avant
Dfx_C = np.array([df_C(f, xi, h) for xi in x])  # Valeurs de la différence centrée

# Créer une figure avec une taille spécifiée
plt.figure(figsize=(18, 10))

# Tracer la fonction originale f(x) = 0.5 * tanh(2x)
plt.plot(x, f_x, 'r-', linewidth=2, label='f(x) = 0.5 * tanh(2x)')

# Tracer l'approximation de la dérivée par différence avant
plt.plot(x, Dfx_A, 'g--', linewidth=3, label='Forward Difference Approximation: (f(x+h) - f(x))/h')

# Tracer l'approximation de la dérivée par différence centrée
plt.plot(x, Dfx_C, 'b.', markersize=0.5, label='Central Difference Approximation: (f(x+h/2) - f(x-h/2))/h')

# Ajouter une grille pour une meilleure lisibilité
plt.grid(True, linestyle='--', alpha=0.7)

# Étiqueter l'axe des x et l'axe des y
plt.xlabel('x', fontsize=14, labelpad=10)
plt.ylabel('f(x) and Approximate Derivatives', fontsize=14, labelpad=10)

# Ajouter un titre au graphique
plt.title('Comparaison des Méthodes de Différentiation Numérique pour f(x) = 0.5 * tanh(2x)', fontsize=16, pad=20)

# Ajouter une légende pour distinguer les tracés, placée en haut à droite
plt.legend(fontsize=12, loc='upper right')

# Ajouter une boîte de texte avec des informations supplémentaires, placée en bas à gauche
info_text = (
    "Méthodes de Différentiation Numérique:\n"
    "- Forward Difference: Approximation du premier ordre, O(h)\n"
    "- Central Difference: Approximation du second ordre, O(h²)\n"
    "- Taille du pas (h) = 1e-7"
)
plt.gca().text(
    0.02, 0.02, info_text, transform=plt.gca().transAxes,
    fontsize=12, verticalalignment='bottom', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8)
)

# Ajouter des étiquettes aux axes et améliorer la lisibilité des graduations
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Ajuster la mise en page pour éviter les chevauchements
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Afficher le graphique
plt.show()
