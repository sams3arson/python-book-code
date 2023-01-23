animal = "cat"
# variables set in the program without any functions are global variables
# they are accessible by any function, but can't be changed inside the function
# if you don't access that global variable before assigning a value to it inside function, no error will be raised
def print_animal(): # no error
    print("before:", animal)

def print_animal_and_change(): # error
    print("before:", animal)
    animal = "dog"
    print("after:", animal)
try:
    print_animal_and_change()
except UnboundLocalError as e:
    print(e)

def animal_assign(): # no error
    animal = "dog"
    print("no before; after:", animal)
animal_assign()
print(animal)

# global variables can be changed inside functions if u use global keyword:
def animal_rewrite():
    global animal
    print("before:", animal)
    animal = "dog"
    print("after:", animal)
animal_rewrite()
print(animal)

animal = "cat"
def change_local():
    animal = "wombat"
    print("locals:", locals())
change_local()
print("globals:", globals())
