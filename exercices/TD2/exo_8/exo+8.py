import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
from threading import Thread

class MadelungApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calcul de la constante de Madelung")
        self.root.geometry("1000x700")

        # Variables
        self.L = tk.IntVar(value=50)
        self.M = tk.DoubleVar(value=0.0)
        self.calculating = False
        self.stop_calculation = False

        # Interface
        self.setup_ui()

    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Frame de contrôle
        control_frame = ttk.LabelFrame(main_frame, text="Paramètres", padding=10)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        # Contrôles
        ttk.Label(control_frame, text="Valeur de L:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(control_frame, textvariable=self.L, width=10).grid(row=0, column=1, pady=5)

        self.btn_calculate = ttk.Button(control_frame, text="Calculer", command=self.start_calculation)
        self.btn_calculate.grid(row=1, column=0, columnspan=2, pady=10)

        self.btn_stop = ttk.Button(control_frame, text="Arrêter", command=self.stop_calculation, state=tk.DISABLED)
        self.btn_stop.grid(row=2, column=0, columnspan=2, pady=5)

        ttk.Label(control_frame, text="Résultat:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.lbl_result = ttk.Label(control_frame, text="M = -")
        self.lbl_result.grid(row=3, column=1, sticky=tk.W, pady=5)

        ttk.Label(control_frame, text="Temps écoulé:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.lbl_time = ttk.Label(control_frame, text="0.0 s")
        self.lbl_time.grid(row=4, column=1, sticky=tk.W, pady=5)

        # Frame pour le graphique
        graph_frame = ttk.LabelFrame(main_frame, text="Visualisation", padding=10)
        graph_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Figure matplotlib
        self.fig = plt.Figure(figsize=(6, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("Convergence de la constante de Madelung")
        self.ax.set_xlabel("Valeur de L")
        self.ax.set_ylabel("Constante de Madelung")
        self.ax.grid(True)

        # Canvas pour afficher le graphique
        self.canvas = FigureCanvasTkAgg(self.fig, master=graph_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Info
        info_text = """Constante de Madelung pour NaCl:
Les atomes Na+ (rouge) sont aux positions où i+j+k est pair
Les atomes Cl- (bleu) sont aux positions où i+j+k est impair
Le potentiel est calculé pour un cube de côté 2L+1"""
        ttk.Label(main_frame, text=info_text, justify=tk.LEFT, wraplength=400).pack(fill=tk.X, padx=10, pady=10)

    def start_calculation(self):
        if self.calculating:
            return

        try:
            L = self.L.get()
            if L <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un entier positif")
            return

        self.calculating = True
        self.stop_calculation = False
        self.btn_calculate.config(state=tk.DISABLED)
        self.btn_stop.config(state=tk.NORMAL)

        # Lancer le calcul dans un thread séparé
        Thread(target=self.calculate_madelung, args=(L,), daemon=True).start()

    def stop_calculation(self):
        self.stop_calculation = True

    def calculate_madelung(self, L):
        start_time = time.time()
        M = 0.0
        total_iterations = (2*L + 1)**3 - 1  # -1 pour exclure l'origine
        current_iteration = 0

        # Pour la visualisation
        x_values = []
        y_values = []

        for i in range(-L, L + 1):
            if self.stop_calculation:
                break

            for j in range(-L, L + 1):
                if self.stop_calculation:
                    break

                for k in range(-L, L + 1):
                    if self.stop_calculation:
                        break

                    if i == 0 and j == 0 and k == 0:
                        continue

                    distance = np.sqrt(i**2 + j**2 + k**2)
                    if (i + j + k) % 2 == 0:
                        M += 1 / distance
                    else:
                        M -= 1 / distance

                    current_iteration += 1

                    # Mise à jour périodique de l'interface
                    if current_iteration % 10000 == 0:
                        elapsed = time.time() - start_time
                        self.root.after(0, self.update_progress, M, elapsed)

                    # Enregistrer les valeurs pour le graphique
                    if (i == L and j == L and k == L) or (i == L and j == L and k == 0):
                        x_values.append(max(abs(i), abs(j), abs(k)))
                        y_values.append(M)
                        self.root.after(0, self.update_plot, x_values, y_values)

        elapsed = time.time() - start_time
        self.root.after(0, self.finish_calculation, M, elapsed)

    def update_progress(self, M, elapsed):
        self.M.set(M)
        self.lbl_result.config(text=f"M = {M:.6f}")
        self.lbl_time.config(text=f"{elapsed:.1f} s")

    def update_plot(self, x_values, y_values):
        self.ax.clear()
        self.ax.plot(x_values, y_values, 'b-o', markersize=4)
        self.ax.set_title("Convergence de la constante de Madelung")
        self.ax.set_xlabel("Valeur de L")
        self.ax.set_ylabel("Constante de Madelung")
        self.ax.grid(True)
        self.canvas.draw()

    def finish_calculation(self, M, elapsed):
        self.calculating = False
        self.btn_calculate.config(state=tk.NORMAL)
        self.btn_stop.config(state=tk.DISABLED)
        self.lbl_result.config(text=f"M = {M:.6f}")
        self.lbl_time.config(text=f"{elapsed:.1f} s")

        # Ajouter la valeur finale au graphique
        x_values = list(range(1, self.L.get() + 1))
        y_values = [self.constante_madelung(i) for i in x_values]
        self.ax.plot(x_values, y_values, 'b-o', markersize=4)
        self.ax.axhline(y=M, color='r', linestyle='--', label=f"Valeur finale: {M:.6f}")
        self.ax.legend()
        self.canvas.draw()

    def constante_madelung(self, L):
        """Version optimisée pour le calcul rapide"""
        M = 0.0
        for i in range(-L, L + 1):
            for j in range(-L, L + 1):
                for k in range(-L, L + 1):
                    if i == 0 and j == 0 and k == 0:
                        continue
                    distance = np.sqrt(i**2 + j**2 + k**2)
                    if (i + j + k) % 2 == 0:
                        M += 1 / distance
                    else:
                        M -= 1 / distance
        return M

if __name__ == "__main__":
    root = tk.Tk()
    app = MadelungApp(root)
    root.mainloop()
