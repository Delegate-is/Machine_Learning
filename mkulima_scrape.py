from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Launch Chrome automatically
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://www.mkulimaonline.co.ke/home/category/1?page=1"
driver.get(url)

time.sleep(5)  # Wait for JavaScript to load products

items = driver.find_elements(By.CLASS_NAME, "card-body")

data = []

for item in items:
    try:
        title = item.find_element(By.TAG_NAME, "h5").text
        price = item.find_element(By.CLASS_NAME, "text-primary").text
        location = item.find_element(By.CLASS_NAME, "text-muted").text

        data.append({
            "title": title,
            "price": price,
            "location": location
        })
    except:
        continue

driver.quit()

df = pd.DataFrame(data)
print(df)

df.to_csv("mkulima_online_listings.csv", index=False)
print("Saved to mkulima_online_listings.csv")
