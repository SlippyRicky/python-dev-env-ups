import math
x1 = float(input("Entrez la coordonnée x du 1e point || X1="))
y1 = float(input("Entrez la coordonnée y du 1e point || Y1="))
x2 = float(input("Entrez la coordonnée x du 2e point || X2="))
y2 = float(input("Entrez la coordonnée y du 2e point || Y2="))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"La distance entre les deux points est {distance}")
