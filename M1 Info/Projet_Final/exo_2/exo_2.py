import matplotlib.pyplot as plt
import numpy as np
import os

T1 = 0.8
T2 = 0.1
M0 = 1.0

t = np.linspace(0, 2, 100)

Mz = M0 * (1 - np.exp(-t/T1))
Mxy = M0 * (np.exp(-t/T2))

print("\n\n")
print("--- Simulation Relaxation T1 & T2 ---")
print(f"{'Temps (s)':<10} | {'Mz (Longi)':<15} | {'Mxy (Trans)':<15}")
print("-" * 45)

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

# Sauvegarde dans le dossier 'output'
output_dir = "output"
os.makedirs(output_dir, exist_ok=True) # Crée le dossier s'il n'existe pas
save_path = os.path.join(output_dir, "relaxation_T1_T2.png")

plt.savefig(save_path)
print(f"Graphique généré et sauvegardé sous '{save_path}'")
plt.show()

# --- 6. Analyse Finale ---
print("\nAnalyse des résultats :")
print(f"- Mxy décroît très vite (T2={T2}s) : perte rapide de cohérence.")
print(f"- Mz remonte lentement (T1={T1}s) : retour progressif à l'équilibre.")
print("Cela explique pourquoi il faut mesurer le signal rapidement après l'impulsion (avant que Mxy ne disparaisse).\n\n")
