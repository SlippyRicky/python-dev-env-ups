import math

diameter = 4.56
radius = diameter / 2
perimeter = round(2 * math.pi * radius, 2)
area = round(math.pi * radius**2, 2)
print(f"Le périmètre du disque est {perimeter} cm")
print(f"L'aire du disque est {area} cm²")
