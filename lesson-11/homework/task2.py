import sqlite3

# Step 1: Create database and table
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
""")

# Step 2: Insert data
cursor.executemany("""
INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)
""", [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
])

conn.commit()

# Step 3: Update Year_Published of 1984 to 1950
cursor.execute("""
UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'
""")
conn.commit()

# Step 4: Retrieve Title and Author where Genre is Dystopian
cursor.execute("""
SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'
""")
print("Dystopian Books:", cursor.fetchall())

# Step 5: Delete books published before 1950
cursor.execute("""
DELETE FROM Books WHERE Year_Published < 1950
""")
conn.commit()

# Step 6: Add new column 'Rating'
cursor.execute("""
ALTER TABLE Books ADD COLUMN Rating REAL
""")
conn.commit()

# Step 6 (continued): Update Rating values
ratings = [
    ("To Kill a Mockingbird", 4.8),
    ("1984", 4.7),
    ("The Great Gatsby", 4.5)
]

for title, rating in ratings:
    cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (rating, title))
conn.commit()

# Step 7: Retrieve all books sorted by Year_Published (ascending)
cursor.execute("""
SELECT * FROM Books ORDER BY Year_Published ASC
""")
print("Sorted by Year Published:", cursor.fetchall())

conn.close()