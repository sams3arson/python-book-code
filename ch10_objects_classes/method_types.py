class Duck():
    def object_method_example(self):
        return "This method is object's method, first argument is object ('self')."

    @classmethod
    def class_method_example(cls):
        return "This method is class's method, first argument is "\
                "class, usually called 'cls'."

    @staticmethod
    def static_method_example():
        return "This method is static method, it doesn't take object or class"\
                " as first argument."

class A():
    count = 0

    def __init__(self):
        A.count += 1

    @classmethod
    def kids(cls):
        print("A has", cls.count, "objects.") # A.count can do the same thing

a1 = A()
a2 = A()
a3 = A()
A.kids()

class CoyoteWeapon():
    @staticmethod
    def commercial():
        print("This CoyoteWeapon has been brought to you by Acme")

CoyoteWeapon.commercial()

