from datetime import datetime
birth_year = int(input("Entrez votre année de naissance: "))
current_year = datetime.now().year
age = current_year - birth_year
print(f"Votre âge est {age} ans.")
