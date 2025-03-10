import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Set up Selenium WebDriver
service = Service("chromedriver.exe")  # Update path as needed
driver = webdriver.Chrome(service=service)

driver.get("https://www.demoblaze.com/")
time.sleep(3)  # Allow time for the page to load

driver.find_element(By.LINK_TEXT, "Laptops").click()
time.sleep(3)

laptops = []

# Scrape laptops
while True:
    items = driver.find_elements(By.CLASS_NAME, "card-title")
    
    for item in items:
        name = item.text
        item.click()
        time.sleep(2)

        price = driver.find_element(By.CLASS_NAME, "price-container").text.split()[0]
        description = driver.find_element(By.ID, "more-information").text

        laptops.append({
            "name": name,
            "price": price,
            "description": description
        })

        driver.back()
        time.sleep(2)

    # Try to click Next button
    try:
        next_btn = driver.find_element(By.LINK_TEXT, "Next")
        next_btn.click()
        time.sleep(3)
    except:
        break  # No next button, exit loop

with open("laptops.json", "w", encoding="utf-8") as file:
    json.dump(laptops, file, indent=4)

driver.quit()