empty_list = []
another_empty_list = list()
print(empty_list, another_empty_list)

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(weekdays)

print(list("cat"))
a_tuple = ("ready", "fire", "aim")
print(list(a_tuple))

# list function can be used to create list object from an iterable object

pirate_day = "9/19/2019"
print(pirate_day.split("/"))
# string.split function returns a list object

actors = ["Malek", "Slater", "Chaikin"]
print(actors[0])
print(actors[1])
print(actors[2])

print(actors[1:3])
print(actors[::-1])
actors.reverse()
print(actors)
# part of lists can be accessed using slices
# [::-1] returns new reversed list; reverse() reverses the list itself

actors = ["Malek", "Chaikin"]

actors.append("Doubleday")
print(actors)

print(["bruh"] * 3)

actors = ["Malek", "Slater"]
others = ["Chaikin", "Doubleday"]
actors.extend(others)
print(actors)

numbers = [1, 2, 3, 4]
numbers[1:3] = [8, 9] # must be iterable
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = [7, 8, 9]
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = []
print(numbers)
# size of new value can be any

numbers = [1, 2, 3, 4]
numbers[1:3] = (98, 99, 100)
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = "wat?"
print(numbers)
# iterable can be literally anything that is iterable

del numbers[1]
print(numbers)
del numbers[0:2]
print(numbers)
# this way items from list can be deleted by their indexes or slices
# del can actually be applied to any variable to unlink it from an object
# and free the memory if that variable was the last link to that object

actors = ["Malek", "Slater", "Chaikin", "Doubleday", "Chaikin"]
actors.remove("Chaikin")
print(actors)
# list.remove() can remove an element of item by its value
# list.remove() removes only the first element found with specified value

print(actors.pop())
print(actors.pop(0))
print(actors)
# list.pop(x) removes and element at index x and returns its value
# if x is not provided, -1 (last element) is used

work_quotes = ['Working hard?', 'Quick question!', 'Number one priorities!']
work_quotes.clear() # from python 3.3
print(work_quotes)

actors = ["Malek", "Slater", "Doubleday", "Chaikin"]
print(actors.index("Slater"))
# returns index of the first match

print("Malek" in actors, "Slater" in actors)
# True while at least one item with specified value is in list

actors = ["Malek", "Slater", "Chaikin", "Doubleday", "Chaikin"]
print(actors.count("Chaikin"))

separator = ", "
joined = separator.join(actors)
print(joined)
print(", ".join(actors))
# str.join() can take any iterable including a string

actors = ["Malek", "Slater", "Doubleday", "Chaikin"]
actors_sorted = sorted(actors) # returns a sorted list
actors.sort() # sorts the list itself
actors.sort(reverse=True)
print(actors_sorted, actors)
# note: all list elements must be same type

print(len(actors))

a = [1, 2, 3]
b = a
print(a, b)
a[0] = "surprise"
print(a, b)
# a and b are both links to the same list

a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]
a[0] = "no surprise"
print(a, b, c, d)

import copy
a = [1, 2, [8, 9]]
b = a.copy()
a[2][1] = 10
print(a, b)
b = copy.deepcopy(a)
a[2][1] = 12
print(a, b)
# if a list contains changeable items like other lists, you need to use
# deepcopy(some_list) from copy package: copy.deepcopy(some_list)

a = [7, 2, 9]
b = [7, 2]
print(a == b)
print(a < b) # this only works when all items on each position of each list is
             # comparable to each other

cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith("x"):
        print("Fuck.")
        break
    else:
        print(cheese)
else:
    print("All good.")

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "eat", fruit, "enjoy", dessert)
# zip() stops iterating when the shortest iterable ends

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(list(zip(english, french)))
print(dict(zip(english, french)))
# zip can create such lists from iterables

# списковые включения:
# [выражение for элемент in итерабельный объект]
number_list = [number - 1 for number in range(1,6)]
print(number_list)
number_list = [number for number in range(1, 6) if number % 2 == 1]
print(number_list)

cells = [(row, col) for row in range(1, 4) for col in range(1, 5)]
print(cells)


