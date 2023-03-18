# Composition and aggregation are often more useful than inheritance.
# Composition is when an object is part of another object.

class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print("This duck has", self.bill.description, "bill and a",
              self.tail.length, "tail")

a_bill = Bill("wide orange")
a_tail = Tail("long")
duck = Duck(a_bill, a_tail)
duck.about()

