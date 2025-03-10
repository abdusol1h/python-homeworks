from bs4 import BeautifulSoup

with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

rows = soup.find("table").find("tbody").find_all("tr")

weather_data = []
for row in rows:
    cols = row.find_all("td")
    day = cols[0].text
    temp = int(cols[1].text.replace("°C", ""))  # Convert to integer
    condition = cols[2].text
    weather_data.append({"day": day, "temperature": temp, "condition": condition})

for entry in weather_data:
    print(f"{entry['day']}: {entry['temperature']}°C, {entry['condition']}")

# Finding the hottest day
hottest_day = max(weather_data, key=lambda x: x["temperature"])
print(f"\nHottest day: {hottest_day['day']} with {hottest_day['temperature']}°C")

# Finding all Sunny days
sunny_days = [entry["day"] for entry in weather_data if entry["condition"] == "Sunny"]
print(f"Sunny days: {', '.join(sunny_days)}")

# Compute average temperature
average_temp = sum(entry["temperature"] for entry in weather_data) / len(weather_data)
print(f"Average temperature for the week: {average_temp:.2f}°C")