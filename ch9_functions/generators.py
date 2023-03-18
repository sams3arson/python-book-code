# to get better understanding of how generators work:
from typing import Generator

def square(lst: list[int]) -> Generator[int, None, None]:
    print("called square with", lst)
    for item in lst:
        print("square yielding", item ** 2)
        yield item ** 2

def out(lst: list[int]) -> Generator[int, None, None]:
    print("called out with", lst)
    yield from square(lst)

lst = [1, 2, 3, 4, 5]
for i in out(lst):
    print("printing i:", i)

