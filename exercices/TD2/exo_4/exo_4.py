import string

mdp = str(input("Quel est votre mot de passe?:"))

minuscules = string.ascii_lowercase
majuscules = string.ascii_uppercase
numeros = [str(i) for i in range(10)]

if len(password)>6 and len(password) < 16:
    isNumber=False
    for n in numeros:
        if n in n mdp:
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
