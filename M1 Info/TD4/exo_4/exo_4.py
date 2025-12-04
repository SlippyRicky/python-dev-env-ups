import numpy as np
import matplotlib as plt

# 2. Définition des constantes et paramètres
g = 9.81  # Accélération due à la gravité (m/s²)
dt = 0.0001  # Pas de temps initial (s)
r = 0.03  # Rayon de la balle de tennis (m)
y0 = 1.5  # Hauteur initiale (m)
vy0 = 0.0  # Vitesse initiale (m/s)

# Initialisation des variables
y = y0  # Position initiale
vy = vy0  # Vitesse initiale
t = 0.0  # Temps initial
i = 0  # Compteur d'itérations

# Initialisation des listes pour stocker les valeurs de position, vitesse et temps
y_values = [y0]
vy_values = [vy0]
time_values = [t]


# 3. Application de la méthode d'Euler
while y > r:
    # Calcul de la nouvelle vitesse
    vy = vy - g * dt
    # Calcul de la nouvelle position
    y = y + vy * dt
    # Incrémentation du temps et du compteur
    t += dt
    i += 1
    # Stockage des valeurs
    y_values.append(y)
    vy_values.append(vy)
    time_values.append(t)

# 4. Affichage graphique
plt.figure(figsize=(3,12))
plt.plot(time_values, y_values, label = "Méthode D\'Euler")
plt.title('Chute libre d\'une balle de rayon r = 3cm')
plt.xlabel('Temps (s)')
plt.ylabel('Position (m)')
plt.show()


# 5. Calcul et affichage de la solution analytique


# 6. Ajout des légendes et affichage

# 7. Test avec différents pas de temps
for dt in dt_values:
    y = y0
    vy = vy0
    t = 0.0
    y_euler = [y0]
    t_euler = [t]

    while y > r:
        vy = vy - g * dt
        y = y + vy * dt
        t += dt
        y_euler.append(y)
        t_euler.append(t)

    plt.plot(t_euler, y_euler, '--', label=f'Pas de temps = {dt:.4f} s')

plt.plot(t_analyt, y_analyt, 'k-', lw=2.5, label='Solution analytique')
plt.title('Comparaison des solutions avec différents pas de temps')
plt.xlabel('Temps (s)')
plt.ylabel('Position (m)')
plt.grid(True)
plt.legend()


# 8. Représentation graphique de la vitesse et de la position en fonction du temps


# Affichage du temps de chute et du nombre d'itérations
print(f"Temps de chute : {round(t, 3)} s")
print(f"Nombre d'itérations : {i}")
print(f"Pas de temps : {dt} s")
