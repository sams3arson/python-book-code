# object/class is a data structure that has attributes (data) and methods (functions)

class Cat():
    pass

cat = Cat()
another_cat = Cat()

# attribute is a variable of a class or object
# attributes can be created at the time of createing an object (defined in class)
# or after creating an object

cat.age = 3
cat.name = "Mr. Fuzzybuttons"
cat.nemesis = another_cat

print(cat.age, cat.name, cat.nemesis)

another_cat.name = "Mr. Bigglesworth"
print(another_cat.name, cat.nemesis.name)

class Cat():
    def __init__(self, name):
        self.name = name

furball = Cat("Grumpy")
print("name:", furball.name)

# classes' and objects' attributes:

class Fruit():
    color = "red"

blueberry = Fruit()
print(blueberry.color, Fruit.color)

blueberry.color = "blue"
print(blueberry.color, Fruit.color)

Fruit.color = "orange"
new_fruit = Fruit()
print(new_fruit.color, Fruit.color, blueberry.color)

