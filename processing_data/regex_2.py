# Go to regex.md for more info
import re
from string import printable

print(re.findall("\d", printable))
print(re.findall("\w", printable))
print(re.findall("\s", printable))

x = "abc" + "-/*" + "\u00ea" + "\u0115"
print(re.findall("\w", x))

