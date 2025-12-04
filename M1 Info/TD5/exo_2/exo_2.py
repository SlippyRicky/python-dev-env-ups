import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    # Obtenir le chemin absolu du répertoire contenant le script
    script_dir = Path(__file__).parent

    # --- 1. Génération des données (Simulation de l'expérience) ---
    x = np.linspace(0, 2 * np.pi, 100)
    # Calcul du pas h (distance entre deux mesures consécutives)
    h = x[1] - x[0]
    # Création du signal bruité (fixe une fois pour toutes)
    np.random.seed(42)
    bruit = 0.1 * np.random.random(size=x.shape)
    y = np.sin(x) + bruit

    # --- 2. Définition des fonctions de dérivation numérique ---
    def derivee_forward(y_data, h):
        """
        Calcule la dérivée via l'approximation forward: (f(x+h) - f(x)) / h
        Note: On perd le dernier point car y[i+1] n'existe pas pour le dernier i.
        """
        dy = np.zeros_like(y_data)
        # Pour tout i jusqu'à l'avant-dernier
        for i in range(len(y_data) - 1):
            dy[i] = (y_data[i+1] - y_data[i]) / h
        dy[-1] = np.nan  # On met NaN pour ne pas l'afficher
        return dy

    def derivee_centre_5_points(y_data, h):
        """
        Calcule la dérivée via la formule centrée à 5 points.
        Formule: (-f(x+2h) + 8f(x+h) - 8f(x-h) + f(x-2h)) / 12h
        Note: Impossible à calculer pour les 2 premiers et 2 derniers points.
        """
        dy = np.zeros_like(y_data)
        N = len(y_data)

        # On commence à l'index 2 et on s'arrête 2 points avant la fin
        for i in range(2, N - 2):
            term1 = -y_data[i+2]
            term2 = 8 * y_data[i+1]
            term3 = -8 * y_data[i-1]
            term4 = y_data[i-2]
            dy[i] = (term1 + term2 + term3 + term4) / (12 * h)

        # On masque les bords invalides
        dy[0:2] = np.nan
        dy[-2:] = np.nan
        return dy

    # --- 3. Calculs ---
    dy_fwd = derivee_forward(y, h)
    dy_5pt = derivee_centre_5_points(y, h)
    dy_theorique = np.cos(x)  # La vraie dérivée de sin(x) sans bruit

    # --- 4. Affichage Graphique (Version Publication) ---
    plt.figure(figsize=(12, 8))

    # Graphique 1 : Les données brutes
    plt.subplot(2, 1, 1)
    plt.plot(x, y, 'o-', color='blue', label='Données mesurées (sin + bruit)', markersize=3, alpha=0.6)
    plt.plot(x, np.sin(x), 'k--', label='Signal réel (sans bruit)', alpha=0.5)
    plt.title("Données de l'expérience")
    plt.legend()
    plt.grid(True)

    # Graphique 2 : Les dérivées
    plt.subplot(2, 1, 2)
    plt.plot(x, dy_theorique, 'k-', linewidth=2, label="Dérivée théorique (cos)", alpha=0.4)
    plt.plot(x, dy_fwd, 'r-', linewidth=1, label="Approximation Forward")
    plt.plot(x, dy_5pt, 'g-', linewidth=2, label="Formule 5 points")
    plt.title("Comparaison des dérivées calculées")
    plt.xlabel("x")
    plt.ylabel("f'(x)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # --- 5. Sauvegarde du graphique ---
    # Création du dossier 'output' dans le répertoire du script s'il n'existe pas
    output_dir = script_dir / "output"
    output_dir.mkdir(exist_ok=True)

    # Chemin complet pour l'image
    image_path = output_dir / "derivatives_comparison.png"

    # Sauvegarde du graphique
    plt.savefig(image_path, format='png', dpi=200, bbox_inches='tight')
    print(f"Le graphique a été sauvegardé sous: {image_path.resolve()}")

    plt.show()

if __name__ == "__main__":
    main()
