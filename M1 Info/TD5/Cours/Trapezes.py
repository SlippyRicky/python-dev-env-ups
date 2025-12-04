import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 10*x**5+10*x**3 + 5*x**2 + 1

import numpy as np

a = -5
b = 5

# 1. Define a fixed number of intervals (e.g., 25)
N = 5

# 2. The step size (dx) is calculated dynamically
dx = (b - a) / N

# 3. Generate points
x_trap = np.linspace(a, b, N + 1)

print(f"Nombre d'intervalles (N) : {N}")
print(f"Taille des intervals: {dx}")

# --- Reste du script (Visualisation) ---

x_trap = np.linspace(a, b, N+1)
y_trap = f(x_trap)

# Calcul de l'aire (Trapèzes)
aire_approx = (dx / 2) * np.sum(2 * y_trap[1:-1] + y_trap[0] + y_trap[-1])

# Graphique
x_smooth = np.linspace(a, b, 1000)
plt.figure(figsize=(8, 5))
plt.plot(x_smooth, f(x_smooth), 'r', linewidth=2, label='Fonction f(x)')

# plt.ylim(f(a), f(b))

# Tracer les trapèzes
for i in range(N):
    xi = [x_trap[i], x_trap[i], x_trap[i+1], x_trap[i+1]]
    yi = [0, f(x_trap[i]), f(x_trap[i+1]), 0]
    plt.fill(xi, yi, 'b', alpha=0.5, edgecolor='black')

plt.fill([], [], 'b', alpha=0.5, edgecolor='black', label='Trapèzes') # Pour légende
plt.title(f"Méthode des Trapèzes (N={N})\nAire approchée ≈ {aire_approx:.4f}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
