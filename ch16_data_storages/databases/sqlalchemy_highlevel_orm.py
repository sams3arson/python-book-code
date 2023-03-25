import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, sessionmaker

engine = sa.create_engine("sqlite:///zoo.db")
conn = engine.connect()

Base = declarative_base()
class Zoo(Base):
    __tablename__ = "zoo"
    critter = sa.Column('critter', sa.String, primary_key=True)
    count = sa.Column('count', sa.Integer)
    damages = sa.Column('damages', sa.Float)

    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = count
        self.damages = damages

    def __repr__(self):
        return "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)

Base.metadata.create_all(conn)

first = Zoo("duck", 10, 0.0)
second = Zoo("bear", 2, 1000.0)
third = Zoo("weasel", 1, 2000.0)
print(first)


Session = sessionmaker(bind=engine)
session = Session()

session.add(first)
session.add_all([second, third])
session.commit()

