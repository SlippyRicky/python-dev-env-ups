import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from pathlib import Path

# ==============================================================================
# █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
# █   SECTION 1 : CONSTANTES PHYSIQUES ET PARAMÈTRES DU SYSTÈME             █
# █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
# ==============================================================================

# Conversion des unités en SI (Système International)
V_cm3 = 1000.0
V = V_cm3 * 1e-6  # Conversion cm^3 -> m^3

# Densité atomique (atomes/m^3)
rho = 6.022e28

# Nombre total d'atomes N
N_atoms = rho * V

# Constantes physiques
kB = 1.380649e-23  # J/K (Constante de Boltzmann standardisée)
Theta_D = 428.0    # K (Température de Debye)
Theta_E = 320.0    # K (Température d'Einstein - souvent ~0.75 * Theta_D pour comparaison)

# ==============================================================================
# █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
# █   SECTION 2 : DÉFINITION DES MODÈLES THÉORIQUES                         █
# █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
# ==============================================================================

def integrand_debye(x):
    """
    L'intégrant du modèle de Debye : x^4 * e^x / (e^x - 1)^2
    Utilise une gestion d'erreur pour éviter la division par zéro à x=0.
    """
    if x == 0:
        return 0
    try:
        return (x**4 * np.exp(x)) / (np.exp(x) - 1)**2
    except OverflowError:
        return 0

def heat_capacity_debye(T, N, V_sys, Theta_D, kB_const):
    """
    Calcule Cv selon le modèle de Debye via intégration numérique adaptative (QUADPACK).

    Physique :
    - À basse T : Comportement en T^3 (Loi de Debye).
    - À haute T : Tend vers 3Nk_B (Loi de Dulong-Petit).
    """
    # Préfacteur constant : 9 * N * kB
    prefactor = 9 * N * kB_const

    # Calcul pour chaque température
    cv_values = []
    for temp in np.atleast_1d(T):
        if temp == 0:
            cv_values.append(0)
            continue

        x_max = Theta_D / temp
        # L'intégration numérique de scipy est beaucoup plus précise que la somme de Riemann
        integral, error = quad(integrand_debye, 0, x_max)

        val = prefactor * (temp / Theta_D)**3 * integral
        cv_values.append(val)

    return np.array(cv_values)

def heat_capacity_einstein(T, N, Theta_E, kB_const):
    """
    Modèle d'Einstein : Suppose que tous les atomes vibrent à la même fréquence.
    Moins précis à très basse température (chute exponentielle trop rapide).
    """
    T = np.atleast_1d(T)
    x = Theta_E / T
    # Protection contre division par zéro ou overflow
    with np.errstate(over='ignore', invalid='ignore'):
        exp_x = np.exp(x)
        cv = 3 * N * kB_const * (x**2) * exp_x / (exp_x - 1)**2

    # Correction pour T=0 ou T très bas
    cv = np.nan_to_num(cv)
    return cv

def heat_capacity_dulong_petit(N, kB_const):
    """
    Loi classique de Dulong-Petit.
    Limite théorique à haute température.
    Valeur constante = 3 * N * kB.
    """
    return 3 * N * kB_const

# ==============================================================================
# █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
# █   SECTION 3 : CALCULS ET GÉNÉRATION DES DONNÉES                         █
# █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
# ==============================================================================

# Plage de température : de 5K à 1000K (pour bien voir le plateau)
T_range = np.linspace(5, 1000, 200)

# 1. Calcul Debye
Cv_Debye = heat_capacity_debye(T_range, N_atoms, V, Theta_D, kB)

# 2. Calcul Einstein (Comparaison)
Cv_Einstein = heat_capacity_einstein(T_range, N_atoms, Theta_E, kB)

# 3. Limite Dulong-Petit
Cv_DP = heat_capacity_dulong_petit(N_atoms, kB)
Cv_DP_line = np.full_like(T_range, Cv_DP)

# ==============================================================================
# █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
# █   SECTION 4 : VISUALISATION SCIENTIFIQUE (PLOTTING)                     █
# █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
# ==============================================================================

# Configuration du style pour publication
plt.rcParams.update({
    'font.size': 12,
    'font.family': 'serif',
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'legend.fontsize': 12,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'lines.linewidth': 2.5
})

fig, ax = plt.subplots(figsize=(12, 7))

# --- Tracé des courbes ---

# Ligne asymptotique (Dulong-Petit)
ax.plot(T_range, Cv_DP_line, color='gray', linestyle='--', linewidth=2,
        label=r'Limite Classique (Dulong-Petit) $3Nk_B$', alpha=0.7)

# Modèle d'Einstein
ax.plot(T_range, Cv_Einstein, color='#E67E22', linestyle='-.', linewidth=2,
        label=r"Modèle d'Einstein ($\Theta_E = 320$ K)")

# Modèle de Debye (Le principal)
ax.plot(T_range, Cv_Debye, color='#2980B9', linestyle='-', linewidth=3,
        label=r'Modèle de Debye ($\Theta_D = 428$ K)')

# --- Annotations et "Storytelling" du graphique ---

# Zone Basse Température
ax.text(69, Cv_DP*0.2, r"$\propto T^3$ (Phonons acoustiques)",
        color='#2980B9', fontsize=12, fontweight='bold')

# Zone Haute Température
ax.text(600, Cv_DP*0.92, r"Saturation des modes",
        color='gray', fontsize=10, style='italic')

# Marquer Theta_D sur l'axe X
ax.axvline(x=Theta_D, color='red', linestyle=':', alpha=0.5)
ax.text(Theta_D + 10, 0, r'$\Theta_D$', color='red', va='bottom')

# --- Mise en forme finale ---

ax.set_title(r"Capacité Thermique du Solide : Debye vs Einstein", pad=20)
ax.set_xlabel(r"Température $T$ (K)")
ax.set_ylabel(r"Capacité Thermique $C_V$ (J/K)")
ax.set_xlim(0, 1000)
ax.set_ylim(0, Cv_DP * 1.1)

# Grille et Légende (CORRIGÉE ICI)
ax.grid(True, which='both', linestyle='--', alpha=0.6)
ax.legend(loc='lower right', frameon=True, shadow=True, fancybox=True, facecolor='white')

# --- Sauvegarde ---
script_dir = Path(__file__).parent
output_dir = script_dir / "output"
output_dir.mkdir(exist_ok=True)
image_path = output_dir / "Scientific_CV_Analysis.png"
plt.savefig(image_path, dpi=300, bbox_inches='tight')

print(f"✅ Analyse terminée. Graphique sauvegardé : {image_path}")
plt.show()
