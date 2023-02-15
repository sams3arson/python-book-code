# Go to regex.md for more info
import re
from string import printable

print(re.findall("\d", printable))
print(re.findall("\w", printable))
print(re.findall("\s", printable))

x = "abc" + "-/*" + "\u00ea" + "\u0115"
print(re.findall("\w", x))


source = """I wish I may, I wish I might
Have a dish of fish tonight."""

print(re.findall("wish", source))
print(re.findall("wish|fish", source))

print(re.findall("^wish", source))
print(re.findall("^I wish", source))
print(re.findall("fish tonight.$", source))

print(re.findall("[wf]ish", source))
print(re.findall("[wsh]+", source))

print(re.findall("I (?=wish)", source))
print(re.findall("(?<=I) wish", source))

# sometimes regexes will mess up with python's escape seqs, use r"" to avoid it:
print(re.findall(r"\bfish", source))

# to save specific matches and access them later at [result].groups(), you
# can enclose template in brackets:
m = re.search(r"(. dish\b).*(\bfish)", source)
print(m.group(), m.groups())

# or, to access in .groups() by name, add '?P<NAME>' after '(':
m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m.group())
print(m.groups())
print(m.group("DISH"))
print(m.group("FISH"))

