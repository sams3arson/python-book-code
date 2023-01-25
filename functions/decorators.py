# decorator - a function that receives a function as an argument and returns another modified function
def document_it(func): # this is a decorator
    def new_function(*args, **kwargs):
        print("Func name:", func.__name__)
        print("Positional args:", args)
        print("Keyword args:", kwargs)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result
    return new_function

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

def add_ints(a, b): # this is the function we will decorate
    return a + b
cooler_add_ints = document_it(add_ints) # manual decoration
cooler_add_ints(3, 5)

@document_it # proper, automatic decoration
def add_ints(a, b):
    return a + b
add_ints(4, 9)

@document_it
@square_it
def add_ints(a, b):
    return a + b
add_ints(8, 10)
