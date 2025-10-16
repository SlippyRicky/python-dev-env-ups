def crypter(texte):
    paire = texte[1::2]
    impaire = texte[::2]
    crypte = paire + impaire
    return crypte

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

encrypt_mode = input("Voulez-vous crypter un nouveau message? (y/n): ")

if encrypt_mode == 'y':
    nouveau_message = input("Donnez un message en texte UTF-8 à crypter: ")
    nouveau_message_crypte = crypter(nouveau_message)
    print(f"Message crypté: {nouveau_message_crypte}")

    q_decrypter = input("Voulez-vous décrypter ce message? (y/n): ")
    if q_decrypter == 'y':
        nouveau_message_decrypte = decrypter(nouveau_message_crypte)
        print(f"Message décrypté: {nouveau_message_decrypte}")
    else:
        print("D'accord, à bientôt!")
else:
    texte_original = "mon message secret"
    print(f"Texte original: {texte_original}")
    texte_crypte = crypter(texte_original)
    print(f"Texte crypté: {texte_crypte}")
    texte_decrypte = decrypter(texte_crypte)
    print(f"Texte décrypté: {texte_decrypte}")
