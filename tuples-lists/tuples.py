empty_tuple = ()
print(empty_tuple)

actors = "Malek",
print(actors)
actors = ("Malek",)
print(actors)

actors = ("Malek", "Chaikin", "Slater") # () are not necessary but recommended
print(actors)

first, second, third = actors
print(first, second, third)

# tuple unpacking

password = "swordfish"
icecream = "tuttifrutti"
password, icecream = icecream, password
print(password, icecream)

# tuples can be used to reassign values to variables without temp variable

actors = ["Malek", "Chaikin", "Slater"]
print(tuple(actors))

actors_part1 = ("Malek", "Slater")
actors_part2 = ("Doubleday", "Chaikin")
print(actors_part1 + actors_part2)

print(("Malek",) * 3)

a = (7, 2)
b = (7, 2, 9)

print(a == b, a <= b, a < b)

actors = actors_part1
actors += actors_part2
print(actors)

