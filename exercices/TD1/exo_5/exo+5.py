nom = input("Entrez votre nom: ")

if nom.isalpha():
    print(f"Bonjour, {nom}")
else:
    print(f"Bonjour, {nom}! But you're a clanker for using non-letter characters in your name!")
