import requests

url = "https://linkedin-jobs-search.p.rapidapi.com/"

payload = {
    "search_terms": "Junior Data Analyst",
    "location": "Kenya",
    "page": 1
}

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "linkedin-jobs-search.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
