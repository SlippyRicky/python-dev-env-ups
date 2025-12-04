# Demander les valeurs à l'utilisateur
montant_initial = float(input("Entrez le montant initial (en euros) : "))
taux_interet = float(input("Entrez le taux d'intérêt annuel (ex: 0.04 pour 4%) : "))
montant_final = float(input("Entrez le montant final souhaité (en euros) : "))

# Initialiser le nombre d'années
annees = 0
montant_actuel = montant_initial

# Tant que le montant actuel n'a pas atteint le montant final
while montant_actuel < montant_final:
    montant_actuel *= (1 + taux_interet)
    annees += 1

# Afficher le résultat
print(f"Il faudra attendre {annees} année(s) pour atteindre {montant_final:.2f} €.")
