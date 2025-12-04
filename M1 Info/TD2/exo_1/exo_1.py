year = int(input("Proposez une annee pour savoir si elle est bisextile: "))

if (year % 400 == 0):
    print(f"{year} est bisextile.")
elif (year % 100 == 0):
    print(f"{year} n'est pas bisextile.")
elif (year % 4 == 0):
    print(f"{year} est bisextile.")
else:
    print(f"{year} n'est pas bisextile.")
