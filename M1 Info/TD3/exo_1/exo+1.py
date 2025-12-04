import matplotlib.pyplot as plt
import numpy as np
import os

# Configuration pour le mode sombre
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
    'figure.figsize': (12, 9),
    'figure.dpi': 300
})

# Créer le dossier s'il n'existe pas
os.makedirs('Images', exist_ok=True)

# Données de Millikan (fréquence en Hz, tension en V)
x = np.array([3.5874e+14, 5.931e+14, 7.4307e+14, 8.2193e+14, 9.6074e+14, 1.184e+15])
y = np.array([0.5309, 1.0842, 1.2734, 1.6598, 2.19856, 3.10891])
N = len(x)

# --- Calcul des moindres carrés ---
Ex = np.sum(x)/N
Ey = np.sum(y)/N
Exx = np.sum(x*x)/N
Exy = np.sum(x*y)/N
m = (Exy - Ex*Ey) / (Exx - Ex**2)
c = (Exx*Ey - Ex*Exy) / (Exx - Ex**2)

# --- Calcul des incertitudes ---
y_fit = m*x + c
residus = y - y_fit
sigma_y = np.std(residus, ddof=2)  # Écart-type des résidus
sigma_m = sigma_y / np.sqrt(N * (Exx - Ex**2))
sigma_c = sigma_y * np.sqrt(Exx / (N * (Exx - Ex**2)))

# --- Calcul de h et son incertitude ---
e = 1.602e-19  # Charge de l'électron (C)
h = m * e
sigma_h = sigma_m * e
h_known = 6.62607015e-34  # Valeur connue de h (J·s)

# --- Droite de régression ---
x_line = np.array([min(x), max(x)])
y_line = m*x_line + c

# --- Création du graphique ---
fig, ax = plt.subplots()
ax.scatter(x/1e14, y, color='#5DADE2', s=100, edgecolor='white', zorder=1, label='Données expérimentales')
ax.plot(x_line/1e14, y_line, color='#F5B041', linewidth=2,
        label=f'Ajustement : $V = ({m:.2e} \\pm {sigma_m:.1e})\\nu + ({c:.2f} \\pm {sigma_c:.2f})$')

# --- Lignes verticales (résidus) ---
for xi, yi in zip(x, y):
    ax.plot([xi/1e14, xi/1e14], [yi, m*xi + c], color='#EC7063', linestyle='--', alpha=0.5, linewidth=0.8)

# --- Personnalisation ---
ax.set_title('Détermination de la constante de Planck ($h$) par l\'effet photoélectrique (Millikan, 1923)', pad=20)
ax.set_xlabel('Fréquence ($\\nu$, en $10^{14}$ Hz)')
ax.set_ylabel('Tension d\'arrêt ($V$, en V)')
ax.grid(axis='both', linestyle='--', alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(0.5)
ax.spines['bottom'].set_linewidth(0.5)
ax.legend(loc='upper left', fontsize=10)

# --- Annotations des points ---
for xi, yi in zip(x, y):
    ax.text(xi/1e14, yi+0.05, f'({xi/1e14:.2f}, {yi:.2f})', ha='center', color='white', fontsize=8)

plt.tight_layout()

# --- Sauvegarde ---
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'Images', 'millikan_photoelectric_dark.png')
plt.savefig(image_path, bbox_inches='tight', dpi=300)
plt.close()

# --- Affichage des résultats ---
print("\n" + "="*60)
print("RÉSULTATS DE L'AJUSTEMENT LINÉAIRE (EFFET PHOTOÉLECTRIQUE)".center(60))
print("="*60)
print(f"\nÉquation de la droite d'ajustement :")
print(f"  V(ν) = ({m:.2e} ± {sigma_m:.1e}) ν + ({c:.2f} ± {sigma_c:.2f})")
print(f"\nConstante de Planck calculée :")
print(f"  h = ({h:.3e} ± {sigma_h:.1e}) J·s")
print(f"  Écart relatif à la valeur connue : {abs(h - h_known)/h_known:.2%}")
print(f"\nValeur connue de h : {h_known:.3e} J·s")
print(f"\nCoefficient de corrélation (r) : {np.corrcoef(x, y)[0,1]:.4f}")
print(f"Écart-type des résidus (σ_y) : {sigma_y:.4f} V")
print(f"Nombre de points (N) : {N}")

print("\n" + "-"*60)
print("DÉTAILS DES CALCULS".center(60))
print("-"*60)
print(f"Moyenne des fréquences (Ex) : {Ex:.2e} Hz")
print(f"Moyenne des tensions (Ey) : {Ey:.2f} V")
print(f"Moyenne des carrés des fréquences (Exx) : {Exx:.2e} Hz²")
print(f"Moyenne des produits (Exy) : {Exy:.2e} Hz·V")
print(f"Pente (m) : {m:.2e} V/Hz ± {sigma_m:.1e}")
print(f"Ordonnée à l'origine (c) : {c:.2f} V ± {sigma_c:.2f}")
print(f"Fonction de travail estimée (ϕ = -e·c) : {abs(c)*e:.2e} J")
print("="*60)
print(f"\nGraphique enregistré : {image_path}")
print("="*60)
