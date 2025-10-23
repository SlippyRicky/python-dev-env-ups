################################################################################
# En physique de la matière condensée, la constante de Madelung décrit le potentiel
# électrique ressenti par un atome dans un cristal. Pour le chlorure de sodium (NaCl) :
# - Les atomes de sodium (charge +e) sont aux positions (i,j,k) où i+j+k est pair.
# - Les atomes de chlore (charge -e) sont aux positions où i+j+k est impair.
#
# On place un atome de sodium à l'origine (i=j=k=0). La distance d'un atome (i,j,k)
# à l'origine est : a * sqrt(i² + j² + k²). Le potentiel créé par cet atome à l'origine
# est :
#   V(i,j,k) = ± e / (4πε₀a * sqrt(i² + j² + k²))
#   (signe + si i+j+k pair, - sinon).
#
# Le potentiel total est la somme de V(i,j,k) pour tous les atomes dans une boîte
# cubique [-L,L]³ (hors origine) :
#   V_total = (e / (4πε₀a)) * M
# où M est la constante de Madelung (approchée pour L fini).
#
# Écrivez un programme calculant M pour la plus grande valeur de L possible,
# avec un temps d'exécution < 1 minute.
################################################################################

import numpy as np

def constante_madelung(L):
    M = 0.0
    for i in range(-L, L + 1):
        for j in range(-L, L + 1):
            for k in range(-L, L + 1):
                if i == 0 and j == 0 and k == 0:
                    continue  # On exclut l'origine
                distance = np.sqrt(i**2 + j**2 + k**2)
                # Déterminer le signe en fonction de i+j+k
                if (i + j + k) % 2 == 0:
                    M += 1 / distance
                else:
                    M -= 1 / distance
    return M

L = input(int("Choisir L le plus grand possible pour une exécution rapide (< 1 min)"))
L = 50  # Tu peux ajuster cette valeur selon la puissance de ton ordinateur
M = constante_madelung(L)
print(f"Constante de Madelung pour L={L} : {M:.6f}")
