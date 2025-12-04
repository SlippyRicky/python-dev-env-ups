import math

def distance_on_earth(lat1, long1, lat2, long2):
    lat1, long1, lat2, long2 = map(math.radians, [lat1, long1, lat2, long2])
    distance_angulaire = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(long2 - long1))
    rayon_terre = 6371
    distance = rayon_terre * distance_angulaire
    return distance

paris_lat = 48.86
paris_long = 2.35
london_lat = 51.51
london_long = -0.13

distance_paris_london = distance_on_earth(paris_lat, paris_long, london_lat, london_long)
print(f"La distance à vol d'oiseau entre Paris et Londres est d'environ {distance_paris_london} km.")

ny_lat = 40.71
ny_long = -74.01

distance_paris_ny = distance_on_earth(paris_lat, paris_long, ny_lat, ny_long)
print(f"La distance à vol d'oiseau entre Paris et New York est d'environ {distance_paris_ny} km.")
