from decimal import Decimal, getcontext

# Set the precision to a high number to handle long floating-point numbers
getcontext().prec = 28

print("Nous allons ajouter deux nombres a et b.")
a = Decimal(input("Entrez la valeur de a: "))
b = Decimal(input("Entrez la valeur de b: "))
sum_ab = a + b
print(f"La somme de {a} et {b} est {sum_ab:28f}")
