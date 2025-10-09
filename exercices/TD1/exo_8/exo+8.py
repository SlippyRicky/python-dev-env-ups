import math

# Ask the user for the diameter of the circle, with a default value of 4.56
diameter = input("Entrez le diamètre du cercle (default 4.56): ") or "4.56"

# Convert the input to a float
diameter = float(diameter)

# Compute the radius
radius = diameter / 2

# Compute the circumference
circumference = 2 * math.pi * radius

print(f"La circonférence du cercle est {circumference}")

