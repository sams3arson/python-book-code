from typing import Generator

# 1
def good() -> list[str]:
    return ["Harry", "Ron", "Hermione"]

# 2
def get_odds() -> Generator[int, None, None]:
    for number in range(10):
        if number % 2 == 1:
            yield number
print(list(get_odds()))

# 3
def test(func):
    def inner(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return inner

@test
def sum_ab(a, b):
    return a + b
print(sum_ab(5, 10))

# 4
class OopsException(Exception):
    pass

try:
    raise OopsException("oops, huh.")
except OopsException:
    print("Caught an oops")


