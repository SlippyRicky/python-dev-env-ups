annees_humaines = int(input("Entrez l'âge en années humaines : "))

if annees_humaines <= 18:
    annees_canines = annees_humaines / 9
else:
    annees_canines = 2 + (annees_humaines - 18) / 6

print(f"{annees_humaines} année(s) humaine(s) équivalent à {annees_canines:.1f} année(s) canine(s).")

annees_canines = int(input("Entrez l'âge du chien en années : "))

if annees_canines <= 2:
    annees_humaines = annees_canines * 9
else:
    annees_humaines = 2 * 9 + (annees_canines - 2) * 6

print(f"{annees_canines} année(s) canine(s) équivalent à {annees_humaines} année(s) humaine(s).")
