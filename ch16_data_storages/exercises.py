import csv
from pprint import pprint

# 16.2
with open("books1.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    books = [row for row in reader]
pprint(books)

# 16.4
import sqlite3
conn = sqlite3.connect("books.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS books (title text, author text, year"
               " integer)")
conn.commit()

# 16.5
with open("books2.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    books = [row for row in reader]

for book in books:
    cursor.execute("INSERT INTO books VALUES (?, ?, ?)",
                   (book["title"], book["author"], book["year"]))
conn.commit()

# 16.6
cursor.execute("SELECT title FROM books ORDER BY title")
result = cursor.fetchall()
print([row[0] for row in result])

# 16.7
cursor.execute("SELECT * FROM books ORDER BY year")
result = cursor.fetchall()
print(result)

# 16.8
import sqlalchemy as sa
engine = sa.create_engine("sqlite:///books.db")
conn = engine.connect()
result = conn.execute(sa.text("SELECT title FROM books ORDER BY title"))
print([row[0] for row in result.fetchall()])

