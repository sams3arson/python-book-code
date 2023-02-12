from random import choice

places = ["McDonalds", "KFC", "Burger King", "Taco Bell", "Wendys", "Arbys", "Pizza Hut"]


def pick():
    """Return random fast food place"""
    # `import` can be used anywhere, for example, inside this function
    import random
    return random.choice(places)
