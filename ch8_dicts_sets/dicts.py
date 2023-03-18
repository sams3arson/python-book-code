empty_dict = {}
empty_dict = dict()

bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
}

acme_customer = {"first": "Wile", "middle": "E", "last": "Coyote"}
acme_customer = dict(first="Wile", middle="E", last="Coyote")
# different ways to create the same dict

lol = [ ["a", "b"], ["c", "d"], ["e", "f"] ]
lot = [ ("a", "b"), ("c", "d"), ("e", "f") ]
print(dict(lol))
print(dict(lot))
# dicts can be created from iterables that consist of 2-length iterables
los = ( "ab", "cd", "ef" )
print(dict(los))

some_pythons = {
    "Graham": "Chapman",
    "John": "Cleese",
    "Eric": "Idle",
    "Terry": "Gilliam",
    "Michael": "Palin",
    "Terry": "Jones",
}
# if the key is not in the dict, a KeyError exception will be raised
print("Groucho" in some_pythons)

print(some_pythons.get("John"))
print(some_pythons.get("Groucho"))
print(some_pythons.get("Groucho", "Not in dict"))
# two ways to check if key is in dict:
# 1 - with 'in', key in dict = bool value True/False
# 2 - dict.get(key) or dict.get(key, optional_return_value)
# dict.get will return the value if key is in dict, None if key is not in dict
# and optional_return_value if it"s specified and key is not in dict

signals = {"green": "go", "yellow": "go faster", "red": "smile for the camera"}
print(signals.keys(), list(signals.keys()))
# .keys() .values() and .items() do not return python lists but iterators,
# just pass it to list() to make a list from it

print(signals.values())
print(signals.items())
# .items() return items of dict in an iterable that consists of tuple(key, value)

first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
third = {'d': 'donuts'}
print({**first, **third, **second})
# dicts can be unpacked with **
# in this example we use ** to unpack dicts to another dict
# note that these copies are linked to the originals (see deepcopy() usage later)

actors = {"Malek": "Rami", "Slater": "Christian"}
others = {"Chaikin": "Carly", "Doubleday": "Portia"}
actors.update(others)
print(actors)
# dict.update(another_dict) adds key-value pairs from another_dict to dict and
# overwrites old values for keys if such are present

del actors["Doubleday"]

deleted_name = actors.pop("Chaikin")
print(deleted_name)
# dict.pop(key) deletes key-value pair from dict and returns the value
# or raises an exception if key is not in dict
print(actors.pop("Esmail", None)) # not in dict
# if key is not in dict and you passed additional value after key, it will
# return that additional value instead of exception

actors.clear()
print(actors)

actors["Malek"] = "Rami"
print("Malek" in actors, "Rami" in actors, "Slater" in actors)

print(actors)
save_actors = actors
actors["Chaikin"] = "Carly"
print(save_actors)

save_actors = actors.copy()
actors["Slater"] = "Christian"
print(save_actors)
# note: if dict items are changeable, use copy.deepcopy()

people = {"actors": ["Malek", "Slater"], "director": "Sam Esmail"}
import copy
people_copy = copy.deepcopy(people)
people["actors"].append("Chaikin")
print(people)
print(people_copy)

a = {1: 1, 2: 2, 3: 3}
b = {3: 3, 1: 1, 2: 2}
print(a == b)
# for dicts, only == and != works. other operators, like <, >, <=, >= will
# raise an exception
# in dict comparison, order of items doesn't matter

for key in actors:
    print(key)

for value in actors.values():
    print(value)

for item in actors.items():
    print(item)

for surname, name in actors.items():
    print(name, surname)

word = "letters"
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

vowels = 'aeiou'
word = "onomatopoeia"
vowel_counts = {letter: word.count(letter) for letter in set(word) \
        if letter in vowels}
print(vowel_counts)

