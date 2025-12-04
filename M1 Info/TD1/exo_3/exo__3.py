import math

while True:
    try:
        ang_d = input("Entrez une valeur d'angle en degrés (ou 'q' pour quitter) : ")
        if ang_d.lower() == 'q' || ang_d.lower() == 'quit':
            print("Au revoir !")
            break  # Sort de la boucle et termine le programme

        ang_d = float(ang_d)
        ang_r = math.radians(ang_d)
        ang_r_mod_2pi = ang_r % (2 * math.pi)
        ang_r_mod_pi = ang_r % math.pi

        print(f"L'angle {ang_d} degrés vaut {ang_r} radians.")
        print(f"Modulo 2π : {ang_r_mod_2pi} radians.")
        print(f"Modulo π : {ang_r_mod_pi} radians.")
    except ValueError:
        print("Veuillez entrer un nombre valide ou 'q' pour quitter.")
