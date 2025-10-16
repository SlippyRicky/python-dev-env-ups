import time
import matplotlib.pyplot as plt
import numpy as np
from functools import lru_cache

# --- 1. Approche récursive naïve (lente pour n > 35) ---
def fib_recursif(n):
    if n <= 1:
        return n
    return fib_recursif(n-1) + fib_recursif(n-2)

# --- 2. Approche récursive optimisée avec mémoisation ---
@lru_cache(maxsize=None)
def fib_recursif_memo(n):
    if n <= 1:
        return n
    return fib_recursif_memo(n-1) + fib_recursif_memo(n-2)

# --- 3. Approche itérative (optimale pour la plupart des cas) ---
def fib_iteratif(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# --- 4. Approche dynamique (avec liste) ---
def fib_dynamique(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

# --- 5. Approche matricielle (O(log n)) ---
def fib_matriciel(n):
    def multiply(a, b):
        return [
            [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]],
        ]

    def matrix_pow(mat, power):
        result = [[1, 0], [0, 1]]  # Matrice identité
        while power > 0:
            if power % 2 == 1:
                result = multiply(result, mat)
            mat = multiply(mat, mat)
            power //= 2
        return result

    if n == 0:
        return 0
    mat = [[1, 1], [1, 0]]
    result = matrix_pow(mat, n-1)
    return result[0][0]

# --- 6. Génération de la liste des nombres de Fibonacci ---
def liste_fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# --- 7. Vérification de F25 = 75025 ---
def verifier_f25():
    return fib_iteratif(25) == 75025

# --- 8. Mesure des performances ---
def mesurer_performance(n):
    methods = {
        "Récursif": fib_recursif,
        "Récursif + Mémo": fib_recursif_memo,
        "Itératif": fib_iteratif,
        "Dynamique": fib_dynamique,
        "Matriciel": fib_matriciel,
    }
    results = {}
    for name, func in methods.items():
        start = time.time()
        func(n)
        end = time.time()
        results[name] = end - start
    return results

# --- 9. Visualisation graphique ---
def visualiser_fibonacci(n):
    fib = liste_fibonacci(n)
    plt.figure(figsize=(10, 6))
    plt.plot(range(n+1), fib, marker='o', linestyle='-', color='b')
    plt.title(f"Suite de Fibonacci (F0 à F{n})")
    plt.xlabel("n")
    plt.ylabel("Fn")
    plt.grid(True)
    plt.show()

# --- Exécution ---
if __name__ == "__main__":
    n = int(input("Entrez un entier n pour calculer Fn : "))
    print(f"F{n} (itératif) = {fib_iteratif(n)}")
    print(f"Liste des nombres de Fibonacci de F0 à F{n} : {liste_fibonacci(n)}")
    print(f"Vérification F25 = 75025 : {'OK' if verifier_f25() else 'KO'}")
    print("\nPerformance pour n=30 :")
    for method, temps in mesurer_performance(30).items():
        print(f"{method}: {temps:.6f} secondes")
    visualiser_fibonacci(n)
