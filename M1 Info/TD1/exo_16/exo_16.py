lst = list(range(6))

lst_plus_3_si_x_sup2 = [x + 3 if x >= 2 else x for x in lst]
print(f"Liste après avoir ajouté 3 à chaque élément >= 2: {lst_plus_3_si_x_sup2}")
