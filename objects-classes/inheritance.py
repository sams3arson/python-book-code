# inheritance is creating a new class from one that already exists with some
# additions and changes
# the original class is called as parent class/superclass/basic class
# new class is called child/subclass/derived class

class Car():
    pass

class Yugo(Car):
    pass

class Megashit(Yugo):
    pass

print(issubclass(Yugo, Car), issubclass(Megashit, Yugo), issubclass(Yugo, Megashit))
# check if a class is inherited from other class

class Car():
    def exclaim(self):
        print("I'm a car.")

class Yugo(Car):
    pass

car = Car()
yugo = Yugo()
car.exclaim()
yugo.exclaim()

class Car():
    def exclaim(self):
        print("I'm a car.")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo!.")
car = Car()
yugo = Yugo()
car.exclaim()
yugo.exclaim()

class Car():
    def exclaim(self):
        print("I'm a car.")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo!.")
    def need_a_push(self):
        print("A little help here?")
car = Car()
yugo = Yugo()
car.exclaim()
yugo.exclaim()
yugo.need_a_push()

class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        # super() is useful when subclass has some specifics but most of work
        # can be done by parent class; also the right way to inherit changes
        # from parent class
        super().__init__(name)
        self.email = email

bob = EmailPerson("Bob Frapples", "bob@frapples.com")
print(bob.name, bob.email)

# Multiple inheritance:

class Animal():
    def says(self):
        return "I speak!"

class Horse(Animal):
    def says(self):
        return "Neigh!"

class Donkey(Animal):
    def says(self):
        return "Hee-haw!"

class Mule(Donkey, Horse):
    pass

class Hinny(Horse, Donkey):
    pass

# class.mro() method shows order of classes, in which Python will look for
# class method or attribute
print("Mule.mro():", Mule.mro())
print("Hinny.mro():", Hinny.mro())

print(Mule().says(), Hinny().says())

# Mixin classes. Mixin classes are auxiliary classes for performing other tasks,
# not directly related to class or its parents.

class DumperMixin():
    def dump(self):
        print(vars(self))

class Thing(DumperMixin):
    def __init__(self, title):
        self.title = title
t = Thing("Table")
t.dump()


