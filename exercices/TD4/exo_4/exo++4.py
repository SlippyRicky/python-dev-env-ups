import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.animation import FuncAnimation

# Configuration des paramètres graphiques
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
    'figure.figsize': (18, 6),
    'figure.dpi': 100
})

# Créer un dossier pour sauvegarder les figures
if not os.path.exists('Graphiques'):
    os.makedirs('Graphiques')

# Constantes et paramètres
g = 9.81  # Accélération due à la gravité (m/s²)
r = 0.03  # Rayon de la balle de tennis (m)
vy0 = 0.0  # Vitesse initiale (m/s)

def simulate_and_animate_fall(y0, dt):
    # Simulation de la chute
    y = y0
    vy = vy0
    t = 0.0
    y_values = [y0]
    vy_values = [vy0]
    time_values = [t]

    while y > r:
        vy = vy - g * dt
        y = y + vy * dt
        t += dt
        y_values.append(y)
        vy_values.append(vy)
        time_values.append(t)

    # Solution analytique pour comparaison
    t_analyt = np.linspace(0, time_values[-1], 1000)
    y_analyt = y0 - 0.5 * g * t_analyt**2

    # Configuration des graphiques
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6), constrained_layout=True)
    fig.suptitle(f'Simulation de Chute (Hauteur initiale: {y0:.2f} m, dt: {dt:.4f} s)', color=plt.rcParams['text.color'])

    # Graphique 1 : Position en fonction du temps (Euler vs Analytique)
    ax1.plot(time_values, y_values, label='Méthode d\'Euler', color='cyan')
    ax1.plot(t_analyt, y_analyt, 'r-', lw=2.5, label='Solution Analytique')
    ax1.set_title('Position en fonction du Temps')
    ax1.set_xlabel('Temps (s)')
    ax1.set_ylabel('Position (m)')
    ax1.grid(True)
    ax1.legend()

    # Graphique 2 : Vitesse en fonction du temps
    ax2.plot(time_values, vy_values, 'g-', label='Vitesse')
    ax2.set_title('Vitesse en fonction du Temps')
    ax2.set_xlabel('Temps (s)')
    ax2.set_ylabel('Vitesse (m/s)')
    ax2.grid(True)
    ax2.legend()

    # Graphique 3 : Animation en temps réel de la chute
    ax3.set_title('Animation de la Chute')
    ax3.set_xlabel('Temps (s)')
    ax3.set_ylabel('Position (m)')
    ax3.set_xlim(0, time_values[-1])
    ax3.set_ylim(0, y0 * 1.1)
    ax3.grid(True)

    line, = ax3.plot([], [], 'o', color='gold', markersize=10, label='Position de la Balle')
    time_text = ax3.text(0.05, 0.95, '', transform=ax3.transAxes, color=plt.rcParams['text.color'])
    position_text = ax3.text(0.05, 0.90, '', transform=ax3.transAxes, color=plt.rcParams['text.color'])
    ax3.legend()

    def init():
        line.set_data([], [])
        time_text.set_text('')
        position_text.set_text('')
        return line, time_text, position_text

    def update(frame):
        current_time = time_values[frame]
        current_position = y_values[frame]
        line.set_data([current_time], [current_position])
        time_text.set_text(f'Temps: {current_time:.2f} s')
        position_text.set_text(f'Position: {current_position:.2f} m')
        return line, time_text, position_text

    ani = FuncAnimation(fig, update, frames=len(time_values), init_func=init, blit=True, interval=dt * 1000)
    plt.show()

    # Sauvegarder l'animation (optionnel)
    # ani.save('Graphiques/ball_fall_animation.gif', writer='pillow', fps=30)

# Demander à l'utilisateur les paramètres
y0 = float(input("Entrez la hauteur initiale (en mètres) : "))
dt = float(input("Entrez le pas de temps (en secondes) : "))

# Lancer la simulation
simulate_and_animate_fall(y0, dt)
