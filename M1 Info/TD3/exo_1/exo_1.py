import matplotlib.pyplot as plt
import numpy as np

# Données de Millikan
x = np.array([5.4874e+14, 6.931e+14, 7.4307e+14, 8.2193e+14, 9.6074e+14, 1.184e+15])  # Fréquences (Hz)
y = np.array([0.5309, 1.0842, 1.2734, 1.6598, 2.19856, 3.10891])  # Tensions (V)

# Calcul des quantités nécessaires
N = len(x)
E_x = np.sum(x) / N
E_y = np.sum(y) / N
E_xx = np.sum(x * x) / N
E_xy = np.sum(x * y) / N

# Calcul de m et c
m = (E_xy - E_x * E_y) / (E_xx - E_x**2)
c = (E_xx * E_y - E_x * E_xy) / (E_xx - E_x**2)

print(f"Valeurs calculées : m = {m:.6e}, c = {c:.6e}")

# Calcul des valeurs ajustées m*x + c
y_fit = m * x + c

# Tracé des données et de la droite
plt.figure()
plt.scatter(x, y, label="Données expérimentales")
plt.plot(x, y_fit, 'r-', label="Ajustement linéaire")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Tension (V)")
plt.legend()
plt.tight_layout()


# Calcul de la constante de Planck h
e = 1.602e-19  # Charge de l'électron (C)
h = m * e  # Puisque V = (h/e)ν - ϕ/e, donc m = h/e
print(f"Valeur calculée de h : {h:.6e} Js")
print(f"Valeur connue de h : 6.63e-34 Js")

plt.show()
