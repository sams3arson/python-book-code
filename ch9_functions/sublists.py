def flatten(input_list: list):
    print(f"{input_list=}")
    for item in input_list:
        if isinstance(item, list):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item

input_l = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]
print(list(flatten(input_l)))

# yield from - an expression that can yield values the same way from an\
# iterator (iterable), from generator as well
# new version with yield from:


def flatten(input_list: list):
    print(f"{input_list=}")
    for item in input_list:
        if isinstance(item, list):
                yield from flatten(item)
        else:
            yield item
print(list(flatten(input_l)))

