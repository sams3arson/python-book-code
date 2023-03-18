# Module is just a file that contains Python code.
# To refer module's code, we refer it with `import [module_name]`
# All code and variables from module become available to our program

# important: for python version <= 3.3, you need to create empty __init__.py file inside a folder for Python to
# consider it a package
from sources import fast, advice

print("Let's go to", fast.pick())
print("Should we take out?", advice.give())

# sys.path is a list of places where Python interpreter looks for modules and packages
import sys
for place in sys.path:
    print(place)

# you can add more paths where Python will look for modules and packages:
sys.path.insert(0, "/my/modules")

# you can use relative imports as well
# . and .. are used for current and parent dirs, like in Unix
# use it as import .[.
# ..[package_name] - access [package_name] package in current dir

# when you import a module or a package in your program, what actually happens is a copy of that module/package is
# being created for your program. so when you do any changes with that copy, it doesn't affect the package/module itself
# for any imported module/package there is only one copy of it for a program
