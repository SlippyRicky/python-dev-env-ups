from math import factorial, exp

lst = list(range(10))

factorial_list = [factorial(x) for x in lst]

square_list = [x**2 for x in lst]

exp_list = [round(exp(x), 2) for x in lst]

print(f"Liste des factoriels: {factorial_list}")
print(f"Liste des carrés: {square_list}")
print(f"Liste des exponentielles: {exp_list}")


# import math : Accès aux fonctions via math.fonction().
# from math import * : Accès direct aux fonctions sans préfixe.
# import math est plus clair et évite les conflits de noms.
# from math import * peut causer des conflits et rendre le code moins lisible.
