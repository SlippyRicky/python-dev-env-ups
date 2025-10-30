import matplotlib.pyplot as plt
import numpy as np
import time

# Données de Millikan
x = np.array([5.4874e+14, 6.931e+14, 7.4307e+14, 8.2193e+14, 9.6074e+14, 1.184e+15])  # Fréquences (Hz)
y = np.array([0.5309, 1.0842, 1.2734, 1.6598, 2.19856, 3.10891])  # Tensions (V)
N = len(x)

# Mesurer le temps d'exécution avec np.sum
start_time = time.time()
E_x = np.sum(x) / N
E_y = np.sum(y) / N
E_xx = np.sum(x * x) / N
E_xy = np.sum(x * y) / N
end_time = time.time()
np_sum_time = end_time - start_time

# Calcul de m et c avec np.sum
m_np = (E_xy - E_x * E_y) / (E_xx - E_x**2)
c_np = (E_xx * E_y - E_x * E_xy) / (E_xx - E_x**2)

# Mesurer le temps d'exécution avec une boucle for
start_time = time.time()
E_x_loop = 0
E_y_loop = 0
E_xx_loop = 0
E_xy_loop = 0
for i in range(N):
    E_x_loop += x[i]
    E_y_loop += y[i]
    E_xx_loop += x[i] * x[i]
    E_xy_loop += x[i] * y[i]
E_x_loop /= N
E_y_loop /= N
E_xx_loop /= N
E_xy_loop /= N
end_time = time.time()
loop_time = end_time - start_time

# Calcul de m et c avec la boucle for
m_loop = (E_xy_loop - E_x_loop * E_y_loop) / (E_xx_loop - E_x_loop**2)
c_loop = (E_xx_loop * E_y_loop - E_x_loop * E_xy_loop) / (E_xx_loop - E_x_loop**2)

# Calcul des valeurs ajustées m*x + c
y_fit_np = m_np * x + c_np
y_fit_loop = m_loop * x + c_loop

# Afficher les temps d'exécution et les valeurs calculées
print(f"Temps d'exécution avec np.sum: {np_sum_time:.6f} secondes")
print(f"Temps d'exécution avec boucle for: {loop_time:.6f} secondes")

print(f"Valeurs calculées avec np.sum : m = {m_np:.6e}, c = {c_np:.6e}")
print(f"Valeurs calculées avec boucle for : m = {m_loop:.6e}, c = {c_loop:.6e}")

# Calcul de la constante de Planck h
e = 1.602e-19  # Charge de l'électron (C)
h_np = m_np * e
h_loop = m_loop * e
print(f"Valeur calculée de h avec np.sum : {h_np:.6e} Js")
print(f"Valeur calculée de h avec boucle for : {h_loop:.6e} Js")
print(f"Valeur connue de h : 6.63e-34 Js")

# Tracé des données et de la droite
plt.figure()
plt.scatter(x, y, label="Données expérimentales")
plt.plot(x, y_fit_np, 'r-', label="Ajustement linéaire (np.sum)")
plt.plot(x, y_fit_loop, 'g--', label="Ajustement linéaire (boucle for)")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Tension (V)")
plt.legend()
plt.tight_layout()
plt.show()
