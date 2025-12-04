import tkinter as tk
from tkinter import ttk, simpledialog, font
import random
from PIL import Image, ImageTk
import os

class FibonacciLapinsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fibonacci Rabbit Simulation")
        self.root.configure(bg="black")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)

        # Style personnalisé avancé
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.configure_styles()

        # Frame principale
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Canevas avec fond vert
        self.canvas = tk.Canvas(self.main_frame, bg="#aadd88", highlightthickness=0, borderwidth=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Charger les images
        self.load_images()

        # Variables
        self.setup_variables()

        # Interface
        self.setup_interface()

        # Lancer l'animation
        self.animate()

    def configure_styles(self):
        """Configuration des styles personnalisés"""
        # Style pour le bouton principal (texte rouge)
        self.style.configure('Accent.TButton',
                           foreground='#E53935',  # Texte rouge
                           background='#4CAF50',
                           font=('Helvetica', 16, 'bold'),
                           borderwidth=2,
                           focusthickness=3,
                           focuscolor='#4CAF50',
                           padding=12,
                           relief='raised')
        self.style.map('Accent.TButton',
                      foreground=[('active', '#E53935')],  # Rouge au survol
                      background=[('active', '#3e8e41'), ('pressed', '#388E3C')],
                      relief=[('pressed', 'sunken'), ('!pressed', 'raised')])

        # Style pour le label du compteur
        self.style.configure('Counter.TLabel',
                           foreground='#E53935',
                           background='#aadd88',
                           font=('Helvetica', 18, 'bold'),
                           padding=10)

        # Style pour le message de fin
        self.style.configure('End.TLabel',
                           foreground='#E53935',
                           background='#aadd88',
                           font=('Helvetica', 20, 'bold'),
                           padding=15)

    def load_images(self):
        """Chargement et traitement des images"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        lapin_path = os.path.join(script_dir, "lapin.png")
        try:
            self.lapin_image = Image.open(lapin_path)
            self.lapin_image = self.lapin_image.resize((50, 50), Image.LANCZOS)
            self.lapin_photo = ImageTk.PhotoImage(self.lapin_image)
            # Image d'ombre pour effet 3D
            shadow = Image.new('RGBA', (50, 50), (0, 0, 0, 128))
            self.shadow_photo = ImageTk.PhotoImage(shadow)
        except FileNotFoundError:
            # Image de secours si lapin.png est manquant
            self.lapin_photo = ImageTk.PhotoImage(Image.new('RGB', (50, 50), '#666'))
            shadow = Image.new('RGBA', (50, 50), (0, 0, 0, 128))
            self.shadow_photo = ImageTk.PhotoImage(shadow)

    def setup_variables(self):
        """Initialisation des variables"""
        self.n = simpledialog.askinteger("Nombre de mois",
                                      "Combien de mois simuler ?",
                                      minvalue=1, maxvalue=24, initialvalue=12)
        if not self.n:
            self.n = 12
        self.fib_sequence = self.generate_fibonacci(self.n)
        self.lapins = []
        self.current_month = 0
        self.total_lapins = 0
        self.animation_id = None
        self.btn = None
        self.end_message = None
        self.counter_window = None

    def setup_interface(self):
        """Configuration de l'interface utilisateur"""
        # Compteur en haut (centré)
        self.counter_var = tk.StringVar(value="Mois 0 : 0 lapins")
        self.counter_label = ttk.Label(
            self.canvas, textvariable=self.counter_var,
            style='Counter.TLabel'
        )
        padding_top = 20
        self.counter_window = self.canvas.create_window(
            0, 0,  # Position initiale, sera recalculée
            window=self.counter_label,
            anchor=tk.N
        )

        # Lier les événements
        self.canvas.bind("<Configure>", self.on_resize)
        self.root.bind("<Return>", lambda e: self.reset())
        self.root.bind("<space>", lambda e: self.toggle_pause())

        # Menu contextuel
        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="Recommencer", command=self.reset)
        self.menu.add_command(label="Quitter", command=self.root.quit)
        self.root.bind("<Button-3>", self.show_context_menu)

    def generate_fibonacci(self, n):
        """Génération de la suite de Fibonacci"""
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib

    def on_resize(self, event=None):
        """Gestion du redimensionnement"""
        self.redraw()

    def redraw(self):
        """Redessin des éléments après redimensionnement"""
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Recentrer le compteur
        if self.counter_window:
            self.canvas.coords(self.counter_window, width//2, 20)

        # Redessiner les lapins avec ombres
        for rel_x, rel_y, img_id, shadow_id in self.lapins:
            x = int(rel_x * (width * 0.8) + width * 0.1)
            y = int(rel_y * (height * 0.8) + height * 0.1)
            self.canvas.coords(img_id, x, y)
            self.canvas.coords(shadow_id, x+2, y+2)

        # Repositionner le bouton et le message de fin
        if self.btn:
            self.canvas.coords(self.btn_window, width//2, height*0.85)
        if self.end_message:
            self.canvas.coords(self.end_message_window, width//2, height//2)

    def animate(self):
        """Animation principale"""
        if self.current_month < len(self.fib_sequence):
            new_lapins = self.fib_sequence[self.current_month] - (self.fib_sequence[self.current_month-1] if self.current_month > 0 else 0)
            width = self.canvas.winfo_width()
            height = self.canvas.winfo_height()

            # Ajouter les nouveaux lapins avec effet d'apparition
            for _ in range(new_lapins):
                rel_x = random.uniform(0.1, 0.9)
                rel_y = random.uniform(0.1, 0.9)
                x = int(rel_x * (width * 0.8) + width * 0.1)
                y = int(rel_y * (height * 0.8) + height * 0.1)

                # Ombre
                shadow_id = self.canvas.create_image(x+2, y+2, image=self.shadow_photo, anchor=tk.NW)
                # Lapin
                img_id = self.canvas.create_image(x, y, image=self.lapin_photo, anchor=tk.NW)
                self.lapins.append((rel_x, rel_y, img_id, shadow_id))

            self.total_lapins = self.fib_sequence[self.current_month]
            self.counter_var.set(f"Mois {self.current_month} : {self.total_lapins} lapins")
            self.current_month += 1
            self.animation_id = self.root.after(800, self.animate)
        else:
            self.show_completion()

    def show_completion(self):
        """Affichage du message de fin et du bouton"""
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Message de fin
        self.end_message_var = tk.StringVar(value="Simulation terminée !")
        self.end_message = ttk.Label(
            self.canvas, textvariable=self.end_message_var,
            style='End.TLabel'
        )
        self.end_message_window = self.canvas.create_window(0, 0, window=self.end_message, anchor=tk.CENTER)

        # Bouton Recommencer stylisé
        self.btn = ttk.Button(
            self.main_frame,
            text="Recommencer",
            command=self.reset,
            style="Accent.TButton"
        )
        self.btn_window = self.canvas.create_window(width//2, height*0.85, window=self.btn, anchor=tk.CENTER)

    def reset(self):
        """Réinitialisation complète"""
        # Arrêter l'animation en cours
        if self.animation_id:
            self.root.after_cancel(self.animation_id)

        # Effacer tous les éléments
        for _, _, img_id, shadow_id in self.lapins:
            self.canvas.delete(img_id)
            self.canvas.delete(shadow_id)
        self.lapins = []

        if self.end_message:
            self.end_message.destroy()
            self.end_message = None

        if self.btn:
            self.btn.destroy()
            self.btn = None

        # Réinitialiser les variables
        self.current_month = 0
        self.total_lapins = 0
        self.counter_var.set("Mois 0 : 0 lapins")

        # Relancer l'animation
        self.animate()

    def toggle_pause(self):
        """Pause/reprise de l'animation"""
        if self.animation_id:
            self.root.after_cancel(self.animation_id)
            self.animation_id = None
        else:
            self.animate()

    def show_context_menu(self, event):
        """Affichage du menu contextuel"""
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

if __name__ == "__main__":
    root = tk.Tk()
    app = FibonacciLapinsApp(root)
    root.mainloop()
