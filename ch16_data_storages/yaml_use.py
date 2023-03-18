import yaml

with open("heisenberg.yaml", "r") as fin:
    text = fin.read()

data = yaml.load(text, Loader=yaml.Loader) # use safe_load() for untrusted sources
print(data["dates"])
print(data["dates"]["birth"].strftime("%d.%m.%Y"))
print(data["details"])

