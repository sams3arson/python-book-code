periodic_table = {"Hydrogen": 1, "Helium": 2}
print(periodic_table)

carbon = periodic_table.setdefault("Carbon", 12)
print(carbon)
print(periodic_table)

helium = periodic_table.setdefault("Helium", 947)
print(helium)
print(periodic_table)
# dict.setdefault(key, new_value): if [key] is in dict, will return the value from dict; if not, will return [
# new_value], add [key] to dict and assign [new_value] to it

from collections import defaultdict
periodic_table = defaultdict(int)

# collections.defaultdict(function): if you ask for a key that is not in dict, it returns the value of [function]
# function, and assign that value to that key in defaultdict

periodic_table["Hydrogen"] = 1
print(periodic_table)
print(periodic_table["Lead"])
print(periodic_table)
