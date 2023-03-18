def game(lst: list[int]) -> None:
    while True:
        value = input("Position [q to quit]? ")
        if value == "q":
            break
        try:
            position = int(value)
            print(lst[position])
        except IndexError:
            print("Bad index:", position)
        except Exception as other:
            print("Unexpected exception raised:", other)

lst = [1, 2, 3]
game(lst)

class UppercaseException(Exception):
    pass

words = ["hello", "bye", "gl", "WTF"]
for word in words:
    if word.isupper():
        raise UppercaseException(word)

