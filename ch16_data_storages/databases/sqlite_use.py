import sqlite3

conn = sqlite3.connect("enterprise.db")
curs = conn.cursor()
curs.execute("""CREATE TABLE IF NOT EXISTS zoo
             (critter VARCHAR(20) PRIMARY KEY,
             count INT,
             damages FLOAT)""")

# '?' in the sql query are values that will be passed as iterable to 
# cursor.execute() - the proper way to pass values
ins = "INSERT INTO zoo (critter, count, damages) VALUES (?, ?, ?)"
curs.execute(ins, ("duck", 5, 0.0))
curs.execute(ins, ("weasel", 1, 2000.0))
curs.execute(ins, ("bear", 2, 1000.0))

# use commit() to commit the changes without closing connection
conn.commit()

curs.execute("SELECT * FROM zoo")
rows = curs.fetchall()
print(rows)

curs.execute("SELECT * FROM zoo ORDER BY count")
rows = curs.fetchall()
print(rows)

curs.execute("SELECT * FROM zoo WHERE damages = (SELECT MAX(damages) FROM zoo)")
rows = curs.fetchall()
print(rows)

# close before finishing
curs.close()
conn.close()

