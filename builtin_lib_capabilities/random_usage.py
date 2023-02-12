import random

# random.choice(iterable) - picks a random value from iterable
iterable1 = [23, 9, 46, "bacon", 0x123bc]
print(random.choice(iterable1))

# random.sample(iterable) - picks several random values from iterable; but doesn't picks one that are already picked so
# sample(..., x) != x * choice(...)
iterable2 = ("a", "one", "and-a", "two")
print(random.sample(iterable1, 3))
print(random.sample(iterable2, 2))
print(random.sample(range(100), 4))

print(random.randint(38, 74), random.randint(38, 74), random.randint(38, 74))  # random value between two ints

print(random.randrange(38, 74), random.randrange(38, 74, 10))  # random value from provided range

print(random.random())  # random real number between 0.0 and 1.0
