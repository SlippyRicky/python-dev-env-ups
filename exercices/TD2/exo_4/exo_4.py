import string

mdp = str(input("Quel est votre mot de passe?:"))

minuscules = string.ascii_lowercase
minuscules_pas_chiant = (a,z)
majuscules = string.ascii_uppercase
numeros = [str(i) for i in range(10)]
caracteres_speciaux = ['$', '#', '@']

if 6 <= len(mpd) <= 16:
    isNumber=False
    for n in numeros:
        if n in mdp:
            isNumber = True
            break

    isCaps = False
    for char in majuscules:
        if char in mdp:
            isCaps = True
            break

    isLow = False
    for char in minuscules:
        if char in mdp:
            isLow=True
            break
