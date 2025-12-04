import numpy as np
import matplotlib.pyplot as plt
import os

# --- 1. Initialisation de l'espace (La Grille) ---
N = 512  # Taille de l'image (128x128 pixels)

# On définit un système de coordonnées de -1 à 1 pour faciliter la géométrie
# Cela permet de centrer les cercles en (0,0) facilement
x = np.linspace(-1, 1, N)
y = np.linspace(-1, 1, N)

# Création des grilles 2D (Matrices de coordonnées)
X, Y = np.meshgrid(x, y)

# --- 2. Création de l'image Noire ---
image_irm = np.zeros((N, N))

# --- 3. Définition des Tissus (Masques Booléens) ---
# Équation d'un cercle au centre a (x0,y0) : (x - x0)^2 + (y - y0)^2 = r^2

# Tissu 1 : Cortex (Grand disque central)
# Centré en (0,0), rayon 0.8
masque_cortex = (X**2 + Y**2 <= 0.8**2)

# Tissu 2 : Graisse (Deux petites zones brillantes)
# Zone 1 : décalée en haut à droite (0.4, 0.4), rayon 0.15
masque_graisse_1 = ((X - 0.4)**2 + (Y + 0.4)**2 <= 0.15**2)
# Zone 2 : décalée en haut à gauche (-0.4, 0.4), rayon 0.15
masque_graisse_2 = ((X + 0.4)**2 + (Y - 0.4)**2 <= 0.15**2)

# Tissu 3 : Liquide (Petit disque sombre au centre)
# Centré en (0,0), rayon 0.2
masque_liquide = (X**2 + Y**2 <= 0.2**2)

# --- 4. Attribution des Intensités ---
# On "peint" les intensités sur l'image.
# L'ordre est important : on peint les couches supérieures par-dessus les inférieures.

# Fond (déjà à 0)
image_irm[masque_cortex]    = 0.6  # Intensité moyenne (Gris)
image_irm[masque_graisse_1] = 0.9  # Intensité forte (Blanc, hyper-signal)
image_irm[masque_graisse_2] = 0.9
image_irm[masque_liquide]   = 0.2  # Intensité faible (Gris foncé, hypo-signal)

# --- 5. Ajout de Bruit (Simulation réaliste) ---
# Aucune IRM n'est parfaite, il y a toujours du "bruit thermique"
bruit = np.random.normal(0, 0.05, (N, N))  # Moyenne 0, écart-type 0.05
image_bruitee = image_irm + bruit

# On s'assure que les valeurs restent entre 0 et 1 (clipping)
image_bruitee = np.clip(image_bruitee, 0, 1)

# --- 6. Affichage et Sauvegarde ---
plt.figure(figsize=(8, 8))

# Affichage de l'image avec une colormap "gray" (niveaux de gris)
plt.imshow(image_bruitee, cmap='BrBG_r', extent=[-1, 1, -1, 1])
plt.colorbar(label='Intensité du Signal')
plt.title(f"Fantôme IRM Synthétique ({N}x{N} pixels)")
plt.xlabel("Position X")
plt.ylabel("Position Y")

# Sauvegarde
output_dir = "output"
plot_name = "irm_synthetique.png"
os.makedirs(output_dir, exist_ok=True)
save_path = os.path.join(output_dir, plot_name)
plt.savefig(save_path)
print(f"Image sauvegardée sous '{save_path}'")

# --- 7. Analyse Textuelle ---
print("\n--- Analyse de l'Image Synthétique ---")
print("1. Cortex (Gris moyen) : Forme la structure principale.")
print("2. Graisse (Brillant)  : Apparaît en hyper-signal (blanc), typique des séquences pondérées T1.")
print("3. Liquide (Sombre)    : Apparaît en hypo-signal au centre.")
print("4. Réalisme : L'ajout de bruit gaussien brise l'aspect artificiel 'trop lisse' des formes géométriques.")

plt.show()
