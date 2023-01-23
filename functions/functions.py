def do_nothing():
    pass


def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == "green":
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."

print(commentary("red"), commentary("green"), commentary("no fucking color"))
if do_nothing() is None:
    print("It's nothing")

def menu(wine, entree, dessert="pudding"):
    return {"wine": wine, "entree": entree, "dessert": dessert}
# note: default values for arguments are calculated when the function is defined, not when called. be careful with
# mutable types of data

print(menu("bordeaux", entree="beef", dessert="bagel"))
# positional arguments must go first
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))

def buggy(arg, result=[]):
    result.append(arg)
    print(result)
buggy("a")
buggy("b")
# haha look at this... never put mutable types of data as default elements for a function
# fix:
def buggy(arg):
    result = []
    result.append(arg)
    print(result)
buggy("a")
buggy("b")

def print_args(*args):
    print("Positional arguments tuple: ", args)
print_args()
print_args(3, 2, 1, 'wait!', 'uh...')

def print_more(required1, required2, *args):
    print("Need this one:", required1)
    print("This one too:", required2)
    print("All the rest:", args)
print_more("Tshirt", "pants", "trainers, water, money")

def print_kwargs(**kwargs):
    print("Keyword arguments:", kwargs)
print_kwargs(wine="merlot", entree="mutton", dessert="macaroon")
# * and ** can only be used when calling or defining a function

def print_data(data, *, start, end):
    print(data[start:end])
print_data((0, 1, 2, 3), start=0, end=2)
# start and end args can only be passed as kwargs

def print_if_true(thing, check):
    """
    Prints the first argument if a second argument is true.
    The operation is:
    1. Check whether the *second* argument is true.
    2. If it is, print the *first* argument.
    """
    # this is how documentation to functions done
    if check:
        print(thing)

help(print_if_true) #  doc is also accessible at function.__doc__

def knights(saying):
    def inner(quote):
        return "We are the knights who say: {}".format(quote)
    return inner(saying)
print(knights("Fuck you!"))

# Python closures:
def knights2(saying):
    def inner2():
        return "We are the knights who say: {}".format(saying)
    return inner2
a = knights2("Duck!")
b = knights2("Fuck you!")
print(a, a())
print(b, b())

# lambdas:
def edit_story(words, func):
    for word in words:
        print(func(word))
edit_story(["bruh", "fuck", "wtf"], lambda word: word.capitalize() + "!")

# generators:
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step
for i in my_range(1, 5):
    print(i)

genobj = (pair for pair in zip(("a", "b"), ("1", "2")))
for thing in genobj:
    print(thing)

