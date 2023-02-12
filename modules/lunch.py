import fast
# you can use aliases to import a module with a specific name:
import fast as f
from fast import pick as who_cares

place = f.pick()
place = who_cares()
print("Let's go to", place)
