import openrouteservice
import numpy as np


# 🔑 Insert your ORS API key here
client = openrouteservice.Client(key='48f54a706812bd0046dc30164dd57581ft4dN8BlKdw')

# List of schools from your previous list
schools = [
    "DEB Solio Secondary School, Laikipia, Kenya",
    "Ihigaini Mixed Day Secondary School, Laikipia, Kenya",
    "Imenti Secondary School, Laikipia, Kenya" 
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

coords = []
for school in schools:
    try:
        # 🛠️ Updated geocoding call
        res = client.pelias_search(text=school)
        if res['features']:
            coords.append(res['features'][0]['geometry']['coordinates'])
        else:
            print(f"No results found for {school}")
    except Exception as e:
        print(f"Error geocoding {school}: {e}")

# Proceed to distance_matrix as before...

# 2. Get Distance Matrix (ORS allows up to 50x50 for free)
matrix = client.distance_matrix(
    locations=coords,
    profile='driving-car',
    metrics=['distance']
)

dist_matrix = np.array(matrix['distances'])

# 3. Your Nearest Neighbor Logic (Same as before)
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

optimal_indices = nearest_neighbor(dist_matrix)

print("Optimal Sequence for Laikipia East:")
for idx in optimal_indices:
    print(schools[idx])