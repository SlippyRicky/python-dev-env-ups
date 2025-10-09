liste = [17, 38, 10, 25, 72]
print(f"Liste initiale : {liste}")

liste_croissante = sorted(liste)
print(f"Liste en ordre croissant: {liste_croissante}")

liste_etandue = liste
liste_etandue.append(12)
print(f"Liste après l'ajout de 12: {liste}")

liste_inversee= liste[::-1]
print(f"Liste en ordre inversée: {liste_inversee}")

indice_17 = liste.index(17)
print(f"L'indice de 17 est maintenant {indice_17}")

liste.remove(38)
print(f"La liste sans l'element 38: {liste}")

s_liste_1 = liste[1:3]
print(f"La sous-liste du 2ème au 3ème élément: {s_liste_1}")

s_liste_2 = liste[2:]
print(f"La sous-liste du 3ème élément à la fin: {s_liste_2}")

element_final = liste[-1]
print(f"Dernier élément (avec indiçage négatif): {element_final}")

element_max = max(liste)
element_min = min(liste)
print(f"Le plus grand des éléments: {element_max},")
print(f"le plus petit des éléments: {element_min}")
