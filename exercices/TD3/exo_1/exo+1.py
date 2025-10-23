import matplotlib.pyplot as plt
\
import numpy as np
import os

# Configuration pour le mode sombre (style similaire à votre graphique)
plt.rcParams.update({
    'figure.facecolor': '#1a1a1a',
    'axes.facecolor': '#1a1a1a',
    'axes.labelcolor': '#e0e0e0',
    'text.color': '#e0e0e0',
    'xtick.color': '#a0a0a0',
    'ytick.color': '#a0a0a0',
    'axes.edgecolor': '#303030',
    'grid.color': '#3a3a3a',
    'figure.titlesize': 16,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.figsize': (10, 5),
    'figure.dpi': 300
})

# Créer le dossier s'il n'existe pas
os.makedirs('Images', exist_ok=True)

# Données fournies
x = np.array([3.5874e+14, 5.931e+14, 7.4307e+14, 8.2193e+14, 9.6074e+14, 1.184e+15])
y = np.array([0.5309, 1.0842, 1.2734, 1.6598, 2.19856, 3.10891])

# Calcul des moindres carrés
N = len(x)
Ex = np.sum(x)/N
Ey = np.sum(y)/N
Exx = np.sum(x*x)/N
Exy = np.sum(x*y)/N

m = (Exy - Ex*Ey) / (Exx - Ex**2)
c = (Exx*Ey - Ex*Exy) / (Exx - Ex**2)

# Calcul de la droite de régression
x_line = np.array([min(x), max(x)])
y_line = m*x_line + c

# Création du graphique
fig, ax = plt.subplots()

# Tracer les points
ax.scatter(x, y, color='#5DADE2', s=100, edgecolor='white', zorder=3,
           label='Données mesurées')

# Tracer la ligne de régression
ax.plot(x_line, y_line, color='#F5B041', linewidth=2,
        label=f'Régression linéaire: y = {m:.2e}x + {c:.2e}')

# Tracer les lignes verticales (distances)
for xi, yi in zip(x, y):
    ax.plot([xi, xi], [yi, m*xi + c], color='#EC7063', linestyle='--',
            alpha=0.5, linewidth=0.8)

# Personnalisation
ax.set_title('Interpolation par moindres carrés', pad=20)
ax.set_xlabel('x (unité)')
ax.set_ylabel('y (unité)')
ax.grid(axis='both', linestyle='--', alpha=0.5)

# Améliorations visuelles (style similaire à votre graphique)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(0.5)
ax.spines['bottom'].set_linewidth(0.5)

# Fond alterné
for i in range(len(x)):
    if i % 2 == 0:
        ax.axvspan(i-0.5, i+0.5, color='#2a2a2a', alpha=0.3)

# Légende
# ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Annotations des points
for i, (xi, yi) in enumerate(zip(x, y)):
    ax.text(xi, yi+0.05, f'({xi:.1e}, {yi:.2f})',
            ha='center', color='white', fontsize=8)

plt.tight_layout()

# Sauvegarde
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'Images', 'least_squares_dark.png')
plt.savefig(image_path, bbox_inches='tight')
plt.close()

print(f"Graphique enregistré à : {image_path}")
print(f"Equation de la droite: y = {m:.2e}x + {c:.2e}")
print(f"Coefficient de corrélation: {np.corrcoef(x, y)[0,1]:.4f}")

# Affichage des calculs intermédiaires
print("\nCalculs intermédiaires:")
print(f"Ex = {Ex:.2e}")
print(f"Ey = {Ey:.2f}")
print(f"Exx = {Exx:.2e}")
print(f"Exy = {Exy:.2e}")
print(f"m = (Exy - Ex*Ey)/(Exx - Ex²) = {m:.2e}")
print(f"c = (Exx*Ey - Ex*Exy)/(Exx - Ex²) = {c:.2e}")
