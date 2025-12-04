import numpy as np
import matplotlib.pyplot as plt
import os

T2 = 0.1
M0 = 1.0
GAMMA = 42.58

B0_eff = 0.0005

f_larmor = 5.0 # [s-1]

dt = 0.0001 # [s]
t = np.arange(0, 0.2, dt)

Xx , Yy = 128, 128

frame = np.meshgrid(x,y)

enveloppe = M0 * np.exp(-t / T2)
oscillation = np.sin(2 * np.pi * f_larmor * t)
S = enveloppe * oscillation

dSdt = np.zeros_like(S)

dSdt[1:-1] = (S[2:] - S[:-2]) / (2 * dt)

dSdt[0]  = (S[1] - S[0]) / dt       # Différence avant
dSdt[-1] = (S[-1] - S[-2]) / dt     # Différence arrière

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(t, S, label='Signal S(t)', color='navy')
plt.plot(t, enveloppe, '--', color='orange', label='Enveloppe T2', linewidth=1.5)
plt.plot(t, -enveloppe, '--', color='orange', linewidth=1.5) # Enveloppe négative
plt.title(f"Signal Spin-Echo Simulé (T2={T2}s, f={f_larmor}Hz)")
plt.ylabel("Amplitude")
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
