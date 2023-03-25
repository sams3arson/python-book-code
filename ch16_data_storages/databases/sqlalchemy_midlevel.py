import sqlalchemy as sa

engine = sa.create_engine("sqlite://")
conn = engine.connect()

meta = sa.MetaData()
zoo = sa.Table("zoo", meta,
               sa.Column('critter', sa.String, primary_key=True),
               sa.Column('count', sa.Integer),
               sa.Column('damages', sa.Float)
)
meta.create_all(conn)

conn.execute(zoo.insert().values(critter="bear", count=2, damages=1000.0))
conn.execute(zoo.insert().values(critter="weasel", count=1, damages=2000.0))
result = conn.execute(zoo.select())

rows = result.fetchall()
print(rows)

