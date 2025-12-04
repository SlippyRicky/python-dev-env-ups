import os
os.environ['MPLBACKEND'] = 'TkAgg'  # or another backend like 'Qt5Agg'
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Functions to calculate volume
def volume_cube(cote):
    return cote ** 3

def volume_sphere(rayon):
    return (4/3) * np.pi * (rayon ** 3)

def volume_cone(rayon, hauteur):
    return (1/3) * np.pi * (rayon ** 2) * hauteur

def volume_pyramide(base, hauteur):
    return (1/3) * (base ** 2) * hauteur

# Functions to plot shapes
def plot_cube(cote):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    r = [0, cote]
    X, Y = np.meshgrid(r, r)
    Z = np.array([[0, 0], [0, 0]])
    ax.plot_surface(X, Y, Z + cote, color='b', alpha=0.5)
    ax.plot_surface(X, Y, Z, color='b', alpha=0.5)
    X, Z = np.meshgrid(r, r)
    ax.plot_surface(X, Y[0], Z, color='g', alpha=0.5)
    ax.plot_surface(X, Y[1], Z, color='g', alpha=0.5)
    Y, Z = np.meshgrid(r, r)
    ax.plot_surface(Y, X[0], Z, color='r', alpha=0.5)
    ax.plot_surface(Y, X[1], Z, color='r', alpha=0.5)
    ax.set_xlim([0, cote])
    ax.set_ylim([0, cote])
    ax.set_zlim([0, cote])
    ax.set_box_aspect([1, 1, 1])  # Set equal aspect ratio
    ax.set_title(f"Cube (Côté = {cote})")
    plt.show()

def plot_sphere(rayon):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = rayon * np.outer(np.cos(u), np.sin(v))
    y = rayon * np.outer(np.sin(u), np.sin(v))
    z = rayon * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='c', alpha=0.5)
    ax.set_xlim([-rayon, rayon])
    ax.set_ylim([-rayon, rayon])
    ax.set_zlim([-rayon, rayon])
    ax.set_box_aspect([1, 1, 1])  # Set equal aspect ratio
    ax.set_title(f"Sphère (Rayon = {rayon})")
    plt.show()

def plot_cone(rayon, hauteur):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    theta = np.linspace(0, 2*np.pi, 100)
    x = rayon * np.cos(theta)
    y = rayon * np.sin(theta)
    z = np.zeros_like(theta)
    ax.plot(x, y, z, color='k')
    theta = np.linspace(0, 2*np.pi, 100)
    z = np.linspace(0, hauteur, 100)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = rayon * (1 - z_grid/hauteur) * np.cos(theta_grid)
    y_grid = rayon * (1 - z_grid/hauteur) * np.sin(theta_grid)
    ax.plot_surface(x_grid, y_grid, z_grid, color='m', alpha=0.5)
    ax.set_xlim([-rayon, rayon])
    ax.set_ylim([-rayon, rayon])
    ax.set_zlim([0, hauteur])
    ax.set_box_aspect([1, 1, 1])  # Set equal aspect ratio
    ax.set_title(f"Cône (Rayon = {rayon}, Hauteur = {hauteur})")
    plt.show()

def plot_pyramide(base, hauteur):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Define vertices of the pyramid
    apex = np.array([base/2, base/2, hauteur])
    vertices = np.array([
        [0, 0, 0],
        [base, 0, 0],
        [base, base, 0],
        [0, base, 0]
    ])

    # Define the faces of the pyramid with different colors
    faces = [
        [vertices[0], vertices[1], vertices[2]],  # Base
        [vertices[0], vertices[1], apex],  # Front face
        [vertices[1], vertices[2], apex],  # Right face
        [vertices[2], vertices[3], apex],  # Back face
        [vertices[3], vertices[0], apex]   # Left face
    ]

    colors = ['y', 'm', 'c', 'r', 'g']  # Colors for each face

    # Plot the base (quadrilateral)
    base_quad = np.array([vertices[0], vertices[1], vertices[2], vertices[3]])
    ax.plot_trisurf(base_quad[:, 0], base_quad[:, 1], base_quad[:, 2], color=colors[0], alpha=0.5)

    # Plot the lateral faces with different colors
    for i, face in enumerate(faces[1:], start=1):
        ax.plot_trisurf(np.array(face)[:, 0], np.array(face)[:, 1], np.array(face)[:, 2], color=colors[i], alpha=0.5)

    # Set limits to ensure the base occupies as much of the base plane as possible
    ax.set_xlim([0, base])
    ax.set_ylim([0, base])
    ax.set_zlim([0, hauteur])

    # Set aspect ratio to ensure the base is square and the z-axis is stretched
    ax.set_box_aspect([1, 1, hauteur / base])
    ax.set_title(f"Pyramide (Base = {base}, Hauteur = {hauteur})")
    plt.show()


# Main function for interaction
def visualiser(forme, longueur1, longueur2=None):
    if forme == "cube":
        plot_cube(longueur1)
    elif forme == "sphere":
        plot_sphere(longueur1)
    elif forme == "cone":
        if longueur2 is None:
            longueur2 = float(input("Entrez la hauteur du cône: "))
        plot_cone(longueur1, longueur2)
    elif forme == "pyramide":
        if longueur2 is None:
            longueur2 = float(input("Entrez la hauteur de la pyramide: "))
        plot_pyramide(longueur1, longueur2)

# User interaction
if __name__ == "__main__":
    formes_valides = ["cube", "sphere", "cone", "pyramide"]

    while True:
        print("Choisissez une forme parmi : cube, sphere, cone, pyramide")
        forme = input("Forme : ").strip().lower()

        forme_trouvee = None
        for f in formes_valides:
            if f in forme:
                forme_trouvee = f
                break

        if forme_trouvee:
            count = sum(1 for f in formes_valides if f in forme)
            if count > 1:
                print("Plusieurs formes détectées. Veuillez entrer une seule forme.")
                continue
            else:
                forme = forme_trouvee
                break
        else:
            print("Forme non reconnue. Veuillez choisir parmi : cube, sphere, cone, pyramide")

    longueur1 = float(input("Longueur 1 (côté/rayon/base) : "))

    if forme in ["cone", "pyramide"]:
        longueur2 = float(input("Longueur 2 (hauteur) : "))
    else:
        longueur2 = None

    visualiser(forme, longueur1, longueur2)
