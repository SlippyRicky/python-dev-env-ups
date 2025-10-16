n_limit = int(input("Sur combien de mois voulez-vous itérer ? "))

F_n = [0, 1]
for n in range(2, n_limit + 1):
    F_n.append(F_n[n-1] + F_n[n-2])

print(f"Liste des nombres de Fibonacci de F0 à F{n_limit} : {F_n}")
