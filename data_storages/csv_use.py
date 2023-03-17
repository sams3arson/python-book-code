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

