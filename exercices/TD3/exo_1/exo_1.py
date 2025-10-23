import matplotlib.pyplot as plt
import numpy as np
x = np.array([5.4874e+14, 6.931e+14, 7.4307e+14, 8.2193e+14, 9.6074e+14, 1.184e+15])
y = np.array([0.5309, 1.0842, 1.2734, 1.6598, 2.19856, 3.10891])
N = len(x)
E_x = np.sum(x) / N
E_y = np.sum(y) / N
E_xx = np.sum(x * x) / N
E_xy = np.sum(x * y) / N
m = (E_xy - E_x * E_y) / (E_xx - E_x**2)
c = (E_xx * E_y - E_x * E_xy) / (E_xx - E_x**2)
x_line = np.array([min(x), max(x)])
y_line = m * x_line + c
plt.figure()
plt.scatter(x, y)
plt.plot(x_line, y_line)
plt.tight_layout()
plt.show()
