import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Constantes données
V = 1000  # cm^3 (volume du solide)
rho = 6.022e28  # m^-3 (densité en nombre d'atomes par unité de volume)
kB = 1.30e-23  # m^2 kg s^-2 K^-1 (constante de Boltzmann)
theta_D = 428  # K (température de Debye)
T = 300  # K (température du système)

def f(x):
    return (x**4 * np.exp(x)) / (np.exp(x) - 1)**2

def cv(T, N, theta_D, V, rho, kB):
    a = 0
    b = theta_D / T
    delta_x = (b - a) / N
    integral = 0.0

    for k in range(N):
        x_mid = a + delta_x * (k + 0.5)
        integral += f(x_mid) * delta_x

    CV = 9 * V * rho * kB * (T / theta_D)**3 * integral
    return CV

def find_N(T, theta_D, V, rho, kB, precision_target):

    N = 1
    precision = 1.0  # Initialiser à une valeur supérieure à la précision cible

    while precision >= precision_target:
        N += 1
        I_N = cv(T, N, theta_D, V, rho, kB)
        I_N_minus_1 = cv(T, N-1, theta_D, V, rho, kB)
        precision = abs((I_N - I_N_minus_1) / I_N)

    return N

# Calculer N pour différentes précisions
precision_targets = [1e-4, 1e-6, 1e-8]
N_values = []

for precision in precision_targets:
    N = find_N(T, theta_D, V, rho, kB, precision)
    N_values.append(N)
    print(f"Nombre de points nécessaire pour une précision de {precision}: {N}")

# 4. Calculer CV(T) pour T variant de 10 à 500 K par pas de 10 K
T_range = np.arange(10, 501, 10)
CV_values = []

# Utiliser le N obtenu pour une précision de 1e-6
N = N_values[1]  # Car 1e-6 est le deuxième élément dans precision_targets

for temp in T_range:
    CV = cv(temp, N, theta_D, V, rho, kB)
    CV_values.append(CV)

# 5. Tracer la courbe de CV(T)
plt.figure(figsize=(10, 6))
plt.plot(T_range, CV_values, 'b-', linewidth=2)
plt.title("Capacité thermique $CV(T)$ d'un solide")
plt.xlabel("Température (K)")
plt.ylabel("Capacité thermique $CV(T)$")
plt.grid(True)

# Sauvegarder le graphique dans un dossier 'output' dans le répertoire du script
script_dir = Path(__file__).parent
output_dir = script_dir / "output"
output_dir.mkdir(exist_ok=True)
image_path = output_dir / "CV_T_plot.png"
plt.savefig(image_path, format='png', dpi=200, bbox_inches='tight')
print(f"Le graphique a été sauvegardé sous: {image_path.resolve()}")
plt.show()
