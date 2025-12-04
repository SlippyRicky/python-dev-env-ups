import math

paris_lat = 48.86
paris_long = 2.35
londres_lat = 51.51
londres_long = -0.13
ny_lat = 40.71
ny_long = -74.01
rayon_terre = 6371

def distance_terrestre(lat1, long1, lat2, long2):
    lat1, long1, lat2, long2 = map(math.radians, [lat1, long1, lat2, long2])
    distance_angulaire = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(long2 - long1))
    distance_oiseau = rayon_terre * distance_angulaire
    return round(distance_oiseau, 4)

def distance_absolue(lat1, long1, lat2, long2):
    lat1, long1, lat2, long2 = map(math.radians, [lat1, long1, lat2, long2])
    x1 = rayon_terre * math.cos(lat1) * math.cos(long1)
    y1 = rayon_terre * math.cos(lat1) * math.sin(long1)
    z1 = rayon_terre * math.sin(lat1)
    x2 = rayon_terre * math.cos(lat2) * math.cos(long2)
    y2 = rayon_terre * math.cos(lat2) * math.sin(long2)
    z2 = rayon_terre * math.sin(lat2)
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return round(distance, 4)

distance_paris_londres = distance_terrestre(paris_lat, paris_long, londres_lat, londres_long)
distance_absolue_paris_londre = distance_absolue(paris_lat, paris_long, londres_lat, londres_long)
# print(distance_paris_londres)
# print(distance_absolue_paris_londre)
# print(distance_paris_ny)
# print(distance_absolue_paris_ny)
print(f"La distance à vol d'oiseau entre Paris et Londres est d'environ {distance_paris_londres} km, soit {round(distance_paris_londres - distance_absolue_paris_londre, 4)} km de plus que leur distance absolue.")
distance_paris_ny = distance_terrestre(paris_lat, paris_long, ny_lat, ny_long)
distance_absolue_paris_ny = distance_absolue(paris_lat, paris_long, ny_lat, ny_long)
print(f"La distance à vol d'oiseau entre Paris et New York est d'environ {distance_paris_ny} km, soit {round(distance_paris_ny - distance_absolue_paris_ny, 4)} km de plus que leur distance absolue.")
