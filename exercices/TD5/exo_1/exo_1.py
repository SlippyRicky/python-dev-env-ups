import matplotlib.pyplot as plt
import numpy as np
from math import tanh

h = np.float64(1e-7)
x = np.linspace(-2, 2, 1000)

def f(x):
    return 1/2 * (tanh(x * 2))

def df_A(f, x, h):
    return (f(x + h) - f(x)) / h

def df_C(f, x, h):
    return (f(x + h/2) - f(x - h/2)) / h

f_x = np.array([f(xi) for xi in x])
Dfx_A = np.array([df_A(f, xi, h) for xi in x])
Dfx_C = np.array([df_C(f, xi, h) for xi in x])

plt.figure(figsize=(10, 6))
plt.plot(x, f_x, 'r-', label='f(x)')
plt.plot(x, Dfx_A, 'g--', linewidth=3, label='Forward Difference Approximation')
plt.plot(x, Dfx_C, 'b.', markersize=0.5, label='Central Difference Approximation')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparaison des Méthodes de Dérivation')
plt.legend()
plt.show()
