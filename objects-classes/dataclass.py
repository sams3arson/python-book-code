from dataclasses import dataclass

# Usual class:
class Dog():
    def __init__(self, name):
        self.name = name

dog = Dog("Barker")
print(dog.name)

# using dataclass:
@dataclass
class DogClass():
    name: str
    age: int = 0

dog1 = DogClass(name="Barker") # age is set by default
print(dog1.name, dog1.age)
dog2 = DogClass(name="Strelka", age=3)
print(dog2.name, dog2.age)

# Official documentation on dataclasses: https://www.python.org/dev/peps/pep-0557/

