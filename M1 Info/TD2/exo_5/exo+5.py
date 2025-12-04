def crypter(texte):
    paire = texte[1::2]
    impaire = texte[::2]
    return paire + impaire

def decrypter(texte_crypte):
    moitie = len(texte_crypte) // 2
    paire = texte_crypte[:moitie]
    impaire = texte_crypte[moitie:]
    decrypte = ""
    for i in range(len(impaire)):
        decrypte += impaire[i]
        if i < len(paire):
            decrypte += paire[i]
    if len(texte_crypte) % 2 != 0:
        decrypte += paire[-1]
    return decrypte

def est_utf8_valide(texte):
    try:
        texte.encode('utf-8').decode('utf-8')
        return True
    except UnicodeError:
        return False

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Crypter un message")
        print("2. Décrypter un message")
        print("3. Quitter")
        choix = input("Choisissez une option (1/2/3): ")

        if choix == '1':
            message = input("Entrez le message à crypter: ")
            if not est_utf8_valide(message):
                print("Erreur: Le message contient des caractères invalides (UTF-8).")
                continue
            message_crypte = crypter(message)
            print(f"Message crypté: {message_crypte}")

        elif choix == '2':
            message_crypte = input("Entrez le message à décrypter: ")
            if not est_utf8_valide(message_crypte):
                print("Erreur: Le message contient des caractères invalides (UTF-8).")
                continue
            message_decrypte = decrypter(message_crypte)
            print(f"Message décrypté: {message_decrypte}")

        elif choix == '3':
            print("Au revoir!")
            break

        else:
            print("Option invalide. Veuillez choisir 1, 2 ou 3.")

if __name__ == "__main__":
    main()
