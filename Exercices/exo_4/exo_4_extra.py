#!/usr/bin/env python3
import tkinter as tk
from tkinter import font
import math
import sys

class AnimationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bonjour le monde!")

        # Initial window size
        self.root.geometry("800x600")

        # Set the background color to black
        self.root.configure(bg='black')

        # Corrected line: Added 'black' as a string for the background color
        self.label = tk.Label(root, text="Bonjour le monde!", fg='red', bg='black')
        self.label.pack(expand=True, fill=tk.BOTH)

        # Bind the resize event
        self.root.bind('<Configure>', self.resize)

        self.start_gradient()

    def resize(self, event):
        # Calculate font size based on window width and height
        width = event.width
        height = event.height
        # Calculate base font size and add 10 points
        base_font_size = min(width, height) // 20
        font_size = base_font_size + 10

        # Set minimum and maximum font sizes
        min_font_size = 20
        max_font_size = 60

        # Ensure font size is within the specified range
        font_size = max(min_font_size, min(max_font_size, font_size))

        custom_font = font.Font(family="Helvetica", size=font_size, weight="bold")
        self.label.config(font=custom_font)

    def start_gradient(self):
        phase = 0
        def update_color():
            nonlocal phase
            # Use a sine wave to cycle through the color spectrum
            phase = (phase + 0.05) % (2 * math.pi)

            # Calculate RGB values based on the phase
            red = int((math.sin(phase) + 1) * 127.5)
            green = int((math.sin(phase + 2 * math.pi / 3) + 1) * 127.5)
            blue = int((math.sin(phase + 4 * math.pi / 3) + 1) * 127.5)

            # Convert RGB values to hexadecimal format for tkinter
            color = f'#{red:02x}{green:02x}{blue:02x}'
            self.label.config(fg=color)

            # Continue the animation
            self.root.after(50, update_color)

        update_color()

def main():
    root = tk.Tk()
    app = AnimationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
