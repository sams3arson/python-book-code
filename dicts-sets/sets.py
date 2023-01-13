empty_set = set()
# empty set can only be created by set(); {} - dict

even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(empty_set, even_numbers, odd_numbers)

print(set("letters"))
print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))
print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother')))
print(set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}))

a = set(["Dasher", "Dancer", "Prancer"])
print(len(a))

s = set((1, 2, 3))
print(s)
s.add(4)
print(s)

s.remove(3)
print(s)

furniture = set(('sofa', 'ottoman', 'table'))
for piece in furniture:
    print(piece)

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}
for name, contents in drinks.items():
    if "vodka" in contents:
        print(name)

for name, contents in drinks.items():
    if "vodka" in contents and not("vermouth" in contents or "cream" in contents):
        print(name)

for name, contents in drinks.items():
    if contents & {"vermouth", "orange juice"}:
        print(name)
# & - set intersection operator, set & set = set of items that exist in both

for name, contents in drinks.items():
    if "vodka" in contents and not contents & {"vermouth", "cream"}:
        print(name)

bruss = drinks["black russian"]
wruss = drinks["white russian"]

a = {1, 2}
b = {2, 3}
print(a & b)
print(a.intersection(b))
print(bruss & wruss)
# & or set.intersection() do the same job - intersection for 2 sets

print(a | b)
print(a.union(b))
# | or set.union() do the same job - union for 2 sets

print(a - b)
print(a.difference(b))
print(bruss - wruss)
print(wruss - bruss)
# - or set.difference() shows difference between first and second set:
# returns items from first set that are not in the second set

print(a ^ b)
print(a.symmetric_difference(b))
# ^ or set.symmetric_difference() shows symmetric difference between 1 and 2 set:
# returns items from 1 set that are not in 2, and items from 2 set that are not in 1

print(a <= b)
print(a.issubset(b))
print(bruss <= wruss)
# <= or set.issubset() checks if items of first set are in the second set

print(a < b, a < a)
print(bruss < wruss)
# < - checks if items of first set are in the second set, and
# that the first set is not empty and not same as second (proper subset)

print(a >= b)
print(a.issuperset(b))
print(wruss >= bruss)
# < or set.issuperset() checks if items of second set are in first set
print(a.issuperset(a)) # true

print(a > b)
print(wruss > bruss)
print(a > a)
# > - checks if first set consists of items of second set and other items (proper superset)

a_set = {number for number in range(1, 6)}
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)

fs = frozenset([3, 2, 1])
fs = frozenset((2, 3, 1))
fs = frozenset({1, 2, 3})
# frozenset, accepts any iterable
print(fs)
# fs.add(4) - will give error as frozenset is a set that can't be changed



