import math as m

def cube(x):
    return x ** 3

def sphere_volume(r):
    return (4 * m.pi * cube(r)) / 3

def pyramide_et_cone_volume(b, h, is_cone=False):
    if is_cone:
        rayon = b / 2
        return (m.pi * rayon**2 * h) / 3
    else:
        return (b * h) / 3

def volume(L, forme, l=None):
    if forme == "cube":
        return L ** 3
    elif forme == "sphere":
        return sphere_volume(L / 2)  # L est le diamètre, donc le rayon est L/2
    elif forme == "cone":
        if l is None:
            raise ValueError("Le cône nécessite un diamètre et une hauteur.")
        return pyramide_et_cone_volume(L, l, is_cone=True)
    elif forme == "pyramide":
        if l is None:
            raise ValueError("La pyramide nécessite une largeur de base et une hauteur.")
        return pyramide_et_cone_volume(L, l)
    else:
        raise ValueError("Forme non reconnue. Utilisez 'cube', 'sphere', 'cone' ou 'pyramide'.")

R = input("Voulez-vous calculer le volume d'un cube, d'une sphere, d'un cone, ou d'une pyramide ? ").lower()
largeur = float(input("Quel est le diamètre ou la largeur de l'objet souhaité ? "))

if R == 'cone':
    hauteur = float(input("Quelle est la hauteur souhaitée du cône ? "))
    print(volume(largeur, R, hauteur))
elif R == 'pyramide':
    hauteur = float(input("Quelle est la hauteur souhaitée de la pyramide ? "))
    print(volume(largeur, R, hauteur))
elif R in ['cube', 'sphere']:
    print(volume(largeur, R))
else:
    print("Forme non reconnue.")
