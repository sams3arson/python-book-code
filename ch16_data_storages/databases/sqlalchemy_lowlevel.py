import sqlalchemy as sa

engine = sa.create_engine("sqlite://") # create engine: sqlite DB in ram
conn = engine.connect() # connect to it

# pass sql statement as str to sqlalchemy.text() and then pass it to
# connection.execute()
result = conn.execute(sa.text("""CREATE TABLE zoo
             (critter VARCHAR(20) PRIMARY KEY,
             count INT,
             damages FLOAT)"""))

ins = sa.text("INSERT INTO zoo (critter, count, damages) VALUES ('duck', 10, 0.0)")
conn.execute(ins)

