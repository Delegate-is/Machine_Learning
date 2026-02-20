import pandas as pd

# Orodha ya shule kulingana na mpango tuliopanga (Optimized Order)
optimized_route = [
    {"Sequence": 1, "Cluster": "Solio & Ngobit", "School Name": "Mukadamia Solio School"},
    {"Sequence": 2, "Cluster": "Solio & Ngobit", "School Name": "DEB Solio Secondary School"},
    {"Sequence": 3, "Cluster": "Solio & Ngobit", "School Name": "Ngobit Girls Secondary School"},
    {"Sequence": 4, "Cluster": "Solio & Ngobit", "School Name": "Ngobit Boys Secondary School"},
    {"Sequence": 5, "Cluster": "Solio & Ngobit", "School Name": "Withare Mixed Secondary School"},
    {"Sequence": 6, "Cluster": "Solio & Ngobit", "School Name": "Tharua Day Secondary School"},
    {"Sequence": 7, "Cluster": "Solio & Ngobit", "School Name": "Wathituga Secondary School"},
    {"Sequence": 8, "Cluster": "Solio & Ngobit", "School Name": "Nyakio Day Secondary School"},
    {"Sequence": 9, "Cluster": "Tigithi & Central", "School Name": "St. Joseph Tigithi Boys Secondary School"},
    {"Sequence": 10, "Cluster": "Tigithi & Central", "School Name": "Imenti Secondary School"},
    {"Sequence": 11, "Cluster": "Tigithi & Central", "School Name": "Irrura Day Secondary School"},
    {"Sequence": 12, "Cluster": "Tigithi & Central", "School Name": "Kihato Secondary School"},
    {"Sequence": 13, "Cluster": "Tigithi & Central", "School Name": "Karigu Ini Secondary School"},
    {"Sequence": 14, "Cluster": "Tigithi & Central", "School Name": "Thome Boys Secondary School"},
    {"Sequence": 15, "Cluster": "Tigithi & Central", "School Name": "Waguthiru Secondary School"},
    {"Sequence": 16, "Cluster": "Tigithi & Central", "School Name": "Ihigaini Mixed Day Secondary School"},
    {"Sequence": 17, "Cluster": "Nanyuki & Airbase", "School Name": "Laikipia Air Base School"},
    {"Sequence": 18, "Cluster": "Nanyuki & Airbase", "School Name": "Sweetwaters Girls Secondary School"},
    {"Sequence": 19, "Cluster": "Nanyuki & Airbase", "School Name": "Sweetwaters Mixed Day Secondary School"},
    {"Sequence": 20, "Cluster": "Nanyuki & Airbase", "School Name": "Shalom Canaan Secondary School"},
    {"Sequence": 21, "Cluster": "Nanyuki & Airbase", "School Name": "Malek Girls Secondary School"},
    {"Sequence": 22, "Cluster": "Nanyuki & Airbase", "School Name": "Lechugu Secondary School"},
    {"Sequence": 23, "Cluster": "Nanyuki & Airbase", "School Name": "Muhonia Secondary School"},
    {"Sequence": 24, "Cluster": "Nanyuki & Airbase", "School Name": "Oltaffeta Day Secondary School"},
    {"Sequence": 25, "Cluster": "Nanyuki & Airbase", "School Name": "St Augustine Sirima Secondary School"},
    {"Sequence": 26, "Cluster": "Nanyuki & Airbase", "School Name": "Mwituria Day School"},
    {"Sequence": 27, "Cluster": "Nanyuki & Airbase", "School Name": "Mwihoko Secondary School"}
]

# Unda DataFrame
df = pd.DataFrame(optimized_route)

# Hifadhi kwenye Excel
file_name = "Ariel_Logistics_Laikipia_Route.xlsx"
df.to_excel(file_name, index=False)

print(f"Mafanikio! Mpango wa njia umehifadhiwa kwenye: {file_name}")