import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
def plot_cube(cote, ax):
    ax.clear()
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
    ax.set_box_aspect([1, 1, 1])
    ax.set_title(f"Cube (Côté = {cote}, Volume = {volume_cube(cote):.2f})")

def plot_sphere(rayon, ax):
    ax.clear()
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = rayon * np.outer(np.cos(u), np.sin(v))
    y = rayon * np.outer(np.sin(u), np.sin(v))
    z = rayon * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='c', alpha=0.5)
    ax.set_xlim([-rayon, rayon])
    ax.set_ylim([-rayon, rayon])
    ax.set_zlim([-rayon, rayon])
    ax.set_box_aspect([1, 1, 1])
    ax.set_title(f"Sphère (Rayon = {rayon}, Volume = {volume_sphere(rayon):.2f})")

def plot_cone(rayon, hauteur, ax):
    ax.clear()
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
    ax.set_box_aspect([1, 1, hauteur/rayon])
    ax.set_title(f"Cône (Rayon = {rayon}, Hauteur = {hauteur}, Volume = {volume_cone(rayon, hauteur):.2f})")

def plot_pyramide(base, hauteur, ax):
    ax.clear()
    apex = np.array([base/2, base/2, hauteur])
    vertices = np.array([
        [0, 0, 0],
        [base, 0, 0],
        [base, base, 0],
        [0, base, 0]
    ])
    faces = [
        [vertices[0], vertices[1], vertices[2]],
        [vertices[0], vertices[1], apex],
        [vertices[1], vertices[2], apex],
        [vertices[2], vertices[3], apex],
        [vertices[3], vertices[0], apex]
    ]
    colors = ['y', 'm', 'c', 'r', 'g']
    base_quad = np.array([vertices[0], vertices[1], vertices[2], vertices[3]])
    ax.plot_trisurf(base_quad[:, 0], base_quad[:, 1], base_quad[:, 2], color=colors[0], alpha=0.5)
    for i, face in enumerate(faces[1:], start=1):
        ax.plot_trisurf(np.array(face)[:, 0], np.array(face)[:, 1], np.array(face)[:, 2], color=colors[i], alpha=0.5)
    ax.set_xlim([0, base])
    ax.set_ylim([0, base])
    ax.set_zlim([0, hauteur])
    ax.set_box_aspect([1, 1, hauteur / base])
    ax.set_title(f"Pyramide (Base = {base}, Hauteur = {hauteur}, Volume = {volume_pyramide(base, hauteur):.2f})")

def update_plot(event=None):
    shape = shape_var.get()
    try:
        dim1 = float(dim1_entry.get())
    except ValueError:
        dim1 = 1.0  # Default value if input is invalid
    try:
        dim2 = float(dim2_entry.get()) if shape in ["cone", "pyramide"] else None
    except ValueError:
        dim2 = 1.0  # Default value if input is invalid

    ax.clear()
    if shape == "cube":
        plot_cube(dim1, ax)
    elif shape == "sphere":
        plot_sphere(dim1, ax)
    elif shape == "cone":
        plot_cone(dim1, dim2, ax)
    elif shape == "pyramide":
        plot_pyramide(dim1, dim2, ax)
    canvas.draw()

def update_input_fields(*args):
    shape = shape_var.get()
    if shape in ["cone", "pyramide"]:
        dim2_label.pack(pady=5)
        dim2_entry.pack(pady=5)
    else:
        dim2_label.pack_forget()
        dim2_entry.pack_forget()

# Create the main window
root = tk.Tk()
root.title("3D Shapes Viewer")
root.attributes('-topmost', True)  # Bring the window to the front
root.attributes('-topmost', False)  # Release the topmost attribute after bringing it to the front

# Create a frame for the sidebar
sidebar = ttk.Frame(root, width=200)
sidebar.pack(side="left", fill="y")

# Create a frame for the plot
plot_frame = ttk.Frame(root)
plot_frame.pack(side="right", fill="both", expand=True)

# Create the figure and axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Create the canvas for the plot
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

# Add widgets to the sidebar
ttk.Label(sidebar, text="Select Shape:").pack(pady=5)
shape_var = tk.StringVar()
shape_dropdown = ttk.OptionMenu(sidebar, shape_var, "cube", "cube", "sphere", "cone", "pyramide", command=lambda _: [update_plot(), update_input_fields()])
shape_dropdown.pack(pady=5)

ttk.Label(sidebar, text="Largeur:").pack(pady=5)
dim1_entry = ttk.Entry(sidebar)
dim1_entry.pack(pady=5)
dim1_entry.insert(0, "1.0")  # Default value
dim1_entry.bind("<Return>", update_plot)

dim2_label = ttk.Label(sidebar, text="Hauteur:")
dim2_entry = ttk.Entry(sidebar)
dim2_entry.insert(0, "1.0")  # Default value
dim2_entry.bind("<Return>", update_plot)

# Initial plot and input fields
update_input_fields()
update_plot()

# Start the Tkinter event loop
root.mainloop()
