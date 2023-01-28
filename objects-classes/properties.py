# We use hidden attributes when we don't want attributes to be changed by anything/anyone
# It's done through getters and setters.
# Basic way:


class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print("inside the getter")
        return self.hidden_name

    def set_name(self, input_name):
        print("inside the setter")
        self.hidden_name = input_name

don = Duck("Donald")
print(don.get_name())
don.set_name("Donna")
print(don.get_name())

# But more pythonic way is properties:
print("========= Using properties method #1 =========")

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print("inside the getter")
        return self.hidden_name

    def set_name(self, input_name):
        print("inside the setter")
        self.hidden_name = input_name
    name = property(get_name, set_name)

don = Duck("Donald")
print(don.name)
don.name = "Donna"
print(don.name)

print("========= Using properties method #2 =========")

# In this method, we use decorators to define getters and setters
# @property is placed before getter
# @[variable_name].setter is placed before setter

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print("inside the getter")
        return self.hidden_name
    
    @name.setter
    def name(self, input_name):
        print("inside the setter")
        self.hidden_name = input_name

duck = Duck("Donald")
print(duck.name)
duck.name = "Donna" # note: we called setter function "name" as well, but it can be anything
print(duck.name)


print("========= Calculated properties =========")
# Properties can also be used to return calculated values. for example:

class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
print(c.diameter)
c.radius = 7
print(c.diameter) # there it is, calculated properties

print("========= Obfuscated attributes =========")

class Duck():
    def __init__(self, input_name):
        self.__name = input_name
        # adding __ to beginning of variable name won't allow to access this
        # variable outside of class by [obj].__[variable], but you still can:
        # [obj]._[cls_name]__[variable]

    @property
    def name(self):
        print("inside the getter")
        return self.__name

    @name.setter
    def name(self, input_name):
        print("inside the setter")
        self.__name = input_name

duck = Duck("Howard")
print(duck.name)
duck.name = "Donald"
print(duck.name)

try:
    print(duck.__name)
except AttributeError as err:
    print(err)

print(duck._Duck__name)

