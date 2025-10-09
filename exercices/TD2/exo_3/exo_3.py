reponse = int(input("Voulez vous 1) Convertir d'annÃ©es humaines ou 2) cannines? 1 ou 2:"))


annees_humaines = int(input("Entrez l'Ã¢ge en annÃ©es humaines : "))
annees_canines = int(input("Entrez l'Ã¢ge du chien en annÃ©es : "))

if reponse == 1:
    conv_homme_chien(annees_humaines, annees_canines)
    print(f"{annees_humaines} annÃ©e(s) humaine(s) Ã©quivalent Ã  {annees_canines:.1f} annÃ©e(s) canine(s).")
    else:
        conv_chien_homme(annees_canines, annees_humaines)
        print(f"{annees_canines} annÃ©e(s) canine(s) Ã©quivalent Ã  {annees_humaines} annÃ©e(s) humaine(s).")

def conv_homme_chien(annees_humaines, annees_canines):
    if annees_humaines <= 18:
        annees_canines = annees_humaines / 9
    else:
        annees_canines = 2 + (annees_humaines - 18) / 6
        
def conv_chien_homme(annees_canines, annees_humaines):
    if annees_canines <= 2:
        annees_humaines = annees_canines * 9
    else:
        annees_humaines = 2 * 9 + (annees_canines - 2) * 6
