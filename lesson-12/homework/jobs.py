import requests
import sqlite3
import csv
from bs4 import BeautifulSoup

# Database setup
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    location TEXT,
    description TEXT,
    apply_link TEXT,
    UNIQUE (title, company, location)
)
""")
conn.commit()

# Scrape job listings
url = "https://realpython.github.io/fake-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

job_listings = soup.find_all("div", class_="card-content")

for job in job_listings:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    description = job.find("div", class_="description").text.strip()
    apply_link = job.find("a")["href"]

    cursor.execute("""
    INSERT INTO jobs (title, company, location, description, apply_link) 
    VALUES (?, ?, ?, ?, ?) 
    ON CONFLICT(title, company, location) 
    DO UPDATE SET description=excluded.description, apply_link=excluded.apply_link
    """, (title, company, location, description, apply_link))

conn.commit()
conn.close()

print("Job listings scraped and stored successfully.")