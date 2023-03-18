import re

# при поиске регулярными выражениями, мы передаем шаблон (pattern) для поиска 
# и строку, в которой нужно искать
source = "Young Frankenstein"

# example:
result = re.match("You", source)
print(result)

# чтобы более сложные проверки, паттерн нужно "скомпилировать" для ускорения:
youpattern = re.compile("You")
result = youpattern.match(source)
print(result)

# re.match - checks if the string starts with pattern
m = re.match("You", source)
if m:
    print(m)

m = re.match("Frank", source)
if m:
    print(m) # prints nothing; m is None

m = re.match(".*Frank", source)
# expl.: '.' stands for any symbol; '*' stands for 0 or more prev elements;
# '.*' results into 0 or more previous symbols
print(m) # 'Young Frank' - matched the pattern


# re.search - finds the pattern anywhere in the string
m = re.search(".*Frank", source)
print(m)


# re.findall - finds all matches to the pattern; returns a list
m = re.findall("n", source)
print(m)
print("Found", len(m), "matches")

m = re.findall("n.", source)
print(m)

m = re.findall("n.?", source) # '?' after '.' means that '.' is optional
print(m)

# re.split - splits the string by pattern
m = re.split("n", source)
print(m)

# re.sub - replaces pattern matches with provided string
m = re.sub("n", "?", source)
print(m)

