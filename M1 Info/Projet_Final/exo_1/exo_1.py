import numpy as np

GAMMA = 42.58  # Unit: MHz/T
B0_values = np.linspace(0, 10, 11)

larmor = GAMMA * B0_values

print("\n\n")
print("--- Fréquences de Larmor ---")
print(f"{'Champs (T)':<10} | {'Frequences (MHz)':<15}")
print("-" * 30)

for b0, freq in zip(B0_values, larmor):
    print(f"{b0:<10.1f} | {freq:<15.2f}")

print("-" * 30)
print(f"Frequences Max atteinte : {larmor.max():.2f} MHz, à {B0_values.max()} T.\n\n")

print(f"Analyse : La fréquence évolue linéairement de 0 à {larmor.max():.2f} MHz sur 10 T.\n\n\n")
