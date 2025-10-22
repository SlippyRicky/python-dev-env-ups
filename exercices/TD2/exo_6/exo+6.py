import tkinter as tk
from tkinter import ttk, simpledialog, font
import random
from PIL import Image, ImageTk
import os

class FibonacciLapinsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulation de Fibonacci - Lapins")
        self.root.configure(bg="black")
        self.root.geometry("800x600")
        self.root.minsize(600, 500)

        # Style moderne
        self.style = ttk.Style()
        self.style.configure("TButton", font=('Helvetica', 12), padding=10)
        self.style.configure("Accent.TButton", background="green", foreground="white", bordercolor="black")
        self.style.map("Accent.TButton", background=[("active", "#45a049")])

        # Frame principale
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Canevas avec bordure arrondie
        self.canvas = tk.Canvas(main_frame, bg="#aadd88", highlightthickness=0, borderwidth=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Charger l'image du lapin
        script_dir = os.path.dirname(os.path.abspath(__file__))
        lapin_path = os.path.join(script_dir, "lapin.png")
        self.lapin_image = Image.open(lapin_path)
        self.lapin_image = self.lapin_image.resize((50, 50), Image.LANCZOS)
        self.lapin_photo = ImageTk.PhotoImage(self.lapin_image)

        # Variables
        self.n = simpledialog.askinteger("Nombre de mois", "Combien de mois simuler ?", minvalue=1, maxvalue=24)
        if not self.n:
            self.n = 12
        self.fib_sequence = self.generate_fibonacci(self.n)
        self.lapins = []
        self.current_month = 0
        self.total_lapins = 0

        # Compteur en haut (centré)
        self.counter_var = tk.StringVar(value="Mois 0 : 0 lapins")
        self.counter_label = ttk.Label(
            self.canvas, textvariable=self.counter_var,
            font=('Helvetica', 16, 'bold'), foreground="#E53935",
            background="#aadd88"
        )
        self.counter_window = self.canvas.create_window(0, 0, window=self.counter_label, anchor=tk.N)

        # Lier les événements
        self.canvas.bind("<Configure>", self.on_resize)
        self.root.bind("<Return>", lambda e: self.reset())

        # Démarrer l'animation
        self.animate()

    def generate_fibonacci(self, n):
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib

    def on_resize(self, event=None):
        self.redraw()

    def redraw(self):
        # Mise à jour des positions
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Recentrer le compteur
        self.canvas.coords(self.counter_window, width//2, 20)

        # Redessiner les lapins (avec marge de sécurité)
        for rel_x, rel_y, img_id in self.lapins:
            x = int(rel_x * (width - 60) + 30)  # Marge de 30px
            y = int(rel_y * (height - 60) + 30)
            self.canvas.coords(img_id, x, y)

    def animate(self):
        if self.current_month < len(self.fib_sequence):
            # Calcul des nouveaux lapins
            new_lapins = self.fib_sequence[self.current_month] - (self.fib_sequence[self.current_month-1] if self.current_month > 0 else 0)

            # Ajouter les nouveaux lapins
            width = self.canvas.winfo_width() - 60
            height = self.canvas.winfo_height() - 60

            for _ in range(new_lapins):
                rel_x = random.uniform(0.1, 0.9)  # Éviter les bords
                rel_y = random.uniform(0.1, 0.9)
                x = int(rel_x * width + 30)
                y = int(rel_y * height + 30)
                img_id = self.canvas.create_image(x, y, image=self.lapin_photo, anchor=tk.NW)
                self.lapins.append((rel_x, rel_y, img_id))

            # Mettre à jour le compteur
            self.total_lapins = self.fib_sequence[self.current_month]
            self.counter_var.set(f"Mois {self.current_month} : {self.total_lapins} lapins")

            self.current_month += 1
            self.root.after(200, self.animate)
        else:
            self.show_completion()

    def show_completion(self):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Message de fin
        self.canvas.create_text(
            width//2, height//2,
            text="Simulation terminée !",
            font=('Helvetica', 18, 'bold'), fill="#E53935"
        )

        # Bouton Recommencer stylisé
        btn_frame = ttk.Frame(self.canvas, style="Accent.TButton")
        ttk.Button(
            btn_frame, text="Recommencer", command=self.reset,
            style="Accent.TButton"
        ).pack(padx=20, pady=10)
        self.btn_window = self.canvas.create_window(width//2, height*0.8, window=btn_frame, anchor=tk.CENTER)

    def reset(self):
        # Effacer tout
        for _, _, img_id in self.lapins:
            self.canvas.delete(img_id)
        self.lapins = []
        self.current_month = 0
        self.total_lapins = 0
        self.counter_var.set("Mois 0 : 0 lapins")

        # Supprimer le message de fin et le bouton
        self.canvas.delete("all")
        self.canvas.create_window(0, 0, window=self.counter_label, anchor=tk.N)

        # Relancer
        self.animate()

if __name__ == "__main__":
    root = tk.Tk()
    app = FibonacciLapinsApp(root)
    root.mainloop()
