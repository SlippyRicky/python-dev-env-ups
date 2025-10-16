import tkinter as tk
from tkinter import ttk

def conv_homme_chien(event=None):
    try:
        annees_humaines = float(entree_humain.get())
        if annees_humaines <= 18:
            result = annees_humaines / 9
        else:
            result = 2 + (annees_humaines - 18) / 6
        entree_chien.delete(0, tk.END)
        entree_chien.insert(0, f"{result:.1f}")
    except ValueError:
        entree_chien.delete(0, tk.END)
        entree_chien.insert(0, "Erreur")

def conv_chien_homme(event=None):
    try:
        annees_canines = float(entree_chien.get())
        if annees_canines <= 2:
            result = annees_canines * 9
        else:
            result = 18 + (annees_canines - 2) * 6
        entree_humain.delete(0, tk.END)
        entree_humain.insert(0, f"{result:.1f}")
    except ValueError:
        entree_humain.delete(0, tk.END)
        entree_humain.insert(0, "Erreur")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Convertisseur d'âge canin/humain")

# Style dark mode
style = ttk.Style()
style.theme_use('clam')
style.configure('TFrame', background='#2d2d2d')
style.configure('TLabel', background='#2d2d2d', foreground='#ffffff', font=('Helvetica', 10))
style.configure('TEntry', fieldbackground='#3d3d3d', foreground='#ffffff', insertbackground='white')
style.configure('TButton', background='#3d3d3d', foreground='#ffffff', borderwidth=1)
style.map('TButton', background=[('active', '#4a4a4a')])

# Frame principal
frame = ttk.Frame(fenetre, padding="20", style='TFrame')
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Section "Humain → Chien"
ttk.Label(frame, text="Années humaines :").grid(row=0, column=0, sticky=tk.W, pady=5)
entree_humain = ttk.Entry(frame, width=10)
entree_humain.grid(row=0, column=1, sticky=tk.W, pady=5)
entree_humain.bind('<Return>', conv_homme_chien)  # Conversion avec la touche Entrée
ttk.Button(frame, text="→", command=conv_homme_chien).grid(row=0, column=2, padx=5, pady=5)

# Section "Chien → Humain"
ttk.Label(frame, text="Années canines :").grid(row=1, column=0, sticky=tk.W, pady=5)
entree_chien = ttk.Entry(frame, width=10)
entree_chien.grid(row=1, column=1, sticky=tk.W, pady=5)
entree_chien.bind('<Return>', conv_chien_homme)  # Conversion avec la touche Entrée
ttk.Button(frame, text="←", command=conv_chien_homme).grid(row=1, column=2, padx=5, pady=5)

# Bouton pour quitter
ttk.Button(frame, text="Quitter", command=fenetre.quit).grid(row=2, column=0, columnspan=3, pady=10)

# Configuration des colonnes pour qu'elles s'étirent
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

# Lancement de la boucle principale
fenetre.mainloop()
