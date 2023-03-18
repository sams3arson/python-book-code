class Thing():
    pass

example = Thing()
print(Thing, example)

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

element1 = Element("Hydrogen", "H", 1)
hydr_dict = {"name": "Hydrogen", "symbol": "H", "number": 1}
hydrogen = Element(**hydr_dict)

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    
    def dump(self):
        print(self.name, self.symbol, self.number)

hydrogen = Element(**hydr_dict)
hydrogen.dump()
print(hydrogen)


class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return ", ".join((self.name, self.symbol, str(self.number)))

hydrogen = Element(**hydr_dict)
print(hydrogen)

class Bear():
    def eats(self):
        return "berries"

class Rabbit():
    def eats(self):
        return "clover"

class Octothorpe():
    def eats(self):
        return "campers"

bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()
print(bear.eats(), rabbit.eats(), octothorpe.eats())


class Laser():
    def does(self):
        return "disintegrate"

class Claw():
    def does(self):
        return "crush"

class SmartPhone():
    def does(self):
        return "ring"

class Robot():
    def __init__(self, laser, claw, smartphone):
        self.laser = laser
        self.claw = claw
        self.smartphone = smartphone

    def does(self):
        print(self.laser.does(), self.claw.does(), self.smartphone.does())

robot = Robot(Laser(), Claw(), SmartPhone())
robot.does()

