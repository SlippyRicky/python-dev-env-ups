from datetime import datetime
birth_year = int(input("Entrez votre année de naissance: "))
current_year = datetime.now().year
age = current_year - birth_year
if age > 123:
    print(f"Vous auriez {age} ans si vous n'étiez pas mort ou fabulateur.")
else:
    print(f"Votre âge est {age} ans.")
