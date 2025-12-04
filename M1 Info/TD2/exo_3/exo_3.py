def conv_homme_chien(annees_humaines):
    if annees_humaines <= 18:
        return annees_humaines / 9
    else:
        return 2 + (annees_humaines - 18) / 6

def conv_chien_homme(annees_canines):
    if annees_canines <= 2:
        return annees_canines * 9
    else:
        return 18 + (annees_canines - 2) * 6

# Demande à l'utilisateur ce qu'il veut convertir
reponse = int(input("Voulez-vous : 1) Convertir d'années humaines en années canines, ou 2) d'années canines en années humaines ? (1 ou 2) : "))

if reponse == 1:
    annees_humaines = int(input("Entrez l'âge en années humaines : "))
    annees_canines = conv_homme_chien(annees_humaines)
    print(f"{annees_humaines} année(s) humaine(s) équivalent à {annees_canines:.1f} année(s) canine(s).")
elif reponse == 2:
    annees_canines = int(input("Entrez l'âge du chien en années : "))
    annees_humaines = conv_chien_homme(annees_canines)
    print(f"{annees_canines} année(s) canine(s) équivalent à {annees_humaines} année(s) humaine(s).")
else:
    print("Réponse invalide. Veuillez entrer 1 ou 2.")
