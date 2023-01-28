from typing import NamedTuple

# Named tuple is type of tuple with which you can specify attributes of object
# and their types. And then you can access these attributes with
# [tuple_name].[attribute]

class Duck(NamedTuple):
    bill: str
    tail: str

duck = Duck(bill="wide orange", tail="long")
print(duck.bill, duck.tail)

# named tuple can also be created by unpacking a dict
parts = {"bill": "wide orange", "tail": "long"}
another_duck = Duck(**parts)

# you can use [namedtuple]._replace() function to get copy of that [namedtuple]
# with new values:
new_duck = another_duck._replace(tail="short")
print(new_duck.bill, new_duck.tail)

