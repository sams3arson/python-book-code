# deque - двусторонняя очередь, которая имеет функции как стека, так и очереди
# полезна, когда нужно добавить или удалить элементы с любого конца последовательности

from collections import deque

def palindrome(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(palindrome("a"))
print(palindrome("racecar"))
print(palindrome("halibut"))
