import requests
from bs4 import BeautifulSoup

# Jumia smartphones page (you can change category)
url = "https://www.jumia.co.ke/smartphones/"

# Send a GET request
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

# Find all product containers
products = soup.find_all("article", class_="prd")

print("---- JUMIA PRODUCT LIST ----")

for product in products:
    # Product name
    name_tag = product.find("h3", class_="name")
    name = name_tag.text.strip() if name_tag else "No name"

    # Product price
    price_tag = product.find("div", class_="prc")
    price = price_tag.text.strip() if price_tag else "No price"

    print(f"{name}  -->  {price}")
