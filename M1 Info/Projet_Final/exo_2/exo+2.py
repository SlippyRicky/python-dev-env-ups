import numpy as np
import matplotlib.pyplot as plt

# --- 1. Constantes et Paramètres ---
T1 = 0.8  # Temps de relaxation longitudinale (s)
T2 = 0.1  # Temps de relaxation transversale (s)
M0 = 1.0  # Aimantation à l'équilibre

# --- 2. Création de l'axe temporel (Vectorisation) ---
# De 0 à 2 secondes, 100 points pour avoir des courbes lisses
t = np.linspace(0, 2, 100)

# --- 3. Calcul des Aimantations (Formules Analytiques) ---
# Relaxation Longitudinale (Mz) : Retour progressif vers M0 (1 - exp)
Mz = M0 * (1 - np.exp(-t / T1))

# Relaxation Transversale (Mxy) : Décroissance rapide vers 0 (exp décroissante)
Mxy = M0 * np.exp(-t / T2)

# --- 4. Affichage des Résultats (Tableau Textuel) ---
print("\n\n")
print("--- Simulation Relaxation T1 & T2 ---")
print(f"{'Temps (s)':<10} | {'Mz (Longi)':<15} | {'Mxy (Trans)':<15}")
print("-" * 45)

# On affiche seulement quelques points clés pour ne pas surcharger la console
# On utilise slicing [::10] pour afficher 1 ligne sur 10
for time_val, z_val, xy_val in zip(t[::10], Mz[::10], Mxy[::10]):
    print(f"{time_val:<10.2f} | {z_val:<15.2f} | {xy_val:<15.2f}")

print("-" * 45)

# --- 5. Tracé Graphique (Matplotlib) ---
plt.figure(figsize=(10, 6))

# Courbe Mz (Bleu)
plt.plot(t, Mz, label=f'Mz (Longitudinale, T1={T1}s)', color='blue', linewidth=2)
# Courbe Mxy (Rouge)
plt.plot(t, Mxy, label=f'Mxy (Transversale, T2={T2}s)', color='red', linewidth=2)

# Lignes repères visuelles
plt.axhline(y=M0, color='gray', linestyle='--', alpha=0.5, label='M0 (Équilibre)')
plt.axvline(x=T2, color='red', linestyle=':', alpha=0.5, label='t = T2')
plt.axvline(x=T1, color='blue', linestyle=':', alpha=0.5, label='t = T1')

plt.title("Évolution des Aimantations : Relaxation T1 vs T2")
plt.xlabel("Temps (s)")
plt.ylabel("Aimantation (M/M0)")
plt.legend()
plt.grid(True, alpha=0.3)

# Sauvegarde et affichage
plt.savefig("relaxation_T1_T2.png")
print("Graphique généré et sauvegardé sous 'relaxation_T1_T2.png'")
plt.show()

# --- 6. Analyse Finale ---
print("\nAnalyse des résultats :")
print(f"- Mxy décroît très vite (T2={T2}s) : perte rapide de cohérence.")
print(f"- Mz remonte lentement (T1={T1}s) : retour progressif à l'équilibre.")
print("Cela explique pourquoi il faut mesurer le signal rapidement après l'impulsion (avant que Mxy ne disparaisse).\n\n")
