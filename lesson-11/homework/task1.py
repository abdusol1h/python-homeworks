import sqlite3

# Step 1: Create database and table
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# Step 2: Insert data
cursor.executemany("""
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

conn.commit()

# Step 3: Update Jadzia Dax's name to Ezri Dax
cursor.execute("""
UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'
""")
conn.commit()

# Step 4: Retrieve and display Name and Age where Species is Bajoran
cursor.execute("""
SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
""")
print("Bajoran Characters:", cursor.fetchall())

# Step 5: Delete characters older than 100 years
cursor.execute("""
DELETE FROM Roster WHERE Age > 100
""")
conn.commit()

# Step 6: Add a new column 'Rank'
cursor.execute("""
ALTER TABLE Roster ADD COLUMN Rank TEXT
""")
conn.commit()

# Step 6 (continued): Update Rank values
ranks = [
    ("Benjamin Sisko", "Captain"),
    ("Ezri Dax", "Lieutenant"),
    ("Kira Nerys", "Major")
]

for name, rank in ranks:
    cursor.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", (rank, name))
conn.commit()

# Step 7: Retrieve all characters sorted by Age (descending)
cursor.execute("""
SELECT * FROM Roster ORDER BY Age DESC
""")
print("Sorted by Age:", cursor.fetchall())

conn.close()