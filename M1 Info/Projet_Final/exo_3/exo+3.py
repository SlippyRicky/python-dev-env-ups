import numpy as np
import matplotlib.pyplot as plt
import os

# --- 1. Constantes et Paramètres ---
T2 = 0.1         # Temps de relaxation transversale (s)
M0 = 1.0         # Aimantation initiale
GAMMA = 42.58    # MHz/T

# NOTE IMPORTANTE POUR LA VISUALISATION :
# Dans la réalité, pour B0 = 1.5 T, la fréquence est ~64 MHz.
# Sur 0.2s, cela ferait 12 millions d'oscillations (impossible à tracer proprement).
# On utilise ici un "B0 effectif" très faible pour voir les oscillations sur le graphe.
B0_eff = 0.0005  # Champ très faible pour avoir une fréquence visible (~21 kHz -> encore trop rapide, on réduit encore)
# Pour l'exercice pédagogique, fixons une fréquence arbitraire visible de 50 Hz
f_larmor = 50.0  # Hz (Oscillations par seconde)

# --- 2. Création de l'axe temporel ---
# On étudie le signal sur [0, 0.2] secondes
# Il faut beaucoup de points pour bien capturer les oscillations sinusoïdales
dt = 0.0001  # Pas de temps (100 microsecondes)
t = np.arange(0, 0.2, dt)

# --- 3. Génération du Signal S(t) ---
# Formule : S(t) = M0 * exp(-t/T2) * sin(2*pi*f*t)
enveloppe = M0 * np.exp(-t / T2)
oscillation = np.sin(2 * np.pi * f_larmor * t)
S = enveloppe * oscillation

# --- 4. Calcul de la Dérivée (Différences Finies Centrées) ---
# dS/dt ≈ (S[i+1] - S[i-1]) / (2*dt)
dSdt = np.zeros_like(S)

# Calcul pour les points intérieurs (de 1 à N-1)
# C'est la méthode "centrée", la plus précise pour ce niveau
dSdt[1:-1] = (S[2:] - S[:-2]) / (2 * dt)

# Gestion des bords (Forward pour le début, Backward pour la fin)
dSdt[0]  = (S[1] - S[0]) / dt       # Différence avant
dSdt[-1] = (S[-1] - S[-2]) / dt     # Différence arrière

# --- 5. Tracé Graphique ---
plt.figure(figsize=(12, 8))

# Sous-graphe 1 : Le Signal S(t)
plt.subplot(2, 1, 1)
plt.plot(t, S, label='Signal S(t)', color='navy')
plt.plot(t, enveloppe, '--', color='orange', label='Enveloppe T2', linewidth=1.5)
plt.plot(t, -enveloppe, '--', color='orange', linewidth=1.5) # Enveloppe négative
plt.title(f"Signal Spin-Echo Simulé (T2={T2}s, f={f_larmor}Hz)")
plt.ylabel("Amplitude (u.a.)")
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)

# Sous-graphe 2 : La Dérivée dS/dt
plt.subplot(2, 1, 2)
plt.plot(t, dSdt, label="Dérivée dS/dt", color='crimson')
plt.title("Dérivée temporelle du signal (Différences Finies)")
plt.xlabel("Temps (s)")
plt.ylabel("Vitesse de variation")
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)

plt.tight_layout()

# --- 6. Sauvegarde ---
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
save_path = os.path.join(output_dir, "spin_echo_derivative.png")
plt.savefig(save_path)
print(f"Graphique sauvegardé sous '{save_path}'")
plt.show()

# --- 7. Analyse Textuelle ---
print("\n--- Analyse des Résultats ---")
print(f"1. Atténuation : Le signal oscille mais s'écrase vite. À t=0.2s (2*T2),")
print(f"   l'amplitude ne vaut plus que {np.exp(-0.2/T2)*100:.1f}% de l'initiale.")
print("2. Dérivée : Elle est déphasée (c'est un cosinus approximatif) mais suit")
print("   la même enveloppe exponentielle décroissante.")
print("3. Méthode : Les différences finies centrées capturent bien la pente locale,")
print("   sauf aux bords où l'approximation est moins robuste.")
