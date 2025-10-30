import numpy as np
import matplotlib.pyplot as plt

# 1. Fonction f(x) = 1 / (1 - x)
def f1(x):
    return 1 / (1 - x)

# 2. Fonction f(x) = exp(sqrt(1 - a * x^2)) si |x| < 1/a, 0 sinon
def f2(x, a=1):
    return np.where(np.abs(x) < 1/a, np.exp(np.sqrt(1 - a * x**2)), 0)

# 3. Conversion radians → degrés
def rad_to_deg(radians):
    return radians * (180 / np.pi)

# Tracé de la fonction 1
x1 = np.linspace(-4.9, 4.9, 500)  # Évite x=1 pour éviter la division par zéro
y1 = f1(x1)

plt.figure(figsize=(10, 5))
plt.plot(x1, y1, label=r'$f(x) = \frac{1}{1-x}$')
plt.axvline(x=1, color='red', linestyle='--', label='Asymptote x=1')
plt.title("Fonction 1 : $f(x) = \frac{1}{1-x}$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()

# Tracé de la fonction 2 pour différentes valeurs de a
x2 = np.linspace(-5, 5, 1000)
a_values = [1, 0.5, 0.1, 0.01]

plt.figure(figsize=(10, 5))
for a in a_values:
    y2 = f2(x2, a)
    plt.plot(x2, y2, label=f'a = {a}')

plt.title("Fonction 2 : $f(x) = e^{\sqrt{1 - a x^2}}$ pour $|x| < 1/a$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()

# Exemple de conversion radians → degrés
angle_rad = np.pi / 4  # 45 degrés en radians
angle_deg = rad_to_deg(angle_rad)
print(f"Conversion : {angle_rad} radians = {angle_deg:.2f} degrés")
