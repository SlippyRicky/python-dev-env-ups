import numpy as np
import matplotlib.pyplot as plt
import os

# Configuration du dark mode avec les couleurs en RGB normalisées
plt.rcParams.update({
    'figure.facecolor': (0.102, 0.102, 0.102),
    'axes.facecolor': (0.102, 0.102, 0.102),
    'axes.labelcolor': (0.878, 0.878, 0.878),
    'text.color': (0.878, 0.878, 0.878),
    'xtick.color': (0.627, 0.627, 0.627),
    'ytick.color': (0.627, 0.627, 0.627),
    'axes.edgecolor': (0.188, 0.188, 0.188),
    'grid.color': (0.227, 0.227, 0.227),
    'figure.titlesize': 16,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.figsize': (12, 9),
    'figure.dpi': 300
})

def f1(x):
    return 1 / (1 - x)

def f2(x, a=1):
    return np.where(np.abs(x) < 1/a, np.exp(np.sqrt(1 - a * x**2)), 0)

def rad_to_deg(radians):
    return radians * (180 / np.pi)

# Création du dossier "Graphiques" s'il n'existe pas
os.makedirs("Graphiques", exist_ok=True)

# Tracé de la fonction 1
x1 = np.linspace(-4.9, 4.9, 500)
y1 = f1(x1)


plt.figure()
plt.plot(x1, y1, label=r'$f(x) = \frac{1}{1-x}$', color='blue')
plt.axvline(x=1, color='red', linestyle='--', label='Asymptote x=1')
plt.title(r"Fonction 1 : $f(x) = \frac{1}{1-x}$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.savefig("Graphiques/fonction1.png", dpi=300, bbox_inches='tight', facecolor=plt.gcf().get_facecolor())
plt.close()

# Tracé de la fonction 2
x2 = np.linspace(-5, 5, 1000)
a_values = [1, 0.5, 0.1, 0.01]

plt.figure()
for a in a_values:
    y2 = f2(x2, a)
    plt.plot(x2, y2, label=f'a = {a}')

plt.title(r"Fonction 2 : $f(x) = e^{\sqrt{1 - a x^2}}$ pour $|x| < 1/a$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.savefig("Graphiques/fonction2.png", dpi=300, bbox_inches='tight', facecolor=plt.gcf().get_facecolor())
plt.close()

# Exemple de conversion radians → degrés
angle_rad = np.pi / 4
angle_deg = rad_to_deg(angle_rad)
print(f"Conversion : {angle_rad} radians = {angle_deg:.2f} degrés")
print("Les graphiques ont été sauvegardés dans le dossier 'Graphiques'.")