# ENONCE
########################################################
# Les hydrogénoïdes (hydrogène, ou atomes ionisés
# à un électron) émettent de la lumière à des
# longueurs d’ondes précises déterminées par la
# formule de Rydberg, que vous trouverez à la page
# suivante : https://en.wikipedia.org/wiki/Rydberg_formula
#
# —  Après avoir lu avec attention la section
#    "Formule de Rydberg pour l’hydrogène" de la
#    page wikipédia, écrire un programme qui imprime
#    à l’écran la longueur d’onde des 4 premières
#    raies de la série de Lyman.
#
# —  À quelle série et quelles transitions ces raies
#    de l’hydrogène correspondent-elle ?
#
# Vous souhaitez généraliser votre programme pour
# aussi traiter le cas des hydrogénoïdes, en
# particulier l’hélium simplement ionisé (noté
# HeII en astronomie, HeI étant l’hélium neutre) :
#
# —  Après avoir lu avec attention la section
#    "Généralisation aux hydrogénoïdes", généralisez
#    votre programme précédent pour traiter le cas Z=2.
#
# —  Déterminez à quelles transitions correspondent
#    les raies HeII observées dans le spectre de la
#    nova V630 Sgr. Qu’en est-il des raies HeI ?
########################################################

import numpy as np

# Constantes
R = 1.0973731568539e7  # Constante de Rydberg (m^-1)
c = 2.99792458e8       # Vitesse de la lumière (m/s)

def longueur_onde_Lyman(Z, n_final=1, n_max=5):
    """Calcule les longueurs d'onde des raies de Lyman pour un hydrogénoïde de numéro atomique Z."""
    for n in range(2, n_max):
        # Formule de Rydberg généralisée : 1/λ = R*Z^2*(1/n_final^2 - 1/n^2)
        inv_lambda = R * Z**2 * (1/n_final**2 - 1/n**2)
        lambda_m = 1/inv_lambda  # Longueur d'onde en mètres
        print(f"Transition n={n} → n={n_final} : {lambda_m:.3e} m")

# Hydrogène (Z=1)
print("Raies de Lyman pour l'hydrogène (Z=1) :")
longueur_onde_Lyman(Z=1)

# Hélium simplement ionisé (Z=2)
print("\nRaies de Lyman pour HeII (Z=2) :")
longueur_onde_Lyman(Z=2)
