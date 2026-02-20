import googlemaps
import itertools
import numpy as np

# 🔑 Insert your Google API key here
API_KEY = "AIzaSyCXXXXXXXXXXXXXXXXXXXX"

gmaps = googlemaps.Client(key=API_KEY)

# Starting point
origin = "Nanyuki, Kenya"

# List of schools
schools = [
    "DEB Solio Secondary School, Laikipia, Kenya",
    "Ihigaini Mixed Day Secondary School, Laikipia, Kenya",
    "Imenti Secondary School, Laikipia, Kenya",
    "Irrura Day Secondary School, Laikipia, Kenya",
    "Karigu Ini Secondary School, Laikipia, Kenya",
    "Kihato Secondary School, Laikipia, Kenya",
    "Laikipia Air Base School, Nanyuki, Kenya",
    "Lechugu Secondary School, Laikipia, Kenya",
    "Malek Girls Secondary School, Laikipia, Kenya",
    "Muhonia Secondary School, Laikipia, Kenya",
    "Mukadamia Solio School, Laikipia, Kenya",
    "Mwihoko Secondary School, Laikipia, Kenya",
    "Mwituria Day School, Laikipia, Kenya",
    "Ngobit Boys Secondary School, Laikipia, Kenya",
    "Ngobit Girls Secondary School, Laikipia, Kenya",
    "Nyakio Day Secondary School, Laikipia, Kenya",
    "Oltaffeta Day Secondary School, Nanyuki, Kenya",
    "Shalom Canaan Secondary School, Laikipia, Kenya",
    "St Augustine Sirima Secondary School, Laikipia, Kenya",
    "St Joseph Tigithi Boys Secondary School, Laikipia, Kenya",
    "Sweetwaters Girls Secondary School, Nanyuki, Kenya",
    "Sweetwaters Mixed Day Secondary School, Nanyuki, Kenya",
    "Tharua Day Secondary School, Laikipia, Kenya",
    "Thome Boys Secondary School, Laikipia, Kenya",
    "Waguthiru Secondary School, Laikipia, Kenya",
    "Wathituga Secondary School, Laikipia, Kenya",
    "Withare Mixed Secondary School, Laikipia, Kenya"
]

# Combine origin + schools
locations = [origin] + schools

# Get distance matrix
matrix = gmaps.distance_matrix(locations, locations, mode="driving")

# Build distance array
distance_matrix = []
for row in matrix['rows']:
    distance_row = []
    for element in row['elements']:
        distance_row.append(element['distance']['value'])
    distance_matrix.append(distance_row)

distance_matrix = np.array(distance_matrix)

# Solve TSP (brute force – works up to ~10-12 points efficiently)
# For 27+ schools, use heuristic (below)

def nearest_neighbor(dist_matrix):
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True

    for _ in range(n - 1):
        last = route[-1]
        next_city = np.argmin([
            dist_matrix[last][i] if not visited[i] else float('inf')
            for i in range(n)
        ])
        route.append(next_city)
        visited[next_city] = True

    return route

route = nearest_neighbor(distance_matrix)

# Print optimal order
print("Optimal Route:\n")
for index in route:
    print(locations[index])
