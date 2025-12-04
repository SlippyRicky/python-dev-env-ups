import math as m

input = input(int("Entrez une valeur d'angle en degres (ex: pi/4)")).strip().lower()

ang_d = lire_angle("Entres une valeur d'angle en degres (90, 120, 34251324) : ")

ang_r1  = ang_d * pi / 180
ang_r2 = randians(ang_r1)

print("L'angle ", ang_d, " vaut ", ang_r2, "radians.")
