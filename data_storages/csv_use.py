import csv

villains = [
        ['Doctor', 'No'],
        ['Rosa', 'Klebb'],
        ['Mister', 'Big'],
        ['Auric', 'Goldfinger'],
        ['Ernst', 'Blofeld'],
        ]
# Writing
with open("villains.csv", "wt") as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)

# Reading
with open("villains.csv", "rt") as fin:
    csvin = csv.reader(fin)
    villains = [row for row in csvin]

from pprint import pprint
pprint(villains)

# Reading as dict
with open("villains.csv", "rt") as fin:
    csvin = csv.DictReader(fin, fieldnames=["first", "last"])
    villains = [row for row in csvin]

pprint(villains)

# Writing headers + data with DictWriter
villains = [
    {'first': 'Doctor', 'last': 'No'},
    {'first': 'Rosa', 'last': 'Klebb'},
    {'first': 'Mister', 'last': 'Big'},
    {'first': 'Auric', 'last': 'Goldfinger'},
    {'first': 'Ernst', 'last': 'Blofeld'},
    ]
with open("villains.csv", "w") as fout:
    csvout = csv.DictWriter(fout, ["first", "last"])
    csvout.writeheader()
    csvout.writerows(villains)

# Reading data as dict with DictReader
with open("villains.csv", "r") as fin:
    csvin = csv.DictReader(fin)
    villains = [row for row in csvin]
print(villains)

